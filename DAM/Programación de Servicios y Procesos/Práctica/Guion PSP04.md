---
tags: [DAM, PSP]
cssclasses:
  - dam-psp
  - table-compact-clean
banner: "![[psp.jpg]]"
banner_y: 0.26
---

# Guion **PSP04**

## 1. Crear una API REST en Java

Para este ejercicio, utilizaremos **JAX-RS con Jersey**, que es lo que se menciona en la documentación como referencia. Jersey es una implementación de JAX-RS (Java API for RESTful Web Services) y nos permite construir APIs REST de manera sencilla.

### 1.1. **Configurar el proyecto con Maven**

Si estás usando **IntelliJ**, sigue estos pasos para configurar un proyecto con Jersey:

1. Crea un nuevo proyecto Maven en IntelliJ.
2. Abre el archivo `pom.xml` y añade las siguientes dependencias:

```xml
<dependencies>
    <!-- Jersey para JAX-RS -->
    <dependency>
        <groupId>org.glassfish.jersey.core</groupId>
        <artifactId>jersey-common</artifactId>
        <version>2.34</version>
    </dependency>
    <dependency>
        <groupId>org.glassfish.jersey.containers</groupId>
        <artifactId>jersey-container-servlet</artifactId>
        <version>2.34</version>
    </dependency>
    <dependency>
        <groupId>org.glassfish.jersey.inject</groupId>
        <artifactId>jersey-hk2</artifactId>
        <version>2.34</version>
    </dependency>

    <!-- JSON processing -->
    <dependency>
        <groupId>org.glassfish.jersey.media</groupId>
        <artifactId>jersey-media-json-jackson</artifactId>
        <version>2.34</version>
    </dependency>

    <!-- Servidor embebido para pruebas -->
    <dependency>
        <groupId>org.eclipse.jetty</groupId>
        <artifactId>jetty-server</artifactId>
        <version>9.4.35.v20201120</version>
    </dependency>
    <dependency>
        <groupId>org.eclipse.jetty</groupId>
        <artifactId>jetty-servlet</artifactId>
        <version>9.4.35.v20201120</version>
    </dependency>
</dependencies>
```

### 1.2. **Crear la estructura del proyecto**

Dentro de `src/main/java`, crea los siguientes paquetes y clases:

```terminal
src
 ├── main
 │   ├── java
 │   │   ├── com.miapi
 │   │   │   ├── Main.java
 │   │   │   ├── Obra.java
 │   │   │   ├── ObraService.java
 │   │   │   ├── ObraResource.java
 │   │   │   ├── JerseyConfig.java
```

### 1.3. **Definir la entidad "Obra"**

En `Obra.java`, definimos la estructura de una obra.

```java
package com.miapi;

public class Obra {
    private int id;
    private String titulo;
    private String anyo;
    private String modalidad;
    private String autor;

    public Obra() {}

    public Obra(int id, String titulo, String anyo, String modalidad, String autor) {
        this.id = id;
        this.titulo = titulo;
        this.anyo = anyo;
        this.modalidad = modalidad;
        this.autor = autor;
    }

    // Getters y Setters
    public int getId() { return id; }
    public void setId(int id) { this.id = id; }

    public String getTitulo() { return titulo; }
    public void setTitulo(String titulo) { this.titulo = titulo; }

    public String getAnyo() { return anyo; }
    public void setAnyo(String anyo) { this.anyo = anyo; }

    public String getModalidad() { return modalidad; }
    public void setModalidad(String modalidad) { this.modalidad = modalidad; }

    public String getAutor() { return autor; }
    public void setAutor(String autor) { this.autor = autor; }
}
```

### 1.4. **Implementar el servicio (CRUD)**

En `ObraService.java`, creamos una lista en memoria para gestionar las obras.

