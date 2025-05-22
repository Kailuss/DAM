---
tags: [AD, DAM]
cssclasses:
  - dam-ad
  - table-compact-clean
banner: "![[ad.jpg]]"
banner_y: 0.32
number headings: max 4, _.1.
---

# **TEMA 6.2.** <br>Bases de Datos Documentales. <br>MongoDB y Java 

## 1. Driver

MongoDB proporciona dos drivers para acceder a la base de datos desde Java:

- **Java Sync:** Permite trabajar de forma síncrona con la base de datos. Es el que utilizaremos.
- **Java Reactive Streams:** Permite trabajar con la base de datos de forma asíncrona.

La mejor manera de añadir el driver de MongoDB a nuestro proyecto es utilizando Maven. Tendremos que añadir las siguientes dependencias al pom (o las versiones posteriores si las hay):

```xml
<dependency>
    <groupId>org.mongodb</groupId>
    <artifactId>mongodb-driver-sync</artifactId>
    <version>5.2.0</version>
</dependency>
<dependency>
    <groupId>org.apache.logging.log4j</groupId>
    <artifactId>log4j-slf4j2-impl</artifactId>
    <version>2.24.3</version>
</dependency>
```

Si no queréis utilizar Maven, debéis tener cuidado, ya que además del jar del driver necesitamos algunos más. Podéis descargarlos desde Maven Repository o desde la página del curso.

- mongodb-driver-sync-5.3.0.jar
- mongodb-driver-core-5.3.0.jar
- bson-5.3.0.jar
- bson-record-codec-5.3.0.jar
- slf4j-api-2.0.16.jar
- log4j-slf4j2-impl-2.24.3.jar
- log4j-api-2.24.3.jar
- log4j-core-2.24.3.jar

En la página de MongoDB podéis encontrar mucha información sobre cómo utilizar el driver:

<https://www.mongodb.com/docs/drivers/java/sync/current/>

## 2. Clases básicas

### 2.1. **Bson**

Es la interfaz que implementa la clase `Document` y todas sus especializaciones. Todos los métodos que nos permiten establecer filtros, proyecciones y ordenaciones devuelven objetos que implementan esta interfaz. Nos basta con saber que existe.

### 2.2. **Document**

La clase `Document` representa uno de los documentos de la colección. Implementa la clase `Bson`. Necesitaremos crear documentos para especificar filtros y proyecciones. Tiene tres constructores:

- Crea el documento vacío:

	```java
    Document nuevo = new Document();
    ```

- Crea el documento con una propiedad. El primer argumento es el nombre de la propiedad y el segundo el valor:

	```java
    Document nuevo = new Document(String, Object);
    ```

- Crea el documento y lo inicializa con las propiedades definidas en el mapa:

	```java
    HashMap <String, Object> propiedades=new HashMap<>();
    propietades.put("nombre", "Yo");
    propietades.put("apellidos", "Mismo");
    Document nuevo = new Document(propietades); [cite: 18]
    ```

Podemos crear un documento con el método `parse` pasándole una cadena con el JSON:

```java
Document nuevo = Document.parse("{\"nombre\":\"Yo\",\"apellidos\":\"Mismo\"}");
```

Para documentos complejos, si tenemos un POJO con los datos, podemos configurar la conexión para utilizarlo. Lo veremos más adelante.

Algunos de los métodos de los que dispone la clase `Document`:

- `.append(String nombre, Object valor)`: Añade la propiedad al documento. Devuelve la referencia al documento, aunque no hace falta recogerla.

	```java
    document.append("ciclo", "DAM");
    ```

- `.get(String nombrePropiedad)`: Devuelve el objeto asociado a la propiedad. Devuelve un valor de tipo `Object`.

	```java
    Object ciclo = document.get("ciclo");
    ```

	También tenemos `getBoolean()`, `getInteger()`, `getString()`, que devuelven el valor en ese formato si es posible.

	```java
    String ciclo = document.getString("ciclo");
    ```

- `.getList(String nombrePropiedad, Class<Elementos>.class)`: Devuelve el array que contiene la propiedad del documento como una lista. El primer parámetro es el campo del documento y el segundo el tipo de los elementos de la lista.

	```java
    MongoCollection<Document> students = database.getCollection("students");
    Document doc = students.find().first();
    List<Integer> grades = doc.getList("grades", Integer.class);
    ```

