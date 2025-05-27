---
tags: [AD, DAM]
cssclasses:
  - dam-ad
  - table-clean
banner: "![[ad.jpg]]"
banner_y: 0.32
---

# **Ejercicios TEMA 2.1.** <br>Sistemas de ficheros
## Instrucciones
1. Crea un proyecto para hacer los ejercicios.
2. Crea un paquete con una clase. Esta clase será abstracta y tendrá un método de clase para cada uno de los ejercicios a no ser que en algún ejercicio diga lo contrario.
3. Crea otro paquete con una clase con main. Desde esta clase prueba todos los métodos creados en los ejercicios.
4. Crea una excepción para tratar los errores propios de la aplicación.
5. Propaga las excepciones hasta el main y tratándolas allí.
## Ejercicios
### Ejercicio 1: Construir un path a partir de un String y mostrar información
**Descripción.** Este ejercicio nos permite familiarizarnos con la clase Path de Java NIO, que proporciona una forma de trabajar con rutas de archivos y directorios de manera independiente del sistema operativo. Es fundamental entender cómo construir y manipular paths antes de realizar operaciones con archivos.
```java
package com.example.ficheros; // Define el paquete donde se encuentra la clase
import java.io.IOException; // Importa la clase para manejar excepciones de E/S
import java.nio.file.*; // Importa las clases principales de NIO para trabajar con ficheros (Path, Paths, Files)
import java.nio.file.attribute.BasicFileAttributes; // Importa la clase para obtener atributos básicos de ficheros
import java.util.List; // Importa la clase List para manejar colecciones de líneas
/**
 * Clase abstracta que contiene métodos estáticos para trabajar con sistemas de ficheros.
 * Al ser abstracta, no se pueden crear instancias directas de esta clase.
 */
public abstract class SistemaFicheros {  
    /**
     * Construye un objeto Path a partir de un String que representa una ruta
     * y muestra diversa información sobre ese Path utilizando sus métodos.
     * @param ruta String que contiene la ruta del fichero o directorio.
     * @throws MiExcepcion Si ocurre un error al intentar crear o analizar el Path (p.ej., ruta inválida).
     */
    public static void muestraInfoPath(String ruta) throws MiExcepcion {
        // Inicio del bloque try-catch para manejar posibles excepciones
        try {
            // Crea un objeto Path a partir de la cadena de texto 'ruta' usando la clase de utilidad Paths.
            Path path = Paths.get(ruta);
            // Imprime la representación del Path tal como se creó.
            System.out.println("Información del path: " + path);
            // Imprime la representación en String del Path (equivalente a path.toString()).
            System.out.println("toString: " + path.toString());
            // Imprime el último componente del Path (nombre del fichero o directorio). Puede ser null si el path termina en '/'.
            System.out.println("getFileName: " + path.getFileName());
            // Imprime el primer elemento de la ruta (si existe). Comprueba antes si getNameCount() > 0.
            System.out.println("getName(0): " + (path.getNameCount() > 0 ? path.getName(0) : "No tiene elementos"));
            // Imprime el número de elementos en la ruta (directorios/fichero).
            System.out.println("getNameCount: " + path.getNameCount());
            // Imprime una subruta desde el índice 0 hasta el 1 (excluyente). Comprueba antes si getNameCount() > 1.
            System.out.println("subpath(0,1): " + (path.getNameCount() > 1 ? path.subpath(0, 1) : "No se puede obtener subpath"));
            // Imprime el Path padre del Path actual (null si no tiene padre o es la raíz).
            System.out.println("getParent: " + path.getParent());
            // Imprime la raíz del Path (p.ej., "/" en Linux, "C:\\" en Windows). Null si es relativa.
            System.out.println("getRoot: " + path.getRoot());
            // Imprime true si el Path es absoluto (empieza desde la raíz), false si es relativo.
            System.out.println("isAbsolute: " + path.isAbsolute());
            // Imprime la representación absoluta del Path, resolviéndola si es relativa respecto al directorio actual.
            System.out.println("toAbsolutePath: " + path.toAbsolutePath());
            // Imprime la representación URI del Path (p.ej., file:///...). Útil para interoperabilidad.
            System.out.println("toUri: " + path.toUri());
        // Captura cualquier excepción que pueda ocurrir dentro del bloque try (p.ej., InvalidPathException).
        } catch (Exception e) {
            // Envuelve la excepción original en una MiExcepcion personalizada y la lanza hacia arriba.
            throw new MiExcepcion("Error al procesar el path: " + e.getMessage(), e);
        }
    }
### Ejercicio 2: Mostrar información de un archivo
**Descripción.** La clase Files proporciona métodos estáticos para trabajar con archivos y directorios. Este ejercicio nos permite explorar las propiedades de un archivo como su tamaño, permisos, fechas de creación y modificación, lo que es esencial para la gestión de archivos.
```java
    /**
     * Muestra información detallada sobre un fichero o directorio utilizando la clase Files.
     * Verifica la existencia y tipo del elemento antes de mostrar sus atributos.
     * @param ruta String con la ruta del fichero o directorio.
     * @throws MiExcepcion Si el fichero no existe o si ocurre un error de E/S al leer sus atributos.
     */
    public static void muestraInfoArchivo(String ruta) throws MiExcepcion {
        // Inicio del bloque try-catch para manejar excepciones de E/S.
        try {
            // Convierte la cadena de texto 'ruta' en un objeto Path.
            Path path = Paths.get(ruta);
            // Comprueba si el fichero o directorio especificado por el Path existe en el sistema de ficheros.
            if (!Files.exists(path)) {
                // Si no existe, lanza una excepción personalizada indicándolo.
                throw new MiExcepcion("El archivo o directorio no existe: " + ruta);
            }
            // Imprime el nombre del fichero o directorio.
            System.out.println("Información del archivo/directorio: " + path.getFileName());
            // Imprime la ruta absoluta.
            System.out.println("Ruta absoluta: " + path.toAbsolutePath());
            // Comprueba e imprime si el Path corresponde a un directorio.
            System.out.println("Es directorio: " + Files.isDirectory(path));
            // Comprueba e imprime si el Path corresponde a un fichero regular (no directorio, no enlace simbólico, etc.).
            System.out.println("Es archivo regular: " + Files.isRegularFile(path));
            // Comprueba e imprime si el Path corresponde a un enlace simbólico.
            System.out.println("Es enlace simbólico: " + Files.isSymbolicLink(path));
            // Imprime el tamaño del fichero en bytes. Lanza excepción si es un directorio.
            // Se añade una comprobación para evitar error si es directorio.
            if (Files.isRegularFile(path)) {
                 System.out.println("Tamaño: " + Files.size(path) + " bytes");
            } else {
                 System.out.println("Tamaño: N/A (es un directorio)");
            }
            // Comprueba e imprime si el fichero tiene permisos de lectura para el usuario actual.
            System.out.println("Permisos de lectura: " + Files.isReadable(path));
            // Comprueba e imprime si el fichero tiene permisos de escritura para el usuario actual.
            System.out.println("Permisos de escritura: " + Files.isWritable(path));
            // Comprueba e imprime si el fichero tiene permisos de ejecución para el usuario actual.
            System.out.println("Permisos de ejecución: " + Files.isExecutable(path));
            // Lee los atributos básicos del fichero (fechas, tamaño, etc.).
            BasicFileAttributes attrs = Files.readAttributes(path, BasicFileAttributes.class);
            // Imprime la fecha y hora de creación del fichero.
            System.out.println("Fecha de creación: " + attrs.creationTime());
            // Imprime la fecha y hora del último acceso al fichero.
            System.out.println("Fecha de último acceso: " + attrs.lastAccessTime());
            // Imprime la fecha y hora de la última modificación del fichero.
            System.out.println("Fecha de última modificación: " + attrs.lastModifiedTime());
        // Captura específicamente excepciones de E/S (IOException).
        } catch (IOException e) {
            // Envuelve la IOException en una MiExcepcion personalizada y la lanza.
            throw new MiExcepcion("Error al acceder al archivo/directorio: " + e.getMessage(), e);
        }
    }
