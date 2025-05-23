# **Ejercicios TEMA 3.** <br>JDBC

## Instrucciones

- Crea un proyecto si puede ser con maven.
    
- Crea un paquete llamado cat.paucasesnovescifp.swpro.jdbc.
    
- Crea la clase PruebasJDBC con main en el paquete cat.paucasesnovescifp.swpro.jdbc. Será la única clase que pueda interactuar con el usuario (pantalla, teclado, ..)
    
- Crea los paquetes cat.paucasesnovescifp.swpro.jdbc.baseDades, cat.paucasesnovescifp.swpro.jdbc.auxiliares y cat.paucasesnovescifp.swpro.jdbc.dades.
    
- Utiliza la base de datos de la biblioteca para hacer los ejercicios.
    
- Baja el driver de MySql. Puedes utilizar el que está el aula virtual, bajarlo directamente de mysql o añadir la dependencia a maven.
    
    https://dev.mysql.com/downloads/connector/j/
    
    Si lo bajas de la web escoge la opción independiente de la plataforma. Descarga el zip. Descomprime el zip. Se generará una carpeta y dentro de ella hay un jar. Incluye al proyecto el jar del driver.
    

#### Datos de la conexión  

**Host**: daw.paucasesnovescifp.cat
**Puerto**: 3306
**Base de datos**: biblioteca
**Usuario**: usuario
**Contraseña**: seCret_24

**Importante**: La base de datos se reinicializa cada noche a las tres de la madrugada. Si, por ejemplo, hoy hacéis insertos o updates mañana no los encontraréis.  

  

## Ejercicios

1. En el paquete auxiliares crea una excepción, _JDBCException_, con el constructor vacía y otro con un parámetro para el mensaje.
    
2. En el paquete _baseDades_ crea la clase _BibliotecaDao_ con un atributo _String_ para la _url_ de la conexión y un objeto _Properties_ para las propiedades.
    
    1. Crea un constructor con parámetros para los dos datos, los getters y los setters.
        
    2. Debe ser imposible asignar a los atributos como url un null o una cadena vacía y como propiedades un null o un objeto sin propiedad alguna.
        
    3. Esta clase no puede mostrar nada por pantalla, ni siquiera las excepciones.
        
3. En la clase _PruebasJDBC_ crea un objeto de la clase _BibliotecaDao_ configurado de manera que se pueda conectar a la biblioteca.
    
4. Crea un método en la clase _BibliotecaDao_ que devuelva todas las lenguas que hay en la base de datos. Lo puede hacer como una lista de _String_. En la clase _PruebasJDBC_ muestra las lenguas que vuelve el método anterior.
    
5. Crea un método en la clase _BibliotecaDao_ que reciba como parámetro el valor de una lengua y lo inserte en la base de datos. Si hay algún error debe tirar una excepción. Llamalo desde el main.
    
6. Crea un método en la clase _BibliotecaDao_ que reciba como parámetro el valor de una lengua y el borrado de la base de datos. Procura que sea una que no active ningún cascade. Si hay algún error debe tirar una excepción. Llamárselo desde el main pasándole alguna de las lenguas que has ido probando el ejercicio anterior...
    
7. Crea un método en la clase _BibliotecaDao_ que reciba como parámetro el valor de una lengua y devuelva los títulos de todos los libros que contiendan este valor como clave foráneo. Pruebalo desde _PruebasJDBC_.
    
8. Repite el ejercicio anterior, pero ahora utilizando un _PreparedStatement_.
    
9. Crea las clases:
    
    1. En el paquete datos dos POJOS por las tablas _Nacionalidad_ y _Autor_.
        
    2. Deben tener un constructor sin parámetros, otro con parámetros para todos los atributos y los getters.
        
    3. El nombre de la nacionalidad no puede ser nulo o una cadena sólo de blancos o vacía.
        
    4. Autor debe tener atributos para los campos de la tabla ID_AUT, NOM_AUT que no pueden ser nulo ni vaciados, y FK_NACIONALITAT que si puede ser nulo.
        
        Piensa que los nombres de los atributos de los POJOS han de seguir las reglas de nomenclatura de Java.
        
