---
tags: [DAM, PSP]
cssclasses: [dam-psp, table-compact-clean]
banner: "![[psp.jpg]]"
banner_y: 0.32
---

# **TEMA 2.** <br>Programación Multihilo


| Anexos     |
| --- |
| [Resumen TEMA 2. Programación Multihilo](Resúmenes/Resumen%20TEMA%202.%20Programación%20Multihilo.md)    |

## 1. Introducción

Un programa puede tener uno o varios flujos de ejecución. En un programa de **flujo único**, las tareas se ejecutan de manera secuencial, una tras otra. En un programa de **flujo múltiple**, las tareas se distribuyen en varios flujos de ejecución, permitiendo que se ejecuten de manera concurrente o simultánea. La **programación multihilo** consiste en desarrollar aplicaciones de flujo múltiple, donde cada flujo es un **hilo** o **thread.**

Un ejemplo común es un navegador web, que puede descargar una imagen, navegar por Internet e iniciar otra descarga simultáneamente. Esto se logra mediante hilos, donde cada tarea se ejecuta en un hilo independiente. Aunque las tareas parecen ejecutarse "a la vez", en realidad se ejecutan concurrentemente, y su paralelismo real depende del sistema operativo y del hardware.

## 2. Conceptos sobre hilos

Un **hilo** es un flujo de control secuencial independiente dentro de un proceso. Cada hilo tiene su propio contador de programa, registros y pila, pero comparte el espacio de memoria con otros hilos del mismo proceso. Un proceso no se ejecuta por sí mismo, sino que lo hacen sus hilos.

### 2.1. **Recursos compartidos por los hilos**

Cada hilo tiene recursos propios, como su identificador, contador de programa, registros y pila. Sin embargo, los hilos de un mismo proceso comparten:

- **Código.** Instrucciones del programa.
- **Datos.** Variables globales.
- **Recursos del sistema.** Ficheros abiertos y señales.

El hecho de que los hilos compartan memoria puede llevar a problemas si un hilo corrompe la memoria, afectando a los demás. Por ello, es crucial utilizar mecanismos de **sincronización** para evitar conflictos.

### 2.2. **Ventajas y uso de hilos**

Los hilos, también llamados **procesos ligeros**, ofrecen varias ventajas sobre los procesos tradicionales:

- **Menor consumo de recursos.** Crear y ejecutar un hilo es más eficiente que hacerlo con un proceso.
- **Conmutación más rápida.** Cambiar entre hilos es más rápido que cambiar entre procesos.
- **Eficiencia en multiprocesadores.** Los hilos pueden ejecutarse en paralelo en sistemas multiprocesador.

Los hilos son ideales para aplicaciones que:

- Manejan entradas de varios dispositivos.
- Realizan múltiples tareas simultáneamente.
- Ejecutan tareas con prioridades variadas.
- Operan en entornos multiprocesador.

Por ejemplo, un servidor web puede usar hilos para atender múltiples peticiones de clientes simultáneamente, mejorando la eficiencia y la capacidad de respuesta.

## 3. Multihilo en Java: Librerías y clases

Java ofrece soporte nativo para la programación multihilo a través de clases e interfaces en el paquete `java.lang` y utilidades avanzadas en `java.util.concurrent`.

### 3.1. **Utilidades de concurrencia del paquete `java.lang`**

En este paquete se encuentran las siguientes clases e interfaces:

| Clase/Interfaz       | Descripción                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| `Thread`             | Clase principal para crear y gestionar hilos.                               |
| `Runnable`           | Interfaz que permite añadir funcionalidad de hilo a una clase.              |
| `ThreadDeath`        | Clase de error para manejar y notificar errores en hilos.                   |
| `ThreadGroup`        | Permite manejar grupos de hilos de manera conjunta.                         |
| `Object`             | Proporciona métodos clave como `wait()`, `notify()` y `notifyAll()`.         |

### 3.2. **Utilidades de concurrencia del paquete `java.util.concurrent`**

Este paquete incluye herramientas avanzadas para desarrollar aplicaciones multihilo complejas:

| | |
|-|-|
| **Clases de sincronización** | `Semaphore`, `CountDownLatch`, `CyclicBarrier`, `Exchanger`. |
| **Interfaces de ejecución** | `Executor`, `ExecutorService`, `Callable`, `Future`. |
| **Colas de hilos** | `BlockingQueue`, `LinkedBlockingQueue`, `ArrayBlockingQueue`, etc. |
| **Variables atómicas** | `AtomicInteger`, `AtomicLong` (en `java.util.concurrent.atomic`). |
| **Alternativas a `synchronized`** | Interfaces como `Lock` y `ReadWriteLock` (en `java.util.concurrent.locks`). |

Estas herramientas facilitan la creación de aplicaciones concurrentes eficientes y robustas, permitiendo un mayor control sobre la sincronización y la gestión de recursos compartidos.

## 4. Creación de hilos

En Java, un hilo se representa mediante una instancia de la clase `java.lang.Thread`. Este objeto se utiliza para iniciar, detener o controlar la ejecución del hilo. Existen dos formas de definir hilos:

1. **Extendiendo la clase `Thread`.**
2. **Implementando la interfaz `Runnable`.**

En ambos casos, es necesario definir el método `run()`, que contiene el código que ejecutará el hilo. La elección entre ambos métodos depende del contexto:

- **Extender `Thread`** es más sencillo, pero no es posible si la clase ya hereda de otra clase (Java no permite herencia múltiple).
- **Implementar `Runnable`** es más flexible y siempre es posible, incluso cuando la clase ya hereda de otra.

### 4.1. **Creación de hilos extendiendo la clase `Thread`**

Para crear un hilo extendiendo `Thread`, se siguen estos pasos:

1. Crear una clase que herede de `Thread`.
2. Redefinir el método `run()` con el código que ejecutará el hilo.
3. Crear un objeto de la nueva clase (el hilo).
4. Iniciar el hilo llamando al método `start()`.

**Ejemplo:**

Imagina que tenemos una clase llamada `Saludo` que extiende la clase `Thread`. Dentro de esta clase, redefinimos el método `run()` para que imprima un mensaje de saludo. Luego, en el método `main`, creamos una instancia de esta clase y la iniciamos con el método `start()`.

```java
public class Saludo extends Thread {
    public void run() {
        System.out.println("¡Saludo desde un hilo extendiendo Thread!");
    }

    public static void main(String args[]) {
        Saludo hilo1 = new Saludo(); // Crear el hilo
        hilo1.start(); // Iniciar el hilo
    }
}
```

### 4.2. **Creación de hilos mediante la interfaz `Runnable`**

Para crear un hilo implementando `Runnable`, se siguen estos pasos:

1. Crear una clase que implemente `Runnable`.
2. Redefinir el método `run()` con el código que ejecutará el hilo.
3. Crear un objeto de la nueva clase.
4. Crear un objeto `Thread` pasando el objeto `Runnable` como argumento.
5. Iniciar el hilo llamando al método `start()`.

**Ejemplo:**

En este caso, tenemos una clase llamada `Saludo` que implementa la interfaz `Runnable`. Dentro de esta clase, redefinimos el método `run()` para que imprima un mensaje de saludo. Luego, en el método `main`, creamos una instancia de esta clase y la pasamos como argumento al constructor de `Thread`. Finalmente, iniciamos el hilo con el método `start()`.

