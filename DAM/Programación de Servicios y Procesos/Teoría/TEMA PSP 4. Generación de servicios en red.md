---
tags: [DAM, PSP]
cssclasses: [dam-psp, table-compact-clean]
banner: "![[psp.jpg]]"
banner_y: 0.32
---

# **TEMA 4.** <br>Generación de servicios en red


| Anexos    |
| --- |
| [Tarea PSP04](../Práctica/Tarea%20PSP04.md)    |
| [Guion PSP04](../Práctica/Guion%20PSP04.md)    |


## 1. Introducción

Una red de ordenadores es un sistema de comunicaciones que conecta equipos informáticos entre sí, permitiendo compartir información y recursos. Esto mejora el rendimiento global del sistema y ofrece ventajas como:

- **Reducción de costos.** Menor presupuesto en software y hardware.
- **Organización de grupos de trabajo.** Facilita la colaboración.
- **Mejora en la administración.** Simplifica la gestión de equipos y aplicaciones.
- **Integridad y seguridad de los datos.** Protege la información y controla el acceso.
- **Facilidad de comunicación.** Permite una comunicación eficiente entre usuarios.

Los servicios en red son programas que proporcionan funcionalidades basadas en protocolos y estándares. Estos servicios se clasifican según su finalidad:

- **Administración/Configuración.** Facilitan la gestión de equipos (ej. DHCP para asignación de direcciones IP, DNS para resolución de nombres).
- **Acceso y control remoto.** Permiten conexiones remotas (ej. Telnet, SSH).
- **Ficheros.** Ofrecen almacenamiento y transferencia de archivos (ej. FTP).
- **Impresión.** Comparten impresoras de forma remota.
- **Información.** Sirven contenidos o datos (ej. HTTP para páginas web, bases de datos).
- **Comunicación.** Facilitan la comunicación entre usuarios (ej. SMTP para correo electrónico).

## 2. Protocolos de comunicaciones <br>del nivel de aplicación

El modelo TCP/IP es fundamental para la comunicación en red, especialmente en Internet. La capa de Aplicación, la más alta en la jerarquía TCP/IP, define los protocolos que usan las aplicaciones para intercambiar datos. Algunos protocolos clave son:

| **Protocolo** | **Función** |
|---------------|-------------|
| FTP           | Transferencia de ficheros. |
| Telnet        | Acceso remoto a máquinas mediante un intérprete de comandos. |
| SMTP          | Transferencia de correo electrónico. |
| HTTP          | Transferencia de hipertexto (páginas web). |
| SSH           | Gestión remota segura. |
| DNS           | Traducción de nombres de dominio a direcciones IP. |
| NNTP          | Transferencia de noticias en redes. |
| IRC           | Chat basado en Internet. |

### 2.1. **Comunicación entre aplicaciones**

El modelo cliente/servidor es la base de TCP/IP. El cliente solicita servicios, mientras que el servidor los proporciona. La comunicación se realiza a través de protocolos de aplicación, como HTTP para la web. Por ejemplo:

1. Un usuario introduce una URL en un navegador (cliente).
2. El navegador solicita la página al servidor mediante el protocolo HTTP.
3. El servidor responde enviando la página web al cliente.
4. El navegador muestra la página al usuario.

Este proceso sigue un diálogo estructurado, como:

- Cliente: `GET /organizacion.htm HTTP/1.0`
- Servidor: `HTTP/1.0 200 OK` (envía la página).

### 2.2. **Conexión, transmisión y desconexión**

Los protocolos de aplicación se comunican con el nivel de transporte mediante sockets, que representan conexiones entre equipos. En Java, esto se implementa con las clases `Socket` y `ServerSocket` del paquete `java.net`. Los pasos para establecer una conexión TCP/IP son:

1. Crear sockets en el cliente y el servidor.
2. El servidor establece un puerto y escucha peticiones.
3. El cliente conecta con el servidor.
4. Se intercambian datos.
5. La conexión se cierra.

Un socket se identifica por cinco parámetros: protocolo, dirección IP local, dirección IP remota, puerto local y puerto remoto.

### 2.3. **DNS y resolución de nombres**

El sistema DNS (Sistema de Nombres de Dominio) traduce nombres de dominio (ej. <www.dominio.es>) en direcciones IP (ej. 192.168.1.1). Esto facilita el acceso a servicios sin recordar direcciones numéricas. Además, DNS permite:

- Compartir una IP entre varios dominios.
- Asignar múltiples IPs a un mismo dominio.
- Cambiar de servidor sin alterar el nombre de dominio.

### 2.4. **El protocolo FTP**

FTP (Protocolo de Transferencia de Archivos) permite la transferencia de archivos entre sistemas en redes TCP/IP. Funciona en modo cliente/servidor, usando los puertos 20 (datos) y 21 (control). Sin embargo, FTP transmite información en texto plano, lo que plantea problemas de seguridad. Alternativas como SFTP (usando SSH) o FTPS (usando SSL) solucionan esto mediante encriptación.

FTP soporta dos modos de conexión:

- **Modo activo.** El servidor inicia la conexión de datos.
- **Modo pasivo.** El cliente inicia ambas conexiones (control y datos).

### 2.5. **Los protocolos SMTP y POP3**

SMTP (Protocolo Simple de Transferencia de Correo) se usa para enviar correo electrónico, mientras que POP3 (Protocolo de Oficina Postal) se usa para recibirlo. El proceso es el siguiente:

1. El usuario redacta un mensaje y lo envía a su servidor SMTP.
2. El servidor SMTP reenvía el mensaje al servidor del destinatario.
3. El destinatario descarga el mensaje usando POP3 o lo consulta vía web con IMAP.

SMTP usa el puerto 25, mientras que POP3 usa el puerto 110.

### 2.6. **El protocolo HTTP**

HTTP (Protocolo de Transferencia de Hipertexto) permite la comunicación entre cliente y servidor para transferir páginas web. Funciona mediante peticiones y respuestas, usando el puerto 80 por defecto. Es un protocolo sin estado, pero las cookies permiten guardar información entre sesiones. Un ejemplo de diálogo HTTP:

1. El cliente solicita un recurso con `GET /organizacion.htm HTTP/1.1`.
2. El servidor responde con `HTTP/1.1 200 OK` y envía la página.
3. El cliente interpreta el contenido HTML y cierra la conexión.

HTTP define la sintaxis y semántica para la comunicación entre clientes (navegadores) y servidores web. Los recursos pueden ser archivos, resultados de programas, consultas a bases de datos, etc.

## 3. Bibliotecas de clases <br>y componentes Java

Java ofrece amplias capacidades para la interconexión TCP/IP, facilitando la creación de aplicaciones cliente/servidor y servicios en red. Algunas funcionalidades incluyen abrir URLs, realizar invocaciones de métodos remotos (RMI) y trabajar con sockets.

El paquete principal para programar aplicaciones con comunicaciones en red es **java.net**, que soporta clases para generar servicios de red, servidores y clientes. Otros paquetes relevantes son:

