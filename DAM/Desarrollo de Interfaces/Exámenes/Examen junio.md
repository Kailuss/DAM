---
cssclasses:
  - dam-di
  - table-clean
banner: "![[di.jpg]]"
number headings: off
---

# **Examen Junio** <br>Desarrollo de Interfaces

#### **1.** ¿Cuál de las siguientes afirmaciones es la correcta?

- **A.** Para ejecutar una aplicación empaquetada en un .jar es necesario que en la máquina donde se va a ejecutar esté instalado el JRE.  
- **B.** En un paquete .jar se pueden incluir las librerías necesarias del JDK para que se ejecute una aplicación Java sin necesidad de que exista el JRE en la máquina destino.  
- **C.** **En los paquetes .jar no podemos incluir las librerías del JDK que necesita una aplicación pero podemos crear un instalador .exe con Install4j que incluya el JRE y lo instale automáticamente en la máquina destino.**  
- **D.** Ninguna de las opciones anteriores es correcta.

#### **2.** Las imágenes estáticas que aparecen en la interfaz de una aplicación como iconos y logos, ¿en qué carpeta del proyecto Maven es conveniente incluirlas para evitar problemas en NetBeans al ejecutar el proyecto?

- **A.** src/images  
- **B.** target/resources  
- **C.** **src/main/resources**  
- **D.** Ninguna de las opciones anteriores es correcta.

#### **3.** ¿Qué plugin de Maven se puede utilizar para incluir los jar de las dependencias en el jar de la aplicación generado?

- **A.** maven-shade-plugin
- **B.** maven-resources-plugin  
- **C.** maven-compiler-plugin  
- **D.** **maven-dependency-plugin**

#### **4.** ¿Cuál de las siguientes afirmaciones es cierta?

- **A.** Install4j lee el pom.xml del proyecto las dependencias Maven y las descarga e incluye en el instalador automáticamente.  
- **B.** Install4j sólo permite crear instaladores para distribuir nuestra aplicación en máquinas donde ya exista instalada previamente una versión del JRE o el JDK.  
- **C.** La versión de prueba de Install4j no permite crear instaladores que necesiten elevación de privilegios para ser instalados.  
- **D.** **Para crear un instalador con Install4j, el fichero jar con la aplicación principal generado desde NetBeans debe incluir los jars de las dependencias de nuestro proyecto.**  
- **E.** **Install4j permite crear instaladores para Windows, Mac y Linux.**

#### **5.** ¿En qué sección principal del pom.xml se tiene que poner la referencia al maven-shade-plugin para que se incluyan automáticamente los jar de las dependencias de un proyecto en el .jar que se generará cuando se hace el build?

- **A.** \<repositories\>...\</repositories\>  
- **B.** \<dependencies\>...\</dependencies\>  
- **C.** **\<build\>...\</build\>**  
- **D.** \<properties\>...\</properties\>

#### **6.** ¿En qué carpeta por defecto se crea el fichero .jar generado al hacer un 'Clean and Build' de una aplicación Java Maven?

- **A.** build  
- **B.** **target**  
- **C.** dist  
- **D.** src

#### **7.** Respecto de una aplicación Java con Maven, ¿cuál de las siguientes opciones es cierta?

- **A.** Las dependencias se incluyen dentro del fichero .jar generado cuando hacemos el 'Build' de la aplicación.  
- **B.** No se puede distribuir como un paquete .jar para Linux.  
- **C.** **Siempre se debe indicar la clase principal del proyecto en el pom.xml si queremos crear un .jar distribuible en otras máquinas.**  
- **D.** Hay que copiar manualmente todos los .jar de las dependencias a la carpeta lib una vez hecho el 'Build'.

#### **8.** ¿Cuál de estas opciones es verdadera respecto a los comentarios Javadoc?  

- **A.** Es todo aquel texto en el archivo fuente que se encuentra entre los caracteres `/*` y `*/`.  
- **B.** No pueden emplear etiquetas HTML.  
- **C.** Pueden precedir métodos y propiedades de una clase, pero no a una clase ni a su constructor.  
- **D.** **Cada línea, excepto la primera y la última, comienza con el carácter `*`.**  

#### **9.** ¿Qué etiqueta Javadoc se emplea para documentar los argumentos de un método?  

