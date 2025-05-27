# Ejercicios TEMA 5: ORDB

## Instrucciones

1. Crea un proyecto para hacer los ejercicios o aprovecha el del bloque de ejercicios anterior.
2. Crea un paquete donde guardarás todas las clases creadas en estos ejercicios.
3. Crea otro paquete con una clase con main. Desde esta clase prueba todos los métodos creados en los ejercicios.
4. Crea una excepción para tratar los errores propios de la aplicación (o reaprovecha la del bloque anterior).
5. Propaga las excepciones hasta el main y tratándolas allí.
6. Descarga el driver JDBC para PostgreSQL y añádelo al classpath del proyecto.

## Ejercicios

### Ejercicio 1: Clase ConexionPostgreSQL

**Descripción**: Esta clase proporciona métodos para establecer y gestionar conexiones a una base de datos PostgreSQL. Implementa el patrón Singleton para asegurar que solo exista una instancia de la conexión en toda la aplicación, lo que optimiza el uso de recursos y simplifica la gestión de conexiones.

```java
package com.example.ordb; // Define el paquete donde se encuentra la clase

import java.sql.Connection; // Para manejar conexiones a la base de datos
import java.sql.DriverManager; // Para obtener conexiones a la base de datos
import java.sql.SQLException; // Para manejar excepciones de SQL

/**
 * Clase para gestionar la conexión a la base de datos PostgreSQL.
 * Implementa el patrón Singleton para asegurar una única instancia de conexión.
 */
public class ConexionPostgreSQL {
    
    // Constantes para la conexión
    private static final String URL = "jdbc:postgresql://localhost:5432/biblioteca"; // URL de conexión a la BD
    private static final String USUARIO = "postgres"; // Usuario de la BD
    private static final String PASSWORD = "postgres"; // Contraseña de la BD
    
    // Instancia única de la clase (patrón Singleton)
    private static ConexionPostgreSQL instancia;
    
    // Objeto de conexión a la BD
    private Connection conexion;
    
    /**
     * Constructor privado para evitar instanciación directa (patrón Singleton).
     * Carga el driver JDBC y establece la conexión a la base de datos.
     * 
     * @throws MiExcepcion Si hay algún error al cargar el driver o conectar a la BD
     */
    private ConexionPostgreSQL() throws MiExcepcion {
        try {
            // Cargamos el driver JDBC para PostgreSQL
            // Esto registra el driver en el DriverManager
            Class.forName("org.postgresql.Driver");
            
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
            // Error al cargar el driver JDBC
            throw new MiExcepcion("Error al cargar el driver JDBC: " + e.getMessage(), e);
        } catch (SQLException e) {
            // Error al establecer la conexión
            throw new MiExcepcion("Error al conectar a la base de datos: " + e.getMessage(), e);
        }
    }
    
    /**
     * Método estático para obtener la instancia única de la clase (patrón Singleton).
     * Si la instancia no existe, la crea; si existe, la devuelve.
     * 
     * @return Instancia única de ConexionPostgreSQL
     * @throws MiExcepcion Si hay algún error al crear la instancia
     */
    public static synchronized ConexionPostgreSQL getInstancia() throws MiExcepcion {
        // Si la instancia no existe, la creamos
        if (instancia == null) {
            instancia = new ConexionPostgreSQL();
        }
        return instancia;
    }
    
    /**
     * Obtiene el objeto Connection para realizar operaciones en la base de datos.
     * 
     * @return Objeto Connection
     */
    public Connection getConexion() {
        return conexion;
    }
    
    /**
     * Cierra la conexión a la base de datos.
     * 
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
            // Error al cerrar la conexión
            throw new MiExcepcion("Error al cerrar la conexión: " + e.getMessage(), e);
        } finally {
            // Establecemos la instancia a null para que se pueda crear una nueva
            instancia = null;
        }
    }
    
    /**
     * Confirma los cambios realizados en la base de datos (commit).
     * 
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
            // Error al confirmar los cambios
            throw new MiExcepcion("Error al confirmar los cambios: " + e.getMessage(), e);
        }
    }
    
    /**
     * Deshace los cambios realizados en la base de datos (rollback).
     * 
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
            // Error al deshacer los cambios
            throw new MiExcepcion("Error al deshacer los cambios: " + e.getMessage(), e);
        }
    }
}
```

