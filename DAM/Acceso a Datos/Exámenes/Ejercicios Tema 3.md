# Ejercicios TEMA 3: JDBC

## Instrucciones

1. Crea un proyecto para hacer los ejercicios o aprovecha el del bloque de ejercicios anterior.
2. Crea un paquete donde guardarás todas las clases creadas en estos ejercicios.
3. Crea otro paquete con una clase con main. Desde esta clase prueba todos los métodos creados en los ejercicios.
4. Crea una excepción para tratar los errores propios de la aplicación (o reaprovecha la del bloque anterior).
5. Propaga las excepciones hasta el main y tratándolas allí.
6. Descarga el driver JDBC para MySQL y añádelo al classpath del proyecto.

## Ejercicios

### Ejercicio 1: Clase ConexionBD

**Descripción**: Esta clase proporciona métodos para establecer y gestionar conexiones a una base de datos MySQL. Implementa el patrón Singleton para asegurar que solo exista una instancia de la conexión en toda la aplicación, lo que optimiza el uso de recursos y simplifica la gestión de conexiones.

```java
package com.example.jdbc; // Define el paquete donde se encuentra la clase

import java.sql.Connection; // Para manejar conexiones a la base de datos
import java.sql.DriverManager; // Para obtener conexiones a la base de datos
import java.sql.SQLException; // Para manejar excepciones de SQL

/**
 * Clase para gestionar la conexión a la base de datos.
 * Implementa el patrón Singleton para asegurar una única instancia de conexión.
 */
public class ConexionBD {
    
    // Constantes para la conexión
    private static final String URL = "jdbc:mysql://localhost:3306/biblioteca"; // URL
    private static final String USUARIO = "root"; // Usuario
    private static final String PASSWORD = "password"; // Contraseña
    
    // Instancia única de la clase (patrón Singleton)
    private static ConexionBD instancia;
    
    // Objeto de conexión a la BD
    private Connection conexion;
    
    /**
     * Constructor privado para evitar instanciación directa (patrón Singleton).
     * Carga el driver JDBC y establece la conexión a la base de datos.
     * @throws MiExcepcion Si hay algún error al cargar el driver o conectar a la BD
     */
    private ConexionBD() throws MiExcepcion {
        try {
            // Cargamos el driver JDBC para MySQL
            // Esto registra el driver en el DriverManager
            Class.forName("com.mysql.cj.jdbc.Driver");
            
            // Establecemos la conexión con la base de datos
            // DriverManager.getConnection devuelve un objeto Connection
            conexion = DriverManager.getConnection(URL, USUARIO, PASSWORD);
            
            // Verificamos que la conexión no sea nula
            if (conexion == null) {
                throw new MiExcepcion("No se pudo establecer la conexión a la base de datos");
            }
            
            // Configuramos la conexión para que no haga autocommit
            // Esto nos permite controlar las transacciones manualmente
            conexion.setAutoCommit(false);
            
            System.out.println("Conexión establecida con éxito a: " + URL);
        } catch (ClassNotFoundException e) {
            throw new MiExcepcion("Error al cargar el driver JDBC: " + e.getMessage(), e);
        } catch (SQLException e) {
            throw new MiExcepcion("Error al conectar a la base de datos: " + e.getMessage(), e);
        }
    }
    
    /**
     * Método estático para obtener la instancia única de la clase (patrón Singleton).
     * Si la instancia no existe, la crea; si existe, la devuelve.
     * @return Instancia única de ConexionBD
     * @throws MiExcepcion Si hay algún error al crear la instancia
     */
    public static synchronized ConexionBD getInstancia() throws MiExcepcion {
        // Si la instancia no existe, la creamos
        if (instancia == null) {
            instancia = new ConexionBD();
        }
        return instancia;
    }
    
    /**
     * Obtiene el objeto Connection para realizar operaciones en la base de datos.
     * @return Objeto Connection
     */
    public Connection getConexion() {
        return conexion;
    }
    
    /**
     * Cierra la conexión a la base de datos.
     * @throws MiExcepcion Si hay algún error al cerrar la conexión
     */
    public void cerrarConexion() throws MiExcepcion {
        try {
            // Verificamos que la conexión no sea nula y no esté cerrada
            if (conexion != null && !conexion.isClosed()) {
                // Cerramos la conexión
                conexion.close();
                System.out.println("Conexión cerrada con éxito");
            }
        } catch (SQLException e) {
            throw new MiExcepcion("Error al cerrar la conexión: " + e.getMessage(), e);
        } finally {
            // Establecemos la instancia a null para que se pueda crear una nueva
            instancia = null;
        }
    }
    
    /**
     * Confirma los cambios realizados en la base de datos (commit).
     * @throws MiExcepcion Si hay algún error al confirmar los cambios
     */
    public void confirmarCambios() throws MiExcepcion {
        try {
            // Verificamos que la conexión no sea nula y no esté cerrada
            if (conexion != null && !conexion.isClosed()) {
                // Confirmamos los cambios (commit)
                conexion.commit();
                System.out.println("Cambios confirmados con éxito");
            }
        } catch (SQLException e) {
            throw new MiExcepcion("Error al confirmar los cambios: " + e.getMessage(), e);
        }
    }
    
    /**
     * Deshace los cambios realizados en la base de datos (rollback)
     * @throws MiExcepcion Si hay algún error al deshacer los cambios
     */
    public void deshacerCambios() throws MiExcepcion {
        try {
            // Verificamos que la conexión no sea nula y no esté cerrada
            if (conexion != null && !conexion.isClosed()) {
                // Deshacemos los cambios (rollback)
                conexion.rollback();
                System.out.println("Cambios deshechos con éxito");
            }
        } catch (SQLException e) {
            throw new MiExcepcion("Error al deshacer los cambios: " + e.getMessage(), e);
        }
    }
}
```

