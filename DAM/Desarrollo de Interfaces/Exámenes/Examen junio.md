---
cssclasses:
  - dam-di
  - table-clean
banner: "![[di.jpg]]"
number headings: off
---

# **Examen Junio** <br>Desarrollo de Interfaces

## Preguntas tipo test

#### **1.** ¿Cuál de las siguientes afirmaciones es la correcta?

- [ ] Para ejecutar una aplicación empaquetada en un .jar es necesario que en la máquina donde se va a ejecutar esté instalado el JRE.  
- [ ] En un paquete .jar se pueden incluir las librerías necesarias del JDK para que se ejecute una aplicación Java sin necesidad de que exista el JRE en la máquina destino.  
- [x] **En los paquetes .jar no podemos incluir las librerías del JDK que necesita una aplicación pero podemos crear un instalador .exe con Install4j que incluya el JRE y lo instale automáticamente en la máquina destino.**  
- [ ] Ninguna de las opciones anteriores es correcta.

#### **2.** Las imágenes estáticas que aparecen en la interfaz de una aplicación como iconos y logos, ¿en qué carpeta del proyecto Maven es conveniente incluirlas para evitar problemas en NetBeans al ejecutar el proyecto?

- [ ] src/images  
- [ ] target/resources  
- [x] **src/main/resources**  
- [ ] Ninguna de las opciones anteriores es correcta.

#### **3.** ¿Qué plugin de Maven se puede utilizar para incluir los jar de las dependencias en el jar de la aplicación generado?

- [ ] maven-shade-plugin
- [ ] maven-resources-plugin  
- [ ] maven-compiler-plugin  
- [x] **maven-dependency-plugin**

#### **4.** ¿Cuál de las siguientes afirmaciones es cierta?

- [ ] Install4j lee el pom.xml del proyecto las dependencias Maven y las descarga e incluye en el instalador automáticamente.  
- [ ] Install4j sólo permite crear instaladores para distribuir nuestra aplicación en máquinas donde ya exista instalada previamente una versión del JRE o el JDK.  
- [ ] La versión de prueba de Install4j no permite crear instaladores que necesiten elevación de privilegios para ser instalados.  
- [x] **Para crear un instalador con Install4j, el fichero jar con la aplicación principal generado desde NetBeans debe incluir los jars de las dependencias de nuestro proyecto.**  
- [x] **Install4j permite crear instaladores para Windows, Mac y Linux.**

#### **5.** ¿En qué sección principal del pom.xml se tiene que poner la referencia al maven-shade-plugin para que se incluyan automáticamente los jar de las dependencias de un proyecto en el .jar que se generará cuando se hace el build?

- [ ] \<repositories\>...\</repositories\>  
- [ ] \<dependencies\>...\</dependencies\>  
- [x] **\<build\>...\</build\>**  
- [ ] \<properties\>...\</properties\>

#### **6.** ¿En qué carpeta por defecto se crea el fichero .jar generado al hacer un 'Clean and Build' de una aplicación Java Maven?

- [ ] build  
- [x] **target**  
- [ ] dist  
- [ ] src

#### **7.** Respecto de una aplicación Java con Maven, ¿cuál de las siguientes opciones es cierta?

- [ ] Las dependencias se incluyen dentro del fichero .jar generado cuando hacemos el 'Build' de la aplicación.  
- [ ] No se puede distribuir como un paquete .jar para Linux.  
- [x] **Siempre se debe indicar la clase principal del proyecto en el pom.xml si queremos crear un .jar distribuible en otras máquinas.**  
- [ ] Hay que copiar manualmente todos los .jar de las dependencias a la carpeta lib una vez hecho el 'Build'.

#### **8.** ¿Cuál de estas opciones es verdadera respecto a los comentarios Javadoc?  

