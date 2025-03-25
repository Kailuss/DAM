---
number headings: max 2, skip ^sk, _.1.1.
obsidianUIMode: preview
banner: "![[di.jpg]]"
banner_y: 0.28
cssclasses:
  - table-compact-clean
---
# **Resumen Tema 6.** <br> Documentación de Aplicaciones

## 1. Ficheros de Ayuda

Los ficheros de ayuda son esenciales para guiar a los usuarios en la instalación, configuración y uso de aplicaciones. En Java, se utiliza **JavaHelp** para generar estos ficheros.

| | |
|------------------------------|---------------------------------------------------------------------------------|
| **Mapa del fichero**         | Asocia identificadores de tema con URLs o rutas de archivos HTML.               |
| **Vista de Información**     | Muestra la información mediante una tabla de contenidos, índice y búsqueda.     |
| **Título del fichero**       | Aparece en la barra de título de la ventana de ayuda.                           |
| **Identificador de inicio**  | Define el tema que se muestra por defecto.                                      |
| **Presentación**             | Ventanas donde se muestran los temas de ayuda.                                  |
| **Sub-Ficheros de ayuda**    | Ficheros más pequeños que se fusionan para crear el fichero de ayuda principal. |
| **Implementación**           | Opcional, define la asignación de la clase `HelpBroker` y el visor de contenido.|

### Formatos comunes

| | |
|--------------|---------------------------------------------------------------------------------|
| **CHM**      | Ayuda HTML Compilado (Microsoft).                                              |
| **HLP**      | Formato WinHelp.                                                               |
| **IPF**      | Usado en sistemas IBM OS/2.                                                    |
| **JavaHelp** | Basado en XML, utilizado en aplicaciones Java.                                 |
| **PDF**      | Abierto por visores PDF o herramientas de ofimática.                           |
| **MAML**     | Lenguaje basado en XML para asistencia en sistemas Microsoft.                  |

## 2. Herramientas de Generación de Ayudas

|   |                                                            |
|-----------------------|---------------------------------------------------------------------------------|
| **Help Workshop**      | Para crear ficheros de ayuda en formato HLP y CHM.                              |
| **JavaHelp**           | Herramienta estándar para aplicaciones Java.                                    |
| **RoboHelp**           | Para crear sistemas de ayuda profesional.                                       |
| **WINHELP**            | Genera ficheros .HLP para Windows.                                              |
| **WEBHELP**            | Basado en HTML y DHTML.                                                         |
| **Help Magician**      | Para crear ayudas HTML o páginas web.                                           |
| **HelpMaker**          | Permite crear ficheros de ayuda en varios formatos.                             |
| **DOCBUILDER**         | Genera documentación en HTML, RTF y archivos de ayuda de Windows.               |

## 3. Ayuda Genérica y Sensible al Contexto

- **Ayuda genérica.** Proporciona acceso a todos los contenidos de ayuda. 
- **Ayuda sensible al contexto.** Muestra información relevante según la situación o el elemento activo.

**Uso de JavaHelp.**

- **Creación de temas de ayuda.** En formato HTML.
- **Creación de ficheros metadatos.** Incluye ficheros map, HelpSet, TOC, Índice y búsqueda.
- **Encapsulación en JAR.** Para distribuir el sistema de ayuda.

**Ejemplo de uso de `jhindexer`.**

```bash
jhindexer directorio_con_archivos_de_ayuda
```

**Verificación de búsqueda.**

```bash
jhsearch JavaHelpSearch
```

**Encapsulación en ficheros JAR.**

```bash
jar -cvf ayuda.jar *
```

**Ver archivos incluidos en el JAR.**

```bash
jar -tvf ayuda.jar
```

**Extraer archivos del JAR.**

```bash
jar -xvf ayuda.jar
```

**Incorporación de ayuda en aplicaciones Java.**

