# Ejercicios TEMA 2.2: Streams

## Instrucciones

1. Crea un proyecto para hacer los ejercicios o aprovecha el del bloque de ejercicios anterior.
2. Crea un paquete donde guardarás todas las clases creadas en estos ejercicios.
3. Crea otro paquete con una clase con main. Desde esta clase prueba todos los métodos creados en los ejercicios.
4. Crea una excepción para tratar los errores propios de la aplicación (o reaprovecha la del bloque anterior).
5. Propaga las excepciones hasta el main y tratándolas allí.
6. Descarga del aula virtual la versión adecuada a tu sistema de el _Himno de los piratas de Mar y Cielo_ y el fichero del _Tirant Lo Blanc_.

## Ejercicios

### Ejercicio 1: Herramientas_ByteStream

**Descripción**: Los ByteStream son flujos de datos a nivel de bytes, útiles para trabajar con todo tipo de archivos, incluyendo binarios. Esta clase proporciona métodos para escribir, leer y copiar datos a nivel de bytes, lo que es fundamental para operaciones de bajo nivel con archivos.

```java
package com.example.streams; // Define el paquete donde se encuentra la clase

import java.io.File; // Para trabajar con archivos
import java.io.FileInputStream; // Para leer bytes de un archivo
import java.io.FileOutputStream; // Para escribir bytes en un archivo
import java.io.IOException; // Para manejar excepciones de E/S
import java.util.ArrayList; // Para almacenar bytes leídos temporalmente

/**
 * Clase de utilidad para trabajar con flujos de bytes (byte streams).
 * Esta clase es abstracta porque solo contiene métodos estáticos y no se instanciará.
 */
public abstract class Herramientas_ByteStream {
    
    /**
     * Guarda en un fichero el texto contenido en un array de bytes.
     * Útil para escribir datos binarios o texto en formato de bytes.
     * 
     * @param desti Ruta del fichero destino donde se escribirán los bytes
     * @param datos Array de bytes con los datos a escribir
     * @throws MiExcepcion Si hay algún error durante la escritura
     */
    public static void escribeByte(String desti, byte[] datos) throws MiExcepcion {
        // Declaramos el flujo fuera del try para poder cerrarlo en el finally
        // FileOutputStream es un flujo de salida para escribir bytes en un archivo
        FileOutputStream fos = null;
        
        try {
            // Abrimos el flujo de salida hacia el fichero
            // Si el fichero no existe, se crea; si existe, se sobrescribe
            fos = new FileOutputStream(desti);
            
            // Escribimos todos los bytes del array de una vez
            // Este método escribe el array completo en el archivo
            fos.write(datos);
            
            // Forzamos que se escriban los datos pendientes en el buffer
            // Esto asegura que todos los datos se escriban en el disco
            fos.flush();
            
            // Informamos al usuario que la operación se ha completado con éxito
            System.out.println("Datos escritos correctamente en: " + desti);
        } catch (IOException e) {
            // Si ocurre un error de E/S, lanzamos nuestra excepción personalizada
            // Incluimos el mensaje original y la excepción como causa
            throw new MiExcepcion("Error al escribir bytes: " + e.getMessage(), e);
        } finally {
            // Cerramos el flujo en el bloque finally para asegurar que se cierre
            // incluso si hay una excepción durante la escritura
            if (fos != null) {
                try {
                    // Intentamos cerrar el flujo
                    fos.close();
                } catch (IOException e) {
                    // Si hay un error al cerrar, lo mostramos pero no interrumpimos el programa
                    System.err.println("Error al cerrar el flujo: " + e.getMessage());
                }
            }
        }
    }
    
    /**
     * Lee un fichero byte a byte y devuelve un array con esos bytes.
     * Útil para leer cualquier tipo de archivo, incluyendo binarios.
     * 
     * @param origen Ruta del fichero a leer
     * @return Array de bytes con el contenido del fichero
     * @throws MiExcepcion Si hay algún error durante la lectura
     */
    public static byte[] tornaBytes(String origen) throws MiExcepcion {
        // Declaramos el flujo fuera del try para poder cerrarlo en el finally
        // FileInputStream es un flujo de entrada para leer bytes de un archivo
        FileInputStream fis = null;
        
        try {
            // Creamos un objeto File para obtener información del fichero
            // y verificar su existencia antes de intentar abrirlo
            File file = new File(origen);
            
            // Verificamos que el fichero existe
            if (!file.exists()) {
                // Si no existe, lanzamos una excepción personalizada
                throw new MiExcepcion("El fichero no existe: " + origen);
            }
            
            // Creamos una lista para almacenar los bytes leídos
            // Usamos ArrayList porque no sabemos cuántos bytes leeremos
            ArrayList<Byte> bytesList = new ArrayList<>();
            
            // Abrimos el flujo de entrada desde el fichero
            fis = new FileInputStream(file);
            
            // Variable para almacenar cada byte leído
            // read() devuelve un int entre 0-255 o -1 si es fin de archivo
            int byteLeido;
            
            // Leemos byte a byte hasta el final del fichero (-1)
            while ((byteLeido = fis.read()) != -1) {
                // Añadimos el byte a la lista (convertido de int a byte)
                bytesList.add((byte) byteLeido);
            }
            
            // Convertimos la lista de Byte (objeto) a un array de byte (primitivo)
            byte[] resultado = new byte[bytesList.size()];
            for (int i = 0; i < bytesList.size(); i++) {
                resultado[i] = bytesList.get(i);
            }
            
            // Informamos al usuario que la operación se ha completado con éxito
            System.out.println("Fichero leído correctamente: " + origen);
            return resultado;
        } catch (IOException e) {
            // Si ocurre un error de E/S, lanzamos nuestra excepción personalizada
            throw new MiExcepcion("Error al leer bytes: " + e.getMessage(), e);
        } finally {
            // Cerramos el flujo en el bloque finally
            if (fis != null) {
                try {
                    // Intentamos cerrar el flujo
                    fis.close();
                } catch (IOException e) {
                    // Si hay un error al cerrar, lo mostramos pero no interrumpimos el programa
                    System.err.println("Error al cerrar el flujo: " + e.getMessage());
                }
            }
        }
    }
    
    /**
     * Copia el contenido de un fichero a otro a nivel de bytes.
     * Más eficiente que leer todo y luego escribir, ya que usa un buffer.
     * 
     * @param origen Ruta del fichero origen
     * @param desti Ruta del fichero destino
     * @throws MiExcepcion Si hay algún error durante la copia
     */
    public static void copiaBytes(String origen, String desti) throws MiExcepcion {
        // Declaramos los flujos fuera del try para poder cerrarlos en el finally
        FileInputStream fis = null;
        FileOutputStream fos = null;
        
        try {
            // Abrimos el flujo de entrada desde el fichero origen
            fis = new FileInputStream(origen);
            
            // Abrimos el flujo de salida hacia el fichero destino
            fos = new FileOutputStream(desti);
            
            // Buffer para leer varios bytes a la vez (más eficiente)
            // 1024 bytes (1KB) es un tamaño común para el buffer
            byte[] buffer = new byte[1024];
            int bytesLeidos;
            
            // Leemos del origen y escribimos en el destino hasta el final
            // read(buffer) devuelve el número de bytes leídos o -1 si es fin de archivo
            while ((bytesLeidos = fis.read(buffer)) != -1) {
                // Escribimos solo los bytes que hemos leído
                // El tercer parámetro indica cuántos bytes escribir del buffer
                fos.write(buffer, 0, bytesLeidos);
            }
            
            // Forzamos que se escriban los datos pendientes
            fos.flush();
            
            // Informamos al usuario que la operación se ha completado con éxito
            System.out.println("Fichero copiado correctamente de " + origen + " a " + desti);
        } catch (IOException e) {
            // Si ocurre un error de E/S, lanzamos nuestra excepción personalizada
            throw new MiExcepcion("Error al copiar bytes: " + e.getMessage(), e);
        } finally {
            // Cerramos los flujos en el bloque finally
            if (fis != null) {
                try {
                    // Intentamos cerrar el flujo de entrada
                    fis.close();
                } catch (IOException e) {
                    // Si hay un error al cerrar, lo mostramos pero no interrumpimos el programa
                    System.err.println("Error al cerrar el flujo de entrada: " + e.getMessage());
                }
            }
            if (fos != null) {
                try {
                    // Intentamos cerrar el flujo de salida
                    fos.close();
                } catch (IOException e) {
                    // Si hay un error al cerrar, lo mostramos pero no interrumpimos el programa
                    System.err.println("Error al cerrar el flujo de salida: " + e.getMessage());
                }
            }
        }
    }
}
```