- **java.rmi.** Permite implementar interfaces de control remoto (RMI).
- **javax.mail.** Facilita la implementación de sistemas de correo electrónico.

Para ciertos servicios estándar, Java no proporciona objetos predefinidos, por lo que se pueden utilizar bibliotecas externas como **Apache Commons Net**, que ofrece APIs para protocolos como Telnet, FTP y FTP sobre HTTP.

### 3.1. **Objetos predefinidos**

El paquete **java.net** proporciona una API dividida en dos niveles:

#### API de bajo nivel
- **Direcciones.** Identificadores de red (direcciones IP).
  - Clase **InetAddress.** Implementa una dirección IP.
- **Sockets.** Mecanismos de comunicación bidireccional.
  - Clase **Socket.** Extremo de una conexión bidireccional.
  - Clase **ServerSocket.** Socket para servidores que escuchan peticiones.
  - Clase **DatagramSocket.** Socket para enviar y recibir datagramas.
  - Clase **MulticastSocket.** Socket para enviar paquetes multidifusión.
- **Interfaces.** Representan interfaces de red.
  - Clase **NetworkInterface.** Representa una interfaz de red con un nombre y direcciones IP.

#### API de alto nivel
- **URI.** Identificadores de recursos universales.
  - Clase **URI.**
- **URL.** Localizadores de recursos universales.
  - Clase **URL.** Representa una dirección URL.
- **Conexiones.** Representan enlaces de comunicación con recursos.
  - Clase **URLConnection.** Superclase para conexiones con URLs.
  - Clase **HttpURLConnection.** Conexión con soporte HTTP.

Estas clases de alto nivel facilitan la creación de programas que acceden a recursos de red.

### 3.2. **Métodos y ejemplos de uso de InetAddress**

La clase **InetAddress** permite manipular direcciones IP y nombres de dominio. Proporciona métodos para resolver nombres de host a direcciones IP y viceversa. Algunos métodos importantes son:

- **getLocalHost().** Devuelve la dirección IP del equipo local.
- **getByName(String host).** Devuelve la dirección IP del host especificado.
- **getAllByName(String host).** Devuelve un array de direcciones IP para el host.
- **getHostAddress().** Devuelve la dirección IP en formato de texto.
- **getHostName().** Devuelve el nombre del host.
- **isReachable(int tiempo).** Verifica si la dirección es alcanzable en el tiempo indicado.

Estos métodos pueden lanzar una excepción **UnknownHostException** si no pueden resolver el nombre.

### 3.3. **Programación con URL**

La programación con URLs se realiza a un nivel más alto que la programación con sockets, facilitando el acceso a recursos de red. Una URL (Localizador Uniforme de Recursos) representa una dirección a un recurso en la web, como un archivo, directorio o resultado de una consulta.

#### Estructura de una URL
- **Protocolo.** Protocolo usado para la comunicación (ej. HTTP, FTP).
- **Nombre del host.** Nombre del servidor que proporciona el servicio.
- **Puerto.** Puerto de red en el servidor (por defecto, 80 para HTTP).
- **Ruta.** Ruta al recurso en el servidor.
- **Referencia.** Fragmento específico dentro del recurso.

Ejemplos de URLs:

- `http://www.iesalandalus.org/organizacion.htm`: Protocolo HTTP, host `www.iesalandalus.org`, ruta `organizacion.htm`.
- `http://www.iesalandalus.org:85/organizacion.htm`: Puerto 85.
- `http://www.dominio.es/public/pag.html#apartado1`: Referencia `#apartado1`.

### 3.4. **Crear y analizar objetos URL**

La clase **URL** permite crear objetos que representan direcciones URL. Algunos constructores incluyen:

- **URL(String protocol, String host, int port, String file).** Crea una URL a partir de sus componentes.
- **URL(String spec).** Crea una URL a partir de una cadena completa.

Métodos para analizar una URL:

- **getProtocol().** Obtiene el protocolo.
- **getHost().** Obtiene el host.
- **getPort().** Obtiene el puerto (devuelve -1 si no está especificado).
- **getFile().** Obtiene el archivo o ruta.
- **getRef().** Obtiene la referencia.

### 3.5. **Leer y escribir a través de una URLConnection**

La clase **URLConnection** permite leer y escribir en recursos remotos. Algunos métodos clave son:

- **openConnection().** Devuelve un objeto **URLConnection.**
- **openStream().** Abre un flujo de entrada para leer el recurso.

Ejemplo de lectura de un archivo desde una URL:

```java
URL url = new URL("http://www.example.com/file.txt");
InputStream inputStream = url.openStream();
// Leer y procesar el contenido
```

### 3.6. **Trabajar con el contenido de una URL**

El método **getContent()** de la clase **URL** devuelve el contenido del recurso. La clase **URLConnection** proporciona métodos para obtener información sobre la conexión:

- **connect().** Establece la conexión con el recurso.
- **getContentType().** Devuelve el tipo de contenido.
- **getContentLength().** Devuelve el tamaño del contenido.
- **getLastModified().** Devuelve la fecha de última modificación.

Ejemplo de uso:

```java
URLConnection connection = url.openConnection();
connection.connect();
String contentType = connection.getContentType();
int contentLength = connection.getContentLength();
```

Este enfoque permite crear aplicaciones que acceden a recursos de Internet de manera eficiente, como clientes web o herramientas para analizar contenido.

## 4. Programación de <br>aplicaciones cliente

La programación de aplicaciones cliente y servidor se basa en el uso de protocolos estándar de la capa de aplicación. Por ejemplo, al programar un servidor HTTP, se habla de un servicio o servidor HTTP, y al programar un cliente, se habla de un cliente HTTP. En esta sección, nos centraremos en la programación de aplicaciones cliente para los protocolos **HTTP**, **FTP**, **SMTP** y **Telnet**, utilizando bibliotecas especiales que facilitan la tarea. En algunos casos, también se verá cómo programar estas aplicaciones mediante sockets.

Es fundamental entender el funcionamiento del protocolo sobre el que se construye el cliente, ya que esto permite comprender el intercambio de mensajes entre cliente y servidor. Esto es especialmente importante cuando se trabaja a niveles bajos, como con sockets.

### 4.1. **Programación de un cliente HTTP**

El protocolo **HTTP** se basa en un modelo de solicitud/respuesta:

1. El cliente establece una conexión con el servidor y envía un mensaje con los datos de la solicitud.
2. El servidor responde con un mensaje que contiene el estado de la operación y su posible resultado.

Un ejemplo básico de cliente HTTP es el acceso a recursos de red mediante las clases **URL** y **URLConnection.** Sin embargo, este enfoque es de alto nivel y oculta detalles de bajo nivel, como los que se manejan al programar con sockets.

#### Ejemplo de cliente HTTP mediante sockets

A continuación, te proporciono un ejemplo sencillo de un cliente HTTP implementado mediante sockets en Java. El código está comentado para facilitar su comprensión.

