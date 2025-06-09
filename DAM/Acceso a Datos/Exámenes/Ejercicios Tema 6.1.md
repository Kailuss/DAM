# Ejercicios TEMA 6.1: MongoDB

## Instrucciones

1. Instala MongoDB en tu sistema operativo.
2. Inicia el servidor MongoDB.
3. Utiliza MongoDB Compass o la shell de MongoDB para realizar los ejercicios.
4. Crea una base de datos llamada "biblioteca".

## Ejercicios

### Ejercicio 1: Crear una colección e insertar documentos

**Descripción**: En este ejercicio aprenderás a crear una colección en MongoDB y a insertar documentos en ella. MongoDB es una base de datos NoSQL orientada a documentos, donde los datos se almacenan en formato BSON (similar a JSON). A diferencia de las bases de datos relacionales, MongoDB no requiere un esquema predefinido, lo que permite mayor flexibilidad en la estructura de los datos.

```javascript
// Seleccionamos la base de datos biblioteca
// Si no existe, MongoDB la creará automáticamente cuando insertemos datos
use biblioteca

// Creamos una colección llamada "libros"
// En MongoDB, no es necesario crear explícitamente una colección antes de insertar documentos
// La colección se creará automáticamente con la primera inserción
// Sin embargo, podemos crearla explícitamente con este comando
db.createCollection("libros")

// Insertamos un documento en la colección "libros"
// Los documentos en MongoDB son similares a objetos JSON
db.libros.insertOne({
  isbn: "9788401352836",                // ISBN como identificador único del libro
  titulo: "El Quijote",                 // Título del libro
  autor: "Miguel de Cervantes",         // Autor del libro
  anio_publicacion: 1605,               // Año de publicación como número
  editorial: "Alfaguara",               // Editorial del libro
  num_paginas: 863,                     // Número de páginas como número
  generos: ["Novela", "Clásico"],       // Array de géneros literarios
  disponible: true                      // Booleano que indica si está disponible
})

// Insertamos varios documentos a la vez usando insertMany
// Esto es más eficiente que insertar documentos uno por uno
db.libros.insertMany([
  {
    isbn: "9788420412146",
    titulo: "Cien años de soledad",
    autor: "Gabriel García Márquez",
    anio_publicacion: 1967,
    editorial: "Cátedra",
    num_paginas: 471,
    generos: ["Novela", "Realismo mágico"],
    disponible: true
  },
  {
    isbn: "9788433920638",
    titulo: "La metamorfosis",
    autor: "Franz Kafka",
    anio_publicacion: 1915,
    editorial: "Anagrama",
    num_paginas: 128,
    generos: ["Novela corta", "Ficción absurda"],
    disponible: false
  },
  {
    isbn: "9788499089515",
    titulo: "El principito",
    autor: "Antoine de Saint-Exupéry",
    anio_publicacion: 1943,
    editorial: "Salamandra",
    num_paginas: 96,
    generos: ["Fábula", "Literatura infantil"],
    disponible: true
  }
])

// Verificamos que los documentos se han insertado correctamente
// find() sin argumentos devuelve todos los documentos de la colección
db.libros.find()
```

### Ejercicio 2: Consultas básicas

**Descripción**: En este ejercicio aprenderás a realizar consultas básicas en MongoDB para recuperar documentos de una colección. MongoDB proporciona métodos como `find()` y `findOne()` para buscar documentos, y permite filtrar los resultados mediante criterios de búsqueda especificados como documentos de consulta.

