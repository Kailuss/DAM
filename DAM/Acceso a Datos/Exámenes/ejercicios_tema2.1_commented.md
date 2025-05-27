# Ejercicios TEMA 2.1: Sistemas de ficheros

## Instrucciones

1. Crea un proyecto para hacer los ejercicios.
2. Crea un paquete con una clase. Esta clase será abstracta y tendrá un método de clase para cada uno de los ejercicios a no ser que en algún ejercicio diga lo contrario.
3. Crea otro paquete con una clase con main. Desde esta clase prueba todos los métodos creados en los ejercicios.
4. Crea una excepción para tratar los errores propios de la aplicación.
5. Propaga las excepciones hasta el main y tratándolas allí.

## Ejercicios

### Ejercicio 1: Construir un path a partir de un String y mostrar información

**Descripción**: Este ejercicio nos permite familiarizarnos con la clase Path de Java NIO, que proporciona una forma de trabajar con rutas de archivos y directorios de manera independiente del sistema operativo. Es fundamental entender cómo construir y manipular paths antes de realizar operaciones con archivos.

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

**Descripción**: La clase Files proporciona métodos estáticos para trabajar con archivos y directorios. Este ejercicio nos permite explorar las propiedades de un archivo como su tamaño, permisos, fechas de creación y modificación, lo que es esencial para la gestión de archivos.

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

**Descripción**: La creación de directorios es una operación básica en la gestión de archivos. Este ejercicio nos permite aprender a crear directorios utilizando la clase Files, lo que es útil para organizar archivos y preparar estructuras de almacenamiento.

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

**Descripción**: La copia de archivos es una operación común en aplicaciones que manejan datos. Este ejercicio nos enseña a utilizar el método copy de la clase Files para duplicar archivos, lo que es útil para crear respaldos o mover datos entre ubicaciones.

```java
    /**
     * Copia un fichero desde una ruta origen a una ruta destino.
     * Si el directorio destino no existe, lo crea. Si el fichero destino ya existe, lo reemplaza.
     * @param origen String con la ruta del fichero origen.
     * @param destino String con la ruta del fichero destino.
     * @throws MiExcepcion Si el fichero origen no existe, no es un fichero regular,
     *                     o si ocurre un error de E/S durante la copia.
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

**Descripción**: Mover archivos es otra operación fundamental en la gestión de archivos. Este ejercicio nos enseña a utilizar el método move de la clase Files, que es más eficiente que copiar y luego eliminar, especialmente cuando se mueven archivos dentro del mismo sistema de archivos.

```java
    /**
     * Mueve (o renombra) un fichero desde una ruta origen a una ruta destino.
     * Si el directorio destino no existe, lo crea. Si el fichero destino ya existe, lo reemplaza.
     * @param origen String con la ruta del fichero origen.
     * @param destino String con la ruta del fichero destino.
     * @throws MiExcepcion Si el fichero origen no existe, no es un fichero regular,
     *                     o si ocurre un error de E/S durante el movimiento.
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
        // Captura específicamente excepciones de E/S (IOException).
        } catch (IOException e) {
            // Envuelve la IOException en una MiExcepcion personalizada y la lanza.
            throw new MiExcepcion("Error al mover el archivo: " + e.getMessage(), e);
        }
    }
```

### Ejercicio 6: Añadir texto al final de un fichero

**Descripción**: Añadir contenido a un archivo existente es una operación común en aplicaciones que generan logs o que necesitan actualizar datos. Este ejercicio nos enseña a utilizar la clase Files para añadir texto al final de un archivo, preservando su contenido original.

```java
    /**
     * Añade una cadena de texto al final de un fichero especificado.
     * Si el fichero no existe, lo crea.
     * @param ruta String con la ruta del fichero.
     * @param texto String con el texto a añadir.
     * @throws MiExcepcion Si ocurre un error de E/S al escribir en el fichero.
     */
    public static void añadeTextoAlFinal(String ruta, String texto) throws MiExcepcion {
        // Inicio del bloque try-catch para manejar excepciones de E/S.
        try {
            // Convierte la cadena de texto 'ruta' en un objeto Path.
            Path path = Paths.get(ruta);

            // Comprueba si el fichero no existe.
            // Aunque Files.write con CREATE lo haría, esta comprobación es explícita.
            // if (!Files.exists(path)) {
            //     // Si no existe, lo crea.
            //     Files.createFile(path);
            // }

            // Escribe los bytes del texto en el fichero.
            // StandardOpenOption.CREATE: Crea el fichero si no existe.
            // StandardOpenOption.APPEND: Escribe los datos al final del fichero en lugar de sobrescribir.
            Files.write(path, texto.getBytes(), StandardOpenOption.CREATE, StandardOpenOption.APPEND);
            // Informa al usuario que el texto se ha añadido correctamente.
            System.out.println("Texto añadido correctamente al final del archivo: " + path);
        // Captura específicamente excepciones de E/S (IOException).
        } catch (IOException e) {
            // Envuelve la IOException en una MiExcepcion personalizada y la lanza.
            throw new MiExcepcion("Error al añadir texto al fichero: " + e.getMessage(), e);
        }
    }
