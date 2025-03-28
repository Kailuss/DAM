---
tags: [DAM, psp]
cssclasses: [dam-psp, table-compact-clean]
banner: "![[psp.jpg]]"
banner_y: 0.32
---

# **Resumen TEMA 2.**<br>Programación Multihilo

## 1. Introducción

Un programa puede tener uno o varios flujos de ejecución. En un programa de *flujo único*, las tareas se ejecutan de manera secuencial, una tras otra. En uno de *flujo múltiple*, las tareas se distribuyen en hilos independientes. Estos hilos permiten ejecutar acciones de forma concurrente, como descargar una imagen y navegar en un navegador web. Aunque parezca simultáneo, depende del hardware y del sistema operativo.

## 2. Conceptos Básicos

|     |     |
| --- | --- |
|**Hilo (Thread).**|Un *hilo* es un flujo de control secuencial dentro de un proceso. Comparte memoria con otros hilos, pero tiene su propio contador de programa y pila. Los recursos compartidos incluyen código, variables globales y archivos abiertos. Si un hilo modifica mal un recurso compartido, afecta a todos. Por eso, la sincronización es esencial.|
| **Ventajas.**|Los hilos son más ligeros que los procesos tradicionales. Consumen menos recursos y permiten conmutación rápida entre tareas. En sistemas multiprocesador, pueden ejecutarse en paralelo. Son ideales para aplicaciones con múltiples entradas, como servidores web que atienden muchas peticiones.|
| **Problemas comunes.**|Condiciones de carrera, interbloqueos (deadlocks).

## 3. Multihilo en Java

Java ofrece soporte nativo para hilos mediante clases en `java.lang` y herramientas avanzadas en `java.util.concurrent`.

### 3.1. **Clases Básicas**
- La clase ***Thread*** permite crear y gestionar hilos directamente.
- La interfaz ***Runnable*** añade funcionalidad a clases que ya heredan de otra.
- Métodos como ***wait()*** y ***notify()*** en la clase *Object* ayudan a sincronizar hilos.

### 3.2. **Herramientas Avanzadas**
- ***Semaphore*** limita el acceso a recursos con permisos.
- ***CountDownLatch*** espera a que varios hilos terminen antes de continuar.
- ***ExecutorService*** gestiona pools de hilos para tareas repetitivas.
- ***AtomicInteger*** realiza operaciones atómicas sin bloqueos explícitos.

## 4. Creación de Hilos

Hay dos enfoques principales en Java:

### 4.1. **Extendiendo `Thread`**

Pasos:

1. Crear una clase que herede de *Thread*.
2. Redefinir el método *run()* con el código a ejecutar.
3. Instanciar la clase y llamar a *start()* para iniciar el hilo.

**Ejemplo:** Imagina una clase *Saludo* que hereda de *Thread*. Su método *run()* imprime un mensaje. Al llamar a *start()*, el mensaje se muestra en un hilo independiente.  

```java
class HiloSaludo extends Thread {
    @Override
    public void run() {
        System.out.println("Hilo creado extendiendo Thread.");
    }

    public static void main(String[] args) {
        HiloSaludo hilo = new HiloSaludo();
        hilo.start(); // Inicia el hilo
    }
}
```

### 4.2. **Implementando `Runnable` (Recomendado)**

Pasos:

1. Crear una clase que implemente *Runnable*.
2. Redefinir *run()*.
3. Pasar un objeto de esta clase a un *Thread* y llamar a *start()*.

**Ejemplo:** Una clase *Saludo* implementa *Runnable*. Se crea un objeto *Thread* con esta clase, y al iniciarlo, ejecuta el código de *run()*.  

```java
class TareaSaludo implements Runnable {
    @Override
    public void run() {
        System.out.println("Hilo creado con Runnable.");
    }

    public static void main(String[] args) {
        Thread hilo = new Thread(new TareaSaludo());
        hilo.start();
    }
}
```

## 5. Estados de un Hilo

Un hilo pasa por cuatro estados principales:

| Estado               | Descripción                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| **Nuevo**            | Hilo creado pero no iniciado.                                               |
| **Ejecutable**       | Listo para ejecutarse (puede estar en espera de CPU).                       |
| **No Ejecutable**    | Bloqueado (por `sleep()`, `wait()`, o E/S).                                 |
| **Terminado**        | Finalizó su ejecución.                                                      |

### 5.1. **Métodos Clave**
- *sleep(milisegundos)*: Pausa el hilo temporalmente.
- *wait()*: Detiene el hilo hasta que otro llame a *notify()*.
- *yield()*: Sugiere al planificador ceder el control a otros hilos.

**Advertencia:** Métodos como *stop()* o *suspend()* están obsoletos por inseguros.

## 6. Gestión de Prioridades

Cada hilo tiene una prioridad del 1 al 10. *MAX_PRIORITY* es 10, *MIN_PRIORITY* es 1. Usa *setPriority()* para ajustarla. Hilos con prioridad alta se ejecutan primero, pero no es garantizado.

**Problema de Hilos Egoístas:** En sistemas sin *time-slicing*, un hilo puede monopolizar la CPU. *yield()* ayuda, pero depende del planificador.

## 7. Sincronización
### 7.1. **Problemas con Recursos Compartidos**

Ejemplo: Si dos hilos incrementan una variable *cuenta* al mismo tiempo, el resultado puede ser incorrecto. Esto se llama *condición de carrera*.

**Solución.** Usar *synchronized* en métodos o bloques de código.
- Un método sincronizado solo permite un hilo a la vez.
- Los bloques sincronizados protegen secciones críticas específicas.