```javascript
// Consulta para obtener todos los documentos de la colección
// El método find() sin argumentos devuelve todos los documentos
db.libros.find()

// Para mejorar la legibilidad de los resultados, podemos usar pretty()
db.libros.find().pretty()

// Consulta para obtener un documento específico por su ISBN
// findOne() devuelve solo el primer documento que coincide con el criterio
db.libros.findOne({ isbn: "9788401352836" })

// Consulta para obtener libros de un autor específico
// Filtramos por el campo "autor"
db.libros.find({ autor: "Miguel de Cervantes" })

// Consulta para obtener libros publicados después de un año específico
// Utilizamos el operador $gt (greater than) para comparaciones
db.libros.find({ anio_publicacion: { $gt: 1950 } })

// Consulta para obtener libros publicados en un rango de años
// Combinamos $gt (greater than) y $lt (less than)
db.libros.find({ 
  anio_publicacion: { 
    $gt: 1900,    // Mayor que 1900
    $lt: 1950     // Menor que 1950
  } 
})

// Consulta para obtener libros disponibles
// Filtramos por el campo booleano "disponible"
db.libros.find({ disponible: true })

// Consulta para obtener libros de un género específico
// Utilizamos $in para buscar en arrays
db.libros.find({ generos: { $in: ["Novela"] } })

// Consulta con múltiples condiciones (AND implícito)
// Libros de un autor específico y disponibles
db.libros.find({ 
  autor: "Gabriel García Márquez", 
  disponible: true 
})

// Consulta con operador $or para condiciones alternativas
// Libros de Cervantes O Kafka
db.libros.find({ 
  $or: [
    { autor: "Miguel de Cervantes" },
    { autor: "Franz Kafka" }
  ] 
})

// Consulta con proyección para seleccionar solo algunos campos
// Solo mostramos título y autor, ocultamos el _id
db.libros.find(
  {}, // Filtro vacío para seleccionar todos los documentos
  { _id: 0, titulo: 1, autor: 1 } // Proyección: 1 incluye, 0 excluye
)
```

### Ejercicio 3: Actualización de documentos

**Descripción**: En este ejercicio aprenderás a actualizar documentos existentes en MongoDB. MongoDB proporciona varios métodos para actualizar documentos, como `updateOne()`, `updateMany()` y `replaceOne()`, junto con operadores de actualización como `$set`, `$inc`, `$push`, etc., que permiten modificar campos específicos sin reemplazar todo el documento.

```javascript
// Actualizar un campo en un documento específico
// $set modifica el valor de un campo existente o lo crea si no existe
db.libros.updateOne(
  { isbn: "9788401352836" },           // Filtro para identificar el documento
  { $set: { titulo: "Don Quijote de la Mancha" } }  // Operación de actualización
)

// Actualizar múltiples campos en un documento
db.libros.updateOne(
  { isbn: "9788401352836" },
  { 
    $set: { 
      editorial: "Real Academia Española",  // Cambiamos la editorial
      num_paginas: 1250                     // Actualizamos el número de páginas
    } 
  }
)

// Incrementar un valor numérico
// $inc incrementa el valor de un campo numérico
db.libros.updateOne(
  { isbn: "9788420412146" },
  { $inc: { num_paginas: 10 } }  // Incrementa num_paginas en 10
)

// Añadir un elemento a un array
// $push añade un elemento al final de un array
db.libros.updateOne(
  { isbn: "9788420412146" },
  { $push: { generos: "Literatura latinoamericana" } }
)

// Añadir múltiples elementos a un array
// $push con $each para añadir varios elementos
db.libros.updateOne(
  { isbn: "9788401352836" },
  { 
    $push: { 
      generos: { 
        $each: ["Sátira", "Aventura"] 
      } 
    } 
  }
)

// Eliminar un elemento de un array
// $pull elimina todos los elementos que coincidan con el criterio
db.libros.updateOne(
  { isbn: "9788401352836" },
  { $pull: { generos: "Aventura" } }
)

// Actualizar múltiples documentos que coincidan con un criterio
// updateMany afecta a todos los documentos que cumplan el filtro
db.libros.updateMany(
  { disponible: false },          // Filtro: todos los no disponibles
  { $set: { disponible: true } }  // Operación: marcarlos como disponibles
)

// Reemplazar completamente un documento
// replaceOne sustituye todo el documento excepto el _id
db.libros.replaceOne(
  { isbn: "9788433920638" },
  {
    isbn: "9788433920638",
    titulo: "La metamorfosis",
    autor: "Franz Kafka",
    anio_publicacion: 1915,
    editorial: "Alianza Editorial",  // Cambiamos la editorial
    num_paginas: 132,                // Actualizamos el número de páginas
    generos: ["Novela corta", "Ficción absurda", "Literatura existencialista"],
    disponible: true,
    traductor: "Jorge Luis Borges"   // Añadimos un nuevo campo
  }
)

// Upsert: actualizar si existe, insertar si no existe
// El tercer parámetro { upsert: true } habilita esta funcionalidad
db.libros.updateOne(
  { isbn: "9788498383621" },  // Este ISBN no existe en nuestra colección
  { 
    $set: { 
      titulo: "El hobbit",
      autor: "J.R.R. Tolkien",
      anio_publicacion: 1937,
      editorial: "Minotauro",
      num_paginas: 310,
      generos: ["Fantasía", "Aventura"],
      disponible: true
    } 
  },
  { upsert: true }  // Si no existe, crea un nuevo documento
)
```