### Ejercicio 2: Clase Libro

**Descripción**: Esta clase representa la entidad Libro en la aplicación, con atributos como ISBN, título, autor, etc. Proporciona métodos para acceder y modificar estos atributos, así como para representar el libro como una cadena de texto. Es una clase POJO (Plain Old Java Object) que se utilizará para mapear los registros de la tabla de libros en la base de datos.

```java
package com.example.jdbc; // Define el paquete donde se encuentra la clase

/**
 * Clase que representa un libro en la biblioteca.
 * Contiene los atributos básicos de un libro y métodos para acceder a ellos.
 */
public class Libro {
    
    // Atributos de la clase
    private String isbn; // ISBN del libro (identificador único)
    private String titulo; // Título del libro
    private String autor; // Autor del libro
    private int anioPublicacion; // Año de publicación
    private String editorial; // Editorial del libro
    private int numPaginas; // Número de páginas
    
    /**
     * Constructor por defecto.
     * Inicializa un libro con valores vacíos.
     */
    public Libro() {
        this.isbn = "";
        this.titulo = "";
        this.autor = "";
        this.anioPublicacion = 0;
        this.editorial = "";
        this.numPaginas = 0;
    }
    
    /**
     * Constructor con parámetros.
     * Inicializa un libro con los valores proporcionados.
     * @param isbn ISBN del libro
     * @param titulo Título del libro
     * @param autor Autor del libro
     * @param anioPublicacion Año de publicación
     * @param editorial Editorial del libro
     * @param numPaginas Número de páginas
     */
    public Libro(String isbn,
		    String titulo,
		    String autor,
		    int anioPublicacion, 
            String editorial,
            int numPaginas)
            {
        this.isbn = isbn;
        this.titulo = titulo;
        this.autor = autor;
        this.anioPublicacion = anioPublicacion;
        this.editorial = editorial;
        this.numPaginas = numPaginas;
    }
    
    // Métodos getter y setter para cada atributo

    public String getIsbn() {
        return isbn;
    }
    
    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }
    
    public String getTitulo() {
        return titulo;
    }
    
    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }
    
    public String getAutor() {
        return autor;
    }
    
    public void setAutor(String autor) {
        this.autor = autor;
    }
    
    public int getAnioPublicacion() {
        return anioPublicacion;
    }
    
    public void setAnioPublicacion(int anioPublicacion) {
        this.anioPublicacion = anioPublicacion;
    }

    public String getEditorial() {
        return editorial;
    }

    public void setEditorial(String editorial) {
        this.editorial = editorial;
    }

    public int getNumPaginas() {
        return numPaginas;
    }

    public void setNumPaginas(int numPaginas) {
        this.numPaginas = numPaginas;
    }
    
    /**
     * Devuelve una representación en texto del libro.
     * Útil para depuración y visualización.
     * @return Representación en texto del libro
     */
    @Override
    public String toString() {
        return "Libro{" +
                "isbn='" + isbn + '\'' +
                ", titulo='" + titulo + '\'' +
                ", autor='" + autor + '\'' +
                ", anioPublicacion=" + anioPublicacion +
                ", editorial='" + editorial + '\'' +
                ", numPaginas=" + numPaginas +
                '}';
    }
}
```

