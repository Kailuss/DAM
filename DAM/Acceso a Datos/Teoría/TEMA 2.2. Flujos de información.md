---
number headings: first-level 0, max 3, _.1.,  skip ^skipped
obsidianUIMode: preview
banner: "![[ad.jpg]]"
banner_y: 0.2
---

# **TEMA 2.2.** Flujos de información

## 1. Persistencia de datos

Persistencia de datos: cómo mantener los datos entre ejecución y ejecución de la aplicación.  

Todo lo que habíamos hecho hasta ahora trabajaba con la RAM del ordenador, por lo tanto, cuando el programa terminaba, se perdía la información que había gestionado.  

Básicamente, hay dos posibilidades para implementar la persistencia:  

- **Archivos: en Java se tratan como flujos,** `Streams`. Van muy bien para aplicaciones pequeñas: No montaremos un servidor de bases de datos para guardar solo los datos de configuración de la aplicación, por ejemplo.  

- **Bases de datos: Cuando la cantidad y estructura de los datos es más compleja, un archivo o conjunto de archivos no nos bastan, entonces sí que vale la pena utilizar un sistema gestor de bases de datos.**  

Vamos a ver los streams.  

## 2. Flujo (Stream)  

Un flujo de datos es una secuencia de datos. Un programa utilizará un flujo de entrada, `input stream`, para leer datos de un origen, y un flujo de salida, `output stream`, para escribir datos a un destino.  

Las operaciones tanto con uno como con el otro se realizan con un elemento a la vez.  

El origen o el destino de los datos pueden ser de diversos tipos: archivos de disco, dispositivos, otros programas, arrays de memoria, ... cualquier cosa que pueda mantener, generar o consumir datos.  

Los flujos pueden manejar cualquier tipo de datos, desde bytes, hasta objetos pasando por tipos primitivos.  

### 2.1. **Flujos de bytes**

Nuestros programas utilizarán los flujos de bytes cuando queramos acceder a recursos a bajo nivel. No los deberíamos utilizar a menos que sea imprescindible, ya que hay clases mucho más especializadas.  

Los veremos porque son la base, la superclase, de todos los demás flujos. Utilizaremos **`FileInputStream`** para leer un archivo. El constructor espera la ruta del archivo como parámetro:  

```java
String origen="/home/alumne/cara.jpg";  
FileInputStream in = new FileInputStream(origen);  
```  

Todas las operaciones con streams pueden lanzar excepciones, por tanto irán dentro de un bloque `try-catch` o dentro de un método que las propague.  

Para leer utilizaremos `read`. Devuelve un `int` y no un `byte` porque así puede devolver el valor -1 para indicar que ha terminado de leer el archivo. Por tanto, para leer todos los bytes del archivo:  

```java
while ((c = in.read()) != -1){  
    byte b=(byte)c; //casteo a byte.  
}  
```  

Los streams siempre se deben cerrar, mejor dentro de un bloque `finally` para asegurarnos. Dejar un recurso abierto, como un archivo, puede provocar problemas, por ejemplo, para extraer un USB:  

```java
} finally {  
    if (in != null)  
        in.close();  
}  
```  

Para escribir un flujo de bytes podemos utilizar **`FileOutputStream`. El constructor también espera un `String` con la ruta del archivo donde debe escribir los datos.  

El método a utilizar es `write`. Tiene como parámetro un `int`.  

```java
out.write(b);  
```  

Este método está sobrecargado, por ejemplo, con un array de bytes como parámetro.  

Las clases que definen los flujos de bytes son abstractas, `InputStream` y `OutputStream`. Algunas subclases son:  

- `FileInputStream` y `FileOutputStream`: Para trabajar con archivos.  
- `ByteArrayInputStream` y `ByteArrayOutputStream`: Para trabajar con arrays como fuente o destino de datos.  
- `AudioInputStream`: Especializada en fuentes de audio.  
- `ObjectInputStream` y `ObjectOutputStream`: Para trabajar con objetos.  

### 2.2. **Paréntesis: try-with-resources**

Esta variante del `try` declara recursos, objetos que el programa debe cerrar cuando ya no los necesite más. Se asegura que los objetos declarados se cierren, tanto si el bloque de código del `try` lanza excepciones como si no.  

Se pueden utilizar como recursos cualquier objeto que implemente la interfaz `AutoCloseable`. Disponible a partir de Java 7.  

```java
try (FileInputStream in = new FileInputStream(origen)) {  
    int c;  
    while ((c = in.read()) != -1) {  
        System.out.print((byte)c);  
    }  
}  
```  

Evidentemente, pueden haber tantos bloques `catch` como nos hagan falta. Antes de ejecutarse, sin embargo, se cerrarán los recursos declarados en el `try`.  

**Si no capturamos las excepciones, las tendremos que propagar.**  

### 2.3. **Flujos de caracteres**

