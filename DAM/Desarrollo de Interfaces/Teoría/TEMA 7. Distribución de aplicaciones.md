---
number headings: max 3, _.1.1., skip ^sk
banner: "![[di.jpg]]"
banner_y: 0.85
obsidianUIMode: preview
cssclasses:
  - table-compact-clean
---

# **TEMA 7.** <br>Distribución de aplicaciones

## 1. Definición y composición de una distribución. Sistema de gestión de paquetes

Una **distribución de software** es un conjunto de programas compilados y configurados, que incluye aplicaciones y paquetes junto con un sistema operativo. Es común en distribuciones de **Linux** como **Debian**, **Ubuntu** o **Red Hat.** Estas distribuciones suelen estar asociadas a licencias como la **GPL** (Licencia Pública General), que protege la libre distribución, modificación y uso del software. También existen **distribuciones binarias**, que incluyen instaladores (como **.exe** o **.msi** en Windows), disponibles para descarga. Las distribuciones pueden ser **oficiales** (de los autores originales) o de **terceros** (desarrolladas por otras personas o empresas).

Un **sistema de gestión de paquetes** automatiza la instalación, actualización, configuración y eliminación de paquetes de software. Es común en sistemas **Linux**, como el **Centro de Software de Ubuntu** o el **Gestor de Paquetes Synaptic.** Los paquetes contienen el software, su nombre, descripción, versión, distribuidor, suma de verificación y dependencias necesarias. Esta información se almacena en una **base de datos local.**

## 2. Instaladores. Pasos en la instalación. Asistente de instalación

Un **instalador** es un programa que automatiza la instalación de software. Normalmente, un programa consta de múltiples archivos que deben copiarse en directorios específicos y, en sistemas **Windows**, registrarse en el **Registro de Windows.** Los instaladores realizan estas tareas de forma transparente para el usuario, guiándolo mediante formularios que limitan las acciones a pequeñas modificaciones o simplemente pulsar **"siguiente".** Copian los archivos, registran la aplicación y crean accesos directos en el escritorio.

Ejemplos de instaladores incluyen: **InstallAnywhere**, **Windows Installer**, **InstallShield**, **NSIS**, **Visual Studio 2019**, **IzPack**, entre otros.

Los pasos en la instalación son:

- **Verificación de compatibilidad.** Se comprueban los requisitos de hardware y software.
- **Verificación de integridad.** Se asegura que el paquete de software es original.
- **Creación de directorios.** Se generan las carpetas necesarias.
- **Creación de usuarios.** Se definen grupos de usuarios para el software.
- **Copia y descompresión.** Los archivos se extraen del paquete.
- **Compilación y enlace.** Se vinculan las bibliotecas requeridas.
- **Configuración.** Se ajustan los parámetros necesarios.
- **Variables de entorno.** Se definen las variables necesarias.
- **Registro.** La aplicación se registra ante el autor.

Los **asistentes de instalación** son aplicaciones que guían al usuario durante el proceso. Permiten personalizar aspectos como la ubicación de instalación, la integración en menús, la aceptación de licencias y el registro del software. Cada paso se muestra en un formulario con la información correspondiente.

## 3. Paquetes autoinstalables

Al finalizar el ciclo de desarrollo de una aplicación, es crucial decidir cómo distribuirla, incluyendo la incorporación de características adicionales, parches y revisiones. Un **paquete autoinstalable** empaqueta la aplicación en un único archivo que contiene todos los archivos y directorios necesarios. Este archivo puede ser un ejecutable en Windows (.**exe**), un paquete **Debian** (.**deb**) en distribuciones como Ubuntu, o un paquete **RPM** en distribuciones como Red Hat.

En **Windows**, el paquete autoinstalable es una aplicación que, al ejecutarse, descomprime los archivos, crea las carpetas necesarias, copia los archivos a sus directorios de destino, modifica el **Registro de Windows**, añade entradas en el menú de aplicaciones y crea accesos directos en el escritorio. El usuario puede personalizar la instalación, eligiendo componentes, modificando directorios o aceptando las opciones por defecto.

