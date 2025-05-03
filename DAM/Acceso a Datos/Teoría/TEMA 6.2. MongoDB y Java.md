---
tags:
  - DAM
  - AD
cssclasses:
  - dam-ad
  - table-compact-clean
banner: "![[ad.jpg]]"
banner_y: 0.32
---

# **TEMA 6.2.** <br>Bases de Datos Documentales. <br>MongoDB y Java 

## 1. Driver y configuración  

MongoDB ofrece dos drivers para Java:  

- **Java Sync** (síncrono, el usado en este curso).  
- **Java Reactive Streams** (asíncrono).  

**Configuración con Maven.**  

```xml
<dependency>
    <groupId>org.mongodb</groupId>
    <artifactId>mongodb-driver-sync</artifactId>
    <version>5.2.0</version>
</dependency>
```  

**Sin Maven.** Se requieren múltiples JARs (`mongodb-driver-sync`, `bson`, `log4j`, etc.).  

## 2. Clases básicas  

### 2.1. **Document**

Representa un documento MongoDB. Métodos clave:  

- `Document.parse(String json)`: Crea un documento desde JSON.  
- `append(String key, Object value)`: Añade una propiedad.  
- `getList(String key, Class<T>)`: Obtiene un array como lista.  
- `toJson()`: Convierte el documento a JSON.  

**Ejemplo.**  

```java
Document doc = new Document("nombre", "Joan")
    .append("edad", 25)
    .append("cursos", Arrays.asList("DAM", "DAW"));
```  

### 2.2. **Conexión**

```java
String url = "mongodb://usuario:contraseña@servidor:27017/?authSource=admin";
try (MongoClient client = MongoClients.create(url)) {
    MongoDatabase db = client.getDatabase("basedatos");
}
```  

## 3. POJOs y Codecs  

Para mapear documentos a objetos Java:  

```java
CodecRegistry pojoCodecRegistry = PojoCodecProvider.builder()
    .register("paquete.modelo")
    .build();

MongoCollection<Alumno> alumnos = db.getCollection("alumnos", Alumno.class)
    .withCodecRegistry(pojoCodecRegistry);
```  

**Requisitos del POJO.**  
- Atributos con nombres coincidentes a los campos del documento.  
- Getters/setters y constructor sin parámetros.  

## 4. Operaciones CRUD  

### 4.1. **Consultas  **
- **Filtros.** Usan la clase `Filters`.  

  ```java
  Bson filtro = and(eq("nombre", "Joan"), gt("edad", 20));
  FindIterable<Document> resultados = coleccion.find(filtro);
  ```  

- **Proyecciones.**  

  ```java
  Bson proyeccion = fields(include("nombre", "edad"), excludeId());
  ```  

- **Ordenación.**  

  ```java
  Bson orden = orderBy(ascending("nombre"), descending("edad"));
  ```  

### 4.2. **Inserciones**

```java
coleccion.insertOne(new Document("nombre", "Ana"));
coleccion.insertMany(List.of(doc1, doc2));
```  

### 4.3. **Actualizaciones**

```java
Bson actualizacion = combine(set("edad", 26), currentDate("ultimaModificacion"));
coleccion.updateOne(eq("nombre", "Joan"), actualizacion);
```  

### 4.4. **Eliminaciones**

```java
coleccion.deleteMany(eq("curso", "DAM"));
```  

## 5. Aggregation Pipeline  

**Ejemplo.** Agrupar y calcular totales.  

```java
List<Bson> etapas = Arrays.asList(
    match(eq("tipo", "venta")),
    group("$producto", sum("total", "$cantidad")),
    sort(descending("total"))
);

coleccion.aggregate(etapas).into(resultados);
```  

**Etapas comunes.**  
- `match`: Filtra documentos.  
- `group`: Agrupa y aplica operaciones (suma, promedio).  
- `sort`: Ordena resultados.  
- `out`: Guarda resultados en una nueva colección.  

## 6. Clientes recomendados  
- **MongoDB Compass.** Interfaz gráfica oficial.  
- **mongosh.** Consola interactiva.  

> [!note] Nota
> Para desarrollo, se recomienda usar el driver síncrono y POJOs con Codecs para un código más limpio y mantenible. 