Java almacena los caracteres en Unicode. Los flujos de caracteres automáticamente los transforman a y desde el conjunto de caracteres locales del sistema.  

Todas las clases que implementan flujos de caracteres descienden de `Reader` y `Writer`.  

Para leer archivos de caracteres disponemos de `FileReader` y `FileWriter`. Los constructores aceptan, entre otros, la ruta del archivo que leerán o donde escribirán.  

El método `read` de **`FileReader`** lee un carácter del stream. Si no hay ninguno disponible, bloquea el programa. Lo devuelve en formato `int`, por tanto, debemos hacer el casteo a `char`.  

Podemos comprobar el estado del flujo con el método `ready`.  

```java
while (in.ready()) {  
    char d = (char) in.read();  
}  
```  

El método `write` de `FileWriter` escribe un carácter al archivo.  

```java
out.write('a');  
```  

Está sobrecargado con versiones que reciben por parámetro `String`.  

```java
out.write("Hola");  
```  

O arrays de `char`:  

```java
char[] caracteres={'H','o','l','a'};  
out.write(caracteres);  
```  

Tanto `read` como `write` utilizan `int` para manejar los datos leídos o escritos en el archivo. 

### 2.4. **Flujos con buffer**

Los flujos que hemos visto hasta ahora no disponen de ningún buffer. Esto significa que cada petición de lectura o escritura se envía directamente al SO, con la consiguiente pérdida de eficiencia, ya que normalmente implican operaciones de disco o red que son muy costosas en tiempo.  

Para mejorar el rendimiento, Java implementa flujos con buffer, con una memoria intermedia.  

Durante la lectura, esta memoria intermedia se llena de golpe y el stream accede a los datos desde la memoria; al estar vacía, se vuelve a llenar.  

Durante la escritura, los datos se escriben en esta memoria y al estar llena, se envían al disco o a la red.  

Disponemos de 4 flujos con buffer: **`BufferedInputStream`** y **`BufferedOutputStream`** para flujos de bytes, y **`BufferedReader`** y **`BufferedWriter`** para flujos de carácter.  

Para crear un flujo con buffer, en su constructor debemos pasarle un flujo sin buffer.  

```java
BufferedReader inputStream = new BufferedReader(new FileReader("original.txt"));  
BufferedWriter outputStream = new BufferedWriter(new FileWriter("sortida.txt"));  
```  

Para leer, **`BufferedReader`** tiene el método `readLine`. Devuelve un `String`, y cuando se acaban los datos del stream, devuelve `null`.  

```java
while ((línea = in.readLine()) != null) {  
}  
```  

Para escribir, **`BufferedWriter`** tiene el método `write` que recibe un `String`. Si queremos que en el archivo haya un salto de línea detrás de la cadena, después debemos ejecutar el método `newLine`:  

```java
out.write(línea);  
out.newLine();  
```  

Si queremos escribir los datos al disco directamente sin esperar a llenar el buffer, podemos ejecutar el método `flush`.  

```java
outputStream.flush();  
```  

**`BufferedReader`** y **`BufferedWriter`** nos proporcionan operaciones sobre líneas de texto. Para trabajar con archivos de texto son más eficientes que `FileReader` y `FileWriter`.  

### 2.5. **Flujos de datos**

Los flujos de datos soportan valores de tipos de datos primitivos (`boolean`, `char`, `byte`, `short`, `int`, `long`, `float`, y `double`) y `String`. Todos los flujos de datos implementan o bien la interfaz `DataInput` o bien la `DataOutput`.  

Como ejemplo, veremos los dos más utilizados, `DataInputStream` y `DataOutputStream`. La primera proporciona métodos para leer datos según el tipo `readBoolean`, `readChar`, `readInt`, `readUTF` (para `String`), ... y la segunda para escribir datos según el tipo `writeBoolean`, ...  

Para crear estos flujos:  

```java
DataOutputStream out;  
DataInputStream in;  
out = new DataOutputStream(new BufferedOutputStream(new FileOutputStream(dataFile)));  
in = new DataInputStream(new BufferedInputStream(new FileInputStream(dataFile)));  
```  

Para crearlos, debemos pasarles como argumento un flujo con buffer.  

`DataOutputStream` guarda los datos como una sucesión de bytes. Es decir, los métodos `writeInt`, `writeDouble`... "transforman" estos tipos primitivos a bytes.  

`DataInputStream` lee estos bytes y los transforma a un determinado tipo según el método que hemos utilizado para leerlos. Por ejemplo, `readBoolean` leerá un solo byte, mientras que `readInt` leerá 4.  

Por tanto, **para leer correctamente un archivo, debemos saber en qué orden se han escrito los datos.**  

La única manera que tenemos de saber cuándo termina un archivo es recoger la excepción `EOFException` (End Of File Exception).  

Por ejemplo, si queremos escribir una lista de productos en un archivo, con el nombre, el precio y las unidades que tenemos, lo haríamos de la siguiente manera:  

