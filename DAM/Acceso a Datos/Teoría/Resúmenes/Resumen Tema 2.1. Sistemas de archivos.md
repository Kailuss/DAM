---
number headings: first-level 0, start-at 1, max 2, _.1., auto, contents ^toc, skip ^skipped
obsidianUIMode: preview
banner: "![[../../../../Banners/ad.jpg]]"
banner_y: 0.19
---

# Resumen Tema 2.1. Sistemas de archivos

Este tema aborda los conceptos fundamentales de los sistemas de archivos, las rutas y cómo interactuar con ellos mediante comandos de consola y clases en programación. A continuación, se presenta un resumen que mantiene los conceptos clave y el código relevante:

## 1. Sistemas de archivos

Un sistema de archivos es un método para almacenar y organizar archivos y datos en una computadora, facilitando su localización y acceso. Los sistemas de archivos utilizan directorios para asociar nombres de archivos con los archivos mismos, a menudo mediante índices como la tabla FAT en MS-DOS o los inodos en Unix. Los nombres de archivos pueden ser estructurados (con extensiones y números de versión) o simplemente cadenas de texto, con metadatos almacenados por separado.

## 2. Rutas

Las rutas son cadenas de texto que especifican la ubicación de un archivo en un sistema de archivos jerárquico. Pueden ser **absolutas** (desde la raíz del sistema) o **relativas** (desde el directorio actual). 

Rutas absolutas:

```bash
/home/sally/statusReport  # En Linux
C:\home\sally\statusReport  # En Windows
```

Rutas relativas:

```bash
sally/statusReport  # Si estamos en /home
```

Se utilizan los caracteres `.` (directorio actual) y `..` (directorio superior) para navegar:

```bash
cd ..  # Sube un nivel
cd ./sally  # Navega a sally desde el directorio actual
```

### **2.1. La clase _Path_**

La clase `Path` representa una ruta en el sistema de archivos y puede referirse a un archivo, directorio o no existir. Se puede crear un objeto `Path` de varias formas:

```java
Path p1 = Path.of("/home/sally/statusReport");
Path p2 = Path.of("home", "sally", "statusReport");
```

#### 2.1.1 Métodos útiles de _Path_

`.toString()`: Devuelve la ruta como cadena.

`.getNameCount()`: Devuelve el número de elementos en la ruta.

`.getName(index)`: Devuelve el elemento en la posición especificada.

`.getFileName()`: Devuelve el último elemento de la ruta.

`.subpath(inicio, fin)`: Devuelve una subruta entre las posiciones especificadas.

### **2.2. La clase _Files_**

La clase `Files` proporciona métodos para manipular archivos y directorios. Es una clase de utilidad con métodos estáticos.

#### 2.2.1 Consultas

`Files.isRegularFile(path)`: Verifica si es un archivo.

`Files.isDirectory(path)`: Verifica si es un directorio.

`Files.size(path)`: Devuelve el tamaño del archivo en bytes.

`Files.isSameFile(path1, path2)`: Verifica si dos rutas apuntan al mismo archivo.

#### 2.2.2 Crear directorios

`Files.createDirectory(path)`: Crea un directorio (la ruta padre debe existir).

`Files.createDirectories(path)`: Crea directorios, incluyendo los padres si no existen.

#### 2.2.3 Eliminar archivos o directorios

`Files.delete(path)`: Elimina el archivo o directorio.

#### 2.2.4 Copiar archivos o directorios

`Files.copy(origen, destino, opciones)`: Copia archivos o directorios.

#### 2.2.5 Mover archivos o directorios

`Files.move(origen, destino, opciones)`: Mueve archivos o directorios.

#### 2.2.6 Leer y escribir archivos

Escribir:

```java
Files.write(Path.of("/home/joe/doi.txt"), "Texto".getBytes(), StandardOpenOption.CREATE, StandardOpenOption.APPEND);
```

Leer:

```java
byte[] bytes = Files.readAllBytes(Path.of("/home/joe/doi.txt"));
List<String> lines = Files.readAllLines(Path.of("/home/joe/doi.txt"), StandardCharsets.UTF_8);
```

#### 2.2.7 Leer el contenido de un directorio

`Files.newDirectoryStream(path)`: Devuelve un stream con los archivos del directorio.

```java
try (DirectoryStream<Path> stream = Files.newDirectoryStream(dir)) {
    for (Path file : stream) {
        System.out.println(file.getFileName());
    }
}
```

## 3. Conclusión

El documento cubre los conceptos básicos de los sistemas de archivos, cómo se estructuran las rutas y cómo interactuar con archivos y directorios mediante comandos de consola y clases como `Path` y `Files` en programación. Estos conceptos son esenciales para la gestión de archivos en sistemas operativos y aplicaciones.