En **Ubuntu**, por ejemplo, se crea un paquete **.deb.** Este paquete contiene todos los archivos y directorios de la aplicación. Al instalar, el usuario utiliza el **Software de Ubuntu**, que guía el proceso mediante ventanas de instalación.

## 4. Herramientas para crear paquetes de instalación. Repositorios

Existen diversas herramientas para crear paquetes de instalación, siendo las más comunes: **InstallAnywhere**, **InstallBuilder**, **Windows Installer**, **InstallShield**, **NSIS**, **IzPack**, entre otras. Un instalador rápido y amigable es esencial, ya que un proceso lento o fallido puede frustrar al usuario.

En **Windows**, herramientas como **NSIS** (Nullsoft Scriptable Install System) permiten crear instaladores personalizados. NSIS es **open-source** y permite crear instaladores que pueden instalar, desinstalar, configurar el sistema y extraer archivos. Está basado en scripts, lo que otorga control total al programador.

En **Linux**, el tipo de paquete depende de la distribución. En **Ubuntu**, se utiliza el formato **.deb**, que empaqueta todos los archivos necesarios y configura el **Software de Ubuntu** para copiar los archivos y ajustar las opciones de configuración.

En sistemas como **Windows** o **Mac OS**, los programas suelen distribuirse como instaladores ejecutables descargables desde Internet o en CDs/DVDs. En sistemas **open source** como **Ubuntu**, el software se distribuye principalmente en paquetes **.deb** (o **.rpm** en Red Hat), que incluyen programas y bibliotecas necesarias.

Los **repositorios** son servidores que centralizan paquetes de software, ofreciendo una amplia variedad de aplicaciones. En **Ubuntu**, los repositorios oficiales suelen ser suficientes, pero es común añadir repositorios de terceros para acceder a más software. Herramientas como el **Centro de Software** facilitan el acceso a estos repositorios.

## 5. Personalización de la instalación

Una vez finalizado el desarrollo de una aplicación, el programador debe decidir el mecanismo de distribución. En **Windows**, se crean instaladores ejecutables (.**exe**), mientras que en **Linux**, como **Ubuntu**, se generan paquetes de instalación (.**deb**). Para ambos casos, se utilizan herramientas de generación de instaladores que permiten personalizar el proceso.

Un instalador personalizado puede incluir el **logotipo** de la aplicación o empresa, un **icono propio**, colores y formatos de ventana específicos, así como formularios para seleccionar el idioma, directorios de instalación y aceptar los acuerdos de licencia. Estos elementos permiten crear un instalador único para cada aplicación.

### 5.1. **Logotipos**

El **logotipo** es un elemento gráfico clave que identifica a la empresa o aplicación. Debe ser **legible**, **escalable**, **reproducible**, **distinguible** y **memorable.** En un instalador, el logotipo puede colocarse en cualquier posición (arriba, abajo, derecha o izquierda), y su tamaño dependerá del diseño del instalador y la fuente utilizada.

En herramientas como **NSIS**, el logotipo se añade usando el atributo **AddBrandingImage**, con la sintaxis:  
```plaintext
(left|right|top|bottom) (width | height) [padding]
```

### 5.2. **Fondos**

El **fondo** del instalador debe ser coherente con el diseño de la aplicación. Un fondo blanco o sin color suele interpretarse como información relevante, mientras que los fondos con color pueden percibirse como menos importantes o publicitarios. La consistencia en el diseño es crucial para mantener la atención del usuario.

### 5.3. **Botones**

Los botones en un instalador suelen incluir opciones como **siguiente**, **anterior**, **instalar** y **finalizar.** Estos botones deben ser consistentes con el diseño gráfico de la aplicación, manteniendo el mismo formato en colores, fuentes y tamaños. Las formas más comunes son rectangulares, aunque también se usan esquinas redondeadas, circulares o elípticas.

### 5.4. **Idioma**

Dado que las aplicaciones se distribuyen globalmente, es esencial que el instalador permita seleccionar el **idioma** de instalación. Aunque el inglés es el idioma predeterminado, es recomendable ofrecer traducciones adicionales. El programador debe diseñar la aplicación y el instalador para soportar múltiples idiomas, permitiendo al usuario elegir el idioma durante la instalación.

## 6. Generación de paquetes de instalación