```java
for (Producto producto : productos) {  
    out.writeDouble(producto.getPrecio());  
    out.writeInt(producto.getUnidades());  
    out.writeUTF(producto.getNombre());  
}  
```  

Para leer este archivo, debemos estar atentos al leer los datos en el mismo orden. Si no lo hacemos, bytes que formaban parte del `double` a lo mejor ahora forman parte de un `int`, etc. y no recuperaremos los datos que hemos guardado. En el mejor de los casos, tendremos otros valores, y en el peor, el programa fallará.  

```java
try {  
    ArrayList<Producto> productos=new ArrayList<>();  
    while (true) {  
        double precio = in.readDouble();  
        int unidades = in.readInt();  
        String nombre = in.readUTF();  
        productos.add(new Producto(nombre, unidades, precio));  
    }  
} catch (EOFException e) {  
}  
```  

### 2.6. **Flujos de objetos**

Los flujos de objetos soportan objetos, es decir, en lugar de guardar en disco un `double`, un `int` y un `String`, podemos guardar directamente un `Producto`.  

**Para poder guardar un objeto en un flujo, su clase debe implementar la interfaz `Serializable`. Se trata de una interfaz marcadora, es decir, sin ningún método, que solo sirve para, utilizando polimorfismo, facilitar la tarea de declarar los métodos de los flujos.**  

Utilizaremos los flujos `ObjectInputStream` y `ObjectOutputStream` para leer y escribir objetos en el flujo.  

```java
ObjectOutputStream out;  
ObjectInputStream in;  
out = new ObjectOutputStream(new BufferedOutputStream(new FileOutputStream(dataFile)));  
in = new ObjectInputStream(new BufferedInputStream(new FileInputStream(dataFile)));  
```  

Para crearlos, necesitamos pasar al constructor un flujo con buffer como argumento.  

Para enviar un objeto al flujo:  

```java
out.writeObject(producto);  
```  

Para recuperar un objeto del flujo:  

```java
Producto recuperado=(Producto) in.readObject();  
```  

Siempre devuelve `Object`, por tanto, debemos hacer el casteo a la clase original del objeto.  

Si el objeto recuperado no es del tipo esperado, se generará una excepción del tipo `ClassNotFoundException`.  

Este flujo no da ninguna señal de haber llegado al final del archivo, EOF. Lo más habitual es poner el `while` que lee a `true` y capturar `EOFException`. Otra posibilidad es guardar algún tipo de metadata, un objeto inicial que indique cuántos hay o situar un objeto al final que podamos reconocer como final de archivo.  

```java
try {  
    ArrayList<Producto> productos=new ArrayList<>();  
    while (true) {  
        Producto recuperado=(Producto) in.readObject();  
        productos.add(recuperado);  
    }  
} catch (EOFException e) {  
}  
```  

#### Escritura y lectura de objetos complejos  

Cuando todos los atributos de un objeto son tipos primitivos, es realmente simple escribir este objeto en un flujo. Pero muchas veces nos encontramos con que un objeto tiene un atributo que es otro objeto. Y este, a su vez, puede contener otro y, por ejemplo, un alumno puede incluir una lista con sus calificaciones.  

En este caso, al recuperar el objeto con `readObject`, también tendremos que recuperar todos estos otros objetos que contiene. Al recuperar el alumno, también tendrá que recuperar la lista con todas sus calificaciones.  

Esto significa que el método `writeObject` debe ser capaz de recorrer toda esta estructura y guardarla de manera que el `readObject` la pueda reconstruir.  

Si dos objetos hacen referencia a otro, por ejemplo, dos alumnos hacen referencia al mismo módulo, al reconstruirlos, se seguirán manteniendo estas referencias, no se crearán dos módulos diferentes.  

Si escribimos dos veces el mismo objeto en el mismo `stream`, estamos guardando el objeto una vez. Lo que repetimos son las referencias, de forma que al volver a recuperar los datos del `stream`, seguiremos teniendo un solo objeto con dos referencias.  

En cambio, si escribimos el mismo objeto en dos flujos diferentes, y recuperamos el objeto de los dos flujos, tendremos dos objetos diferentes.  

Por ejemplo, para guardar en el archivo una lista de productos, podemos hacerlo de la siguiente manera:  

```java
ObjectOutputStream out;  
out = new ObjectOutputStream(new BufferedOutputStream(new FileOutputStream(dataFile)));  
ArrayList<Producto> productos=new ArrayList<>();  
... //Llenamos la lista  
out.writeObject(productos);  
```  

De esta manera, guardamos toda la lista en el archivo. Para recuperarla:  

```java
ObjectInputStream in;  
in = new ObjectInputStream(new BufferedInputStream(new FileInputStream(dataFile)));  
ArrayList<Producto> recuperados=(ArrayList<Producto>) in.readObject();  
```  

De esta manera, tenemos dentro de `recuperados` la lista de productos que habíamos guardado antes.
