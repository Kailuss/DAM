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

# **TEMA 3.** <br>Comunicaciones en Red

| Anexos |
| ------ |
| [**TEMA 3.1.** Ampliación de conceptos](TEMA%203.1.%20Ampliación%20de%20conceptos.md) |
| [**TEMA 3.2.** Aplicaciones cliente-servidor](TEMA%203.2.%20Aplicaciones%20cliente-servidor.md) |
| [Tarea PSP03](../Práctica/Tarea%20PSP03.md) |
| [Guion PSP03](../Práctica/Guion%20PSP03.md) |

## 1. Conexiones TCP/IP 

En 1969, ARPA (Advanced Research Projects Agency) del Departamento de Defensa de EE. UU. inició un proyecto para conectar ordenadores mediante redes telefónicas. Diseñado en plena Guerra Fría, el objetivo era garantizar la comunicación entre nodos incluso si parte de la red quedaba destruida. Esto dio lugar en 1972 a ARPAnet, la primera red de conmutación de paquetes, caracterizada por su fiabilidad gracias a topologías malladas y múltiples líneas punto a punto.

El crecimiento de ARPAnet y la incorporación de nuevas tecnologías (radio y satélite) plantearon problemas de interoperabilidad, resolviéndose con el desarrollo del modelo TCP/IP, una pila de protocolos que permitió crear Internet. A diferencia del modelo OSI, donde se definieron cuidadosamente capas y servicios antes de los protocolos, TCP/IP nació de una práctica más pragmática: primero se desarrollaron los protocolos y luego se definió el modelo, resultando en una arquitectura más simple pero específica para su propia red.

El modelo TCP/IP consta de cuatro capas:

- **Capa Host-Red.** Conecta el equipo con la red, transforma información en impulsos físicos y utiliza direcciones MAC para el direccionamiento físico.
- **Capa de Red.** Permite enviar paquetes entre redes mediante el protocolo IP, gestionando encaminamiento y evitando congestión. Utiliza direccionamiento lógico (IP).
- **Capa de Transporte.** Facilita la comunicación entre equipos con protocolos como TCP (orientado a conexión y fiable) y UDP (no orientado a conexión y más rápido). Realiza el direccionamiento por puertos.
- **Capa de Aplicación.** Combina funcionalidades de las capas superiores del modelo OSI, incluyendo protocolos como HTTP, FTP y TELNET.

![Capas Modelo TCP/IP](../../../_Media/Imágenes/PSP/03-Capas-Modelo-TCP-IP.png)

### 1.1. **Conexiones TCP/UDP**

La capa de transporte establece reglas para conectar dispositivos, organizando los paquetes desordenados recibidos de la capa de red en un flujo coherente. Se encarga de transferir datos sin errores entre equipos.

Existen dos tipos de conexiones:

- **TCP (Transmission Control Protocol).** Protocolo fiable y orientado a conexión, que fragmenta y reensambla mensajes. Incluye control de flujo para evitar saturación.
- **UDP (User Datagram Protocol).** Protocolo sin conexión, más rápido pero menos fiable, ideal para aplicaciones como transmisión en tiempo real, donde los retrasos son críticos.

La elección entre TCP o UDP depende de las necesidades específicas de la aplicación.

### 1.2. **Puertos de Comunicación**

Los puertos permiten que las aplicaciones se comuniquen identificando el servicio específico en el equipo destino. Según la IANA, los puertos se clasifican en:

| | | |
| - | - | - |
|**Puertos conocidos** | 0-1023 | Reservados para servicios estándar (ej. HTTP, FTP). | 
|**Puertos registrados** | 1024-49151 | Asignados a servicios o aplicaciones específicas. | 
|**Puertos dinámicos** | 49152-65535 | Utilizados para conexiones temporales entre aplicaciones. | 

Las aplicaciones suelen emplear puertos en el rango 1024-49151.

### 1.3. **Nombres en Internet**