- **A.** `@args`  
- **B.** **`@param`**  
- **C.** `@[tipo_de_datos_del_parámetro]`  
- **D.** `@see`

#### **10.** ¿Qué etiqueta Javadoc se emplea para documentar el valor que retorna un método?  

- **A.** `@[tipo_de_datos_del_valor_de_retorno]`  
- **B.** **`@return`**  
- **C.** `@param`  
- **D.** `@out`  

#### **11.** ¿Cuál de los siguientes formatos es exclusivo para aplicaciones Java?

- **A.** CHM
- **B.** PDF
- **C.** **JavaHelp**
- **D.** HLP

#### **12.** ¿Qué herramienta es desarrollada por Microsoft para crear archivos HLP y CHM?

- **A.** JavaHelp
- **B.** RoboHelp
- **C.** **Help Workshop**
- **D.** WebHelp

#### **13.** ¿Cuál NO es una característica de los archivos CHM?

- **A.** Compresión de datos
- **B.** Soporte para applets Java
- **C.** Soporte para búsqueda
- **D.** **Código fuente incluido**

#### **14.** ¿Qué fichero en JavaHelp define la estructura de la ayuda?

- **A.** .toc
- **B.** **.hs**
- **C.** .jhm
- **D.** .xml

#### **15.** ¿Qué clase Java se utiliza para asociar la ayuda sensible al contexto?

- **A.** HelpViewer
- **B.** HelpSet
- **C.** HelpContext
- **D.** **HelpBroker**

#### **16.** ¿Cuál es el objetivo principal del índice en un sistema de ayuda?

- **A.** Mejorar la estética
- **B.** Buscar sin conexión
- **C.** **Acceso rápido por palabras clave**
- **D.** Crear diagramas

#### **17.** ¿Qué elemento no forma parte de un fichero JAR firmado digitalmente?

- **A.** MANIFEST.MF
- **B.** Archivo .SF
- **C.** Archivo .DSA
- **D.** **Archivo .ISO**

#### **18.** ¿Qué tipo de manual proporciona información detallada para usuarios expertos?

- **A.** Manual de instalación
- **B.** Guía rápida
- **C.** Manual de usuario
- **D.** **Guía de referencia**

#### **19.** ¿Qué tipo de archivo se usa en Ubuntu para distribuir software?

- **A.** .exe
- **B.** .rpm
- **C.** **.deb**
- **D.** .jar

#### **20.** ¿Qué herramienta permite crear instaladores personalizados mediante scripts?

- **A.** InstallBuilder
- **B.** **NSIS**
- **C.** Visual Studio
- **D.** apturl

#### **21.** ¿Qué parámetro se usa en NSIS para una instalación silenciosa?

- **A.** /QUIET
- **B.** /NORESTART
- **C.** **/S**
- **D.** /silent

#### **22.** ¿Cuál es el paso que NO se realiza durante una instalación de software?

- **A.** Verificación de compatibilidad
- **B.** Registro en el sistema
- **C.** **Compilación del programa**
- **D.** Creación de accesos directos

#### **23.** ¿Qué función cumple el archivo MANIFEST.MF en un JAR?

- **A.** Almacena texto legal
- **B.** **Define la clase principal y resúmenes**
- **C.** Cifra el contenido
- **D.** Enlaza DLLs externas

#### **24.** ¿Cuál es el objetivo de los asistentes de instalación?

- **A.** Reducir tamaño del programa
- **B.** Permitir que el usuario programe
- **C.** **Guiar paso a paso el proceso de instalación**
- **D.** Ejecutar software en la nube

#### **25.** ¿Qué herramienta en Ubuntu permite instalar software desde un enlace web?

- **A.** Synaptic
- **B.** APT
- **C.** **apturl**
- **D.** dpkg

#### **26.** ¿Qué NO se considera parte de la personalización de un instalador?

- **A.** Selección de idioma
- **B.** Inclusión de logotipo
- **C.** **Compilación de código fuente**
- **D.** Estilo de botones

#### **1.** Enumera los diferentes tipos de documentación que podemos encontrar en un proyecto de software dirigidas al usuario final de la aplicación.