```

### Ejercicio 7: Leer el contenido de un fichero de texto

**Descripción**: La lectura de archivos de texto es una operación básica en muchas aplicaciones. Este ejercicio nos enseña a utilizar la clase Files para leer el contenido completo de un archivo de texto y devolverlo como una lista de cadenas, donde cada elemento representa una línea del archivo.

```java
    /**
     * Lee todo el contenido de un fichero de texto y lo devuelve como una lista de Strings,
     * donde cada String representa una línea del fichero.
     * @param ruta String con la ruta del fichero a leer.
     * @return Una List<String> con las líneas del fichero.
     * @throws MiExcepcion Si el fichero no existe, no es un fichero regular,
     *                     o si ocurre un error de E/S durante la lectura.
     */
    public static List<String> leeContenidoFichero(String ruta) throws MiExcepcion {
        // Inicio del bloque try-catch para manejar excepciones de E/S.
        try {
            // Convierte la cadena de texto 'ruta' en un objeto Path.
            Path path = Paths.get(ruta);

            // Comprueba si el fichero existe.
            if (!Files.exists(path)) {
                // Si no existe, lanza una excepción personalizada.
                throw new MiExcepcion("El archivo no existe: " + ruta);
            }

            // Comprueba si es un fichero regular (no un directorio).
            if (!Files.isRegularFile(path)) {
                // Si no es un fichero regular, lanza una excepción personalizada.
                throw new MiExcepcion("No es un archivo regular: " + ruta);
            }

            // Lee todas las líneas del fichero y las almacena en una lista de Strings.
            // Este método asume la codificación por defecto del sistema (puede especificarse otra).
            List<String> lineas = Files.readAllLines(path);
            // Informa al usuario que la lectura se ha realizado correctamente.
            System.out.println("Archivo leído correctamente: " + path);
            // Devuelve la lista de líneas leídas.
            return lineas;
        // Captura específicamente excepciones de E/S (IOException).
        } catch (IOException e) {
            // Envuelve la IOException en una MiExcepcion personalizada y la lanza.
            throw new MiExcepcion("Error al leer el fichero: " + e.getMessage(), e);
        }
    }
} // Fin de la clase SistemaFicheros
```

### Clase de excepción personalizada

**Descripción**: Para manejar los errores específicos de nuestra aplicación, creamos una clase de excepción personalizada que extiende de Exception. Esto nos permite propagar errores con mensajes descriptivos y mantener la causa original del error.

```java
package com.example.ficheros; // Define el paquete donde se encuentra la clase

/**
 * Excepción personalizada para encapsular errores específicos de la lógica
 * de manejo de ficheros dentro de esta aplicación. Extiende Exception,
 * lo que la convierte en una excepción comprobada (checked exception).
 */
public class MiExcepcion extends Exception {

    /**
     * Constructor por defecto sin parámetros.
     * Llama al constructor de la clase padre (Exception).
     */
    public MiExcepcion() {
        // Llama al constructor de Exception().
        super();
    }

    /**
     * Constructor que acepta un mensaje descriptivo del error.
     * @param mensaje String que describe la causa del error.
     */
    public MiExcepcion(String mensaje) {
        // Llama al constructor de Exception(String message).
        super(mensaje);
    }

    /**
     * Constructor que acepta un mensaje descriptivo y la excepción original (causa).
     * Esto es útil para mantener la traza de la excepción original.
     * @param mensaje String que describe la causa del error.
     * @param causa Throwable (la excepción original) que provocó esta MiExcepcion.
     */
    public MiExcepcion(String mensaje, Throwable causa) {
        // Llama al constructor de Exception(String message, Throwable cause).
        super(mensaje, causa);
    }
}
```

### Clase principal con main

**Descripción**: La clase principal contiene el método main que prueba todos los métodos implementados en la clase SistemaFicheros. Aquí se capturan y manejan las excepciones que puedan ocurrir durante la ejecución de los métodos.

```java
package com.example.main; // Define el paquete donde se encuentra la clase principal

import com.example.ficheros.MiExcepcion; // Importa la excepción personalizada
import com.example.ficheros.SistemaFicheros; // Importa la clase con los métodos de ficheros
import java.util.List; // Importa la clase List

/**
 * Clase principal que contiene el método main para ejecutar y probar
 * las funcionalidades definidas en la clase SistemaFicheros.
 */
public class Principal {

