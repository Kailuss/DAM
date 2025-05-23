# **Chuleta 3.** <br>PostgreSQL ORDB, <br>JSON y MongoDB

## PostgreSQL ORDB - Tipos y Tablas

```sql
-- Crear tipo compuesto
CREATE TYPE direccion AS (
    calle VARCHAR(100),
    ciudad VARCHAR(50),
    codigo_postal VARCHAR(10)
);

-- Crear tabla con tipo compuesto
CREATE TABLE personas (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    dir direccion,
    fecha_nacimiento DATE
);

-- Insertar datos con tipo compuesto
INSERT INTO personas (nombre, dir, fecha_nacimiento)
VALUES ('Juan Pérez', ROW('Calle Mayor 10', 'Madrid', '28001'), '1990-05-15');

-- Consultar datos de tipo compuesto
SELECT nombre, (dir).calle, (dir).ciudad FROM personas;

-- Herencia de tablas
CREATE TABLE empleados (
    salario DECIMAL(10,2),
    departamento VARCHAR(50)
) INHERITS (personas);

-- Consulta con herencia
SELECT * FROM personas; -- Incluye empleados
SELECT * FROM ONLY personas; -- Solo personas, no empleados

-- Arrays
CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    etiquetas VARCHAR[]
);

-- Insertar con arrays
INSERT INTO productos (nombre, etiquetas)
VALUES ('Laptop', ARRAY['electrónica', 'portátil', 'trabajo']);

-- Consultar arrays
SELECT nombre, etiquetas[1] FROM productos; -- Primer elemento
SELECT nombre FROM productos WHERE 'electrónica' = ANY(etiquetas); -- Contiene valor
```

## PostgreSQL ORDB - JDBC

```java
// Mapear tipo compuesto a clase Java
public class Direccion {
    private String calle;
    private String ciudad;
    private String codigoPostal;
    
    // Constructor, getters, setters...
}

// Leer tipo compuesto
try (Connection conn = DriverManager.getConnection(url, usuario, password);
     Statement stmt = conn.createStatement();
     ResultSet rs = stmt.executeQuery("SELECT id, nombre, dir FROM personas")) {
    
    while (rs.next()) {
        int id = rs.getInt("id");
        String nombre = rs.getString("nombre");
        
        // Obtener tipo compuesto como PGobject
        PGobject pgObj = (PGobject) rs.getObject("dir");
        String dirStr = pgObj.getValue(); // (calle,ciudad,codigo_postal)
        
        // Parsear manualmente o usar biblioteca
        // Ejemplo simplificado:
        String[] parts = dirStr.substring(1, dirStr.length() - 1).split(",");
        Direccion dir = new Direccion(parts[0], parts[1], parts[2]);
    }
}

// Leer array
try (Connection conn = DriverManager.getConnection(url, usuario, password);
     Statement stmt = conn.createStatement();
     ResultSet rs = stmt.executeQuery("SELECT id, nombre, etiquetas FROM productos")) {
    
    while (rs.next()) {
        int id = rs.getInt("id");
        String nombre = rs.getString("nombre");
        
        // Obtener array
        Array array = rs.getArray("etiquetas");
        String[] etiquetas = (String[]) array.getArray();
        
        for (String etiqueta : etiquetas) {
            System.out.println(etiqueta);
        }
    }
}
```

## JSON con Jackson

```java
// Dependencia Maven
// <dependency>
//     <groupId>com.fasterxml.jackson.core</groupId>
//     <artifactId>jackson-databind</artifactId>
//     <version>2.13.0</version>
// </dependency>

// Clase POJO
public class Producto {
    private Long id;
    private String nombre;
    private Double precio;
    private List<String> categorias;
    
    // Constructor, getters, setters...
}

// Objeto a JSON (serialización)
ObjectMapper mapper = new ObjectMapper();

// Objeto simple a JSON
Producto producto = new Producto(1L, "Laptop", 999.99, 
                                Arrays.asList("Electrónica", "Computadoras"));
String json = mapper.writeValueAsString(producto);
// Resultado: {"id":1,"nombre":"Laptop","precio":999.99,"categorias":["Electrónica","Computadoras"]}

// Escribir a archivo
mapper.writeValue(new File("producto.json"), producto);

// Lista a JSON
List<Producto> productos = Arrays.asList(
    new Producto(1L, "Laptop", 999.99, Arrays.asList("Electrónica")),
    new Producto(2L, "Smartphone", 599.99, Arrays.asList("Electrónica"))
);
String jsonLista = mapper.writeValueAsString(productos);

// JSON a objeto (deserialización)
String json = "{\"id\":1,\"nombre\":\"Laptop\",\"precio\":999.99,\"categorias\":[\"Electrónica\"]}";
Producto producto = mapper.readValue(json, Producto.class);

// JSON a lista
String jsonLista = "[{\"id\":1,\"nombre\":\"Laptop\"},{\"id\":2,\"nombre\":\"Smartphone\"}]";
List<Producto> productos = mapper.readValue(jsonLista, 
                                          new TypeReference<List<Producto>>(){});

// Leer de archivo
Producto producto = mapper.readValue(new File("producto.json"), Producto.class);
```