- [ ] Es todo aquel texto en el archivo fuente que se encuentra entre los caracteres `/*` y `*/`.  
- [ ] No pueden emplear etiquetas HTML.  
- [ ] Pueden precedir métodos y propiedades de una clase, pero no a una clase ni a su constructor.  
- [x] **Cada línea, excepto la primera y la última, comienza con el carácter `*`.**  

#### **9.** ¿Qué etiqueta Javadoc se emplea para documentar los argumentos de un método?  

- [ ] `@args`  
- [x] **`@param`**  
- [ ] `@[tipo_de_datos_del_parámetro]`  
- [ ] `@see`

#### **10.** ¿Qué etiqueta Javadoc se emplea para documentar el valor que retorna un método?  

- [ ] `@[tipo_de_datos_del_valor_de_retorno]`  
- [x] **`@return`**  
- [ ] `@param`  
- [ ] `@out`  

#### **11.** ¿Cuál de los siguientes formatos es exclusivo para aplicaciones Java?

- [ ] CHM
- [ ] PDF
- [x] **JavaHelp**
- [ ] HLP

#### **12.** ¿Qué herramienta es desarrollada por Microsoft para crear archivos HLP y CHM?

- [ ] JavaHelp
- [ ] RoboHelp
- [x] **Help Workshop**
- [ ] WebHelp

#### **13.** ¿Cuál NO es una característica de los archivos CHM?

- [ ] Compresión de datos
- [ ] Soporte para applets Java
- [ ] Soporte para búsqueda
- [x] **Código fuente incluido**

#### **14.** ¿Qué fichero en JavaHelp define la estructura de la ayuda?

- [ ] .toc
- [x] .**hs**
- [ ] .jhm
- [ ] .xml

#### **15.** ¿Qué clase Java se utiliza para asociar la ayuda sensible al contexto?

- [ ] HelpViewer
- [ ] HelpSet
- [ ] HelpContext
- [x] **HelpBroker**

#### **16.** ¿Cuál es el objetivo principal del índice en un sistema de ayuda?

- [ ] Mejorar la estética
- [ ] Buscar sin conexión
- [x] **Acceso rápido por palabras clave**
- [ ] Crear diagramas

#### **17.** ¿Qué elemento no forma parte de un fichero JAR firmado digitalmente?

- [ ] MANIFEST.MF
- [ ] Archivo .SF
- [ ] Archivo .DSA
- [x] **Archivo .ISO**

#### **18.** ¿Qué tipo de manual proporciona información detallada para usuarios expertos?

- [ ] Manual de instalación
- [ ] Guía rápida
- [ ] Manual de usuario
- [x] **Guía de referencia**

#### **19.** ¿Qué tipo de archivo se usa en Ubuntu para distribuir software?

- [ ] .exe
- [ ] .rpm
- [x] .**deb**
- [ ] .jar

#### **20.** ¿Qué herramienta permite crear instaladores personalizados mediante scripts?

- [ ] InstallBuilder
- [x] **NSIS**
- [ ] Visual Studio
- [ ] apturl

#### **21.** ¿Qué parámetro se usa en NSIS para una instalación silenciosa?

- [ ] /QUIET
- [ ] /NORESTART
- [x] **/S**
- [ ] /silent

#### **22.** ¿Cuál es el paso que NO se realiza durante una instalación de software?

- [ ] Verificación de compatibilidad
- [ ] Registro en el sistema
- [x] **Compilación del programa**
- [ ] Creación de accesos directos

#### **23.** ¿Qué función cumple el archivo MANIFEST.MF en un JAR?

- [ ] Almacena texto legal
- [x] **Define la clase principal y resúmenes**
- [ ] Cifra el contenido
- [ ] Enlaza DLLs externas

#### **24.** ¿Cuál es el objetivo de los asistentes de instalación?

- [ ] Reducir tamaño del programa
- [ ] Permitir que el usuario programe
- [x] **Guiar paso a paso el proceso de instalación**
- [ ] Ejecutar software en la nube

#### **25.** ¿Qué herramienta en Ubuntu permite instalar software desde un enlace web?

