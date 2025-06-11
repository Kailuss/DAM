---
tags:
  - DAM
  - PSP
cssclasses:
  - table-compact-clean
  - dam-psp
banner: "![[psp.jpg]]"
banner_y: 0.25
number headings: off
---

# **Examen de PSP**

## Ejercicio 1.

1. **¿Qué es un proceso? Explica qué es un proceso padre e hijo y cómo pueden comunicarse entre sí en Java.**

   > Un **proceso** es una instancia en ejecución de un programa. Tiene su propio espacio de direcciones en memoria, variables, contador de programa, pila y otros recursos del sistema operativo.
   >
   > Un **proceso padre** es aquel que crea a otro proceso, el **proceso hijo**, generalmente mediante una llamada al sistema.
   >
   > En Java, los procesos pueden crearse usando la clase `ProcessBuilder` o `Runtime`.
   >
   > **Comunicación entre procesos (IPC)** en Java puede lograrse mediante:
   > - Pipes (Tubos)
   > - Archivos compartidos
   > - Sockets
   > - Señales (aunque más común en sistemas UNIX directamente)
   >
   >
   >```java
   >// Ejemplo simple de creación de un proceso hijo en Java
   >
   > ProcessBuilder pb = new ProcessBuilder(
   >	   "java",
   >	   "-cp",
   >	   "../psp/out/artifacts/psp__jar/psp.jar",
   >	   "org.example.carregarPaginaWeb" );
   > Process p = pb.start();
   >```
   > 
   >```java
   >// Comunicación usando un Pipe (simulado)
   >
   >ProcessBuilder pb = new ProcessBuilder("java", "MiProcesoHijo");
   >Process proceso = pb.start();
   >
   >OutputStream os = proceso.getOutputStream();
   >os.write("Mensaje al hijo".getBytes());
   >os.flush();
   >```

<br>

2. **Modelos OSI y TCP/IP. Capas y función.**

   > **<u>Modelo OSI</u> (de capa 7 a 1):**
   > 
   > | Capa | Función | 
   > | - | - | 
   > | 1. **Aplicación** | Interactúa con el usuario (SMTP, HTTP, DNS, SSH) | 
   > | 2. **Presentación** | Traducción, cifrado y codificación de datos | 
   > | 3. **Sesión** | Controla y mantiene sesiones entre aplicaciones | 
   > | 4. **Transporte** | Transferencia de datos con control de errores (TCP, UDP) | 
   > | 5. **Red** | Enrutamiento de paquetes (IP) | 
   > | 6. **Enlace de Datos** | Manejo de direcciones físicas (MAC, switches) | 
   > | 7. **Física** | Medio de transmisión (cables, WiFi, etc.) | 
   > 
   > **<u>Modelo TCP/IP</u> (equivalente simplificado):**
   > 
   > | Capa | Función | 
   > | - | - | 
   > | 1. **Acceso a la red.** |Equivalente a física + enlace de datos.|
   > | 2. **Internet.**| Encaminamiento (IP).|
   > | 3. **Transporte.** |TCP/UDP.|
   > | 4. **Aplicación.** |Protocolos como HTTP, FTP, DNS.|

<br>

3. **Describe los protocolos vistos que pertenecen a la capa de aplicación del modelo TCP/IP.**

   > **<u>HTTP</u> (Hypertext Transfer Protocol)**
   > 
   > - Usado para la transferencia de páginas web.
   > - Funciona sobre TCP, puerto 80 o 443 (HTTPS).
   >     
   > **<u>DNS</u> (Domain Name System)**
   > 
   > - Traduce nombres de dominio (como `google.com`) a direcciones IP.
   > - Usa UDP y TCP, puerto 53.
   >     
   > 
   > **<u>FTP</u> (File Transfer Protocol)**
   > 
   > - Permite la transferencia de archivos entre sistemas remotos.
   > - Utiliza TCP, puertos 20 (datos) y 21 (control).
   >     
   > 
   > **<u>SSH</u> (Secure Shell)**
   > 
   > - Proporciona acceso remoto seguro a sistemas mediante línea de comandos.   
   > - Utiliza TCP, puerto 22.   
   > 
   > **<u>SMTP</u> (Simple Mail Transfer Protocol)**
   > 
   > - Se utiliza para el envío de correos electrónicos.
   > - Utiliza TCP, puerto 25 (o 587 para envío autenticado, y 465 para SMTP seguro).