```java
package com.miapi;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public class ObraService {
    private static List<Obra> obras = new ArrayList<>();
    private static int contadorId = 1;

    public List<Obra> getAllObras() {
        return obras;
    }

    public Obra getObraById(int id) {
        return obras.stream().filter(o -> o.getId() == id).findFirst().orElse(null);
    }

    public List<Obra> getObrasByAutor(String autor) {
        List<Obra> resultado = new ArrayList<>();
        for (Obra obra : obras) {
            if (obra.getAutor().equalsIgnoreCase(autor)) {
                resultado.add(obra);
            }
        }
        return resultado;
    }

    public Obra addObra(Obra obra) {
        obra.setId(contadorId++);
        obras.add(obra);
        return obra;
    }

    public boolean updateObra(int id, Obra obraActualizada) {
        Optional<Obra> obraOpt = obras.stream().filter(o -> o.getId() == id).findFirst();
        if (obraOpt.isPresent()) {
            Obra obra = obraOpt.get();
            obra.setTitulo(obraActualizada.getTitulo());
            obra.setAnyo(obraActualizada.getAnyo());
            obra.setModalidad(obraActualizada.getModalidad());
            obra.setAutor(obraActualizada.getAutor());
            return true;
        }
        return false;
    }

    public boolean deleteObra(int id) {
        return obras.removeIf(o -> o.getId() == id);
    }
}
```

### 1.5. **Crear el controlador REST**

En `ObraResource.java`, implementamos los endpoints REST.

```java
package com.miapi;

import jakarta.ws.rs.*;
import jakarta.ws.rs.core.MediaType;
import java.util.List;

@Path("/obras")
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
public class ObraResource {
    private ObraService obraService = new ObraService();

    @GET
    public List<Obra> getObras() {
        return obraService.getAllObras();
    }

    @GET
    @Path("/{id}")
    public Obra getObra(@PathParam("id") int id) {
        return obraService.getObraById(id);
    }

    @GET
    @Path("/autor/{autor}")
    public List<Obra> getObrasPorAutor(@PathParam("autor") String autor) {
        return obraService.getObrasByAutor(autor);
    }

    @POST
    public Obra crearObra(Obra obra) {
        return obraService.addObra(obra);
    }

    @PUT
    @Path("/{id}")
    public boolean actualizarObra(@PathParam("id") int id, Obra obra) {
        return obraService.updateObra(id, obra);
    }

    @DELETE
    @Path("/{id}")
    public boolean eliminarObra(@PathParam("id") int id) {
        return obraService.deleteObra(id);
    }
}
```

### 1.6. **Configurar Jersey**

En `JerseyConfig.java`, registramos los recursos.

```java
package com.miapi;

import org.glassfish.jersey.server.ResourceConfig;
import jakarta.ws.rs.ApplicationPath;

@ApplicationPath("/api")
public class JerseyConfig extends ResourceConfig {
    public JerseyConfig() {
        packages("com.miapi");
    }
}
```

### 1.7. **Arrancar el servidor**

Crea `Main.java` para iniciar un servidor embebido con Jetty.

```java
package com.miapi;

import org.eclipse.jetty.server.Server;
import org.eclipse.jetty.servlet.ServletContextHandler;
import org.glassfish.jersey.servlet.ServletContainer;

public class Main {
    public static void main(String[] args) throws Exception {
        Server server = new Server(8080);
        ServletContextHandler context = new ServletContextHandler(ServletContextHandler.SESSIONS);
        context.setContextPath("/");
        server.setHandler(context);
        context.addServlet(ServletContainer.class, "/api/*");
        server.start();
        server.join();
    }
}
```

---

Ahora puedes probarlo con **Postman** o el navegador:

- `GET http://localhost:8080/api/obras`
- `POST http://localhost:8080/api/obras` (con JSON en el body)

Vale, vamos con el **cliente SMTP en Java.**

## 2. Crear un cliente SMTP en Java

SMTP (Simple Mail Transfer Protocol) es el protocolo estándar para enviar correos electrónicos. En este caso, programaremos un cliente en **Java** que se conecte a un servidor SMTP y envíe correos.

### 2.1. **Elegir una forma de envío**

Tenemos dos opciones para implementar el cliente SMTP:

1. **Con sockets directamente** (bajo nivel).
2. **Usando la librería `javax.mail`** (alto nivel y más recomendable).

Vamos a hacer ambas para que veas las diferencias.

## 3. Opción 1: <br>Cliente SMTP con sockets (bajo nivel)

Aquí conectamos manualmente al servidor SMTP en el puerto **25** (o 587 para TLS).