## MongoDB con Java

```java
// Dependencia Maven
// <dependency>
//     <groupId>org.mongodb</groupId>
//     <artifactId>mongodb-driver-sync</artifactId>
//     <version>4.4.0</version>
// </dependency>

// Conexión a MongoDB
MongoClient mongoClient = MongoClients.create("mongodb://localhost:27017");
MongoDatabase database = mongoClient.getDatabase("tienda");
MongoCollection<Document> collection = database.getCollection("productos");

// Insertar documento
Document producto = new Document("nombre", "Laptop")
                        .append("precio", 999.99)
                        .append("stock", 10)
                        .append("categorias", Arrays.asList("Electrónica", "Computadoras"))
                        .append("especificaciones", new Document("ram", "16GB")
                                                       .append("procesador", "Intel i7"));
collection.insertOne(producto);

// Insertar múltiples documentos
List<Document> productos = Arrays.asList(
    new Document("nombre", "Smartphone").append("precio", 599.99),
    new Document("nombre", "Tablet").append("precio", 399.99)
);
collection.insertMany(productos);

// Buscar documentos
// Todos los documentos
FindIterable<Document> todosProductos = collection.find();
for (Document doc : todosProductos) {
    System.out.println(doc.toJson());
}

// Con filtro
Document filtro = new Document("precio", new Document("$gt", 500));
FindIterable<Document> productosFiltrados = collection.find(filtro);

// Con proyección (seleccionar campos)
Document proyeccion = new Document("nombre", 1).append("precio", 1).append("_id", 0);
FindIterable<Document> productosProyectados = collection.find().projection(proyeccion);

// Actualizar documento
Document filtroUpdate = new Document("nombre", "Laptop");
Document update = new Document("$set", new Document("precio", 899.99));
collection.updateOne(filtroUpdate, update);

// Eliminar documento
Document filtroDelete = new Document("nombre", "Tablet");
collection.deleteOne(filtroDelete);

// Agregaciones
List<Document> pipeline = Arrays.asList(
    new Document("$match", new Document("precio", new Document("$gt", 500))),
    new Document("$group", new Document("_id", "$categorias")
                              .append("precioPromedio", new Document("$avg", "$precio")))
);
AggregateIterable<Document> resultado = collection.aggregate(pipeline);
for (Document doc : resultado) {
    System.out.println(doc.toJson());
}
```

## MongoDB con POJOs

```java
// Configuración para mapeo POJO
CodecRegistry pojoCodecRegistry = fromRegistries(MongoClientSettings.getDefaultCodecRegistry(),
                                                fromProviders(PojoCodecProvider.builder().automatic(true).build()));
MongoClientSettings settings = MongoClientSettings.builder()
                                                 .codecRegistry(pojoCodecRegistry)
                                                 .build();
MongoClient mongoClient = MongoClients.create(settings);
MongoDatabase database = mongoClient.getDatabase("tienda");
MongoCollection<Producto> collection = database.getCollection("productos", Producto.class);

// Insertar POJO
Producto producto = new Producto(null, "Laptop", 999.99, Arrays.asList("Electrónica"));
collection.insertOne(producto);

// Buscar como POJO
Producto encontrado = collection.find(eq("nombre", "Laptop")).first();

// Actualizar POJO
collection.updateOne(eq("nombre", "Laptop"), 
                    set("precio", 899.99));

// Buscar con filtros complejos
List<Producto> productos = collection.find(
                             and(gt("precio", 500), 
                                 in("categorias", "Electrónica")))
                           .into(new ArrayList<>());
```