### Ejercicio 4: Eliminación de documentos

**Descripción**: En este ejercicio aprenderás a eliminar documentos de una colección en MongoDB. MongoDB proporciona los métodos `deleteOne()` y `deleteMany()` para eliminar documentos que coincidan con un criterio específico. También es posible eliminar colecciones enteras o incluso bases de datos.

```javascript
// Eliminar un documento específico
// deleteOne elimina el primer documento que coincide con el filtro
db.libros.deleteOne({ isbn: "9788498383621" })

// Eliminar múltiples documentos que coincidan con un criterio
// deleteMany elimina todos los documentos que coinciden con el filtro
db.libros.deleteMany({ anio_publicacion: { $lt: 1900 } })

// Eliminar documentos que cumplan condiciones complejas
// Combinamos múltiples condiciones con operadores lógicos
db.libros.deleteMany({
  $or: [
    { disponible: false },
    { num_paginas: { $lt: 100 } }
  ]
})

// Eliminar todos los documentos de una colección
// Esto mantiene la colección y sus índices, solo elimina los documentos
db.libros.deleteMany({})

// Eliminar una colección completa
// Esto elimina la colección y todos sus índices
db.libros.drop()

// Eliminar una base de datos completa
// Esto elimina la base de datos actual y todas sus colecciones
// db.dropDatabase()  // Comentado para evitar ejecutarlo accidentalmente
```

### Ejercicio 5: Consultas avanzadas

**Descripción**: En este ejercicio aprenderás a realizar consultas más avanzadas en MongoDB, utilizando operadores de consulta, expresiones regulares, proyecciones y métodos de cursor como `sort()`, `limit()` y `skip()`. Estas técnicas te permitirán realizar búsquedas más precisas y controlar mejor los resultados obtenidos.

