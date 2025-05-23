---
tags:
  - DAM
  - PSP
cssclasses:
  - dam-psp
  - table-compact-clean
banner: "![[psp.jpg]]"
banner_y: 0.25
---

# **TEMA 3.1.** <br>Programación de <br> Servicios y Procesos

## 1. Programación de <br>comunicaciones en red

Hoy en día, es impensable un dispositivo de procesamiento de información sin capacidad de comunicación. La mayoría de las aplicaciones necesitan conexión para instalarse, actualizarse o ejecutarse correctamente. Las redes permiten compartir recursos entre dispositivos, lo que ha llevado al desarrollo de aplicaciones distribuidas transparentes, donde el usuario no necesita preocuparse por la distribución de los procesos.

### 1.1. **Aspectos teóricos de la comunicación**

La comunicación implica la transferencia de información entre agentes independientes. Para que sea posible, los agentes deben compartir una forma común de representar la información, aunque internamente puedan manejarla de manera diferente. El mensaje, codificado de forma común, se transmite a través de un medio, siendo el agente que lo genera el emisor y el que lo recibe el receptor. Este proceso establece un canal de comunicación.

### 1.2. **Roles cliente y servidor**

El modelo clásico de comunicación es el cliente-servidor. El servidor contiene información que comparte con los clientes, quienes solicitan partes específicas de esa información. El servidor procesa las peticiones y envía las respuestas correspondientes. Actualmente, muchos dispositivos pueden actuar como clientes y servidores simultáneamente, lo que permite una mayor distribución de datos y procesos.

![](../../../_Media/Imágenes/PSP/03.1-ServidorCliente1.png)

<p class=pie-de-foto>Figura 1.2. Esquema de las tareas genéricas de los procesos servidor y cliente</p>

### 1.3. **Bases de la comunicación entre aplicaciones**

La comunicación en redes se basa en la transmisión de paquetes de información, similar al envío de cartas. Cada paquetes contiene datos necesarios para llegar a su destino, como la dirección IP y el puerto. Internet utiliza el protocolo IP para el direccionamiento y TCP para garantizar la integridad y el orden de los datos.

#### Arquitectura de Internet: una estructura de capas

La comunicación en Internet se estructura en capas: física, enlace, red, transporte y aplicación. Cada capa añade información adicional a los datos, como direcciones y controles, para asegurar su correcta transmisión. La capa de transporte, implementada solo en los dispositivos finales, garantiza la calidad de la transmisión mediante protocolos como TCP y UDP.

![](../../../_Media/Imágenes/PSP/03.1-capas.png)

<p class=pie-de-foto>Figura 1.3.1. Esquema de la arquitectura de capas de Internet</p>

#### Cabeceras y datos

Cada capa añade una cabecera a los datos, que contiene información específica para su gestión. En la recepción, estas cabeceras se eliminan progresivamente, dejando solo los datos originales para la aplicación.

![](../../../_Media/Imágenes/PSP/03.1-Encabezados-capas.png)
<p class=pie-de-foto>Figura 1.3.2. Esquema del traspaso de información entre capas</p>

#### Contenido de la información en cada capa

La capa de aplicación formatea los datos según el protocolo utilizado. La capa de transporte gestiona los puertos y la integridad de los datos. La capa de red se encarga del direccionamiento IP, mientras que la capa de enlace gestiona la transmisión física de los datos.

![](../../../_Media/Imágenes/PSP/03.1-Orden-capas.png)

### 1.4. **Elementos de programación de aplicaciones en red**

Los lenguajes de alto nivel, como Java, ofrecen bibliotecas para desarrollar aplicaciones distribuidas. Estas bibliotecas abstraen los detalles de las capas inferiores, permitiendo al programador centrarse en la lógica de la aplicación.

#### Direccionamiento (Clase `InetAddress`)

Java proporciona la clase `InetAddress` para gestionar direcciones IP de forma transparente, independientemente de si son IPv4 o IPv6. Los métodos como `getByName` y `getAllByName` permiten obtener instancias de `InetAddress` a partir de nombres de dominio o direcciones IP.

La clase `InetAddress` representa una dirección de Protocolo de Internet (IP), que es la base de protocolos como UDP y TCP. Una instancia de `InetAddress` contiene una dirección IP y, posiblemente, su nombre de host correspondiente (dependiendo de si se construyó con un nombre de host o si ya se realizó la resolución inversa de nombres).

##### Tipos de direcciones