<br>

4. **Etapas o estados por los que pasa un proceso durante su ciclo de vida.

   >| Etapa | Explicación | 
   >| - | - | 
   >| **New** | El proceso ha sido creado, pero aún no está listo para ejecutarse.| 
   >| **Ready** | El proceso está listo para ejecutarse y espera su turno de CPU.| 
   >| **Running** | El proceso está siendo ejecutado por el procesador.| 
   >| **Blocked** | El proceso está esperando un recurso o evento externo.| 
   >| **Detached (Terminado)** | El proceso ha finalizado su ejecución.| 

<br>

5. **¿Cuáles son las diferencias entre procesos e hilos? Pon ejemplos de cómo se declara cada uno de ellos en el lenguaje Java.**

   > |Característica|Proceso|Hilo|
   > |---|---|---|
   > |Memoria|Independiente|Comparte memoria del proceso padre|
   > |Comunicación|Más compleja (IPC)|Más sencilla (variables compartidas)|
   > |Creación|Costosa|Rápida|
   > |Ejecución paralela|Sí|Sí|
   > 
   > ```java
   > // Proceso
   > 
   > ProcessBuilder pb = new ProcessBuilder("notepad");
   > Process p = pb.start();
   > ```
   > 
   > ```java
   > // Hilo
   > 
   > public class MiHilo extends Thread {
   >     public void run() {
   >         System.out.println("Hola desde un hilo");
   >     }
   > }
   > 
   > new MiHilo().start();
   > ```

<br>

6. **¿Cuáles son los mecanismos de sincronización existentes? Describe cada uno de ellos (ventajas, diferencias, etc.), pon ejemplos y explica cómo se instancian en Java.**

   >**`synchronized`**
   >- Bloquea un método o bloque para acceso exclusivo.
   >- Ventaja: fácil de usar.
   >- Desventaja: poca granularidad.
   >
   >```java
   >public synchronized void metodoCritico() {
   >	// código exclusivo
   >}
   >```
   >---
   >   
    >**`ReentrantLock`** (de `java.util.concurrent.locks`)
    >
    >Más flexible que `synchronized`. Permite lock interrumpible y comprobaciones.
    >
    >```java
    >Lock lock = new ReentrantLock();
    >lock.lock();
    >try {
    >	// sección crítica
    >} finally {
    >	lock.unlock();
    >}
    >```
    >---
    >    
    >**`Semaphore`**
    >
    >Controla acceso a recursos limitados.
    >
    >```java
    >Semaphore sem = new Semaphore(3); // max 3 threads
    >sem.acquire();
    >// acceso al recurso
    >sem.release();
    >```
    >---
    >    
    >**`CountDownLatch` y `CyclicBarrier`**
    >
    >Para coordinar múltiples hilos.
    >
    >```java
    >CountDownLatch latch = new CountDownLatch(1);
    >new Thread(() -> {
    >	// espera
    >	latch.await();
    >}).start();
    >// señal
    >latch.countDown();
    >```

<br>

7. **¿Cómo se puede pasar información entre procesos en Java?**

   > Los **procesos** son independientes, por lo tanto, para **comunicarlos (IPC)** se usan mecanismos como:
   > 
   > 
   >**<u>Entrada/Salida estándar</u> (`stdin`/`stdout`)**
   >
    >```java
    >ProcessBuilder pb = new ProcessBuilder("java", "MiProcesoHijo");
    >Process p = pb.start();
    >
    >// Enviar información al hijo
    >OutputStream os = p.getOutputStream();
    >PrintWriter writer = new PrintWriter(os, true);
    >writer.println("Hola desde el padre");
    >
    >// Leer respuesta del hijo
    >BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
    >String respuesta = reader.readLine();
    >System.out.println("Respuesta del hijo: " + respuesta);
    >```
    >
    >**<u>Archivos compartidos:</u>** Padre y hijo leen/escriben un archivo común.
    >
    >**<u>Sockets:</u>** Comunicación red/localhost. Más compleja pero potente.
    >
    >**<u>RMI o servicios web:</u>** Para procesos distribuidos (más avanzado).
    >

<br>

8. **¿Cuáles son las formas de declarar hilos?**

   >**Extendiendo `Thread`**
   >
   >```java
   >class MiHilo extends Thread {
   >	public void run() {
   >		System.out.println("Desde el hilo");
   >	}
   >}
   >```
   >
   >**Implementando `Runnable`**
   >
   >```java
   >class MiTarea implements Runnable {
   >	public void run() {
   >		System.out.println("Tarea ejecutada");
   >	}
   >}
   >```