Para generar paquetes de instalación de una aplicación, existen varias alternativas:

- **Utilizar entornos de desarrollo.** Muchos entornos de desarrollo incluyen herramientas para generar paquetes, aunque no siempre son "amigables" para el usuario. Por ejemplo, en **NetBeans**, se puede crear un paquete **JAR** para aplicaciones Java, pero el usuario debe manejar la instalación y ejecución.
- **Herramientas externas.** Existen herramientas complementarias que permiten crear instaladores más avanzados a partir de paquetes generados en entornos de desarrollo. Estas herramientas pueden generar instaladores o autoinstalables para aplicaciones Java.
- **Instalación en modo desatendido.** Esta opción permite automatizar la instalación sin interacción del usuario.

### 6.1. **Entorno de desarrollo**

En el desarrollo de aplicaciones **Java**, el objetivo es generar un archivo **JAR** para su distribución. En **NetBeans**, una vez finalizado el desarrollo, se construye el proyecto y se genera el archivo **JAR** en la carpeta **dist.** Si la aplicación requiere bibliotecas adicionales, estas se almacenan en una subcarpeta **lib** dentro de **dist.**

Para ejecutar la aplicación fuera del IDE, el usuario puede hacer doble clic en el archivo **JAR** o usar la línea de comandos. Si la aplicación no se ejecuta, puede deberse a que el archivo **JAR** no está asociado con el **Java Runtime Environment (JRE)** o falta la opción **-jar** en el comando de ejecución.

#### Empaquetado y distribución de aplicaciones Java de escritorio

Para distribuir una aplicación Java, se crea un archivo **JAR** ejecutable. Este archivo contiene múltiples ficheros y carpetas, similar a un archivo **ZIP**, pero con atributos adicionales para la ejecución de aplicaciones Java. El proceso incluye:

- **Configuración del proyecto.** Definir la clase principal y añadir las bibliotecas necesarias.
- **Construcción del proyecto.** Generar el archivo **JAR** y las bibliotecas en la carpeta **dist.**
- **Ejecución dentro del IDE.** Probar la aplicación antes de distribuirla.
- **Ejecución fuera del IDE.** Verificar que la aplicación funciona correctamente fuera del entorno de desarrollo.

#### Configuración de la clase principal

La clase principal debe especificarse en el archivo **manifest** del **JAR** para que el usuario pueda ejecutar la aplicación. En **NetBeans**, esto se configura en las propiedades del proyecto, seleccionando la clase principal en la opción **Main class.**

#### Añadir las librerías necesarias

Si la aplicación utiliza bibliotecas externas, estas deben añadirse al proyecto. En **NetBeans**, esto se hace a través del nodo **Bibliotecas** en la ventana del proyecto. Por ejemplo, si se usa **GroupLayout**, se añade la biblioteca **Swing Layout Extensions.**

#### Construcción del proyecto y creación del fichero JAR

Una vez configurado el proyecto, se construye generando el archivo **JAR** en la carpeta **dist.** Las bibliotecas necesarias se copian en la subcarpeta **lib**, y el archivo **manifest** se actualiza con la clase principal y las bibliotecas requeridas.

#### Ejecución de la aplicación dentro del IDE

Antes de distribuir la aplicación, es esencial probarla dentro del IDE para asegurar su correcto funcionamiento. En **NetBeans**, esto se hace seleccionando la opción **Ejecutar** en el menú contextual del proyecto.

#### Ejecución de la aplicación fuera del IDE

Para verificar que la aplicación funciona fuera del IDE, se navega hasta la carpeta **dist** y se ejecuta el archivo **JAR.** Si la aplicación no se ejecuta, puede deberse a problemas con la asociación del archivo **JAR** con el **JRE.**

#### Distribución de la aplicación

La aplicación se distribuye empaquetando el archivo **JAR** y la carpeta **lib** en un archivo **ZIP.** El usuario final debe mantener ambos elementos en la misma carpeta para ejecutar la aplicación.

#### Posibles problemas

Si la aplicación no se ejecuta al hacer doble clic en el archivo **JAR**, puede deberse a:

- Falta de asociación del archivo **JAR** con el **JRE.**
- Falta de la opción **-jar** en el comando de ejecución.

