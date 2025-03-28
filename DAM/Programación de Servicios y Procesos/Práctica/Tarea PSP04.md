---
number headings: max 3, _.1.1., skip ^sk
tags:
  - DAM
  - PSP
banner: "![[psp.jpg]]"
banner_y: 0.32
cssclasses:
  - dam-psp
  - table-compact-clean
---

# Tarea **PSP04**

## 1. Instrucciones

### 1.1. **Crear una API REST**

Usando lo aprendido en clase, genera un servidor API REST que pueda gestionar la información de obras. La API debe permitir:

- Listar todas las obras.
- Listar una obra específica a partir de su ID.
- Listar las obras de un autor.
- Crear una obra nueva.
- Actualizar los campos de una obra dado su ID.
- Eliminar una obra dado su ID.

Una vez creada la API, se debe comprobar su correcto funcionamiento mediante peticiones desde un navegador o la aplicación POSTMAN.

Después, se debe desarrollar un cliente en **Java** que realice las siguientes peticiones:

- **GET** (Listar todas las obras) → `http://localhost:8080/API_REST_v1/api/obres`
- **GET** (Listar una obra por ID) → `http://localhost:8080/API_REST_v1/api/obres/7`
- **GET** (Listar las obras de un autor) → `http://localhost:8080/API_REST_v1/api/obres/Leonardo Da Vinci`
- **POST** (Crear una nueva obra) → `http://localhost:8080/API_REST_v1/api/obres/createObra`
- **PUT** (Actualizar una obra existente) → `http://localhost:8080/API_REST_v1/api/obres/updateObra`
- **DELETE** (Eliminar una obra por ID)

### 1.2. Estructura de una obra

Una obra debe contener los siguientes campos:

- **int** ID_OBRA
- **String** TITULO
- **String** AÑO
- **String** MODALIDAD
- **String** AUTOR

**Ayuda.**  
Guía para crear el servidor con **IntelliJ** disponible en el aula virtual.

- **Crear API REST.** [Tutorial Java JAX-RS Jersey](https://rosamarfil.es/tutoriales/programacion/crear-api-rest-java-jax-rs-jersey/)
- **Crear Cliente Java.** [Implementar peticiones GET y POST](https://dzone.com/articles/how-to-implement-get-and-post-request-through-simp)

### 1.3. **Crear un cliente SMTP**

Se debe desarrollar un cliente **SMTP** que se conecte al servidor `alt1.gmail-smtp-in.l.google.com` en el puerto **25** para enviar correos electrónicos.

El mensaje debe estar escrito directamente en el código y **no** debe solicitar datos al usuario por consola.

**Ejemplo de Cliente SMTP en Java.**

```java
String received = in.readLine();
System.out.println(received);
out.println("HELO example.com");
out.flush();
received = in.readLine();
System.out.println(received);
out.println("MAIL FROM: <a@gmail.com>");
out.flush();
received = in.readLine();
System.out.println(received);
out.println("RCPT TO: <jaume@gmail.com>");
out.flush();
received = in.readLine();
System.out.println(received);
```

**Nota.** Si realizas pruebas de envío, revisa la carpeta de **SPAM**, ya que es probable que los correos se almacenen allí.

### 1.4. **Crear un cliente FTP**

Se debe desarrollar un cliente **FTP** que se conecte al siguiente servidor:

- **Servidor.** `ftp://test.rebex.net`
- **Puerto.** **21** (Puerto de control)
- **Usuario.** `demo`
- **Contraseña.** `password`

El cliente debe conectarse y realizar una operación **"LIST"** para mostrar el contenido del directorio actual en el servidor.

**Consideraciones.**

- El cliente usa **dos canales de comunicación.**
	- **Canal de CONTROL** → Envía comandos.
	- **Canal de DATOS** → Recibe respuestas del servidor.
- Utilizar **modo PASV** para listar contenido.
- Solo se requiere leer y mostrar los nombres de archivos y directorios.
- **Opcional.** Subir un archivo al servidor.

**Otros servidores FTP públicos disponibles.**

1. **ftp.dlptest.com**
	
	- **Usuario.** `dlpuser`
	- **Contraseña.** `rNrKYTX9g7z3RgJRmxWuGHbeu`
2. **speedtest.tele2.net**
	
	- **Usuario.** `anonymous`
	- **Contraseña.** (cualquier correo electrónico)

**Nota.** Se debe grabar la pantalla en cada una de las pruebas de ejecución, además de entregar el código fuente.

## 2. Criterios de calificación

Para la entrega, el alumno deberá adjuntar:

- Todo el código de los proyectos.
- Un video explicativo de **máximo 6 minutos** mostrando la ejecución de las actividades.

**Puntuación.**

|Ejercicio|Puntos|
|---|---|
|1 - API REST|3 puntos|
|2 - Cliente SMTP|2 puntos|
|3 - Cliente FTP|2 puntos|
|Extra (Subir archivo FTP)|1 punto|
|Video demostrativo|2 puntos|

**IMPORTANTE.**

- Si el código **no compila o no se ejecuta correctamente**, la práctica se calificará con **0 puntos.**
- No seguir los criterios del enunciado supondrá penalizaciones en la nota final.