- `.toJson()`: Devuelve la cadena con el JSON del documento.

	```java
    String json = document.toJson();
    ```

Para representar un array dentro de un documento debemos utilizar cualquier implementación de `List`.

```java
ArrayList datos=new ArrayList();
datos.add("v3.2");
datos.add(3.0);
datos.add(true);
document.append("lista", datos);
```

Si queremos incluir un objeto como valor para una propiedad de un documento, debemos crear un documento nuevo que represente este objeto e incluirlo como propiedad:

Java

```java
Document coordenadas=new Document();
coordenadas.put("lat", 40.45);
coordenadas.put("lng", -77.85);
document.put("coordinates", coordenadas);
```

## 3. Conexión al servidor

El servidor necesita estar configurado para aceptar conexiones desde el exterior. Para ello se debe modificar el fichero `mongod.conf` y poner la propiedad `bindIP = 0.0.0.0`. El objeto `MongoClient` representa la conexión con el servidor. En realidad es un pool de conexiones.

Para conectar la aplicación al servidor, la manera más fácil es utilizando la cadena de conexión. Si la tenéis configurada en Compass la podéis copiar desde allí. Esta cadena de conexión debe tener el formato:

`mongodb://usuario:password@servidor:port/?authSource=admin`

Debemos especificar qué base de datos se utilizará para la autenticación con el parámetro `authSource=admin`.

Utilizamos el método static `create` de la clase `MongoClients` para obtener el cliente pasándole un String con la URL de conexión:

```java
String uri = "mongodb://alumno:seCret_25@daw.paucasesnovescifp.cat:27017/?authSource=admin";
try (MongoClient mongoClient = MongoClients.create(uri)) { }
```

## 4. Bases de datos

Una vez tenemos la instancia de `MongoClient` la utilizaremos para obtener acceso a la base de datos representada por la clase `MongoDatabase`:

```java
MongoDatabase db = mongoClient.getDatabase("pruebas");
```

Métodos de la clase `MongoDatabase`:

- `.getCollection("nombre")`: Recupera la colección que tiene por nombre el que recibe como argumento:

	```java
    MongoCollection<Document> col = db.getCollection("orders");
    ```

- `.createCollection("newCollection")`: Podemos crear una colección pasándole el nombre como argumento:

	```java
    db.createCollection("newCollection");
    ```

- `.drop()`: Elimina la base de datos del servidor, con todo lo que contiene:

	```java
    db.drop();
    ```

- `.getName()`: Devuelve el nombre de la base de datos.

	```java
    String nom = db.getName();
    ```

- `.listCollections()`: Devuelve un iterador para las colecciones de la base de datos. Para cada una tendremos un documento con información sobre la colección.

	Java

	```java
    ListCollectionsIterable<Document> colecciones = database.listCollections();
    for (Document document : colecciones) {
        System.out.println(document.toJson());
    }
    ```

- `.listCollectionNames()`: Devuelve un iterador para las colecciones de la base de datos. Para cada una tendremos un String con el nombre de la colección.

	```java
    ListCollectionNamesIterable colecciones = database.listCollectionNames();
    for (String nom : colecciones) {
        System.out.println(nom);
    }
    ```

### 4.1. **Ejemplo completo**

```java
String uri = "mongodb://alumno:seCret_25@daw.paucasesnovescifp.cat:27017/?authSource=admin";
try (MongoClient mongoClient = MongoClients.create(uri)) {
    MongoDatabase db = mongoClient.getDatabase("pruebas");
    ListCollectionsIterable<Document> colecciones = db.listCollections();
    for (Document document : colecciones) {
        System.out.println(document.toJson());
    }
    MongoCollection<Document> col = db.getCollection("orders");
}
```

## 5. Iteradores

La mayoría de operaciones con el driver nos devolverán un iterador. Se pueden utilizar con el `for`: como hemos visto en el ejemplo anterior.

```java
ListCollectionsIterable<Document> colecciones = database.listCollections();
for (Document document : colecciones) {
    System.out.println(document.toJson());
}
```