En **Windows**, se puede solucionar asociando el archivo **JAR** con **Java Platform SE Binary.** En sistemas **UNIX** o **Linux**, el procedimiento varía según el entorno de escritorio (**GNOME** o **KDE**).

### 6.2. **Herramientas externas**

Existen herramientas externas a los entornos de desarrollo que permiten crear paquetes de instalación para aplicaciones. En el caso de aplicaciones **Java**, herramientas como **IzPack** y **NSIS** son ampliamente utilizadas.

#### Creación de un instalador utilizando NSIS

**NSIS** (Nullsoft Scriptable Install System) es una herramienta **open-source** que permite crear instaladores para aplicaciones, incluyendo aplicaciones **Java.** Funciona mediante un lenguaje de scripts, donde el programador define el comportamiento del instalador. Una vez compilado el script, se genera un ejecutable que actúa como instalador.

**NSIS** permite personalizar el proceso de instalación, incluyendo la creación de accesos directos, la modificación del registro de **Windows** y la selección de componentes por parte del usuario. Además, incluye scripts de ejemplo que pueden adaptarse a las necesidades del proyecto.

#### Creación de scripts mediante NSIS

Un script **NSIS** es un archivo de texto con extensión **.nsi** que define el comportamiento del instalador. Los scripts pueden incluir:

- **Atributos del instalador.** Determinan el nombre de la aplicación, el directorio de instalación y otros parámetros. Por ejemplo:

  ```nsis
  Name "Ejemplo de creación de instalador"
  OutFile "Ejemplo.exe"
  InstallDir "$PROGRAMFILES\Ejemplo"
  ```

- **Páginas.** Definen las ventanas que se muestran durante la instalación, como la página de bienvenida, la aceptación de licencia y la selección de componentes. Por ejemplo:

  ```nsis
  !insertmacro MUI_PAGE_WELCOME
  !insertmacro MUI_PAGE_LICENSE "licencia.txt"
  !insertmacro MUI_PAGE_DIRECTORY
  !insertmacro MUI_PAGE_INSTFILES
  ```

- **Secciones.** Definen los componentes que se instalarán. Cada sección puede incluir instrucciones para copiar archivos, crear directorios o modificar el registro. Por ejemplo:

  ```nsis
  Section "My Program"
    SetOutPath $INSTDIR
    File "My Program.exe"
    File "Readme.txt"
  SectionEnd
  ```

- **Funciones.** Contienen código que se ejecuta en eventos específicos, como la inicialización del instalador. Por ejemplo:

  ```nsis
  Function .onInit
    MessageBox MB_YESNO "¿Desea instalar el programa?" IDYES gogogo
      Abort
    gogogo:
  FunctionEnd
  ```

- **Variables.** Permiten almacenar valores temporales durante la instalación. Por ejemplo:

  ```nsis
  Var VARIABLE
  Section
    StrCpy $VARIABLE "valor"
  SectionEnd
  ```

#### Entorno de NSIS

Una vez creado el script, se compila utilizando el compilador de **NSIS.** Si no hay errores, se genera un archivo ejecutable que actúa como instalador. El entorno de **NSIS** incluye una interfaz gráfica para compilar scripts y acceder a ejemplos y documentación.

#### Ejemplo de uso de NSIS

Para crear un instalador con **NSIS**, se siguen estos pasos:

1. **Definir la interfaz.** Incluir la interfaz deseada, como `MUI2.nsh`.

   ```nsis
   !include "MUI2.nsh"
   ```

2. **Configurar parámetros generales.** Establecer el nombre del instalador, el archivo de salida y el directorio de instalación.

   ```nsis
   Name "Ejemplo de creación de instalador"
   OutFile "Ejemplo.exe"
   InstallDir "$PROGRAMFILES\Ejemplo"
   ```

3. **Definir páginas.** Especificar las páginas que se mostrarán durante la instalación.

   ```nsis
   !insertmacro MUI_PAGE_WELCOME
   !insertmacro MUI_PAGE_LICENSE "licencia.txt"
   !insertmacro MUI_PAGE_DIRECTORY
   !insertmacro MUI_PAGE_INSTFILES
   ```