| | |
|-|-|
| **Unicast**       | Identificador para una única interfaz. Un paquete enviado a una dirección unicast se entrega a la interfaz identificada por esa dirección. |
| **Dirección no especificada** | También llamada *anylocal* o *wildcard*. Nunca se asigna a ningún nodo. Indica la ausencia de una dirección. Se usa, por ejemplo, como destino en `bind`, permitiendo que un servidor acepte conexiones en cualquier interfaz. |
| **Dirección de loopback** | Asignada a la interfaz de loopback. Cualquier cosa enviada a esta dirección se devuelve como entrada IP en el host local. Se usa comúnmente para pruebas. |
| **Multicast**     | Identificador para un conjunto de interfaces (normalmente en diferentes nodos). Un paquete enviado a una dirección multicast se entrega a todas las interfaces identificadas por esa dirección. |

##### Alcance de las direcciones IP

| | |
|-|-|
| **Direcciones link-local**| Diseñadas para ser usadas en un solo enlace, como en la configuración automática de direcciones o cuando no hay routers presentes.|
| **Direcciones site-local**| Usadas dentro de un sitio sin necesidad de un prefijo global.|
| **Direcciones globales**| Únicas en toda Internet.|

##### Representación textual de direcciones IP

La representación textual de una dirección IP depende de la familia de direcciones. Para IPv4, consultar `Inet4Address#format`; para IPv6, consultar `Inet6Address#format`.

##### Resolución de nombres de host

La resolución de nombres de host a direcciones IP se realiza mediante la combinación de la configuración local del sistema y servicios de nombres como DNS (Domain Name System) o NIS (Network Information Service). La resolución inversa permite obtener el nombre de host asociado a una dirección IP.

La clase `InetAddress` proporciona métodos para resolver nombres de host a direcciones IP y viceversa.

##### Caché de `InetAddress`

La clase `InetAddress` utiliza una caché para almacenar tanto las resoluciones de nombres exitosas como las fallidas. Por defecto, cuando hay un administrador de seguridad instalado, las resoluciones exitosas se almacenan indefinidamente para proteger contra ataques de suplantación DNS. Sin un administrador de seguridad, las entradas se almacenan durante un tiempo limitado (dependiente de la implementación). Las resoluciones fallidas se almacenan durante un corto período (10 segundos) para mejorar el rendimiento.

Si el comportamiento por defecto no es deseado, se puede configurar un valor de TTL (Time-to-live) diferente mediante propiedades de seguridad de Java:

- **networkaddress.cache.ttl**: Controla el tiempo de caché para resoluciones exitosas. Un valor de `-1` indica "almacenar indefinidamente".
- **networkaddress.cache.negative.ttl**: Controla el tiempo de caché para resoluciones fallidas. Un valor de `0` indica "no almacenar", y `-1` indica "almacenar indefinidamente". El valor por defecto es 10 segundos.

#### Referencias remotas y obtención de recursos

Las aplicaciones pueden acceder a recursos remotos mediante URLs. Java ofrece las clases `URL` y `URLConnection` para trabajar con estos recursos. La clase `URLConnection` permite obtener flujos de entrada y salida, así como información adicional sobre el recurso, como su tipo y codificación.

![](../../../_Media/Imágenes/PSP/03.1-URLConnection.png)

<p class=pie-de-foto>Figura 1.4.2. Jerarquía de las clases que representan recursos remotos</p>

#### Sockets

Los sockets son la interfaz de programación que permite a dos aplicaciones intercambiar información a través de la red. En Java, los sockets pueden ser orientados a conexión (TCP) o no orientados a conexión (UDP). Los sockets TCP garantizan la integridad y el orden de los datos, mientras que los UDP son más rápidos pero menos fiables.

![](../../../_Media/Imágenes/PSP/03.1-Socket.png)

<p class=pie-de-foto>Figura 1.4.3 Jerarquía de clases para implementar sockets no orientados a conexión</p>

#### Implementación de sockets no orientados a conexión

Java ofrece las clases `DatagramSocket` y `DatagramPacket` para implementar comunicaciones UDP. Estas clases permiten enviar y recibir paquetes de datos sin establecer una conexión previa. La clase `MulticastSocket` extiende `DatagramSocket` para soportar comunicaciones multicast, donde un servidor envía datos a múltiples clientes.

![](../../../_Media/Imágenes/PSP/03.1-ServidorCliente2.png)

<p class=pie-de-foto>Figura 1.4.4. Diagrama de flujo del proceso de un servidor multicast</p>

#### Implementación de sockets orientados a conexión

Los sockets orientados a conexión utilizan el protocolo TCP. En Java, el servidor usa `ServerSocket` para escuchar peticiones de conexión, mientras que el cliente usa `Socket` para conectarse al servidor. Una vez establecida la conexión, ambos extremos pueden intercambiar datos mediante flujos de entrada y salida.