Mongo dispone de toda una jerarquía de herencia con distintas interfaces que implementan iteradores. La raíz de esta jerarquía es `MongoIterable`. El método que utilizaremos más de esta interfaz es:

- `.into(Collection)`: Guarda el contenido del iterador dentro de una subclase de `Collection`, por ejemplo `List` o `ArrayList`.

	Java

	```java
    ArrayList<Document> documents = new ArrayList<>();
    database.listCollections().into(documents);
    ```

La subinterfaz `AggregateIterable` define un método que tendremos que utilizar cuando la última etapa de una agregación sea `out` o `merge`:

- `.toCollection()`: Si la última etapa es `merge` incluye los documentos dentro de la colección, en cambio si es `out` crea la colección y pone los documentos.

## 6. POJO's

Seguramente utilizaremos objetos para tratar la información que contienen los documentos. Tanto la base de datos como las colecciones se pueden configurar de manera que en lugar de utilizar documentos utilicen POJO's. Necesitaremos utilizar una serie de clases para hacerlo:

- **Codecs:** Los códecs son clases que permiten el mapeo entre documentos y objetos. Se pueden configurar, pero para este curso nos bastará con la configuración por defecto que busca los mismos nombres de propiedades en los documentos y en los objetos.
- **CodecProvider:** Es el que crea las instancias de los códecs.
- **CodecRegistry:** Es una colección de instancias de códecs. El driver los utilizará para convertir de Bson a POJO y al revés.

Si solo necesitamos la configuración por defecto, que asocia campos de los documentos con atributos de los POJOs utilizando el nombre, nos basta el código siguiente:

```java
try (MongoClient mongoClient = MongoClients.create(uri)) {
    CodecProvider pojoCodecProvider = PojoCodecProvider.builder().automatic(true).build();
    CodecRegistry pojoCodecRegistry = fromRegistries(getDefaultCodecRegistry(), fromProviders(pojoCodecProvider));

    MongoDatabase database = mongoClient.getDatabase("pruebas");
    MongoCollection<Flower> collection = database.getCollection("flowers", Flower.class).withCodecRegistry(pojoCodecRegistry);
}
```

**Importante:** Este codec comprueba si la clase tiene un atributo con el mismo nombre que una propiedad del documento de manera *caseSensitive*. La única excepción es la propiedad `_id`, que se mapea a `id`, sin el underscore.

La configuración se puede hacer en la base de datos, y afectará a todas sus colecciones:

```java
MongoDatabase database = mongoClient.getDatabase("pruebas").withCodecRegistry(pojoCodecRegistry);
MongoCollection<Flower> collection = database.getCollection("flowers", Flower.class);
```

o únicamente a una colección:

```java
MongoDatabase database = mongoClient.getDatabase("pruebas");
MongoCollection<Flower> collection = database.getCollection("flowers", Flower.class).withCodecRegistry(pojoCodecRegistry);
```

Se debe elegir una de las dos opciones.

La mayoría de métodos están sobrecargados, es decir, tienen más de una versión. Por ejemplo, si quiero utilizar una colección recuperando `Document`s llamaré `getCollection` solo con el nombre de la colección:

```java
MongoCollection<Document> col = db.getCollection("orders");
```

En cambio, si quiero utilizar la colección con POJOs tendré que utilizar `getCollection` con dos parámetros, el nombre de la colección y la clase del POJO:

```java
MongoCollection<Flower> collection = database.getCollection("flowers", Flower.class);
```

## 7. Colecciones

La colección se representa como una instancia de la clase `MongoCollection` que contiene objetos `org.bson.Document`. El único método que tiene para trabajar con colecciones es:

- `.drop()`: Elimina la colección de la base de datos.

	```java
    col.drop();
    ```

### 7.1. **Consultas**

La clase `MongoCollection` proporciona los siguientes métodos para consultar datos sobre la colección o recuperar documentos de la colección. Más adelante hablaremos de los filtros de datos.

- `.countDocuments()`: Devuelve el número de documentos de la colección:

	```java
    long cantidad = col.countDocuments();
    ```

- `.countDocuments(Bson filtro)`: Devuelve el número de documentos de la colección que cumplen el filtro:

	```java
    Bson query = eq("nombre", "Juan");
    long cantidad = col.countDocuments(query);
    ```