4. **Configurar componentes.** Definir los archivos y directorios que se instalarán.

   ```nsis
   Section "Fichero jar"
     SetOutPath $INSTDIR
     File "Tarea_U07.jar"
     File "lib\swing-layout-1.0.4.jar"
   SectionEnd
   ```

5. **Agregar desinstalador.** Incluir una sección para desinstalar la aplicación.

   ```nsis
   Section "Desinstalar"
     Delete "$INSTDIR\Uninstall.exe"
     RMDir "$INSTDIR"
     DeleteRegKey /ifempty HKCU "Software\ejemplo"
   SectionEnd
   ```

6. **Compilar el script.** Utilizar el compilador de **NSIS** para generar el instalador ejecutable.

Este proceso genera un instalador personalizado que permite al usuario seleccionar componentes, elegir el directorio de instalación y desinstalar la aplicación si es necesario.

### 6.3. **Modo desatendido**

Una **instalación en modo desatendido** es aquella en la que el usuario no interviene en el proceso de instalación. No se solicitan decisiones como el directorio de instalación, el idioma o las variables de entorno. Este modo es útil para instalar software en múltiples equipos o sistemas operativos de manera automatizada.

Para automatizar el proceso, se pueden utilizar **scripts** que registren las acciones del usuario (pulsaciones de teclado y ratón) y las reproduzcan durante la instalación. Otra opción es emplear **parámetros específicos** que los instaladores ofrecen para ejecutarse en modo silencioso.

- **NSIS.** Utiliza el parámetro **/S** para ejecutar la instalación en modo silencioso.
- **INNO Setup.** Emplea los parámetros **/SP- /VERYSILENT /NORESTART** para instalaciones desatendidas.
- **Windows Installer (MSI).** Usa los comandos **/qn**, **/qb** o **/quiet** para instalaciones silenciosas, junto con **/norestart** para evitar reinicios.

En algunos casos, es posible extraer los archivos de un instalador (por ejemplo, con **WinRAR**) y reempaquetarlos con un instalador que admita parámetros silenciosos.

## 7. Parámetros de la instalación

Los **parámetros de la instalación** permiten personalizar la aplicación según las necesidades del usuario. Estos parámetros incluyen:

- **Selección de idioma.** Dado que las aplicaciones se distribuyen globalmente, es común que el instalador permita elegir el idioma de la interfaz.
- **Aceptación de licencia.** El usuario debe aceptar los términos de la licencia para continuar con la instalación. Si no los acepta, la instalación se cancela.
- **Instalación de componentes adicionales.** Algunas instalaciones incluyen aplicaciones o barras de herramientas opcionales, como complementos para navegadores web.
- **Ruta de instalación.** El instalador sugiere una ruta predeterminada, pero el usuario puede modificarla.
- **Creación de accesos directos.** El usuario puede elegir si desea crear accesos directos en el menú de inicio, el escritorio o el inicio rápido (en Windows).
- **Ejecución automática.** Al finalizar la instalación, el usuario puede optar por ejecutar la aplicación inmediatamente.

Estos parámetros permiten adaptar la instalación a las preferencias del usuario, mejorando la experiencia y facilitando la configuración inicial de la aplicación.

## 8. Interacción con el usuario

En las aplicaciones con **interfaz gráfica (GUI)**, la interacción con el usuario se basa en principios de **usabilidad** y diseño amigable. Los instaladores gráficos siguen una serie de pasos estandarizados para guiar al usuario durante el proceso de instalación:

1. **Ventana de selección de idioma.** El usuario elige el idioma en el que se mostrarán los mensajes durante la instalación.

2. **Ventana de bienvenida.** Proporciona información sobre la versión de la aplicación, recomendaciones y otros detalles relevantes.

3. **Acuerdo de licencia.** El usuario debe aceptar los términos de uso del software. Si no los acepta, la instalación se cancela.

4. **Aceptación de herramientas opcionales.** Se ofrecen complementos adicionales, como barras de herramientas para navegadores web. El usuario puede elegir instalarlos o no, sin afectar la instalación principal.

5. **Selección de la ubicación de instalación.** El instalador sugiere una ruta predeterminada (por ejemplo, `C:\Programas`), pero el usuario puede modificarla según sus preferencias.