    /**
     * Punto de entrada de la aplicación. Llama a los diferentes métodos
     * de SistemaFicheros para demostrar su funcionamiento y maneja
     * las posibles MiExcepcion que puedan lanzar.
     * @param args Argumentos de línea de comandos (no utilizados en este ejemplo).
     */
    public static void main(String[] args) {
        // Inicio del bloque try-catch general para capturar MiExcepcion.
        try {
            // Define rutas de ejemplo (ajustar según el sistema operativo y usuario).
            // IMPORTANTE: Asegúrate de que el directorio base /home/ubuntu/test_files exista o créalo.
            String baseDir = "/home/ubuntu/test_files"; // Directorio base para los ficheros de prueba
            SistemaFicheros.creaDirectorio(baseDir); // Crea el directorio base si no existe
            
            String rutaEjemplo = baseDir + "/documento.txt"; // Ruta para muestraInfoPath
            String dirEjemplo = baseDir + "/directorio_prueba"; // Directorio a crear
            String ficheroOrigen = "/etc/hosts"; // Fichero existente para copiar/mover (asegúrate de tener permisos de lectura)
            String ficheroCopia = dirEjemplo + "/hosts.copia"; // Destino de la copia
            String ficheroMovido = dirEjemplo + "/subdir/hosts.movido"; // Destino del movimiento
            String ficheroAnadir = dirEjemplo + "/subdir/log.txt"; // Fichero para añadir texto

            // --- Prueba de muestraInfoPath ---
            System.out.println("=== Prueba de muestraInfoPath ===");
            // Llama al método para mostrar información sobre una ruta.
            SistemaFicheros.muestraInfoPath(rutaEjemplo);
            System.out.println("--- Fin Prueba muestraInfoPath ---\n");

            // --- Prueba de muestraInfoArchivo --- 
            // Nota: Este método fallará si el fichero no existe. Lo probamos con un fichero que sabemos que existe.
            System.out.println("=== Prueba de muestraInfoArchivo ===");
            // Llama al método para mostrar información sobre un fichero existente.
            SistemaFicheros.muestraInfoArchivo(ficheroOrigen);
            System.out.println("--- Fin Prueba muestraInfoArchivo ---\n");

            // --- Prueba de creaDirectorio --- 
            // Crea el directorio principal y el subdirectorio necesario para mover el fichero después.
            System.out.println("=== Prueba de creaDirectorio ===");
            // Llama al método para crear un directorio (y subdirectorios si es necesario).
            SistemaFicheros.creaDirectorio(dirEjemplo + "/subdir");
            System.out.println("--- Fin Prueba creaDirectorio ---\n");

            // --- Prueba de copiaFichero ---
            System.out.println("=== Prueba de copiaFichero ===");
            // Llama al método para copiar un fichero.
            SistemaFicheros.copiaFichero(ficheroOrigen, ficheroCopia);
            System.out.println("--- Fin Prueba copiaFichero ---\n");

            // --- Prueba de mueveFichero ---
            System.out.println("=== Prueba de mueveFichero ===");
            // Llama al método para mover el fichero copiado previamente al subdirectorio.
            SistemaFicheros.mueveFichero(ficheroCopia, ficheroMovido);
            System.out.println("--- Fin Prueba mueveFichero ---\n");

            // --- Prueba de añadeTextoAlFinal ---
            System.out.println("=== Prueba de añadeTextoAlFinal ===");
            // Llama al método para añadir texto a un fichero (lo crea si no existe).
            SistemaFicheros.añadeTextoAlFinal(ficheroAnadir, "Primera línea añadida.\n");
            SistemaFicheros.añadeTextoAlFinal(ficheroAnadir, "Segunda línea añadida.\n");
            System.out.println("--- Fin Prueba añadeTextoAlFinal ---\n");

            // --- Prueba de leeContenidoFichero ---
            System.out.println("=== Prueba de leeContenidoFichero ===");
            // Llama al método para leer el contenido del fichero modificado.
            List<String> lineas = SistemaFicheros.leeContenidoFichero(ficheroAnadir);
            // Imprime cada línea leída del fichero.
            System.out.println("Contenido de " + ficheroAnadir + ":");
            // Itera sobre la lista de líneas obtenida.
            for (String linea : lineas) {
                // Imprime cada línea precedida por "> ".
                System.out.println("> " + linea);
            }
            System.out.println("--- Fin Prueba leeContenidoFichero ---\n");

        // Captura cualquier MiExcepcion lanzada por los métodos de SistemaFicheros.
        } catch (MiExcepcion e) {
            // Imprime un mensaje de error en la salida de error estándar.
            System.err.println("ERROR EN LA APLICACIÓN: " + e.getMessage());
            // Si la excepción tiene una causa (la excepción original), la imprime también.
            if (e.getCause() != null) {
                System.err.println("CAUSA ORIGINAL: " + e.getCause().getClass().getSimpleName() + ": " + e.getCause().getMessage());
            }
            // Imprime la traza completa de la pila de llamadas para depuración.
            e.printStackTrace();
        }
    }
}
```

