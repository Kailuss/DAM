# Test Acceso a Datos

## U1 - El archivo manifest
1. **El archivo manifest:**
   - a. Se encuentra dentro de la carpeta `META-INF` del JAR.  
   - b. Todas las respuestas son ciertas.  
   - c. Permite indicar la ruta de otros componentes y bibliotecas que necesita el código de este JAR para funcionar.  
   - d. Describe el contenido del JAR.  

2. **¿Cuál de las siguientes afirmaciones sobre los paquetes es cierta?**  
   - a. Los paquetes generan espacios de nombres; el nombre completo de una clase es el nombre de la clase con el nombre del paquete como prefijo.  
   - b. El estándar de nomenclatura dice que el nombre de los paquetes de una empresa u organización comienza con el nombre del dominio de internet al revés.  
   - c. Es importante organizar el código en paquetes, de manera que sea fácil localizar las clases.  
   - d. Todas las respuestas son ciertas.  

3. **MVC significa:**  
   - a. Todas las otras respuestas son falsas.  
   - b. Modelo Vista Controlador.  
   - c. Máquina Virtual Completa.  
   - d. Make Visual Cooperation.  

4. **Un archivo con la extensión JAR es:**  
   - a. No existen archivos con esta extensión.  
   - b. Todas las otras respuestas son falsas.  
   - c. Un archivo Java ejecutable.  
   - d. Un archivo que contiene todas las clases y otros archivos necesarios para incorporar un componente a otra aplicación o para ejecutar una aplicación con el comando `java -jar`.  

## U2 - Clases para manejo de archivos
1. **La clase `Files`:**  
   - a. Nos permite leer las líneas que contiene un archivo de texto.  
   - b. Todas las respuestas son ciertas.  
   - c. Escribe siempre los datos a un archivo como bytes.  
   - d. Nos permite leer los bytes que contiene un archivo.  

2. **Todas las clases para el tratamiento de flujos de bytes heredan de `Read` y `Write`.**  
   - Verdadero  
   - Falso  

3. **El concepto de flujo de datos:**  
   - a. Solo se aplica a archivos.  
   - b. Se puede aplicar a archivos, salidas de dispositivos, salidas de otros programas, etc.  
   - c. Todas las respuestas son correctes.  
   - d. Todas las otras respuestas son falsas.  

4. **La ruta `../sally/preguntes.txt`:**  
   - a. No es una ruta correcta.  
   - b. Hace referencia al archivo `preguntes.txt` que se encuentra en la subcarpeta `sally` de la carpeta que contiene la carpeta actual.  
   - c. Solo es correcta en sistemas Windows.  
   - d. Solo es correcta en sistemas Linux.  

5. **La clase `FileReader`:**  
   - a. Puede leer el archivo de texto carácter a carácter o línea a línea.  
   - b. Todas las otras respuestas son falsas.  
   - c. Lee el archivo carácter a carácter y los devuelve como `int`, debemos hacer el casting a `char`.  
   - d. Devuelve el contenido del archivo de texto línea a línea.  

6. **Para copiar un archivo o directorio podemos usar `Files.copy()`.**  
   - Verdadero  
   - Falso  

7. **Los flujos de bytes:**  
   - a. Solo pueden leer archivos de texto.  
   - b. Leen directamente los bytes que forman el archivo; se debe programar el código necesario para interpretarlos (como una imagen, etc.).  
   - c. No pueden leer archivos de texto.  
   - d. Leen los bytes del archivo y devuelven un objeto con los datos interpretados (por ejemplo, una imagen).  

8. **Los `ObjectStreams`:**  
   - a. Mantienen las referencias de los objetos guardados en los archivos.  
   - b. Todas las respuestas son correctas.  
   - c. Siempre devuelven un objeto de la clase `Object`; debemos hacer el casting a la clase adecuada.  
   - d. Permiten guardar objetos complejos en el archivo y recuperarlos.  

9. **Los `DataStreams` pueden guardar valores de tipos primitivos dentro de un archivo. ¿Cuál de las siguientes afirmaciones es cierta?**  
   - a. Todas las respuestas son correctas.  
   - b. Al leer los datos del archivo, estas clases se encargan de hacer el casting al tipo adecuado.  
   - c. Los datos se deben leer en el orden correcto y con los métodos adecuados; si no, no recuperaremos los datos originales.  
   - d. Estos flujos solo pueden guardar datos de un único tipo dentro del mismo archivo.  