|**Tipo de Documentación**|**Descripción / Ejemplos**|
|---|---|
|**Documentación de Producto**|- Manual de instrucciones<br>- Manual de referencia<br>- Guías de instalación|
|**Documentación para Usuarios**|- Guías prácticas (How-to guides)<br>- Tutoriales- Documentación de referencia<br>- Explicaciones|
|**Manual de Usuario**|Documento técnico con instrucciones detalladas, capturas, solución de problemas, FAQ, glosario e índice.|
|**Guía de Referencia**|Manual para usuarios avanzados: comandos, sintaxis, mensajes de error.|
|**Guías Rápidas**|Versión resumida con tareas básicas. Ideal para usuarios con poco tiempo o aplicaciones simples.|
|**Manuales de Instalación**|Información para instalar/configurar la aplicación, requisitos, archivos, y software adicional.|
|**Configuración y Administración**|Guías para personalizar y mantener el sistema, incluyendo scripts y comandos.|
|**Ayuda en Línea / JavaHelp**|Sistema de ayuda integrado en la aplicación: mapas, índice, búsqueda, TOC y ayuda sensible al contexto.|
|**Tutoriales Multimedia**|Contenidos visuales e interactivos con herramientas como Camtasia, Wink, Adobe Captivate, etc.|

#### **2.** Indica cuáles son los tipos de documentación de un proyecto de software dirigidas al equipo de desarrollo del proyecto.

|**Tipo de Documentación**|**Descripción / Ejemplos**|
|---|---|
|**Documentación de Proyecto**|- Documentos de diseño técnico<br>- Planes de proyecto<br>- Especificaciones de requisitos|
|**Documentación de Procesos**|- Planes de desarrollo<br>- Planes de prueba<br>- Planes de lanzamiento<br>- Informes de errores|
|**Documentación Técnica**|- Documentación de API<br>- Documentación del modelo de datos<br>- Documentación de arquitectura|
||- Guía del usuario técnico- Notas de lanzamiento<br>- README|
|**Documentación del Sistema**|- Guía de resolución de problemas<br>- Documentación de arquitectura<br>- Manual técnico del sistema|
|**Herramientas de Documentación**|- Generadores automáticos<br>- Sistemas de control de versiones<br>- Bases de conocimiento colaborativas|

#### **3.** Explica de forma esquemática pero precisa cuál es el procedimiento que hay que seguir para crear un instalador para Windows de una aplicación Java utilizando la herramienta Install4j. Se ha de tener en cuenta que la aplicación Java puede tener dependencias y recursos externos que también hay que desplegar o instalar en las máquinas destino.

##### ✅ Procedimiento para crear un instalador con Install4j para una aplicación Java (con dependencias)

|**Etapa**|**Pasos y detalles**|
|---|---|
|**1. Preparación del proyecto**|- Asegurarse de que la aplicación Java esté completamente desarrollada y probada.|
|**2. Uso de Shade Plugin (Maven)**|- Usar el plugin `maven-shade-plugin` para empaquetar todas las dependencias en un solo `.jar`.<br>- Esto genera un _fat JAR_ ejecutable.<br>- Se debe definir la clase `Main-Class` en el `MANIFEST.MF`. **Ruta de salida:** `target\carpetaBuild`|
|**3. Configuración del proyecto en Install4j**|- Crear un nuevo proyecto en **Install4j**.<br>- Definir el directorio base del proyecto como: `target\carpetaBuild`.|

##### 🧭 Launcher Configuration

|Elemento|Detalles|
|---|---|
|**Nombre del ejecutable**|`MiAplicacion.exe` o el nombre deseado.|
|**Ruta de logs**|`logs\app.log` (configurable dentro del directorio de instalación).|
|**Nivel de ejecución**|**Administrador**, si la app necesita escribir en `Program Files` u otras rutas protegidas.|
|**Icono del launcher**|Archivo `.ico` personalizado (por ejemplo: `src\main\resources\icono.ico`).|
|**JAR objetivo**|JAR generado por el Shade plugin (ej: `miAppConDependencias.jar`).|
|**Clase Main**|`com.miempresa.miapp.Main` o la que corresponda.|
|**Splash Screen**|Imagen en `.png` o `.jpg` mostrada mientras arranca la app.|

##### 💻 Media Configuration

|Elemento|Detalles|
|---|---|
|**Tipo de SO**|**Windows 64-bit** o ambas arquitecturas si se desea compatibilidad ampliada.|
|**Bundle de JRE**|Incluir un **JRE embebido** (por ejemplo: una distribución de OpenJDK o Azul Zulu). Esto garantiza que la aplicación funcione sin requerir JDK externo en la máquina destino.|  