- [ ] Synaptic
- [ ] APT
- [x] **apturl**
- [ ] dpkg

### Preguntas de desarrollo

#### **1.** Enumera los diferentes tipos de documentación que podemos encontrar en un proyecto de software dirigidas al usuario final de la aplicación

|**Tipo de Documentación**|**Descripción / Ejemplos**|
|---|---|
|**Documentación de Producto**|- Manual de instrucciones<br>- Manual de referencia<br>- Guías de instalación|
|**Documentación para Usuarios**|- Guías prácticas (How-to guides)<br>- Tutoriales<br>- Documentación de referencia<br>- Explicaciones|
|**Manual de Usuario**|Documento técnico con instrucciones detalladas, capturas, solución de problemas, FAQ, glosario e índice.|
|**Guía de Referencia**|Manual para usuarios avanzados: comandos, sintaxis, mensajes de error.|
|**Guías Rápidas**|Versión resumida con tareas básicas. Ideal para usuarios con poco tiempo o aplicaciones simples.|
|**Manuales de Instalación**|Información para instalar/configurar la aplicación, requisitos, archivos, y software adicional.|
|**Configuración y Administración**|Guías para personalizar y mantener el sistema, incluyendo scripts y comandos.|
|**Ayuda en Línea / JavaHelp**|Sistema de ayuda integrado en la aplicación: mapas, índice, búsqueda, TOC y ayuda sensible al contexto.|
|**Tutoriales Multimedia**|Contenidos visuales e interactivos con herramientas como Camtasia, Wink, Adobe Captivate, etc.|

#### **2.** Indica cuáles son los tipos de documentación de un proyecto de software dirigidas al equipo de desarrollo del proyecto

|**Tipo de Documentación**|**Descripción / Ejemplos**|
|---|---|
|**Documentación de Proyecto**|- Documentos de diseño técnico<br>- Planes de proyecto<br>- Especificaciones de requisitos|
|**Documentación de Procesos**|- Planes de desarrollo<br>- Planes de prueba<br>- Planes de lanzamiento<br>- Informes de errores|
|**Documentación Técnica**|- Documentación de API<br>- Documentación del modelo de datos<br>- Documentación de arquitectura<br>- Guía del usuario técnico<br>- Notas de lanzamiento<br>- README|
|**Documentación del Sistema**|- Guía de resolución de problemas<br>- Documentación de arquitectura<br>- Manual técnico del sistema|
|**Herramientas de Documentación**|- Generadores automáticos<br>- Sistemas de control de versiones<br>- Bases de conocimiento colaborativas|

#### **3.** Explica de forma esquemática pero precisa cuál es el procedimiento que hay que seguir para crear un instalador para Windows de una aplicación Java utilizando la herramienta Install4j. Se ha de tener en cuenta que la aplicación Java puede tener dependencias y recursos externos que también hay que desplegar o instalar en las máquinas destino

##### ✅ Procedimiento para crear un instalador con Install4j para una aplicación Java (con dependencias)

|**Etapa**|**Pasos y detalles**|
|---|---|
|**1. Preparación del proyecto**|- Asegurarse de que la aplicación Java esté completamente desarrollada y probada.|
|**2. Uso de Shade Plugin (Maven)**|- Usar el plugin `maven-shade-plugin` para empaquetar todas las dependencias en un solo `.jar`.<br>- Esto genera un *fat JAR* ejecutable.<br>- Se debe definir la clase `Main-Class` en el `MANIFEST.MF`. **Ruta de salida:** `target\carpetaBuild`|
|**3. Configuración del proyecto en Install4j**|- Crear un nuevo proyecto en **Install4j.**<br>- Definir el directorio base del proyecto como: `target\carpetaBuild`.|

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

#### **4.** Explica detalladamente qué hay que hacer en Install4j para crear una carpeta en `C:\Users\[usuario]\AppData\Local` y que se escriban en ella un conjunto de ficheros cuando la aplicación se instale