10. **El método `Path.getFilename(path)`:**  
	- a. Todas las respuestas son correctas.  
	- b. La clase `Path` no tiene este método.  
	- c. Devuelve la última parte del `path` pasado como argumento.  
	- d. Da error si el `path` hace referencia a un directorio o carpeta.  

11. **Cuando operamos con rutas de archivos, el carácter separador entre directorios o carpetas:**  
	- a. En Java se utiliza `:` como separador.  
	- b. Es recomendable usar siempre `\`.  
	- c. Cambia dependiendo del sistema operativo.  
	- d. Es recomendable usar siempre `/`.  

12. **Si usamos el método `Files.createDirectory()`:**  
	- a. La ruta hasta el directorio donde queremos crear el nuevo debe existir.  
	- b. Solo podemos crear directorios nuevos dentro del directorio actual.  
	- c. Creará los directorios que hagan falta para completar la ruta recibida como parámetro.  
	- d. Todas las respuestas son correctas.  

13. **Los flujos de caracteres:**  
	- a. Si se usan con clases sin buffer, los procesos de lectura/escritura serán más lentos.  
	- b. Todas son correctas.  
	- c. Disponen de clases con buffer y sin buffer.  
	- d. Se pueden manipular con subclases de las clases abstractas `Reader` y `Writer`.  

14. **Los streams:**  
	- a. Se deben cerrar manualmente o abrirlos dentro de un `try-with-resources`.  
	- b. Todas las otras respuestas son falsas.  
	- c. En ningún caso se deben cerrar.  
	- d. Siempre se deben cerrar manualmente llamando al método `close()`.  

15. **La ruta `/home/joe/statusReport`:**  
	- a. Es una ruta correcta en un sistema Windows.  
	- b. Todas las respuestas son correctas.  
	- c. Todas las otras respuestas son falsas.  
	- d. Es una ruta correcta en un sistema Linux.  

16. **Si usamos el método `Files.createDirectories()`:**  
	- a. La ruta hasta el directorio donde queremos crear el nuevo debe existir.  
	- b. Creará los directorios que hagan falta para completar la ruta recibida como parámetro.  
	- c. Todas las respuestas son correctas.  
	- d. Solo podemos crear directorios nuevos dentro del directorio actual.  

17. **Para crear un directorio en Java usaremos el método:**  
	- a. `Files.mkdir(ruta)`.  
	- b. `Path.createDirectory(ruta)`.  
	- c. Todas son correctas.  
	- d. `Files.createDirectory(path)`.  

18. **`BufferedWriter` se utiliza para añadir un buffer a un flujo de tipo `FileReader`.**  
	- Verdadero  
	- Falso  

19. **Con las clases que implementan buffers se intentan minimizar las operaciones en disco.**  
	- Verdadero  
	- Falso  

## U3 - Bases de datos y JDBC  

1. **Un procedimiento almacenado es un procedimiento o subprograma que está almacenado en la base de datos.**  
   - Verdadero  
   - Falso  

2. **Un procedimiento almacenado típico tiene:**  
   - a. Unas sentencias SQL.  
   - b. Una lista de parámetros.  
   - c. Un nombre.  
   - d. Todas las respuestas son correctas.  

3. **Una transacción incluye desde el último `COMMIT` o `ROLLBACK` hasta el siguiente `COMMIT`.**  
   - Verdadero  
   - Falso  

4. **El conector (driver) lo puede proporcionar:**  
   - a. Cada programador de aplicaciones desarrolla el suyo.  
   - b. Oracle Drivers & Co.  
   - c. El fabricante de la base de datos o un tercero.  
   - d. No hace falta utilizar un conector a la base de datos.  

5. **Una transacción tiene tres finales posibles: `COMMIT`, `EXIT` o `ROLLBACK`.**  
   - Verdadero  
   - Falso  

6. **La clase `Statement` tiene el inconveniente de que:**  
   - a. Se debe compilar cada vez.  
   - Verdadero  
   - Falso  

7. **Al ejecutar una transacción, el motor de la base de datos garantiza:**  
   - a. Subjetividad.  
   - b. Atomicidad.  
   - c. Inconsistencia.  
   - d. Temporalidad.  

8. **Tradicionalmente, la programación de bases de datos ha contado con un único producto: JDBC.**  
   - Verdadero  
   - Falso  

9. **En un bloque de instrucciones, el bloque `finally` se ejecutará:**  
   - a. A veces, dependiendo de si hay errores o no.  
   - Verdadero  
   - Falso  

10. **Un driver suele ser un archivo `.zip` que contiene una implementación de algunas interfaces de la API JDBC.**  
	- Verdadero  
	- Falso  

11. **Respecto a las consultas preparadas (`PreparedStatement`), señala la afirmación correcta:**  
	- a. Son menos eficientes que las consultas normales.  
	- b. Pueden tener parámetros.  
	- c. Cada ejecución de la consulta implica comenzar todo el proceso de análisis y compilación de la query.  
	- d. Son consultas que se compilan en cada `executeQuery` o `executeUpdate`.  

12. **La gran mayoría de sistemas gestores de bases de datos no permiten crear la base de datos desde la línea de comandos.**  
	- Verdadero  
	- Falso  

13. **El proceso de creación y destrucción de una conexión a una base de datos es rápido y no afecta sensiblemente al rendimiento de una aplicación.**  
	- Verdadero  
	- Falso  

14. **En el modelo relacional hay relaciones y conjuntos debido a su naturaleza matemática.**  
	- Verdadero  
	- Falso  

15. **Para operar con una base de datos y ejecutar consultas, nuestra aplicación debe:**  
	- a. Establecer una conexión con la base de datos.  
	- b. Enviar consultas SQL y procesar el resultado.  
	- c. Liberar los recursos al terminar.  
	- d. Todas las anteriores son necesarias.  

16. **Las acciones sobre una base de datos pueden lanzar la excepción `DataBaseException`.**  
	- Verdadero  
	- Falso  

17. **La escritura mediante JDBC implica:**  
	- a. Abrir una conexión.  
	- b. Copiar los valores necesarios en la sentencia y ejecutarla para almacenar el objeto.  
	- c. Crear una sentencia SQL.  
	- d. Todas son correctas.  

18. **La ventaja de usar conectores JDBC es que independiza la aplicación de la definición del driver de la base de datos.**  
	- Verdadero  
	- Falso  

## U4 - Persistencia y JPA  

1. **Un objeto recién creado que no está enlazado con el gestor de persistencia se encuentra en estado:**  
   - a. `Managed`.  
   - b. `Detached` (Disociado).  
   - c. `New` (Nuevo).  
   - d. `Removed` (Borrado).  

2. **Son propiedades JDBC de JPA:**  
   - a. `jakarta.persistence.jdbc.url`.  
   - b. `jakarta.persistence.user`.  
   - c. `jakarta.connection.contrasenya`.  
   - d. `jakarta.connection.usuari`.  

3. **El lenguaje JPQL es sensible a mayúsculas.**  
   - Verdadero  
   - Falso  

4. **Ventajas de las herramientas ORM:**  
   - a. Reutilización de código.  
   - b. Reducción del tiempo de desarrollo.  
   - c. Independencia de la base de datos.  
   - d. Todas las respuestas son correctas.  

5. **Un objeto recuperado de la base de datos, cuando el `EntityManager` se ha cerrado, está en estado:**  
   - a. `New`.  
   - b. `Removed`.  
   - c. `Detached`.  
   - d. `Managed`.  

6. **En sistemas estándar de bases de datos, SQL solo puede almacenar y manipular valores escalares organizados en tablas relacionales.**  
   - Verdadero  
   - Falso  

7. **Si un objeto está en memoria después de haber terminado la sesión, está en estado:**  
   - a. `Persistent`.  
   - b. `Transient` (Transitorio).  
   - c. `Detached` (Disociado).  
   - d. `Removed` (Eliminado).  

8. **El conjunto de órdenes que se ejecutan de forma atómica e indivisible es:**  
   - a. Una sesión.  
   - b. Una consulta.  
   - c. Una transacción.  
   - d. Una excepción.  

9. **Las herramientas ORM convierten objetos en registros y viceversa.**  
   - Verdadero  
   - Falso  

10. **Un objeto en estado `Managed`:**  
	- a. Está marcado como borrado en la base de datos.  
	- b. Está enlazado a la sesión actual de la base de datos.  
	- c. No está enlazado a la sesión.  
	- d. Todas las opciones son incorrectas.  

11. **¿Qué entendemos por mapeo objeto-relacional?**  
	- a. Técnica que convierte entre tipos de datos de objetos y bases de datos relacionales.  
	- b. Técnica para almacenar objetos en bases de datos no relacionales.  
	- c. Proceso de búsqueda avanzada en bases de datos relacionales.  
	- d. Software para mejorar la depuración en POO.  

12. **El lenguaje de consultas propio de JPA es:**  
	- a. `NamedQuery`.  
	- b. `SQLQuery`.  
	- c. `JPQL`.  
	- d. `HQL`.  

13. **En JPA, el método para crear consultas es:**  
	- a. `Session.createSQLQuery()`.  
	- b. `Session.SQLQuery()`.  
	- c. `Session.query()`.  
	- d. `entityManager.createQuery()`.  

14. **¿Cómo se llama el archivo que contiene información sobre la base de datos y otras propiedades?**  
	- a. `persistence.properties`.  
	- b. No existe tal archivo.  
	- c. `persistence.configuration`.  
	- d. `persistence.xml`.  

15. **¿Qué es lo primero que debemos hacer para configurar Hibernate?**  
	- a. Escoger un parámetro de `org.properties`.  
	- b. Buscar el archivo de propiedades.  
	- c. Ninguna de las opciones es correcta.  
	- d. Establecer las propiedades de `hibernate.cfg.xml`.  

16. **Tipos de multiplicidad en relaciones:**  
	- a. `2-f`.  
	- b. `1-10`.  
	- c. `n-3`.  
	- d. Ninguna de las anteriores es correcta.  

## U5 - PostgreSQL y tipos avanzados

1. **La sentencia que se utiliza en Java para eliminar datos en PostgreSQL es:**
   - `sta.executeQuery(String sentenciaSQL)`
   - `sta.execute(String sentenciaSQL)`
   - `sta.executeDelete(String sentenciaSQL)`
   - `sta.executeUpdate(String sentenciaSQL)`

2. **En PostgreSQL, al hacer UPDATE de un campo tipo Array indicando posición:**
   - Si la posición no existe → error
   - Si la posición está ocupada → no hace UPDATE
   - Si la posición no existe → la crea (incluyendo intermedias)
   - Los arrays no se pueden actualizar

3. **Método de ResultSet para obtener referencia a array en PostgreSQL:**
   - `getList()`
   - `getCollection()`
   - `getArrayList()`
   - `getArray()`

4. **Objeto JDBC para trabajar con arrays:**
   - `java.sql.Array`
   - `java.util.Arrays`
   - `java.util.List`
   - `java.lang.Array`

5. **Afirmación correcta sobre tipos compuestos en PostgreSQL:**
   - Se pueden crear sin especificar tipos de atributos
   - Deben tener mínimo 3 atributos
   - No pueden contener arrays
   - Se declaran como tablas pero sin restricciones

6. **Tipo de colección soportado por PostgreSQL:**
   - LIST
   - SET
   - ARRAY
   - MULTISET

7. **Para acceder a atributo de campo tipo compuesto:**
   - Usar nombre de tabla coincidente
   - Nombre de tabla entre paréntesis
   - Nombre del campo entre comillas dobles
   - Nombre del campo entre paréntesis

8. **Método para recuperar columna BOOLEAN en JDBC:**
   - `getBit()`
   - `getString()`
   - `getBoolean()`
   - `getInt()`

9. **Sobre colecciones (agrupaciones multidimensionales):**
   - PostgreSQL solo soporta LIST
   - PostgreSQL solo soporta ARRAY
   - PostgreSQL soporta MULTIARRAY
   - PostgreSQL soporta SET

10. **Estructura de valores de objeto SQL en PostgreSQL:**
	- Con corchetes []
	- Formato JSON
	- Entre paréntesis separados por comas
	- Separados por punto y coma

11. **Diferencia entre tipo compuesto y tabla normal:**
	- Tipos no tienen restricciones
	- No se puede usar nombre de tabla existente como tipo
	- Se crean igual
	- Tablas tienen campos ilimitados

12. **Método para registrar mapeo tipo PostgreSQL → clase Java:**
	- `addDataType()`
	- `setJavaMapping()`
	- `mapSQLType()`
	- `registerJavaType()`

13. **Seleccionar segundo elemento de array en PostgreSQL:**
	- `SELECT emails(2) FROM Clients`
	- `SELECT emails[2] FROM Clients`
	- `SELECT emails->2 FROM Clients`
	- `SELECT emails[0] FROM Clients`

14. **En `UPDATE ciutat SET monumental=1 WHERE id=123`:**
	- 'monumental' es booleano
	- Inserta valor 1 en todos los registros
	- 'monumental' es numérico
	- Actualiza campo booleano del registro 123

15. **Insertar valores estructurados en tabla:**
	- No es posible
	- Usando ROW
	- Usando STRUCT
	- Campo estructurado entre comillas dobles

16. **Forma NO válida para insertar ARRAY:**
	- `ARRAY['email1@mail.com', 'email2@mail.com']`
	- `'email1@mail.com,email2@mail.com'`
	- `ARRAY[]`
	- `'{"email1@mail.com","email2@mail.com"}'`

17. **Retorno de getObject() con tipos definidos por usuario:**
	- `java.util.Object`
	- `java.sql.Struct`
	- `java.lang.Object`
	- `org.postgresql.util.PGobject`

18. **Evitar que tipo compuesto tenga nombre de tabla existente:**
	- Porque tablas crean automáticamente tipo con su nombre
	- Porque no se pueden definir tipos compuestos
	- Porque solo se usan en tablas separadas
	- Porque máximo 5 atributos

19. **Sintaxis correcta para actualizar atributo de tipo compuesto:**
	- `UPDATE Clients SET telefon`
	- `UPDATE Clients SET telefon->numero`
	- `UPDATE Clients SET telefon.numero`
	- `UPDATE Clients SET (telefon).numero`

20. **Característica principal de PostgreSQL:**
	- Ninguna es propia de PostgreSQL
	- Bloqueo exclusivo al escribir
	- No requiere definir funciones
	- Usa un único tipo nativo universal

## U6 - MongoDB y Java

1. **Codecs en MongoDB:**
   - Mapean documentos ↔ objetos Java
   - Son excepciones de acceso a BD
   - Definen operaciones CRUD
   - Permiten conexión con BD

2. **Campo identificador único en documento:**
   - `primary_key`
   - `id_autoincrement`
   - `mongo_key`
   - `_id`

3. **Método para eliminar colección:**
   - `remove()`
   - `delete()`
   - `drop()`
   - `truncate()`

4. **Eliminar documentos que cumplen filtro:**
   - `removeAll(Bson filtro)`
   - `delete(Bson filtro)`
   - `removeMany(Bson filtro)`
   - `deleteMany(Bson filtro)`

5. **Operador $gt en consultas:**
   - Valor menor que dado
   - Valor diferente
   - Valor igual
   - Valor mayor que dado

6. **Ventaja de indexación:**
   - Duplica datos por seguridad
   - Asegura integridad referencial
   - Reduce tamaño documentos
   - Mejora velocidad de búsqueda

7. **Ejecutar JavaScript en servidor:**
   - Reemplaza SQL
   - Permite consultas personalizadas
   - JavaScript más rápido que BSON
   - Obligatorio usar solo JavaScript

8. **Comando para eliminar documentos con filtro:**
   - `removeAll`
   - `deleteMany`
   - `dropDocuments`
   - `deleteAll`

9. **Obtener colección desde base de datos:**
   - `getCollections()`
   - `listCollections()`
   - `listCollectionNames()`
   - `getCollection(String nombre)`

10. **Constructor NO válido de Document:**
	- `new Document(String, Object)`
	- `Document.parse(HashSet valores)`
	- `new Document(HashMap)`
	- `new Document()`

11. **Inconveniente principal de MongoDB:**
	- No escala horizontalmente
	- No implementa ACID completo
	- No almacena datos binarios
	- No permite consultas complejas

12. **En MongoDB, un documento es...**
	- Objeto JSON válido
	- Fila de tabla
	- Estructura XML fija
	- Colección de registros

13. **MongoDB es una base de datos...**
	- Orientada a documentos
	- Orientada a gráficos
	- Solo para datos XML
	- Basada en tablas relacionales

14. **Insertar documento en colección:**
	- `add(Document doc)`
	- `insertOne(Document doc)`
	- `save(Document doc)`
	- `insert(Document doc)`

15. **Añadir propiedad a documento:**
	- `add(String nombre, Object valor)`
	- `append(String nombre, Object valor)`
	- `put(String nombre, Object valor)`
	- `set(String nombre, Object valor)`

16. **Operador para modificar campo:**
	- `$set`
	- `$updateField`
	- `$change`
	- `$modify`

17. **Modificar primer documento con filtro:**
	- `updateOne(Bson filtro, Bson cambios)`
	- `modifyOne(Bson filtro, Bson cambios)`
	- `changeOne(Bson filtro, Bson cambios)`
	- `update(Bson filtro, Bson cambios)`

18. **Excluir campo _id en consulta:**
	- `excludeId()`
	- `removeId()`
	- `withoutId()`
	- `hideId()`

19. **Operador para igualdad:**
	- `eq(String campo, valor)`
	- `is(String campo, valor)`
	- `compare(String campo, valor)`
	- `equals(String campo, valor)`

20. **Operador para agrupar en Aggregation Pipeline:**
	- `$aggregate`
	- `$sum`
	- `$group`
	- `$collect`