### Ejercicio 2: Clase Direccion (Tipo Compuesto)

**Descripción**: Esta clase representa una dirección postal que se utilizará como tipo compuesto en PostgreSQL. En bases de datos objeto-relacionales, los tipos compuestos permiten agrupar varios atributos en una sola estructura, similar a una clase en programación orientada a objetos.

```java
package com.example.ordb; // Define el paquete donde se encuentra la clase

/**
 * Clase que representa una dirección postal.
 * Se utilizará como tipo compuesto en PostgreSQL.
 */
public class Direccion {
    
    // Atributos de la clase
    private String calle; // Nombre de la calle
    private int numero; // Número de la dirección
    private String piso; // Piso (puede incluir letra, por eso es String)
    private String ciudad; // Ciudad
    private String codigoPostal; // Código postal (String porque puede empezar por 0)
    
    /**
     * Constructor por defecto.
     * Inicializa una dirección con valores vacíos.
     */
    public Direccion() {
        this.calle = "";
        this.numero = 0;
        this.piso = "";
        this.ciudad = "";
        this.codigoPostal = "";
    }
    
    /**
     * Constructor con parámetros.
     * Inicializa una dirección con los valores proporcionados.
     * 
     * @param calle Nombre de la calle
     * @param numero Número de la dirección
     * @param piso Piso (puede incluir letra)
     * @param ciudad Ciudad
     * @param codigoPostal Código postal
     */
    public Direccion(String calle, int numero, String piso, String ciudad, String codigoPostal) {
        this.calle = calle;
        this.numero = numero;
        this.piso = piso;
        this.ciudad = ciudad;
        this.codigoPostal = codigoPostal;
    }
    
    /**
     * Obtiene el nombre de la calle.
     * 
     * @return Nombre de la calle
     */
    public String getCalle() {
        return calle;
    }
    
    /**
     * Establece el nombre de la calle.
     * 
     * @param calle Nuevo nombre de la calle
     */
    public void setCalle(String calle) {
        this.calle = calle;
    }
    
    /**
     * Obtiene el número de la dirección.
     * 
     * @return Número de la dirección
     */
    public int getNumero() {
        return numero;
    }
    
    /**
     * Establece el número de la dirección.
     * 
     * @param numero Nuevo número de la dirección
     */
    public void setNumero(int numero) {
        this.numero = numero;
    }
    
    /**
     * Obtiene el piso.
     * 
     * @return Piso (puede incluir letra)
     */
    public String getPiso() {
        return piso;
    }
    
    /**
     * Establece el piso.
     * 
     * @param piso Nuevo piso
     */
    public void setPiso(String piso) {
        this.piso = piso;
    }
    
    /**
     * Obtiene la ciudad.
     * 
     * @return Ciudad
     */
    public String getCiudad() {
        return ciudad;
    }
    
    /**
     * Establece la ciudad.
     * 
     * @param ciudad Nueva ciudad
     */
    public void setCiudad(String ciudad) {
        this.ciudad = ciudad;
    }
    
    /**
     * Obtiene el código postal.
     * 
     * @return Código postal
     */
    public String getCodigoPostal() {
        return codigoPostal;
    }
    
    /**
     * Establece el código postal.
     * 
     * @param codigoPostal Nuevo código postal
     */
    public void setCodigoPostal(String codigoPostal) {
        this.codigoPostal = codigoPostal;
    }
    
    /**
     * Convierte la dirección a una cadena en formato PostgreSQL.
     * Formato: (calle, numero, piso, ciudad, codigoPostal)
     * 
     * @return Cadena en formato PostgreSQL
     */
    public String toPostgresString() {
        return "(" + 
               "\"" + calle + "\"" + ", " + 
               numero + ", " + 
               "\"" + piso + "\"" + ", " + 
               "\"" + ciudad + "\"" + ", " + 
               "\"" + codigoPostal + "\"" + 
               ")";
    }
    
    /**
     * Devuelve una representación en texto de la dirección.
     * Útil para depuración y visualización.
     * 
     * @return Representación en texto de la dirección
     */
    @Override
    public String toString() {
        return "Direccion{" +
                "calle='" + calle + '\'' +
                ", numero=" + numero +
                ", piso='" + piso + '\'' +
                ", ciudad='" + ciudad + '\'' +
                ", codigoPostal='" + codigoPostal + '\'' +
                '}';
    }
}
```

