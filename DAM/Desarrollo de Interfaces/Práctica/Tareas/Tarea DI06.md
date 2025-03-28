---
banner: "![[di.jpg]]"
banner_y: 0.76
number headings: max 2, _.1.1., skip ^sk
cssclasses:
  - dam-di
  - table-compact-clean
tags:
  - DAM
  - DI
---

# Tarea **DI06**

## Dominio del problema

Ha llegado el momento de documentar nuestras aplicaciones para ayudar a los usuarios y a otros colaboradores del proyecto a utilizarlas y desarrollarlas correctamente.

## Especificaciones

En primer lugar, sincronizaremos nuestras aplicaciones con una base de datos maestra alojada en la nube. Por lo tanto, la primera tarea será adaptar el código de la aplicación para que funcione con la base de datos alojada en Azure.

Aquí se incluye un mensaje del foro con más detalles:

> **Bon dia**, en la tarea de esta unidad, uno de los apartados será hacer el manual de usuario de la aplicación que desarrolló un compañer@ en la unidad anterior.  
> Para unificar los datos con los que trabajamos, utilizaremos la misma base de datos en todas las aplicaciones.  
> Por ello, lo primero que debemos hacer es actualizar la *connection string* de la base de datos en vuestra aplicación y comprobar que funciona correctamente y muestra los datos.  
> Aquí tenéis la *connection string*:

```
String connectionStringAzureSQLServer = "jdbc:sqlserver://simulapsqlserver.database.windows.net:1433;database=simulapdb25;user=simulapdbadmin@simulapsqlserver;password=Pwd1234.;encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.database.windows.net;loginTimeout=30;";
```

Como podéis ver, se proporcionan las credenciales del usuario administrador de la base de datos. Sabemos que esto **no es una buena práctica**, pero nos permite desarrollar con más flexibilidad. **Se ruega precaución** al realizar inserciones, actualizaciones y eliminaciones, ya que otros grupos también están utilizando la misma base de datos. En caso de problemas, hay una copia de seguridad disponible.

Podéis acceder a la base de datos remota a través de *SQL Server Management Studio* o *Azure Data Studio* creando una conexión específica.  
Es posible que tengáis que adaptar vuestro código para que los campos de las tablas coincidan con los de la base de datos online. **No modifiquéis la estructura de las tablas ni los campos.** Si necesitáis algún cambio, contactad con el instructor.

> **IMPORTANTE.**  
> La contraseña del usuario instructor **Dr. Otero** para la base de datos es `'string'`.

Además, debéis hacer un **commit** en vuestro repositorio con las credenciales actualizadas.  
El repositorio de la tarea debe ser público, así que si aún no lo es, cambiadlo en *GitHub*.

Si vuestra aplicación usa alguna dependencia externa (como un componente de calendario), debéis indicarlo en la documentación y explicar cómo añadirlo al proyecto. Otra opción es generar un `.jar` con las dependencias incluidas (*maven-shaded-plugin*) y publicarlo en *GitHub* como *release* para que el compañero que haga la documentación pueda ejecutarlo sin necesidad de clonar y abrir el proyecto en *NetBeans*.

En el enunciado de la tarea se indica cómo y dónde debéis hacer el manual de usuario.

## Tareas

### **1ª Tarea: Migrar la aplicación**

Debéis modificar vuestra aplicación para que utilice la base de datos establecida y el servidor de archivos correspondiente.

### **2ª Tarea: Documentación Javadoc**

Debéis documentar las clases, métodos y propiedades del proyecto con comentarios Javadoc, proporcionando toda la información útil para otros desarrolladores.

Pasos a seguir:

- Añadir comentarios Javadoc a todas las clases, métodos y propiedades importantes.
- Generar la documentación HTML usando el *maven-javadoc-plugin*.
- Configurar la generación automática de la documentación al hacer *Build* en *NetBeans*.
- Guardar la documentación en `directorio_raíz_proyecto/doc` (al mismo nivel que `/src` y `/target`).
- Hacer *push* para subir la documentación al repositorio en *GitHub*.

### **3ª Tarea: Hacer el repositorio público y escribir el Manual de Usuario**

- Hacer el repositorio público para que otros puedan clonar, descargar y probar la aplicación.
- Escribir un **Manual de Usuario** para la aplicación de un compañero asignado al azar.
- El manual debe redactarse en **Markdown** y publicarse en la wiki del repositorio en *GitHub*.
- Para editar la wiki de otro repositorio, el propietario debe añadir al redactor como colaborador.
- Si es necesario, se pueden hacer públicos otros repositorios relacionados con el proyecto.

📌 **Todas las solicitudes y comunicaciones deben realizarse a través de los *Issues* de GitHub.**  
Si necesitáis información sobre el proyecto, publicad un *issue* en el repositorio del compañero.

El **Manual de Usuario** debe seguir las pautas y buenas prácticas indicadas en los apuntes de clase y en el tutorial de *OpenWebinars*.

- Debe estar bien redactado, incluir imágenes y animaciones.
- Debe ser claro, inteligible y visualmente atractivo para mejorar la experiencia de usuario (*UX*).

### **4ª Tarea: Reportar *Issues* en GitHub**

Como parte de la documentación, debéis crear al menos **dos *issues*** en el repositorio del compañero al que hacéis la documentación:

1. **Un *issue* sobre usabilidad** (algo que pueda mejorarse para facilitar su uso).
2. **Otro *issue* a elección** (puede ser un bug, una nueva funcionalidad, etc.).

📌 **Referencias recomendadas.**  
Para aprender a escribir un informe de errores (*bug report*), podéis consultar:  
🔗 [https://marker.io/blog/how-to-write-bug-report](https://marker.io/blog/how-to-write-bug-report).

⚠️ **Importante.**  
Esta tarea ya se hizo en la unidad 3, pero de manera más informal. Ahora se debe seguir rigurosamente la guía para escribir *bug reports* y documentación técnica.

## Criterios de calificación

|Tarea|Puntos|
|---|---|
|Modificar el código para usar la base de datos en Azure|**1p**|
|Documentación Javadoc|**3p**|
|Manual de usuario|**4p**|
|Issues en GitHub|**2p**|

## Recursos necesarios

- *Connection string* de la base de datos en Azure.
- Proyectos entregados en unidades anteriores.
- Herramientas de documentación técnica.
- Repositorio de GitHub.

## Indicaciones de entrega

1. Subir la solución y la aplicación migrada a la nueva base de datos en vuestro repositorio de GitHub.
2. Enviar el enlace del repositorio en la tarea de *Moodle* en cuanto lo creéis.
3. Indicar en *Moodle* el compañero al que habéis hecho el Manual de Usuario y enlazar a la wiki.
4. Enviar también los enlaces a los *Issues* creados en otros repositorios.

📌 **Citación de código.**  
Si utilizáis código ajeno (por ejemplo, de *Stack Overflow*, *ChatGPT* o un compañero), citad la fuente en vuestro código.  
🔗 [http://integrity.mit.edu/handbook/writing-code](http://integrity.mit.edu/handbook/writing-code).

⚠️ **No copiéis código de otros compañeros.** Si usáis código externo, aseguraos de entenderlo y respetad las licencias.

## Hitos y fechas clave

📅 **17/03/2025** → Adaptar código a la BBDD, hacer público el repositorio y añadir al compañero como colaborador.  
📅 **25/03/2025** → Documentación Javadoc.  
📅 **01/04/2025** → Manual de Usuario y *Issues* en GitHub.  
📅 **03/04/2025 @ 23:55** → **Fecha límite de entrega.**
