# Guía de Implementación - Sistema de Chat Multiusuario

Esta guía detalla los pasos seguidos para implementar el sistema de chat multiusuario según los requisitos especificados en la tarea PSP03 y siguiendo los conceptos teóricos de comunicaciones en red.

## 1. Estructura del Proyecto

Se ha creado un proyecto Maven con la siguiente estructura:

```
MultiuserChat/
├── src/
│   └── main/
│       └── java/
│           └── com/
│               └── tuchat/
│                   ├── Server.java     # Implementación del servidor
│                   ├── Client.java     # Implementación del cliente
│                   └── Utils.java      # Clases auxiliares
└── pom.xml                            # Configuración de Maven
```

## 2. Implementación del Servidor (Server.java)

El servidor implementa las siguientes funcionalidades siguiendo el modelo teórico:

- **Gestión de conexiones TCP**: Utiliza `ServerSocket` para aceptar conexiones de clientes, como se muestra en la teoría de sockets TCP.
- **Manejo concurrente de clientes**: Cada cliente es gestionado por un hilo independiente (`ClientHandler`), siguiendo el patrón de servidor concurrente explicado en el tema 3.2.
- **Broadcast de mensajes**: Reenvía los mensajes recibidos a todos los clientes conectados.
- **Notificaciones UDP**: Envía notificaciones cuando un cliente se conecta o desconecta utilizando `DatagramSocket` y `DatagramPacket`, como se explica en la teoría de sockets UDP.
- **Mensajes privados**: Permite el envío de mensajes entre usuarios específicos.
- **Sistema de logs**: Registra todas las interacciones en un archivo de log.

### Características técnicas implementadas:

- Uso de `DataInputStream` y `DataOutputStream` para la comunicación, siguiendo los ejemplos de la teoría.
- Verificación de nombres de usuario duplicados.
- Comandos para listar usuarios conectados.
- Sistema de mensajes privados.
- Registro detallado de actividad con marcas de tiempo.

## 3. Implementación del Cliente (Client.java)

El cliente implementa:

- **Conexión TCP**: Se conecta al servidor mediante un socket TCP, como se muestra en los ejemplos teóricos.
- **Hilos separados**: Utiliza hilos independientes para enviar mensajes, recibir mensajes y recibir notificaciones UDP.
- **Interfaz de consola**: Proporciona una interfaz sencilla para interactuar con el sistema.
- **Comandos especiales**: Implementa comandos como `/usuarios`, `/privado` y `/salir`.
- **Recepción de notificaciones UDP**: Escucha en un puerto UDP para recibir notificaciones del servidor, siguiendo el modelo de comunicación UDP explicado en la teoría.

### Características técnicas implementadas:

- Uso de `DataInputStream` y `DataOutputStream` para la comunicación TCP.
- Uso de `DatagramSocket` y `DatagramPacket` para la comunicación UDP.
- Personalización del puerto UDP.
- Interfaz de usuario mejorada con prompt y comandos.
- Manejo de errores y desconexiones.

## 4. Clase de Utilidades (Utils.java)

Se ha creado una clase de utilidades que proporciona:

- Formateo de marcas de tiempo.
- Formateo de mensajes de chat.
- Funciones para solicitar entrada al usuario.

## 5. Configuración Maven (pom.xml)

El archivo `pom.xml` configura:

- Dependencias necesarias (SLF4J para logging).
- Plugins para compilación.
- Configuración para generar JARs ejecutables tanto para el servidor como para el cliente.

## 6. Protocolo de Comunicación

Se ha implementado el protocolo de comunicación especificado:

- **Mensajes TCP**: Utilizando `DataInputStream.writeUTF()` y `DataOutputStream.readUTF()` para enviar y recibir mensajes.
- **Notificaciones UDP**: `NOTIFICACIÓN: [NombreUsuario] se ha unido/desconectado del chat`.
- **Comandos especiales**: Comienzan con `/` y tienen una sintaxis específica.

## 7. Extensiones Implementadas

Se han implementado las extensiones opcionales mencionadas en la tarea:

- **Mensajes privados**: Mediante el comando `/privado <usuario> <mensaje>`.
- **Sistema de logs**: El servidor mantiene un registro detallado de todas las interacciones.

## 8. Compilación y Ejecución

### Compilación con Maven

Para compilar el proyecto y generar los archivos JAR ejecutables:

```bash
cd MultiuserChat
mvn clean package
```

Este comando generará dos archivos JAR en el directorio `target`:
- `server-jar-with-dependencies.jar` - Servidor
- `client-jar-with-dependencies.jar` - Cliente

### Ejecución del Servidor

Para iniciar el servidor:

```bash
java -jar target/server-jar-with-dependencies.jar
```

El servidor se iniciará en el puerto TCP 5000 y UDP 5001 por defecto.

### Ejecución del Cliente

Para iniciar un cliente:

```bash
java -jar target/client-jar-with-dependencies.jar
```

Sigue las instrucciones en pantalla para conectarte al servidor.

## 9. Relación con la Teoría

La implementación se basa directamente en los conceptos teóricos explicados en los documentos:

### Modelo Cliente/Servidor
- Se implementa el paradigma cliente/servidor explicado en el TEMA 3.2, donde el servidor actúa como back-end gestionando recursos y el cliente como front-end interactuando con el usuario.

### Sockets TCP
- Se utilizan sockets TCP para la comunicación principal, siguiendo el modelo explicado en el TEMA 3, con `ServerSocket` para el servidor y `Socket` para los clientes.
- Los flujos de datos se gestionan mediante `DataInputStream` y `DataOutputStream`, como se muestra en los ejemplos teóricos.

### Sockets UDP
- Se implementan datagramas UDP para las notificaciones, utilizando `DatagramSocket` y `DatagramPacket` como se explica en el TEMA 3.
- El servidor envía notificaciones UDP a todos los clientes cuando hay cambios en la conexión.

### Concurrencia
- Se utiliza el modelo de servidor concurrente explicado en el TEMA 3.2, donde cada cliente es atendido por un hilo independiente.
- La clase `ClientHandler` extiende `Runnable` para ejecutarse en un hilo separado.

### Optimización
- Se implementan técnicas de optimización como el manejo adecuado de excepciones y el cierre correcto de recursos.
- Se utiliza `ConcurrentHashMap` para gestionar de forma segura la lista de clientes conectados.

## 10. Pruebas Realizadas

El sistema ha sido diseñado para soportar:

- Múltiples clientes conectados simultáneamente.
- Envío y recepción de mensajes en tiempo real.
- Conexiones y desconexiones sin afectar la estabilidad del servidor.
- Manejo adecuado de errores y situaciones excepcionales.

## 11. Conclusiones

La implementación cumple con todos los requisitos funcionales y no funcionales especificados en la tarea PSP03, siguiendo fielmente los conceptos teóricos de comunicaciones en red. El sistema es robusto, escalable y fácil de usar, proporcionando una base sólida que podría extenderse con funcionalidades adicionales en el futuro.
