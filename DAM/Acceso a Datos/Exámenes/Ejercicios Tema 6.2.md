# Ejercicios TEMA 6.2: MongoDB y Java

## Instrucciones

1. Crea un proyecto para hacer los ejercicios o aprovecha el del bloque de ejercicios anterior.
2. Crea un paquete donde guardarás todas las clases creadas en estos ejercicios.
3. Crea otro paquete con una clase con main. Desde esta clase prueba todos los métodos creados en los ejercicios.
4. Crea una excepción para tratar los errores propios de la aplicación (o reaprovecha la del bloque anterior).
5. Propaga las excepciones hasta el main y tratándolas allí.
6. Añade las dependencias necesarias para MongoDB Java Driver.

## Ejercicios

### Ejercicio 1: Clase ConexionMongoDB

**Descripción**: Esta clase proporciona métodos para establecer y gestionar conexiones a una base de datos MongoDB desde Java. Implementa el patrón Singleton para asegurar que solo exista una instancia de la conexión en toda la aplicación, lo que optimiza el uso de recursos y simplifica la gestión de conexiones.

```java
package com.example.mongodb; // Define el paquete donde se encuentra la clase

import com.mongodb.client.MongoClient; // Cliente para conectar a MongoDB
import com.mongodb.client.MongoClients; // Factoría para crear clientes MongoDB
import com.mongodb.client.MongoDatabase; // Representa una base de datos MongoDB
import com.mongodb.MongoClientSettings; // Configuración del cliente MongoDB
import com.mongodb.ConnectionString; // Cadena de conexión a MongoDB
import com.mongodb.ServerApi; // API del servidor MongoDB
import com.mongodb.ServerApiVersion; // Versión de la API del servidor

/**
 * Clase para gestionar la conexión a la base de datos MongoDB.
 * Implementa el patrón Singleton para asegurar una única instancia de conexión.
 */
public class ConexionMongoDB {
    
    // Constantes para la conexión
    private static final String CONNECTION_STRING = "mongodb://localhost:27017"; // URL de conexión a MongoDB
    private static final String DATABASE_NAME = "biblioteca"; // Nombre de la base de datos
    
    // Instancia única de la clase (patrón Singleton)
    private static ConexionMongoDB instancia;
    
    // Objetos para la conexión a MongoDB
    private MongoClient mongoClient; // Cliente MongoDB
    private MongoDatabase database; // Base de datos MongoDB
    
    /**
     * Constructor privado para evitar instanciación directa (patrón Singleton).
     * Establece la conexión a la base de datos MongoDB.
     * 
     * @throws MiExcepcion Si hay algún error al conectar a la BD
     */
    private ConexionMongoDB() throws MiExcepcion {
        try {
            // Configuramos la conexión a MongoDB
            // Creamos una cadena de conexión a partir de la URL
            ConnectionString connectionString = new ConnectionString(CONNECTION_STRING);
            
            // Configuramos la versión de la API del servidor
            ServerApi serverApi = ServerApi.builder()
                    .version(ServerApiVersion.V1) // Usamos la versión 1 de la API
                    .build();
            
            // Configuramos el cliente MongoDB con la cadena de conexión y la API del servidor
            MongoClientSettings settings = MongoClientSettings.builder()
                    .applyConnectionString(connectionString)
                    .serverApi(serverApi)
                    .build();
            
            // Creamos el cliente MongoDB con la configuración
            mongoClient = MongoClients.create(settings);
            
            // Obtenemos la base de datos
            database = mongoClient.getDatabase(DATABASE_NAME);
            
            System.out.println("Conexión establecida con éxito a MongoDB: " + CONNECTION_STRING);
            System.out.println("Base de datos: " + DATABASE_NAME);
        } catch (Exception e) {
            // Error al establecer la conexión
            throw new MiExcepcion("Error al conectar a la base de datos MongoDB: " + e.getMessage(), e);
        }
    }
    
    /**
     * Método estático para obtener la instancia única de la clase (patrón Singleton).
     * Si la instancia no existe, la crea; si existe, la devuelve.
     * 
     * @return Instancia única de ConexionMongoDB
     * @throws MiExcepcion Si hay algún error al crear la instancia
     */
    public static synchronized ConexionMongoDB getInstancia() throws MiExcepcion {
        // Si la instancia no existe, la creamos
        if (instancia == null) {
            instancia = new ConexionMongoDB();
        }
        return instancia;
    }
    
    /**
     * Obtiene el cliente MongoDB para realizar operaciones en la base de datos.
     * 
     * @return Cliente MongoDB
     */
    public MongoClient getMongoClient() {
        return mongoClient;
    }
    
    /**
     * Obtiene la base de datos MongoDB para realizar operaciones.
     * 
     * @return Base de datos MongoDB
     */
    public MongoDatabase getDatabase() {
        return database;
    }
    
    /**
     * Cierra la conexión a la base de datos MongoDB.
     * 
     * @throws MiExcepcion Si hay algún error al cerrar la conexión
     */
    public void cerrarConexion() throws MiExcepcion {
        try {
            // Verificamos que el cliente no sea nulo
            if (mongoClient != null) {
                // Cerramos el cliente MongoDB
                mongoClient.close();
                System.out.println("Conexión cerrada con éxito");
            }
        } catch (Exception e) {
            // Error al cerrar la conexión
            throw new MiExcepcion("Error al cerrar la conexión: " + e.getMessage(), e);
        } finally {
            // Establecemos la instancia a null para que se pueda crear una nueva
            instancia = null;
        }
    }
}
```