### Ejercicio 2: Herramientas_CharacterStream

**Descripción**: Los CharacterStream son flujos de datos a nivel de caracteres, ideales para trabajar con archivos de texto, especialmente cuando contienen caracteres especiales o acentos. Esta clase proporciona métodos para leer, escribir y copiar texto, asegurando que se preserven correctamente los caracteres.

```java
package com.example.streams; // Define el paquete donde se encuentra la clase

import java.io.FileReader; // Para leer caracteres de un archivo
import java.io.FileWriter; // Para escribir caracteres en un archivo
import java.io.IOException; // Para manejar excepciones de E/S

/**
 * Clase de utilidad para trabajar con flujos de caracteres (character streams).
 * Esta clase es abstracta porque solo contiene métodos estáticos y no se instanciará.
 */
public abstract class Herramientas_CharacterStream {
    
    /**
     * Lee un fichero carácter a carácter y lo muestra por consola.
     * Útil para visualizar el contenido de archivos de texto.
     * 
     * @param origen Ruta del fichero a leer
     * @throws MiExcepcion Si hay algún error durante la lectura
     */
    public static void muestraCharacters(String origen) throws MiExcepcion {
        // Declaramos el flujo fuera del try para poder cerrarlo en el finally
        // FileReader es un flujo de entrada para leer caracteres de un archivo
        FileReader fr = null;
        
        try {
            // Abrimos el flujo de entrada de caracteres desde el fichero
            // FileReader utiliza la codificación por defecto del sistema
            fr = new FileReader(origen);
            
            // Variable para almacenar cada carácter leído
            // read() devuelve un int que representa el código Unicode del carácter
            // o -1 si es fin de archivo
            int caracterLeido;
            
            // Mostramos un mensaje informativo
            System.out.println("Contenido del fichero " + origen + ":");
            
            // Leemos carácter a carácter hasta el final del fichero (-1)
            while ((caracterLeido = fr.read()) != -1) {
                // Convertimos el entero a carácter y lo mostramos
                // sin salto de línea para mantener el formato original
                System.out.print((char) caracterLeido);
            }
            
            // Añadimos un salto de línea al final e informamos del éxito
            System.out.println("\nFichero leído correctamente.");
        } catch (IOException e) {
            // Si ocurre un error de E/S, lanzamos nuestra excepción personalizada
            throw new MiExcepcion("Error al leer caracteres: " + e.getMessage(), e);
        } finally {
            // Cerramos el flujo en el bloque finally
            if (fr != null) {
                try {
                    // Intentamos cerrar el flujo
                    fr.close();
                } catch (IOException e) {
                    // Si hay un error al cerrar, lo mostramos pero no interrumpimos el programa
                    System.err.println("Error al cerrar el flujo: " + e.getMessage());
                }
            }
        }
    }
    
    /**
     * Guarda en un fichero el texto contenido en un String.
     * Útil para escribir texto en un archivo.
     * 
     * @param desti Ruta del fichero destino
     * @param datos String con los datos a escribir
     * @throws MiExcepcion Si hay algún error durante la escritura
     */
    public static void escribeCharacters(String desti, String datos) throws MiExcepcion {
        // Declaramos el flujo fuera del try para poder cerrarlo en el finally
        // FileWriter es un flujo de salida para escribir caracteres en un archivo
        FileWriter fw = null;
        
        try {
            // Abrimos el flujo de salida de caracteres hacia el fichero
            // Si el fichero no existe, se crea; si existe, se sobrescribe
            fw = new FileWriter(desti);
            
            // Escribimos todo el String de una vez
            // Este método escribe todos los caracteres del String en el archivo
            fw.write(datos);
            
            // Forzamos que se escriban los datos pendientes en el buffer
            // Esto asegura que todos los datos se escriban en el disco
            fw.flush();
            
            // Informamos al usuario que la operación se ha completado con éxito
            System.out.println("Datos escritos correctamente en: " + desti);
        } catch (IOException e) {
            // Si ocurre un error de E/S, lanzamos nuestra excepción personalizada
            throw new MiExcepcion("Error al escribir caracteres: " + e.getMessage(), e);
        } finally {
            // Cerramos el flujo en el bloque finally
            if (fw != null) {
                try {
                    // Intentamos cerrar el flujo
                    fw.close();
                } catch (IOException e) {
                    // Si hay un error al cerrar, lo mostramos pero no interrumpimos el programa
                    System.err.println("Error al cerrar el flujo: " + e.getMessage());
                }
            }
        }
    }
    
    /**
     * Copia el contenido de un fichero a otro a nivel de caracteres.
     * Útil para copiar archivos de texto preservando la codificación de caracteres.
     * 
     * @param origen Ruta del fichero origen
     * @param desti Ruta del fichero destino
     * @throws MiExcepcion Si hay algún error durante la copia
     */
    public static void copiaCharacters(String origen, String desti) throws MiExcepcion {
        // Declaramos los flujos fuera del try para poder cerrarlos en el finally
        FileReader fr = null;
        FileWriter fw = null;
        
        try {
            // Abrimos el flujo de entrada de caracteres desde el fichero origen
            fr = new FileReader(origen);
            
            // Abrimos el flujo de salida de caracteres hacia el fichero destino
            fw = new FileWriter(desti);
            
            // Buffer para leer varios caracteres a la vez (más eficiente)
            // 1024 caracteres es un tamaño común para el buffer
            char[] buffer = new char[1024];
            int caracteresLeidos;
            
            // Leemos del origen y escribimos en el destino hasta el final
            // read(buffer) devuelve el número de caracteres leídos o -1 si es fin de archivo
            while ((caracteresLeidos = fr.read(buffer)) != -1) {
                // Escribimos solo los caracteres que hemos leído
                // El tercer parámetro indica cuántos caracteres escribir del buffer
                fw.write(buffer, 0, caracteresLeidos);
            }
            
            // Forzamos que se escriban los datos pendientes
            fw.flush();
            
            // Informamos al usuario que la operación se ha completado con éxito
            System.out.println("Fichero copiado correctamente de " + origen + " a " + desti);
        } catch (IOException e) {
            // Si ocurre un error de E/S, lanzamos nuestra excepción personalizada
            throw new MiExcepcion("Error al copiar caracteres: " + e.getMessage(), e);
        } finally {
            // Cerramos los flujos en el bloque finally
            if (fr != null) {
                try {
                    // Intentamos cerrar el flujo de entrada
                    fr.close();
                } catch (IOException e) {
                    // Si hay un error al cerrar, lo mostramos pero no interrumpimos el programa
                    System.err.println("Error al cerrar el flujo de entrada: " + e.getMessage());
                }
            }
            if (fw != null) {
                try {
                    // Intentamos cerrar el flujo de salida
                    fw.close();
                } catch (IOException e) {
                    // Si hay un error al cerrar, lo mostramos pero no interrumpimos el programa
                    System.err.println("Error al cerrar el flujo de salida: " + e.getMessage());
                }
            }
        }
    }
    
    /**
     * Método inútil para medir el tiempo de lectura carácter a carácter.
     * Solo lee el archivo sin hacer nada con los datos, para pruebas de rendimiento.
     * 
     * @param origen Ruta del fichero a leer
     * @throws MiExcepcion Si hay algún error durante la lectura
     */
    public static void inutil(String origen) throws MiExcepcion {
        // Declaramos el flujo fuera del try para poder cerrarlo en el finally
        FileReader fr = null;
        
        try {
            // Abrimos el flujo de entrada de caracteres desde el fichero
            fr = new FileReader(origen);
            
            // Variable para almacenar cada carácter leído
            int caracterLeido;
            
            // Leemos carácter a carácter hasta el final del fichero (-1)
            // pero no hacemos nada con los caracteres leídos
            // Este bucle es "inútil" porque solo lee sin procesar los datos
            while ((caracterLeido = fr.read()) != -1) {
                // No hacemos nada, solo leemos
                // Este método se usa para medir el tiempo de lectura sin procesamiento
            }
        } catch (IOException e) {
            // Si ocurre un error de E/S, lanzamos nuestra excepción personalizada
            throw new MiExcepcion("Error al leer caracteres: " + e.getMessage(), e);
        } finally {
            // Cerramos el flujo en el bloque finally
            if (fr != null) {
                try {
                    // Intentamos cerrar el flujo
                    fr.close();
                } catch (IOException e) {
                    // Si hay un error al cerrar, lo mostramos pero no interrumpimos el programa
                    System.err.println("Error al cerrar el flujo: " + e.getMessage());
                }
            }
        }
    }
}
```