![](../../../_Media/Imágenes/PSP/03.1-SLLServerSocket.png)

<p class=pie-de-foto>Figura 1.4.5a. Jerarquía de clases para implementar sockets orientados a conexión</p>

![](../../../_Media/Imágenes/PSP/03.1-ServidorCliente3.png)

<p class=pie-de-foto>Figura 1.4.5b. Esquema del procedimiento seguido para conectar con un servidor TCP en Java</p>

**Ejemplo de implementación de un servidor TCP en Java**

```java
public class TcpSocketServer {
    static final int PORT = 8080;
    private boolean end = false;

    public void listen() {
        ServerSocket serverSocket = null;
        Socket clientSocket = null;
        try {
            serverSocket = new ServerSocket(PORT);
            while (!end) {
                clientSocket = serverSocket.accept();
                processClientRequest(clientSocket);
                closeClient(clientSocket);
            }
            if (serverSocket != null && !serverSocket.isClosed())
                serverSocket.close();
        } catch (IOException ex) {
            Logger.getLogger(TcpSocketServer.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    private void processClientRequest(Socket clientSocket) {
        boolean farewellMessage = false;
        String clientMessage = "";
        BufferedReader in = null;
        PrintStream out = null;
        try {
            in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            out = new PrintStream(clientSocket.getOutputStream());
            do {
                String dataToSend = processData(clientMessage);
                out.println(dataToSend);
                out.flush();
                clientMessage = in.readLine();
                farewellMessage = isFarewellMessage(clientMessage);
            } while (clientMessage != null && !farewellMessage);
        } catch (IOException ex) {
            Logger.getLogger(TcpSocketServer.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    private void closeClient(Socket clientSocket) {
        try {
            if (clientSocket != null && !clientSocket.isClosed()) {
                if (!clientSocket.isInputShutdown())
                    clientSocket.shutdownInput();
                if (!clientSocket.isOutputShutdown())
                    clientSocket.shutdownOutput();
                clientSocket.close();
            }
        } catch (IOException ex) {
            Logger.getLogger(TcpSocketServer.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
```

Este código muestra un servidor TCP que escucha en el puerto 8080, procesa las peticiones de los clientes y cierra la conexión adecuadamente.

**Ejemplo de implementación de un cliente TCP en Java**

El cliente TCP en Java utiliza la clase `Socket` para conectarse al servidor. A continuación, se muestra un ejemplo de cómo implementar un cliente que se comunica con el servidor TCP anterior.

```java
public class TcpSocketClient {
    public void connect(String address, int port) {
        String serverData;
        String request;
        boolean continueConnected = true;
        Socket socket = null;
        BufferedReader in = null;
        PrintStream out = null;

        try {
            socket = new Socket(InetAddress.getByName(address), port);
            in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            out = new PrintStream(socket.getOutputStream());

            while (continueConnected) {
                serverData = in.readLine();
                request = getRequest(serverData);
                out.println(request);
                out.flush();
                continueConnected = mustFinish(request);
            }
            close(socket);
        } catch (UnknownHostException ex) {
            reportError("Error de conexión. No existe el host", ex);
        } catch (IOException ex) {
            reportError("Error de conexión indefinido", ex);
        }
    }

    private String getRequest(String serverData) {
        // Procesa la respuesta del servidor y genera una nueva petición.
        return "Nueva petición basada en: " + serverData;
    }

    private boolean mustFinish(String request) {
        // Determina si la petición implica finalizar la conexión.
        return request.equals("FIN");
    }

    private void close(Socket socket) {
        try {
            if (socket != null && !socket.isClosed()) {
                if (!socket.isInputShutdown())
                    socket.shutdownInput();
                if (!socket.isOutputShutdown())
                    socket.shutdownOutput();
                socket.close();
            }
        } catch (IOException ex) {
            Logger.getLogger(TcpSocketClient.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    private void reportError(String message, Exception ex) {
        Logger.getLogger(TcpSocketClient.class.getName()).log(Level.SEVERE, message, ex);
    }
}
```

Este cliente se conecta al servidor en la dirección y puerto especificados. Luego, entra en un bucle donde recibe datos del servidor, genera una nueva petición basada en esos datos, y la envía de vuelta al servidor. El bucle continúa hasta que se recibe una señal de finalización.

### 1.5. **Comunicación segura con SSL**

Para comunicaciones seguras, Java ofrece las clases `SSLServerSocket` y `SSLSocket`, que extienden `ServerSocket` y `Socket` respectivamente. Estas clases implementan el protocolo SSL/TLS, que cifra la comunicación entre el cliente y el servidor.