**Ejemplo.** En un servidor web, el método *incrementaCuenta()* se marca como *synchronized*. Así, solo un hilo actualiza la variable a la vez.  

```java
class Contador {
    private int valor = 0;

    public synchronized void incrementar() {
        valor++;
    }

    public synchronized int getValor() {
        return valor;
    }
}
```

### 7.2. **Comunicación entre Hilos (`wait()`, `notify()`)**
- *wait()*: Pone el hilo en espera hasta que otro lo notifique.
- *notify()*: Despierta a un hilo en espera.
- *notifyAll()*: Despierta a todos los hilos en espera.

**Ejemplo del Productor-Consumidor.** El productor llena un búfer y el consumidor lo vacía. Si el búfer está lleno, el productor espera con *wait()*. Cuando el consumidor vacía, usa *notify()* para avisar.  

```java
class Buffer {
    private int dato;
    private boolean disponible = false;

    public synchronized void producir(int valor) throws InterruptedException {
        while (disponible) wait(); // Espera si hay dato sin consumir
        dato = valor;
        disponible = true;
        notify(); // Notifica al consumidor
    }

    public synchronized int consumir() throws InterruptedException {
        while (!disponible) wait(); // Espera si no hay dato
        disponible = false;
        notify(); // Notifica al productor
        return dato;
    }
}
```

### 7.3. **Interbloqueo (Deadlock)**

Ocurre cuando dos hilos esperan recursos bloqueados mutuamente.

**Condiciones:**
1. Exclusión mutua.
2. Retención y espera.
3. No apropiación.
4. Espera circular.

**Ejemplo.**  
Hilo1 bloquea *recurso1* y espera *recurso2*. Hilo2 bloquea *recurso2* y espera *recurso1*. Ambos se bloquean indefinidamente.  

**Solución.** Ordenar la solicitud de recursos o usar *tryLock()* con tiempo límite.  

## 8. Herramientas Avanzadas
### 8.1. **`Semaphore`**

Controla el acceso a recursos mediante permisos.  
- *acquire()*: Solicita un permiso.  
- *release()*: Libera un permiso.  

**Ejemplo.** Un semáforo con un permiso garantiza que solo un hilo acceda a una sección crítica.  

```java
Semaphore semaforo = new Semaphore(3); // Permite 3 accesos simultáneos

semaforo.acquire(); // Adquiere un permiso
// Acceso al recurso
semaforo.release(); // Libera el permiso
```

### 8.2. **`CountDownLatch`**

Espera a que varios hilos terminen.  
- *await()*: Bloquea hasta que el contador llegue a cero.  
- *countDown()*: Reduce el contador.  

**Ejemplo.** Un hilo principal espera a que cinco hilos secundarios completen tareas antes de continuar.  

```java
CountDownLatch latch = new CountDownLatch(3);

// En cada hilo:
latch.countDown(); // Decrementa el contador

// Hilo principal:
latch.await(); // Espera hasta que el contador llegue a 0
```

### 8.3. **`ExecutorService` (Pools de Hilos)**

Gestiona pools de hilos para optimizar recursos.  
- *newFixedThreadPool()*: Crea un número fijo de hilos.  
- *submit()*: Envía tareas al pool.  

**Ejemplo.** Un servidor usa un pool de diez hilos para manejar cien solicitudes de clientes.  

```java
ExecutorService executor = Executors.newFixedThreadPool(4);
executor.submit(() -> {
    // Tarea a ejecutar
});
executor.shutdown();
```

## 9. Buenas Prácticas


|     |     |
| --- | --- |
| **Seguridad.**| Evitar condiciones de carrera con sincronización.|
| **Viveza.**| Prevenir interbloqueos e inanición.|
| **Manejo de Excepciones.**| Usar *UncaughtExceptionHandler* para capturar errores no tratados.|
| **Documentación.**| Explicar claramente cómo interactúan los hilos.|

**Consejo Final:** Prioriza claridad sobre optimización prematura. Usa herramientas como *java.util.concurrent* en lugar de reinventar soluciones.

## 10. Ejemplo Integrado: Sistema de Venta de Tickets

```java
class SistemaTickets {
    private int ticketsDisponibles = 100;
    private final Lock lock = new ReentrantLock();

    public void comprarTicket(String cliente) {
        lock.lock();
        try {
            if (ticketsDisponibles > 0) {
                System.out.println(cliente + " compró ticket #" + ticketsDisponibles);
                ticketsDisponibles--;
            }
        } finally {
            lock.unlock();
        }
    }

    public static void main(String[] args) {
        SistemaTickets sistema = new SistemaTickets();
        ExecutorService executor = Executors.newFixedThreadPool(5);

        for (int i = 0; i < 10; i++) {
            executor.submit(() -> sistema.comprarTicket(Thread.currentThread().getName()));
        }

        executor.shutdown();
    }
}
```

**Explicación:**
- Usa `ReentrantLock` para sincronizar el acceso a `ticketsDisponibles`.
- Un `ExecutorService` maneja 5 hilos que compiten por comprar tickets.
- Cada hilo ejecuta `comprarTicket()`, que reduce el contador de forma segura.

## 11. Conclusión

La programación multihilo en Java permite ejecutar tareas concurrentes eficientemente. Claves:

- Usar `Runnable` para flexibilidad.
- Sincronizar con `synchronized` o `Lock`.
- Utilizar herramientas como `Semaphore` y `ExecutorService` para casos complejos.
- Evitar interbloqueos y condiciones de carrera con diseño cuidadoso.