### Ejercicio 3: Herramientas_BufferedStream

**Descripción**: Los BufferedStream añaden un buffer a los flujos de datos, lo que mejora significativamente el rendimiento al reducir el número de accesos al sistema de archivos. Esta clase proporciona métodos para leer, escribir y copiar texto línea a línea, lo que es más eficiente y conveniente para muchas aplicaciones.

```java
package com.example.streams; // Define el paquete donde se encuentra la clase

import java.io.BufferedReader; // Para leer texto de manera eficiente con buffer
import java.io.BufferedWriter; // Para escribir texto de manera eficiente con buffer
import java.io.FileReader; // Para leer caracteres de un archivo
import java.io.FileWriter; // Para escribir caracteres en un archivo
import java.io.IOException; // Para manejar excepciones de E/S
import java.util.ArrayList; // Para almacenar líneas leídas

/**
 * Clase de utilidad para trabajar con flujos de caracteres con buffer.
 * Esta clase es abstracta porque solo contiene métodos estáticos y no se instanciará.
 */
public abstract class Herramientas_BufferedStream {
    
    /**
     * Lee un fichero línea a línea y devuelve un ArrayList con las líneas.
     * Mucho más eficiente que leer carácter a carácter.
     * 
     * @param origen Ruta del fichero a leer
     * @return ArrayList<String> con las líneas del fichero
     * @throws MiExcepcion Si hay algún error durante la lectura
     */
    public static ArrayList<String> tornaLine(String origen) throws MiExcepcion {
        // Declaramos los flujos fuera del try para poder cerrarlos en el finally
        FileReader fr = null;
        BufferedReader br = null;
        
        try {
            // Creamos un ArrayList para almacenar las líneas
            ArrayList<String> lineas = new ArrayList<>();
            
            // Abrimos el flujo de entrada de caracteres desde el fichero
            fr = new FileReader(origen);
            
            // Añadimos un buffer al flujo para leer líneas completas
            // BufferedReader mejora el rendimiento y permite leer líneas enteras
            br = new BufferedReader(fr);
            
            // Variable para almacenar cada línea leída
            String linea;
            
            // Leemos línea a línea hasta el final del fichero (null)
            // readLine() devuelve null cuando llega al final del archivo
            while ((linea = br.readLine()) != null) {
                // Añadimos la línea al ArrayList
                lineas.add(linea);
            }
            
            // Informamos al usuario que la operación se ha completado con éxito
            System.out.println("Fichero leído correctamente: " + origen);
            return lineas;
        } catch (IOException e) {
            // Si ocurre un error de E/S, lanzamos nuestra excepción personalizada
            throw new MiExcepcion("Error al leer líneas: " + e.getMessage(), e);
        } finally {
            // Cerramos los flujos en el bloque finally
            // Solo necesitamos cerrar el BufferedReader, que cerrará automáticamente el FileReader
            if (br != null) {
                try {
                    // Intentamos cerrar el flujo
                    br.close();
                } catch (IOException e) {
                    // Si hay un error al cerrar, lo mostramos pero no interrumpimos el programa
                    System.err.println("Error al cerrar el flujo: " + e.getMessage());
                }
            }
        }
    }
    
    /**
     * Guarda en un fichero el texto contenido en un array de Strings, uno por línea.
     * Útil para escribir colecciones de líneas en un archivo.
     * 
     * @param desti Ruta del fichero destino
     * @param datos Array de Strings con los datos a escribir
     * @throws MiExcepcion Si hay algún error durante la escritura
     */
    public static void escribeLine(String desti, String[] datos) throws MiExcepcion {
        // Declaramos los flujos fuera del try para poder cerrarlos en el finally
        FileWriter fw = null;
        BufferedWriter bw = null;
        
        try {
            // Abrimos el flujo de salida de caracteres hacia el fichero
            fw = new FileWriter(desti);
            
            // Añadimos un buffer al flujo para escribir líneas completas
            // BufferedWriter mejora el rendimiento y permite escribir líneas enteras
            bw = new BufferedWriter(fw);
            
            // Escribimos cada String del array en una línea
            for (String linea : datos) {
                // Escribimos la línea
                bw.write(linea);
                // Añadimos un salto de línea después de cada línea
                // newLine() añade el separador de línea específico del sistema
                bw.newLine();
            }
            
            // Forzamos que se escriban los datos pendientes en el buffer
            bw.flush();
            
            // Informamos al usuario que la operación se ha completado con éxito
            System.out.println("Datos escritos correctamente en: " + desti);
        } catch (IOException e) {
            // Si ocurre un error de E/S, lanzamos nuestra excepción personalizada
            throw new MiExcepcion("Error al escribir líneas: " + e.getMessage(), e);
        } finally {
            // Cerramos los flujos en el bloque finally
            // Solo necesitamos cerrar el BufferedWriter, que cerrará automáticamente el FileWriter
            if (bw != null) {
                try {
                    // Intentamos cerrar el flujo
                    bw.close();
                } catch (IOException e) {
                    // Si hay un error al cerrar, lo mostramos pero no interrumpimos el programa
                    System.err.println("Error al cerrar el flujo: " + e.getMessage());
                }
            }
        }
    }
    
    /**
     * Copia el contenido de un fichero a otro línea a línea.
     * Más eficiente que copiar carácter a carácter.
     * 
     * @param origen Ruta del fichero origen
     * @param desti Ruta del fichero destino
     * @throws MiExcepcion Si hay algún error durante la copia
     */
    public static void copiaLine(String origen, String desti) throws MiExcepcion {
        // Declaramos los flujos fuera del try para poder cerrarlos en el finally
        FileReader fr = null;
        BufferedReader br = null;
        FileWriter fw = null;
        BufferedWriter bw = null;
        
        try {
            // Abrimos el flujo de entrada de caracteres desde el fichero origen
            fr = new FileReader(origen);
            
            // Añadimos un buffer al flujo para leer líneas completas
            br = new BufferedReader(fr);
            
            // Abrimos el flujo de salida de caracteres hacia el fichero destino
            fw = new FileWriter(desti);
            
            // Añadimos un buffer al flujo para escribir líneas completas
            bw = new BufferedWriter(fw);
            
            // Variable para almacenar cada línea leída
            String linea;
            
            // Leemos línea a línea hasta el final del fichero (null)
            while ((linea = br.readLine()) != null) {
                // Escribimos la línea en el fichero destino
                bw.write(linea);
                // Añadimos un salto de línea después de cada línea
                bw.newLine();
            }
            
            // Forzamos que se escriban los datos pendientes
            bw.flush();
            
            // Informamos al usuario que la operación se ha completado con éxito
            System.out.println("Fichero copiado correctamente de " + origen + " a " + desti);
        } catch (IOException e) {
            // Si ocurre un error de E/S, lanzamos nuestra excepción personalizada
            throw new MiExcepcion("Error al copiar líneas: " + e.getMessage(), e);
        } finally {
            // Cerramos los flujos en el bloque finally
            if (br != null) {
                try {
                    // Intentamos cerrar el flujo de entrada
                    br.close(); // Esto también cerrará fr
                } catch (IOException e) {
                    // Si hay un error al cerrar, lo mostramos pero no interrumpimos el programa
                    System.err.println("Error al cerrar el flujo de entrada: " + e.getMessage());
                }
            }
            if (bw != null) {
                try {
                    // Intentamos cerrar el flujo de salida
                    bw.close(); // Esto también cerrará fw
                } catch (IOException e) {
                    // Si hay un error al cerrar, lo mostramos pero no interrumpimos el programa
                    System.err.println("Error al cerrar el flujo de salida: " + e.getMessage());
                }
            }
        }
    }
    
    /**
     * Método inútil para medir el tiempo de lectura línea a línea.
     * Solo lee el archivo sin hacer nada con los datos, para pruebas de rendimiento.
     * 
     * @param origen Ruta del fichero a leer
     * @throws MiExcepcion Si hay algún error durante la lectura
     */
    public static void inutil(String origen) throws MiExcepcion {
        // Declaramos los flujos fuera del try para poder cerrarlos en el finally
        FileReader fr = null;
        BufferedReader br = null;
        
        try {
            // Abrimos el flujo de entrada de caracteres desde el fichero
            fr = new FileReader(origen);
            
            // Añadimos un buffer al flujo para leer líneas completas
            br = new BufferedReader(fr);
            
            // Variable para almacenar cada línea leída
            String linea;
            
            // Leemos línea a línea hasta el final del fichero (null)
            // pero no hacemos nada con las líneas leídas
            // Este bucle es "inútil" porque solo lee sin procesar los datos
            while ((linea = br.readLine()) != null) {
                // No hacemos nada, solo leemos
                // Este método se usa para medir el tiempo de lectura sin procesamiento
            }
        } catch (IOException e) {
            // Si ocurre un error de E/S, lanzamos nuestra excepción personalizada
            throw new MiExcepcion("Error al leer líneas: " + e.getMessage(), e);
        } finally {
            // Cerramos los flujos en el bloque finally
            if (br != null) {
                try {
                    // Intentamos cerrar el flujo
                    br.close(); // Esto también cerrará fr
                } catch (IOException e) {
                    // Si hay un error al cerrar, lo mostramos pero no interrumpimos el programa
                    System.err.println("Error al cerrar el flujo: " + e.getMessage());
                }
            }
        }
    }
}
```