```java
public class Saludo implements Runnable {
    public void run() {
        System.out.println("¡Saludo desde un hilo creado con Runnable!");
    }

    public static void main(String args[]) {
        Saludo miRunnable = new Saludo(); // Crear el objeto Runnable
        Thread hilo1 = new Thread(miRunnable); // Crear el hilo
        hilo1.start(); // Iniciar el hilo
    }
}
```

## 5. Estados de un hilo

El ciclo de vida de un hilo comprende varios estados:

| Estado           | Descripción                                                                 |
|------------------|-----------------------------------------------------------------------------|
| **Nuevo (New)**  | El hilo ha sido creado pero no está listo para ejecutarse.                  |
| **Ejecutable (Runnable)** | El hilo está listo para ejecutarse, pero puede no estar ejecutándose activamente. |
| **No Ejecutable (Not Runnable)** | El hilo está detenido temporalmente (por ejemplo, por `sleep()`, `wait()` o bloqueos de E/S). |
| **Muerto (Terminated)** | El hilo ha finalizado su ejecución, normalmente al terminar el método `run()`. |

El método `getState()` de la clase `Thread` permite obtener el estado actual de un hilo.

### 5.1. **Iniciar un hilo**

Para iniciar un hilo, se llama al método `start()`, que realiza las siguientes acciones:

1. Crea los recursos necesarios para ejecutar el hilo.
2. Llama al método `run()` y lo ejecuta como un subproceso independiente.

**Consideraciones importantes:**

- Llamar directamente a `run()` no inicia un nuevo hilo, sino que ejecuta el código en el hilo actual.
- No se puede llamar a `start()` más de una vez en un mismo hilo, ya que lanzaría una excepción `IllegalThreadStateException`.
- El orden de ejecución de los hilos es no determinístico.

**Ejemplo de ejecución no determinística:**

Imagina que tenemos tres hilos: `hilo1`, `hilo2` y `hilo3`. Cada hilo imprime su nombre varias veces. Al iniciar los hilos, no sabemos en qué orden se ejecutarán, ya que depende del planificador del sistema operativo.

```java
public class Main {
    public static void main(String[] args) {
        Thread hilo1 = new Hilo_Thread("Isabel");
        Thread hilo2 = new Hilo_Thread();
        Thread hilo3 = new Thread(new Hilo_Runnable());

        hilo1.start();
        hilo2.start();
        hilo3.start();
    }
}

class Hilo_Thread extends Thread {
    String nombre;

    public Hilo_Thread(String nb) {
        nombre = nb;
    }

    public Hilo_Thread() {
        nombre = "Hilo_derviaThread";
    }

    @Override
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println(nombre);
        }
    }
}

class Hilo_Runnable implements Runnable {
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println("  Hilo_Runnable");
        }
    }
}
```

### 5.2. **Detener temporalmente un hilo**

Un hilo puede pasar al estado **No Ejecutable** por las siguientes razones:

- **Dormido.** Se llama al método `sleep()` para detener el hilo durante un tiempo específico.
- **Esperando.** Se llama al método `wait()`, y el hilo permanece detenido hasta que otro hilo llame a `notify()` o `notifyAll()`.
- **Bloqueado.** El hilo está esperando un recurso, como una operación de E/S.

| Métodos clave | |
|-|-|
| `sleep(long millis)` | Detiene el hilo durante el tiempo especificado en milisegundos. |
| `wait()` | Detiene el hilo hasta que se llame a `notify()` o `notifyAll()`. |
| `notify()` y `notifyAll()` | Reanudan hilos en espera. |

> [!warning] Nota
> Los métodos `suspend()` y `resume()` están en desuso y no deben utilizarse, ya que no son seguros. 

### 5.3. **Finalizar un hilo**

Un hilo finaliza naturalmente cuando termina de ejecutar su método `run()`, pasando al estado **Muerto (Terminated).** Una vez que un hilo ha muerto, no puede reiniciarse con `start()`. Si se desea realizar la misma tarea nuevamente, es necesario crear un nuevo hilo.

#### Verificación del estado de un hilo

Para comprobar si un hilo está vivo o no, se utiliza el método `isAlive()` de la clase `Thread`. Este método devuelve:

- **`true`.** El hilo está vivo (en estado **Ejecutable** o **No Ejecutable**).
- **`false`.** El hilo está en estado **Nuevo** o **Muerto.**

**Nota.** El método `stop()` de la clase `Thread` está en desuso y no debe utilizarse, ya que no es seguro.

#### Ejemplo de uso de `isAlive()` y `getState()`

Imagina que tenemos un hilo llamado `Hilo_Auxiliar` que cuenta desde 10 hasta 1. En el método `main`, verificamos el estado del hilo antes y después de iniciarlo, y luego esperamos a que termine usando `join()`.

```java
package PaquetePrincipal;

public class Main {
    public static void main(String[] args) {
        Hilo_Auxiliar hilo1 = new Hilo_Auxiliar();
        System.out.println("Hilo Auxiliar Nuevo: Estado=" + hilo1.getState()
                + ", ¿Vivo? isAlive()=" + hilo1.isAlive());

        hilo1.start();
        System.out.println("Hilo Auxiliar Iniciado: Estado="
                + hilo1.getState()
                + ", ¿Vivo? isAlive()=" + hilo1.isAlive() + "\n");

        try {
            hilo1.join(); // Espera a que el hilo muera
        } catch (InterruptedException e) {
            System.out.println(e);
        }
        System.out.println("\n Hilo Auxiliar Muerto: Estado="
                + hilo1.getState()
                + ", ¿Vivo? isAlive()=" + hilo1.isAlive());
    }
}

class Hilo_Auxiliar extends Thread {
    @Override
    public void run() {
        for (int i = 10; i >= 1; i--)
            System.out.print(i + ",");
    }
}
```

#### Ejemplo: Dormir un hilo con `sleep()`

El método `sleep()` de la clase `Thread` permite detener temporalmente un hilo durante un tiempo específico. Este método es útil para controlar la ejecución de hilos, especialmente cuando se necesita esperar a que otro hilo complete una tarea.

#### Funcionamiento de `sleep()`

- **`sleep(long milisegundos)`.** Detiene el hilo durante el tiempo especificado en milisegundos.
- **`sleep(long milisegundos, int nanosegundos)`.** Detiene el hilo durante el tiempo especificado en milisegundos y nanosegundos.

> [!warning] Nota
> Cualquier llamada a `sleep()` puede lanzar una excepción `InterruptedException`, que debe manejarse con un bloque `try-catch`. 

#### Ejemplo de uso de `sleep()`

Imagina que tenemos un hilo que cuenta del 1 al 5, pero entre cada número, el hilo se duerme durante 1 segundo. Esto permite que el hilo no consuma todos los recursos de la CPU y dé tiempo a otros hilos para ejecutarse.

```java
public class EjemploSleep {
    public static void main(String[] args) {
        Thread hilo = new Thread(() -> {
            for (int i = 1; i <= 5; i++) {
                System.out.println("Contador: " + i);
                try {
                    Thread.sleep(1000); // Dormir el hilo durante 1 segundo
                } catch (InterruptedException e) {
                    System.out.println("Hilo interrumpido");
                }
            }
        });
        hilo.start();
    }
}
```

## 6. Gestión y planificación de hilos

La ejecución de hilos puede realizarse mediante:

- **Paralelismo.** En sistemas con múltiples CPU, cada CPU ejecuta un hilo diferente.
- **Pseudoparalelismo.** En sistemas con una sola CPU, la CPU alterna la ejecución de múltiples hilos.

### 6.1. **Prioridad de hilos**