### Ejercicio 2: Clase Libro

**Descripción**: Esta clase representa la entidad Libro en la aplicación, con atributos como ISBN, título, autor, etc. Proporciona métodos para acceder y modificar estos atributos, así como para convertir el libro a un documento BSON (formato utilizado por MongoDB) y viceversa. Es una clase POJO (Plain Old Java Object) que se utilizará para mapear los documentos de la colección de libros en MongoDB.

```java
package com.example.mongodb; // Define el paquete donde se encuentra la clase

import java.util.ArrayList; // Para manejar listas
import java.util.List; // Interfaz para listas

import org.bson.Document; // Representa un documento BSON en MongoDB
import org.bson.types.ObjectId; // Representa un ObjectId de MongoDB

/**
 * Clase que representa un libro en la biblioteca.
 * Contiene los atributos básicos de un libro y métodos para convertir entre Libro y Document.
 */
public class Libro {
    
    // Atributos de la clase
    private ObjectId id; // ID generado por MongoDB
    private String isbn; // ISBN del libro (identificador único)
    private String titulo; // Título del libro
    private String autor; // Autor del libro
    private int anioPublicacion; // Año de publicación
    private String editorial; // Editorial del libro
    private int numPaginas; // Número de páginas
    private List<String> generos; // Géneros literarios
    private boolean disponible; // Disponibilidad del libro
    private double precio; // Precio del libro
    
    /**
     * Constructor por defecto.
     * Inicializa un libro con valores vacíos.
     */
    public Libro() {
        this.id = null;
        this.isbn = "";
        this.titulo = "";
        this.autor = "";
        this.anioPublicacion = 0;
        this.editorial = "";
        this.numPaginas = 0;
        this.generos = new ArrayList<>();
        this.disponible = false;
        this.precio = 0.0;
    }
    
    /**
     * Constructor con parámetros básicos.
     * 
     * @param isbn ISBN del libro
     * @param titulo Título del libro
     * @param autor Autor del libro
     */
    public Libro(String isbn, String titulo, String autor) {
        this.id = null;
        this.isbn = isbn;
        this.titulo = titulo;
        this.autor = autor;
        this.anioPublicacion = 0;
        this.editorial = "";
        this.numPaginas = 0;
        this.generos = new ArrayList<>();
        this.disponible = false;
        this.precio = 0.0;
    }
    
    /**
     * Constructor con todos los parámetros.
     * 
     * @param isbn ISBN del libro
     * @param titulo Título del libro
     * @param autor Autor del libro
     * @param anioPublicacion Año de publicación
     * @param editorial Editorial del libro
     * @param numPaginas Número de páginas
     * @param generos Géneros literarios
     * @param disponible Disponibilidad del libro
     * @param precio Precio del libro
     */
    public Libro(String isbn, String titulo, String autor, int anioPublicacion, 
                String editorial, int numPaginas, List<String> generos, 
                boolean disponible, double precio) {
        this.id = null;
        this.isbn = isbn;
        this.titulo = titulo;
        this.autor = autor;
        this.anioPublicacion = anioPublicacion;
        this.editorial = editorial;
        this.numPaginas = numPaginas;
        this.generos = generos != null ? generos : new ArrayList<>();
        this.disponible = disponible;
        this.precio = precio;
    }
    
    // Métodos getter y setter para cada atributo
    
    /**
     * Obtiene el ID de MongoDB.
     * 
     * @return ID de MongoDB
     */
    public ObjectId getId() {
        return id;
    }
    
    /**
     * Establece el ID de MongoDB.
     * 
     * @param id Nuevo ID de MongoDB
     */
    public void setId(ObjectId id) {
        this.id = id;
    }
    
    /**
     * Obtiene el ISBN del libro.
     * 
     * @return ISBN del libro
     */
    public String getIsbn() {
        return isbn;
    }
    
    /**
     * Establece el ISBN del libro.
     * 
     * @param isbn Nuevo ISBN del libro
     */
    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }
    
    /**
     * Obtiene el título del libro.
     * 
     * @return Título del libro
     */
    public String getTitulo() {
        return titulo;
    }
    
    /**
     * Establece el título del libro.
     * 
     * @param titulo Nuevo título del libro
     */
    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }
    
    /**
     * Obtiene el autor del libro.
     * 
     * @return Autor del libro
     */
    public String getAutor() {
        return autor;
    }
    
    /**
     * Establece el autor del libro.
     * 
     * @param autor Nuevo autor del libro
     */
    public void setAutor(String autor) {
        this.autor = autor;
    }
    
    /**
     * Obtiene el año de publicación del libro.
     * 
     * @return Año de publicación
     */
    public int getAnioPublicacion() {
        return anioPublicacion;
    }
    
    /**
     * Establece el año de publicación del libro.
     * 
     * @param anioPublicacion Nuevo año de publicación
     */
    public void setAnioPublicacion(int anioPublicacion) {
        this.anioPublicacion = anioPublicacion;
    }
    
    /**
     * Obtiene la editorial del libro.
     * 
     * @return Editorial del libro
     */
    public String getEditorial() {
        return editorial;
    }
    
    /**
     * Establece la editorial del libro.
     * 
     * @param editorial Nueva editorial del libro
     */
    public void setEditorial(String editorial) {
        this.editorial = editorial;
    }
    
    /**
     * Obtiene el número de páginas del libro.
     * 
     * @return Número de páginas
     */
    public int getNumPaginas() {
        return numPaginas;
    }
    
    /**
     * Establece el número de páginas del libro.
     * 
     * @param numPaginas Nuevo número de páginas
     */
    public void setNumPaginas(int numPaginas) {
        this.numPaginas = numPaginas;
    }
    
    /**
     * Obtiene los géneros literarios del libro.
     * 
     * @return Géneros literarios
     */
    public List<String> getGeneros() {
        return generos;
    }
    
    /**
     * Establece los géneros literarios del libro.
     * 
     * @param generos Nuevos géneros literarios
     */
    public void setGeneros(List<String> generos) {
        this.generos = generos != null ? generos : new ArrayList<>();
    }
    
    /**
     * Añade un género literario al libro.
     * 
     * @param genero Género a añadir
     */
    public void addGenero(String genero) {
        if (genero != null && !genero.isEmpty()) {
            this.generos.add(genero);
        }
    }
    
    /**
     * Comprueba si el libro está disponible.
     * 
     * @return true si está disponible, false en caso contrario
     */
    public boolean isDisponible() {
        return disponible;
    }
    
    /**
     * Establece la disponibilidad del libro.
     * 
     * @param disponible Nueva disponibilidad
     */
    public void setDisponible(boolean disponible) {
        this.disponible = disponible;
    }
    
    /**
     * Obtiene el precio del libro.
     * 
     * @return Precio del libro
     */
    public double getPrecio() {
        return precio;
    }
    
    /**
     * Establece el precio del libro.
     * 
     * @param precio Nuevo precio del libro
     */
    public void setPrecio(double precio) {
        this.precio = precio;
    }
    
    /**
     * Convierte el libro a un documento BSON para MongoDB.
     * 
     * @return Documento BSON
     */
    public Document toDocument() {
        Document doc = new Document();
        
        // Añadimos todos los campos al documento
        if (id != null) {
            doc.append("_id", id);
        }
        doc.append("isbn", isbn);
        doc.append("titulo", titulo);
        doc.append("autor", autor);
        doc.append("anio_publicacion", anioPublicacion);
        doc.append("editorial", editorial);
        doc.append("num_paginas", numPaginas);
        doc.append("generos", generos);
        doc.append("disponible", disponible);
        doc.append("precio", precio);
        
        return doc;
    }
    
    /**
     * Crea un objeto Libro a partir de un documento BSON de MongoDB.
     * 
     * @param doc Documento BSON
     * @return Objeto Libro
     */
    public static Libro fromDocument(Document doc) {
        if (doc == null) {
            return null;
        }
        
        Libro libro = new Libro();
        
        // Extraemos todos los campos del documento
        libro.setId(doc.getObjectId("_id"));
        libro.setIsbn(doc.getString("isbn"));
        libro.setTitulo(doc.getString("titulo"));
        libro.setAutor(doc.getString("autor"));
        libro.setAnioPublicacion(doc.getInteger("anio_publicacion", 0));
        libro.setEditorial(doc.getString("editorial"));
        libro.setNumPaginas(doc.getInteger("num_paginas", 0));
        
        // Extraemos la lista de géneros
        List<String> generos = doc.getList("generos", String.class);
        if (generos != null) {
            libro.setGeneros(generos);
        }
        
        libro.setDisponible(doc.getBoolean("disponible", false));
        libro.setPrecio(doc.getDouble("precio", 0.0));
        
        return libro;
    }
    
    /**
     * Devuelve una representación en texto del libro.
     * Útil para depuración y visualización.
     * 
     * @return Representación en texto del libro
     */
    @Override
    public String toString() {
        return "Libro{" +
                "id=" + id +
                ", isbn='" + isbn + '\'' +
                ", titulo='" + titulo + '\'' +
                ", autor='" + autor + '\'' +
                ", anioPublicacion=" + anioPublicacion +
                ", editorial='" + editorial + '\'' +
                ", numPaginas=" + numPaginas +
                ", generos=" + generos +
                ", disponible=" + disponible +
                ", precio=" + precio +
                '}';
    }
}
```