### Ejercicio 4: Herramientas_DataStream

**Descripción**: Los DataStream permiten escribir y leer tipos de datos primitivos de Java de manera portable entre diferentes plataformas. Esta clase proporciona métodos para escribir y leer arrays de números en formato binario, lo que es útil para almacenar datos numéricos de manera eficiente.

```java
package com.example.streams; // Define el paquete donde se encuentra la clase

import java.io.DataInputStream; // Para leer tipos primitivos de un flujo de entrada
import java.io.DataOutputStream; // Para escribir tipos primitivos en un flujo de salida
import java.io.FileInputStream; // Para leer bytes de un archivo
import java.io.FileOutputStream; // Para escribir bytes en un archivo
import java.io.IOException; // Para manejar excepciones de E/S

/**
 * Clase de utilidad para trabajar con flujos de datos (data streams).
 * Esta clase es abstracta porque solo contiene métodos estáticos y no se instanciará.
 */
public abstract class Herramientas_DataStream {
    
    /**
     * Escribe un array de doubles en un fichero binario.
     * Útil para almacenar datos numéricos de manera eficiente y portable.
     * 
     * @param desti Ruta del fichero destino
     * @param datos Array de doubles con los datos a escribir
     * @throws MiExcepcion Si hay algún error durante la escritura
     */
    public static void escribeDades(String desti, double[] datos) throws MiExcepcion {
        // Declaramos los flujos fuera del try para poder cerrarlos en el finally
        FileOutputStream fos = null;
        DataOutputStream dos = null;
        
        try {
            // Abrimos el flujo de salida hacia el fichero
            fos = new FileOutputStream(desti);
            
            // Añadimos un DataOutputStream para escribir tipos primitivos
            // DataOutputStream permite escribir tipos primitivos de Java en formato binario
            dos = new DataOutputStream(fos);
            
            // Primero escribimos la longitud del array
            // Esto nos permitirá saber cuántos elementos leer después
            dos.writeInt(datos.length);
            
            // Luego escribimos cada elemento del array
            for (double dato : datos) {
                // writeDouble escribe un double en formato binario (8 bytes)
                dos.writeDouble(dato);
            }
            
            // Forzamos que se escriban los datos pendientes
            dos.flush();
            
            // Informamos al usuario que la operación se ha completado con éxito
            System.out.println("Datos escritos correctamente en: " + desti);
        } catch (IOException e) {
            // Si ocurre un error de E/S, lanzamos nuestra excepción personalizada
            throw new MiExcepcion("Error al escribir datos: " + e.getMessage(), e);
        } finally {
            // Cerramos los flujos en el bloque finally
            // Solo necesitamos cerrar el DataOutputStream, que cerrará automáticamente el FileOutputStream
            if (dos != null) {
                try {
                    // Intentamos cerrar el flujo
                    dos.close();
                } catch (IOException e) {
                    // Si hay un error al cerrar, lo mostramos pero no interrumpimos el programa
                    System.err.println("Error al cerrar el flujo: " + e.getMessage());
                }
            }
        }
    }
    
    /**
     * Lee un array de doubles desde un fichero binario.
     * Debe leer en el mismo orden y formato en que se escribió.
     * 
     * @param origen Ruta del fichero origen
     * @return Array de doubles con los datos leídos
     * @throws MiExcepcion Si hay algún error durante la lectura
     */
    public static double[] leeDades(String origen) throws MiExcepcion {
        // Declaramos los flujos fuera del try para poder cerrarlos en el finally
        FileInputStream fis = null;
        DataInputStream dis = null;
        
        try {
            // Abrimos el flujo de entrada desde el fichero
            fis = new FileInputStream(origen);
            
            // Añadimos un DataInputStream para leer tipos primitivos
            // DataInputStream permite leer tipos primitivos de Java en formato binario
            dis = new DataInputStream(fis);
            
            // Primero leemos la longitud del array
            // Debe ser lo primero que se escribió en el archivo
            int longitud = dis.readInt();
            
            // Creamos un array con esa longitud
            double[] datos = new double[longitud];
            
            // Leemos cada elemento del array
            for (int i = 0; i < longitud; i++) {
                // readDouble lee un double en formato binario (8 bytes)
                datos[i] = dis.readDouble();
            }
            
            // Informamos al usuario que la operación se ha completado con éxito
            System.out.println("Datos leídos correctamente desde: " + origen);
            return datos;
        } catch (IOException e) {
            // Si ocurre un error de E/S, lanzamos nuestra excepción personalizada
            throw new MiExcepcion("Error al leer datos: " + e.getMessage(), e);
        } finally {
            // Cerramos los flujos en el bloque finally
            // Solo necesitamos cerrar el DataInputStream, que cerrará automáticamente el FileInputStream
            if (dis != null) {
                try {
                    // Intentamos cerrar el flujo
                    dis.close();
                } catch (IOException e) {
                    // Si hay un error al cerrar, lo mostramos pero no interrumpimos el programa
                    System.err.println("Error al cerrar el flujo: " + e.getMessage());
                }
            }
        }
    }
}
```