**Ejemplo de servidor SSL:**

```java
public class SslSocketServer {
    static final int PORT = 8443;

    public void listen() {
        SSLServerSocketFactory factory = (SSLServerSocketFactory) SSLServerSocketFactory.getDefault();
        try (SSLServerSocket serverSocket = (SSLServerSocket) factory.createServerSocket(PORT)) {
            while (true) {
                try (SSLSocket clientSocket = (SSLSocket) serverSocket.accept()) {
                    processClientRequest(clientSocket);
                }
            }
        } catch (IOException ex) {
            Logger.getLogger(SslSocketServer.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    private void processClientRequest(SSLSocket clientSocket) {
        try (BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
             PrintStream out = new PrintStream(clientSocket.getOutputStream())) {
            String clientMessage = in.readLine();
            String response = "Respuesta segura: " + clientMessage;
            out.println(response);
            out.flush();
        } catch (IOException ex) {
            Logger.getLogger(SslSocketServer.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
```

**Ejemplo de cliente SSL:**

```java
public class SslSocketClient {
    public void connect(String address, int port) {
        SSLSocketFactory factory = (SSLSocketFactory) SSLSocketFactory.getDefault();
        try (SSLSocket socket = (SSLSocket) factory.createSocket(address, port)) {
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintStream out = new PrintStream(socket.getOutputStream());

            out.println("Petición segura");
            out.flush();
            String response = in.readLine();
            System.out.println("Respuesta del servidor: " + response);
        } catch (IOException ex) {
            Logger.getLogger(SslSocketClient.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
```

Estos ejemplos muestran cómo implementar un servidor y un cliente que utilizan SSL para cifrar la comunicación. El servidor escucha en el puerto 8443 y responde a las peticiones de los clientes de forma segura.

### 1.6. **Consideraciones finales**

La programación de servicios y procesos en red requiere un entendimiento claro de los protocolos de comunicación y las herramientas que los lenguajes de programación ofrecen para implementarlos. Java, con sus bibliotecas de red, proporciona una forma eficiente y segura de desarrollar aplicaciones distribuidas, ya sea utilizando TCP, UDP o SSL.

Al trabajar con sockets, es crucial manejar correctamente los recursos, como los flujos de entrada y salida, y asegurarse de que las conexiones se cierren adecuadamente para evitar fugas de recursos. Además, la elección entre TCP y UDP dependerá de los requisitos de la aplicación: TCP para comunicaciones fiables y UDP para transmisiones rápidas pero menos seguras.

En resumen, la programación de servicios en red es un área amplia y compleja, pero con las herramientas adecuadas y un enfoque estructurado, es posible desarrollar aplicaciones robustas y eficientes.

## 2. Programación de procesos y servicios

Además de la comunicación en red, la programación de servicios y procesos implica gestionar la ejecución de tareas concurrentes y paralelas. Esto es especialmente importante en aplicaciones que requieren manejar múltiples solicitudes simultáneamente, como servidores web o sistemas de procesamiento de datos.

### 2.1. **Concurrencia y paralelismo**

La **concurrencia** se refiere a la capacidad de un sistema para manejar múltiples tareas aparentemente al mismo tiempo, aunque no necesariamente se ejecuten en paralelo. El **paralelismo**, por otro lado, implica la ejecución simultánea de tareas en múltiples núcleos de CPU.

En Java, la concurrencia se maneja principalmente mediante **hilos** (threads). Un hilo es una unidad de ejecución independiente dentro de un proceso. Java proporciona la clase `Thread` y la interfaz `Runnable` para crear y gestionar hilos.

**Ejemplo básico de creación de hilos en Java:**

```java
public class SimpleThread extends Thread {
    @Override
    public void run() {
        System.out.println("Hilo ejecutándose: " + Thread.currentThread().getName());
    }

    public static void main(String[] args) {
        SimpleThread thread1 = new SimpleThread();
        SimpleThread thread2 = new SimpleThread();
        thread1.start();
        thread2.start();
    }
}
```

En este ejemplo, se crean dos hilos que ejecutan el método `run()` de forma concurrente. Cada hilo imprime su nombre en la consola.

### 2.2. **Gestión de hilos con Executors**

Para gestionar hilos de manera más eficiente, Java ofrece el framework **Executor**, que permite manejar un grupo de hilos (thread pool) y asignar tareas a ellos. Esto evita la sobrecarga de crear y destruir hilos constantemente.

**Ejemplo de uso de ExecutorService:**