- `.find()`: Devuelve todos los documentos de la colección.

	```java
    MongoCollection<Document> bios= database.getCollection("bios");
    FindIterable<Document> documents = bios.find();
    for (Document document : documents) {
     System.out.println("document.toJson() = " + document.toJson());
    }
    ```

	Si lo hemos configurado para devolver POJOs el `FindIterable` debería estar parametrizado con la clase del POJO.

	```java
    MongoCollection<Flower> bios = database.getCollection("flowers", Flower.class).withCodecRegistry(pojoCodecRegistry);
    FindIterable<Flower> documents = bios.find();
    ```

- `.find(Bson filtro)`: Devuelve todos los documentos de la colección que cumplen el filtro.

	```java
    MongoCollection<Document> bios = database.getCollection("bios");
    Bson filter = eq("name.first","John");
    FindIterable<Document> documents = bios.find(filter);
    ```

- `.find().into(Collection lista)`, `.find(Bson filtro).into(Collection lista)`: Nos permite poner directamente el contenido del `FindIterable` dentro de un objeto de cualquier subclase de `Collection`:

	```java
    List<Flower> flowers = new ArrayList<>();
    collection.find().into(flowers);
    ```

- `distinct(String nombreCampo, Class<T> claseResultado)`: Devuelve los distintos valores del campo especificado. Devuelve los valores como objetos de la clase `claseResultado`.

	```java
    DistinctIterable<String> nombres = collection.distinct("nombre", String.class);
    for(String nombre : nombres) {
        System.out.println(nombre);
    }
    ```

- `distinct(String nombreCampo, Bson filtro, Class<T> claseResultado)`: Devuelve los distintos valores del campo especificado, pero solo tiene en cuenta los documentos que satisfacen el filtro.

	```java
    Bson filter = eq("codigoPostal","07865");
    DistinctIterable<String> nombres = collection.distinct("nombre", filter, String.class);
    for(String nombre : nombres) {
        System.out.println(nombre);
    }
    ```

#### 7.1.1. Filters

Podemos filtrar los datos que nos devuelve una consulta a la base de datos. Un filtro vendría a ser un `WHERE` de SQL.

La clase `com.mongodb.client.model.Filters` proporciona métodos estáticos para todos los operadores que podemos utilizar en las consultas que podemos hacer a la base de datos. Cada uno de estos métodos devuelve un objeto `Bson` que podemos pasar como argumento a los métodos `find`, `deleteOne`, `deleteMany`, `updateOne`, `updateMany` y a la etapa `match` de la agregación.

Normalmente se hace una importación estática de los métodos de la clase Filter:

import static com.mongodb.client.model.Filters.*;

##### Operadores relacionales

- `eq(String campo, <T> valor)`: igual.

	```java
    Bson iguales = eq("qty", 5);
    FindIterable<Document> resultado = collection.find(iguales);
    ```

- `ne(String campo, <T> valor)`: distinto.

	```java
    Bson distintosDe = ne("qty", 5);
    FindIterable<Document> resultado = collection.find(distintosDe);
    ```

- `gt(String campo, <T> valor)`, `gte(String campo, <T>valor)`: mayor, mayor o igual.

	```java
    Bson mayores = gt("qty", 5);
    ```

- `lt(String campo, <T> valor)`, `lte(String campo, <T> valor)`: menor, menor o igual.

	```java
    Bson menoresOIguales = lte("qty", 5);
    ```

- `in(String campo, <T> ... valores)` o `in(String campo, List<T> lista)`: El valor del campo se encuentra entre los valores o dentro de la lista.

	```java
    Bson filter = in("name.first", "John", "Guido");
    // o bien
    Bson filter = in("name.first", List.of("John", "Guido"));
    ```

- `nin(String campo, <T> ... valores)` o `nin(String campo, List<T> lista)`: El valor del campo no se encuentra entre los valores especificados o dentro de la lista.

	```java
    Bson filter = nin("name.first", "John", "Guido");
    Bson filter = nin("name.first", List.of("John", "Guido"));
    ```

##### Operadores lógicos