### Ejercicio 5: Herramientas_ObjectStream

**Descripción**: Los ObjectStream permiten serializar y deserializar objetos Java completos, lo que es útil para almacenar y recuperar estructuras de datos complejas. Esta clase proporciona métodos para escribir y leer objetos en formato binario, preservando sus relaciones y estado.

```java
package com.example.streams; // Define el paquete donde se encuentra la clase

import java.io.FileInputStream; // Para leer bytes de un archivo
import java.io.FileOutputStream; // Para escribir bytes en un archivo
import java.io.IOException; // Para manejar excepciones de E/S
import java.io.ObjectInputStream; // Para leer objetos de un flujo de entrada
import java.io.ObjectOutputStream; // Para escribir objetos en un flujo de salida
import java.io.Serializable; // Interfaz que deben implementar los objetos serializables

/**
 * Clase de utilidad para trabajar con flujos de objetos (object streams).
 * Esta clase es abstracta porque solo contiene métodos estáticos y no se instanciará.
 */
public abstract class Herramientas_ObjectStream {
    
    /**
     * Escribe un objeto en un fichero binario.
     * El objeto debe implementar la interfaz Serializable.
     * 
     * @param desti Ruta del fichero destino
     * @param objeto Objeto a escribir (debe implementar Serializable)
     * @throws MiExcepcion Si hay algún error durante la escritura
     */
    public static void escribeObjeto(String desti, Object objeto) throws MiExcepcion {
        // Declaramos los flujos fuera del try para poder cerrarlos en el finally
        FileOutputStream fos = null;
        ObjectOutputStream oos = null;
        
        try {
            // Verificamos que el objeto no sea nulo
            if (objeto == null) {
                throw new MiExcepcion("No se puede escribir un objeto nulo");
            }
            
            // Verificamos que el objeto sea serializable
            // instanceof comprueba si el objeto implementa la interfaz Serializable
            if (!(objeto instanceof Serializable)) {
                throw new MiExcepcion("El objeto debe implementar Serializable");
            }
            
            // Abrimos el flujo de salida hacia el fichero
            fos = new FileOutputStream(desti);
            
            // Añadimos un ObjectOutputStream para escribir objetos
            // ObjectOutputStream permite serializar objetos Java completos
            oos = new ObjectOutputStream(fos);
            
            // Escribimos el objeto
            // writeObject serializa el objeto y lo escribe en el flujo
            oos.writeObject(objeto);
            
            // Forzamos que se escriban los datos pendientes
            oos.flush();
            
            // Informamos al usuario que la operación se ha completado con éxito
            System.out.println("Objeto escrito correctamente en: " + desti);
        } catch (IOException e) {
            // Si ocurre un error de E/S, lanzamos nuestra excepción personalizada
            throw new MiExcepcion("Error al escribir objeto: " + e.getMessage(), e);
        } finally {
            // Cerramos los flujos en el bloque finally
            // Solo necesitamos cerrar el ObjectOutputStream, que cerrará automáticamente el FileOutputStream
            if (oos != null) {
                try {
                    // Intentamos cerrar el flujo
                    oos.close();
                } catch (IOException e) {
                    // Si hay un error al cerrar, lo mostramos pero no interrumpimos el programa
                    System.err.println("Error al cerrar el flujo: " + e.getMessage());
                }
            }
        }
    }
    
    /**
     * Lee un objeto desde un fichero binario.
     * Es responsabilidad del llamante hacer el casting al tipo correcto.
     * 
     * @param origen Ruta del fichero origen
     * @return Objeto leído
     * @throws MiExcepcion Si hay algún error durante la lectura
     */
    public static Object leeObjeto(String origen) throws MiExcepcion {
        // Declaramos los flujos fuera del try para poder cerrarlos en el finally
        FileInputStream fis = null;
        ObjectInputStream ois = null;
        
        try {
            // Abrimos el flujo de entrada desde el fichero
            fis = new FileInputStream(origen);
            
            // Añadimos un ObjectInputStream para leer objetos
            // ObjectInputStream permite deserializar objetos Java completos
            ois = new ObjectInputStream(fis);
            
            // Leemos el objeto
            // readObject deserializa el objeto desde el flujo
            Object objeto = ois.readObject();
            
            // Informamos al usuario que la operación se ha completado con éxito
            System.out.println("Objeto leído correctamente desde: " + origen);
            return objeto;
        } catch (IOException | ClassNotFoundException e) {
            // Capturamos tanto IOException como ClassNotFoundException
            // ClassNotFoundException ocurre si la clase del objeto no se encuentra
            throw new MiExcepcion("Error al leer objeto: " + e.getMessage(), e);
        } finally {
            // Cerramos los flujos en el bloque finally
            // Solo necesitamos cerrar el ObjectInputStream, que cerrará automáticamente el FileInputStream
            if (ois != null) {
                try {
                    // Intentamos cerrar el flujo
                    ois.close();
                } catch (IOException e) {
                    // Si hay un error al cerrar, lo mostramos pero no interrumpimos el programa
                    System.err.println("Error al cerrar el flujo: " + e.getMessage());
                }
            }
        }
    }
}
```

### Clase Datos (para el ejercicio 5)