En Java, cada hilo tiene una prioridad representada por un valor entero entre 1 y 10. Cuanto mayor es el valor, mayor es la prioridad del hilo. Las constantes definidas en la clase `Thread` son:

| Constantes | Prioridad |  |
| - | - | - |
| `MAX_PRIORITY` | **10** | Prioridad máxima. |
| `MIN_PRIORITY` | **1** | Prioridad mínima. |
| `NORM_PRIORITY` | **5** | Prioridad normal (valor por defecto). |

Los métodos `getPriority()` y `setPriority()` permiten obtener y modificar la prioridad de un hilo.

#### Ejemplo de uso de prioridades

Imagina que tenemos varios hilos con diferentes prioridades: algunos con prioridad mínima, otros con prioridad normal y otros con prioridad máxima. Cada hilo realiza una tarea repetitiva y, al final, imprime un mensaje indicando que ha terminado.

```java
package PaquetePrincipal;

public class Programa {
    public static void main(String[] args) {
        int contador = 5;
        Thread[] hiloMIN = new Thread[contador];
        Thread[] hiloNORM = new Thread[contador];
        Thread[] hiloMAX = new Thread[contador];

        for (int i = 0; i < contador; i++) {
            hiloMIN[i] = new Hilo(Thread.MIN_PRIORITY);
            hiloNORM[i] = new Hilo();
            hiloMAX[i] = new Hilo(Thread.MAX_PRIORITY);
        }

        System.out.println("Hilos en proceso, espera...\n");

        for (int i = 0; i < contador; i++) {
            hiloMIN[i].start();
            hiloNORM[i].start();
            hiloMAX[i].start();
        }
    }
}

class Hilo extends Thread {
    public Hilo() {} // Constructor por defecto

    public Hilo(int prioridad) {
        this.setPriority(prioridad);
    }

    @Override
    public void run() {
        String strCadena = "";
        for (int i = 0; i < 20000; ++i) {
            strCadena += "A";
            yield(); // Sugiere al planificador que seleccione otro hilo
        }
        System.out.println("Hilo de prioridad " + this.getPriority() + " termina ahora");
    }
}
```

### 6.2. **Hilos egoístas y programación expulsora**

En sistemas operativos sin **time-slicing**, un hilo puede monopolizar la CPU hasta que finalice, impidiendo que otros hilos se ejecuten. Este comportamiento se conoce como **hilo egoísta.**

Para evitar esto, Java proporciona el método `yield()`, que sugiere al planificador que ceda el control a otros hilos de la misma prioridad. Sin embargo, el comportamiento de `yield()` no está garantizado.

#### Ejemplo de uso de `yield()`

Imagina que tenemos un hilo llamado `HiloEgoista` que imprime números del 1 al 100. En cada iteración, el hilo cede el control a otros hilos usando `yield()`.

```java
public class HiloEgoista extends Thread {
    private String color;

    public HiloEgoista(String color) {
        this.color = color;
    }

    @Override
    public void run() {
        for (int i = 1; i <= 100; i++) {
            System.out.println(color + i);
            yield(); // Cede el control a otros hilos
        }
    }
}
```

## 7. Sincronización y comunicación de hilos

En programas multihilo, es común que varios hilos necesiten compartir recursos o información. Esto puede llevar a conflictos si no se gestiona adecuadamente. Para evitar problemas como condiciones de carrera o bloqueos, es necesario utilizar mecanismos de **sincronización** y **comunicación** entre hilos.

### 7.1. **Información compartida entre hilos**

Cuando varios hilos acceden a un mismo recurso, como una variable o un archivo, se pueden producir **condiciones de carrera.** Esto ocurre cuando dos o más hilos modifican un recurso compartido de manera no controlada, lo que puede resultar en valores inconsistentes o inesperados.

#### Ejemplo: Problema de los jardines

En este ejemplo, varios hilos acceden a una variable compartida `cuenta`, que representa el número de personas en un jardín. Algunos hilos incrementan el valor de `cuenta` (entran al jardín), mientras que otros lo decrementan (salen del jardín). Sin sincronización, el valor de `cuenta` puede volverse inconsistente.

```java
package problemajardines;

public class Main {
    public static void main(String[] args) {
        RecursoJardin jardin = new RecursoJardin();

        for (int i = 1; i <= 10; i++) {
            (new Entra_Jardin("Entra" + i, jardin)).start();
        }

        for (int i = 1; i <= 15; i++) {
            (new Sale_Jardin("Sale" + i, jardin)).start();
        }
    }
}

class Entra_Jardin extends Thread {
    private RecursoJardin jardin;

    public Entra_Jardin(String nombre, RecursoJardin j) {
        this.setName(nombre);
        this.jardin = j;
    }

    @Override
    public void run() {
        jardin.incrementaCuenta();
    }
}

class Sale_Jardin extends Thread {
    private RecursoJardin jardin;

    public Sale_Jardin(String nombre, RecursoJardin j) {
        this.setName(nombre);
        this.jardin = j;
    }

    @Override
    public void run() {
        jardin.decrementaCuenta();
    }
}

class RecursoJardin {
    private int cuenta;

    public RecursoJardin() {
        cuenta = 100;
    }

    public void incrementaCuenta() {
        System.out.println("hilo " + Thread.currentThread().getName() + "----- Entra en Jardín");
        cuenta++;
        System.out.println(cuenta + " en jardín");
    }

    public void decrementaCuenta() {
        System.out.println("hilo " + Thread.currentThread().getName() + "----- Sale de Jardín");
        cuenta--;
        System.out.println(cuenta + " en jardín");
    }
}
```

#### Solución: Sincronización con `synchronized`

Para evitar condiciones de carrera, se deben proteger las **secciones críticas** del código, es decir, las partes donde se accede o modifica el recurso compartido. En Java, esto se logra utilizando la palabra clave `synchronized`.

```java
package jardinessincronizado;

public class RecursoJardin {
    private int cuenta;

    public RecursoJardin() {
        cuenta = 100;
    }

    public synchronized void incrementaCuenta() {
        System.out.println("hilo " + Thread.currentThread().getName() + "----- Entra en Jardín");
        cuenta++;
        System.out.println(cuenta + " en jardín");
    }

    public synchronized void decrementaCuenta() {
        System.out.println("hilo " + Thread.currentThread().getName() + "----- Sale de Jardín");
        cuenta--;
        System.out.println(cuenta + " en jardín");
    }
}
```

Al marcar los métodos `incrementaCuenta()` y `decrementaCuenta()` como `synchronized`, solo un hilo puede ejecutar estos métodos a la vez, evitando así condiciones de carrera.

### 7.2. **Monitores y métodos `synchronized`**

Un **monitor** en Java es un mecanismo que permite controlar el acceso a un recurso compartido mediante la palabra clave `synchronized`. Cuando un método o bloque de código se marca como `synchronized`, se asocia con un **mutex** (exclusión mutua), que garantiza que solo un hilo puede ejecutar ese código a la vez.

#### Funcionamiento de un monitor

- **Mutex libre.** Si el mutex está libre, el hilo lo toma y ejecuta el código `synchronized`.
- **Mutex ocupado.** Si otro hilo tiene el mutex, el hilo actual se bloquea y espera hasta que el mutex se libere.

#### Ejemplo: Sincronización de acceso a un servidor

En este ejemplo, varios hilos simulan el acceso a un servidor web. El método `incrementaCuenta()` está sincronizado para evitar que varios hilos modifiquen la variable `cuenta` al mismo tiempo.