```javascript
// Primero, vamos a insertar algunos documentos para trabajar
db.libros.insertMany([
  {
    isbn: "9788401352836",
    titulo: "Don Quijote de la Mancha",
    autor: "Miguel de Cervantes",
    anio_publicacion: 1605,
    editorial: "Real Academia Española",
    num_paginas: 1250,
    generos: ["Novela", "Clásico", "Sátira"],
    disponible: true,
    precio: 25.50,
    idioma: "Español"
  },
  {
    isbn: "9788420412146",
    titulo: "Cien años de soledad",
    autor: "Gabriel García Márquez",
    anio_publicacion: 1967,
    editorial: "Cátedra",
    num_paginas: 481,
    generos: ["Novela", "Realismo mágico", "Literatura latinoamericana"],
    disponible: true,
    precio: 19.95,
    idioma: "Español"
  },
  {
    isbn: "9788433920638",
    titulo: "La metamorfosis",
    autor: "Franz Kafka",
    anio_publicacion: 1915,
    editorial: "Alianza Editorial",
    num_paginas: 132,
    generos: ["Novela corta", "Ficción absurda", "Literatura existencialista"],
    disponible: true,
    precio: 12.75,
    idioma: "Español"
  },
  {
    isbn: "9788499089515",
    titulo: "El principito",
    autor: "Antoine de Saint-Exupéry",
    anio_publicacion: 1943,
    editorial: "Salamandra",
    num_paginas: 96,
    generos: ["Fábula", "Literatura infantil"],
    disponible: true,
    precio: 9.95,
    idioma: "Español"
  },
  {
    isbn: "9780061120084",
    titulo: "To Kill a Mockingbird",
    autor: "Harper Lee",
    anio_publicacion: 1960,
    editorial: "HarperCollins",
    num_paginas: 336,
    generos: ["Novela", "Ficción legal", "Bildungsroman"],
    disponible: true,
    precio: 15.99,
    idioma: "Inglés"
  },
  {
    isbn: "9780141439518",
    titulo: "Pride and Prejudice",
    autor: "Jane Austen",
    anio_publicacion: 1813,
    editorial: "Penguin Classics",
    num_paginas: 480,
    generos: ["Novela", "Romance", "Sátira"],
    disponible: false,
    precio: 14.50,
    idioma: "Inglés"
  }
])

// Consulta con expresiones regulares
// Buscar libros cuyo título contenga la palabra "Quijote" (case sensitive)
db.libros.find({ titulo: /Quijote/ })

// Expresión regular con opciones
// Buscar libros cuyo título contenga "quijote" (case insensitive)
db.libros.find({ titulo: /quijote/i })

// Consulta con operador $elemMatch para arrays
// Buscar libros que tengan exactamente los géneros especificados
db.libros.find({ 
  generos: { 
    $all: ["Novela", "Sátira"] 
  } 
})

// Consulta con operador $size para arrays
// Buscar libros que tengan exactamente 3 géneros
db.libros.find({ generos: { $size: 3 } })

// Consulta con operador $exists
// Buscar libros que tengan el campo "traductor"
db.libros.find({ traductor: { $exists: true } })

// Consulta con operador $type
// Buscar libros donde el precio sea un número
db.libros.find({ precio: { $type: "number" } })

// Ordenar resultados
// Ordenar libros por año de publicación (ascendente)
db.libros.find().sort({ anio_publicacion: 1 })

// Ordenar por múltiples campos
// Primero por disponibilidad (descendente) y luego por precio (ascendente)
db.libros.find().sort({ disponible: -1, precio: 1 })

// Limitar el número de resultados
// Obtener solo los 3 primeros libros
db.libros.find().limit(3)

// Saltar resultados
// Útil para paginación: saltar los 2 primeros y mostrar los 2 siguientes
db.libros.find().skip(2).limit(2)

// Combinar ordenación, salto y límite
// Ordenar por precio, saltar los 2 más baratos y mostrar los 3 siguientes
db.libros.find().sort({ precio: 1 }).skip(2).limit(3)

// Contar documentos
// Contar cuántos libros hay en total
db.libros.countDocuments()

// Contar documentos que cumplen un criterio
// Contar cuántos libros están disponibles
db.libros.countDocuments({ disponible: true })

// Consulta con operador $and explícito
// Libros en español Y disponibles
db.libros.find({ 
  $and: [
    { idioma: "Español" },
    { disponible: true }
  ] 
})

// Consulta con operadores de comparación combinados
// Libros con precio entre 10 y 20
db.libros.find({ 
  precio: { 
    $gte: 10,   // Greater than or equal
    $lte: 20    // Less than or equal
  } 
})

// Proyección con exclusión de múltiples campos
// Mostrar todos los campos excepto _id y num_paginas
db.libros.find(
  {}, 
  { _id: 0, num_paginas: 0 }
)
```

### Ejercicio 6: Agregaciones

**Descripción**: En este ejercicio aprenderás a utilizar el framework de agregación de MongoDB, que permite realizar operaciones avanzadas de procesamiento y transformación de datos. El framework de agregación se basa en el concepto de pipeline (tubería), donde los documentos pasan por varias etapas de procesamiento, como filtrado, agrupación, proyección, ordenación, etc.

