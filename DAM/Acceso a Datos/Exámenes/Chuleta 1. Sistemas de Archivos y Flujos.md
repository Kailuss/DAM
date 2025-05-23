---
tags:
  - DAM
  - AD
cssclasses:
  - dam-ad
  - table-clean
banner: "![[ad.jpg]]"
banner_y: 0.32
---

# **Chuleta 1.** <br>Sistemas de Archivos y Flujos

## Sistemas de Archivos (Path y Files)

```java
// Crear Path
Path ruta = Path.of("/home/usuario/archivo.txt");
Path ruta2 = Path.of("directorio", "subdirectorio", "archivo.txt");

// Información de Path
int elementos = ruta.getNameCount();       // Número de elementos
Path elemento = ruta.getName(0);           // Elemento en posición 0
Path archivo = ruta.getFileName();         // Último elemento
Path subRuta = ruta.subpath(0, 2);         // Subruta desde 0 hasta 2 (excl.)

// Consultas Files
boolean esArchivo = Files.isRegularFile(ruta);
boolean esDirectorio = Files.isDirectory(ruta);
boolean esLegible = Files.isReadable(ruta);
boolean esEscribible = Files.isWritable(ruta);
long tamaño = Files.size(ruta);

// Crear directorios
Files.createDirectory(ruta);               // Crea directorio (debe existir padre)
Files.createDirectories(ruta);             // Crea directorio y padres si no existen

// Eliminar, copiar y mover
Files.delete(ruta);
Files.copy(origen, destino, StandardCopyOption.REPLACE_EXISTING);
Files.move(origen, destino, StandardCopyOption.REPLACE_EXISTING);

// Leer y escribir archivos
byte[] bytes = Files.readAllBytes(ruta);
List<String> lineas = Files.readAllLines(ruta, StandardCharsets.UTF_8);
Files.write(ruta, "Contenido".getBytes(), StandardOpenOption.CREATE, 
            StandardOpenOption.APPEND);

// Leer directorio
try (DirectoryStream<Path> stream = Files.newDirectoryStream(ruta)) {
    for (Path archivo : stream) {
        System.out.println(archivo.getFileName());
    }
}
```

## Flujos de Bytes

```java
// Try-with-resources para gestión automática de recursos
try (FileInputStream in = new FileInputStream("origen.dat");
     FileOutputStream out = new FileOutputStream("destino.dat")) {
    
    int c;
    while ((c = in.read()) != -1) {
        out.write(c);
    }
}
```

## Flujos de Caracteres

```java
// Flujos de caracteres con buffer
try (BufferedReader in = new BufferedReader(new FileReader("origen.txt", StandardCharsets.UTF_8));
     BufferedWriter out = new BufferedWriter(new FileWriter("destino.txt", StandardCharsets.UTF_8))) {
    
    String linea;
    while ((linea = in.readLine()) != null) {
        out.write(linea);
        out.newLine();
    }
    out.flush(); // Forzar escritura del buffer
}
```

## Flujos de Datos

```java
// Escribir datos primitivos
try (DataOutputStream out = new DataOutputStream(
        new BufferedOutputStream(new FileOutputStream("datos.dat")))) {
    
    out.writeInt(42);
    out.writeDouble(3.14);
    out.writeUTF("Hola");
}

// Leer datos primitivos
try (DataInputStream in = new DataInputStream(
        new BufferedInputStream(new FileInputStream("datos.dat")))) {
    
    try {
        while (true) {
            int entero = in.readInt();
            double decimal = in.readDouble();
            String texto = in.readUTF();
            // Procesar datos...
        }
    } catch (EOFException e) {
        // Fin del archivo
    }
}
```

## Serialización de Objetos

```java
// Clase serializable
public class Producto implements Serializable {
    private static final long serialVersionUID = 1L;
    private String nombre;
    private double precio;
    
    // Constructor, getters, setters...
}

// Escribir objetos
try (ObjectOutputStream out = new ObjectOutputStream(
        new BufferedOutputStream(new FileOutputStream("objetos.dat")))) {
    
    Producto p = new Producto("Laptop", 999.99);
    out.writeObject(p);
    
    ArrayList<Producto> lista = new ArrayList<>();
    lista.add(p);
    out.writeObject(lista); // Serializa toda la lista
}

// Leer objetos
try (ObjectInputStream in = new ObjectInputStream(
        new BufferedInputStream(new FileInputStream("objetos.dat")))) {
    
    try {
        while (true) {
            Producto p = (Producto) in.readObject();
            // Procesar objeto...
        }
    } catch (EOFException e) {
        // Fin del archivo
    } catch (ClassNotFoundException e) {
        // Clase no encontrada
    }
}
```