6. **Selección de accesos directos.** El usuario decide si desea crear accesos directos en el menú de inicio, el escritorio u otras ubicaciones.

7. **Proceso de instalación.** Comienza la copia de archivos en el disco duro, en la ubicación seleccionada por el usuario.

8. **Finalización.** El instalador notifica al usuario que el proceso ha concluido, ofreciendo opciones como ejecutar la aplicación inmediatamente o cerrar el instalador.

Estos pasos garantizan una experiencia de usuario clara y consistente, facilitando la instalación de software de manera intuitiva y eficiente.

## 9. Ficheros firmados digitalmente

Una **firma digital** es un esquema matemático que garantiza la autenticidad de un documento digital, como un fichero. En el contexto de la distribución de software, una firma digital válida asegura que el fichero fue creado por un autor o empresa conocida y que no ha sido alterado durante su transferencia. Esto es especialmente importante en descargas de Internet, donde la autenticidad y la integridad del software son críticas.

La plataforma **Java** permite firmar digitalmente ficheros **JAR.** Al firmar un fichero **JAR**, se asegura a los usuarios que el software proviene de un autor confiable. El proceso de verificación de la firma digital confirma que el fichero no ha sido modificado desde su firma.

### 9.1. **Firma digital en ficheros JAR**

La firma digital en **Java** se basa en el uso de **claves públicas y privadas**, junto con **certificados** emitidos por una **autoridad de certificación (CA).** Aquí se explica el proceso:

1. **Claves públicas y privadas.**  
   - La **clave privada** es utilizada por el desarrollador para firmar el fichero **JAR.**  
   - La **clave pública** se incluye en el fichero **JAR**, junto con un **certificado**, para que cualquier persona pueda verificar la firma.

2. **Certificado.**  
   - Es una declaración digital firmada por una **autoridad de certificación** que confirma la propiedad de la clave pública.  
   - El certificado garantiza que la clave pública pertenece al autor del software.

3. **Resúmenes y ficheros de firmas.**  
   - Al firmar un fichero **JAR**, se generan **resúmenes** (hashes) de cada archivo contenido en el **JAR.** Estos resúmenes se almacenan en el archivo **MANIFEST.MF.**  
   - Además, se crea un archivo de firma (con extensión **.SF**) en el directorio **META-INF**, que contiene resúmenes de las entradas del manifiesto y un resumen del manifiesto completo.

4. **Archivo de bloque de firma.**  
   - Se genera un archivo de bloque de firma (con extensión **.DSA** o similar) que contiene:  
	 - La **firma digital** del fichero **JAR**, generada con la clave privada.  
	 - El **certificado** con la clave pública del firmante.  
   - Este archivo no es legible y es esencial para la verificación.

#### Firmar un fichero JAR

Para firmar un fichero **JAR**, se utiliza la herramienta **jarsigner**, que forma parte del **JDK.** El proceso básico es el siguiente:

1. **Generar o tener una clave privada.**  
   Las claves se almacenan en un **keystore**, una base de datos protegida que puede contener múltiples claves identificadas por un **alias.**

2. **Comando básico para firmar.**  

   ```bash
   jarsigner jar-file alias
   ```

   - **jar-file.** Ruta del fichero **JAR** a firmar.  
   - **alias.** Alias que identifica la clave privada en el keystore.  

   Ejemplo:

   ```bash
   jarsigner miAplicacion.jar miAlias
   ```

3. **Opciones adicionales.**  
   - **-keystore.** Especifica la ruta del keystore si no es el predeterminado.  
   - **-storepass.** Proporciona la contraseña del keystore.  
   - **-keypass.** Proporciona la contraseña de la clave privada.  

   Ejemplo con opciones:

   ```bash
   jarsigner -keystore /ruta/al/keystore -storepass contraseña -keypass clave miAplicacion.jar miAlias
   ```

4. **Verificación de la firma.**  
   Para verificar la firma de un fichero **JAR**, se usa el mismo comando con la opción **-verify.**

   ```bash
   jarsigner -verify miAplicacion.jar
   ```

#### Ejemplo de archivos generados