```javascript
// Agregación simple: agrupar libros por idioma y contar cuántos hay de cada uno
db.libros.aggregate([
  // Primera etapa: agrupar por idioma
  { 
    $group: { 
      _id: "$idioma",           // Campo por el que agrupar
      cantidad: { $sum: 1 }     // Contador de documentos
    } 
  }
])

// Agregación con múltiples etapas: precio promedio por idioma para libros disponibles
db.libros.aggregate([
  // Primera etapa: filtrar solo libros disponibles
  { 
    $match: { 
      disponible: true 
    } 
  },
  // Segunda etapa: agrupar por idioma y calcular precio promedio
  { 
    $group: { 
      _id: "$idioma",
      precioPromedio: { $avg: "$precio" },
      cantidadLibros: { $sum: 1 }
    } 
  },
  // Tercera etapa: ordenar por precio promedio descendente
  { 
    $sort: { 
      precioPromedio: -1 
    } 
  }
])

// Agregación con proyección: transformar los documentos
db.libros.aggregate([
  // Primera etapa: proyectar solo algunos campos y crear campos calculados
  { 
    $project: { 
      _id: 0,                                   // Excluir _id
      titulo: 1,                                // Incluir título
      autor: 1,                                 // Incluir autor
      antiguedad: { $subtract: [2023, "$anio_publicacion"] },  // Calcular antigüedad
      precioConIVA: { $multiply: ["$precio", 1.21] }           // Calcular precio con IVA
    } 
  }
])

// Agregación con $unwind: descomponer arrays
db.libros.aggregate([
  // Primera etapa: descomponer el array de géneros
  { 
    $unwind: "$generos" 
  },
  // Segunda etapa: agrupar por género y contar libros
  { 
    $group: { 
      _id: "$generos",
      cantidadLibros: { $sum: 1 },
      libros: { $push: "$titulo" }  // Crear array con títulos
    } 
  },
  // Tercera etapa: ordenar por cantidad descendente
  { 
    $sort: { 
      cantidadLibros: -1 
    } 
  }
])

// Agregación con $lookup: similar a un JOIN en SQL
// Primero creamos una colección de autores
db.autores.insertMany([
  {
    nombre: "Miguel de Cervantes",
    nacionalidad: "Española",
    anio_nacimiento: 1547,
    anio_fallecimiento: 1616
  },
  {
    nombre: "Gabriel García Márquez",
    nacionalidad: "Colombiana",
    anio_nacimiento: 1927,
    anio_fallecimiento: 2014
  },
  {
    nombre: "Franz Kafka",
    nacionalidad: "Austrohúngara",
    anio_nacimiento: 1883,
    anio_fallecimiento: 1924
  }
])

// Ahora hacemos la agregación con $lookup
db.libros.aggregate([
  // Primera etapa: filtrar solo algunos libros
  { 
    $match: { 
      idioma: "Español" 
    } 
  },
  // Segunda etapa: JOIN con la colección de autores
  { 
    $lookup: { 
      from: "autores",              // Colección con la que hacer JOIN
      localField: "autor",          // Campo en la colección actual
      foreignField: "nombre",       // Campo en la colección externa
      as: "informacion_autor"       // Nombre del nuevo campo para los resultados
    } 
  },
  // Tercera etapa: proyectar solo los campos que nos interesan
  { 
    $project: { 
      _id: 0,
      titulo: 1,
      autor: 1,
      anio_publicacion: 1,
      informacion_autor: 1
    } 
  }
])

// Agregación con $facet: múltiples agregaciones en paralelo
db.libros.aggregate([
  { 
    $facet: { 
      // Primera faceta: estadísticas por idioma
      "porIdioma": [
        { $group: { _id: "$idioma", cantidad: { $sum: 1 } } }
      ],
      // Segunda faceta: estadísticas por disponibilidad
      "porDisponibilidad": [
        { $group: { _id: "$disponible", cantidad: { $sum: 1 } } }
      ],
      // Tercera faceta: libros más antiguos
      "masAntiguos": [
        { $sort: { anio_publicacion: 1 } },
        { $limit: 3 },
        { $project: { _id: 0, titulo: 1, autor: 1, anio_publicacion: 1 } }
      ]
    } 
  }
])
```

### Ejercicio 7: Índices

**Descripción**: En este ejercicio aprenderás a crear y gestionar índices en MongoDB. Los índices mejoran el rendimiento de las consultas al permitir que MongoDB encuentre documentos sin tener que escanear toda la colección. Sin embargo, los índices también tienen un costo en términos de espacio de almacenamiento y rendimiento de escritura, por lo que deben utilizarse estratégicamente.