### Ejercicio 3: Clase LibroDAO

**Descripción**: Esta clase implementa el patrón DAO (Data Access Object) para la entidad Libro, proporcionando métodos para realizar operaciones CRUD en la colección de libros de MongoDB. Encapsula la lógica de acceso a datos, separándola de la lógica de negocio, lo que mejora la mantenibilidad y modularidad del código.

```java
package com.example.mongodb; // Define el paquete donde se encuentra la clase

import java.util.ArrayList; // Para manejar listas
import java.util.List; // Interfaz para listas

import org.bson.Document; // Representa un documento BSON en MongoDB
import org.bson.conversions.Bson; // Interfaz para filtros y actualizaciones
import org.bson.types.ObjectId; // Representa un ObjectId de MongoDB

import com.mongodb.client.FindIterable; // Resultado de una consulta find
import com.mongodb.client.MongoCollection; // Representa una colección en MongoDB
import com.mongodb.client.MongoCursor; // Cursor para iterar sobre resultados
import com.mongodb.client.MongoDatabase; // Representa una base de datos MongoDB
import com.mongodb.client.model.Filters; // Utilidades para crear filtros
import com.mongodb.client.model.Updates; // Utilidades para crear actualizaciones
import com.mongodb.client.result.DeleteResult; // Resultado de una operación delete
import com.mongodb.client.result.InsertOneResult; // Resultado de una operación insertOne
import com.mongodb.client.result.UpdateResult; // Resultado de una operación update

/**
 * Clase que implementa el patrón DAO (Data Access Object) para la entidad Libro.
 * Proporciona métodos para realizar operaciones CRUD en la colección de libros.
 */
public class LibroDAO {
    
    // Nombre de la colección en MongoDB
    private static final String COLLECTION_NAME = "libros";
    
    // Colección de MongoDB
    private MongoCollection<Document> collection;
    
    /**
     * Constructor que recibe una base de datos MongoDB.
     * 
     * @param database Base de datos MongoDB
     */
    public LibroDAO(MongoDatabase database) {
        // Obtenemos la colección de libros
        this.collection = database.getCollection(COLLECTION_NAME);
    }
    
    /**
     * Inserta un nuevo libro en la colección.
     * 
     * @param libro Libro a insertar
     * @return true si la inserción fue exitosa, false en caso contrario
     * @throws MiExcepcion Si hay algún error durante la inserción
     */
    public boolean insertar(Libro libro) throws MiExcepcion {
        try {
            // Convertimos el libro a un documento BSON
            Document doc = libro.toDocument();
            
            // Insertamos el documento en la colección
            InsertOneResult result = collection.insertOne(doc);
            
            // Si se generó un ID, la inserción fue exitosa
            if (result.getInsertedId() != null) {
                // Actualizamos el ID del libro con el generado por MongoDB
                libro.setId(doc.getObjectId("_id"));
                return true;
            }
            
            return false;
        } catch (Exception e) {
            // Error al ejecutar la operación
            throw new MiExcepcion("Error al insertar libro: " + e.getMessage(), e);
        }
    }
    
    /**
     * Actualiza un libro existente en la colección.
     * 
     * @param libro Libro con los nuevos datos
     * @return true si la actualización fue exitosa, false en caso contrario
     * @throws MiExcepcion Si hay algún error durante la actualización
     */
    public boolean actualizar(Libro libro) throws MiExcepcion {
        try {
            // Creamos el filtro para identificar el libro por su ISBN
            Bson filtro = Filters.eq("isbn", libro.getIsbn());
            
            // Convertimos el libro a un documento BSON
            Document doc = libro.toDocument();
            
            // Eliminamos el campo _id para evitar errores al actualizar
            doc.remove("_id");
            
            // Actualizamos el documento en la colección
            // Reemplazamos todo el documento excepto el _id
            UpdateResult result = collection.replaceOne(filtro, doc);
            
            // Si se modificó al menos un documento, la actualización fue exitosa
            return result.getModifiedCount() > 0;
        } catch (Exception e) {
            // Error al ejecutar la operación
            throw new MiExcepcion("Error al actualizar libro: " + e.getMessage(), e);
        }
    }
    
    /**
     * Actualiza campos específicos de un libro.
     * 
     * @param isbn ISBN del libro a actualizar
     * @param campos Mapa de campos a actualizar (nombre del campo -> nuevo valor)
     * @return true si la actualización fue exitosa, false en caso contrario
     * @throws MiExcepcion Si hay algún error durante la actualización
     */
    public boolean actualizarCampos(String isbn, Document campos) throws MiExcepcion {
        try {
            // Creamos el filtro para identificar el libro por su ISBN
            Bson filtro = Filters.eq("isbn", isbn);
            
            // Creamos la actualización con los campos proporcionados
            // $set actualiza los campos especificados sin modificar el resto
            Bson actualizacion = new Document("$set", campos);
            
            // Actualizamos el documento en la colección
            UpdateResult result = collection.updateOne(filtro, actualizacion);
            
            // Si se modificó al menos un documento, la actualización fue exitosa
            return result.getModifiedCount() > 0;
        } catch (Exception e) {
            // Error al ejecutar la operación
            throw new MiExcepcion("Error al actualizar campos del libro: " + e.getMessage(), e);
        }
    }
    
    /**
     * Elimina un libro de la colección por su ISBN.
     * 
     * @param isbn ISBN del libro a eliminar
     * @return true si la eliminación fue exitosa, false en caso contrario
     * @throws MiExcepcion Si hay algún error durante la eliminación
     */
    public boolean eliminar(String isbn) throws MiExcepcion {
        try {
            // Creamos el filtro para identificar el libro por su ISBN
            Bson filtro = Filters.eq("isbn", isbn);
            
            // Eliminamos el documento de la colección
            DeleteResult result = collection.deleteOne(filtro);
            
            // Si se eliminó al menos un documento, la eliminación fue exitosa
            return result.getDeletedCount() > 0;
        } catch (Exception e) {
            // Error al ejecutar la operación
            throw new MiExcepcion("Error al eliminar libro: " + e.getMessage(), e);
        }
    }
    
    /**
     * Obtiene todos los libros de la colección.
     * 
     * @return Lista de todos los libros
     * @throws MiExcepcion Si hay algún error durante la consulta
     */
    public List<Libro> obtenerTodos() throws MiExcepcion {
        try {
            // Lista para almacenar los libros
            List<Libro> libros = new ArrayList<>();
            
            // Obtenemos todos los documentos de la colección
            FindIterable<Document> documentos = collection.find();
            
            // Iteramos sobre los documentos y los convertimos a objetos Libro
            try (MongoCursor<Document> cursor = documentos.iterator()) {
                while (cursor.hasNext()) {
                    Document doc = cursor.next();
                    Libro libro = Libro.fromDocument(doc);
                    libros.add(libro);
                }
            }
            
            return libros;
        } catch (Exception e) {
            // Error al ejecutar la operación
            throw new MiExcepcion("Error al obtener todos los libros: " + e.getMessage(), e);
        }
    }
    
    /**
     * Obtiene un libro de la colección por su ISBN.
     * 
     * @param isbn ISBN del libro a buscar
     * @return Libro encontrado o null si no existe
     * @throws MiExcepcion Si hay algún error durante la consulta
     */
    public Libro obtenerPorIsbn(String isbn) throws MiExcepcion {
        try {
            // Creamos el filtro para identificar el libro por su ISBN
            Bson filtro = Filters.eq("isbn", isbn);
            
            // Buscamos el documento en la colección
            Document doc = collection.find(filtro).first();
            
            // Si encontramos el documento, lo convertimos a un objeto Libro
            if (doc != null) {
                return Libro.fromDocument(doc);
            }
            
            // Si no encontramos el documento, devolvemos null
            return null;
        } catch (Exception e) {
            // Error al ejecutar la operación
            throw new MiExcepcion("Error al obtener libro por ISBN: " + e.getMessage(), e);
        }
    }
    
    /**
     * Obtiene libros de la colección por autor.
     * 
     * @param autor Autor de los libros a buscar
     * @return Lista de libros del autor
     * @throws MiExcepcion Si hay algún error durante la consulta
     */
    public List<Libro> obtenerPorAutor(String autor) throws MiExcepcion {
        try {
            // Lista para almacenar los libros
            List<Libro> libros = new ArrayList<>();
            
            // Creamos el filtro para buscar libros por autor
            Bson filtro = Filters.eq("autor", autor);
            
            // Buscamos los documentos en la colección
            FindIterable<Document> documentos = collection.find(filtro);
            
            // Iteramos sobre los documentos y los convertimos a objetos Libro
            try (MongoCursor<Document> cursor = documentos.iterator()) {
                while (cursor.hasNext()) {
                    Document doc = cursor.next();
                    Libro libro = Libro.fromDocument(doc);
                    libros.add(libro);
                }
            }
            
            return libros;
        } catch (Exception e) {
            // Error al ejecutar la operación
            throw new MiExcepcion("Error al obtener libros por autor: " + e.getMessage(), e);
        }
    }
    
    /**
     * Obtiene libros de la colección por género.
     * 
     * @param genero Género de los libros a buscar
     * @return Lista de libros del género
     * @throws MiExcepcion Si hay algún error durante la consulta
     */
    public List<Libro> obtenerPorGenero(String genero) throws MiExcepcion {
        try {
            // Lista para almacenar los libros
            List<Libro> libros = new ArrayList<>();
            
            // Creamos el filtro para buscar libros por género
            // $in busca documentos donde el campo generos contiene el valor especificado
            Bson filtro = Filters.in("generos", genero);
            
            // Buscamos los documentos en la colección
            FindIterable<Document> documentos = collection.find(filtro);
            
            // Iteramos sobre los documentos y los convertimos a objetos Libro
            try (MongoCursor<Document> cursor = documentos.iterator()) {
                while (cursor.hasNext()) {
                    Document doc = cursor.next();
                    Libro libro = Libro.fromDocument(doc);
                    libros.add(libro);
                }
            }
            
            return libros;
        } catch (Exception e) {
            // Error al ejecutar la operación
            throw new MiExcepcion("Error al obtener libros por género: " + e.getMessage(), e);
        }
    }
    
    /**
     * Obtiene libros de la colección por disponibilidad.
     * 
     * @param disponible Disponibilidad de los libros a buscar
     * @return Lista de libros disponibles o no disponibles
     * @throws MiExcepcion Si hay algún error durante la consulta
     */
    public List<Libro> obtenerPorDisponibilidad(boolean disponible) throws MiExcepcion {
        try {
            // Lista para almacenar los libros
            List<Libro> libros = new ArrayList<>();
            
            // Creamos el filtro para buscar libros por disponibilidad
            Bson filtro = Filters.eq("disponible", disponible);
            
            // Buscamos los documentos en la colección
            FindIterable<Document> documentos = collection.find(filtro);
            
            // Iteramos sobre los documentos y los convertimos a objetos Libro
            try (MongoCursor<Document> cursor = documentos.iterator()) {
                while (cursor.hasNext()) {
                    Document doc = cursor.next();
                    Libro libro = Libro.fromDocument(doc);
                    libros.add(libro);
                }
            }
            
            return libros;
        } catch (Exception e) {
            // Error al ejecutar la operación
            throw new MiExcepcion("Error al obtener libros por disponibilidad: " + e.getMessage(), e);
        }
    }
    
    /**
     * Obtiene libros de la colección por rango de precio.
     * 
     * @param precioMin Precio mínimo
     * @param precioMax Precio máximo
     * @return Lista de libros en el rango de precio
     * @throws MiExcepcion Si hay algún error durante la consulta
     */
    public List<Libro> obtenerPorRangoPrecio(double precioMin, double precioMax) throws MiExcepcion {
        try {
            // Lista para almacenar los libros
            List<Libro> libros = new ArrayList<>();
            
            // Creamos el filtro para buscar libros por rango de precio
            // $gte: mayor o igual que, $lte: menor o igual que
            Bson filtro = Filters.and(
                    Filters.gte("precio", precioMin),
                    Filters.lte("precio", precioMax)
            );
            
            // Buscamos los documentos en la colección
            FindIterable<Document> documentos = collection.find(filtro);
            
            // Iteramos sobre los documentos y los convertimos a objetos Libro
            try (MongoCursor<Document> cursor = documentos.iterator()) {
                while (cursor.hasNext()) {
                    Document doc = cursor.next();
                    Libro libro = Libro.fromDocument(doc);
                    libros.add(libro);
                }
            }
            
            return libros;
        } catch (Exception e) {
            // Error al ejecutar la operación
            throw new MiExcepcion("Error al obtener libros por rango de precio: " + e.getMessage(), e);
        }
    }
}
```