- `and(Bson... filtro)` o `and(List<Bson> filtros)`: Devuelve los documentos que cumplen todos los filtros. El ejemplo devuelve todos los documentos con una nota mayor o igual a 6 del curso S1P.

	```java
    Bson filter = and(gte("nota", 6), eq("curso", "S1P"));
    // o bien
    List<Bson> filters = List.of(gte("nota", 6), eq("curso", "S1P"));
    Bson filter = and(filters);
    ```

- `or(Bson... filtro)` o `or(List<Bson> filtros)`: Devuelve los documentos que cumplen al menos uno de los filtros. El ejemplo devuelve todos los documentos del curso S1W o del curso S1P.

	```java
    Bson filter = or(eq("curso", "S1W"), eq("curso", "S1P"));
    // o bien
    List<Bson> filters = List.of(eq("curso", "S1W"), eq("curso", "S1P"));
    Bson filter = or(filters);
    ```

- `not(Bson filtro)`: Devuelve los documentos que no cumplen el filtro. El ejemplo devuelve todos los documentos que no son del curso S1W.

	```java
    Bson filter = not(eq("curso", "S1W"));
    ```

- `nor(Bson... filtros)` o `nor(List<Bson> filtros)`: Devuelve todos los documentos que no cumplen ninguno de los filtros. El ejemplo devolverá todos los documentos que no sean ni de S1W ni de S1P.

	```java
    Bson filter = nor(eq("curso", "S1W"), eq("curso", "S1P"));
    // o bien
    List<Bson> filters = List.of(eq("curso", "S1W"), eq("curso", "S1P"));
    Bson filter = nor(filters);
    ```

##### Operadores sobre la estructura de los documentos

- `exists(String nombreCampo)`, `exists(String nombreCampo, boolean existe)`: Permite filtrar los documentos que tengan un determinado campo. Recordemos que nada obliga a que todos los documentos de una colección tengan la misma estructura. El booleano nos permite filtrar documentos que no tengan el campo solicitado.

	```java
    // Todos los alumnos que tengan nota
    Bson filter = exists("nota");
    // Todos los alumnos que no tengan nota
    Bson filter = exists("nota", false);
    ```

##### Operadores sobre arrays

Todos estos operadores devuelven documentos que tengan el campo que se pide y que este sea un array.

- `all(String nombreCampo, <T> ... valores)` o `all(String nombreCampo, List<T> lista)`: Devuelve todos los documentos cuyo array contenga todos los valores especificados o que contenga la lista.

	```java
    Bson filter = all("modulos","SPADD", "SPPRO");
    // o bien
    List<String> buscados = List.of("SPADD", "SPPRO");
    Bson filter = all("modulos", buscados);
    ```

- `elemMatch(String nombreCampo, Bson filtro)`: Devuelve todos los documentos donde el array contenga al menos un documento que coincida con el filtro. El ejemplo devuelve todos los documentos donde el array `notas` contenga al menos un documento con el campo `SPPRO` con valor mayor o igual a 5.

	```java
    Bson filter = elemMatch("notas",gte("SPPRO", 5));
    ```

	**Nota importante:** El filtro se aplica sobre el array. Esto quiere decir que el elemento del array debe tener un campo con el nombre que pasamos al filtro. Esto implica que no lo podemos utilizar en arrays planos del tipo `[1, 2, 3, 4]`.
- `size(String nombreCampo, int longitud)`: Devuelve todos los documentos donde el array tiene la longitud solicitada. El ejemplo devolverá todos los documentos con el array `notas` con 5 valores.

	```java
    Bson filter = size("notas", 5);
    ```

#### 7.1.2. Projections

Las proyecciones nos permiten determinar qué campos de los documentos queremos que nos devuelva la consulta. Vendría a ser la cláusula `SELECT` de SQL.

Las proyecciones se aplican al resultado del método `find` utilizando el método `projection`. La clase `com.mongodb.client.model.Projections` proporciona métodos estáticos para todos los operadores que podemos utilizar en las proyecciones que podemos hacer a la base de datos.

```java
collection.find().projection(include("nombre"));
```

Todos los métodos de esta clase devuelven un objeto `Bson` con las proyecciones especificadas.

##### Inclusión y exclusión de campos en la proyección