### 3.1. **Código**

```java
import java.io.*;
import java.net.Socket;

public class ClienteSMTP {
    public static void main(String[] args) {
        String smtpServer = "alt1.gmail-smtp-in.l.google.com"; // Servidor SMTP de Google
        int puerto = 25;

        try {
            // Conectamos con el servidor SMTP
            Socket socket = new Socket(smtpServer, puerto);
            BufferedReader entrada = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter salida = new PrintWriter(socket.getOutputStream(), true);

            // Leer respuesta inicial del servidor
            System.out.println(entrada.readLine());

            // Enviar saludo al servidor SMTP
            salida.println("HELO example.com");
            System.out.println(entrada.readLine());

            // Indicar quién envía el correo
            salida.println("MAIL FROM: <tuemail@gmail.com>");
            System.out.println(entrada.readLine());

            // Indicar destinatario
            salida.println("RCPT TO: <destinatario@gmail.com>");
            System.out.println(entrada.readLine());

            // Indicar que se enviará un mensaje
            salida.println("DATA");
            System.out.println(entrada.readLine());

            // Escribir el mensaje
            salida.println("Subject: Prueba SMTP desde Java");
            salida.println("From: tuemail@gmail.com");
            salida.println("To: destinatario@gmail.com");
            salida.println("");
            salida.println("Hola, este es un correo de prueba enviado desde un cliente SMTP en Java.");
            salida.println(".");
            System.out.println(entrada.readLine());

            // Cerrar conexión
            salida.println("QUIT");
            System.out.println(entrada.readLine());

            // Cerrar recursos
            salida.close();
            entrada.close();
            socket.close();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### 3.2. **Notas importantes**

🔹 **Este método es obsoleto**, ya que la mayoría de los servidores SMTP requieren autenticación y cifrado (SSL/TLS).  
🔹 **No funcionará con Gmail** a menos que uses un servidor sin autenticación.  
🔹 **Alternativa recomendada.** Usar `javax.mail`.

## 4. Opción 2: <br>Cliente SMTP con `javax.mail` (recomendado)

Este método es más seguro y compatible con los servidores modernos.

### 4.1. **Agregar dependencias en Maven**

Si usas **Maven**, añade esto en `pom.xml`:

```xml
<dependency>
    <groupId>com.sun.mail</groupId>
    <artifactId>javax.mail</artifactId>
    <version>1.6.2</version>
</dependency>
```

Si no usas Maven, puedes descargar la librería de **[javax.mail](https://javaee.github.io/javamail/).**

### 4.2. **Código del Cliente SMTP con autenticación y TLS**

Este código envía un correo mediante **Gmail** u otro servidor SMTP con autenticación.

```java
import java.util.Properties;
import javax.mail.*;
import javax.mail.internet.*;

