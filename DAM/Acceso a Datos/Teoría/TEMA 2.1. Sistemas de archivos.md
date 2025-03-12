---
number headings: first-level 0, max 3, _.1., skip ^skipped
obsidianUIMode: preview
banner: "![[ad.jpg]]"
banner_y: 0.2
---

# **TEMA 2.1.** Sistemas de archivos
## 1. Sistemas de archivos

El sistema de archivos es un método para almacenar y organizar archivos de ordenador y los datos que contienen para facilitar su localización y acceso.  

Generalmente, un sistema de archivos tiene directorios que asocian nombres de archivos con archivos, normalmente conectando el nombre de archivo a un índice en una tabla de asignación de archivos de algún tipo, como FAT en sistemas de archivos MS-DOS o los inodos de los sistemas Unix.  

En algunos sistemas de archivos, los nombres de archivos son estructurados, con sintaxis especiales para extensiones de archivos y números de versión. En otros, los nombres de archivos son simplemente cadenas de texto y las metadatos de cada archivo se almacenan por separado.  

## 2. Rutas

En sistemas de archivos jerárquicos, normalmente, se declara la ubicación precisa de un archivo con una cadena de texto llamada "ruta". La nomenclatura para rutas varía ligeramente de sistema en sistema, pero mantienen en general una misma estructura.  