- `include(String ... campos)` o `include(List<String> campos)`: Muestra solo los campos del documento pasados como argumento. A no ser que se especifique lo contrario siempre se incluye `_id`.

	Java

	```java
    Bson projection = include("nombre", "apellidos");
    collection.find(filter).projection(projection);
    ```

- `exclude(String ... campos)` o `exclude(List<String> campos)`: Muestra todos los campos del documento excepto los pasados como argumento. A no ser que se especifique lo contrario siempre se incluye `_id`.

	```java
    Bson projection = exclude("nombre", "apellidos");
    collection.find(filter).projection(projection);
    ```

- `excludeId()`: Muestra todos los campos del documento excepto `_id`.

	```java
    Bson projection = excludeId();
    collection.find(filter).projection(projection);
    ```

##### Combinación de projecciones

- `fields(Bson ... projeccion)` o `fields(List<Bson> projeccion)`: Permite combinar diversas proyecciones:

	```java
    Bson projection = fields( include("nombre", "apellidos"), excludeId() );
    collection.find(filter).projection(projection);
    ```

##### Proyecciones de arrays

- `elemMatch(String nombreCampo, Bson filtros)`: Devuelve el primer elemento del array con el nombre especificado que satisface el filtro. El ejemplo mostrará todos los documentos de la colección y solo mostrará el contenido del array `awards` que tengan el campo `year` con valor 1975.

	```java
     Bson projection = Projections.elemMatch("awards", eq("year",1975));
     collection.find().projection(projection);
    ```

	**Nota importante:** El filtro se aplica sobre el array. Esto quiere decir que el elemento del array debe tener un campo con el nombre que pasamos al filtro. Esto implica que no lo podemos utilizar en arrays planos del tipo `[1, 2, 3, 4]`.
- `slice(String nombreCampo, int cantidad)`: Devuelve como máximo `cantidad` elementos del array. El ejemplo mostrará los dos primeros elementos del array `awards`.

	```java
     Bson projection = Projections.slice("contribs", 2);
     collection.find().projection(projection);
    ```

- `slice(String nombreCampo, int skip, int cantidad)`: Devuelve como máximo `cantidad` elementos del array obviando los `skip` primeros elementos. El ejemplo mostrará los elementos segundo y tercero del array `awards` si existen.

	Java

	```java
     Bson projection = Projections.slice("contribs", 1, 2);
     collection.find().projection(projection);
    ```

#### 7.1.3. Sorts

La clase `com.mongodb.client.model.Sorts` proporciona métodos estáticos para ordenar los resultados de la consulta. Se aplican al resultado del `find` o del `projections` si lo hay.

- `ascending(String... campos)` o `ascending(List<String> campos)`: ordena el resultado de forma ascendente según los campos especificados.

	```java
    Bson ordenacion = ascending("apellidos", "nombre");
    collection.find().sort(ordenacion);
    // o bien
    Bson ordenacion = ascending(List.of("apellidos", "nombre"));
    collection.find().sort(ordenacion);
    ```

- `descending(String... campos)` o `descending(List<String> camps)`: ordena el resultado de forma descendente según los campos especificados.

	```java
    Bson ordenacion = descending("apellidos", "nombre");
    collection.find().sort(ordenacion);
    // o bien
    Bson ordenacion = descending(List.of("apellidos", "nombre"));
    collection.find().sort(ordenacion);
    ```

- `orderBy(Bson... campos)` o `orderBy(List<Bson> camps)`: Aplica los diferentes criterios de ordenación a los documentos devueltos por la búsqueda. Permite, por ejemplo, ordenar por un campo de forma ascendente y por otro de forma descendente.

	```java
    Bson ordenacion = orderBy(ascending("apellidos"), descending("nombre"));
    // o bien
    List<Bson> criterios = List.of(ascending("apellidos"), descending("nombre"));
    Bson ordenacion = orderBy(criterios);
    collection.find().sort(ordenacion);
    ```

#### 7.1.4. Ejemplo completo

```java
try (MongoClient mongoClient = MongoClients.create(uri)) {
    MongoDatabase database = mongoClient.getDatabase("pruebas");
    MongoCollection<Document> collection = database.getCollection("bios");

    Bson filter = size("contribs", 2);
    Bson projection = fields(include("name"), include("contribs"), excludeId());
    Bson ordenacion = orderBy(descending("name.last"));

    FindIterable<Document> resultado = collection.find(filter).projection(projection).sort(ordenacion);
    resultado.forEach(document -> {
        System.out.println(document.toJson());
    });
}
```