```java
package clientehttp;

// Importaciones necesarias para manejar flujos de entrada/salida y conexiones de red
import java.io.*;
import java.net.*;

/**
 * Clase que implementa un cliente HTTP básico mediante sockets.
 * Este cliente se conecta a un servidor HTTP, envía una solicitud GET
 * y muestra la respuesta del servidor en la consola.
 *
 * @author TuNombre
 */
public class ClienteHTTP {

    /**
     * Método principal que ejecuta el cliente HTTP.
     *
     * @param args Argumentos de la línea de comandos (no se utilizan en este ejemplo).
     */
    public static void main(String[] args) {
        // Definimos el host y el recurso que queremos solicitar
        String host = "www.example.com";
        String recurso = "/";

        try {
            // Creamos un socket para conectarnos al servidor en el puerto 80 (HTTP)
            Socket socket = new Socket(host, 80);

            // Creamos un flujo de salida para enviar la solicitud HTTP al servidor
            OutputStream out = socket.getOutputStream();
            PrintWriter writer = new PrintWriter(out, true);

            // Creamos un flujo de entrada para recibir la respuesta del servidor
            InputStream in = socket.getInputStream();
            BufferedReader reader = new BufferedReader(new InputStreamReader(in));

            // Enviamos la solicitud HTTP GET al servidor
            writer.println("GET " + recurso + " HTTP/1.1");
            writer.println("Host: " + host);
            writer.println("Connection: Close");
            writer.println(); // Línea en blanco para indicar el fin de la cabecera

            // Leemos y mostramos la respuesta del servidor línea por línea
            String linea;
            System.out.println("Respuesta del servidor:");
            while ((linea = reader.readLine()) != null) {
                System.out.println(linea);
            }

            // Cerramos los flujos y el socket
            writer.close();
            reader.close();
            socket.close();

        } catch (UnknownHostException e) {
            // Manejo de excepción si no se puede encontrar el host
            System.err.println("No se pudo encontrar el host: " + host);
        } catch (IOException e) {
            // Manejo de excepción si ocurre un error de E/S durante la comunicación
            System.err.println("Error de E/S: " + e.getMessage());
        }
    }
}
```

#### Ejemplo de salida

Al ejecutar este código, obtendrás una respuesta similar a la siguiente (dependiendo del servidor y el recurso solicitado):

``` http
HTTP/1.1 200 OK
Date: Mon, 23 Oct 2023 12:34:56 GMT
Server: Apache/2.4.41 (Unix)
Content-Length: 1234
Content-Type: text/html; charset=UTF-8

<!DOCTYPE html>
<html>
<head>
    <title>Example Domain</title>
    ...
</head>
<body>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents...</p>
</body>
</html>
```

Este código es un ejemplo básico y puede extenderse para manejar más casos, como solicitudes POST, manejo de cabeceras adicionales, o procesamiento de la respuesta.

### 4.2. **Programación de un cliente FTP**

Una forma sencilla de crear un cliente FTP es utilizando la clase **FTPClient.** El esquema básico de trabajo es el siguiente:

1. **Conexión.** Conectar el cliente al servidor mediante `connect(InetAddress host)`.
2. **Verificación.** Comprobar la conexión con `getReplyCode()`.
3. **Autenticación.** Validar el usuario con `login(String usuario, String password)`.
4. **Operaciones.** Realizar operaciones como listar archivos con `listNames()` o descargar un archivo con `retrieveFile(String rutaRemota, OutputStream ficheroLocal)`.
5. **Desconexión.** Cerrar la conexión con `disconnect()` o `logout()`.

Durante este proceso, pueden generarse excepciones como **SocketException** (si se supera el tiempo de espera) o **IOException** (si no se puede acceder al archivo).

#### Bibliotecas para programar un cliente FTP

Java no proporciona bibliotecas específicas para programar clientes y servidores FTP. Sin embargo, la organización **Apache Software Foundation** ofrece una API para implementar clientes FTP. El paquete principal es **org.apache.commons.net.ftp**, que incluye las siguientes clases:

- **FTP.** Proporciona funcionalidades básicas para implementar un cliente FTP.
- **FTPReply.** Almacena los códigos de respuesta del servidor.
- **FTPClient.** Encapsula la funcionalidad necesaria para interactuar con un servidor FTP.
- **FTPClientConfig.** Permite configurar objetos **FTPClient.**
- **FTPSClient.** Proporciona FTP seguro sobre SSL.