Una ruta viene dada por una sucesión de nombres de directorios y subdirectorios, ordenados jerárquicamente de izquierda a derecha y separados por algún carácter especial que suele ser una barra (’/’) o barra invertida ('\') y puede acabar con el nombre de un archivo presente en la última rama de directorios especificada.  

Un archivo se identifica de forma única con su ruta. Una ruta puede ser absoluta, cuando contiene la raíz del sistema, o relativa cuando contiene solo parte de la ruta, o el inicio de la ruta no es la raíz.  

Por ejemplo:  

```bash
/home/sally/statusReport / (Solaris root)  
```

```powershell
C:\ (Windows root)  
```

Si comienza con `/` es una ruta absoluta a partir de la raíz del sistema de archivos.  

En cambio, si el primer carácter no es `/` se trata de una ruta relativa al directorio donde nos encontramos actualmente.  

Por ejemplo, si estamos dentro de la carpeta `home`, la ruta relativa al mismo archivo sería:  

```bash
sally/statusReport  
```

En un sistema Windows, una ruta es absoluta si comienza con el nombre de la unidad seguida de `:` y `\` Para el mismo archivo, la ruta absoluta sería:  

```powershell
c:\home\sally\statusReport
```

Las rutas relativas serán todas las que no incluyan el nombre de la unidad.  

```bash
home/sally/statusReport  // Relativa a la raíz  
sally/statusReport       // Si estamos situados en el directorio home
```

Tanto en sistemas Linux como Windows podemos utilizar los caracteres `.` y `..`. 

- `.` significa el directorio actual. Si estamos en la carpeta home:  

```bash
/sally/statusReport 
```

- `..` significa el directorio superior, el que incluye el actual. Por ejemplo, si nos encontramos en el directorio *joe*, para acceder al archivo *statusReport* podemos poner:  

```bash
../sally/statusReport
```

En el sistema de archivos podemos encontrar archivos especiales que sirven de referencia a otros archivos, los enlaces simbólicos. Cualquier operación realizada sobre el enlace se lleva a cabo con el archivo o directorio que enlaza, excepto la eliminación o el cambio de nombre. Normalmente son transparentes al usuario.  

### 2.1. **Comandos de consola básicos**

#### Cambiar de directorio

`cd` (Change Directory) tanto en sistemas Linux como Windows  

```bash
cd /home/sally    // Ruta relativa  
cd ./sally        // Desde home 
cd ..             // Va a home si estamos dentro del directorio joe  
```

---

#### Ver el contenido del directorio actual

`ls` en sistemas Linux.

`dir` en sistemas Windows.

## 3. La clase *Path*

Esta clase representa una ruta dentro del sistema de archivos. Puede hacer referencia a un archivo, a un directorio o no existir. Utiliza la notación propia del sistema de archivos que estamos utilizando.  

### 3.1. **Crear un objeto de la clase *Path***

La forma más sencilla es utilizando el método estático of. Recibe como parámetro una cadena con la ruta que queremos utilizar:  

```bash
Path p1 = Path.of("/home/sally/statusReport");  

Path p2 = Path.of("home","sally","statusReport"); // Junta las cadenas
                                                     para formar la ruta.  

Path p3 = Path.of(URLcreate("file:///home/sally/statusReport");  
```

Para cada nivel de la ruta guarda un elemento que lo representa.  

### 3.2. **Recuperar información del *Path***

Si tenemos el path **/home/joe/foo** entonces:  

- `.toString()` devuelve **/home/joe/foo.**  
- `.getNameCount()` devuelve cuántos elementos hay en el path.  
- `.getName(index)` devuelve el path del elemento de la ruta en esta posición.
- `.getName(0)` devuelve **home.**  
- `.getFileName()` devuelve el path que representa el último elemento de la ruta, tanto si es un archivo como un directorio. En este caso **foo.**  
- `.subpath(inicio, fin)` devuelve el path entre la posición inicio y fin.
- `.subPath(0,2)` devuelve **home/joe.**

## 4. La clase *Files*

Es una clase de utilidad (una clase abstracta con métodos de clase) que nos permite leer, escribir y manipular archivos y directorios.

### 4.1. **Consultas**

- `Files.isRegularFile(path)` true si el path que recibe como argumento es un archivo, false si es un directorio o un enlace.
- `Files.isDirectory(path)` true si el path que recibe como argumento es un directorio.
- `Files.isReadable(path)`  
- `Files.isWriteable(path)` 
- `Files.isExecutable(path)`  
- `Files.isSameFile(path1, path2)` true si los dos paths que recibe como argumentos representan el mismo objeto.
- `Files.size(path)` tamaño del archivo en bytes.  
- `Files.isHidden(path)`
- `Files.get/setLastModifiedTime(path)`
- `Files.get/setOwner(path)`

### 4.2. **Crear directorio**

- `Files.createDirectory(Path)` Crea el directorio definido por el parámetro. La ruta donde queremos crear el directorio debe existir. Es decir, si queremos crear **/home/joe/pruebas**, la ruta **/home/joe** debe existir.  
- `Files.createDirectories(Path)` Crea el directorio definido por el parámetro. Si la ruta donde queremos crear el directorio no existe, la crea. Es decir, si queremos crear **/home/joe/pruebas** y no existe el directorio **joe**, también lo crea.  

### 4.3. **Eliminar archivos o directorios**

`Files.delete(Path)` Elimina el objeto representado por el path.  

### 4.4. **Copiar archivos o directorios**

`Files.copy(origen, destino, opciones)` Origen y destino son paths y opciones es un *vararg* para las constantes `StandardCopyOption.REPLACE_EXISTING`, `COPY_ATTRIBUTES`, `LinkOption.NOFOLLOW_LINKS`.  

### 4.5. **Mover archivos o directorios**

`Files.move(origen, destino, opciones)` Origen y destino son paths y opciones es un *vararg* para las constantes `StandardCopyOption.REPLACE_EXISTING`, `StandardCopyOption.ATOMIC_MOVE`.  

### 4.6. **Leer y escribir contenidos del archivo**

Estos métodos nos servirán cuando necesitemos manipular archivos sencillos. Para otros casos será mucho mejor utilizar los streams que veremos próximamente.  

#### `Files.write(Path, bytes[], opciones)`

Escribe el contenido del array de bytes al archivo. Dentro de las opciones podemos decidir cómo se abre el archivo:

- `StandardOpenOption.WRITE` Abre el archivo para escritura.  
- `StandardOpenOption.READ` Abre el archivo para lectura.
- `StandardOpenOption.CREATE` Lo abre si existe y si no lo crea.
- `StandardOpenOption.APPEND` Junto con los anteriores lo abre al final para añadir datos.  

El siguiente código abre para escritura el archivo /home/joe/doi.txt. Si no existe lo crea. Añade los bytes de la cadena de texto al final del archivo.  

```bash
Files.write(Path.of("/home/joe/doi.txt"),"Esto era y no era".getBytes(StandardCharsets.UTF_8), StandardOpenOption.CREATE, StandardOpenOption.APPEND);
```

#### `Files.readAllBytes(path)`

Lee el contenido del archivo como bytes. Devuelve `byte[]`. 

```bash
try {  
  byte[] bytes = Files.readAllBytes(Path.of(files.toString() + "/doi.txt"));
  System.out.println(Arrays.toString(bytes));
} catch (IOException e) {
  System.out.println("Error:"+e.getMessage());
}
```

Si leemos el archivo escrito anteriormente veremos por pantalla:

```bash
[ 65, 105, 120, 111, 32, 101, 114, 97, 32, 105, 32, 110, 111, 32, 101, 114, 97 ]
```

#### `Files.readAllLines(Path)`

```bash
try {
  List linees = Files.readAllLines(Path.of(fitxers.toString() + "/doi.txt"));
  System.out.println(linees);
} catch (IOException e) {
  System.out.println("Error:" + e.getMessage());
}
```

Si leemos el archivo escrito anteriormente veremos por pantalla:  

```bash
[Esto era y no era]
```

Este método está sobrescrito con una versión que acepta como parámetro el juego de caracteres en el que está escrito el texto.  

Por ejemplo, si queremos especificar que el archivo contiene caracteres en UTF-8:  

```bash
List linies = Files.readAllLines(Path.of(fitxers.toString() + "/doi.txt"), StandardCharsets.UTF_8);
```

O si está escrito en el juego de caracteres que utiliza normalmente Windows:

```bash
List linies = Files.readAllLines(Path.of(fitxers.toString() + "/doi.txt"), StandardCharsets.ISO_8859_1);
```

### 4.7. **Leer el contenido de un directorio**

#### `Files.newDirectoryStream()`

Devuelve un stream donde cada elemento es un path dentro del directorio. 

```bash
Path dir = ...;  

try (DirectoryStream<Path> stream = Files.newDirectoryStream(dir)) {  
  for (Path file: stream) {  
    System.out.println(file.getFileName());  
  }  
}
```