### 7.2. **Inserciones**

- `.insertOne(Document document)`: Inserta el documento en la colección:

	```java
    Document document = new Document("nombre", "Yo");
    collection.insertOne(document);
    ```

- `.insertMany(List<Document> documents)`: Inserta una lista de documentos en la base de datos:

	```java
    ArrayList<Document> documents = new ArrayList<>();
    documents.add(new Document("nombre", "Yo"));
    documents.add(new Document("nombre", "Tú"));
    collection.insertMany(documents);
    ```

### 7.3. **Modificaciones**

- `.replaceOne(Bson filtro, Document document)`: Reemplaza el primer documento que devuelve el filtro por el documento que recibe como parámetro.

	```java
    Bson filter = eq("nombre", "Yo");
    collection.replaceOne(filter, new Document("apellidos", "También"));
    ```

- `.updateOne(Bson filtro, Bson modificaciones)`: Modifica el primer documento que devuelve el filtro con las modificaciones especificadas. Utilizaremos los métodos static de la clase `Updates` para indicar los cambios que queremos hacer al documento. Más adelante los veremos. En el ejemplo utilizamos `set` para cambiar el valor del campo apellidos. Devuelve un objeto de la clase `UpdateResult` con el resultado de la operación.

	```java
	Bson filter = eq("apellidos", "También");
	Bson modification = set("apellidos", "Pons");
	collection.updateOne(filter, modification);
	```

- `.updateMany(Bson filtro, Bson modificaciones)`: Modifica los documentos que devuelve el filtro con las modificaciones especificadas. Devuelve un objeto de la clase `UpdateResult` con el resultado de la operación.

	```java
	Bson filter = eq("apellidos", "También");
	Bson modification = set("apellidos", "Pons");
	collection.updateMany(filter, modification);
	```

#### 7.3.1. Updates

La clase `com.mongodb.client.model.Updates` incluye métodos static que nos permiten especificar las modificaciones que queremos hacer al documento. Se suele hacer un `import static com.mongodb.client.model.Updates.*;` para utilizarlos más fácilmente.

- `set(String nombreCampo, <T> valor)`: Cambia el valor del campo por el que pasamos como segundo argumento. Si el campo no existe lo crea.

	```java
	Bson modification = set("apellidos", "Pons");
	collection.updateMany(filter, modification);
	```

- `unset(String nombreCampo)`: Elimina el campo del documento.

	```java
	Bson modification = unset("apellidos");
	collection.updateMany(filter, modification);
	```

- `inc(String nombreCampo, Number valor)`: Incrementa el campo el valor especificado. Si el campo no existe lo crea. Valor puede tener valores enteros, reales, positivos o negativos. El ejemplo incrementará el valor del campo 2 unidades.

	```java
	Bson modification = inc("resueltos", 2);
	collection.updateMany(filter, modification);
	```

- `mul(String nombreCampo, Number valor)`: Multiplica el valor del campo por el valor especificado. Si el campo no existe lo crea con valor cero. Valor puede tener valores enteros, reales, positivos o negativos. El ejemplo doblará el valor del campo.

	```java
	Bson modification = mul("resueltos", 2);
	collection.updateMany(filter, modification);
	```

- `currentDate(String nombreCampo)`: Modifica o crea el campo con el valor de la fecha actual.

	```java
	Bson modification = currentDate("actualizado");
	collection.updateMany(filter, modification);
	```

- `combine(Bson... modificaciones)` o `combine(List<Bson> modificaciones)`: Combina múltiples modificaciones.

	```java
	Bson modification1 = currentDate("actualizado");
	Bson modification2 = inc("resueltos", 2);
	Bson modification = combine(modification1, modification2);
	collection.updateMany(filter, modification);
	```

### 7.4. **Eliminaciones**

- `.deleteOne(Bson filtro)`: Elimina el primer documento de la colección que cumple el filtro. Devuelve un objeto `DeleteResult` que indica si la operación se ha realizado y cuántos documentos se han eliminado.

	```java
	Bson filter = eq("nombre", "Juan");
	DeleteResult resultado = col.deleteOne(filter);
	System.out.println( resultado.wasAcknowledged()+" "+ resultado.getDeletedCount());
	```