**Descripción**: Esta clase representa un objeto simple con atributos numéricos y alfanuméricos, que se utilizará para probar la serialización y deserialización de objetos. Implementa Serializable para poder ser guardada y recuperada mediante ObjectStream.

```java
package com.example.streams; // Define el paquete donde se encuentra la clase

import java.io.Serializable; // Interfaz que deben implementar los objetos serializables

/**
 * Clase para representar datos simples.
 * Implementa Serializable para poder ser guardada en un ObjectStream.
 */
public class Datos implements Serializable {
    
    // Necesario para la serialización
    // Identifica la versión de la clase para la serialización
    // Si cambia la estructura de la clase, este valor debería cambiar
    private static final long serialVersionUID = 1L;
    
    // Atributos
    private int numerico; // Valor numérico
    private String alfanumerico; // Valor alfanumérico
    
    /**
     * Constructor con parámetros.
     * Inicializa los atributos con los valores proporcionados.
     * 
     * @param numerico Valor numérico
     * @param alfanumerico Valor alfanumérico
     */
    public Datos(int numerico, String alfanumerico) {
        this.numerico = numerico;
        this.alfanumerico = alfanumerico;
    }
    
    // Getters y setters
    
    /**
     * Obtiene el valor numérico.
     * @return Valor numérico
     */
    public int getNumerico() {
        return numerico;
    }
    
    /**
     * Establece el valor numérico.
     * @param numerico Nuevo valor numérico
     */
    public void setNumerico(int numerico) {
        this.numerico = numerico;
    }
    
    /**
     * Obtiene el valor alfanumérico.
     * @return Valor alfanumérico
     */
    public String getAlfanumerico() {
        return alfanumerico;
    }
    
    /**
     * Establece el valor alfanumérico.
     * @param alfanumerico Nuevo valor alfanumérico
     */
    public void setAlfanumerico(String alfanumerico) {
        this.alfanumerico = alfanumerico;
    }
    
    // Métodos equals, hashCode y toString
    
    /**
     * Compara este objeto con otro para determinar si son iguales.
     * Dos objetos Datos son iguales si tienen los mismos valores numérico y alfanumérico.
     * 
     * @param obj Objeto a comparar
     * @return true si son iguales, false en caso contrario
     */
    @Override
    public boolean equals(Object obj) {
        // Si es el mismo objeto, son iguales
        if (this == obj) return true;
        // Si el objeto es nulo o de otra clase, no son iguales
        if (obj == null || getClass() != obj.getClass()) return false;
        
        // Convertimos el objeto a Datos
        Datos datos = (Datos) obj;
        
        // Comparamos los atributos
        if (numerico != datos.numerico) return false;
        // Para String, usamos equals (puede ser null)
        return alfanumerico != null ? alfanumerico.equals(datos.alfanumerico) : datos.alfanumerico == null;
    }
    
    /**
     * Calcula el código hash del objeto.
     * Objetos iguales deben tener el mismo código hash.
     * 
     * @return Código hash
     */
    @Override
    public int hashCode() {
        // Usamos el valor numérico como base
        int result = numerico;
        // Combinamos con el hash del valor alfanumérico
        result = 31 * result + (alfanumerico != null ? alfanumerico.hashCode() : 0);
        return result;
    }
    
    /**
     * Devuelve una representación en texto del objeto.
     * Útil para depuración y logging.
     * 
     * @return Representación en texto
     */
    @Override
    public String toString() {
        return "Datos{" +
                "numerico=" + numerico +
                ", alfanumerico='" + alfanumerico + '\'' +
                '}';
    }
}
```

### Clase DatosComplejos (para el ejercicio 5)

**Descripción**: Esta clase representa un objeto complejo que contiene otro objeto, lo que permite probar la serialización y deserialización de estructuras de datos anidadas. También implementa Serializable para poder ser guardada y recuperada mediante ObjectStream.

```java
package com.example.streams; // Define el paquete donde se encuentra la clase

import java.io.Serializable; // Interfaz que deben implementar los objetos serializables

/**
 * Clase para representar datos complejos que contienen otros objetos.
 * Implementa Serializable para poder ser guardada en un ObjectStream.
 * Demuestra la serialización de objetos anidados.
 */
public class DatosComplejos implements Serializable {
    
    // Necesario para la serialización
    // Identifica la versión de la clase para la serialización
    private static final long serialVersionUID = 1L;
    
    // Atributos
    private String identificador; // Identificador del objeto
    private Datos datos; // Objeto Datos contenido (también debe ser serializable)
    
    /**
     * Constructor con parámetros.
     * Inicializa los atributos con los valores proporcionados.
     * 
     * @param identificador Identificador del objeto
     * @param datos Objeto Datos contenido
     */
    public DatosComplejos(String identificador, Datos datos) {
        this.identificador = identificador;
        this.datos = datos;
    }
    
    // Getters y setters
    
    /**
     * Obtiene el identificador.
     * @return Identificador
     */
    public String getIdentificador() {
        return identificador;
    }
    
    /**
     * Establece el identificador.
     * @param identificador Nuevo identificador
     */
    public void setIdentificador(String identificador) {
        this.identificador = identificador;
    }
    
    /**
     * Obtiene el objeto Datos contenido.
     * @return Objeto Datos
     */
    public Datos getDatos() {
        return datos;
    }
    
    /**
     * Establece el objeto Datos contenido.
     * @param datos Nuevo objeto Datos
     */
    public void setDatos(Datos datos) {
        this.datos = datos;
    }
    
    // Métodos equals, hashCode y toString
    
    /**
     * Compara este objeto con otro para determinar si son iguales.
     * Dos objetos DatosComplejos son iguales si tienen el mismo identificador y datos.
     * 
     * @param obj Objeto a comparar
     * @return true si son iguales, false en caso contrario
     */
    @Override
    public boolean equals(Object obj) {
        // Si es el mismo objeto, son iguales
        if (this == obj) return true;
        // Si el objeto es nulo o de otra clase, no son iguales
        if (obj == null || getClass() != obj.getClass()) return false;
        
        // Convertimos el objeto a DatosComplejos
        DatosComplejos that = (DatosComplejos) obj;
        
        // Comparamos los atributos
        // Para String y objetos, usamos equals (pueden ser null)
        if (identificador != null ? !identificador.equals(that.identificador) : that.identificador != null)
            return false;
        return datos != null ? datos.equals(that.datos) : that.datos == null;
    }
    
    /**
     * Calcula el código hash del objeto.
     * Objetos iguales deben tener el mismo código hash.
     * 
     * @return Código hash
     */
    @Override
    public int hashCode() {
        // Usamos el hash del identificador como base
        int result = identificador != null ? identificador.hashCode() : 0;
        // Combinamos con el hash de los datos
        result = 31 * result + (datos != null ? datos.hashCode() : 0);
        return result;
    }
    
    /**
     * Devuelve una representación en texto del objeto.
     * Útil para depuración y logging.
     * 
     * @return Representación en texto
     */
    @Override
    public String toString() {
        return "DatosComplejos{" +
                "identificador='" + identificador + '\'' +
                ", datos=" + datos +
                '}';
    }
}
```

### Clase Cronometro (para medir tiempos)

**Descripción**: Esta clase proporciona funcionalidad para medir el tiempo de ejecución de operaciones, lo que es útil para comparar el rendimiento de diferentes enfoques de lectura/escritura de archivos.