### Ejercicio 4: Clase MiExcepcion

**Descripción**: Esta clase representa una excepción personalizada para la aplicación, que permite encapsular y propagar errores específicos de manera controlada. Es especialmente útil para manejar errores relacionados con la base de datos y convertir excepciones técnicas en mensajes más comprensibles para el usuario.

```java
package com.example.mongodb; // Define el paquete donde se encuentra la clase

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

### Ejercicio 5: Clase PruebasMongoDB (con main)

**Descripción**: Esta clase contiene el método main y métodos para probar todas las funcionalidades implementadas en las clases anteriores. Aquí se realizan pruebas de conexión a la base de datos MongoDB y operaciones CRUD sobre la colección de libros, demostrando el uso del driver de MongoDB para Java.

```java
package com.example.main; // Define el paquete donde se encuentra la clase principal

import java.util.ArrayList; // Para manejar listas
import java.util.Arrays; // Utilidades para arrays
import java.util.List; // Interfaz para listas

import org.bson.Document; // Representa un documento BSON en MongoDB

import com.mongodb.client.MongoDatabase; // Representa una base de datos MongoDB

import com.example.mongodb.ConexionMongoDB; // Importamos la clase de conexión
import com.example.mongodb.Libro; // Importamos la clase Libro
import com.example.mongodb.LibroDAO; // Importamos la clase DAO
import com.example.mongodb.MiExcepcion; // Importamos nuestra excepción personalizada