```javascript
// Crear un índice simple
// Creamos un índice sobre el campo isbn para acelerar las búsquedas por ISBN
db.libros.createIndex({ isbn: 1 })  // 1 para orden ascendente

// Crear un índice único
// Asegura que no haya valores duplicados en el campo isbn
db.libros.createIndex({ isbn: 1 }, { unique: true })

// Crear un índice compuesto
// Útil para consultas que filtran por autor y título
db.libros.createIndex({ autor: 1, titulo: 1 })

// Crear un índice de texto
// Permite búsquedas de texto completo en los campos especificados
db.libros.createIndex({ titulo: "text", autor: "text" })

// Realizar una búsqueda de texto utilizando el índice de texto
db.libros.find({ $text: { $search: "Quijote Cervantes" } })

// Ver todos los índices de una colección
db.libros.getIndexes()

// Eliminar un índice específico
db.libros.dropIndex("autor_1_titulo_1")  // Nombre del índice

// Crear un índice en segundo plano
// Útil para colecciones grandes en entornos de producción
db.libros.createIndex(
  { anio_publicacion: 1 },
  { background: true }
)

// Crear un índice con tiempo de vida (TTL)
// Los documentos se eliminarán automáticamente después del tiempo especificado
// Útil para datos temporales o de caducidad
db.sesiones.createIndex(
  { ultima_actividad: 1 },
  { expireAfterSeconds: 3600 }  // 1 hora
)

// Crear un índice parcial
// Solo indexa los documentos que cumplen una condición
db.libros.createIndex(
  { precio: 1 },
  { partialFilterExpression: { disponible: true } }
)

// Crear un índice con cobertura (covered query)
// Incluye todos los campos necesarios para la consulta
db.libros.createIndex(
  { autor: 1, titulo: 1, precio: 1 }
)

// Consulta que puede ser satisfecha completamente por el índice
// (no necesita acceder a los documentos)
db.libros.find(
  { autor: "Miguel de Cervantes" },
  { _id: 0, titulo: 1, precio: 1 }
)
```

### Ejercicio 8: Modelado de datos

**Descripción**: En este ejercicio aprenderás diferentes estrategias para modelar datos en MongoDB. A diferencia de las bases de datos relacionales, MongoDB permite estructuras de datos flexibles, incluyendo documentos embebidos y referencias entre documentos. La elección entre estas estrategias depende de los patrones de acceso a los datos y de las necesidades específicas de la aplicación.