```
### Ejercicio 3: Crear un directorio
**Descripción.** La creación de directorios es una operación básica en la gestión de archivos. Este ejercicio nos permite aprender a crear directorios utilizando la clase Files, lo que es útil para organizar archivos y preparar estructuras de almacenamiento.
```java
    /**
     * Crea un directorio en la ruta especificada. Si los directorios padre no existen,
     * también los crea (similar al comando 'mkdir -p').
     * @param ruta String con la ruta del directorio a crear.
     * @throws MiExcepcion Si ocurre un error de E/S durante la creación del directorio.
     */
    public static void creaDirectorio(String ruta) throws MiExcepcion {
        // Inicio del bloque try-catch para manejar excepciones de E/S.
        try {
            // Convierte la cadena de texto 'ruta' en un objeto Path.
            Path path = Paths.get(ruta);
            // Comprueba si el directorio (o fichero) ya existe en la ruta especificada.
            if (Files.exists(path)) {
                // Si ya existe, informa al usuario y no intenta crearlo de nuevo.
                System.out.println("El directorio o fichero ya existe: " + path);
                // Sale del método.
                return;
            }
            // Intenta crear el directorio. Si los directorios padre no existen, los crea también.
            Files.createDirectories(path);
            // Informa al usuario que el directorio se ha creado correctamente.
            System.out.println("Directorio creado correctamente: " + path);
        // Captura específicamente excepciones de E/S (IOException).
        } catch (IOException e) {
            // Envuelve la IOException en una MiExcepcion personalizada y la lanza.
            throw new MiExcepcion("Error al crear el directorio: " + e.getMessage(), e);
        }
    }