1. En el paso de Installer añadiremos la opción "Copy files and directories".  
2. En la ruta origen seleccionaremos la carpeta con el conjunto de ficheros.  
3. En la ruta destino usaremos las variables del Install4j `sys.localappdata` y le añadiremos `\\nombreCarpeta`.  
4. De este modo nos va a crear la carpeta con todo su contenido en `%localAppdata%`.

#### **5.** Diferencias entre `maven-shade-plugin` y `maven-depandency-pluing`

La diferencia entre **`maven-shade-plugin`** y **`maven-dependency-plugin`** radica principalmente en **qué hacen con las dependencias** y **cómo preparan el paquete final.**

##### 🧩 Comparación: Shade Plugin vs Dependency Plugin

|**Característica**|**`maven-shade-plugin`**|**`maven-dependency-plugin`**|
|---|---|---|
|**Propósito principal**|Empaquetar **todas las dependencias** en un solo archivo `.jar` ("fat JAR").|Copiar dependencias o archivos a una ubicación específica del proyecto.|
|**Resultado típico**|Un `.jar` ejecutable con todas las clases y recursos necesarios.|Copia las dependencias en `target/lib` o similar (no las empaqueta).|
|**Uso común**|Crear un único `.jar` listo para distribución o integración con instaladores.|Preparar directorios para distribuciones manuales o scripts personalizados.|
|**Transformación de clases o recursos**|Sí. Puede reubicar paquetes, combinar `META-INF`, modificar el `MANIFEST`, etc.|No. Solo copia archivos, no los modifica.|
|**Define Main-Class en MANIFEST**|**Sí**, mediante el `ManifestResourceTransformer`.| **No.** Se debe configurar aparte si se usa para ejecución.|
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

#### **5.** Explica los diferentes formatos de ficheros de ayuda y sus características principales

|**Formato**|**Descripción**|
|---|---|
|**CHM (Ayuda HTML Compilado)**|Formato propietario de **Microsoft**. Incluye archivos HTML, tabla de contenidos e índice. Permite **compresión de datos**, **búsqueda** y **fusión de ficheros**.|
|**HLP (WinHelp)**|Formato clásico de Windows. Usa archivos `.hlp`, `.cnt` (tabla de contenidos) y `.gid` (información de ventana). Incluye `.hpj` (proyecto), `.rtf` (contenido) y `.shg` (mapas de imagen).|
|**JavaHelp**|Sistema de ayuda basado en **XML** para **aplicaciones Java**. Visualizado mediante navegadores específicos de JavaHelp. Es **independiente de la plataforma**.|
|**PDF**|Formato **abierto y portátil**. Puede visualizarse con lectores de PDF o herramientas de ofimática. Aceptado universalmente y fácil de imprimir.|
|**MAML**|Lenguaje XML utilizado en sistemas Microsoft. Estructurado en **FAQ**, **glosarios**, **procedimientos** y **tutoriales**. Diseñado para documentación interactiva.|
|**IPF**|Utilizado en **IBM OS/2**. Compilado en archivos `.inf` o `.hlp`. Sintaxis similar a HTML con **45 comandos básicos**. Enfocado a sistemas legacy.|

#### **6.** Describe los componentes principales de un sistema JavaHelp y cómo se integran en una aplicación Java

|**Elemento**|**Descripción**|
|---|---|
|**Temas de ayuda (topics)**|Archivos en formato **HTML** que contienen el contenido explicativo o instructivo de la ayuda.|
|**Fichero map (.jhm)**|Archivo en **XML** que asocia identificadores con **URLs o rutas** a archivos HTML e imágenes.|
|**Fichero HelpSet (.hs)**|Archivo principal que **configura y fusiona todos los ficheros de ayuda**. Es el punto de entrada para JavaHelp.|
|**Fichero TOC**|Define la **estructura jerárquica** de la tabla de contenidos mostrada al usuario.|
|**Fichero Índice**|Establece la **organización alfabética** y los términos clave que aparecen en la ayuda.|
|**Base de datos de búsqueda**|Generada mediante la herramienta `jhindexer`, permite realizar **búsquedas de texto completo**.|