```java
package sincronizametodo;

public class ServidorWeb {
    private int cuenta;

    public ServidorWeb() {
        cuenta = 0;
    }

    public synchronized void incrementaCuenta() {
        System.out.println("hilo " + Thread.currentThread().getName() + "----- Entra en Servidor");
        cuenta++;
        System.out.println(cuenta + " accesos");
    }
}

class Hilo_Terminal extends Thread {
    private ServidorWeb servidor;

    public Hilo_Terminal(ServidorWeb s) {
        this.servidor = s;
    }

    @Override
    public void run() {
        for (int i = 1; i <= 10; i++) {
            servidor.incrementaCuenta();
            yield();
        }
    }
}

public class Main {
    public static void main(String[] args) {
        ServidorWeb servidor = new ServidorWeb();
        Hilo_Terminal hterminal1 = new Hilo_Terminal(servidor);
        Hilo_Terminal hterminal2 = new Hilo_Terminal(servidor);
        Hilo_Terminal hterminal3 = new Hilo_Terminal(servidor);
        Hilo_Terminal hterminal4 = new Hilo_Terminal(servidor);

        hterminal1.start();
        hterminal2.start();
        hterminal3.start();
        hterminal4.start();
    }
}
```

En este caso, el método `incrementaCuenta()` está sincronizado, lo que garantiza que solo un hilo puede acceder a él a la vez, evitando condiciones de carrera.

### 7.3. **Monitores: Segmentos de código `synchronized`**

En algunos casos, no es posible o no es conveniente sincronizar un método completo. Por ejemplo, si no tenemos acceso al código fuente del método o si solo necesitamos sincronizar una parte específica del código. En estas situaciones, podemos utilizar **segmentos de código sincronizados** con la palabra clave `synchronized`.

#### Funcionamiento de los segmentos `synchronized`

Un segmento de código `synchronized` permite sincronizar el acceso a un objeto específico. El bloque de código dentro del segmento `synchronized` solo puede ser ejecutado por un hilo a la vez, garantizando la exclusión mutua.

##### Sintaxis

```java
synchronized (objeto) {
    // Código que necesita ser sincronizado
}
```

- **`objeto`.** Es el objeto cuyo monitor se desea adquirir. Solo un hilo puede tener el monitor de este objeto a la vez.
- **Código sincronizado.** El bloque de código dentro del segmento `synchronized` solo puede ser ejecutado por un hilo a la vez.

#### Ejemplo: Sincronización de un segmento de código

En el ejemplo del "Problema de los jardines", en lugar de sincronizar los métodos `incrementaCuenta()` y `decrementaCuenta()`, podemos sincronizar el acceso al objeto `jardin` dentro de los métodos `run()` de los hilos.

```java
package sincronizasegmentojardines;

public class Main {
    public static void main(String[] args) {
        RecursoJardin jardin = new RecursoJardin();

        for (int i = 1; i <= 10; i++) {
            (new Entra_Jardin("Entra" + i, jardin)).start();
        }

        for (int i = 1; i <= 15; i++) {
            (new Sale_Jardin("Sale" + i, jardin)).start();
        }
    }
}

class Entra_Jardin extends Thread {
    private RecursoJardin jardin;

    public Entra_Jardin(String nombre, RecursoJardin j) {
        this.setName(nombre);
        this.jardin = j;
    }

    @Override
    public void run() {
        synchronized (jardin) { // Segmento sincronizado
            jardin.incrementaCuenta();
        }
    }
}

class Sale_Jardin extends Thread {
    private RecursoJardin jardin;

    public Sale_Jardin(String nombre, RecursoJardin j) {
        this.setName(nombre);
        this.jardin = j;
    }

    @Override
    public void run() {
        synchronized (jardin) { // Segmento sincronizado
            jardin.decrementaCuenta();
        }
    }
}

class RecursoJardin {
    private int cuenta;

    public RecursoJardin() {
        cuenta = 100;
    }

    public void incrementaCuenta() {
        System.out.println("hilo " + Thread.currentThread().getName() + "----- Entra en Jardín");
        cuenta++;
        System.out.println(cuenta + " en jardín");
    }

    public void decrementaCuenta() {
        System.out.println("hilo " + Thread.currentThread().getName() + "----- Sale de Jardín");
        cuenta--;
        System.out.println(cuenta + " en jardín");
    }
}
```

#### Observaciones

1. **Exclusión mutua.** Solo un hilo puede ejecutar el segmento `synchronized` a la vez, lo que garantiza que no haya condiciones de carrera.
2. **Flexibilidad.** Este enfoque es útil cuando no se puede modificar el código fuente de los métodos que se desean sincronizar.
3. **Rendimiento.** Sincronizar segmentos de código en lugar de métodos completos puede mejorar el rendimiento, ya que se reduce el tiempo de bloqueo.
4. **Legibilidad.** Aunque es más flexible, sincronizar métodos completos suele ser más legible y fácil de mantener.

#### Consideraciones adicionales

- **Interbloqueo (Deadlock).** Al sincronizar múltiples objetos, es posible que se produzca un interbloqueo si dos o más hilos esperan indefinidamente por los recursos que cada uno tiene bloqueados. Este problema se abordará en detalle más adelante.
- **Sincronización en clases predefinidas.** Muchas clases de Java, como las de AWT y Swing, ya tienen métodos sincronizados. Por ejemplo, el método `addMouseListener()` de la clase `Component` está sincronizado.

```java
public synchronized void addMouseListener(MouseListener l) {
    // Código sincronizado
}
```

### 7.4. **Comunicación entre hilos con métodos de `java.lang.Object`**

La comunicación entre hilos es esencial para coordinar su ejecución y evitar conflictos al acceder a recursos compartidos. Java proporciona los métodos `wait()`, `notify()`, y `notifyAll()` de la clase `java.lang.Object` para facilitar esta comunicación.

#### Métodos de comunicación entre hilos

##### `wait()`
- **Descripción.** Detiene el hilo que lo invoca y lo pone en estado **No Ejecutable** hasta que otro hilo lo notifique.
- **Condiciones.**
  - Debe invocarse dentro de un bloque `synchronized`.
  - El hilo debe tener el **mutex** del objeto sobre el que se invoca `wait()`.
  - Libera el mutex del objeto mientras el hilo está en espera.
- **Excepción.** Puede lanzar una `InterruptedException`.

##### `notify()`
- **Descripción.** Notifica a uno de los hilos que están en espera (invocaron `wait()` sobre el mismo objeto) para que continúe su ejecución.
- **Comportamiento.**
  - Solo reactiva un hilo de la cola de espera.
  - El hilo reactivado intentará obtener el mutex del objeto para continuar su ejecución.

##### `notifyAll()`
- **Descripción.** Notifica a **todos** los hilos en espera para que continúen su ejecución.
- **Comportamiento.**
  - Todos los hilos reactivados competirán por el mutex del objeto.
  - Solo uno podrá obtener el mutex y continuar su ejecución.

#### Ejemplo: Problema del Productor-Consumidor

Este problema clásico ilustra la necesidad de sincronización y comunicación entre hilos. Un hilo **productor** genera datos y los coloca en un búfer, mientras que un hilo **consumidor** los retira y procesa. Ambos hilos deben coordinarse para evitar que el productor intente colocar datos en un búfer lleno o que el consumidor intente retirar datos de un búfer vacío.