public class ClienteSMTPSeguro {
    public static void main(String[] args) {
        // Datos de la cuenta SMTP
        final String usuario = "tuemail@gmail.com";  // Cambia esto
        final String contraseña = "tucontraseña";    // O usa una contraseña de aplicación

        // Configuración del servidor SMTP
        Properties props = new Properties();
        props.put("mail.smtp.host", "smtp.gmail.com");  // Servidor SMTP
        props.put("mail.smtp.port", "587");             // Puerto TLS
        props.put("mail.smtp.auth", "true");            // Requiere autenticación
        props.put("mail.smtp.starttls.enable", "true"); // Habilita TLS

        // Crear una sesión con autenticación
        Session sesion = Session.getInstance(props, new Authenticator() {
            protected PasswordAuthentication getPasswordAuthentication() {
                return new PasswordAuthentication(usuario, contraseña);
            }
        });

        try {
            // Crear el mensaje
            Message mensaje = new MimeMessage(sesion);
            mensaje.setFrom(new InternetAddress(usuario));
            mensaje.setRecipients(Message.RecipientType.TO, InternetAddress.parse("destinatario@gmail.com"));
            mensaje.setSubject("Prueba de JavaMail");
            mensaje.setText("Hola, este es un correo de prueba enviado desde Java usando javax.mail.");

            // Enviar el mensaje
            Transport.send(mensaje);
            System.out.println("Correo enviado correctamente");

        } catch (MessagingException e) {
            e.printStackTrace();
        }
    }
}
```

### 4.3. **Explicación**

✅ **Seguridad:**

- Usa **TLS** en el puerto `587` (Gmail no permite envíos sin autenticación).
- Alternativamente, podrías usar **SSL** en el puerto `465` con `mail.smtp.ssl.enable`.

✅ **Autenticación:**

- Se requiere una cuenta de correo válida (`usuario` y `contraseña`).
- Si usas **Gmail**, necesitas habilitar `Acceso de apps menos seguras` o generar una `Contraseña de Aplicación`.

✅ **Formato del correo:**

- El método `setText()` define el cuerpo del mensaje.
- Para **HTML**, usa `setContent("<html>...</html>", "text/html")`.

### 4.4. **Otras mejoras**

Si quieres **adjuntar archivos**, usa este código:

```java
MimeBodyPart adjunto = new MimeBodyPart();
adjunto.attachFile("ruta/al/archivo.pdf");
Multipart multipart = new MimeMultipart();
multipart.addBodyPart(adjunto);
mensaje.setContent(multipart);
```

### 4.5. **¿Cómo probarlo?**

1. Cambia `usuario` y `contraseña` por tu correo de prueba.  
2. Modifica `destinatario@gmail.com` por la dirección a la que quieres enviar.  
3. Ejecuta el programa y verifica tu bandeja de entrada.

Perfecto, ahora vamos con el **cliente FTP en Java.**

## 5. Crear un cliente FTP en Java

FTP (**File Transfer Protocol**) es un protocolo para transferir archivos entre un cliente y un servidor.

### 5.1. **Opciones para implementar un cliente FTP**

1. **Usando sockets directamente** (bajo nivel, complejo y poco recomendable).
2. **Usando Apache Commons Net** (alto nivel, más fácil y seguro).

Nos centraremos en la **segunda opción** usando la librería **Apache Commons Net.**

### 5.2. **Agregar la dependencia en Maven**

Si usas **Maven**, añade esta dependencia en `pom.xml`:

```xml
<dependency>
    <groupId>commons-net</groupId>
    <artifactId>commons-net</artifactId>
    <version>3.9.0</version>
</dependency>
```

Si no usas Maven, puedes descargar la librería desde [Apache Commons Net](https://commons.apache.org/proper/commons-net/download_net.cgi).

### 5.3. **Cliente FTP básico (conexión y listado de archivos)**

Este código se conecta a un **servidor FTP**, inicia sesión y lista los archivos del directorio actual.

```java
import org.apache.commons.net.ftp.FTPClient;
import java.io.IOException;

public class ClienteFTP {
    public static void main(String[] args) {
        String servidor = "test.rebex.net";  // Servidor de prueba
        int puerto = 21;                     // Puerto FTP estándar
        String usuario = "demo";             // Usuario de prueba
        String contraseña = "password";      // Contraseña de prueba

        FTPClient ftpClient = new FTPClient();

        try {
            // Conectar al servidor
            ftpClient.connect(servidor, puerto);
            System.out.println("Conectado a " + servidor);

            // Iniciar sesión
            boolean login = ftpClient.login(usuario, contraseña);
            if (login) {
                System.out.println("Inicio de sesión exitoso.");
            } else {
                System.out.println("Error al iniciar sesión.");
                return;
            }

            // Listar archivos del directorio actual
            System.out.println("Archivos en el directorio:");
            String[] archivos = ftpClient.listNames();
            for (String archivo : archivos) {
                System.out.println("- " + archivo);
            }

            // Cerrar sesión y desconectar
            ftpClient.logout();
            ftpClient.disconnect();
            System.out.println("Desconectado del servidor.");

        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
            ex.printStackTrace();
        }
    }
}
```

### 5.4. **Explicación**

✅ **Se conecta a un servidor FTP en el puerto `21`.**  
✅ **Inicia sesión con usuario y contraseña** (usa credenciales de prueba).  
✅ **Lista archivos del directorio actual.**  
✅ **Se desconecta al finalizar.**

### 5.5. **Cliente FTP con descarga de archivos**

Este código **descarga un archivo** desde el servidor FTP.

```java
import org.apache.commons.net.ftp.FTPClient;
import java.io.FileOutputStream;
import java.io.IOException;