<br>

9. **¿Cómo se ejecuta un hilo según cómo fue creado?**

   >Los casos anteriores se ejecutan usando un objeto `Thread`:
   >
   >```java
   >Thread t1 = new MiHilo();
   >// si extiende Thread
   >t1.start();
   >
   >Thread t2 = new Thread(new MiTarea()); 
   >// si implementa Runnable
   >t2.start();
   >```
   >
   > **Importante:** Nunca uses `.run()` directamente si quieres paralelismo; siempre `.start()`.

<br>

10. **¿Cómo se pueden bloquear hilos y por qué motivo?**

    >Los **hilos se bloquean** para:
    >
    >- Esperar recursos
    >- Sincronizar ejecución
    >- Esperar que termine otro hilo
    >- Evitar condiciones de carrera
    >
    >**Ejemplo 1:** `Thread.sleep()` – Bloqueo por tiempo
    >
    >```java
    >Thread.sleep(2000); // pausa 2 segundos
    >```
    >
    >**Ejemplo 2:** `join()` – Esperar a otro hilo
    >
    >```java
    >Thread hilo = new MiHilo();
    >hilo.start();
    >hilo.join(); // el hilo actual espera hasta que 'hilo' termine
    >```
    >
    >**Ejemplo 3:** `wait()` – Espera controlada con sincronización
    >
    >```java
    >synchronized (objeto) {
    >	objeto.wait(); // hilo se suspende hasta que otro lo despierte con notify()
    >}
    >```

<br>

11. **Mecanismos de sincronización en Java**

    >**`Semaphore` (java.util.concurrent)**
    >
    >Controla cuántos hilos pueden acceder a un recurso al mismo tiempo.
    >
    >```java
    >Semaphore sem = new Semaphore(2); // Máximo 2 hilos al mismo tiempo
    >
    >Runnable tarea = () -> {
    >    try {
    >        sem.acquire();
    >        System.out.println(Thread.currentThread().getName() + " entra");
    >        Thread.sleep(1000); // simula trabajo
    >    } catch (InterruptedException e) {} 
    >    finally {
    >        sem.release();
    >    }
    >};
    >```
    >
    >**Ventajas:**
    >- Permite concurrencia parcial.
    >- Mejor control de acceso.
    >
    >---
    >**`synchronized` + `wait()` y `notify()`**
    >
    >Permite sincronización más detallada entre hilos.
    >
    >```java
    >class RecursoCompartido {
    >	private boolean disponible = false;
    >
    >	public synchronized void producir() throws InterruptedException {
    >		while (disponible) wait();
    >		System.out.println("Produciendo...");
    >		disponible = true;
    >		notify();
    >	}
    >
    >	public synchronized void consumir() throws InterruptedException {
    >		while (!disponible) wait();
    >		System.out.println("Consumiendo...");
    >		disponible = false;
    >		notify();
    >	}
    >}
    >```
    >
    >**Ventajas:**
    >
    >- Coordinación más directa entre productor y consumidor.
    >- Útil para notificaciones específicas.
    >
    >---
    >
    >**Diferencias entre `Semaphore` y `wait/notify`:**
    >
    >|Característica|`Semaphore`|`wait()/notify()`|
    >|---|---|---|
    >|Nivel de abstracción|Más alto|Más bajo|
    >|Flexibilidad|Control numérico de acceso|Control de condición compartida|
    >|Uso típico|Límite de acceso concurrente|Productor-consumidor|
    >|Requiere bloque `sync`|No|Sí|

---

## Ejercicio 2.
Trata de construir un programa parecido a un chat, usando un protocolo orientado a conexión. Para realizar este ejercicio, la estructura tiene que ser Cliente-Servidor, donde habrá un único servidor y múltiples hilos cliente. Explica todo lo que puedas y realiza un programa en Java o pseudocódigo que simule el funcionamiento.

La idea es que los clientes envíen mensajes al servidor, este los imprima por pantalla y les responda con el mensaje “Mensaje recibido”. Para añadir control de concurrencia, necesitamos que los mensajes recibidos por el servidor, además de imprimirse, también se almacenen en un fichero.

---