```java
import javax.help.*;

HelpSet hs = HelpSet.findHelpSet(null, "ruta/al/helpset.hs");
HelpBroker hb = hs.createHelpBroker();
hb.enableHelpKey(componente, "id_tema", hs);
```

## 4. Tablas de Contenidos (TOC)

| | |
|-----------------------------|---------------------------------------------------------------------------------|
| **Organización**            | Jerárquica, similar a las carpetas de un administrador de archivos.             |
| **Profundidad de niveles**  | Depende del tamaño y el detalle del diseño de la ayuda.                        |
| **Navegación**              | Mediante hipervínculos incrustados en el texto.                                 |

## 5. Índices

| | |
|-----------------------------|---------------------------------------------------------------------------------|
| **Lista de palabras clave** | Ordenadas alfabéticamente para facilitar el acceso a términos específicos.      |
| **Herramienta `jhindexer`** | Crea la base de datos de búsqueda necesaria para el índice.                     |

## 6. Sistemas de Búsqueda

| | |
|-----------------------------|---------------------------------------------------------------------------------|
| **Búsqueda de términos**    | Permite encontrar referencias de un término específico.                         |
| **Herramienta `jhsearch`**  | Realiza búsquedas en la base de datos generada por `jhindexer`.                 |

## 7. Incorporación de Ayuda a la Aplicación

| | |
|---------------------------------|---------------------------------------------------------------------------------|
| **Importar paquetes**           | `javax.help.*` y `java.net.*`.                                                  |
| **Localizar y crear HelpSet**   | `HelpSet.findHelpSet(null, "ayuda/ayuda.hs");`.                                 |
| **Crear HelpBroker**            | `HelpBroker hb = hs.createHelpBroker();`.                                       |
| **Asociar ayuda a botones**     | `hb.enableHelpOnButton(jButton1, "introducción", hs);`.                         |
| **Ayuda sensible al contexto**  | `hb.enableHelpKey(getRootPane(), "introduccion", hs);`.                         |

## 8. Tipos de Manuales

| | |
|---------------------------------|---------------------------------------------------------------------------------|
| **Manual de usuario**           | Detalla instalación, configuración y uso.                                       |
| **Guía de referencia**          | Para usuarios experimentados, con información técnica.                          |
| **Guías rápidas**               | Versión resumida de un manual.                                                  |
| **Manuales de instalación**     | Para administradores de sistemas.                                               |
| **Manuales de configuración**   | Para aplicaciones complejas.                                                    |

## 9. Confección de Tutoriales Multimedia

| | |
|--------------------------------|---------------------------------------------------------------------------------|
| **Snagit, Hypersnap DX**       | Captura de pantalla.                                                            |
| **CamStudio, Camtasia**        | Creación de videotutoriales.                                                    |

## 10. Herramientas de Confección de Manuales Interactivos

| | |
|--------------------------------|---------------------------------------------------------------------------------|
| **Adobe Captivate**            | Para crear tutoriales multimedia.                                               |
| **Wink**                       | Permite capturas de pantalla, vídeos, y añadir explicaciones.                   |
| **Malted**                     | Utilizado por el Ministerio de Educación, permite crear ejercicios interactivos.|

## Códigos Importantes

**JavaHelp**

```java

import javax.help.*;

HelpSet hs = HelpSet.findHelpSet(null, "ruta/al/helpset.hs");

HelpBroker hb = hs.createHelpBroker();

hb.enableHelpKey(componente, "id_tema", hs);

``` |
| **Encapsulación en JAR**       | ```bash
jar -cvf ayuda.jar *
jar -tvf ayuda.jar
jar -xvf ayuda.jar
``` |
| **Uso de `jhindexer` y `jhsearch`** | ```bash
jhindexer directorio_con_archivos_de_ayuda
jhsearch JavaHelpSearch
``` |

Este resumen en formato de tablas cubre los aspectos clave del tema, incluyendo los códigos y comandos más relevantes para el estudio.