```
### Ejercicio 4: Copiar un fichero
**Descripción.** La copia de archivos es una operación común en aplicaciones que manejan datos. Este ejercicio nos enseña a utilizar el método copy de la clase Files para duplicar archivos, lo que es útil para crear respaldos o mover datos entre ubicaciones.
```java
    /**
     * Copia un fichero desde una ruta origen a una ruta destino.
     * Si el directorio destino no existe, lo crea. Si el fichero destino ya existe, lo reemplaza.
     * @param origen String con la ruta del fichero origen.
     * @param destino String con la ruta del fichero destino.
     * @throws MiExcepcion Si el fichero origen no existe, no es un fichero regular,
     *                     o si ocurre un error de E/S durante la copia.
     */
    public static void copiaFichero(String origen, String destino) throws MiExcepcion {
        // Inicio del bloque try-catch para manejar excepciones de E/S.
        try {
            // Convierte las cadenas de texto 'origen' y 'destino' en objetos Path.
            Path pathOrigen = Paths.get(origen);
            Path pathDestino = Paths.get(destino);
            // Comprueba si el fichero origen existe.
            if (!Files.exists(pathOrigen)) {
                // Si no existe, lanza una excepción personalizada.
                throw new MiExcepcion("El archivo origen no existe: " + origen);
            }
            // Comprueba si el origen es un fichero regular (no un directorio).
            if (!Files.isRegularFile(pathOrigen)) {
                // Si no es un fichero regular, lanza una excepción personalizada.
                throw new MiExcepcion("El origen no es un archivo regular: " + origen);
            }
            // Obtiene el directorio padre del destino.
            Path dirDestino = pathDestino.getParent();
            // Comprueba si el directorio padre del destino existe.
            if (dirDestino != null && !Files.exists(dirDestino)) {
                 // Si no existe, lo crea (junto con los directorios padre necesarios).
                Files.createDirectories(dirDestino);
            }
            // Copia el fichero desde el origen al destino.
            // StandardCopyOption.REPLACE_EXISTING indica que si el fichero destino ya existe, debe ser reemplazado.
            Files.copy(pathOrigen, pathDestino, StandardCopyOption.REPLACE_EXISTING);
            // Informa al usuario que la copia se ha realizado correctamente.
            System.out.println("Archivo copiado correctamente de " + origen + " a " + destino);
        // Captura específicamente excepciones de E/S (IOException).
        } catch (IOException e) {
            // Envuelve la IOException en una MiExcepcion personalizada y la lanza.
            throw new MiExcepcion("Error al copiar el archivo: " + e.getMessage(), e);
        }
    }
```
### Ejercicio 5: Mover un fichero
**Descripción.** Mover archivos es otra operación fundamental en la gestión de archivos. Este ejercicio nos enseña a utilizar el método move de la clase Files, que es más eficiente que copiar y luego eliminar, especialmente cuando se mueven archivos dentro del mismo sistema de archivos.
```java
    /**
     * Mueve (o renombra) un fichero desde una ruta origen a una ruta destino.
     * Si el directorio destino no existe, lo crea. Si el fichero destino ya existe, lo reemplaza.
     * @param origen String con la ruta del fichero origen.
     * @param destino String con la ruta del fichero destino.
     * @throws MiExcepcion Si el fichero origen no existe, no es un fichero regular,
     *                     o si ocurre un error de E/S durante el movimiento.
     */
    public static void mueveFichero(String origen, String destino) throws MiExcepcion {
        // Inicio del bloque try-catch para manejar excepciones de E/S.
        try {
            // Convierte las cadenas de texto 'origen' y 'destino' en objetos Path.
            Path pathOrigen = Paths.get(origen);
            Path pathDestino = Paths.get(destino);
            // Comprueba si el fichero origen existe.
            if (!Files.exists(pathOrigen)) {
                // Si no existe, lanza una excepción personalizada.
                throw new MiExcepcion("El archivo origen no existe: " + origen);
            }
            // Comprueba si el origen es un fichero regular (no un directorio).
            if (!Files.isRegularFile(pathOrigen)) {
                // Si no es un fichero regular, lanza una excepción personalizada.
                throw new MiExcepcion("El origen no es un archivo regular: " + origen);
            }
            // Obtiene el directorio padre del destino.
            Path dirDestino = pathDestino.getParent();
             // Comprueba si el directorio padre del destino existe.
            if (dirDestino != null && !Files.exists(dirDestino)) {
                 // Si no existe, lo crea (junto con los directorios padre necesarios).
                Files.createDirectories(dirDestino);
            }
            // Mueve el fichero desde el origen al destino.
            // StandardCopyOption.REPLACE_EXISTING indica que si el fichero destino ya existe, debe ser reemplazado.
            // El movimiento suele ser atómico si origen y destino están en el mismo sistema de ficheros.
            Files.move(pathOrigen, pathDestino, StandardCopyOption.REPLACE_EXISTING);
            // Informa al usuario que el movimiento se ha realizado correctamente.
            System.out.println("Archivo movido correctamente de " + origen + " a " + destino);
        //
(Content truncated due to size limit. Use line ranges to read in chunks)