Para integrar JavaHelp en una aplicación Java:

1. Se importan las clases necesarias: `import javax.help.*` y `import java.net.*`
2. Se localiza y crea el fichero HelpSet: `URL hsURL = HelpSet.findHelpSet(null, "ayuda/ayuda.hs")`
3. Se crea un objeto HelpBroker: `HelpBroker hb = hs.createHelpBroker()`
4. Se asocia la ayuda a componentes de la interfaz:
   - Para botones: `hb.enableHelpOnButton(jButton1, "introducción", hs)`
   - Para ayuda sensible al contexto: `hb.enableHelp(jButton1, "guardar", hs)`
   - Para tecla de ayuda (F1): `hb.enableHelpKey(getRootPane(), "introduccion", hs)`

#### **7.** Compara los diferentes tipos de documentación para usuarios finales y explique su propósito

1. **Manual de usuario.** Documento técnico detallado que incluye información sobre instalación, configuración y uso de la aplicación, con capturas de pantalla. Contiene secciones como portada, prólogo, tabla de contenidos, guía de uso, solución de problemas, FAQ, glosario e índice.<br><br>
2. **Guía de referencia.** Manual detallado para usuarios experimentados que proporciona información técnica específica como listas de comandos, sintaxis de lenguajes de programación o mensajes de error.<br><br>
3. **Guías rápidas.** Versión resumida de un manual, ideal para usuarios con poco tiempo o para aplicaciones con funcionalidad limitada. Cubre las tareas más importantes de forma concisa.<br><br>
4. **Manuales de instalación.** Proporcionan información específica para instalar y configurar la aplicación, incluyendo requisitos, archivos necesarios y software adicional.<br><br>
5. **Ayuda en línea/JavaHelp.** Sistema de ayuda integrado en la aplicación que incluye mapas, índice, búsqueda, tabla de contenidos y ayuda sensible al contexto.<br><br>
6. **Tutoriales multimedia.** Contenidos visuales e interactivos creados con herramientas como Camtasia, Wink o Adobe Captivate.

#### **8.** Explica qué es un paquete autoinstalable y describa los diferentes tipos según el sistema operativo

- **Windows.** Archivos ejecutables (.exe) que, al ejecutarse, descomprimen los archivos, crean carpetas, copian archivos a sus directorios de destino, modifican el Registro de Windows, añaden entradas en el menú de aplicaciones y crean accesos directos. El usuario puede personalizar la instalación eligiendo componentes o modificando directorios.<br><br>
- **Linux (Ubuntu).** Paquetes .deb que contienen todos los archivos y directorios de la aplicación. La instalación se realiza mediante el Software de Ubuntu, que guía el proceso con ventanas de instalación.<br><br>
- **Linux (Red Hat).** Paquetes .rpm con estructura similar a los .deb pero específicos para distribuciones basadas en Red Hat.

Estos paquetes facilitan la distribución de software al incluir todo lo necesario para la instalación en un único archivo, simplificando el proceso para el usuario final.

#### **9.** Describe los pasos principales en el proceso de instalación de software y su propósito

|**Paso**|**Descripción**|
|---|---|
|**1. Verificación de compatibilidad**|Comprueba que el **hardware y software** del sistema cumplen con los **requisitos mínimos** de la aplicación.|
|**2. Verificación de integridad**|Asegura que el paquete de software es **original** y no ha sido modificado, mediante **sumas de verificación**.|
|**3. Creación de directorios**|Genera las **carpetas necesarias** para almacenar los archivos de la aplicación.|
|**4. Creación de usuarios**|Define **grupos de usuarios** específicos para el software, si es necesario.|
|**5. Copia y descompresión**|Extrae los archivos del paquete y los **copia en las ubicaciones correspondientes**.|
|**6. Compilación y enlace**|Vincula las **bibliotecas requeridas** con la aplicación (si se requiere post-instalación).|
|**7. Configuración**|Ajusta los **parámetros necesarios** para el funcionamiento del software.|
|**8. Variables de entorno**|Define las **variables necesarias** para la ejecución del software (ej. `JAVA_HOME`, `PATH`).|
|**9. Registro**|Registra la aplicación ante el **autor** o el **sistema operativo**, si es requerido.|