### Ejercicio 3: Clase Persona

**Descripción**: Esta clase representa una persona con atributos básicos y una dirección (tipo compuesto). Se utilizará para demostrar cómo trabajar con tipos compuestos en PostgreSQL, donde un atributo de una tabla puede ser un objeto complejo con su propia estructura.

```java
package com.example.ordb; // Define el paquete donde se encuentra la clase

/**
 * Clase que representa una persona con atributos básicos y una dirección.
 * Demuestra el uso de tipos compuestos en PostgreSQL.
 */
public class Persona {
    
    // Atributos de la clase
    private int id; // Identificador único
    private String nombre; // Nombre de la persona
    private String apellidos; // Apellidos de la persona
    private int edad; // Edad de la persona
    private Direccion direccion; // Dirección (tipo compuesto)
    
    /**
     * Constructor por defecto.
     * Inicializa una persona con valores vacíos.
     */
    public Persona() {
        this.id = 0;
        this.nombre = "";
        this.apellidos = "";
        this.edad = 0;
        this.direccion = new Direccion();
    }
    
    /**
     * Constructor con parámetros básicos.
     * 
     * @param id Identificador único
     * @param nombre Nombre de la persona
     * @param apellidos Apellidos de la persona
     * @param edad Edad de la persona
     */
    public Persona(int id, String nombre, String apellidos, int edad) {
        this.id = id;
        this.nombre = nombre;
        this.apellidos = apellidos;
        this.edad = edad;
        this.direccion = new Direccion();
    }
    
    /**
     * Constructor con todos los parámetros.
     * 
     * @param id Identificador único
     * @param nombre Nombre de la persona
     * @param apellidos Apellidos de la persona
     * @param edad Edad de la persona
     * @param direccion Dirección de la persona
     */
    public Persona(int id, String nombre, String apellidos, int edad, Direccion direccion) {
        this.id = id;
        this.nombre = nombre;
        this.apellidos = apellidos;
        this.edad = edad;
        this.direccion = direccion;
    }
    
    /**
     * Obtiene el identificador único.
     * 
     * @return Identificador único
     */
    public int getId() {
        return id;
    }
    
    /**
     * Establece el identificador único.
     * 
     * @param id Nuevo identificador único
     */
    public void setId(int id) {
        this.id = id;
    }
    
    /**
     * Obtiene el nombre de la persona.
     * 
     * @return Nombre de la persona
     */
    public String getNombre() {
        return nombre;
    }
    
    /**
     * Establece el nombre de la persona.
     * 
     * @param nombre Nuevo nombre de la persona
     */
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    /**
     * Obtiene los apellidos de la persona.
     * 
     * @return Apellidos de la persona
     */
    public String getApellidos() {
        return apellidos;
    }
    
    /**
     * Establece los apellidos de la persona.
     * 
     * @param apellidos Nuevos apellidos de la persona
     */
    public void setApellidos(String apellidos) {
        this.apellidos = apellidos;
    }
    
    /**
     * Obtiene la edad de la persona.
     * 
     * @return Edad de la persona
     */
    public int getEdad() {
        return edad;
    }
    
    /**
     * Establece la edad de la persona.
     * 
     * @param edad Nueva edad de la persona
     */
    public void setEdad(int edad) {
        this.edad = edad;
    }
    
    /**
     * Obtiene la dirección de la persona.
     * 
     * @return Dirección de la persona
     */
    public Direccion getDireccion() {
        return direccion;
    }
    
    /**
     * Establece la dirección de la persona.
     * 
     * @param direccion Nueva dirección de la persona
     */
    public void setDireccion(Direccion direccion) {
        this.direccion = direccion;
    }
    
    /**
     * Devuelve una representación en texto de la persona.
     * Útil para depuración y visualización.
     * 
     * @return Representación en texto de la persona
     */
    @Override
    public String toString() {
        return "Persona{" +
                "id=" + id +
                ", nombre='" + nombre + '\'' +
                ", apellidos='" + apellidos + '\'' +
                ", edad=" + edad +
                ", direccion=" + direccion +
                '}';
    }
}
```