- **MANIFEST.MF.**  

  ```plaintext
  Name: test/classes/ClassOne.class
  SHA1-Digest: TD1GZt8G11dXY2p4olSZPc5Rj64=
  ```

- **Archivo de firma (.SF).**  

  ```plaintext
  Signature-Version: 1.0
  SHA1-Digest-Manifest: h1yS+K9T7DyHtZrtI+LxvgqaMYM=
  Created-By: 1.6.0 (Sun Microsystems Inc.)
  Name: test/classes/ClassOne.class
  SHA1-Digest: fcav7ShIG6i86xPepmitOVo4vWY=
  ```

- **Archivo de bloque de firma (.DSA).**  
  Contiene la firma digital y el certificado, no es legible.

### 9.2. **Resumen del proceso de firma digital**

1. **Firma.**  
   - El desarrollador firma el fichero **JAR** con su **clave privada.**  
   - Se incluyen la **clave pública** y el **certificado** en el fichero **JAR.**

2. **Verificación.**  
   - El usuario verifica la firma utilizando la **clave pública** y el **certificado.**  
   - Se recalculan los resúmenes de los archivos y se comparan con los almacenados en el **MANIFEST.MF** y el archivo de firma (**.SF**).

Este proceso garantiza la autenticidad e integridad del software distribuido, protegiendo a los usuarios de posibles alteraciones o suplantaciones.

## 10. Instalación de aplicaciones desde un servidor

Cuando se distribuye un paquete de software, una opción común es alojarlo en un **servidor web** para que los usuarios puedan acceder y descargarlo directamente. Este enfoque es especialmente popular en distribuciones **Linux** como **Ubuntu**, donde los usuarios pueden instalar aplicaciones simplemente haciendo clic en un **hipervínculo.**

### 10.1. **Ventajas de los servidores de aplicaciones**

- **Centralización.** Todas las aplicaciones están disponibles en un solo lugar, lo que facilita su gestión y distribución.
- **Disminución de la complejidad.** No es necesario programar las aplicaciones desde cero; se pueden ensamblar a partir de bloques existentes y ponerlas a disposición en el servidor.

### 10.2. **Uso de `apturl` para instalación desde servidores**

En distribuciones como **Ubuntu**, se utiliza **apturl**, un miniprograma gráfico que permite instalar aplicaciones directamente desde un repositorio. Para distribuir aplicaciones de esta manera, se edita una página web con una descripción del programa y un enlace en el siguiente formato:

```html
<a href="apt:paquete">Nombre del paquete a instalar</a>
```

Si se desea instalar múltiples paquetes en un solo enlace, la sintaxis es:

```html
<a href="apt:paquete1,paquete2,paquete3">Nombre de la aplicación</a>
```

**Ejemplo.**  
Para instalar **Pidgin** y **Pidgin Plugin Pack**, el enlace sería:

```html
<a href="apt:pidgin,pidgin-plugin-pack">Instalar Pidgin y Plugin Pack</a>
```

## 11. Descarga y ejecución de aplicaciones ubicadas en servidores web

Cuando se descarga un fichero desde un servidor web, existen varias formas de proceder según el tipo de archivo:

### Ficheros ejecutables ^sk

Si el fichero descargado es un ejecutable (por ejemplo, un **.exe** en **Windows** o un **.sh** en **Linux**), basta con ejecutarlo para iniciar el proceso de instalación.

### Ficheros empaquetados y comprimidos ^sk

Si la aplicación se distribuye en un fichero comprimido (como **.zip**, **.rar** o una imagen **.iso**), se debe descomprimir o montar antes de la instalación:

- **Imágenes ISO.** Se pueden grabar en un **CD/DVD** o montar con herramientas como **Daemon Tools.**
- **Paquetes comprimidos.** Se necesita un programa compatible para descomprimir (por ejemplo, **WinRAR** o **7-Zip**).

### Paquetes específicos de Linux ^sk

En distribuciones como **Ubuntu**, es común descargar paquetes **.deb** o **.rpm.** Estos paquetes contienen aplicaciones instalables y pueden gestionarse mediante:

- **Entorno gráfico.** Usando el **Gestor de Paquetes de Ubuntu.**
- **Entorno de consola.** Utilizando comandos como `dpkg` o `apt`.

**Ejemplo de instalación desde consola.**

```bash
sudo dpkg -i paquete.deb
sudo apt install -f  # Para resolver dependencias
```

### Paquetes JAR o archivos comprimidos ^sk
- **Paquetes JAR.** Requieren una **máquina virtual Java (JVM)** para su ejecución.
- **Archivos comprimidos (ZIP/RAR).** Necesitan un programa de descompresión compatible.

### Consideraciones importantes ^sk

- **Compatibilidad del sistema operativo.** Asegúrese de que el software descargado sea compatible con su sistema operativo y arquitectura (por ejemplo, **32-bit** o **64-bit**).
- **Seguridad.** Verifique la autenticidad del software descargado, especialmente si proviene de fuentes no oficiales.

### Ejemplo de distribución de software ^sk

Supongamos que queremos distribuir una aplicación llamada **MiAplicacion** en formato **.deb** para **Ubuntu.** El proceso sería:

1. **Crear el paquete .deb.**  
   - Empaquetar la aplicación y sus dependencias en un fichero **.deb.**

2. **Subir el paquete a un servidor web.**  
   - Alojar el fichero **.deb** en un servidor accesible.

3. **Proporcionar un enlace de descarga.**  
   - Incluir un enlace en una página web para que los usuarios puedan descargar e instalar la aplicación.

**Ejemplo de enlace.**

```html
<a href="https://miservidor.com/MiAplicacion.deb">Descargar MiAplicacion</a>
```

4. **Instalación por el usuario.**  
   - El usuario descarga el fichero **.deb** y lo instala usando el gestor de paquetes o la consola.

Este enfoque simplifica la distribución de software y permite a los usuarios instalar aplicaciones de manera rápida y segura.

## Autoevaluación ^sk

### 1: ¿Qué paso no se realiza en la instalación de un programa?

**Respuesta: Compilar el programa.**  
En el proceso de instalación, no se compila el programa. La compilación es parte del desarrollo, no de la instalación. Los pasos de instalación incluyen la creación de directorios, verificación de compatibilidad, copia de archivos, etc.

### 2: ¿Qué herramienta no crea programas de instalación?

**Respuesta: Centro de software.**  
El **Centro de software** es una herramienta para instalar aplicaciones, no para crear instaladores. Herramientas como **IzPack**, **NSIS** e **InstallShield** sí se utilizan para crear programas de instalación.

### 3: ¿Qué tipo de archivo es el que se utiliza en Ubuntu para distribuir aplicaciones?

**Respuesta: Paquetes deb.**  
En distribuciones como **Ubuntu**, las aplicaciones se distribuyen en paquetes **.deb**, que contienen el software y sus dependencias.

### 4: Para crear un instalador personalizado en Windows deberemos

**Respuesta: Utilizar algún software específico como NSIS.**  
En **Windows**, se utilizan herramientas como **NSIS**, **InstallShield** o **Inno Setup** para crear instaladores personalizados.

### 5: Los ficheros JAR

**Respuesta: Son paquetes ejecutables que contienen clases Java y otros recursos.**  
Los ficheros **JAR** son archivos comprimidos que contienen clases Java, recursos y un archivo **MANIFEST.MF** para definir la clase principal.

### 6: En una instalación desatendida

**Respuesta: La aplicación se instala de forma transparente al usuario.**  
En una instalación desatendida, el usuario no interactúa con el instalador. El proceso se realiza automáticamente sin intervención del usuario.

### 7: El reconocimiento de la firma digital de un archivo JAR se conoce como

**Respuesta: Verificación.**  
El proceso de reconocimiento de la firma digital se llama **verificación**, donde se confirma que el archivo no ha sido alterado y proviene de una fuente confiable.

### 8: En una instalación desde un servidor web

**Respuesta: La aplicación se instala automáticamente sólo si se trata de un archivo ejecutable.**  
La instalación automática desde un servidor web depende del tipo de archivo. Si es un ejecutable (como un **.exe** o un **.sh**), puede instalarse directamente. Otros formatos (como **.deb** o **.jar**) requieren pasos adicionales.