public class ClienteFTPDescarga {
    public static void main(String[] args) {
        String servidor = "test.rebex.net";
        int puerto = 21;
        String usuario = "demo";
        String contraseña = "password";
        String archivoRemoto = "readme.txt";  // Archivo en el servidor
        String archivoLocal = "descargado.txt";  // Nombre local

        FTPClient ftpClient = new FTPClient();

        try {
            ftpClient.connect(servidor, puerto);
            ftpClient.login(usuario, contraseña);

            // Descargar el archivo
            FileOutputStream fos = new FileOutputStream(archivoLocal);
            boolean exito = ftpClient.retrieveFile(archivoRemoto, fos);
            fos.close();

            if (exito) {
                System.out.println("Archivo descargado correctamente: " + archivoLocal);
            } else {
                System.out.println("No se pudo descargar el archivo.");
            }

            ftpClient.logout();
            ftpClient.disconnect();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
}
```

*Explicación*

✅ **Descarga un archivo desde el servidor.**  
✅ **Usa `retrieveFile()` para recibir el archivo y guardarlo localmente.**  
✅ **Guarda el archivo en `descargado.txt`.**

### 5.6. **Cliente FTP con subida de archivos**

Este código **sube un archivo** al servidor FTP.

```java
import org.apache.commons.net.ftp.FTP;
import org.apache.commons.net.ftp.FTPClient;
import java.io.FileInputStream;
import java.io.IOException;

public class ClienteFTPUpload {
    public static void main(String[] args) {
        String servidor = "test.rebex.net";
        int puerto = 21;
        String usuario = "demo";
        String contraseña = "password";
        String archivoLocal = "archivo.txt";  // Archivo a subir
        String archivoRemoto = "subido.txt";  // Nombre en el servidor

        FTPClient ftpClient = new FTPClient();

        try {
            ftpClient.connect(servidor, puerto);
            ftpClient.login(usuario, contraseña);

            // Configurar modo binario para archivos no textuales
            ftpClient.setFileType(FTP.BINARY_FILE_TYPE);

            // Subir archivo
            FileInputStream fis = new FileInputStream(archivoLocal);
            boolean exito = ftpClient.storeFile(archivoRemoto, fis);
            fis.close();

            if (exito) {
                System.out.println("Archivo subido correctamente.");
            } else {
                System.out.println("Error al subir el archivo.");
            }

            ftpClient.logout();
            ftpClient.disconnect();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
}
```

**Explicación**

✅ **Lee un archivo local (`archivo.txt`).**  
✅ **Usa `storeFile()` para subirlo al servidor.**  
✅ **Lo guarda como `subido.txt` en el servidor.**

### 5.7. **Cliente FTP con eliminación de archivos**

Si quieres **eliminar un archivo** en el servidor:

```java
boolean eliminado = ftpClient.deleteFile("archivo_remoto.txt");
if (eliminado) {
    System.out.println("Archivo eliminado correctamente.");
} else {
    System.out.println("No se pudo eliminar el archivo.");
}
```

### 5.8. **Cliente FTP con cambio de directorio**

Si quieres **cambiar de carpeta** en el servidor:

```java
boolean cambio = ftpClient.changeWorkingDirectory("/nueva_carpeta");
if (cambio) {
    System.out.println("Cambiado a /nueva_carpeta");
} else {
    System.out.println("No se pudo cambiar de directorio.");
}
```

### 5.9. **¿Cómo probarlo?**

1️⃣ **Ejecuta `ClienteFTP.java`** para listar archivos.  
2️⃣ **Ejecuta `ClienteFTPDescarga.java`** para descargar un archivo (`readme.txt`).  
3️⃣ **Ejecuta `ClienteFTPUpload.java`** para subir un archivo (`archivo.txt`).

Puedes usar servidores FTP públicos como:

- **<ftp://test.rebex.net>** (Usuario: `demo`, Contraseña: `password`).
- **<ftp://speedtest.tele2.net>** (Usuario: `anonymous`, sin contraseña).
