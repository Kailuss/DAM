---
number headings: first-level 0, start-at 1, max 2, _.1., auto, contents ^toc, skip ^skipped
obsidianUIMode: preview
banner: "![[../../../../Banners/ad.jpg]]"
banner_y: 0.19
---

# Resumen Tema 2.2. Flujos de información

El tema aborda la **persistencia de datos** en Java, es decir, cómo mantener los datos entre ejecuciones de una aplicación. Se centra en dos enfoques principales: el uso de **archivos** (a través de flujos o *streams*) y las **bases de datos**, que son más adecuadas para aplicaciones con datos complejos.

## 1. Persistencia de datos

- **Persistencia.** Mantener los datos entre ejecuciones de la aplicación.
- **RAM.** Los datos en la memoria RAM se pierden cuando el programa termina.
- **Archivos.** Se utilizan para aplicaciones pequeñas, como guardar configuraciones.
- **Bases de datos.** Se usan cuando la cantidad y estructura de los datos son más complejas.

## 2. Flujo (Stream)

Un **flujo de datos** es una secuencia de datos que se lee o escribe desde/hacia un origen o destino. Los flujos pueden ser de entrada (*input stream*) o de salida (*output stream*), y pueden manejar diferentes tipos de datos, como bytes, caracteres, objetos, etc.

### 2.1. Flujos de bytes

- **Flujos de bytes.** Se utilizan para acceder a recursos a bajo nivel.
- **`FileInputStream`** y **`FileOutputStream`.** Para leer y escribir archivos.

Ejemplo de lectura:

```java
FileInputStream in = new FileInputStream("/home/alumne/cara.jpg");
while ((c = in.read()) != -1) {
    byte b = (byte)c;
}
```

Ejemplo de escritura:

```java
FileOutputStream out = new FileOutputStream("destino.jpg");
out.write(b);
```

Siempre se deben cerrar los flujos, preferiblemente en un bloque `finally`.

### 2.2. Paréntesis: try-with-resources

- **`try-with-resources`.** Asegura que los recursos se cierren automáticamente.

Ejemplo:

```java
try (FileInputStream in = new FileInputStream(origen)) {
    int c;
    while ((c = in.read()) != -1) {
        System.out.print((byte)c);
    }
}
```

### 2.3. Flujos de caracteres

- **Flujos de caracteres.** Transforman automáticamente los caracteres a Unicode.
- **`FileReader`** y **`FileWriter`.** Para leer y escribir caracteres.

Ejemplo de lectura:

```java
while (in.ready()) {
    char d = (char) in.read();
}
```

Ejemplo de escritura:

```java
out.write("Hola");
```

### 2.4. Flujos con buffer

- **Flujos con buffer.** Mejoran el rendimiento al usar una memoria intermedia.
- **`BufferedReader`** y **`BufferedWriter`.** Para flujos de caracteres.

Ejemplo de lectura:

```java
BufferedReader inputStream = new BufferedReader(new FileReader("original.txt"));
while ((línea = in.readLine()) != null) {
}
```

Ejemplo de escritura:

```java
out.write(línea);
out.newLine();
```

### 2.5. Flujos de datos

- **Flujos de datos.** Manejan tipos primitivos y `String`.
- **`DataInputStream`** y **`DataOutputStream`.** Para leer y escribir datos primitivos.

Ejemplo de escritura:

```java
DataOutputStream out = new DataOutputStream(new BufferedOutputStream(new FileOutputStream(dataFile)));
out.writeDouble(producto.getPrecio());
out.writeInt(producto.getUnidades());
out.writeUTF(producto.getNombre());
```

Ejemplo de lectura:

```java
DataInputStream in = new DataInputStream(new BufferedInputStream(new FileInputStream(dataFile)));
double precio = in.readDouble();
int unidades = in.readInt();
String nombre = in.readUTF();
```

### 2.6. Flujos de objetos

- **Flujos de objetos.** Permiten guardar y recuperar objetos directamente.
- **Serializable.** La clase del objeto debe implementar esta interfaz.
- **`ObjectInputStream`** y **`ObjectOutputStream`.** Para leer y escribir objetos.

Ejemplo de escritura:

```java
ObjectOutputStream out = new ObjectOutputStream(new BufferedOutputStream(new FileOutputStream(dataFile)));
out.writeObject(producto);
```

Ejemplo de lectura:

```java
ObjectInputStream in = new ObjectInputStream(new BufferedInputStream(new FileInputStream(dataFile)));
Producto recuperado = (Producto) in.readObject();
```

### 2.7. Escritura y lectura de objetos complejos

**Objetos complejos.** Si un objeto contiene otros objetos, estos también se serializan.

Ejemplo de escritura de lista:

```java
ObjectOutputStream out = new ObjectOutputStream(new BufferedOutputStream(new FileOutputStream(dataFile)));
ArrayList<Producto> productos = new ArrayList<>();
out.writeObject(productos);
```

Ejemplo de lectura de lista:

```java
ObjectInputStream in = new ObjectInputStream(new BufferedInputStream(new FileInputStream(dataFile)));
ArrayList<Producto> recuperados = (ArrayList<Producto>) in.readObject();
```

## 3. Conclusión

El documento explica cómo trabajar con flujos de datos en Java para implementar la persistencia de datos. Se cubren flujos de bytes, caracteres, datos primitivos y objetos, destacando la importancia de cerrar los recursos y manejar excepciones adecuadamente. También se introduce el uso de buffers para mejorar el rendimiento y la serialización de objetos complejos.