### Ejercicio 4: Clase PersonaDAO

**Descripción**: Esta clase implementa el patrón DAO (Data Access Object) para la entidad Persona, proporcionando métodos para realizar operaciones CRUD en la base de datos PostgreSQL. Demuestra cómo trabajar con tipos compuestos en consultas SQL, utilizando la sintaxis específica de PostgreSQL para manipular estos tipos.

```java
package com.example.ordb; // Define el paquete donde se encuentra la clase

import java.sql.Connection; // Para manejar conexiones a la base de datos
import java.sql.PreparedStatement; // Para ejecutar consultas SQL parametrizadas
import java.sql.ResultSet; // Para almacenar los resultados de las consultas
import java.sql.SQLException; // Para manejar excepciones de SQL
import java.sql.Statement; // Para ejecutar consultas SQL simples
import java.util.ArrayList; // Para almacenar listas de personas
import java.util.List; // Interfaz para listas

/**
 * Clase que implementa el patrón DAO (Data Access Object) para la entidad Persona.
 * Proporciona métodos para realizar operaciones CRUD en la tabla de personas.
 * Demuestra cómo trabajar con tipos compuestos en PostgreSQL.
 */
public class PersonaDAO {
    
    // Consultas SQL
    private static final String SQL_INSERT = 
            "INSERT INTO personas (id, nombre, apellidos, edad, direccion) " +
            "VALUES (?, ?, ?, ?, ?::direccion_t)";
    
    private static final String SQL_UPDATE = 
            "UPDATE personas SET nombre = ?, apellidos = ?, edad = ?, " +
            "direccion = ?::direccion_t WHERE id = ?";
    
    private static final String SQL_DELETE = 
            "DELETE FROM personas WHERE id = ?";
    
    private static final String SQL_SELECT_ALL = 
            "SELECT id, nombre, apellidos, edad, " +
            "(direccion).calle, (direccion).numero, (direccion).piso, " +
            "(direccion).ciudad, (direccion).codigo_postal " +
            "FROM personas";
    
    private static final String SQL_SELECT_BY_ID = 
            "SELECT id, nombre, apellidos, edad, " +
            "(direccion).calle, (direccion).numero, (direccion).piso, " +
            "(direccion).ciudad, (direccion).codigo_postal " +
            "FROM personas WHERE id = ?";
    
    // Conexión a la base de datos
    private Connection conexion;
    
    /**
     * Constructor que recibe una conexión a la base de datos.
     * 
     * @param conexion Conexión a la base de datos
     */
    public PersonaDAO(Connection conexion) {
        this.conexion = conexion;
    }
    
    /**
     * Inserta una nueva persona en la base de datos.
     * 
     * @param persona Persona a insertar
     * @return true si la inserción fue exitosa, false en caso contrario
     * @throws MiExcepcion Si hay algún error durante la inserción
     */
    public boolean insertar(Persona persona) throws MiExcepcion {
        PreparedStatement ps = null;
        
        try {
            // Preparamos la consulta SQL con parámetros
            ps = conexion.prepareStatement(SQL_INSERT);
            
            // Establecemos los valores de los parámetros básicos
            ps.setInt(1, persona.getId());
            ps.setString(2, persona.getNombre());
            ps.setString(3, persona.getApellidos());
            ps.setInt(4, persona.getEdad());
            
            // Establecemos el valor del tipo compuesto (dirección)
            // Convertimos la dirección a una cadena en formato PostgreSQL
            ps.setString(5, persona.getDireccion().toPostgresString());
            
            // Ejecutamos la consulta y obtenemos el número de filas afectadas
            int filasAfectadas = ps.executeUpdate();
            
            // Si se afectó al menos una fila, la inserción fue exitosa
            return filasAfectadas > 0;
        } catch (SQLException e) {
            // Error al ejecutar la consulta
            throw new MiExcepcion("Error al insertar persona: " + e.getMessage(), e);
        } finally {
            // Cerramos el PreparedStatement
            cerrarStatement(ps);
        }
    }
    
    /**
     * Actualiza una persona existente en la base de datos.
     * 
     * @param persona Persona con los nuevos datos
     * @return true si la actualización fue exitosa, false en caso contrario
     * @throws MiExcepcion Si hay algún error durante la actualización
     */
    public boolean actualizar(Persona persona) throws MiExcepcion {
        PreparedStatement ps = null;
        
        try {
            // Preparamos la consulta SQL con parámetros
            ps = conexion.prepareStatement(SQL_UPDATE);
            
            // Establecemos los valores de los parámetros básicos
            ps.setString(1, persona.getNombre());
            ps.setString(2, persona.getApellidos());
            ps.setInt(3, persona.getEdad());
            
            // Establecemos el valor del tipo compuesto (dirección)
            ps.setString(4, persona.getDireccion().toPostgresString());
            
            // Establecemos el ID (clave primaria)
            ps.setInt(5, persona.getId());
            
            // Ejecutamos la consulta y obtenemos el número de filas afectadas
            int filasAfectadas = ps.executeUpdate();
            
            // Si se afectó al menos una fila, la actualización fue exitosa
            return filasAfectadas > 0;
        } catch (SQLException e) {
            // Error al ejecutar la consulta
            throw new MiExcepcion("Error al actualizar persona: " + e.getMessage(), e);
        } finally {
            // Cerramos el PreparedStatement
            cerrarStatement(ps);
        }
    }
    
    /**
     * Elimina una persona de la base de datos por su ID.
     * 
     * @param id ID de la persona a eliminar
     * @return true si la eliminación fue exitosa, false en caso contrario
     * @throws MiExcepcion Si hay algún error durante la eliminación
     */
    public boolean eliminar(int id) throws MiExcepcion {
        PreparedStatement ps = null;
        
        try {
            // Preparamos la consulta SQL con parámetros
            ps = conexion.prepareStatement(SQL_DELETE);
            
            // Establecemos el valor del parámetro
            ps.setInt(1, id);
            
            // Ejecutamos la consulta y obtenemos el número de filas afectadas
            int filasAfectadas = ps.executeUpdate();
            
            // Si se afectó al menos una fila, la eliminación fue exitosa
            return filasAfectadas > 0;
        } catch (SQLException e) {
            // Error al ejecutar la consulta
            throw new MiExcepcion("Error al eliminar persona: " + e.getMessage(), e);
        } finally {
            // Cerramos el PreparedStatement
            cerrarStatement(ps);
        }
    }
    
    /**
     * Obtiene todas las personas de la base de datos.
     * 
     * @return Lista de todas las personas
     * @throws MiExcepcion Si hay algún error durante la consulta
     */
    public List<Persona> obtenerTodos() throws MiExcepcion {
        PreparedStatement ps = null;
        ResultSet rs = null;
        List<Persona> personas = new ArrayList<>();
        
        try {
            // Preparamos la consulta SQL
            ps = conexion.prepareStatement(SQL_SELECT_ALL);
            
            // Ejecutamos la consulta y obtenemos los resultados
            rs = ps.executeQuery();
            
            // Recorremos los resultados y creamos objetos Persona
            while (rs.next()) {
                // Creamos un objeto Persona con los datos básicos
                Persona persona = new Persona();
                persona.setId(rs.getInt("id"));
                persona.setNombre(rs.getString("nombre"));
                persona.setApellidos(rs.getString("apellidos"));
                persona.setEdad(rs.getInt("edad"));
                
                // Creamos un objeto Direccion con los datos del tipo compuesto
                Direccion direccion = new Direccion();
                direccion.setCalle(rs.getString("calle"));
                direccion.setNumero(rs.getInt("numero"));
                direccion.setPiso(rs.getString("piso"));
                direccion.setCiudad(rs.getString("ciudad"));
                direccion.setCodigoPostal(rs.getString("codigo_postal"));
                
                // Establecemos la dirección en la persona
                persona.setDireccion(direccion);
                
                // Añadimos la persona a la lista
                personas.add(persona);
            }
            
            return personas;
        } catch (SQLException e) {
            // Error al ejecutar la consulta
            throw new MiExcepcion("Error al obtener todas las personas: " + e.getMessage(), e);
        } finally {
            // Cerramos el ResultSet y el PreparedStatement
            cerrarResultSet(rs);
            cerrarStatement(ps);
        }
    }
    
    /**
     * Obtiene una persona de la base de datos por su ID.
     * 
     * @param id ID de la persona a buscar
     * @return Persona encontrada o null si no existe
     * @throws MiExcepcion Si hay algún error durante la consulta
     */
    public Persona obtenerPorId(int id) throws MiExcepcion {
        PreparedStatement ps = null;
        ResultSet rs = null;
        Persona persona = null;
        
        try {
            // Preparamos la consulta SQL con parámetros
            ps = conexion.prepareStatement(SQL_SELECT_BY_ID);
            
            // Establecemos el valor del parámetro
            ps.setInt(1, id);
            
            // Ejecutamos la consulta y obtenemos los resultados
            rs = ps.executeQuery();
            
            // Si hay un resultado, creamos un objeto Persona
            if (rs.next()) {
                // Creamos un objeto Persona con los datos básicos
                persona = new Persona();
                persona.setId(rs.getInt("id"));
                persona.setNombre(rs.getString("nombre"));
                persona.setApellidos(rs.getString("apellidos"));
                persona.setEdad(rs.getInt("edad"));
                
                // Creamos un objeto Direccion con los datos del tipo compuesto
                Direccion direccion = new Direccion();
                direccion.setCalle(rs.getString("calle"));
                direccion.setNumero(rs.getInt("numero"));
                direccion.setPiso(rs.getString("piso"));
                direccion.setCiudad(rs.getString("ciudad"));
                direccion.setCodigoPostal(rs.getString("codigo_postal"));
                
                // Establecemos la dirección en la persona
                persona.setDireccion(direccion);
            }
            
            return persona;
        } catch (SQLException e) {
            // Error al ejecutar la consulta
            throw new MiExcepcion("Error al obtener persona por ID: " + e.getMessage(), e);
        } finally {
            // Cerramos el ResultSet y el PreparedStatement
            cerrarResultSet(rs);
            cerrarStatement(ps);
        }
    }
    
    /**
     * Cierra un objeto Statement o PreparedStatement.
     * 
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
     * 
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

### Ejercicio 5: Clase MiExcepcion

**Descripción**: Esta clase representa una excepción personalizada para la aplicación, que permite encapsular y propagar errores específicos de manera controlada. Es especialmente útil para manejar errores relacionados con la base de datos y convertir excepciones técnicas en mensajes más comprensibles para el usuario.

```java
package com.example.ordb; // Define el paquete donde se encuentra la clase

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