```java
public class Hilo_Pintor extends Thread {
    private AlmacenCuadros almacen;

    public Hilo_Pintor(AlmacenCuadros a) {
        almacen = a;
    }

    public void run() {
        for (int i = 1; i < 30; i++) {
	        // Pinta y guarda cuadros en el almacén
            almacen.guardar();
        }
    }
}

public class Hilo_Vendedor extends Thread {
    private AlmacenCuadros almacen;

    public Hilo_Vendedor(AlmacenCuadros a) {
        almacen = a;
    }

    public void run() {
        for (int i = 1; i < 30; i++) {
	        // Vende cuadros del almacén
            almacen.sacar();
        }
    }
}

public class AlmacenCuadros {
	// Contador de cuadros en el almacén
    private int cuadros = 0;

    public synchronized void guardar() {
        try {
	        // Si hay cuadros, espera
            while (cuadros > 0) {
                this.wait();
            }
            // Guarda un cuadro
            cuadros++;
            System.out.println("Pintado cuadro: " + cuadros);
            // Notifica al consumidor
            this.notify();
        } catch (InterruptedException e) {}
    }

    public synchronized void sacar() {
        try {
	        // Si no hay cuadros, espera
            while (cuadros == 0) {
                this.wait();
            }
            // Vende un cuadro
            cuadros--;
            System.out.println("Vendido cuadro: " + cuadros);
            // Notifica al productor
            this.notify();
        } catch (InterruptedException e) {}
    }
}

public class Main {
    public static void main(String[] args) {
        AlmacenCuadros almacen = new AlmacenCuadros();
        Hilo_Pintor pintor = new Hilo_Pintor(almacen);
        Hilo_Vendedor vendedor = new Hilo_Vendedor(almacen);

        pintor.start();
        vendedor.start();
    }
}
```

#### Ejemplo: Problema de los Lectores-Escritores

Este problema modela el acceso simultáneo de varios hilos a un recurso compartido, como una base de datos. Los **lectores** pueden acceder al recurso simultáneamente, pero los **escritores** requieren acceso exclusivo.

```java
public class Semaforo {
    public final static int LIBRE = 0;
    public final static int CON_LECTORES = 1;
    public final static int CON_ESCRITOR = 2;
    private int estado = LIBRE;
    private int tLectores = 0;

    public synchronized void accesoLeer() {
        String nombre = Thread.currentThread().getName();
        if (estado == LIBRE) {
            estado = CON_LECTORES;
        } else if (estado != CON_LECTORES) {
            while (estado == CON_ESCRITOR) {
                try {
                    wait();
                } catch (InterruptedException e) {}
            }
            estado = CON_LECTORES;
        }
        tLectores++;
        System.out.println("BD:" + estado + " " + tLectores + "L " + nombre + " Leyendo.....");
    }

    public synchronized void accesoEscribir() {
        String nombre = Thread.currentThread().getName();
        if (estado == LIBRE) {
            estado = CON_ESCRITOR;
        } else {
            while (estado != LIBRE) {
                try {
                    wait();
                } catch (InterruptedException e) {}
            }
            estado = CON_ESCRITOR;
        }
        System.out.println("BD:" + estado + " " + tLectores + "L " + nombre + " Escribiendo..");
    }

    public synchronized void lecturaFinalizada() {
        tLectores--;
        if (tLectores == 0) {
            estado = LIBRE;
            notify();
        }
    }

    public synchronized void escrituraFinalizada() {
        estado = LIBRE;
        notify();
    }
}

public class HiloLector extends Thread {
    private Semaforo semaforo;

    public HiloLector(String nombre, Semaforo s) {
        this.setName(nombre);
        this.semaforo = s;
    }

    @Override
    public void run() {
        semaforo.accesoLeer();
        try {
            sleep((int) (Math.random() * 50));
        } catch (InterruptedException e) {}
        semaforo.lecturaFinalizada();
    }
}

public class HiloEscritor extends Thread {
    private Semaforo semaforo;

    public HiloEscritor(String nombre, Semaforo s) {
        this.setName(nombre);
        this.semaforo = s;
    }

    @Override
    public void run() {
        semaforo.accesoEscribir();
        try {
            sleep((int) (Math.random() * 50));
        } catch (InterruptedException e) {}
        semaforo.escrituraFinalizada();
    }
}

public class Main {
    public static void main(String[] args) {
        Semaforo smfro = new Semaforo();
        for (int i = 1; i <= 5; i++) {
            new HiloLector("Lector" + i, smfro).start();
        }
        for (int i = 1; i <= 2; i++) {
            new HiloEscritor("Escritor" + i, smfro).start();
        }
    }
}
```

### 7.5. **El problema del interbloqueo (deadlock)**

El **interbloqueo** o **deadlock** ocurre cuando dos o más hilos se bloquean mutuamente, esperando indefinidamente a que el otro libere un recurso. Esto sucede cuando:

1. **Cada hilo espera un recurso** que otro hilo tiene bloqueado.
2. **Forman un ciclo de espera**, donde cada hilo está esperando a que otro hilo libere un recurso.

#### Condiciones para el interbloqueo

Para que ocurra un interbloqueo, deben cumplirse las siguientes condiciones:

1. **Exclusión mutua.** Solo un hilo puede acceder a un recurso a la vez.
2. **Retención y espera.** Un hilo retiene un recurso mientras espera por otro.
3. **No apropiación.** Un recurso no puede ser arrebatado a un hilo; debe ser liberado voluntariamente.
4. **Espera circular.** Existe un ciclo de hilos, cada uno esperando por un recurso que el siguiente hilo tiene.

#### Ejemplo de interbloqueo

Imagina que tenemos dos hilos, `hilo1` y `hilo2`, que intentan acceder a dos recursos, `recurso1` y `recurso2`. `hilo1` bloquea `recurso1` y espera por `recurso2`, mientras que `hilo2` bloquea `recurso2` y espera por `recurso1`. Ambos hilos quedan en un estado de espera indefinida, causando un **interbloqueo.**

```java
public class DeadlockExample {
    private static final Object recurso1 = new Object();
    private static final Object recurso2 = new Object();

    public static void main(String[] args) {
        Thread hilo1 = new Thread(() -> {
            synchronized (recurso1) {
                System.out.println("Hilo 1: Bloqueado recurso 1");
                try {
                    Thread.sleep(100); // Simula un retraso
                } catch (InterruptedException e) {}
                synchronized (recurso2) {
                    System.out.println("Hilo 1: Bloqueado recurso 2");
                }
            }
        });

        Thread hilo2 = new Thread(() -> {
            synchronized (recurso2) {
                System.out.println("Hilo 2: Bloqueado recurso 2");
                try {
                    Thread.sleep(100); // Simula un retraso
                } catch (InterruptedException e) {}
                synchronized (recurso1) {
                    System.out.println("Hilo 2: Bloqueado recurso 1");
                }
            }
        });

        hilo1.start();
        hilo2.start();
    }
}
```

#### Solución al interbloqueo

Para evitar el interbloqueo, se pueden aplicar las siguientes estrategias:

1. **Evitar la espera circular.** Asegurarse de que los hilos soliciten los recursos en un orden predefinido.
2. **Timeouts.** Usar `tryLock()` con un tiempo de espera máximo para evitar que los hilos esperen indefinidamente.
3. **Detección y recuperación.** Monitorear los hilos y liberar recursos manualmente si se detecta un interbloqueo.

### 7.6. **La clase `Semaphore`**

La clase `Semaphore` en Java permite controlar el acceso a un recurso compartido mediante un sistema de permisos. Un semáforo puede ser utilizado para limitar el número de hilos que pueden acceder a un recurso simultáneamente.

#### Métodos principales de `Semaphore`