Estos pasos aseguran que la aplicación se instale correctamente y esté lista para su uso, minimizando problemas de configuración y compatibilidad.

#### **10.** Explica cómo se puede personalizar un instalador y qué elementos se pueden modificar

1. **Logotipos.** Elementos gráficos que identifican a la empresa o aplicación. Deben ser legibles, escalables, reproducibles, distinguibles y memorables. En herramientas como NSIS, se añaden usando el atributo `AddBrandingImage`.<br><br>
2. **Fondos.** El diseño del fondo debe ser coherente con la aplicación. Un fondo blanco o sin color suele interpretarse como información relevante, mientras que los fondos con color pueden percibirse como menos importantes.<br><br>
3. **Botones.** Incluyen opciones como "siguiente", "anterior", "instalar" y "finalizar". Deben mantener consistencia con el diseño gráfico de la aplicación en colores, fuentes y tamaños.<br><br>
4. **Idioma.** Es esencial permitir seleccionar el idioma de instalación, especialmente para aplicaciones distribuidas globalmente. Aunque el inglés suele ser el idioma predeterminado, es recomendable ofrecer traducciones adicionales.<br><br>
5. **Estructura de ventanas.** Se puede personalizar el número y tipo de ventanas que aparecen durante la instalación, como la bienvenida, licencia, selección de componentes, etc.<br><br>
6. **Opciones de instalación.** Se pueden añadir opciones para que el usuario elija componentes específicos, ubicación de instalación, creación de accesos directos, etc.

La personalización del instalador mejora la experiencia del usuario y refuerza la identidad de la aplicación o empresa.

#### **11.** Describe el proceso de creación de un instalador para una aplicación Java utilizando herramientas externas

1. **Preparación del proyecto.**
   - Asegurarse de que la aplicación Java esté completamente desarrollada y probada.
   - Generar un archivo JAR ejecutable con todas las dependencias (usando Maven con plugins como maven-shade-plugin).

2. **Creación del script NSIS.**

   - Definir atributos del instalador (nombre, archivo de salida, directorio de instalación):

```nsis
Name "Mi Aplicación Java"
OutFile "MiAplicacion.exe"
InstallDir "$PROGRAMFILES\MiAplicacion"
```

   - Configurar páginas del instalador (bienvenida, licencia, directorio, instalación):

```nsis
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_LICENSE "licencia.txt"
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
```

   - Definir secciones para copiar archivos y crear accesos directos:

```nsis
Section "Mi Aplicación Java"
SetOutPath $INSTDIR
File "MiAplicacion.jar"
File /r "lib\"
CreateShortCut "$DESKTOP\Mi Aplicación.lnk" "$INSTDIR\MiAplicacion.jar"
SectionEnd
```

   - Incluir funciones para eventos específicos si es necesario.

3. **Compilación del script.**
- Utilizar el compilador de NSIS para generar el archivo ejecutable del instalador.
- Verificar que no haya errores durante la compilación.
  
4. **Prueba del instalador.**
- Ejecutar el instalador en diferentes entornos para asegurar su correcto funcionamiento.
- Comprobar que la aplicación se instala y ejecuta correctamente.

#### **12.** Explica las diferencias entre los sistemas de gestión de paquetes en Windows y Linux