/**
 * Clase principal para probar las funcionalidades de MongoDB con Java.
 * Contiene el método main y métodos para probar cada aspecto de la conexión y operaciones CRUD.
 */
public class PruebasMongoDB {
    
    /**
     * Método principal que ejecuta las pruebas.
     * 
     * @param args Argumentos de línea de comandos (no utilizados)
     */
    public static void main(String[] args) {
        try {
            // Obtenemos la instancia de conexión a MongoDB
            ConexionMongoDB conexionMongoDB = ConexionMongoDB.getInstancia();
            MongoDatabase database = conexionMongoDB.getDatabase();
            
            // Creamos un objeto LibroDAO con la base de datos
            LibroDAO libroDAO = new LibroDAO(database);
            
            // Probamos las diferentes operaciones CRUD
            probarInsercion(libroDAO);
            probarConsulta(libroDAO);
            probarActualizacion(libroDAO);
            probarEliminacion(libroDAO);
            probarConsultasAvanzadas(libroDAO);
            
            // Cerramos la conexión
            conexionMongoDB.cerrarConexion();
            
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
     * Prueba la inserción de libros en la base de datos.
     * 
     * @param libroDAO Objeto DAO para realizar operaciones con libros
     * @throws MiExcepcion Si hay algún error durante la inserción
     */
    private static void probarInsercion(LibroDAO libroDAO) throws MiExcepcion {
        System.out.println("\n=== Prueba de Inserción ===");
        
        // Creamos algunos libros de ejemplo
        Libro libro1 = new Libro(
                "9788401352836",
                "Don Quijote de la Mancha",
                "Miguel de Cervantes",
                1605,
                "Real Academia Española",
                1250,
                Arrays.asList("Novela", "Clásico", "Sátira"),
                true,
                25.50
        );
        
        Libro libro2 = new Libro(
                "9788420412146",
                "Cien años de soledad",
                "Gabriel García Márquez",
                1967,
                "Cátedra",
                481,
                Arrays.asList("Novela", "Realismo mágico", "Literatura latinoamericana"),
                true,
                19.95
        );
        
        // Insertamos los libros en la base de datos
        boolean resultado1 = libroDAO.insertar(libro1);
        boolean resultado2 = libroDAO.insertar(libro2);
        
        // Mostramos los resultados
        System.out.println("Inserción de libro 1: " + (resultado1 ? "Exitosa" : "Fallida"));
        System.out.println("Inserción de libro 2: " + (resultado2 ? "Exitosa" : "Fallida"));
        
        // Mostramos los IDs generados por MongoDB
        System.out.println("ID del libro 1: " + libro1.getId());
        System.out.println("ID del libro 2: " + libro2.getId());
    }
    
    /**
     * Prueba la consulta de libros en la base de datos.
     * 
     * @param libroDAO Objeto DAO para realizar operaciones con libros
     * @throws MiExcepcion Si hay algún error durante la consulta
     */
    private static void probarConsulta(LibroDAO libroDAO) throws MiExcepcion {
        System.out.println("\n=== Prueba de Consulta ===");
        
        // Consultamos todos los libros
        List<Libro> libros = libroDAO.obtenerTodos();
        
        // Mostramos los libros obtenidos
        System.out.println("Libros en la base de datos:");
        for (Libro libro : libros) {
            System.out.println("  " + libro);
        }
        
        // Consultamos un libro por su ISBN
        String isbn = "9788401352836"; // ISBN de "Don Quijote de la Mancha"
        Libro libro = libroDAO.obtenerPorIsbn(isbn);
        
        // Mostramos el libro obtenido
        if (libro != null) {
            System.out.println("\nLibro con ISBN " + isbn + ":");
            System.out.println("  " + libro);
        } else {
            System.out.println("\nNo se encontró un libro con ISBN " + isbn);
        }
    }
    
    /**
     * Prueba la actualización de libros en la base de datos.
     * 
     * @param libroDAO Objeto DAO para realizar operaciones con libros
     * @throws MiExcepcion Si hay algún error durante la actualización
     */
    private static void probarActualizacion(LibroDAO libroDAO) throws MiExcepcion {
        System.out.println("\n=== Prueba de Actualización ===");
        
        // Obtenemos un libro existente
        String isbn = "9788401352836"; // ISBN de "Don Quijote de la Mancha"
        Libro libro = libroDAO.obtenerPorIsbn(isbn);
        
        if (libro != null) {
            // Mostramos el libro antes de la actualización
            System.out.println("Libro antes de actualizar:");
            System.out.println("  " + libro);
            
            // Modificamos algunos datos del libro
            libro.setNumPaginas(1300);
            libro.setPrecio(29.99);
            libro.addGenero("Literatura española");
            
            // Actualizamos el libro en la base de datos
            boolean resultado = libroDAO.actualizar(libro);
            
            // Mostramos el resultado
            System.out.println("Actualización completa: " + (resultado ? "Exitosa" : "Fallida"));
            
            // Consultamos el libro actualizado
            Libro libroActualizado = libroDAO.obtenerPorIsbn(isbn);
            
            // Mostramos el libro después de la actualización
            System.out.println("Libro después de actualizar:");
            System.out.println("  " + libroActualizado);
            
            // Actualizamos solo algunos campos del libro
            Document campos = new Document();
            campos.append("editorial", "Penguin Clásicos");
            campos.append("disponible", false);
            
            // Actualizamos los campos en la base de datos
            boolean resultadoCampos = libroDAO.actualizarCampos(isbn, campos);
            
            // Mostramos el resultado
            System.out.println("Actualización de campos: " + (resultadoCampos ? "Exitosa" : "Fallida"));
            
            // Consultamos el libro actualizado
            libroActualizado = libroDAO.obtenerPorIsbn(isbn);
            
            // Mostramos el libro después de la actualización de campos
            System.out.println("Libro después de actualizar campos:");
            System.out.println("  " + libroActualizado);
        } else {
            System.out.println("No se encontró un libro con ISBN " + isbn + " para actualizar");
        }
    }
    
    /**
     * Prueba la eliminación de libros en la base de datos.
     * 
     * @param libroDAO Objeto DAO para realizar operaciones con libros
     * @throws MiExcepcion Si hay algún error durante la eliminación
     */
    private static void probarEliminacion(LibroDAO libroDAO) throws MiExcepcion {
        System.out.println("\n=== Prueba de Eliminación ===");
        
        // Creamos un libro para eliminar
        Libro libroEliminar = new Libro(
                "9788433920638",
                "La metamorfosis",
                "Franz Kafka",
                1915,
                "Alianza Editorial",
                132,
                Arrays.asList("Novela corta", "Ficción absurda", "Literatura existencialista"),
                true,
                12.75
        );
        
        // Insertamos el libro en la base de datos
        boolean resultadoInsercion = libroDAO.insertar(libroEliminar);
        
        // Mostramos el resultado de la inserción
        System.out.println("Inserción del libro a eliminar: " + (resultadoInsercion ? "Exitosa" : "Fallida"));
        
        // Verificamos que el libro existe
        String isbn = "9788433920638"; // ISBN de "La metamorfosis"
        Libro libro = libroDAO.obtenerPorIsbn(isbn);
        
        if (libro != null) {
            // Mostramos el libro a eliminar
            System.out.println("Libro a eliminar:");
            System.out.println("  " + libro);
            
            // Eliminamos el libro de la base de datos
            boolean resultadoEliminacion = libroDAO.eliminar(isbn);
            
            // Mostramos el resultado
            System.out.println("Eliminación: " + (resultadoEliminacion ? "Exitosa" : "Fallida"));
            
            // Verificamos que el libro ya no existe
            Libro libroEliminado = libroDAO.obtenerPorIsbn(isbn);
            
            if (libroEliminado == null) {
                System.out.println("El libro con ISBN " + isbn + " ya no existe en la base de datos");
            } else {
                System.out.println("¡Error! El libro con ISBN " + isbn + " todavía existe en la base de datos");
            }
        } else {
            System.out.println("No se encontró un libro con ISBN " + isbn + " para eliminar");
        }
    }
    
    /**
     * Prueba consultas avanzadas en la base de datos.
     * 
     * @param libroDAO Objeto DAO para realizar operaciones con libros
     * @throws MiExcepcion Si hay algún error durante las consultas
     */
    private static void probarConsultasAvanzadas(LibroDAO libroDAO) throws MiExcepcion {
        System.out.println("\n=== Prueba de Consultas Avanzadas ===");
        
        // Insertamos algunos libros adicionales para las pruebas
        Libro libro3 = new Libro(
                "9788499089515",
                "El principito",
                "Antoine de Saint-Exupéry",
                1943,
                "Salamandra",
                96,
                Arrays.asList("Fábula", "Literatura infantil"),
                true,
                9.95
        );
        
        Libro libro4 = new Libro(
                "9780061120084",
                "To Kill a Mockingbird",
                "Harper Lee",
                1960,
                "HarperCollins",
                336,
                Arrays.asList("Novela", "Ficción legal", "Bildungsroman"),
                true,
                15.99
        );
        
        // Insertamos los libros en la base de datos
        libroDAO.insertar(libro3);
        libroDAO.insertar(libro4);
        
        // Consulta por autor
        System.out.println("\nLibros de Gabriel García Márquez:");
        List<Libro> librosPorAutor = libroDAO.obtenerPorAutor("Gabriel García Márquez");
        for (Libro libro : librosPorAutor) {
            System.out.println("  " + libro.getTitulo() + " (" + libro.getAnioPublicacion() + ")");
        }
        
        // Consulta por género
        System.out.println("\nLibros del género 'Novela':");
        List<Libro> librosPorGenero = libroDAO.obtenerPorGenero("Novela");
        for (Libro libro : librosPorGenero) {
            System.out.println("  " + libro.getTitulo() + " - " + libro.getAutor());
        }
        
        // Consulta por disponibilidad
        System.out.println("\nLibros disponibles:");
        List<Libro> librosDisponibles = libroDAO.obtenerPorDisponibilidad(true);
        for (Libro libro : librosDisponibles) {
            System.out.println("  " + libro.getTitulo() + " - " + libro.getPrecio() + "€");
        }
        
        // Consulta por rango de precio
        System.out.println("\nLibros con precio entre 10€ y 20€:");
        List<Libro> librosPorPrecio = libroDAO.obtenerPorRangoPrecio(10.0, 20.0);
        for (Libro libro : librosPorPrecio) {
            System.out.println("  " + libro.getTitulo() + " - " + libro.getPrecio() + "€");
        }
    }
}
```

### Archivo `pom.xml` (para Maven)

**Descripción**: Este archivo de configuración XML define las dependencias del proyecto para Maven, incluyendo el driver de MongoDB para Java. Maven se encargará de descargar automáticamente las dependencias necesarias y configurar el classpath del proyecto.

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <groupId>com.example</groupId>
    <artifactId>mongodb-java</artifactId>
    <version>1.0-SNAPSHOT</version>
    
    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>
    
    <dependencies>
        <!-- MongoDB Java Driver -->
        <dependency>
            <groupId>org.mongodb</groupId>
            <artifactId>mongodb-driver-sync</artifactId>
            <version>4.9.1</version>
        </dependency>
        
        <!-- SLF4J API -->
        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-api</artifactId>
            <version>2.0.7</version>
        </dependency>
        
        <!-- SLF4J Simple (implementación) -->
        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-simple</artifactId>
            <version>2.0.7</version>
        </dependency>
    </dependencies>
    
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.10.1</version>
                <configuration>
                    <source>11</source>
                    <target>11</target>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```