### Ejercicio 3: Clase LibroDAO

**Descripción**: Esta clase implementa el patrón DAO (Data Access Object) para la entidad Libro, proporcionando métodos para realizar operaciones CRUD (Create, Read, Update, Delete) en la base de datos. Encapsula la lógica de acceso a datos, separándola de la lógica de negocio, lo que mejora la mantenibilidad y modularidad del código.

```java
package com.example.jdbc; // Define el paquete donde se encuentra la clase

import java.sql.Connection; // Para manejar conexiones a la base de datos
import java.sql.PreparedStatement; // Para ejecutar consultas SQL parametrizadas
import java.sql.ResultSet; // Para almacenar los resultados de las consultas
import java.sql.SQLException; // Para manejar excepciones de SQL
import java.sql.Statement; // Para ejecutar consultas SQL simples
import java.util.ArrayList; // Para almacenar listas de libros
import java.util.List; // Interfaz para listas

/**
 * Clase que implementa el patrón DAO (Data Access Object) para la entidad Libro.
 * Proporciona métodos para realizar operaciones CRUD en la tabla de libros.
 */
public class LibroDAO {
    
    // Consultas SQL
    private static final String SQL_INSERT = 
        "INSERT INTO libros (isbn, titulo, autor, anio_publicacion, editorial, num_paginas) " +
        "VALUES (?, ?, ?, ?, ?, ?)";
    
    private static final String SQL_UPDATE = 
        "UPDATE libros SET titulo = ?, autor = ?, anio_publicacion = ?, " +
        "editorial = ?, num_paginas = ? WHERE isbn = ?";
    
    private static final String SQL_DELETE = 
        "DELETE FROM libros WHERE isbn = ?";
    
    private static final String SQL_SELECT_ALL = 
        "SELECT isbn, titulo, autor, anio_publicacion, editorial, num_paginas " +
        "FROM libros";
    
    private static final String SQL_SELECT_BY_ISBN = 
        "SELECT isbn, titulo, autor, anio_publicacion, editorial, num_paginas " +
        "FROM libros WHERE isbn = ?";
    
    // Conexión a la base de datos
    private Connection conexion;
    
    /**
     * Constructor que recibe una conexión a la base de datos.
     * @param conexion Conexión a la base de datos
     */
    public LibroDAO(Connection conexion) {
        this.conexion = conexion;
    }
    
    /**
     * Inserta un nuevo libro en la base de datos.
     * @param libro Libro a insertar
     * @return true si la inserción fue exitosa, false en caso contrario
     * @throws MiExcepcion Si hay algún error durante la inserción
     */
    public boolean insertar(Libro libro) throws MiExcepcion {
        PreparedStatement ps = null;
        
        try {
            // Preparamos la consulta SQL con parámetros
            ps = conexion.prepareStatement(SQL_INSERT);
            
            // Establecemos los valores de los parámetros
            // Los índices empiezan en 1 y corresponden a los ? en la consulta
            ps.setString(1, libro.getIsbn());
            ps.setString(2, libro.getTitulo());
            ps.setString(3, libro.getAutor());
            ps.setInt(4, libro.getAnioPublicacion());
            ps.setString(5, libro.getEditorial());
            ps.setInt(6, libro.getNumPaginas());
            
            // Ejecutamos la consulta y obtenemos el número de filas afectadas
            int filasAfectadas = ps.executeUpdate();
            
            // Si se afectó al menos una fila, la inserción fue exitosa
            return filasAfectadas > 0;
        } catch (SQLException e) {
            throw new MiExcepcion("Error al insertar libro: " + e.getMessage(), e);
        } finally {
            // Cerramos el PreparedStatement
            cerrarStatement(ps);
        }
    }
    
    /**
     * Actualiza un libro existente en la base de datos.
     * @param libro Libro con los nuevos datos
     * @return true si la actualización fue exitosa, false en caso contrario
     * @throws MiExcepcion Si hay algún error durante la actualización
     */
    public boolean actualizar(Libro libro) throws MiExcepcion {
        PreparedStatement ps = null;
        
        try {
            // Preparamos la consulta SQL con parámetros
            ps = conexion.prepareStatement(SQL_UPDATE);
            
            // Establecemos los valores de los parámetros
            ps.setString(1, libro.getTitulo());
            ps.setString(2, libro.getAutor());
            ps.setInt(3, libro.getAnioPublicacion());
            ps.setString(4, libro.getEditorial());
            ps.setInt(5, libro.getNumPaginas());
            ps.setString(6, libro.getIsbn()); // El ISBN es la clave primaria
            
            // Ejecutamos la consulta y obtenemos el número de filas afectadas
            int filasAfectadas = ps.executeUpdate();
            
            // Si se afectó al menos una fila, la actualización fue exitosa
            return filasAfectadas > 0;
        } catch (SQLException e) {
            throw new MiExcepcion("Error al actualizar libro: " + e.getMessage(), e);
        } finally {
            // Cerramos el PreparedStatement
            cerrarStatement(ps);
        }
    }
    
    /**
     * Elimina un libro de la base de datos por su ISBN.
     * @param isbn ISBN del libro a eliminar
     * @return true si la eliminación fue exitosa, false en caso contrario
     * @throws MiExcepcion Si hay algún error durante la eliminación
     */
    public boolean eliminar(String isbn) throws MiExcepcion {
        PreparedStatement ps = null;
        
        try {
            // Preparamos la consulta SQL con parámetros
            ps = conexion.prepareStatement(SQL_DELETE);
            
            // Establecemos el valor del parámetro
            ps.setString(1, isbn);
            
            // Ejecutamos la consulta y obtenemos el número de filas afectadas
            int filasAfectadas = ps.executeUpdate();
            
            // Si se afectó al menos una fila, la eliminación fue exitosa
            return filasAfectadas > 0;
        } catch (SQLException e) {
            throw new MiExcepcion("Error al eliminar libro: " + e.getMessage(), e);
        } finally {
            // Cerramos el PreparedStatement
            cerrarStatement(ps);
        }
    }
    
    /**
     * Obtiene todos los libros de la base de datos.
     * @return Lista de todos los libros
     * @throws MiExcepcion Si hay algún error durante la consulta
     */
    public List<Libro> obtenerTodos() throws MiExcepcion {
        PreparedStatement ps = null;
        ResultSet rs = null;
        List<Libro> libros = new ArrayList<>();
        
        try {
            // Preparamos la consulta SQL
            ps = conexion.prepareStatement(SQL_SELECT_ALL);
            
            // Ejecutamos la consulta y obtenemos los resultados
            rs = ps.executeQuery();
            
            // Recorremos los resultados y creamos objetos Libro
            while (rs.next()) {
                Libro libro = new Libro();
                libro.setIsbn(rs.getString("isbn"));
                libro.setTitulo(rs.getString("titulo"));
                libro.setAutor(rs.getString("autor"));
                libro.setAnioPublicacion(rs.getInt("anio_publicacion"));
                libro.setEditorial(rs.getString("editorial"));
                libro.setNumPaginas(rs.getInt("num_paginas"));
                
                // Añadimos el libro a la lista
                libros.add(libro);
            }
            
            return libros;
        } catch (SQLException e) {
            throw new MiExcepcion("Error al obtener todos los libros: " + e.getMessage(), e);
        } finally {
            // Cerramos el ResultSet y el PreparedStatement
            cerrarResultSet(rs);
            cerrarStatement(ps);
        }
    }
    
    /**
     * Obtiene un libro de la base de datos por su ISBN.
     * @param isbn ISBN del libro a buscar
     * @return Libro encontrado o null si no existe
     * @throws MiExcepcion Si hay algún error durante la consulta
     */
    public Libro obtenerPorIsbn(String isbn) throws MiExcepcion {
        PreparedStatement ps = null;
        ResultSet rs = null;
        Libro libro = null;
        
        try {
            // Preparamos la consulta SQL con parámetros
            ps = conexion.prepareStatement(SQL_SELECT_BY_ISBN);
            
            // Establecemos el valor del parámetro
            ps.setString(1, isbn);
            
            // Ejecutamos la consulta y obtenemos los resultados
            rs = ps.executeQuery();
            
            // Si hay un resultado, creamos un objeto Libro
            if (rs.next()) {
                libro = new Libro();
                libro.setIsbn(rs.getString("isbn"));
                libro.setTitulo(rs.getString("titulo"));
                libro.setAutor(rs.getString("autor"));
                libro.setAnioPublicacion(rs.getInt("anio_publicacion"));
                libro.setEditorial(rs.getString("editorial"));
                libro.setNumPaginas(rs.getInt("num_paginas"));
            }
            return libro;
        } catch (SQLException e) {
            throw new MiExcepcion("Error al obtener libro por ISBN: " + e.getMessage(), e);
        } finally {
            // Cerramos el ResultSet y el PreparedStatement
            cerrarResultSet(rs);
            cerrarStatement(ps);
        }
    }
    
    /**
     * Cierra un objeto Statement o PreparedStatement.
     * @param st Statement a cerrar
     */
    private void cerrarStatement(Statement st) {
        if (st != null) {
            try {
                st.close();
            } catch (SQLException e) {
                System.err.println("Error al cerrar Statement: " + e.getMessage());
            }
        }
    }
    
    /**
     * Cierra un objeto ResultSet.
     * @param rs ResultSet a cerrar
     */
    private void cerrarResultSet(ResultSet rs) {
        if (rs != null) {
            try {
                rs.close();
            } catch (SQLException e) {
                System.err.println("Error al cerrar ResultSet: " + e.getMessage());
            }
        }
    }
}
```