**Windows.**
- Utiliza principalmente archivos ejecutables (.exe) o instaladores Windows Installer (.msi) para la distribución de software.
- No tiene un sistema centralizado de gestión de paquetes; cada aplicación gestiona su propia instalación y actualización.
- Las aplicaciones se registran en el Registro de Windows, una base de datos centralizada.
- La instalación suele requerir privilegios de administrador y puede necesitar reiniciar el sistema.
- Las actualizaciones generalmente son gestionadas por cada aplicación individualmente o mediante Windows Update para software de Microsoft.

**Linux.**
- Utiliza sistemas de gestión de paquetes centralizados como APT (para distribuciones basadas en Debian como Ubuntu) o YUM/DNF (para distribuciones basadas en Red Hat).
- Los paquetes tienen formatos específicos como .deb (Debian/Ubuntu) o .rpm (Red Hat/Fedora).
- Mantiene una base de datos de paquetes instalados con información sobre versiones, dependencias y archivos.
- Permite la instalación, actualización y eliminación de software desde repositorios centralizados.
- Gestiona automáticamente las dependencias, instalando los paquetes adicionales necesarios.
- Ofrece herramientas gráficas (Centro de Software, Synaptic) y de línea de comandos (apt, yum, dnf).
- Permite actualizar todo el sistema con un solo comando.

Estas diferencias reflejan filosofías distintas: Windows con un enfoque más descentralizado y Linux con un sistema más integrado y centralizado para la gestión de software.

#### **13.** Explica los beneficios de crear documentación de software y cómo contribuye a la calidad del producto

  1. **Mejor experiencia del usuario.** La documentación ayuda a los usuarios a entender cómo utilizar el software y proporciona la información necesaria para que logren sus objetivos, mejorando su experiencia y permitiéndoles aprovechar al máximo las funcionalidades.<br><br>
  2. **Mayor colaboración.** Facilita que los desarrolladores y otros interesados técnicos comprendan los aspectos técnicos del software, mejorando la colaboración dentro del equipo y garantizando que todos trabajen hacia los mismos objetivos.<br><br>
  3. **Aumento de la eficiencia.** Una documentación clara, coherente y actualizada permite a los desarrolladores encontrar rápidamente la información que necesitan, evitando pérdidas de tiempo tratando de entender el código por sí mismos.<br><br>
  4. **Mejora en la calidad del software.** Garantiza que el proceso de desarrollo sea coherente y repetible, además de proporcionar un registro de decisiones y acciones tomadas, lo que contribuye a mejorar la calidad general del software y prevenir errores.<br><br>
  5. **Facilita el mantenimiento.** Una buena documentación hace que sea más fácil mantener y actualizar el software a lo largo del tiempo, especialmente cuando nuevos desarrolladores se unen al proyecto.<br><br>
  6. **Reduce costos a largo plazo.** Aunque crear documentación requiere tiempo y recursos iniciales, reduce significativamente los costos de soporte, mantenimiento y capacitación a largo plazo.<br><br>
  7. **Mejora la comunicación.** Establece un lenguaje común entre desarrolladores, usuarios y otros interesados, facilitando la comunicación efectiva sobre el software.

#### **14.** Describe las mejores prácticas para escribir documentación de software efectiva

1. **Priorizar la documentación en el proceso de desarrollo.**
	- No permitir que se lance una función sin la documentación adecuada
	- Contratar redactores técnicos que fomenten la importancia de la documentación
	- Invertir en herramientas adecuadas para facilitar la creación de documentación
<br><br>
2. **Identificar a la audiencia.**
	- Analizar información sobre los usuarios y consultar equipos de soporte
	- Identificar los objetivos del usuario
	- Crear perfiles y definiciones de audiencia
	- Determinar los formatos adecuados (FAQ, wiki, base de conocimientos)
<br><br>
3. **Definir el alcance y los objetivos.**
	- Enfocarse en funcionalidades específicas o casos de uso
	- Proporcionar información clave para completar ciertas tareas
<br><br>
4. **Desarrollar una estrategia de contenido.**
	- Establecer un calendario de creación y actualización
	- Definir herramientas y recursos necesarios
	- Diseñar un proceso de revisión y actualización