```java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ExecutorExample {
    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(2);

        Runnable task1 = () -> System.out.println("Tarea 1 ejecutada por: " + Thread.currentThread().getName());
        Runnable task2 = () -> System.out.println("Tarea 2 ejecutada por: " + Thread.currentThread().getName());

        executor.submit(task1);
        executor.submit(task2);

        executor.shutdown();
    }
}
```

En este ejemplo, se crea un pool de 2 hilos utilizando `Executors.newFixedThreadPool(2)`. Las tareas se asignan al pool mediante el método `submit()`. Finalmente, se cierra el pool con `shutdown()`.

### 2.3. **Sincronización de hilos**

Cuando varios hilos acceden a recursos compartidos, es necesario sincronizarlos para evitar condiciones de carrera (race conditions). Java proporciona mecanismos como **synchronized** y **locks** para garantizar que solo un hilo acceda a un recurso compartido a la vez.

**Ejemplo de sincronización con `synchronized`:**

```java
public class Counter {
    private int count = 0;

    public synchronized void increment() {
        count++;
    }

    public int getCount() {
        return count;
    }
}

public class SynchronizedExample {
    public static void main(String[] args) throws InterruptedException {
        Counter counter = new Counter();

        Runnable task = () -> {
            for (int i = 0; i < 1000; i++) {
                counter.increment();
            }
        };

        Thread thread1 = new Thread(task);
        Thread thread2 = new Thread(task);

        thread1.start();
        thread2.start();

        thread1.join();
        thread2.join();

        System.out.println("Contador final: " + counter.getCount());
    }
}
```

En este ejemplo, el método `increment()` está sincronizado, lo que garantiza que solo un hilo pueda incrementar el contador a la vez. Esto evita que ambos hilos modifiquen el valor de `count` simultáneamente.

### 2.4. **Futuros y Callables**

Java también ofrece la interfaz `Callable`, que es similar a `Runnable`, pero puede devolver un resultado y lanzar excepciones. Los resultados de las tareas `Callable` se pueden obtener mediante objetos `Future`.

**Ejemplo de uso de `Callable` y `Future`:**

```java
import java.util.concurrent.*;

public class CallableExample {
    public static void main(String[] args) throws ExecutionException, InterruptedException {
        ExecutorService executor = Executors.newSingleThreadExecutor();

        Callable<String> task = () -> {
            Thread.sleep(1000);
            return "Resultado de la tarea";
        };

        Future<String> future = executor.submit(task);

        System.out.println("Esperando resultado...");
        String result = future.get();
        System.out.println("Resultado: " + result);

        executor.shutdown();
    }
}
```

En este ejemplo, se crea una tarea `Callable` que devuelve un resultado después de un retraso de 1 segundo. El resultado se obtiene mediante `future.get()`, que bloquea la ejecución hasta que la tarea esté completa.

## 3. Servicios y daemons

En aplicaciones de larga duración, como servidores, es común utilizar **daemons** o servicios que se ejecutan en segundo plano. En Java, los hilos pueden marcarse como daemons utilizando el método `setDaemon(true)`.

**Ejemplo de hilo daemon:**

```java
public class DaemonThreadExample {
    public static void main(String[] args) {
        Thread daemonThread = new Thread(() -> {
            while (true) {
                System.out.println("Daemon ejecutándose...");
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });

        daemonThread.setDaemon(true);
        daemonThread.start();

        System.out.println("Hilo principal finalizado.");
    }
}
```

En este ejemplo, el hilo daemon continúa ejecutándose en segundo plano incluso después de que el hilo principal haya finalizado. Sin embargo, cuando todos los hilos no daemon terminan, la JVM finaliza, deteniendo también los hilos daemon.

## 4. Consideraciones finales

La programación de servicios y procesos en Java implica gestionar la concurrencia, la sincronización y la ejecución de tareas en segundo plano. Utilizando herramientas como hilos, Executors, y mecanismos de sincronización, es posible desarrollar aplicaciones robustas y eficientes que manejen múltiples tareas simultáneamente.

Además, es importante considerar el uso de hilos daemon para tareas de fondo y servicios que deben ejecutarse continuamente. Sin embargo, siempre se debe tener en cuenta la gestión adecuada de recursos y la finalización correcta de los hilos para evitar problemas como fugas de memoria o bloqueos.

En resumen, la programación de servicios y procesos en Java es un área amplia que requiere un buen entendimiento de los conceptos de concurrencia y paralelismo, así como de las herramientas que el lenguaje ofrece para manejarlos. Con un enfoque estructurado y un uso adecuado de las bibliotecas de Java, es posible desarrollar aplicaciones escalables y eficientes.
