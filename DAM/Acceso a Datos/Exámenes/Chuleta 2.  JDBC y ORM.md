# **Chuleta 2.** <br>JDBC y ORM

## JDBC - Conexión y Consultas Básicas

```java
// Cargar driver (opcional desde Java 6)
Class.forName("org.postgresql.Driver");

// Establecer conexión
String url = "jdbc:postgresql://localhost:5432/basedatos";
String usuario = "usuario";
String password = "contraseña";
Connection conn = DriverManager.getConnection(url, usuario, password);

// Try-with-resources para gestión de recursos
try (Connection conn = DriverManager.getConnection(url, usuario, password);
     Statement stmt = conn.createStatement()) {
    
    // Ejecutar consulta SELECT
    ResultSet rs = stmt.executeQuery("SELECT * FROM productos");
    while (rs.next()) {
        int id = rs.getInt("id");
        String nombre = rs.getString("nombre");
        double precio = rs.getDouble("precio");
        // Procesar datos...
    }
    
    // Ejecutar INSERT, UPDATE, DELETE
    int filasAfectadas = stmt.executeUpdate(
        "INSERT INTO productos (nombre, precio) VALUES ('Laptop', 999.99)");
}
```

## JDBC - PreparedStatement

```java
// Consulta parametrizada
String sql = "SELECT * FROM productos WHERE precio > ? AND categoria = ?";
try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
    
    // Establecer parámetros
    pstmt.setDouble(1, 100.0);
    pstmt.setString(2, "Electrónica");
    
    // Ejecutar consulta
    ResultSet rs = pstmt.executeQuery();
    while (rs.next()) {
        // Procesar resultados...
    }
}

// INSERT con PreparedStatement
String insertSql = "INSERT INTO productos (nombre, precio, categoria) VALUES (?, ?, ?)";
try (PreparedStatement pstmt = conn.prepareStatement(insertSql)) {
    
    pstmt.setString(1, "Smartphone");
    pstmt.setDouble(2, 599.99);
    pstmt.setString(3, "Electrónica");
    
    int filasAfectadas = pstmt.executeUpdate();
}
```

## JDBC - Transacciones

```java
// Gestión manual de transacciones
Connection conn = DriverManager.getConnection(url, usuario, password);
try {
    // Desactivar autocommit
    conn.setAutoCommit(false);
    
    // Realizar operaciones
    Statement stmt = conn.createStatement();
    stmt.executeUpdate("UPDATE cuentas SET saldo = saldo - 100 WHERE id = 1");
    stmt.executeUpdate("UPDATE cuentas SET saldo = saldo + 100 WHERE id = 2");
    
    // Confirmar transacción
    conn.commit();
} catch (SQLException e) {
    // Deshacer transacción en caso de error
    conn.rollback();
    throw e;
} finally {
    // Restaurar autocommit y cerrar conexión
    conn.setAutoCommit(true);
    conn.close();
}
```

## JDBC - Batch Updates

```java
// Operaciones en lote
try (Connection conn = DriverManager.getConnection(url, usuario, password);
     PreparedStatement pstmt = conn.prepareStatement(
         "INSERT INTO productos (nombre, precio) VALUES (?, ?)")) {
    
    // Desactivar autocommit
    conn.setAutoCommit(false);
    
    // Añadir operaciones al lote
    for (Producto p : listaProductos) {
        pstmt.setString(1, p.getNombre());
        pstmt.setDouble(2, p.getPrecio());
        pstmt.addBatch();
    }
    
    // Ejecutar lote
    int[] resultados = pstmt.executeBatch();
    
    // Confirmar transacción
    conn.commit();
}
```

## ORM - JPA/Hibernate Entidades

```java
// Definición de entidad
@Entity
@Table(name = "productos")
public class Producto {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(name = "nombre", nullable = false, length = 100)
    private String nombre;
    
    @Column(name = "precio")
    private Double precio;
    
    @ManyToOne
    @JoinColumn(name = "categoria_id")
    private Categoria categoria;
    
    // Constructor, getters, setters...
}

// Relación OneToMany
@Entity
@Table(name = "categorias")
public class Categoria {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    private String nombre;
    
    @OneToMany(mappedBy = "categoria", cascade = CascadeType.ALL)
    private List<Producto> productos = new ArrayList<>();
    
    // Constructor, getters, setters...
}

// Relación ManyToMany
@Entity
public class Estudiante {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    private String nombre;
    
    @ManyToMany
    @JoinTable(
        name = "estudiante_curso",
        joinColumns = @JoinColumn(name = "estudiante_id"),
        inverseJoinColumns = @JoinColumn(name = "curso_id")
    )
    private List<Curso> cursos = new ArrayList<>();
    
    // Constructor, getters, setters...
}
```

## ORM - JPA/Hibernate Operaciones

```java
// Configuración EntityManager
EntityManagerFactory emf = Persistence.createEntityManagerFactory("nombreUnidad");
EntityManager em = emf.createEntityManager();

// Operaciones CRUD
try {
    // Iniciar transacción
    em.getTransaction().begin();
    
    // Crear (persist)
    Producto p = new Producto();
    p.setNombre("Laptop");
    p.setPrecio(999.99);
    em.persist(p);
    
    // Leer (find)
    Producto encontrado = em.find(Producto.class, 1L);
    
    // Actualizar
    encontrado.setPrecio(899.99);
    
    // Eliminar (remove)
    Producto aEliminar = em.find(Producto.class, 2L);
    em.remove(aEliminar);
    
    // Confirmar transacción
    em.getTransaction().commit();
} catch (Exception e) {
    em.getTransaction().rollback();
    throw e;
} finally {
    em.close();
}
```

## ORM - JPQL Consultas

```java
// Consulta simple
TypedQuery<Producto> query = em.createQuery(
    "SELECT p FROM Producto p WHERE p.precio > :precio", Producto.class);
query.setParameter("precio", 100.0);
List<Producto> productos = query.getResultList();

// Consulta con join
TypedQuery<Producto> joinQuery = em.createQuery(
    "SELECT p FROM Producto p JOIN p.categoria c WHERE c.nombre = :categoria", 
    Producto.class);
joinQuery.setParameter("categoria", "Electrónica");
List<Producto> productosElectronicos = joinQuery.getResultList();

// Consulta con agregación
TypedQuery<Double> avgQuery = em.createQuery(
    "SELECT AVG(p.precio) FROM Producto p WHERE p.categoria.id = :catId", 
    Double.class);
avgQuery.setParameter("catId", 1L);
Double precioPromedio = avgQuery.getSingleResult();

// Named Query (definida en la entidad)
@NamedQuery(name = "Producto.porCategoria", 
            query = "SELECT p FROM Producto p WHERE p.categoria.nombre = :categoria")
// Uso:
TypedQuery<Producto> namedQuery = em.createNamedQuery("Producto.porCategoria", Producto.class);
namedQuery.setParameter("categoria", "Electrónica");
List<Producto> resultado = namedQuery.getResultList();
```