| | |
|-|-|
| `acquire()` | Solicita un permiso. Si no hay permisos disponibles, el hilo se bloquea hasta que uno sea liberado.
| `release()` | Libera un permiso, permitiendo que otro hilo lo adquiera.
| `tryAcquire()` | Intenta adquirir un permiso sin bloquear el hilo. Devuelve `true` si el permiso fue adquirido, `false` en caso contrario.

#### Ejemplo: Uso de `Semaphore` para proteger secciones críticas

En este ejemplo, se simula el acceso simultáneo de 4 terminales a un servidor, utilizando un semáforo para controlar el acceso.

```java
package semaphoreejemplo1;

import java.util.concurrent.Semaphore;

public class Hilo_Terminal extends Thread {
    private ServidorWeb servidor;
    private Semaphore semaforo;

    public Hilo_Terminal(ServidorWeb s, Semaphore se) {
        this.servidor = s;
        this.semaforo = se;
    }

    @Override
    public void run() {
        for (int i = 1; i <= 10; i++) {
            try {
                semaforo.acquire(); // Adquiere el permiso
                servidor.incrementaCuenta(); // Accede al recurso compartido
            } catch (InterruptedException e) {
                e.printStackTrace();
            } finally {
                semaforo.release(); // Libera el permiso
            }
            Thread.yield();
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Semaphore semaforo = new Semaphore(1); // Semáforo con 1 permiso
        ServidorWeb servidor = new ServidorWeb();

        Hilo_Terminal hterminal1 = new Hilo_Terminal(servidor, semaforo);
        Hilo_Terminal hterminal2 = new Hilo_Terminal(servidor, semaforo);
        Hilo_Terminal hterminal3 = new Hilo_Terminal(servidor, semaforo);
        Hilo_Terminal hterminal4 = new Hilo_Terminal(servidor, semaforo);

        hterminal1.start();
        hterminal2.start();
        hterminal3.start();
        hterminal4.start();
    }
}

class ServidorWeb {
    private int cuenta;

    public ServidorWeb() {
        cuenta = 0;
    }

    public void incrementaCuenta() {
        System.out.println("hilo " + Thread.currentThread().getName() + "----- Entra en Servidor");
        cuenta++;
        System.out.println(cuenta + " accesos");
    }
}
```

#### Ejemplo: Uso de `Semaphore` para comunicar hilos (Lectores-Escritores)

En este ejemplo, se simula el acceso de lectores y escritores a una base de datos, utilizando un semáforo para garantizar que los escritores tengan acceso exclusivo.

```java
package semaphoreejemplo2;

import java.util.concurrent.Semaphore;

public class Escritor extends Thread {
    private Semaphore semaforo;

    public Escritor(String nombre, Semaphore s) {
        super(nombre);
        this.semaforo = s;
    }

    @Override
    public void run() {
        System.out.println(getName() + " intentando escribir");
        try {
            semaforo.acquire(5); // Adquiere 5 permisos (acceso exclusivo)
            System.out.println(getName() + ": Escribiendo");
            Thread.sleep((int) (Math.random() * 50)); // Simula la escritura
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            semaforo.release(5); // Libera los permisos
            System.out.println(getName() + ": Ya he escrito");
        }
    }
}

public class Lector extends Thread {
    private Semaphore semaforo;

    public Lector(String nombre, Semaphore s) {
        super(nombre);
        this.semaforo = s;
    }

    @Override
    public void run() {
        System.out.println(getName() + " : Intentando leer");
        try {
            semaforo.acquire(); // Adquiere un permiso
            System.out.println(getName() + " : Leyendo");
            Thread.sleep((int) (Math.random() * 50)); // Simula la lectura
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            semaforo.release(); // Libera el permiso
            System.out.println(getName() + " : Ya he leido");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Semaphore sema = new Semaphore(5); // Semáforo con 5 permisos

        for (int i = 1; i <= 2; i++) {
            new Escritor("Escritor " + i, sema).start();
        }
        for (int i = 1; i <= 5; i++) {
            new Lector("Lector " + i, sema).start();
        }
    }
}
```

### 7.7. **El búfer circular**

Un **búfer circular** es una estructura de datos que permite almacenar datos de manera cíclica. Es útil en situaciones donde los datos se producen y consumen de manera asíncrona, como en el problema del productor-consumidor.

#### Características del búfer circular

- **Tamaño fijo.** El búfer tiene un tamaño máximo predefinido.
- **Acceso cíclico.** Cuando se llega al final del búfer, se vuelve al principio.
- **Sincronización.** Se debe garantizar que el productor no sobreescriba datos no consumidos y que el consumidor no lea datos no producidos.

#### Ejemplo: Búfer circular en Java

Imagina que tenemos un búfer circular que almacena números enteros. Un hilo productor produce números y los almacena en el búfer, mientras que un hilo consumidor los consume. El búfer circular garantiza que no se sobreescriban datos no consumidos y que no se lean datos no producidos.

```java
public class BufferCircular {
    private final int[] buffer;
    private int tamaño;
    private int frente;
    private int fin;
    private int contador;

    public BufferCircular(int capacidad) {
        buffer = new int[capacidad];
        tamaño = capacidad;
        frente = 0;
        fin = 0;
        contador = 0;
    }

    public synchronized void producir(int dato) throws InterruptedException {
        while (contador == tamaño) {
            wait(); // Espera si el búfer está lleno
        }
        buffer[fin] = dato;
        fin = (fin + 1) % tamaño;
        contador++;
        notifyAll(); // Notifica a los consumidores
    }

    public synchronized int consumir() throws InterruptedException {
        while (contador == 0) {
            wait(); // Espera si el búfer está vacío
        }
        int dato = buffer[frente];
        frente = (frente + 1) % tamaño;
        contador--;
        notifyAll(); // Notifica a los productores
        return dato;
    }
}

public class Productor extends Thread {
    private BufferCircular buffer;

    public Productor(BufferCircular b) {
        this.buffer = b;
    }

    @Override
    public void run() {
        for (int i = 0; i < 10; i++) {
            try {
                buffer.producir(i);
                System.out.println("Producido: " + i);
                Thread.sleep(100); // Simula la producción
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

public class Consumidor extends Thread {
    private BufferCircular buffer;

    public Consumidor(BufferCircular b) {
        this.buffer = b;
    }

    @Override
    public void run() {
        for (int i = 0; i < 10; i++) {
            try {
                int dato = buffer.consumir();
                System.out.println("Consumido: " + dato);
                Thread.sleep(150); // Simula el consumo
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

public class Main {
    public static void main(String[] args) {
        BufferCircular buffer = new BufferCircular(5); // Búfer de tamaño 5
        Productor productor = new Productor(buffer);
        Consumidor consumidor = new Consumidor(buffer);

        productor.start();
        consumidor.start();
    }
}
```

### 7.8. **La clase `Exchanger`**

La clase `Exchanger` del paquete `java.util.concurrent` permite que dos hilos intercambien objetos en un punto de sincronización. Es útil en escenarios donde un hilo produce datos y otro los consume, permitiendo que ambos trabajen de manera concurrente.

#### Métodos principales de `Exchanger`

- **`exchange(V x)`.** Intercambia un objeto con otro hilo. El hilo que llama a este método se bloquea hasta que otro hilo también llame a `exchange()`.
- **`exchange(V x, long timeout, TimeUnit unit)`.** Similar al anterior, pero con un tiempo de espera máximo. Si el tiempo de espera se agota, el método lanza una excepción `TimeoutException`.

#### Funcionamiento de `Exchanger`

