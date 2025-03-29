---
tags: [DAM, PSP]
cssclasses:
  - dam-psp
  - table-compact-clean
banner: "![[psp.jpg]]"
banner_y: 0.26
---

# Guion **PSP03**

## 1. Pasos para crear el proyecto con Maven

1. **Crear el proyecto Maven**  
	En tu IDE favorito (por ejemplo, IntelliJ IDEA o Eclipse):
	
	- Selecciona la opción para crear un nuevo proyecto Maven.
	- Configura el archivo `pom.xml` con las dependencias necesarias.
2. **Estructura básica del proyecto**  
	Maven crea automáticamente la estructura básica:

	```
    src/
    ├── main/
    │   ├── java/
    │   │   └── com.tuchat/          # Paquete base
    │   │       ├── Server.java      # Código del servidor
    │   │       ├── Client.java      # Código del cliente
    │   │       └── Utils.java       # Clases auxiliares, si es necesario
    │   └── resources/               # Archivos de configuración, si los necesitas
    └── test/
    ```

3. **Archivo `pom.xml`**  
	Añade las dependencias básicas. Por ejemplo:

	```xml
    <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
        <modelVersion>4.0.0</modelVersion>
        <groupId>com.tuchat</groupId>
        <artifactId>MultiuserChat</artifactId>
        <version>1.0-SNAPSHOT</version>
    
        <dependencies>
            <!-- Dependencias adicionales opcionales -->
            <dependency>
                <groupId>org.slf4j</groupId>
                <artifactId>slf4j-api</artifactId>
                <version>2.0.9</version>
            </dependency>
            <dependency>
                <groupId>org.slf4j</groupId>
                <artifactId>slf4j-simple</artifactId>
                <version>2.0.9</version>
            </dependency>
        </dependencies>
    </project>
    ```

## 2. Implementación del Servidor

1. **Clase `Server`**

	```java
    package com.tuchat;
    
    import java.io.*;
    import java.net.*;
    import java.util.*;
    import java.util.concurrent.*;
    
    public class Server {
        private static final int TCP_PORT = 5000;
        private static final int UDP_PORT = 5001;
        private static Map<String, ClientHandler> clients = new ConcurrentHashMap<>();
        private static DatagramSocket udpSocket;
    
        public static void main(String[] args) {
            try (ServerSocket serverSocket = new ServerSocket(TCP_PORT)) {
                udpSocket = new DatagramSocket();
                System.out.println("Servidor iniciado en el puerto " + TCP_PORT);
    
                while (true) {
                    Socket clientSocket = serverSocket.accept();
                    ClientHandler clientHandler = new ClientHandler(clientSocket);
                    new Thread(clientHandler).start();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    
        public static void broadcast(String message, String sender) {
            clients.forEach((name, handler) -> {
                if (!name.equals(sender)) {
                    handler.sendMessage(message);
                }
            });
        }
    
        public static void notifyClients(String notification) {
            byte[] data = notification.getBytes();
            clients.forEach((name, handler) -> {
                try {
                    InetAddress address = handler.getAddress();
                    int port = handler.getUdpPort();
                    DatagramPacket packet = new DatagramPacket(data, data.length, address, port);
                    udpSocket.send(packet);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            });
        }
    
        static class ClientHandler implements Runnable {
            private Socket socket;
            private PrintWriter out;
            private String name;
            private InetAddress address;
            private int udpPort;
    
            public ClientHandler(Socket socket) {
                this.socket = socket;
            }
    
            public InetAddress getAddress() {
                return address;
            }
    
            public int getUdpPort() {
                return udpPort;
            }
    
            @Override
            public void run() {
                try (
                    InputStream input = socket.getInputStream();
                    BufferedReader reader = new BufferedReader(new InputStreamReader(input));
                    OutputStream output = socket.getOutputStream();
                    PrintWriter writer = new PrintWriter(output, true)
                ) {
                    this.out = writer;
    
                    // Solicitar nombre del cliente
                    writer.println("Introduce tu nombre:");
                    this.name = reader.readLine();
                    this.address = socket.getInetAddress();
                    this.udpPort = Integer.parseInt(reader.readLine());
    
                    clients.put(name, this);
                    System.out.println(name + " se ha conectado.");
                    notifyClients("NOTIFICACIÓN: " + name + " se ha unido al chat.");
    
                    String message;
                    while ((message = reader.readLine()) != null) {
                        broadcast(name + ": " + message, name);
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                } finally {
                    disconnect();
                }
            }
    
            public void sendMessage(String message) {
                out.println(message);
            }
    
            private void disconnect() {
                try {
                    clients.remove(name);
                    socket.close();
                    notifyClients("NOTIFICACIÓN: " + name + " se ha desconectado.");
                    System.out.println(name + " se ha desconectado.");
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
    ```

## 3. Implementación del Cliente

2. **Clase `Client`**

	```java
    package com.tuchat;
    
    import java.io.*;
    import java.net.*;
    
    public class Client {
        private static final String SERVER_ADDRESS = "localhost";
        private static final int TCP_PORT = 5000;
        private static final int UDP_PORT = 5001;
    
        public static void main(String[] args) {
            try (
                Socket socket = new Socket(SERVER_ADDRESS, TCP_PORT);
                BufferedReader consoleReader = new BufferedReader(new InputStreamReader(System.in));
                PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);
                BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()))
            ) {
                System.out.println("Conectado al servidor.");
    
                // Enviar nombre y puerto UDP
                System.out.print("Introduce tu nombre: ");
                String name = consoleReader.readLine();
                writer.println(name);
                writer.println(UDP_PORT);
    
                // Hilo para recibir mensajes
                new Thread(() -> {
                    try {
                        String serverMessage;
                        while ((serverMessage = reader.readLine()) != null) {
                            System.out.println(serverMessage);
                        }
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }).start();
    
                // Hilo para recibir notificaciones UDP
                new Thread(() -> {
                    try (DatagramSocket udpSocket = new DatagramSocket(UDP_PORT)) {
                        byte[] buffer = new byte[1024];
                        while (true) {
                            DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
                            udpSocket.receive(packet);
                            String notification = new String(packet.getData(), 0, packet.getLength());
                            System.out.println(notification);
                        }
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }).start();
    
                // Enviar mensajes al servidor
                String message;
                while ((message = consoleReader.readLine()) != null) {
                    writer.println(message);
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
    ```