- `.deleteMany(Bson filtro)`: Elimina los documentos de la colección que cumplen el filtro. Devuelve un objeto `DeleteResult` que indica si la operación se ha realizado y cuántos documentos se han eliminado.

	```java
	Bson filter = eq("nombre", "Juan");
	DeleteResult resultado = col.deleteMany(filter);
	System.out.println( resultado.wasAcknowledged()+" "+ resultado.getDeletedCount());
	```

### 7.5. **Agregaciones**

Con el driver evidentemente también podemos especificar agregaciones. Lo haremos con el método `aggregate`. Con las agregaciones podemos:

- Hacer búsquedas.
- Cambiar el nombre de los campos.
- Calcular valores sobre los campos.
- Agrupar valores.
- Resumir datos.

La agregación se hace utilizando el método `.aggregate(List<Bson> etapas)`. Este método devuelve un `AggregateIterable`. Normalmente utilizaremos el método `into` para guardar el resultado dentro de una lista o `toCollection` para crear una lista nueva si la última etapa es `out`.

Aunque las distintas etapas se podrían generar manualmente, se recomienda utilizar los métodos estáticos de la clase `Aggregates` que facilitan la creación de las etapas.

- `.match(Bson filtro)`: Genera una etapa `match`. El filtro se puede generar con los métodos de la clase `Filters`.

	```java
	match(eq("title", "The Shawshank Redemption")); [cite: 197]
	```

- `.project(Bson projection)`: crea una etapa `projection` con la proyección que recibe como argumento.

	```java
	project(fields(include("title", "plot"), excludeId()));
	```

- `.sort(Bson sort)`: crea una etapa `sort` con la ordenación que recibe como argumento.

	```java
	sort(orderBy(descending("year"), ascending("title")));
	```

- `.skip(int n)`: crea una etapa `skip` que ignora los `n` primeros documentos.

	```java
	skip(5);
	```

- `.limit(int n)`: Devuelve como máximo `n` resultados.

	```java
	limit(10);
	```

- `.group(String id, List<Bson> acumuladores)` o `.group(String id, Bson... acumuladores)`: Agrupa documentos por la expresión determinada por los acumuladores y genera un documento para cada grupo. El primer parámetro es el campo que actuará como id.

	```java
	group("$customerId", sum("totalQuantity", "$quantity"), avg("averageQuantity", "$quantity"));
	```

- `.unwind(String nombreCampo)`: genera un nuevo documento para cada elemento del array contenido dentro `nombreCampo`.

	```java
	unwind("$sizes");
	```

- `.out(String nombreColeccion)`: genera una nueva colección con los documentos que le llegan. Al acabar la agregación se debe incluir `toCollection();`.

	```java
	out("authors");
	```

- `.merge(String nombreColeccion)`: introduce los documentos que le llegan dentro de la colección especificada. Al acabar la agregación se debe incluir `toCollection();`.

	```java
	merge("authors");
	```

- `.count(String nombre)`: Cuenta los documents que le llegan y crea el campo con el nombre que recibe como argumento para guardar esta cuenta.

	```java
	count("total");
	```

Podéis ver las etapas disponibles en la página:

< www.mongodb.com/docs/drivers/java/sync/v5.2/fundamentals/builders/aggregates >

#### 7.5.1. Ejemplo completo

```java
try (MongoClient mongoClient = MongoClients.create(uri)) {
    MongoDatabase database = mongoClient.getDatabase("pruebas");
    MongoCollection<Document> collection = database.getCollection("bios");

    // Creamos las etapas
    Bson filter = match(gte("_id", 3)); // Traducido filtra a filter
    Bson projection = project(fields(include("name"), include("awards"), excludeId()));
    Bson unwindOp = unwind("$awards");

    // Las ejecutamos y recogemos el resultado dentro de una variable.
    ArrayList<Document> resultado = new ArrayList<>();
    collection.aggregate(asList(filter, projection, unwindOp)).into(resultado);

    // Mostramos el resultado
    resultado.forEach(document -> {
        System.out.println(document.toJson());
    });
}
```