1. Dos hilos (por ejemplo, `hiloA` y `hiloB`) intercambian objetos del mismo tipo.
2. El `hiloA` llama a `exchange(objetoA)` y el `hiloB` llama a `exchange(objetoB)`.
3. El hilo que llama primero a `exchange()` se bloquea hasta que el otro hilo también llame a `exchange()`.
4. Una vez que ambos hilos han llamado a `exchange()`, el método devuelve el objeto intercambiado. El `hiloA` recibe `objetoB` y el `hiloB` recibe `objetoA`.

#### Ejemplo: Uso de `Exchanger`

En este ejemplo, un hilo productor genera una cadena de 10 caracteres, mientras que un hilo consumidor la imprime. Ambos hilos utilizan un `Exchanger` para intercambiar la cadena.

```java
package PaquetePrincipal;

import java.util.concurrent.Exchanger;

public class Main {
    public static void main(String[] args) {
        Exchanger<String> exgr = new Exchanger<>(); // Intercambiador para cadenas

        HiloProductor productor = new HiloProductor(exgr); // Hilo productor
        productor.start(); // Inicia el hilo productor

        HiloConsumidor consumidor = new HiloConsumidor(exgr); // Hilo consumidor
        consumidor.start(); // Inicia el hilo consumidor

        try {
            Thread.sleep(1000); // Espera 1 segundo
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        productor.parada(); // Detiene el hilo productor
    }
}

class HiloConsumidor extends Thread {
    private final Exchanger<String> intercambiadorCadena;
    private String str;

    HiloConsumidor(Exchanger<String> echger) {
        this.intercambiadorCadena = echger;
    }

    @Override
    public void run() {
        while (str == null || str.length() > 0) {
            try {
                str = intercambiadorCadena.exchange(""); // Intercambia una cadena vacía
                if (str.length() > 0) {
                    System.out.println("Consumidor escribe " + str);
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

class HiloProductor extends Thread {
    private final Exchanger<String> intercambiadorCadena;
    private boolean continuar;
    private String str;

    HiloProductor(Exchanger<String> echger) {
        this.intercambiadorCadena = echger;
        this.continuar = true;
        this.str = "";
    }

    @Override
    public void run() {
        char ch = 'A';
        while (continuar) {
            for (int j = 0; j < 10; j++) {
                str += (char) ch++;
                if (ch > 'Z') ch = 'A'; // Reinicia el carácter si llega a 'Z'
            }
            try {
                str = intercambiadorCadena.exchange(str); // Intercambia la cadena
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        try {
            intercambiadorCadena.exchange(str); // Señal de parada
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public void parada() {
        continuar = false; // Detiene el hilo
    }
}
```

### 7.9. **La clase `CountDownLatch`**

La clase `CountDownLatch` permite que uno o más hilos esperen hasta que otros hilos completen su trabajo. Es útil para sincronizar tareas que deben esperar a que otras finalicen.

#### Métodos principales de `CountDownLatch`

- **`await()`.** Bloquea el hilo hasta que el contador llegue a cero.
- **`countDown()`.** Decrementa el contador en uno.
- **`getCount()`.** Devuelve el valor actual del contador.

#### Ejemplo: Uso de `CountDownLatch`

En este ejemplo, se suman los elementos de una matriz en paralelo. Cada fila de la matriz es sumada por un hilo, y el hilo principal espera a que todos los hilos terminen antes de calcular la suma total.

```java
package PaquetePrincipal;

import java.util.concurrent.CountDownLatch;

public class Main {
    private static int[][] tabla = {
        {1}, {1, 1}, {1, 2, 1}, {1, 3, 3, 1}, {1, 4, 6, 4, 1},
        {1, 5, 10, 10, 5, 1}, {1, 6, 15, 20, 15, 6, 1},
        {1, 7, 21, 35, 35, 21, 7, 1}, {1, 8, 28, 56, 70, 56, 28, 8, 1},
        {1, 9, 36, 84, 126, 126, 84, 36, 9, 1}
    };
    private static int[] resultadoTanda;

    public static void main(String[] args) {
        final int ntandas = tabla.length;
        resultadoTanda = new int[ntandas];
        CountDownLatch cdl = new CountDownLatch(ntandas);

        System.out.println("Obteniendo la suma de los elementos de cada tanda...\n");

        for (int i = 0; i < ntandas; i++) {
            new SumaTanda(cdl, i).start();
        }

        try {
            cdl.await(); // Espera a que todos los hilos terminen
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        int sumaTotal = 0;
        for (int i = 0; i < ntandas; i++) {
            sumaTotal += resultadoTanda[i];
        }

        System.out.println("\nTodas las tandas han sido sumadas. Total: " + sumaTotal);
    }

    private static class SumaTanda extends Thread {
        private final CountDownLatch cdl;
        private final int t;

        SumaTanda(CountDownLatch cdl, int t) {
            this.cdl = cdl;
            this.t = t;
        }

        @Override
        public void run() {
            int sumaTanda = 0;
            for (int i = 0; i < tabla[t].length; i++) {
                sumaTanda += tabla[t][i];
            }
            resultadoTanda[t] = sumaTanda;
            System.out.println("La suma de los elementos de la tanda " + t + " es: " + sumaTanda);
            cdl.countDown(); // Decrementa el contador
        }
    }
}
```

### 7.10. **La clase `CyclicBarrier`**

La clase `CyclicBarrier` permite que un grupo de hilos esperen hasta que todos hayan alcanzado un punto de sincronización. A diferencia de `CountDownLatch`, `CyclicBarrier` puede ser reutilizada.

#### Métodos principales de `CyclicBarrier`

- **`await()`.** Bloquea el hilo hasta que todos los hilos hayan llamado a `await()`.
- **`reset()`.** Reinicia la barrera a su estado inicial.
- **`getNumberWaiting()`.** Devuelve el número de hilos esperando en la barrera.

#### Ejemplo: Uso de `CyclicBarrier`

En este ejemplo, se suman los elementos de una matriz en paralelo. Cada fila es sumada por un hilo, y cuando 5 hilos terminan, se dispara una acción que suma los resultados parciales.

```java
package PaquetePrincipal;

import java.util.concurrent.CyclicBarrier;

public class Main {
    private static int[][] tabla = {
        {1}, {1, 1}, {1, 2, 1}, {1, 3, 3, 1}, {1, 4, 6, 4, 1},
        {1, 5, 10, 10, 5, 1}, {1, 6, 15, 20, 15, 6, 1},
        {1, 7, 21, 35, 35, 21, 7, 1}, {1, 8, 28, 56, 70, 56, 28, 8, 1},
        {1, 9, 36, 84, 126, 126, 84, 36, 9, 1}
    };
    private static int[] resultadoTanda;

    public static void main(String[] args) {
        final int ntandas = tabla.length;
        resultadoTanda = new int[ntandas];

        Runnable sumaParcial = () -> {
            int totalAcumulado = 0;
            for (int i = 0; i < ntandas; i++) {
                totalAcumulado += resultadoTanda[i];
            }
            System.out.println("\nBarrera completada. Total acumulado: " + totalAcumulado + "\n");
        };

        CyclicBarrier barreraCiclica = new CyclicBarrier(5, sumaParcial);

        for (int i = 0; i < ntandas; i++) {
            new SumaTanda(barreraCiclica, i).start();
        }
    }

    private static class SumaTanda extends Thread {
        private final CyclicBarrier barreraCiclica;
        private final int t;

        SumaTanda(CyclicBarrier barreraCiclica, int t) {
            this.barreraCiclica = barreraCiclica;
            this.t = t;
        }

        @Override
        public void run() {
            int sumaParcial = 0;
            for (int i = 0; i < tabla[t].length; i++) {
                sumaParcial += tabla[t][i];
            }
            resultadoTanda[t] = sumaParcial;
            System.out.println("La suma de los elementos de la tanda " + t + " es: " + sumaParcial);

            try {
                barreraCiclica.await(); // Espera a que otros hilos terminen
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}
```