Aunque los equipos se identifican mediante direcciones IP, se prefieren nombres más fáciles de recordar (ej. [www.mec.es](http://www.mec.es/)). El sistema DNS (Domain Name System) asocia nombres a direcciones IP, facilitando la comunicación y permitiendo cambios de máquina sin afectar las referencias.

DNS utiliza servidores jerárquicos para resolver nombres, combinando centralización para sincronización y descentralización para flexibilidad.

### 1.4. **Modelos de Comunicaciones**

El modelo **Cliente/Servidor** es el más usado en informática, con servidores que ofrecen servicios y clientes que los consumen (ej. servidores web y navegadores).

El **Modelo de Información Distribuido** amplía este esquema, permitiendo que los equipos actúen como clientes y servidores simultáneamente, interactuando para compartir recursos y realizar tareas. Aunque externamente funciona como cliente/servidor, internamente distribuye funciones entre sus componentes.

## 2. Sockets TCP

### 2.1. **Introducción**

Los **sockets** permiten la comunicación entre procesos en diferentes equipos de una red. Un socket es un punto por el cual un proceso puede enviar o recibir datos.

Existen dos protocolos principales:

- **TCP.** Orientado a la conexión, asegura la entrega fiable de datos.
- **UDP.** No orientado a conexión, prioriza la velocidad sobre la fiabilidad.

Esta sección aborda los **sockets TCP**, en los que el servidor usa un puerto (normalmente entre 1 y 1023) para recibir solicitudes de clientes. Tras establecer la conexión, cada comunicación cliente-servidor utiliza un socket único con puertos dinámicos (49152-65535).

### 2.2. **Servidor**

Pasos para establecer comunicación:

- **Publicar puerto.** Se usa `ServerSocket` indicando el puerto.

	```java
    ServerSocket skServidor = new ServerSocket(Puerto);
    ```

- **Esperar cliente.** El servidor queda a la espera con `accept()`. Cuando un cliente se conecta, se crea un socket para la comunicación:

	```java
    Socket sCliente = skServidor.accept();
    ```

- **Enviar y recibir datos.** Se crean flujos de entrada y salida para intercambiar información.
- **Cerrar conexión.** El socket se cierra tras finalizar la comunicación:

	```java
    sCliente.close();
    ```

**Ejemplo de servidor.**

```java
import java.io.* ;
import java.net.* ;
class Servidor {
    static final int Puerto=2000;
    public Servidor() {
        try {
            ServerSocket skServidor = new ServerSocket(Puerto);
            System.out.println("Escucho el puerto " + Puerto);
            Socket sCliente = skServidor.accept(); 
            sCliente.close();
        } catch(Exception e) {
            System.out.println(e.getMessage());
        }
    }
    public static void main(String[] arg) {
        new Servidor();
    }
}
```

### 2.3. **Cliente**

Pasos para establecer comunicación:

- **Conexión al servidor.** Se usa `Socket` indicando la dirección del servidor y el puerto:

	```java
    Socket sCliente = new Socket(Host, Puerto);
    ```

- **Enviar y recibir datos.** Se crean flujos de entrada y salida.
- **Cerrar conexión.** El socket se cierra tras finalizar la comunicación:

	```java
    sCliente.close();
    ```

**Ejemplo de cliente.**

```java
import java.io.*;
import java.net.*;
class Cliente {
    static final String Host = "localhost";
    static final int Puerto=2000;
    public Cliente() {
        try {
            Socket sCliente = new Socket(Host, Puerto);
            sCliente.close();
        } catch(Exception e) {
            System.out.println(e.getMessage());
        }
    }
    public static void main(String[] arg) {
        new Cliente();
    }
}
```

### 2.4. **Flujos de entrada y salida**

Para intercambiar datos se usan flujos. Ejemplo de flujo de salida:

```java
OutputStream aux = sCliente.getOutputStream();
DataOutputStream flujo_salida = new DataOutputStream(aux);
flujo_salida.writeUTF("Enviar datos");
```

Ejemplo de flujo de entrada:

```java
InputStream aux = sCliente.getInputStream();
DataInputStream flujo_entrada = new DataInputStream(aux);
String datos = flujo_entrada.readUTF();
```

### 2.5. **Ejemplo completo**

**Servidor que atiende a 3 clientes secuencialmente.**

```java
class Servidor {
    static final int Puerto = 2000;
    public Servidor() {
        try {
            ServerSocket skServidor = new ServerSocket(Puerto);
            for (int nCli = 0; nCli < 3; nCli++) {
                Socket sCliente = skServidor.accept();
                OutputStream aux = sCliente.getOutputStream();
                DataOutputStream flujo_salida = new DataOutputStream(aux);
                flujo_salida.writeUTF("Hola cliente " + nCli);
                sCliente.close();
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
    public static void main(String[] arg) {
        new Servidor();
    }
}
```

**Cliente que se conecta al servidor.**

```java
class Cliente {
    static final String HOST = "localhost";
    static final int Puerto = 2000;
    public Cliente() {
        try {
            Socket sCliente = new Socket(HOST, Puerto);
            InputStream aux = sCliente.getInputStream();
            DataInputStream flujo_entrada = new DataInputStream(aux);
            System.out.println(flujo_entrada.readUTF());
            sCliente.close();
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
    public static void main(String[] arg) {
        new Cliente();
    }
}
```

**Compilación y ejecución.**

- Compilar:

	``` bash
    javac Servidor.java Cliente.java
    ```

- Ejecutar:

	``` bash
    java Servidor
    java Cliente
    ```

Este ejemplo muestra cómo un servidor atiende a tres clientes secuencialmente, enviándoles un mensaje.

## 3. Sockets UDP

Los sockets UDP no establecen conexión como los TCP; permiten enviar y recibir mensajes mediante una dirección IP y un puerto. Sin embargo, no garantizan la entrega de los mensajes. En Java, la clase `DatagramSocket` gestiona los sockets UDP, y los mensajes se manejan con `DatagramPacket`. Los paquetes incluyen el mensaje, su longitud, el equipo destinatario y el puerto.

### 3.1. **Receptor**

Para iniciar un socket UDP en un puerto específico:

```java
DatagramSocket sSocket = new DatagramSocket(puerto);
```

Para recibir mensajes:

- Se crea un espacio para el mensaje:

	```java
    byte[] cadena = new byte[1000];
    DatagramPacket mensaje = new DatagramPacket(cadena, cadena.length);
    ```

- El socket recibe el mensaje:

	```java
    sSocket.receive(mensaje);
    ```

- Se muestra el contenido:

	```java
    String datos = new String(mensaje.getData(), 0, mensaje.getLength());
    System.out.println("\tMensaje Recibido: " + datos);
    ```

- Se cierra el socket al finalizar:

	```java
    sSocket.close();
    ```

### 3.2. **Emisor**

Para enviar mensajes UDP:

- Inicializar el socket:

	```java
    DatagramSocket sSocket = new DatagramSocket();
    ```

- Crear el mensaje especificando contenido, longitud, equipo y puerto:

	```java
    InetAddress equipo = InetAddress.getByName("localhost");
    DatagramPacket mensaje = new DatagramPacket(mensajeBytes, mensajeBytes.length, equipo, puerto);
    ```

- Enviar el mensaje:

	```java
    sSocket.send(mensaje);
    ```

- Cerrar el socket:

	```java
    sSocket.close();
    ```

### 3.3. **Ejemplo**

**Objetivo.** Crear dos procesos, `ReceptorUDP` y `EmisorUDP`, para intercambiar mensajes a través del puerto 1500.

#### ReceptorUDP.java

```java
import java.net.*;
import java.io.*;

public class ReceptorUDP {
    public static void main(String[] args) {
        if (args.length != 0) {
            System.err.println("Uso: java ReceptorUDP");
        } else try {
            DatagramSocket sSocket = new DatagramSocket(1500);
            byte[] cadena = new byte[1000];
            DatagramPacket mensaje = new DatagramPacket(cadena, cadena.length);
            System.out.println("Esperando mensajes...");
            
            while (true) {
                sSocket.receive(mensaje);
                String datos = new String(mensaje.getData(), 0, mensaje.getLength());
                System.out.println("\tMensaje Recibido: " + datos);
            }
        } catch (Exception e) {
            System.err.println(e.getMessage());
        }
    }
}
```

#### EmisorUDP.java

```java
import java.net.*;
import java.io.*;

public class EmisorUDP {
    public static void main(String[] args) {
        if (args.length != 2) {
            System.err.println("Uso: java EmisorUDP <equipo> <mensaje>");
        } else try {
            DatagramSocket sSocket = new DatagramSocket();
            InetAddress maquina = InetAddress.getByName(args[0]);
            int puerto = 1500;

            byte[] cadena = args[1].getBytes();
            DatagramPacket mensaje = new DatagramPacket(cadena, cadena.length, maquina, puerto);
            sSocket.send(mensaje);
            sSocket.close();
        } catch (Exception e) {
            System.err.println(e.getMessage());
        }
    }
}
```

### 3.4. **Prueba**

- Compilar ambos programas:

	```bash
    javac ReceptorUDP.java
    javac EmisorUDP.java
    ```

- Ejecutar el receptor en un terminal:

	```bash
    java ReceptorUDP
    ```

- En otro terminal, ejecutar el emisor:

	```bash
    java EmisorUDP <equipo> <mensaje>
    ```

	Por ejemplo:

	```bash
    java EmisorUDP localhost hola
    ```