```java
package com.example.streams; // Define el paquete donde se encuentra la clase

/**
 * Clase para medir tiempos de ejecución.
 * Útil para comparar el rendimiento de diferentes métodos.
 */
public class Cronometro {
    
    // Atributos
    private long inicio; // Tiempo de inicio en milisegundos
    private long fin; // Tiempo de fin en milisegundos
    private boolean enMarcha; // Indica si el cronómetro está en marcha
    
    /**
     * Constructor por defecto.
     * Inicializa el cronómetro pero no lo pone en marcha.
     */
    public Cronometro() {
        inicio = 0;
        fin = 0;
        enMarcha = false;
    }
    
    /**
     * Inicia el cronómetro.
     * Guarda el tiempo actual como tiempo de inicio.
     */
    public void iniciar() {
        // System.currentTimeMillis() devuelve el tiempo actual en milisegundos
        inicio = System.currentTimeMillis();
        enMarcha = true;
    }
    
    /**
     * Detiene el cronómetro.
     * Guarda el tiempo actual como tiempo de fin.
     */
    public void parar() {
        fin = System.currentTimeMillis();
        enMarcha = false;
    }
    
    /**
     * Reinicia el cronómetro.
     * Pone a cero los tiempos de inicio y fin.
     */
    public void reiniciar() {
        inicio = 0;
        fin = 0;
        enMarcha = false;
    }
    
    /**
     * Devuelve el tiempo transcurrido en milisegundos.
     * Si el cronómetro está en marcha, calcula el tiempo hasta ahora.
     * 
     * @return Tiempo en milisegundos
     */
    public long getTiempoMilisegundos() {
        if (enMarcha) {
            // Si está en marcha, calculamos el tiempo hasta ahora
            return System.currentTimeMillis() - inicio;
        } else {
            // Si está parado, devolvemos el tiempo entre inicio y fin
            return fin - inicio;
        }
    }
    
    /**
     * Devuelve el tiempo transcurrido en segundos.
     * Convierte el tiempo de milisegundos a segundos.
     * 
     * @return Tiempo en segundos
     */
    public double getTiempoSegundos() {
        // Dividimos por 1000.0 para convertir a segundos con decimales
        return getTiempoMilisegundos() / 1000.0;
    }
    
    /**
     * Devuelve una representación en texto del tiempo transcurrido.
     * Formato: "segundos,milisegundos segundos"
     * 
     * @return String con el tiempo formateado
     */
    @Override
    public String toString() {
        // Obtenemos el tiempo en milisegundos
        long tiempo = getTiempoMilisegundos();
        // Calculamos los segundos (división entera)
        long segundos = tiempo / 1000;
        // Calculamos los milisegundos restantes (módulo)
        long milisegundos = tiempo % 1000;
        
        // Devolvemos el tiempo formateado
        return segundos + "," + milisegundos + " segundos";
    }
}
```

### Clase MiExcepcion (excepción personalizada)

**Descripción**: Esta clase representa una excepción personalizada para la aplicación, que permite encapsular y propagar errores específicos de manera controlada.

```java
package com.example.streams; // Define el paquete donde se encuentra la clase

/**
 * Excepción personalizada para la aplicación.
 * Extiende Exception para ser una excepción comprobada (checked).
 */
public class MiExcepcion extends Exception {
    
    /**
     * Constructor sin parámetros.
     * Llama al constructor de la clase padre.
     */
    public MiExcepcion() {
        super();
    }
    
    /**
     * Constructor con mensaje.
     * 
     * @param mensaje Mensaje descriptivo del error
     */
    public MiExcepcion(String mensaje) {
        super(mensaje);
    }
    
    /**
     * Constructor con mensaje y causa.
     * Útil para encapsular excepciones de bajo nivel.
     * 
     * @param mensaje Mensaje descriptivo del error
     * @param causa Excepción original que causó el error
     */
    public MiExcepcion(String mensaje, Throwable causa) {
        super(mensaje, causa);
    }
}
```

### Clase PruebasStreams (con main)

**Descripción**: Esta clase contiene el método main y métodos para probar todas las funcionalidades implementadas en las clases anteriores. Aquí se realizan pruebas de lectura, escritura y copia de archivos utilizando diferentes tipos de streams.