##### 🧰 Installer Configuration

|Elemento|Detalles|
|---|---|
|**Acceso directo al escritorio**|Crear acceso directo con nombre e ícono.|
|**Copia de ficheros**|- Copiar el `.jar`, dependencias, `config`, `logs`, etc. a subcarpetas específicas.<br>- Establecer variables de entorno o rutas si es necesario.|
|**Configuraciones adicionales**|- Crear entradas en el menú inicio.<br>- Configurar permisos.|

##### ⚙️ Build del instalador

|Paso|Detalle|
|---|---|
|**Compilar instalador**|- Seleccionar `Build Installer`.<br>- Se generará un archivo `.exe` instalable (ej. `setup.exe`).|
|**Opcional**|- Crear instaladores firmados digitalmente.<br>- Crear versiones portables o para otros SO si se desea.|

#### **4.** Explica detalladamente qué hay que hacer en Install4j para crear una carpeta en `C:\Users\[usuario]\AppData\Local` y que se escriban en ella un conjunto de ficheros cuando la aplicación se instale.

1. En el paso de Installer añadiremos la opción "Copy files and directories".  
2. En la ruta origen seleccionaremos la carpeta con el conjunto de ficheros.  
3. En la ruta destino usaremos las variables del Install4j `sys.localappdata` y le añadiremos `\\nombreCarpeta`.  
4. De este modo nos va a crear la carpeta con todo su contenido en `%localAppdata%`.

#### **5.** Diferencias entre `maven-shade-plugin` y `maven-depandency-pluing`

La diferencia entre **`maven-shade-plugin`** y **`maven-dependency-plugin`** radica principalmente en **qué hacen con las dependencias** y **cómo preparan el paquete final**.

##### 🧩 Comparación: Shade Plugin vs Dependency Plugin

|**Característica**|**`maven-shade-plugin`**|**`maven-dependency-plugin`**|
|---|---|---|
|**Propósito principal**|Empaquetar **todas las dependencias** en un solo archivo `.jar` ("fat JAR").|Copiar dependencias o archivos a una ubicación específica del proyecto.|
|**Resultado típico**|Un `.jar` ejecutable con todas las clases y recursos necesarios.|Copia las dependencias en `target/lib` o similar (no las empaqueta).|
|**Uso común**|Crear un único `.jar` listo para distribución o integración con instaladores.|Preparar directorios para distribuciones manuales o scripts personalizados.|
|**Transformación de clases o recursos**|Sí. Puede reubicar paquetes, combinar `META-INF`, modificar el `MANIFEST`, etc.|No. Solo copia archivos, no los modifica.|
|**Define Main-Class en MANIFEST**|**Sí**, mediante el `ManifestResourceTransformer`.| **No**. Se debe configurar aparte si se usa para ejecución.|
|**Típico en proyectos con**|Instaladores (Install4j, Inno Setup), ejecutables únicos, apps con muchas dependencias.|Scripts de instalación, proyectos que requieren estructura de carpetas.|

##### 🛠️ Ejemplo de uso

###### `maven-shade-plugin` (fat JAR con todo)

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-shade-plugin</artifactId>
  ...
</plugin>
```

**Resultado:** `target/miApp-jar-con-todo.jar`

###### `maven-dependency-plugin` (copiar dependencias)

```xml
<plugin>
  <artifactId>maven-dependency-plugin</artifactId>
  <executions>
    <execution>
      <id>copy-dependencies</id>
      <phase>package</phase>
      <goals><goal>copy-dependencies</goal></goals>
    </execution>
  </executions>
</plugin>
```

**Resultado:** Copia todos los `.jar` de dependencias en `target/dependency/`

##### 🧠 ¿Cuándo usar uno u otro?

|**Caso**|**Plugin recomendado**|
|---|---|
|Quieres un solo `.jar` ejecutable con todo|✅ `shade-plugin`|
|Necesitas copiar dependencias a una carpeta|✅ `dependency-plugin`|
|Vas a crear un instalador con Install4j|✅ `shade-plugin` (ideal)|
|Vas a distribuir archivos sueltos o scripts|✅ `dependency-plugin`|