[Apache Commons Net 3.11.1 API](https://commons.apache.org/proper/commons-net/apidocs/org/apache/commons/net/ftp/package-summary.html)

#### Ejemplo de cliente FTP

```java
package clienteftp;

//librerías de apache para FTP
import org.apache.commons.net.ftp.FTPClient;
import org.apache.commons.net.ftp.FTPReply;

//librerías de java
import java.io.IOException;
import java.io.FileOutputStream;
import java.net.SocketException;

/**
 * Clase para recuperar un fichero de un Servidor FTP. El fichero se deposita en
 * el primer nivel de la carpeta del proyecto
 *
 * ¡¡¡IMPORTANTE!!!
 * Para probar el ejemplo puede que tengas que deshabilitar cualquier
 * cortafuegos que tengas activado
 * ¡¡¡NO OLVIDARSE DE DESHACER LOS CAMBIOS!!! La seguridad del Sistema podría
 * verse comprometida
 *
 * @author IMCG
 */
public class Main {

  //objeto de la clase FTPClient de Apache, con diversos métodos para
  //interactuar y recuperar un archivo de un servidor FTP
  private static FTPClient clienteFTP;
  //flujo de salida para la escritura de datos en un fichero
  private static FileOutputStream ficheroObtenido;
  //URL del servidor
  private static String servidorURL = "ftp.rediris.es";
  //ruta relativa (en Servidor FTP) de la carpeta que contiene
  //el fichero que vamos a descargar
  private static String rutaFichero = "debian";
  //nombre del fichero (aunque carece de extensión, se trata de un fichero de
  //texto que puede abrise con el bloc de notas)
  private static String nombreFichero = "README";
  //usuario
  private static String usuario = "anonymous";
  //contraseña
  private static String password = "";
  //array de carpetas disponibles
  private static String[] nombreCarpeta;

  /**
   * **************************************************************************
   * recupera el contenido de un fichero desde un Servidor FTP, y lo deposita en
   * un nuevo fichero en el directorio de nuestro proyecto
   *
   * @param args
   */
  public static void main(String[] args) {
    try {
      int reply;
      //creación del objeto cliente FTP
      clienteFTP = new FTPClient();
      //conexión del cliente al servidor FTP
      clienteFTP.connect("ftp.rediris.es");
      //omprobación de la conexión
      reply = clienteFTP.getReplyCode();
      //si la conexión  es satisfactoria
      if (FTPReply.isPositiveCompletion(reply)) {
        //abre una sesión con el usuario anónimo
        clienteFTP.login(usuario, password);
        //lista las carpetas de primer nivel del servidor FTP
        System.out.println("Carpetas disponibles en el Servidor:");
        nombreCarpeta = clienteFTP.listNames();
        for (int i = 0; i < nombreCarpeta.length; i++) {
          System.out.println(nombreCarpeta[i]);
        }
        //nombre que el que va a recuperarse
        ficheroObtenido = new FileOutputStream(nombreFichero);
        //mensaje
        System.out.println("\nDescargando el fichero " + nombreFichero + " de "
                + "la carpeta " + rutaFichero);
        //recupera el contenido del fichero en el Servidor, y lo escribe en el
        //nuevo fichero del directorio del proyecto
        clienteFTP.retrieveFile("/" + rutaFichero + "/"
               + nombreFichero, ficheroObtenido);
        //cierra el nuevo fichero
        ficheroObtenido.close();
        //cierra la conexión con el Servidor
        clienteFTP.disconnect();
        //
        System.out.println("Descarga finalizada correctamente");
      } else {
        //desconecta
        clienteFTP.disconnect();
        System.err.println("FTP ha rechazado la conexión esblecida");
        System.exit(1);
      }
    } catch (SocketException ex) {
      //error de Socket
      System.out.println(ex.toString());
    } catch (IOException ex) {
      //error de fichero
      System.out.println(ex.toString());
    }
  }
}
```

### 4.3. **Programación de un cliente Telnet**

El protocolo **Telnet** permite acceder y administrar equipos de forma remota. Está basado en el modelo cliente/servidor y utiliza el puerto 23. Sin embargo, debido a su falta de seguridad (los datos se transmiten en texto plano), ha sido reemplazado por protocolos como **SSH.**

A modo ilustrativo, se puede programar un cliente Telnet utilizando la biblioteca **org.apache.commons.net.telnet.** La clase principal es **TelnetClient**, que permite implementar un terminal virtual para Telnet. Algunos métodos clave son:

- **connect().** Establece la conexión con el servidor.
- **getInputStream()** y **getOutputStream().** Permiten enviar y recibir datos.
- **disconnect().** Cierra la conexión y los flujos de entrada/salida.

#### Ejemplo de cliente Telnet

```java
package clientetelnet;

// Importaciones necesarias para manejar flujos de entrada/salida y conexiones de red
import java.io.*;
import java.net.*;

/**
 * Clase que implementa un cliente Telnet básico mediante sockets.
 * Este cliente se conecta a un servidor Telnet, envía comandos
 * y muestra la respuesta del servidor en la consola.
 *
 * @author TuNombre
 */
public class ClienteTelnet {

    /**
     * Método principal que ejecuta el cliente Telnet.
     *
     * @param args Argumentos de la línea de comandos (no se utilizan en este ejemplo).
     */
    public static void main(String[] args) {
        // Definimos el host y el puerto del servidor Telnet
        String host = "localhost"; // Cambia esto por la dirección del servidor Telnet
        int puerto = 23; // Puerto estándar para Telnet

        try {
            // Creamos un socket para conectarnos al servidor Telnet
            Socket socket = new Socket(host, puerto);

            // Creamos un flujo de salida para enviar comandos al servidor
            OutputStream out = socket.getOutputStream();
            PrintWriter writer = new PrintWriter(out, true);

            // Creamos un flujo de entrada para recibir la respuesta del servidor
            InputStream in = socket.getInputStream();
            BufferedReader reader = new BufferedReader(new InputStreamReader(in));

            // Creamos un flujo de entrada para leer comandos desde la consola
            BufferedReader consola = new BufferedReader(new InputStreamReader(System.in));

            // Mensaje de conexión exitosa
            System.out.println("Conectado al servidor Telnet en " + host + ":" + puerto);
            System.out.println("Escribe 'exit' para salir.");

            // Bucle para enviar comandos y recibir respuestas
            String comando;
            while (true) {
                // Leemos un comando desde la consola
                System.out.print("> ");
                comando = consola.readLine();

                // Enviamos el comando al servidor
                writer.println(comando);

                // Si el comando es 'exit', salimos del bucle
                if (comando.equalsIgnoreCase("exit")) {
                    break;
                }

                // Leemos y mostramos la respuesta del servidor línea por línea
                String linea;
                while ((linea = reader.readLine()) != null) {
                    System.out.println(linea);
                }
            }

            // Cerramos los flujos y el socket
            writer.close();
            reader.close();
            consola.close();
            socket.close();

            // Mensaje de desconexión
            System.out.println("Desconectado del servidor Telnet.");

        } catch (UnknownHostException e) {
            // Manejo de excepción si no se puede encontrar el host
            System.err.println("No se pudo encontrar el host: " + host);
        } catch (IOException e) {
            // Manejo de excepción si ocurre un error de E/S durante la comunicación
            System.err.println("Error de E/S: " + e.getMessage());
        }
    }
}
```

#### Ejemplo de Salida

```shell
Conectado al servidor Telnet en localhost:23
Escribe 'exit' para salir.
> ls
archivo1.txt
archivo2.txt
directorio
> exit
Desconectado del servidor Telnet.
```

### 4.4. **Programación de un cliente SMTP**

Para programar un cliente SMTP, se pueden utilizar dos enfoques: mediante sockets o mediante el API **javax.mail.**

#### Ejemplo con sockets

```java
package clientesmtp;

// Importaciones necesarias para manejar flujos de entrada/salida y conexiones de red
import java.io.*;
import java.net.*;

/**
 * Clase que implementa un cliente SMTP básico mediante sockets.
 * Este cliente se conecta a un servidor SMTP, envía un correo electrónico
 * y muestra la respuesta del servidor en la consola.
 *
 * ¡¡¡IMPORTANTE!!!
 * Este es un ejemplo básico y no maneja todos los casos posibles,
 * como autenticación, cifrado (TLS/SSL), o manejo de errores avanzados.
 *
 * @author TuNombre
 */
public class ClienteSMTP {

    /**
     * Método principal que ejecuta el cliente SMTP.
     *
     * @param args Argumentos de la línea de comandos (no se utilizan en este ejemplo).
     */
    public static void main(String[] args) {
        // Definimos el host y el puerto del servidor SMTP
        String host = "smtp.example.com"; // Cambia esto por la dirección del servidor SMTP
        int puerto = 25; // Puerto estándar para SMTP

        // Información del correo electrónico
        String remitente = "remitente@example.com";
        String destinatario = "destinatario@example.com";
        String asunto = "Prueba de correo SMTP";
        String cuerpo = "Este es un correo de prueba enviado desde un cliente SMTP en Java.";

        try {
            // Creamos un socket para conectarnos al servidor SMTP
            Socket socket = new Socket(host, puerto);

            // Creamos un flujo de salida para enviar comandos al servidor
            OutputStream out = socket.getOutputStream();
            PrintWriter writer = new PrintWriter(out, true);

            // Creamos un flujo de entrada para recibir la respuesta del servidor
            InputStream in = socket.getInputStream();
            BufferedReader reader = new BufferedReader(new InputStreamReader(in));

            // Leemos la respuesta inicial del servidor
            String respuesta = reader.readLine();
            System.out.println("Respuesta del servidor: " + respuesta);

            // Enviamos el comando HELO para iniciar la comunicación
            writer.println("HELO " + host);
            respuesta = reader.readLine();
            System.out.println("Respuesta del servidor: " + respuesta);

            // Enviamos el comando MAIL FROM para indicar el remitente
            writer.println("MAIL FROM: <" + remitente + ">");
            respuesta = reader.readLine();
            System.out.println("Respuesta del servidor: " + respuesta);

            // Enviamos el comando RCPT TO para indicar el destinatario
            writer.println("RCPT TO: <" + destinatario + ">");
            respuesta = reader.readLine();
            System.out.println("Respuesta del servidor: " + respuesta);

            // Enviamos el comando DATA para indicar que vamos a enviar el cuerpo del correo
            writer.println("DATA");
            respuesta = reader.readLine();
            System.out.println("Respuesta del servidor: " + respuesta);

            // Enviamos el asunto y el cuerpo del correo
            writer.println("Subject: " + asunto);
            writer.println(); // Línea en blanco para separar el asunto del cuerpo
            writer.println(cuerpo);
            writer.println("."); // Línea con un punto para indicar el fin del mensaje
            respuesta = reader.readLine();
            System.out.println("Respuesta del servidor: " + respuesta);

            // Enviamos el comando QUIT para finalizar la conexión
            writer.println("QUIT");
            respuesta = reader.readLine();
            System.out.println("Respuesta del servidor: " + respuesta);

            // Cerramos los flujos y el socket
            writer.close();
            reader.close();
            socket.close();

            // Mensaje de finalización
            System.out.println("Correo enviado correctamente.");

        } catch (UnknownHostException e) {
            // Manejo de excepción si no se puede encontrar el host
            System.err.println("No se pudo encontrar el host: " + host);
        } catch (IOException e) {
            // Manejo de excepción si ocurre un error de E/S durante la comunicación
            System.err.println("Error de E/S: " + e.getMessage());
        }
    }
}
```

#### Ejemplo de salida

```terminal
Respuesta del servidor: 220 smtp.example.com ESMTP Postfix
Respuesta del servidor: 250 smtp.example.com
Respuesta del servidor: 250 2.1.0 Ok
Respuesta del servidor: 250 2.1.5 Ok
Respuesta del servidor: 354 End data with <CR><LF>.<CR><LF>
Respuesta del servidor: 250 2.0.0 Ok: queued as 12345
Respuesta del servidor: 221 2.0.0 Bye
Correo enviado correctamente.
```

#### Ejemplo con javax.mail

El paquete **javax.mail** proporciona las clases necesarias para implementar un sistema de correo. Algunas clases y métodos clave son:

- **Session.** Representa una sesión de correo. Se obtiene mediante `getDefaultInstance()`.
- **Message.** Modela un mensaje de correo electrónico. Métodos como `setFrom()`, `setRecipients()`, `setSubject()` y `setText()` permiten configurar el mensaje.
- **Transport.** Representa el transporte de mensajes. El método `send()` envía el mensaje a las direcciones indicadas.

Este ejemplo utiliza SMTP seguro (SMTP sobre SSL), por lo que no se usa el puerto 25 tradicional, sino uno específico para conexiones seguras.

```java
package clientesmtpseguro;

// Importaciones necesarias para usar javax.mail
import javax.mail.*;
import javax.mail.internet.*;
import java.util.Properties;

/**
 * Clase que implementa un cliente SMTP seguro utilizando la biblioteca javax.mail.
 * Este cliente se conecta a un servidor SMTP sobre SSL, envía un correo electrónico
 * y maneja la autenticación del usuario.
 *
 * ¡¡¡IMPORTANTE!!!
 * Este ejemplo utiliza SMTP seguro (SSL) y requiere credenciales válidas
 * para autenticarse en el servidor SMTP.
 *
 * @author TuNombre
 */
public class ClienteSMTPSeguro {

    /**
     * Método principal que ejecuta el cliente SMTP seguro.
     *
     * @param args Argumentos de la línea de comandos (no se utilizan en este ejemplo).
     */
    public static void main(String[] args) {
        // Configuración del servidor SMTP
        String host = "smtp.gmail.com"; // Servidor SMTP de Gmail (puedes cambiarlo)
        int puerto = 465; // Puerto para SMTP sobre SSL
        String usuario = "tucorreo@gmail.com"; // Cambia esto por tu correo
        String contraseña = "tupassword"; // Cambia esto por tu contraseña

        // Configuración de propiedades para la sesión SMTP
        Properties propiedades = new Properties();
        propiedades.put("mail.smtp.host", host); // Servidor SMTP
        propiedades.put("mail.smtp.port", puerto); // Puerto SMTP
        propiedades.put("mail.smtp.ssl.enable", "true"); // Habilitar SSL
        propiedades.put("mail.smtp.auth", "true"); // Habilitar autenticación

        // Crear una sesión de correo con autenticación
        Session sesion = Session.getInstance(propiedades, new Authenticator() {
            @Override
            protected PasswordAuthentication getPasswordAuthentication() {
                return new PasswordAuthentication(usuario, contraseña);
            }
        });

        try {
            // Crear un mensaje de correo
            Message mensaje = new MimeMessage(sesion);
            mensaje.setFrom(new InternetAddress(usuario)); // Remitente
            mensaje.setRecipients(Message.RecipientType.TO, InternetAddress.parse("destinatario@example.com")); // Destinatario
            mensaje.setSubject("Prueba de correo SMTP seguro"); // Asunto
            mensaje.setText("Este es un correo de prueba enviado desde un cliente SMTP seguro en Java."); // Cuerpo del mensaje

            // Enviar el mensaje
            Transport.send(mensaje);

            // Mensaje de éxito
            System.out.println("Correo enviado correctamente.");

        } catch (MessagingException e) {
            // Manejo de excepción si ocurre un error al enviar el correo
            System.err.println("Error al enviar el correo: " + e.getMessage());
        }
    }
}
```

#### Explicación

1. **Paquete y declaración de la clase.**
   - El código está organizado en el paquete `clientesmtpseguro`.
   - La clase `ClienteSMTPSeguro` contiene el método principal (`main`) que ejecuta el cliente.

2. **Importaciones.**
   - Se importan las clases necesarias de la biblioteca `javax.mail` para manejar correos electrónicos.

3. **Configuración del servidor SMTP.**
   - Se define el servidor SMTP (`smtp.gmail.com`), el puerto (`465` para SSL), y las credenciales de autenticación (usuario y contraseña).

4. **Propiedades de la sesión.**
   - Se configuran las propiedades para habilitar SSL (`mail.smtp.ssl.enable`) y la autenticación (`mail.smtp.auth`).

5. **Autenticación.**
   - Se crea una sesión de correo con autenticación utilizando `Authenticator` y `PasswordAuthentication`.

6. **Creación del mensaje.**
   - Se crea un objeto `MimeMessage` para representar el correo electrónico.
   - Se define el remitente, el destinatario, el asunto y el cuerpo del mensaje.

7. **Envío del mensaje.**
   - Se utiliza el método `Transport.send(mensaje)` para enviar el correo electrónico.

8. **Manejo de excepciones.**
   - Se captura y maneja la excepción `MessagingException` si ocurre un error al enviar el correo.

9. **Mensajes de estado.**
   - Se muestra un mensaje en la consola para indicar que el correo se envió correctamente.

#### Requisitos previos

1. **Biblioteca javax.mail.**
   - Asegúrate de tener la biblioteca `javax.mail` en tu proyecto. Puedes descargarla desde [aquí](https://javaee.github.io/javamail/) o agregarla como dependencia en Maven:

```xml
<dependency>
    <groupId>com.sun.mail</groupId>
    <artifactId>javax.mail</artifactId>
    <version>1.6.2</version>
</dependency>
```

2. **Credenciales de correo.**
   - Usa un correo electrónico válido y su contraseña. Si usas Gmail, asegúrate de habilitar el acceso a aplicaciones menos seguras o generar una contraseña de aplicación.

#### Ejemplo de uso

1. **Configura el servidor SMTP.** Cambia `smtp.gmail.com` por el servidor SMTP que uses (por ejemplo, `smtp.outlook.com` para Outlook).

2. **Proporciona las credenciales.** Cambia `tucorreo@gmail.com` y `tupassword` por tu correo y contraseña.

3. **Ejecuta el programa.** El cliente se conecta al servidor SMTP sobre SSL, autentica al usuario y envía el correo electrónico.

4. **Verifica el correo.** Revisa la bandeja de entrada del destinatario para confirmar que el correo se envió correctamente.

#### Ejemplo de salida

```terminal
Correo enviado correctamente.
```

Este código es un ejemplo básico y puede extenderse para manejar más casos, como adjuntar archivos, enviar correos HTML, o manejar múltiples destinatarios.

## 5. Programación de servidores

Al diseñar o programar un servidor o servicio en red, es importante considerar los siguientes aspectos:

- **Concurrencia.** El servidor debe poder atender múltiples peticiones simultáneas. Esto se logra mediante el uso de hilos (**Threads**).
- **Optimización del tiempo de respuesta.** Es crucial monitorizar los tiempos de procesamiento y transmisión para mejorar la eficiencia del servidor.

La clase **ServerSocket** es fundamental en Java para crear servidores. Para programar servidores basados en protocolos de la capa de aplicación, como HTTP, es necesario entender el comportamiento del protocolo y los mensajes que intercambia con el cliente.

### 5.1. **Programación de un servidor HTTP**

Antes de programar un servidor HTTP, es importante recordar cómo funciona este protocolo. El servidor que vamos a implementar cumple con lo siguiente:

- Se basa en la versión 1.1 del protocolo HTTP.
- Implementa solo una parte del protocolo.
- Maneja dos tipos de mensajes: peticiones de clientes y respuestas del servidor.
- Solo procesa peticiones **GET.**

El esquema básico para crear un servidor HTTP es:

1. Crear un **ServerSocket** asociado al puerto 80 (puerto por defecto para HTTP).
2. Esperar peticiones del cliente.
3. Aceptar la petición del cliente.
4. Procesar la petición (intercambio de mensajes según el protocolo y transmisión de datos).
5. Cerrar el socket del cliente.

A continuación, se presenta un ejemplo de un servidor web básico que escucha en el puerto 8066. Dependiendo de la URL que se ingrese en el navegador, el servidor responderá con diferentes mensajes:

- `<http://localhost:8066>.` Muestra un mensaje de bienvenida.
- `http://localhost:8066/quijote` Muestra un párrafo de "El Quijote".
- **Otras URLs.** Muestra un mensaje de error.

Aquí tienes el ejemplo del **Servidor HTTP** presentado de la misma forma que los anteriores, con comentarios descriptivos integrados en el código:

#### ServidorHTTP.java

```java
package PaquetePrincipal;

import java.io.BufferedReader;
import java.net.Socket;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;

/**
 * *****************************************************************************
 * Servidor HTTP que atiende peticiones de tipo 'GET' recibidas por el puerto 8066.
 *
 * NOTA: Para probar este código, comprueba primero que no tienes ningún otro
 * servicio usando el puerto 8066 (por ejemplo, con el comando 'netstat' en Windows).
 *
 * @author IMCG
 */
class ServidorHTTP {

    /**
     * **************************************************************************
     * Procedimiento principal que asigna a cada petición entrante un socket
     * cliente, por donde se enviará la respuesta una vez procesada.
     *
     * @param args Argumentos de la línea de comandos (no se utilizan en este ejemplo).
     */
    public static void main(String[] args) throws IOException, Exception {

        // Asociamos al servidor el puerto 8066
        ServerSocket socServidor = new ServerSocket(8066);
        imprimeDisponible();
        Socket socCliente;

        // Ante una petición entrante, procesa la petición por el socket cliente
        // por donde la recibe
        while (true) {
            // A la espera de peticiones
            socCliente = socServidor.accept();
            // Atiende un cliente
            System.out.println("Atendiendo al cliente ");
            procesaPeticion(socCliente);
            // Cierra la conexión entrante
            socCliente.close();
            System.out.println("Cliente atendido");
        }
    }

    /**
     * **************************************************************************
     * Procesa la petición recibida.
     *
     * @param socketCliente Socket del cliente que realiza la petición.
     * @throws IOException Si ocurre un error de entrada/salida.
     */
    private static void procesaPeticion(Socket socketCliente) throws IOException {
        // Variables locales
        String peticion;
        String html;

        // Flujo de entrada
        InputStreamReader inSR = new InputStreamReader(socketCliente.getInputStream());
        // Espacio en memoria para la entrada de peticiones
        BufferedReader bufLeer = new BufferedReader(inSR);

        // Objeto de java.io que permite escribir 'línea a línea' en un flujo de salida
        PrintWriter printWriter = new PrintWriter(socketCliente.getOutputStream(), true);

        // Mensaje de petición del cliente
        peticion = bufLeer.readLine();

        // Para compactar la petición y facilitar su análisis, suprimimos todos
        // los espacios en blanco que contenga
        peticion = peticion.replaceAll(" ", "");

        // Si realmente se trata de una petición 'GET' (que es la única que vamos a
        // implementar en nuestro Servidor)
        if (peticion.startsWith("GET")) {
            // Extrae la subcadena entre 'GET' y 'HTTP/1.1'
            peticion = peticion.substring(3, peticion.lastIndexOf("HTTP"));

            // Si corresponde a la página de inicio
            if (peticion.length() == 0 || peticion.equals("/")) {
                // Sirve la página
                html = Paginas.html_index;
                printWriter.println(Mensajes.lineaInicial_OK);
                printWriter.println(Paginas.primeraCabecera);
                printWriter.println("Content-Length: " + html.length() + 1);
                printWriter.println("\n");
                printWriter.println(html);
            } 
            // Si corresponde a la página del Quijote
            else if (peticion.equals("/quijote")) {
                // Sirve la página
                html = Paginas.html_quijote;
                printWriter.println(Mensajes.lineaInicial_OK);
                printWriter.println(Paginas.primeraCabecera);
                printWriter.println("Content-Length: " + html.length() + 1);
                printWriter.println("\n");
                printWriter.println(html);
            } 
            // En cualquier otro caso
            else {
                // Sirve la página de error
                html = Paginas.html_noEncontrado;
                printWriter.println(Mensajes.lineaInicial_NotFound);
                printWriter.println(Paginas.primeraCabecera);
                printWriter.println("Content-Length: " + html.length() + 1);
                printWriter.println("\n");
                printWriter.println(html);
            }
        }
    }

    /**
     * **************************************************************************
     * Muestra un mensaje en la salida que confirma el arranque y da algunas
     * indicaciones posteriores.
     */
    private static void imprimeDisponible() {
        System.out.println("El Servidor WEB se está ejecutando y permanece a la "
                + "escucha por el puerto 8066.\nEscribe en la barra de direcciones "
                + "de tu explorador preferido:\n\nhttp://localhost:8066\npara "
                + "solicitar la página de bienvenida\n\nhttp://localhost:8066/"
                + "quijote\n para solicitar una página del Quijote,\n\nhttp://"
                + "localhost:8066/q\n para simular un error");
    }
}
```

#### Mensajes.java

```java
package PaquetePrincipal;

/**
 * ****************************************************************************
 * Clase que contiene los mensajes que intercambia el Servidor con el Cliente
 * según el protocolo HTTP.
 *
 * @author IMCG
 */
public class Mensajes {
    public static final String lineaInicial_OK = "HTTP/1.1 200 OK";
    public static final String lineaInicial_NotFound = "HTTP/1.1 404 Not Found";
    // public static final String lineaInicial_BadRequest = "HTTP/1.1 400 Bad Request";
}
```

#### Paginas.java

```java
package PaquetePrincipal;

/**
 * ****************************************************************************
 * Clase no instanciable donde se definen algunos valores finales, como las
 * páginas HTML que servirá el servidor.
 *
 * @author IMCG
 */
public class Paginas {

    public static final String primeraCabecera = "Content-Type:text/html;charset=UTF-8";

    // Contenido de la página de inicio
    public static final String html_index = "<html>"
            + "<head><title>index</title></head>"
            + "<body>"
            + "<h1>¡Enhorabuena!</h1>"
            + "<p>Tu servidor HTTP mínimo funciona correctamente</p>"
            + "</body>"
            + "</html>";

    // Contenido de la página del Quijote
    public static final String html_quijote = "<html>"
            + "<head><title>quijote</title></head>"
            + "<body>"
            + "<h1>Así comienza el Quijote</h1>"
            + "<p>En un lugar de la Mancha, de cuyo nombre no quiero "
            + "acordarme, no ha mucho tiempo que vivía un hidalgo de los "
            + "de lanza en astillero, adarga antigua, rocín flaco y galgo "
            + "corredor. Una olla de algo más vaca que carnero, salpicón "
            + "las más noches, duelos y quebrantos (huevos con tocino) los "
            + "sábados, lentejas los viernes, algún palomino de añadidura "
            + "los domingos, consumían las tres partes de su hacienda. El "
            + "resto della concluían sayo de velarte (traje de paño fino), "
            + "calzas de velludo (terciopelo) para las fiestas con sus "
            + "pantuflos de lo mismo, y los días de entresemana se honraba "
            + "con su vellorí (pardo de paño) de lo más fino. Tenía en su "
            + "casa una ama que pasaba de los cuarenta, y una sobrina que "
            + "no llegaba a los veinte, y un mozo de campo y plaza, que "
            + "así ensillaba el rocín como tomaba la podadera...</p>"
            + "</body>"
            + "</html>";

    // Contenido de la página de error
    public static final String html_noEncontrado = "<html>"
            + "<head><title>noEncontrado</title></head>"
            + "<body>"
            + "<h1>¡ERROR! Página no encontrada</h1>"
            + "<p>La página que solicitaste no existe en nuestro servidor</p>"
            + "</body>"
            + "</html>";
}
```

#### Ejemplo de uso

1. **Ejecuta el servidor**:
   - El servidor se inicia y escucha en el puerto 8066.

2. **Accede al servidor desde un navegador**:
   - Abre un navegador y escribe las siguientes URLs:
     - `http://localhost:8066`: Muestra la página de bienvenida.
     - `http://localhost:8066/quijote`: Muestra un fragmento de "El Quijote".
     - `http://localhost:8066/q`: Simula un error y muestra la página de "No encontrado".

3. **Verifica las respuestas**:
   - El servidor responde con las páginas HTML correspondientes y muestra mensajes en la consola.

#### Ejemplo de salida en la consola

```terminal
El Servidor WEB se está ejecutando y permanece a la escucha por el puerto 8066.
Escribe en la barra de direcciones de tu explorador preferido:

http://localhost:8066
para solicitar la página de bienvenida

http://localhost:8066/quijote
para solicitar una página del Quijote,

http://localhost:8066/q
para simular un error

Atendiendo al cliente 
Cliente atendido
```

Este código es un ejemplo básico y puede extenderse para manejar más casos, como peticiones POST, manejo de archivos estáticos, o soporte para múltiples clientes concurrentes.

### 5.2. **Implementar comunicaciones simultáneas**

Para que un servidor HTTP pueda atender múltiples peticiones simultáneamente, es necesario utilizar hilos (**Threads**). El esquema de funcionamiento es el siguiente:

1. El hilo principal crea un **ServerSocket** y espera peticiones.
2. Cuando llega una petición, el hilo principal acepta la conexión y asigna un socket cliente.
3. En lugar de atender la petición directamente, el hilo principal crea un nuevo hilo (**HiloDespachador**) para manejar la solicitud.
4. El hilo principal continúa esperando nuevas peticiones.

El código del hilo principal tendría la siguiente estructura:

```java
try {
  ServerSocket socServidor = new ServerSocket(puerto);
  while (true) {
    // Acepta una petición y asigna un socket cliente
    Socket socketCliente = socServidor.accept();
    // Crea un nuevo hilo para manejar la petición
    Thread hilo = new HiloDespachador(socketCliente);
    hilo.start();
  }
} catch (IOException ex) {
  ex.printStackTrace();
}
```

La clase **HiloDespachador** extiende **Thread** y maneja la petición del cliente:

```java
class HiloDespachador extends Thread {
  private Socket socketCliente;

  public HiloDespachador(Socket socketCliente) {
    this.socketCliente = socketCliente;
  }

  public void run() {
    try {
      // Procesa la petición del cliente
    } catch (IOException ex) {
      ex.printStackTrace();
    }
  }
}
```

Este enfoque permite que el servidor maneje múltiples peticiones de manera concurrente, mejorando su eficiencia.

### 5.3. **Monitorización de tiempos de respuesta**

Para evaluar el rendimiento de un servidor, es importante medir los tiempos de respuesta, que incluyen:

- **Tiempo de procesamiento.** El tiempo que tarda el servidor en procesar la petición y enviar los datos.
- **Tiempo de transmisión.** El tiempo que tardan los mensajes en llegar al cliente a través de la red.

#### Medición del tiempo de procesamiento

El tiempo de procesamiento se puede medir en el servidor utilizando el siguiente código:

```java
long inicio = System.currentTimeMillis();
// Procesar la petición
long fin = System.currentTimeMillis();
long tiempoProcesamiento = fin - inicio;
System.out.println("Tiempo de procesamiento: " + tiempoProcesamiento + " ms");
```

#### Medición del tiempo de transmisión

Para medir el tiempo de transmisión, el servidor debe enviar al cliente la hora en que inicia la transmisión. El cliente compara esta hora con su hora local para calcular el tiempo de transmisión. Es crucial que los relojes del servidor y el cliente estén sincronizados, por ejemplo, mediante el protocolo **NTP** (Network Time Protocol).

### 5.4. **Ejemplo de monitorización del tiempo de transmisión**

A continuación, se presenta un ejemplo de cómo calcular el tiempo de transmisión de un recurso desde un servidor web. Se modifica un cliente HTTP basado en las clases **URL** y **URLConnection** para incluir la función **URLConnection.getDate()**, que devuelve la hora en que el servidor inició la transmisión.

El código del cliente podría ser:

```java
URL url = new URL("http://localhost:8066");
URLConnection conexion = url.openConnection();
long tiempoServidor = conexion.getDate();
long tiempoCliente = System.currentTimeMillis();
long tiempoTransmision = tiempoCliente - tiempoServidor;
System.out.println("Tiempo de transmisión: " + tiempoTransmision + " ms");
```

En el siguiente enlace puedes descargar el proyecto Java completo:

#### Ejemplo de monitorización de tiempo de transmisión

Aquí tienes el código de la clase `HiloBoton` con comentarios descriptivos integrados, siguiendo el mismo formato que los ejemplos anteriores:

#### HiloBoton.java

```java
package tiempotransmisionurl;

import java.io.*;
import java.net.URL;
import java.net.URLConnection;
import java.net.MalformedURLException;

/**
 * ****************************************************************************
 * Hilo para medir el tiempo que tarda en transmitirse un recurso URL tecleado
 * por el usuario, desde el servidor hasta el cliente.
 *
 * Se basa en el encabezado 'Date', donde el servidor le envía al cliente el
 * tiempo transcurrido (en milisegundos) desde el 1 de enero de 1970 GMT, hasta
 * el inicio de la transmisión.
 *
 * @author IMCG
 */
class HiloBoton extends Thread {

    // Variable local para almacenar la URL proporcionada por el usuario
    private final String cadenaURL;

    /**
     * **************************************************************************
     * Constructor de la clase HiloBoton.
     *
     * @param cadenaURL La URL del recurso que se va a medir.
     */
    public HiloBoton(String cadenaURL) {
        this.cadenaURL = cadenaURL;
    }

    /**
     * **************************************************************************
     * Método run() que contiene el código ejecutado por el hilo.
     * Este método realiza la conexión con el servidor, mide el tiempo de transmisión
     * del recurso y muestra el resultado en la consola.
     */
    @Override
    public void run() {
        try {
            // Conexión implícita con el servidor para acceder al recurso
            URL url = new URL(cadenaURL);
            URLConnection conexion = url.openConnection();
            conexion.connect();

            // Fuerza la transmisión del recurso mediante su lectura byte a byte
            InputStream inputStream = conexion.getInputStream();
            while (inputStream.read() > -1) {
                // Lee todos los bytes del recurso
            }

            // Instante 'fin de transmisión', con respecto al 1 de enero de 1970 GMT
            long tiempoCliente = System.currentTimeMillis();

            // Instante 'inicio de transmisión', con respecto al 1 de enero de 1970 GMT
            long tiempoServidor = conexion.getDate();

            // Calcula y muestra el tiempo de transmisión en milisegundos
            System.out.println(String.format("El tiempo de transmisión del recurso "
                    + "ha sido de %sms", Math.round(tiempoCliente - tiempoServidor)));

        } catch (MalformedURLException e) {
            // Manejo de excepción si la URL no tiene un formato válido
            System.err.println("URL sin sentido");
        } catch (IOException e) {
            // Manejo de excepción si ocurre un error de lectura/escritura
            System.err.println("Error de lectura/escritura");
        } finally {
            // Termina la aplicación
            System.exit(0);
        }
    }
}
```


#### Explicación del código integrada en los comentarios

1. **Paquete y declaración de la clase**:
   - El código está organizado en el paquete `tiempotransmisionurl`.
   - La clase `HiloBoton` extiende `Thread` y se encarga de medir el tiempo de transmisión de un recurso URL.

2. **Importaciones**:
   - Se importan las clases necesarias para manejar flujos de entrada/salida (`java.io.*`) y conexiones de red (`java.net.*`).

3. **Variables locales**:
   - `cadenaURL`: Almacena la URL del recurso que se va a medir.

4. **Constructor**:
   - El constructor recibe la URL como parámetro y la asigna a la variable `cadenaURL`.

5. **Método `run()`**:
   - Este método contiene el código que se ejecuta cuando el hilo inicia.
   - Se realiza una conexión implícita con el servidor utilizando `URL` y `URLConnection`.
   - Se fuerza la transmisión del recurso leyendo todos los bytes del flujo de entrada (`InputStream`).
   - Se calcula el tiempo de transmisión comparando el tiempo de inicio (obtenido del encabezado `Date`) y el tiempo de finalización (obtenido con `System.currentTimeMillis()`).
   - Se muestra el tiempo de transmisión en la consola.

6. **Manejo de excepciones**:
   - Se capturan y manejan excepciones como `MalformedURLException` (si la URL no es válida) e `IOException` (si ocurre un error de lectura/escritura).

7. **Finalización**:
   - El programa termina después de mostrar el tiempo de transmisión.

#### Ejemplo de uso

1. **Crear una instancia de `HiloBoton`**:
   - Proporciona una URL válida como argumento al constructor.

2. **Iniciar el hilo**:
   - Llama al método `start()` en la instancia de `HiloBoton` para iniciar la ejecución del hilo.

3. **Verificar la salida**:
   - El hilo se conecta al servidor, mide el tiempo de transmisión del recurso y muestra el resultado en la consola.

#### Ejemplo de salida en la consola

```terminal
El tiempo de transmisión del recurso ha sido de 250ms
```

Este código es un ejemplo básico y puede extenderse para manejar más casos, como la medición de múltiples recursos, la validación de URLs, o la integración en una interfaz gráfica.