```java
package com.example.main; // Define el paquete donde se encuentra la clase principal

import com.example.streams.*; // Importa todas las clases del paquete streams
import java.util.ArrayList; // Para trabajar con listas dinámicas
import java.util.Arrays; // Para trabajar con arrays

/**
 * Clase principal para probar las funcionalidades de streams.
 * Contiene el método main y métodos para probar cada tipo de stream.
 */
public class PruebasStreams {
    
    /**
     * Método principal que ejecuta las pruebas.
     * 
     * @param args Argumentos de línea de comandos (no utilizados)
     */
    public static void main(String[] args) {
        try {
            // Definimos rutas para los archivos de prueba
            String rutaBase = "/tmp/pruebas_streams/";
            String rutaHimno = rutaBase + "himno.txt";
            String rutaTirant = rutaBase + "tirant.txt";
            
            // Creamos el directorio base si no existe
            new java.io.File(rutaBase).mkdirs();
            
            // Probamos los diferentes tipos de streams
            probarByteStream(rutaBase);
            probarCharacterStream(rutaBase);
            probarBufferedStream(rutaBase);
            probarDataStream(rutaBase);
            probarObjectStream(rutaBase);
            
            // Comparamos rendimiento de diferentes métodos de lectura
            compararRendimiento(rutaTirant);
            
        } catch (MiExcepcion e) {
            // Capturamos y mostramos cualquier excepción personalizada
            System.err.println("Error: " + e.getMessage());
            if (e.getCause() != null) {
                System.err.println("Causa: " + e.getCause().getMessage());
            }
            e.printStackTrace();
        }
    }
    
    /**
     * Prueba las funcionalidades de ByteStream.
     * 
     * @param rutaBase Directorio base para los archivos de prueba
     * @throws MiExcepcion Si hay algún error durante las pruebas
     */
    private static void probarByteStream(String rutaBase) throws MiExcepcion {
        System.out.println("\n=== Pruebas de ByteStream ===");
        
        // Definimos rutas para los archivos de prueba
        String rutaOriginal = rutaBase + "original_bytes.txt";
        String rutaCopia = rutaBase + "copia_bytes.txt";
        
        // Creamos un texto de prueba
        String texto = "Este es un texto de prueba para ByteStream.\nContiene varias líneas.\nFin del texto.";
        
        // Convertimos el texto a bytes
        byte[] bytes = texto.getBytes();
        
        // Escribimos los bytes en un archivo
        System.out.println("Escribiendo bytes en " + rutaOriginal);
        Herramientas_ByteStream.escribeByte(rutaOriginal, bytes);
        
        // Leemos los bytes del archivo
        System.out.println("Leyendo bytes de " + rutaOriginal);
        byte[] bytesLeidos = Herramientas_ByteStream.tornaBytes(rutaOriginal);
        
        // Convertimos los bytes leídos a texto y lo mostramos
        String textoLeido = new String(bytesLeidos);
        System.out.println("Texto leído: \n" + textoLeido);
        
        // Copiamos el archivo a otro
        System.out.println("Copiando bytes de " + rutaOriginal + " a " + rutaCopia);
        Herramientas_ByteStream.copiaBytes(rutaOriginal, rutaCopia);
    }
    
    /**
     * Prueba las funcionalidades de CharacterStream.
     * 
     * @param rutaBase Directorio base para los archivos de prueba
     * @throws MiExcepcion Si hay algún error durante las pruebas
     */
    private static void probarCharacterStream(String rutaBase) throws MiExcepcion {
        System.out.println("\n=== Pruebas de CharacterStream ===");
        
        // Definimos rutas para los archivos de prueba
        String rutaOriginal = rutaBase + "original_chars.txt";
        String rutaCopia = rutaBase + "copia_chars.txt";
        
        // Creamos un texto de prueba con caracteres especiales
        String texto = "Este es un texto de prueba para CharacterStream.\nContiene caracteres especiales: áéíóúñÁÉÍÓÚÑ.\nFin del texto.";
        
        // Escribimos el texto en un archivo
        System.out.println("Escribiendo caracteres en " + rutaOriginal);
        Herramientas_CharacterStream.escribeCharacters(rutaOriginal, texto);
        
        // Mostramos el contenido del archivo
        System.out.println("Mostrando caracteres de " + rutaOriginal);
        Herramientas_CharacterStream.muestraCharacters(rutaOriginal);
        
        // Copiamos el archivo a otro
        System.out.println("Copiando caracteres de " + rutaOriginal + " a " + rutaCopia);
        Herramientas_CharacterStream.copiaCharacters(rutaOriginal, rutaCopia);
    }
    
    /**
     * Prueba las funcionalidades de BufferedStream.
     * 
     * @param rutaBase Directorio base para los archivos de prueba
     * @throws MiExcepcion Si hay algún error durante las pruebas
     */
    private static void probarBufferedStream(String rutaBase) throws MiExcepcion {
        System.out.println("\n=== Pruebas de BufferedStream ===");
        
        // Definimos rutas para los archivos de prueba
        String rutaOriginal = rutaBase + "original_lines.txt";
        String rutaCopia = rutaBase + "copia_lines.txt";
        
        // Creamos un array de líneas de prueba
        String[] lineas = {
            "Primera línea de prueba para BufferedStream.",
            "Segunda línea con caracteres especiales: áéíóúñÁÉÍÓÚÑ.",
            "Tercera y última línea."
        };
        
        // Escribimos las líneas en un archivo
        System.out.println("Escribiendo líneas en " + rutaOriginal);
        Herramientas_BufferedStream.escribeLine(rutaOriginal, lineas);
        
        // Leemos las líneas del archivo
        System.out.println("Leyendo líneas de " + rutaOriginal);
        ArrayList<String> lineasLeidas = Herramientas_BufferedStream.tornaLine(rutaOriginal);
        
        // Mostramos las líneas leídas
        System.out.println("Líneas leídas:");
        for (String linea : lineasLeidas) {
            System.out.println("  " + linea);
        }
        
        // Copiamos el archivo a otro
        System.out.println("Copiando líneas de " + rutaOriginal + " a " + rutaCopia);
        Herramientas_BufferedStream.copiaLine(rutaOriginal, rutaCopia);
    }
    
    /**
     * Prueba las funcionalidades de DataStream.
     * 
     * @param rutaBase Directorio base para los archivos de prueba
     * @throws MiExcepcion Si hay algún error durante las pruebas
     */
    private static void probarDataStream(String rutaBase) throws MiExcepcion {
        System.out.println("\n=== Pruebas de DataStream ===");
        
        // Definimos ruta para el archivo de prueba
        String rutaDatos = rutaBase + "datos.bin";
        
        // Creamos un array de doubles de prueba
        double[] datos = {1.1, 2.2, 3.3, 4.4, 5.5};
        
        // Escribimos los datos en un archivo
        System.out.println("Escribiendo datos en " + rutaDatos);
        Herramientas_DataStream.escribeDades(rutaDatos, datos);
        
        // Leemos los datos del archivo
        System.out.println("Leyendo datos de " + rutaDatos);
        double[] datosLeidos = Herramientas_DataStream.leeDades(rutaDatos);
        
        // Mostramos los datos leídos
        System.out.println("Datos leídos: " + Arrays.toString(datosLeidos));
    }
    
    /**
     * Prueba las funcionalidades de ObjectStream.
     * 
     * @param rutaBase Directorio base para los archivos de prueba
     * @throws MiExcepcion Si hay algún error durante las pruebas
     */
    private static void probarObjectStream(String rutaBase) throws MiExcepcion {
        System.out.println("\n=== Pruebas de ObjectStream ===");
        
        // Definimos rutas para los archivos de prueba
        String rutaDatos = rutaBase + "objeto_datos.bin";
        String rutaDatosComplejos = rutaBase + "objeto_datos_complejos.bin";
        
        // Creamos objetos de prueba
        Datos datos = new Datos(42, "Texto de prueba");
        DatosComplejos datosComplejos = new DatosComplejos("ID-123", datos);
        
        // Escribimos el objeto Datos en un archivo
        System.out.println("Escribiendo objeto Datos en " + rutaDatos);
        Herramientas_ObjectStream.escribeObjeto(rutaDatos, datos);
        
        // Leemos el objeto Datos del archivo
        System.out.println("Leyendo objeto Datos de " + rutaDatos);
        Datos datosLeidos = (Datos) Herramientas_ObjectStream.leeObjeto(rutaDatos);
        
        // Mostramos el objeto leído
        System.out.println("Objeto Datos leído: " + datosLeidos);
        
        // Escribimos el objeto DatosComplejos en un archivo
        System.out.println("Escribiendo objeto DatosComplejos en " + rutaDatosComplejos);
        Herramientas_ObjectStream.escribeObjeto(rutaDatosComplejos, datosComplejos);
        
        // Leemos el objeto DatosComplejos del archivo
        System.out.println("Leyendo objeto DatosComplejos de " + rutaDatosComplejos);
        DatosComplejos datosComplejosLeidos = (DatosComplejos) Herramientas_ObjectStream.leeObjeto(rutaDatosComplejos);
        
        // Mostramos el objeto leído
        System.out.println("Objeto DatosComplejos leído: " + datosComplejosLeidos);
    }
    
    /**
     * Compara el rendimiento de diferentes métodos de lectura.
     * 
     * @param rutaArchivo Ruta del archivo a leer
     * @throws MiExcepcion Si hay algún error durante las pruebas
     */
    private static void compararRendimiento(String rutaArchivo) throws MiExcepcion {
        System.out.println("\n=== Comparación de Rendimiento ===");
        
        // Creamos un cronómetro
        Cronometro crono = new Cronometro();
        
        // Medimos el tiempo de lectura carácter a carácter
        System.out.println("Midiendo tiempo de lectura carácter a carácter...");
        crono.iniciar();
        Herramientas_CharacterStream.inutil(rutaArchivo);
        crono.parar();
        System.out.println("Tiempo de lectura carácter a carácter: " + crono);
        
        // Reiniciamos el cronómetro
        crono.reiniciar();
        
        // Medimos el tiempo de lectura línea a línea
        System.out.println("Midiendo tiempo de lectura línea a línea...");
        crono.iniciar();
        Herramientas_BufferedStream.inutil(rutaArchivo);
        crono.parar();
        System.out.println("Tiempo de lectura línea a línea: " + crono);
        
        // Mostramos conclusión
        System.out.println("Conclusión: La lectura línea a línea con buffer es generalmente más eficiente que la lectura carácter a carácter.");
    }
}
```