### Ejercicio 4: Clase MiExcepcion

**Descripción**: Esta clase representa una excepción personalizada para la aplicación, que permite encapsular y propagar errores específicos de manera controlada. Es especialmente útil para manejar errores relacionados con la base de datos y convertir excepciones técnicas en mensajes más comprensibles para el usuario.

```java
package com.example.jdbc; // Define el paquete donde se encuentra la clase

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
     * @param mensaje Mensaje descriptivo del error
     */
    public MiExcepcion(String mensaje) {
        super(mensaje);
    }
    
    /**
     * Constructor con mensaje y causa.
     * Útil para encapsular excepciones de bajo nivel.
     * @param mensaje Mensaje descriptivo del error
     * @param causa Excepción original que causó el error
     */
    public MiExcepcion(String mensaje, Throwable causa) {
        super(mensaje, causa);
    }
}
```

### Ejercicio 5: Clase PruebasJDBC (con main)

**Descripción**: Esta clase contiene el método main y métodos para probar todas las funcionalidades implementadas en las clases anteriores. Aquí se realizan pruebas de conexión a la base de datos y operaciones CRUD sobre la tabla de libros, demostrando el uso de JDBC para interactuar con una base de datos relacional.

```java
package com.example.main; // Define el paquete de la clase principal

import java.sql.Connection; // Para manejar conexiones a DB
import java.util.List; // Para trabajar con listas

import com.example.jdbc.ConexionBD; // Importamos la clase de conexión
import com.example.jdbc.Libro; // Importamos la clase Libro
import com.example.jdbc.LibroDAO; // Importamos la clase DAO
import com.example.jdbc.MiExcepcion; // Importamos excepción personalizada

/**
 * Clase principal para probar las funcionalidades de JDBC.
 * Contiene el método main y métodos para probar cada aspecto de la conexión y operaciones CRUD.
 */
public class PruebasJDBC {
    
    /**
     * Método principal que ejecuta las pruebas.
     * @param args Argumentos de línea de comandos (no utilizados)
     */
    public static void main(String[] args) {
        try {
            // Obtenemos la instancia de conexión a la BD
            ConexionBD conexionBD = ConexionBD.getInstancia();
            Connection conexion = conexionBD.getConexion();
            
            // Creamos un objeto LibroDAO con la conexión
            LibroDAO libroDAO = new LibroDAO(conexion);
            
            // Probamos las diferentes operaciones CRUD
            probarInsercion(libroDAO);
            probarConsulta(libroDAO);
            probarActualizacion(libroDAO);
            probarEliminacion(libroDAO);
            
            // Confirmamos los cambios en la base de datos
            conexionBD.confirmarCambios();
            
            // Cerramos la conexión
            conexionBD.cerrarConexion();
            
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
	        "El Quijote",
	        "Miguel de Cervantes", 
            1605,
            "Alfaguara",
            863
        );
        
        Libro libro2 = new Libro(
	        "9788420412146",
	        "Cien años de soledad",
	        "Gabriel García Márquez",
	        1967,
	        "Cátedra",
	        471
	    );
        
        // Insertamos los libros en la base de datos
        boolean resultado1 = libroDAO.insertar(libro1);
        boolean resultado2 = libroDAO.insertar(libro2);
        
        // Mostramos los resultados
        System.out.println("Inserción de libro 1: " + (resultado1 ? "Exitosa" : "Fallida"));
        System.out.println("Inserción de libro 2: " + (resultado2 ? "Exitosa" : "Fallida"));
    }
    
    /**
     * Prueba la consulta de libros en la base de datos.
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
        String isbn = "9788401352836"; // ISBN de "El Quijote"
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
     * @param libroDAO Objeto DAO para realizar operaciones con libros
     * @throws MiExcepcion Si hay algún error durante la actualización
     */
    private static void probarActualizacion(LibroDAO libroDAO) throws MiExcepcion {
        System.out.println("\n=== Prueba de Actualización ===");
        
        // Obtenemos un libro existente
        String isbn = "9788401352836"; // ISBN de "El Quijote"
        Libro libro = libroDAO.obtenerPorIsbn(isbn);
        
        if (libro != null) {
            // Mostramos el libro antes de la actualización
            System.out.println("Libro antes de actualizar:");
            System.out.println("  " + libro);
            
            // Modificamos algunos datos del libro
            libro.setTitulo("Don Quijote de la Mancha");
            libro.setEditorial("Real Academia Española");
            libro.setNumPaginas(1250);
            
            // Actualizamos el libro en la base de datos
            boolean resultado = libroDAO.actualizar(libro);
            
            // Mostramos el resultado
            System.out.println("Actualización: " + (resultado ? "Exitosa" : "Fallida"));
            
            // Consultamos el libro actualizado
            Libro libroActualizado = libroDAO.obtenerPorIsbn(isbn);
            
            // Mostramos el libro después de la actualización
            System.out.println("Libro después de actualizar:");
            System.out.println("  " + libroActualizado);
        } else {
            System.out.println("No se encontró un libro con ISBN " + isbn + " para actualizar");
        }
    }
    
    /**
     * Prueba la eliminación de libros en la base de datos.
     * @param libroDAO Objeto DAO para realizar operaciones con libros
     * @throws MiExcepcion Si hay algún error durante la eliminación
     */
    private static void probarEliminacion(LibroDAO libroDAO) throws MiExcepcion {
        System.out.println("\n=== Prueba de Eliminación ===");
        
        // ISBN del libro a eliminar
        String isbn = "9788420412146"; // ISBN de "Cien años de soledad"
        
        // Verificamos que el libro existe antes de eliminarlo
        Libro libro = libroDAO.obtenerPorIsbn(isbn);
        
        if (libro != null) {
            // Mostramos el libro a eliminar
            System.out.println("Libro a eliminar:");
            System.out.println("  " + libro);
            
            // Eliminamos el libro de la base de datos
            boolean resultado = libroDAO.eliminar(isbn);
            
            // Mostramos el resultado
            System.out.println("Eliminación: " + (resultado ? "Exitosa" : "Fallida"));
            
            // Verificamos que el libro ya no existe
            Libro libroEliminado = libroDAO.obtenerPorIsbn(isbn);
            
            if (libroEliminado == null) {
                System.out.println(
	            "El libro con ISBN " + isbn + " ya no existe en la base de datos");
            } else {
                System.out.println(
	            "¡Error! El libro con ISBN " + isbn + " todavía existe en la base de datos");
            }
        } else {
            System.out.println(
            "No se encontró un libro con ISBN " + isbn + " para eliminar");
        }
    }
}
```

### Script SQL para crear la base de datos

**Descripción**: Este script SQL crea la base de datos y la tabla necesaria para los ejercicios. Debe ejecutarse en el servidor MySQL antes de ejecutar las pruebas de JDBC.

```sql
-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS biblioteca;

-- Usar la base de datos
USE biblioteca;

-- Crear la tabla de libros
CREATE TABLE IF NOT EXISTS libros (
    isbn VARCHAR(20) PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    anio_publicacion INT,
    editorial VARCHAR(50),
    num_paginas INT
);

-- Eliminar datos existentes (opcional)
-- TRUNCATE TABLE libros;
```