```javascript
// Modelo con documentos embebidos
// Útil cuando los datos relacionados se acceden juntos frecuentemente
// Ejemplo: un libro con sus reseñas embebidas
db.libros_con_resenas.insertOne({
  isbn: "9788401352836",
  titulo: "Don Quijote de la Mancha",
  autor: "Miguel de Cervantes",
  anio_publicacion: 1605,
  editorial: "Real Academia Española",
  num_paginas: 1250,
  generos: ["Novela", "Clásico", "Sátira"],
  disponible: true,
  precio: 25.50,
  idioma: "Español",
  // Reseñas embebidas como un array de subdocumentos
  resenas: [
    {
      usuario: "lector123",
      puntuacion: 5,
      comentario: "Una obra maestra de la literatura universal.",
      fecha: new Date("2022-03-15")
    },
    {
      usuario: "bookworm",
      puntuacion: 4,
      comentario: "Excelente, aunque algunas partes son densas.",
      fecha: new Date("2022-05-20")
    }
  ]
})

// Consulta que aprovecha la estructura embebida
// Buscar libros con reseñas de puntuación 5
db.libros_con_resenas.find({
  "resenas.puntuacion": 5
})

// Modelo con referencias (similar a claves foráneas en SQL)
// Útil cuando los datos relacionados son grandes o se acceden independientemente
// Ejemplo: libros y autores en colecciones separadas

// Colección de autores
db.autores_ref.insertMany([
  {
    _id: ObjectId(),  // MongoDB genera un _id único
    nombre: "Miguel de Cervantes",
    nacionalidad: "Española",
    anio_nacimiento: 1547,
    anio_fallecimiento: 1616,
    biografia: "Miguel de Cervantes Saavedra fue un novelista, poeta y dramaturgo español..."
  },
  {
    _id: ObjectId(),
    nombre: "Gabriel García Márquez",
    nacionalidad: "Colombiana",
    anio_nacimiento: 1927,
    anio_fallecimiento: 2014,
    biografia: "Gabriel José de la Concordia García Márquez fue un escritor y periodista colombiano..."
  }
])

// Guardamos los IDs para usarlos en las referencias
var cervantesId = db.autores_ref.findOne({ nombre: "Miguel de Cervantes" })._id;
var marquezId = db.autores_ref.findOne({ nombre: "Gabriel García Márquez" })._id;

// Colección de libros con referencias a autores
db.libros_ref.insertMany([
  {
    isbn: "9788401352836",
    titulo: "Don Quijote de la Mancha",
    autor_id: cervantesId,  // Referencia al autor
    anio_publicacion: 1605,
    editorial: "Real Academia Española",
    num_paginas: 1250,
    generos: ["Novela", "Clásico", "Sátira"],
    disponible: true
  },
  {
    isbn: "9788420412146",
    titulo: "Cien años de soledad",
    autor_id: marquezId,  // Referencia al autor
    anio_publicacion: 1967,
    editorial: "Cátedra",
    num_paginas: 481,
    generos: ["Novela", "Realismo mágico"],
    disponible: true
  }
])

// Consulta con $lookup para unir datos de diferentes colecciones
db.libros_ref.aggregate([
  {
    $lookup: {
      from: "autores_ref",
      localField: "autor_id",
      foreignField: "_id",
      as: "autor_info"
    }
  },
  {
    $project: {
      _id: 0,
      isbn: 1,
      titulo: 1,
      anio_publicacion: 1,
      "autor_info.nombre": 1,
      "autor_info.nacionalidad": 1
    }
  }
])

// Modelo híbrido: combina documentos embebidos y referencias
// Útil para escenarios complejos con diferentes patrones de acceso
db.editoriales.insertOne({
  _id: ObjectId(),
  nombre: "Editorial Académica",
  pais: "España",
  fundacion: 1950,
  sitio_web: "www.editorialacademica.es"
})

var editorialId = db.editoriales.findOne({ nombre: "Editorial Académica" })._id;

db.libros_hibrido.insertOne({
  isbn: "9788401352836",
  titulo: "Don Quijote de la Mancha",
  // Información básica del autor embebida para acceso rápido
  autor: {
    nombre: "Miguel de Cervantes",
    nacionalidad: "Española"
  },
  // Referencia al autor completo para detalles adicionales
  autor_id: cervantesId,
  // Referencia a la editorial
  editorial_id: editorialId,
  anio_publicacion: 1605,
  num_paginas: 1250,
  generos: ["Novela", "Clásico", "Sátira"],
  disponible: true,
  // Reseñas embebidas (datos pequeños y frecuentemente accedidos juntos)
  resenas: [
    {
      usuario: "lector123",
      puntuacion: 5,
      comentario: "Una obra maestra de la literatura universal."
    }
  ]
})

// Modelo para relaciones muchos a muchos
// Ejemplo: libros y categorías

// Colección de categorías
db.categorias.insertMany([
  { _id: ObjectId(), nombre: "Ficción", descripcion: "Obras de ficción literaria" },
  { _id: ObjectId(), nombre: "Clásicos", descripcion: "Obras clásicas de la literatura" },
  { _id: ObjectId(), nombre: "Aventura", descripcion: "Libros de aventuras" }
])

// Guardamos los IDs para usarlos en las referencias
var ficcionId = db.categorias.findOne({ nombre: "Ficción" })._id;
var clasicosId = db.categorias.findOne({ nombre: "Clásicos" })._id;
var aventuraId = db.categorias.findOne({ nombre: "Aventura" })._id;

// Colección de libros con referencias a categorías
db.libros_categorias.insertOne({
  isbn: "9788401352836",
  titulo: "Don Quijote de la Mancha",
  autor: "Miguel de Cervantes",
  anio_publicacion: 1605,
  // Array de referencias a categorías
  categoria_ids: [ficcionId, clasicosId, aventuraId]
})

// Alternativamente, colección de relaciones
// Útil cuando necesitamos metadatos sobre la relación
db.libro_categoria.insertMany([
  { libro_id: "9788401352836", categoria_id: ficcionId, fecha_asignacion: new Date() },
  { libro_id: "9788401352836", categoria_id: clasicosId, fecha_asignacion: new Date() },
  { libro_id: "9788401352836", categoria_id: aventuraId, fecha_asignacion: new Date() }
])
```