## 8. Aplicaciones multihilo

Las aplicaciones multihilo deben cumplir con dos propiedades fundamentales:

1. **Seguridad.** La aplicación no debe llegar a un estado inconsistente debido a un mal uso de los recursos compartidos. Esto implica sincronizar hilos para garantizar la **exclusión mutua.**
2. **Viveza.** La aplicación no debe bloquearse ni provocar que un hilo no pueda ejecutarse. Esto implica evitar **interbloqueos** (deadlocks) y **inanición** (starvation).

**Corrección de una aplicación multihilo**

- **Corrección parcial.** Se cumple la propiedad de seguridad. El programa termina y el resultado es el deseado.
- **Corrección total.** Se cumplen las propiedades de seguridad y viveza. El programa termina y el resultado es correcto.

**Aspectos a considerar en aplicaciones multihilo**

- **Situación de los hilos.** 
  - **Independientes.** No es necesario sincronizar o comunicar los hilos.
  - **Colaborando/compitiendo.** Es necesario sincronizar y comunicar los hilos, evitando interbloqueos y esperas indefinidas.
- **Gestión de prioridades.** Los hilos más importantes deben ejecutarse primero.
- **No determinismo.** La ejecución de hilos es no determinística, lo que complica la depuración y el diseño.

**Ventajas de usar librerías estándar**

- **Facilitan la programación.** Requieren menos esfuerzo que desarrollar una solución desde cero.
- **Mayor rendimiento.** Los algoritmos están optimizados por expertos.
- **Mayor fiabilidad.** Evitan interbloqueos, condiciones de carrera y otros problemas comunes.
- **Menor mantenimiento.** El código es más legible y fácil de actualizar.
- **Mayor productividad.** Reduce el tiempo de aprendizaje y mejora la coordinación entre desarrolladores.

### 8.1. **Otras utilidades de concurrencia**

Además de las utilidades de sincronización, el paquete `java.util.concurrent` ofrece otras herramientas para manejar la concurrencia:

#### La interfaz `Executor`

- Permite ejecutar tareas en un hilo en segundo plano, en un hilo nuevo, o en un **pool de hilos.**
- Método principal: `execute(Runnable)`.
- Implementaciones comunes: `ExecutorService`, `ScheduledExecutorService`.

#### Colecciones concurrentes

- **`Queue`.** Colección diseñada para almacenar elementos antes de procesarlos.
- **`BlockingQueue`.** Cola segura para hilos (thread-safe) que permite esperar si no hay elementos disponibles.
- Implementaciones concurrentes de `Map` y `List`.

#### La clase `Locks`

- Proporciona bloqueos más flexibles que `synchronized`.
- Métodos principales:
  - `lock()`: Bloquea el recurso.
  - `unlock()`: Libera el recurso.
  - `newCondition()`: Crea una condición asociada al bloqueo.

#### Variables atómicas

- Clases como `AtomicInteger`, `AtomicLong`, etc., permiten operaciones atómicas sin necesidad de sincronización explícita.

### 8.2. **La interfaz `Executor` y los pools de hilos**

En aplicaciones tipo servidor, es común manejar un gran número de tareas concurrentes. Crear un hilo por cada tarea puede consumir muchos recursos. Los **pools de hilos** ofrecen una solución eficiente.

#### Creación de pools de hilos

- **`newFixedThreadPool(int numeroHilos)`.** Crea un pool con un número fijo de hilos.
- **`newCachedThreadPool()`.** Crea un pool que ajusta dinámicamente el número de hilos.
- **`newSingleThreadExecutor()`.** Crea un pool de un solo hilo.
- **`newScheduledThreadPool(int corePoolSize)`.** Crea un pool para ejecutar tareas programadas.

#### Ejemplo: Uso de `ExecutorService`

Imagina que tenemos un pool de 2 hilos y enviamos 30 tareas al pool. Cada tarea genera números aleatorios y los imprime. El pool gestiona la ejecución de las tareas de manera eficiente.

```java
package PaquetePrincipal;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Main {
    public static void main(String[] args) {
        // Crea un pool de 2 hilos
        ExecutorService executor = Executors.newFixedThreadPool(2);

        // Envía 30 tareas al pool
        for (int i = 1; i <= 30; i++) {
            executor.submit(new NumerosAleatorios());
        }

        // Cierra el pool después de que todas las tareas hayan terminado
        executor.shutdown();
    }
}

class NumerosAleatorios implements Runnable {
    @Override
    public void run() {
        Random random = new Random();
        StringBuilder strReturn = new StringBuilder();
        for (int i = 0; i < 10; i++) {
            strReturn.append(random.nextInt(50)).append(", ");
            Thread.yield();
        }
        System.out.println("Números aleatorios obtenidos por " 
            + Thread.currentThread().getName() + ": " + strReturn);
    }
}
```

### 8.3. **Gestión de excepciones**

En aplicaciones multihilo, las excepciones no capturadas pueden causar que un hilo termine abruptamente. Para manejar excepciones, se puede usar un **manejador de excepciones no capturadas.**

#### Ejemplo: Manejador de excepciones

Imagina que tenemos varios hilos que realizan una división. Si ocurre una división por cero, el hilo lanza una excepción. Usamos un manejador de excepciones para capturar y manejar estas excepciones.

```java
package manejoexcepciones;

public class Main {
    public static void main(String[] args) {
        ManejadorExcepciones manejador = new ManejadorExcepciones();

        for (int i = 1; i <= 5; i++) {
            Hilo hilo = new Hilo("hilo" + i);
            hilo.setUncaughtExceptionHandler(manejador);
            hilo.start();
        }
    }
}

class Hilo extends Thread {
    public Hilo(String nombre) {
        super(nombre);
    }

    @Override
    public void run() {
        Random random = new Random();
        int division = 100 / random.nextInt(4); // Puede lanzar ArithmeticException
        System.out.println("División: " + division);
    }
}

class ManejadorExcepciones implements Thread.UncaughtExceptionHandler {
    @Override
    public void uncaughtException(Thread t, Throwable e) {
        System.out.printf("Hilo que lanzó la excepción: %s\n", t.getName());
        e.printStackTrace();
    }
}
```

### 8.4. **Depuración y documentación**

#### Depuración de aplicaciones multihilo

La depuración de aplicaciones multihilo es compleja debido al comportamiento no determinístico de los hilos. Algunas herramientas útiles son:

- **`dumpStack()`.** Muestra la traza de la pila del hilo actual.
- **`getAllStackTraces()`.** Devuelve un mapa con las trazas de todos los hilos vivos.
- **`getStackTrace()`.** Devuelve la traza de la pila de un hilo específico.

#### Documentación con JavaDoc

La documentación es crucial para mejorar la legibilidad y mantenibilidad del código. JavaDoc permite generar documentación HTML a partir de comentarios en el código.

```java
/**
 * Esta clase representa un hilo que genera números aleatorios.
 */
class NumerosAleatorios implements Runnable {
    /**
     * Método run que genera 10 números aleatorios.
     */
    @Override
    public void run() {
        Random random = new Random();
        for (int i = 0; i < 10; i++) {
            System.out.println(random.nextInt(50));
        }
    }
}
```