10. En la clase _BibliotecaDao_ crea los métodos:
    
    1. getNacionalidades() vuelve un objeto ArrayList<Nacionalidad> con las filas de la mesa.
        
    2. getAutor(Clave primaria Autor) vuelve un objeto Autor con los datos de la fila de la tabla con esta clave primaria.
        
    3. getAutors(Nacionalidad nacionalidad) vuelve un ArrayList<Autor> con las filas de la tabla Autores que tienen como clave forána la clave primaria de Nacionalidades.
        
    4. En la clase PruebasJDBC prueba los métodos anteriores:
        
        1. Muestra por pantalla la información de todas las nacionalidades de la base de datos.
            
        2. Muestra por pantalla la fila Autor con una cierta clave primaria.
            
        3. Muestra por pantalla a los autores asociados a una determinada nacionalidad.
            
11. Crea en la clase _BaseDades__Dao_ un método llamado _insertaNacionalidadAutores_() que reciba como a parámetro una nacionalidad y una lista de autores de esta nacionalidad. Debe insertar los mismos en la base de datos. Comprueba que la base de datos se ha actualizado correctamente, puedes utilizar los métodos hechos anteriormente para comprobarlo.
    
12. Crea el método _borraNacionalidad_() que dada una nacionalidad como parámetro el borrado de la base de datos, junto con todos los autores de esta nacionalidad. Prohibido añadir cascadas a la bbdd. Si lo hay, programa el código como si no hubiera.
    
13. Crea el método _insertaNacionalidadAutoresTransaccio_() que reciba como parámetro una nacionalidad y una lista de autores de la misma nacionalidad. Los debe insertar en la base de datos utilizando una transacción. Captura el SQLException y si ha habido un error haz un rollback.
    
14. Nos damos cuenta de que en la base de datos tenemos una lengua mal escrita. Al ser clave primaria y tiene registros asociados, no la podemos borrar directamente. Para arreglarlo, dentro de una transacción haremos lo siguiente:
    
    1. Inserta una lengua con los datos corregidas.
        
    2. Actualiza todos los libros que tienen como clave foráneo la que está mal escrita, de manera que ahora tengan la correcta.
        
    3. Borra la lengua mal escrita.
        
15. Programa un miniworkbench de consola. Haz una clase que pida por consola una sentencia SELECT, la ejecute y muestre el resultado por consola.
    
    1. Añade a _BibliotecaDao_ un método que reciba por parámetro una cadena con un SELECT, la ejecute y vuelva un array de cadenas con una cadena para cada fila del resultado. Puedes separar los distintos campos con tabuladores.
        
        Utiliza _ResultSetMetaData meta = rs.getMetaData();_ para obtener los metadatos de la consulta
        
        Utiliza _meta.getColumnCount()_ para saber cuántas columnas tiene el _resultset_.
        
        Puedes añadir una cadena al principio que incluya los nombres de las columnas:
        
        Utiliza _meta.getColumnLabel_(i) para saber el nombre de la columna i-ésima de la consulta.
        
    2. Crea una clase con main. Debe tener:
        
        1. Un atributo de la clase _BibliotecaDao_.
            
        2. Un método que lea la sentencia por teclado.
            
        3. Un método que utilice _BibliotecaDao_ para ejecutarla y que muestre el resultado por pantalla.
            
    
    **NOTA**: Puedes tratar todos los datos recuperadas como si fueran cadenas.
    
16. (Opcional) Haz la versión con GUI de ejercicio anterior. Diseña un _JFrame_ con un textarea para entrar una consulta Select, un botón para ejecutarla y otro textarea para mostrar los resultados. Se puede conectar automáticamente en la base de datos. Utiliza _ResultSet.getMetadata_(). _getColumnCount_() para saber cuántas columnas tiene el resultset.
    
    **NOTA**: Puedes tratar todos los datos recuperadas como si fueran cadenas.
    
17. (Opcional) Crea el paquete _recuerdos_. Dentro de él:
    
    1. Crea una excepción descendiente de RuntimeException para los errores de la aplicación.
        
    2. Crea un _recuerdo_ para representar a la Nacionalidad. EL nombre de la nacionalidad no puede ser null ni cadena de espacios ni cadena vacía.
        
    3. Crea un _recuerdo_ para representar al Autor. El identificador puede ser nulo ni negativo y el no puede ser null ni cadena de espacios ni cadena vacía.
        
    4. Copia la clase _BaseDadesDao_ en el paquete _recuerdos_. Modificala de manera que utilice los _recuerdos_ en lugar de los _POJOs_.
        
    5. Copia la clase con main dentro del paquete _recuerdos_ y modificala de manera que funcione con clase del punto anterior.