### Ejercicio 6: Clase PruebasORDB (con main)

**Descripción**: Esta clase contiene el método main y métodos para probar todas las funcionalidades implementadas en las clases anteriores. Aquí se realizan pruebas de conexión a la base de datos PostgreSQL y operaciones CRUD sobre la tabla de personas, demostrando el uso de tipos compuestos en una base de datos objeto-relacional.

```java
package com.example.main; // Define el paquete donde se encuentra la clase principal

import java.sql.Connection; // Para manejar conexiones a la base de datos
import java.util.List; // Para trabajar con listas

import com.example.ordb.ConexionPostgreSQL; // Importamos la clase de conexión
import com.example.ordb.Direccion; // Importamos la clase Direccion
import com.example.ordb.MiExcepcion; // Importamos nuestra excepción personalizada
import com.example.ordb.Persona; // Importamos la clase Persona
import com.example.ordb.PersonaDAO; // Importamos la clase DAO

/**
 * Clase principal para probar las funcionalidades de ORDB con PostgreSQL.
 * Contiene el método main y métodos para probar cada aspecto de la conexión y operaciones CRUD.
 */
public class PruebasORDB {
    
    /**
     * Método principal que ejecuta las pruebas.
     * 
     * @param args Argumentos de línea de comandos (no utilizados)
     */
    public static void main(String[] args) {
        try {
            // Obtenemos la instancia de conexión a la BD
            ConexionPostgreSQL conexionBD = ConexionPostgreSQL.getInstancia();
            Connection conexion = conexionBD.getConexion();
            
            // Creamos un objeto PersonaDAO con la conexión
            PersonaDAO personaDAO = new PersonaDAO(conexion);
            
            // Probamos las diferentes operaciones CRUD
            probarInsercion(personaDAO);
            probarConsulta(personaDAO);
            probarActualizacion(personaDAO);
            probarEliminacion(personaDAO);
            
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
     * Prueba la inserción de personas en la base de datos.
     * 
     * @param personaDAO Objeto DAO para realizar operaciones con personas
     * @throws MiExcepcion Si hay algún error durante la inserción
     */
    private static void probarInsercion(PersonaDAO personaDAO) throws MiExcepcion {
        System.out.println("\n=== Prueba de Inserción ===");
        
        // Creamos algunas direcciones de ejemplo
        Direccion direccion1 = new Direccion("Calle Mayor", 10, "2A", "Madrid", "28001");
        Direccion direccion2 = new Direccion("Avenida Diagonal", 250, "5B", "Barcelona", "08013");
        
        // Creamos algunas personas de ejemplo
        Persona persona1 = new Persona(1, "Juan", "Pérez", 30, direccion1);
        Persona persona2 = new Persona(2, "María", "García", 25, direccion2);
        
        // Insertamos las personas en la base de datos
        boolean resultado1 = personaDAO.insertar(persona1);
        boolean resultado2 = personaDAO.insertar(persona2);
        
        // Mostramos los resultados
        System.out.println("Inserción de persona 1: " + (resultado1 ? "Exitosa" : "Fallida"));
        System.out.println("Inserción de persona 2: " + (resultado2 ? "Exitosa" : "Fallida"));
    }
    
    /**
     * Prueba la consulta de personas en la base de datos.
     * 
     * @param personaDAO Objeto DAO para realizar operaciones con personas
     * @throws MiExcepcion Si hay algún error durante la consulta
     */
    private static void probarConsulta(PersonaDAO personaDAO) throws MiExcepcion {
        System.out.println("\n=== Prueba de Consulta ===");
        
        // Consultamos todas las personas
        List<Persona> personas = personaDAO.obtenerTodos();
        
        // Mostramos las personas obtenidas
        System.out.println("Personas en la base de datos:");
        for (Persona persona : personas) {
            System.out.println("  " + persona);
        }
        
        // Consultamos una persona por su ID
        int id = 1; // ID de Juan Pérez
        Persona persona = personaDAO.obtenerPorId(id);
        
        // Mostramos la persona obtenida
        if (persona != null) {
            System.out.println("\nPersona con ID " + id + ":");
            System.out.println("  " + persona);
        } else {
            System.out.println("\nNo se encontró una persona con ID " + id);
        }
    }
    
    /**
     * Prueba la actualización de personas en la base de datos.
     * 
     * @param personaDAO Objeto DAO para realizar operaciones con personas
     * @throws MiExcepcion Si hay algún error durante la actualización
     */
    private static void probarActualizacion(PersonaDAO personaDAO) throws MiExcepcion {
        System.out.println("\n=== Prueba de Actualización ===");
        
        // Obtenemos una persona existente
        int id = 1; // ID de Juan Pérez
        Persona persona = personaDAO.obtenerPorId(id);
        
        if (persona != null) {
            // Mostramos la persona antes de la actualización
            System.out.println("Persona antes de actualizar:");
            System.out.println("  " + persona);
            
            // Modificamos algunos datos de la persona
            persona.setEdad(31);
            persona.getDireccion().setCalle("Calle Nueva");
            persona.getDireccion().setNumero(20);
            
            // Actualizamos la persona en la base de datos
            boolean resultado = personaDAO.actualizar(persona);
            
            // Mostramos el resultado
            System.out.println("Actualización: " + (resultado ? "Exitosa" : "Fallida"));
            
            // Consultamos la persona actualizada
            Persona personaActualizada = personaDAO.obtenerPorId(id);
            
            // Mostramos la persona después de la actualización
            System.out.println("Persona después de actualizar:");
            System.out.println("  " + personaActualizada);
        } else {
            System.out.println("No se encontró una persona con ID " + id + " para actualizar");
        }
    }
    
    /**
     * Prueba la eliminación de personas en la base de datos.
     * 
     * @param personaDAO Objeto DAO para realizar operaciones con personas
     * @throws MiExcepcion Si hay algún error durante la eliminación
     */
    private static void probarEliminacion(PersonaDAO personaDAO) throws MiExcepcion {
        System.out.println("\n=== Prueba de Eliminación ===");
        
        // ID de la persona a eliminar
        int id = 2; // ID de María García
        
        // Verificamos que la persona existe antes de eliminarla
        Persona persona = personaDAO.obtenerPorId(id);
        
        if (persona != null) {
            // Mostramos la persona a eliminar
            System.out.println("Persona a eliminar:");
            System.out.println("  " + persona);
            
            // Eliminamos la persona de la base de datos
            boolean resultado = personaDAO.eliminar(id);
            
            // Mostramos el resultado
            System.out.println("Eliminación: " + (resultado ? "Exitosa" : "Fallida"));
            
            // Verificamos que la persona ya no existe
            Persona personaEliminada = personaDAO.obtenerPorId(id);
            
            if (personaEliminada == null) {
                System.out.println("La persona con ID " + id + " ya no existe en la base de datos");
            } else {
                System.out.println("¡Error! La persona con ID " + id + " todavía existe en la base de datos");
            }
        } else {
            System.out.println("No se encontró una persona con ID " + id + " para eliminar");
        }
    }
}
```

### Script SQL para crear la base de datos

**Descripción**: Este script SQL crea la base de datos, el tipo compuesto y la tabla necesaria para los ejercicios. Debe ejecutarse en el servidor PostgreSQL antes de ejecutar las pruebas de ORDB.

```sql
-- Crear la base de datos
CREATE DATABASE biblioteca;

-- Conectarse a la base de datos
\c biblioteca;

-- Crear el tipo compuesto para direcciones
CREATE TYPE direccion_t AS (
    calle VARCHAR(100),
    numero INTEGER,
    piso VARCHAR(10),
    ciudad VARCHAR(50),
    codigo_postal VARCHAR(10)
);

-- Crear la tabla de personas con un atributo de tipo compuesto
CREATE TABLE personas (
    id INTEGER PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(50) NOT NULL,
    edad INTEGER,
    direccion direccion_t
);

-- Eliminar datos existentes (opcional)
-- TRUNCATE TABLE personas;
```