## Ejercicio 3.
En el ejercicio anterior, queremos mejorar la seguridad del sistema. Por eso, implementa un método de encriptación (si es posible) que consideres apropiado para proteger la comunicación entre el cliente y el servidor, y viceversa.

---

## Ejercicio 4.
Crea la siguiente aplicación en Java:
1. Escribe un programa llamado `ExerciciosMultiproceso1_ParImpar`. Este recibirá un número entero positivo y deberá mostrar el resultado `Par` si es par o `Impar` si es impar.
2. Escribe un programa llamado “ExercicisMultiproces1”. Este creará un proceso hijo para ejecutar el programa `ParellSenar` anterior. El proceso padre mostrará por pantalla “Introdueix un nombre:” y el usuario podrá introducir:
    - Un número entero positivo: en ese caso se creará el proceso hijo y se mostrará el resultado de su ejecución.
    - La palabra `exit`: en ese caso se terminará la ejecución del programa.
    

**Ejemplo:**

```plaintext
Introdueix un nombre:
10
Parell
Introdueix un nombre:
15
Senar
Introdueix un nombre:
30
Parell
Introdueix un nombre:
exit
BUILD SUCCESSFUL (total time: 9 seconds)
```

---

## Ejercicio 5.
Escribe un programa que haga lo siguiente:  
1. Crear un proceso hijo llamado `ExercicisMultiproces2_ModificarString`.
2. El proceso padre (llamado `ExercicisMultiproces2`) y el proceso hijo se comunicarán de forma bidireccional utilizando streams.
3. El padre leerá líneas desde su entrada estándar y las enviará a la entrada estándar del hijo (utilizando el `OutputStream` del hijo).
4. El hijo leerá el texto desde su entrada estándar, lo transformará todo a letras mayúsculas y sustituirá todas las vocales por el símbolo de guion bajo `_`. 
5. El padre imprimirá por pantalla lo que reciba del hijo mediante el InputStream del mismo. 
6. Cuando el padre hable, la salida en pantalla debe comenzar con: `El PADRE dice:` y cuando hable el hijo debe comenzar con: `El Hijo dice:`

**Ejemplo:**

```terminal
hello, world!
El PADRE dice: El hijo dice: H_LL_, W_RLD!
BUILD SUCCESSFUL (total time: 10 seconds)
```

**Tienes que crear dos proyectos:**

- `ExercicisMultiproces2` (padre)
- `ExercicisMultiproces2_ModificarString` (hijo)
    

---

## Ejercicio 6.
Se trata de construir un programa llamado TICTACTOC. La idea es que al ejecutarse imprima por pantalla la secuencia TIC – TAC – TOC. Cada hilo imprimirá la palabra correspondiente y la irá concatenando dentro de una variable compartida entre todos. Una vez que todos los hilos hayan terminado, el programa principal imprimirá esa variable compartida por pantalla.
    

Ten en cuenta que la ejecución por pantalla debe seguir el orden TIC – TAC – TOC – TIC – TAC – TOC, etc., pero la variable puede quedar con otro orden, por ejemplo:  
`tictactoctoctictactactoc` o `tictictictactoctoctoctictac`

Escribe en Java o pseudocódigo todas las clases que consideres necesarias.

---

## Ejercicio 7.

La topología de red en anillo se caracteriza por formar una conexión circular, en la que cada nodo solo puede comunicarse con el siguiente, hasta cerrar el anillo.
    

Simula esta topología en anillo usando **Datagram Sockets**, donde cada nodo (ordenador) será un Datagrama. El primer nodo iniciará la transmisión enviando su ID. Cada nodo, al recibir un mensaje, le concatenará su propio ID y lo reenviará al siguiente. La comunicación finaliza cuando el anillo se cierra.

El resultado final podría ser:

```terminal
Impreso desde el NODO1: Nodo1 Nodo2 Nodo3 Nodo4
```

Escribe en Java o pseudocódigo todas las clases necesarias para esta simulación.

---

## Ejercicio 8.
De los siguientes protocolos, escoge uno. Ubícalo dentro de una de las capas del modelo TCP/IP, explica todo lo que sepas sobre él (puedes usar esquemas si lo deseas) y pon un ejemplo de uso en pseudocódigo o Java. Protocolos: `DNS`, `SMTP`, `FTP` o `HTTP`.
    

---

## Ejercicio 9.
Explica cómo se realiza la **comunicación a través de SSL** y pon un ejemplo de utilización del protocolo. Puedes usar pseudocódigo o Java.