<br><br>
5. **Crear una guía de estilo.**
	- Establecer terminología estándar
	- Definir voz y tono
	- Especificar formato de página
	- Estandarizar elección de palabras
	- Normalizar uso de imágenes y vídeos
<br><br>
6. **Escribir de forma clara y concisa.**
	- Utilizar lenguaje claro y sencillo
	- Evitar tecnicismos innecesarios
	- Estructurar bien la información con encabezados y listas
	- Incluir ejemplos e ilustraciones
<br><br>
7. **Revisar y actualizar regularmente.**
	- Involucrar a desarrolladores y usuarios en el proceso de revisión
	- Revisar la documentación para detectar errores o inconsistencias
	- Mantener la documentación actualizada conforme evoluciona el software
<br><br>
8. **Garantizar inclusividad y accesibilidad.**
	- Evitar modismos o referencias culturales específicas
	- Asegurar compatibilidad con lectores de pantalla
	- Proporcionar descripciones alternativas para imágenes
	- Utilizar colores con suficiente contraste
<br><br>
9. **Usar elementos visuales.**
	- Incorporar imágenes, diagramas y vídeos para ilustrar conceptos
	- Hacer la documentación más atractiva y comprensible
<br><br>
10. **Incluir ejemplos prácticos.**
	- Proporcionar ejemplos de código, casos de uso y ejercicios
	- Facilitar el aprendizaje mediante aplicaciones prácticas

#### **15.** Compare y contraste las tablas de contenidos e índices en los sistemas de ayuda, explicando sus diferencias fundamentales y propósito.

Las tablas de contenidos e índices son componentes esenciales en los sistemas de ayuda, pero tienen diferencias fundamentales en su estructura, organización y propósito:

##### Tablas de contenidos (TOC

- **Estructura**: Organizan los temas de ayuda en una estructura jerárquica, similar a las carpetas de un administrador de archivos.
- **Organización**: Cada ítem representa un tema principal que puede expandirse para mostrar subtemas más específicos, siguiendo una organización lógica basada en la estructura del contenido.
- **Navegación**: Cuando el usuario selecciona un tema, se muestra el texto asociado en la ventana de ayuda, permitiendo navegar entre temas mediante hipervínculos.
- **Propósito**: Proporcionar una visión general y estructurada de todo el contenido de la ayuda, facilitando la comprensión de la organización temática.
- **Implementación técnica**: En JavaHelp, se crea mediante un fichero TOC con sintaxis basada en XML que describe la estructura y distribución de los temas.

##### Índices

- **Estructura**: Consisten en una lista alfabética de palabras clave o términos específicos.
- **Organización**: Se ordenan alfabéticamente, independientemente de la estructura del contenido, facilitando la búsqueda de términos concretos.
- **Navegación**: El usuario puede navegar por la lista de términos o buscar directamente en un campo de texto para acceder a definiciones o temas relacionados.
- **Propósito**: Funcionar como un glosario o guía de definiciones, aclarando conceptos específicos relacionados con la aplicación y permitiendo acceso rápido a términos concretos.
- **Implementación técnica**: En JavaHelp, se utiliza la herramienta `jhindexer` para crear la base de datos de búsqueda necesaria, y el fichero de generación del índice está en formato XML.

##### Diferencias clave

1. **Organización**: Las tablas de contenidos siguen una estructura jerárquica basada en la organización lógica del contenido, mientras que los índices siguen un orden alfabético de términos.
2. **Propósito de uso**: Las tablas de contenidos son útiles cuando el usuario quiere explorar la estructura general de la ayuda, mientras que los índices son más eficientes cuando se busca información sobre un término específico.
3. **Método de acceso**: Las tablas de contenidos facilitan la navegación secuencial y jerárquica, mientras que los índices permiten un acceso directo y puntual a la información.

Ambos elementos son complementarios en un sistema de ayuda completo, ya que ofrecen diferentes formas de acceder a la información según las necesidades del usuario en cada momento.