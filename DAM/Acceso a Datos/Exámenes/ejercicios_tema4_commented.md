# Ejercicios TEMA 4: ORM

## Instrucciones

1. Crea un proyecto para hacer los ejercicios o aprovecha el del bloque de ejercicios anterior.
2. Crea un paquete donde guardarás todas las clases creadas en estos ejercicios.
3. Crea otro paquete con una clase con main. Desde esta clase prueba todos los métodos creados en los ejercicios.
4. Crea una excepción para tratar los errores propios de la aplicación (o reaprovecha la del bloque anterior).
5. Propaga las excepciones hasta el main y tratándolas allí.
6. Añade las dependencias necesarias para Hibernate y JPA.

## Ejercicios

### Ejercicio 1: Clase Libro (Entidad JPA)

**Descripción**: Esta clase representa la entidad Libro en la aplicación, ahora anotada con anotaciones JPA para mapear la clase a una tabla en la base de datos. Las anotaciones permiten definir la estructura de la tabla, claves primarias, relaciones y otras propiedades de persistencia sin necesidad de configuración XML.

```java
package com.example.orm; // Define el paquete donde se encuentra la clase

import javax.persistence.Column; // Para definir propiedades de columnas
import javax.persistence.Entity; // Para marcar la clase como entidad JPA
import javax.persistence.Id; // Para marcar el identificador único
import javax.persistence.Table; // Para definir propiedades de la tabla

/**
 * Clase que representa un libro en la biblioteca.
 * Anotada como entidad JPA para mapeo objeto-relacional.
 */
@Entity // Indica que esta clase es una entidad JPA
@Table(name = "libros") // Especifica el nombre de la tabla en la base de datos
public class Libro {
    
    // Atributos de la clase, mapeados a columnas de la tabla
    
    @Id // Indica que este campo es la clave primaria
    @Column(name = "isbn", length = 20) // Especifica propiedades de la columna
    private String isbn; // ISBN del libro (id único)
    
    @Column(name = "titulo", nullable = false, length = 100) // Columna no nula
    private String titulo; // Título del libro
    
    @Column(name = "autor", nullable = false, length = 100)
    private String autor; // Autor del libro
    
    @Column(name = "anio_publicacion") // Nombre de columna diferente al nombre del atributo
    private int anioPublicacion; // Año de publicación
    
    @Column(name = "editorial", length = 50)
    private String editorial; // Editorial del libro
    
    @Column(name = "num_paginas")
    private int numPaginas; // Número de páginas
    
    /**
     * Constructor por defecto.
     * Requerido por JPA para crear instancias al cargar desde la base de datos.
     */
    public Libro() {
        // Constructor vacío requerido por JPA
    }
    
    /**
     * Constructor con parámetros.
     * Inicializa un libro con los valores proporcionados.
     * 
     * @param isbn ISBN del libro
     * @param titulo Título del libro
     * @param autor Autor del libro
     * @param anioPublicacion Año de publicación
     * @param editorial Editorial del libro
     * @param numPaginas Número de páginas
     */
    public Libro(
	    String isbn,
	    String titulo,
	    String autor,
	    int anioPublicacion, 
        String editorial,
        int numPaginas
    ) {
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
     * 
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
    
    /**
     * Compara este libro con otro objeto para determinar si son iguales.
     * Dos libros son iguales si tienen el mismo ISBN.
     * 
     * @param obj Objeto a comparar
     * @return true si son iguales, false en caso contrario
     */
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        
        Libro libro = (Libro) obj;
        
        return isbn != null ? isbn.equals(libro.isbn) : libro.isbn == null;
    }
    
    /**
     * Calcula el código hash del libro.
     * Basado en el ISBN, que es el identificador único.
     * 
     * @return Código hash
     */
    @Override
    public int hashCode() {
        return isbn != null ? isbn.hashCode() : 0;
    }
}
```

### Ejercicio 2: Clase Autor (Entidad JPA)

**Descripción**: Esta clase representa la entidad Autor en la aplicación, anotada con anotaciones JPA. Incluye una relación uno-a-muchos con la entidad Libro, demostrando cómo se pueden modelar relaciones entre entidades en JPA.

```java
package com.example.orm; // Define el paquete donde se encuentra la clase

import java.util.ArrayList; // Para la colección de libros
import java.util.List; // Interfaz para listas

import javax.persistence.CascadeType; // Para definir operaciones en cascada
import javax.persistence.Column; // Para definir propiedades de columnas
import javax.persistence.Entity; // Para marcar la clase como entidad JPA
import javax.persistence.FetchType; // Para definir estrategia de carga
import javax.persistence.GeneratedValue; // Para generar valores automáticamente
import javax.persistence.GenerationType; // Estrategias de generación de valores
import javax.persistence.Id; // Para marcar el identificador único
import javax.persistence.OneToMany; // Para definir relación uno-a-muchos
import javax.persistence.Table; // Para definir propiedades de la tabla

/**
 * Clase que representa un autor en la biblioteca.
 * Anotada como entidad JPA para mapeo objeto-relacional.
 * Demuestra relaciones uno-a-muchos con la entidad Libro.
 */
@Entity // Indica que esta clase es una entidad JPA
@Table(name = "autores") // Especifica el nombre de la tabla en la base de datos
public class Autor {
    
    // Atributos de la clase, mapeados a columnas de la tabla
    
    @Id // Indica que este campo es la clave primaria
    @GeneratedValue(strategy = GenerationType.IDENTITY) // Genera valores automáticamente (autoincremento)
    @Column(name = "id") // Especifica propiedades de la columna
    private Long id; // Identificador único del autor
    
    @Column(name = "nombre", nullable = false, length = 50) // Columna no nula
    private String nombre; // Nombre del autor
    
    @Column(name = "apellidos", nullable = false, length = 50)
    private String apellidos; // Apellidos del autor
    
    @Column(name = "nacionalidad", length = 50)
    private String nacionalidad; // Nacionalidad del autor
    
    @Column(name = "anio_nacimiento")
    private Integer anioNacimiento; // Año de nacimiento (puede ser null)
    
    // Relación uno-a-muchos con la entidad Libro
    // Un autor puede tener muchos libros
    @OneToMany(mappedBy = "autor", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    private List<LibroConAutor> libros; // Lista de libros del autor
    
    /**
     * Constructor por defecto.
     * Requerido por JPA para crear instancias al cargar desde la base de datos.
     * Inicializa la lista de libros.
     */
    public Autor() {
        // Inicializamos la lista de libros vacía
        this.libros = new ArrayList<>();
    }
    
    /**
     * Constructor con parámetros básicos.
     * 
     * @param nombre Nombre del autor
     * @param apellidos Apellidos del autor
     */
    public Autor(String nombre, String apellidos) {
        this.nombre = nombre;
        this.apellidos = apellidos;
        this.libros = new ArrayList<>();
    }
    
    /**
     * Constructor con todos los parámetros.
     * 
     * @param nombre Nombre del autor
     * @param apellidos Apellidos del autor
     * @param nacionalidad Nacionalidad del autor
     * @param anioNacimiento Año de nacimiento
     */
    public Autor(
	    String nombre,
	    String apellidos,
	    String nacionalidad,
	    Integer anioNacimiento
	) {
        this.nombre = nombre;
        this.apellidos = apellidos;
        this.nacionalidad = nacionalidad;
        this.anioNacimiento = anioNacimiento;
        this.libros = new ArrayList<>();
    }
    
    // Métodos getter y setter para cada atributo
    
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }
    public String getApellidos() { return apellidos; }
    public void setApellidos(String apellidos) { this.apellidos = apellidos; }
    public String getNacionalidad() { return nacionalidad; }
    public void setNacionalidad(String nacionalidad) { this.nacionalidad = nacionalidad; }
    public Integer getAnioNacimiento() { return anioNacimiento; }
    public void setAnioNacimiento(Integer anioNacimiento) { this.anioNacimiento = anioNacimiento; }
    public List<LibroConAutor> getLibros() { return libros; }
    public void setLibros(List<LibroConAutor> libros) { this.libros = libros; }
    
    /**
     * Añade un libro a la lista de libros del autor.
     * También establece este autor como el autor del libro.
     * 
     * @param libro Libro a añadir
     */
    public void addLibro(LibroConAutor libro) {
        // Añadimos el libro a la lista de libros del autor
        this.libros.add(libro);
        // Establecemos este autor como el autor del libro
        libro.setAutor(this);
    }
    
    /**
     * Elimina un libro de la lista de libros del autor.
     * También elimina la referencia al autor en el libro.
     * 
     * @param libro Libro a eliminar
     */
    public void removeLibro(LibroConAutor libro) {
        // Eliminamos el libro de la lista de libros del autor
        this.libros.remove(libro);
        // Eliminamos la referencia al autor en el libro
        libro.setAutor(null);
    }
    
    /**
     * Devuelve una representación en texto del autor.
     * Útil para depuración y visualización.
     * No incluye la lista de libros para evitar recursión infinita.
     * 
     * @return Representación en texto del autor
     */
    @Override
    public String toString() {
        return "Autor{" +
                "id=" + id +
                ", nombre='" + nombre + '\'' +
                ", apellidos='" + apellidos + '\'' +
                ", nacionalidad='" + nacionalidad + '\'' +
                ", anioNacimiento=" + anioNacimiento +
                ", numLibros=" + (libros != null ? libros.size() : 0) +
                '}';
    }
    
    /**
     * Compara este autor con otro objeto para determinar si son iguales.
     * Dos autores son iguales si tienen el mismo ID.
     * 
     * @param obj Objeto a comparar
     * @return true si son iguales, false en caso contrario
     */
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        
        Autor autor = (Autor) obj;
        
        return id != null ? id.equals(autor.id) : autor.id == null;
    }
    
    /**
     * Calcula el código hash del autor.
     * Basado en el ID, que es el identificador único.
     * 
     * @return Código hash
     */
    @Override
    public int hashCode() {
        return id != null ? id.hashCode() : 0;
    }
}
```

### Ejercicio 3: Clase LibroConAutor (Entidad JPA con relación)

**Descripción**: Esta clase representa la entidad Libro con una relación muchos-a-uno con la entidad Autor. Demuestra cómo se pueden modelar relaciones bidireccionales entre entidades en JPA, donde un libro pertenece a un autor y un autor tiene muchos libros.

```java
package com.example.orm; // Define el paquete donde se encuentra la clase

import javax.persistence.Column; // Para definir propiedades de columnas
import javax.persistence.Entity; // Para marcar la clase como entidad JPA
import javax.persistence.FetchType; // Para definir estrategia de carga
import javax.persistence.Id; // Para marcar el identificador único
import javax.persistence.JoinColumn; // Para definir columna de unión en relaciones
import javax.persistence.ManyToOne; // Para definir relación muchos-a-uno
import javax.persistence.Table; // Para definir propiedades de la tabla

/**
 * Clase que representa un libro en la biblioteca con relación a su autor.
 * Anotada como entidad JPA para mapeo objeto-relacional.
 * Demuestra relaciones muchos-a-uno con la entidad Autor.
 */
@Entity // Indica que esta clase es una entidad JPA
@Table(name = "libros_con_autor") // Especifica el nombre de la tabla en la base de datos
public class LibroConAutor {
    
    // Atributos de la clase, mapeados a columnas de la tabla
    
    @Id // Indica que este campo es la clave primaria
    @Column(name = "isbn", length = 20) // Especifica propiedades de la columna
    private String isbn; // ISBN del libro (id único)
    
    @Column(name = "titulo", nullable = false, length = 100) // Columna no nula
    private String titulo; // Título del libro
    
    @Column(name = "anio_publicacion") // Nombre de columna diferente al nombre del atributo
    private int anioPublicacion; // Año de publicación
    
    @Column(name = "editorial", length = 50)
    private String editorial; // Editorial del libro
    
    @Column(name = "num_paginas")
    private int numPaginas; // Número de páginas
    
    // Relación muchos-a-uno con la entidad Autor
    // Muchos libros pueden pertenecer a un autor
    @ManyToOne(fetch = FetchType.LAZY) // Carga perezosa para mejorar rendimiento
    @JoinColumn(name = "autor_id") // Columna que almacena la clave foránea
    private Autor autor; // Autor del libro
    
    /**
     * Constructor por defecto.
     * Requerido por JPA para crear instancias al cargar desde la base de datos.
     */
    public LibroConAutor() {
        // Constructor vacío requerido por JPA
    }
    
    /**
     * Constructor con parámetros básicos.
     * 
     * @param isbn ISBN del libro
     * @param titulo Título del libro
     * @param anioPublicacion Año de publicación
     */
    public LibroConAutor(String isbn, String titulo, int anioPublicacion) {
        this.isbn = isbn;
        this.titulo = titulo;
        this.anioPublicacion = anioPublicacion;
    }
    
    /**
     * Constructor con todos los parámetros excepto autor.
     * 
     * @param isbn ISBN del libro
     * @param titulo Título del libro
     * @param anioPublicacion Año de publicación
     * @param editorial Editorial del libro
     * @param numPaginas Número de páginas
     */
    public LibroConAutor(String isbn, String titulo, int anioPublicacion, 
                        String editorial, int numPaginas) {
        this.isbn = isbn;
        this.titulo = titulo;
        this.anioPublicacion = anioPublicacion;
        this.editorial = editorial;
        this.numPaginas = numPaginas;
    }
    
    /**
     * Constructor con todos los parámetros incluyendo autor.
     * 
     * @param isbn ISBN del libro
     * @param titulo Título del libro
     * @param anioPublicacion Año de publicación
     * @param editorial Editorial del libro
     * @param numPaginas Número de páginas
     * @param autor Autor del libro
     */
    public LibroConAutor(String isbn, String titulo, int anioPublicacion, 
                        String editorial, int numPaginas, Autor autor) {
        this.isbn = isbn;
        this.titulo = titulo;
        this.anioPublicacion = anioPublicacion;
        this.editorial = editorial;
        this.numPaginas = numPaginas;
        this.autor = autor;
    }
    
    // Métodos getter y setter para cada atributo

    public String getIsbn() { return isbn; }
    public void setIsbn(String isbn) { this.isbn = isbn; }
    public String getTitulo() { return titulo; }
    public void setTitulo(String titulo) { this.titulo = titulo; }
    public int getAnioPublicacion() { return anioPublicacion; }
    public void setAnioPublicacion(int anioPublicacion) { this.anioPublicacion = anioPublicacion; }
    public String getEditorial() { return editorial; }
    public void setEditorial(String editorial) { this.editorial = editorial; }
    public int getNumPaginas() { return numPaginas; }
    public void setNumPaginas(int numPaginas) { this.numPaginas = numPaginas; }
    public Autor getAutor() { return autor; }
    public void setAutor(Autor autor) { this.autor = autor; }
    
    /**
     * Devuelve una representación en texto del libro.
     * Útil para depuración y visualización.
     * No incluye el autor completo para evitar recursión infinita.
     * 
     * @return Representación en texto del libro
     */
    @Override
    public String toString() {
        return "LibroConAutor{" +
                "isbn='" + isbn + '\'' +
                ", titulo='" + titulo + '\'' +
                ", anioPublicacion=" + anioPublicacion +
                ", editorial='" + editorial + '\'' +
                ", numPaginas=" + numPaginas +
                ", autor=" + (autor != null ? autor.getNombre() + " " + autor.getApellidos() : "null") +
                '}';
    }
    
    /**
     * Compara este libro con otro objeto para determinar si son iguales.
     * Dos libros son iguales si tienen el mismo ISBN.
     * 
     * @param obj Objeto a comparar
     * @return true si son iguales, false en caso contrario
     */
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        
        LibroConAutor libro = (LibroConAutor) obj;
        
        return isbn != null ? isbn.equals(libro.isbn) : libro.isbn == null;
    }
    
    /**
     * Calcula el código hash del libro.
     * Basado en el ISBN, que es el identificador único.
     * 
     * @return Código hash
     */
    @Override
    public int hashCode() {
        return isbn != null ? isbn.hashCode() : 0;
    }
}
```

### Ejercicio 4: Clase HibernateUtil

**Descripción**: Esta clase proporciona métodos para gestionar la sesión de Hibernate y el EntityManager de JPA. Implementa el patrón Singleton para asegurar que solo exista una instancia de SessionFactory/EntityManagerFactory en toda la aplicación, lo que optimiza el uso de recursos.

```java
package com.example.orm; // Define el paquete donde se encuentra la clase

import javax.persistence.EntityManager; // Para gestionar entidades JPA
import javax.persistence.EntityManagerFactory; // Para crear EntityManager
import javax.persistence.Persistence; // Para crear EntityManagerFactory

import org.hibernate.SessionFactory; // Para gestionar sesiones Hibernate
import org.hibernate.cfg.Configuration; // Para configurar Hibernate

/**
 * Clase de utilidad para gestionar la sesión de Hibernate y el EntityManager de JPA.
 * Implementa el patrón Singleton para asegurar una única instancia de SessionFactory/EntityManagerFactory.
 */
public class HibernateUtil {
    
    // Constantes
    private static final String PERSISTENCE_UNIT_NAME = "bibliotecaPU"; // Nombre de la unidad de persistencia
    
    // Instancias únicas (patrón Singleton)
    private static SessionFactory sessionFactory; // Para Hibernate nativo
    private static EntityManagerFactory entityManagerFactory; // Para JPA
    
    /**
     * Constructor privado para evitar instanciación directa (patrón Singleton).
     */
    private HibernateUtil() {
        // Constructor privado para evitar instanciación
    }
    
    /**
     * Obtiene la instancia única de SessionFactory (Hibernate nativo).
     * Si la instancia no existe, la crea; si existe, la devuelve.
     * 
     * @return Instancia única de SessionFactory
     */
    public static synchronized SessionFactory getSessionFactory() {
        if (sessionFactory == null) {
            try {
                // Creamos una configuración de Hibernate
                Configuration configuration = new Configuration();
                
                // Cargamos la configuración desde hibernate.cfg.xml
                configuration.configure();
                
                // Creamos la SessionFactory
                sessionFactory = configuration.buildSessionFactory();
            } catch (Exception e) {
                System.err.println("Error al crear SessionFactory: " + e.getMessage());
                throw new RuntimeException("Error al crear SessionFactory", e);
            }
        }
        return sessionFactory;
    }
    
    /**
     * Obtiene la instancia única de EntityManagerFactory (JPA).
     * Si la instancia no existe, la crea; si existe, la devuelve.
     * 
     * @return Instancia única de EntityManagerFactory
     */
    public static synchronized EntityManagerFactory getEntityManagerFactory() {
        if (entityManagerFactory == null) {
            try {
                // Creamos la EntityManagerFactory usando la unidad de persistencia definida en persistence.xml
                entityManagerFactory = Persistence.createEntityManagerFactory(PERSISTENCE_UNIT_NAME);
            } catch (Exception e) {
                System.err.println("Error al crear EntityManagerFactory: " + e.getMessage());
                throw new RuntimeException("Error al crear EntityManagerFactory", e);
            }
        }
        return entityManagerFactory;
    }
    
    /**
     * Obtiene un nuevo EntityManager de JPA.
     * 
     * @return Nuevo EntityManager
     */
    public static EntityManager getEntityManager() {
        return getEntityManagerFactory().createEntityManager();
    }
    
    /**
     * Cierra la SessionFactory y la EntityManagerFactory.
     */
    public static void shutdown() {
        // Cerramos la SessionFactory si existe
        if (sessionFactory != null && !sessionFactory.isClosed()) {
            sessionFactory.close();
        }
        
        // Cerramos la EntityManagerFactory si existe
        if (entityManagerFactory != null && entityManagerFactory.isOpen()) {
            entityManagerFactory.close();
        }
    }
}
```

### Ejercicio 5: Clase LibroDAO (con JPA)

**Descripción**: Esta clase implementa el patrón DAO (Data Access Object) para la entidad Libro, utilizando JPA para realizar operaciones CRUD en la base de datos. A diferencia de la versión JDBC, esta implementación aprovecha las capacidades de mapeo objeto-relacional de JPA, simplificando el código y reduciendo la posibilidad de errores.

```java
package com.example.orm; // Define el paquete donde se encuentra la clase

import java.util.List; // Para trabajar con listas

import javax.persistence.EntityManager; // Para gestionar entidades JPA
import javax.persistence.EntityTransaction; // Para gestionar transacciones
import javax.persistence.TypedQuery; // Para consultas tipadas

/**
 * Clase que implementa el patrón DAO (Data Access Object) para la entidad Libro.
 * Utiliza JPA para realizar operaciones CRUD en la base de datos.
 */
public class LibroDAO {
    
    /**
     * Inserta un nuevo libro en la base de datos.
     * 
     * @param libro Libro a insertar
     * @return true si la inserción fue exitosa, false en caso contrario
     * @throws MiExcepcion Si hay algún error durante la inserción
     */
    public boolean insertar(Libro libro) throws MiExcepcion {
        EntityManager em = null;
        EntityTransaction tx = null;
        
        try {
            em = HibernateUtil.getEntityManager(); // Obtenemos un EntityManager
            tx = em.getTransaction(); // Iniciamos una transacción
            tx.begin();
            em.persist(libro); // Persistimos el libro
            tx.commit(); // Confirmamos la transacción
            
            return true;
        } catch (Exception e) {
            // Si hay un error, deshacemos la transacción
            if (tx != null && tx.isActive()) {
                tx.rollback();
            }
            throw new MiExcepcion("Error al insertar libro: " + e.getMessage(), e);
        } finally {
            // Cerramos el EntityManager
            if (em != null && em.isOpen()) {
                em.close();
            }
        }
    }
    
    /**
     * Actualiza un libro existente en la base de datos.
     * 
     * @param libro Libro con los nuevos datos
     * @return true si la actualización fue exitosa, false en caso contrario
     * @throws MiExcepcion Si hay algún error durante la actualización
     */
    public boolean actualizar(Libro libro) throws MiExcepcion {
        EntityManager em = null;
        EntityTransaction tx = null;
        
        try {
            em = HibernateUtil.getEntityManager(); // Obtenemos un EntityManager
            tx = em.getTransaction(); // Iniciamos una transacción
            tx.begin();
            
            // Actualizamos el libro
            Libro libroActualizado = em.merge(libro); // merge devuelve la entidad gestionada
            tx.commit(); // Confirmamos la transacción
            
            return libroActualizado != null;
        } catch (Exception e) {
            // Si hay un error, deshacemos la transacción
            if (tx != null && tx.isActive()) {
                tx.rollback();
            }
            throw new MiExcepcion("Error al actualizar libro: " + e.getMessage(), e);
        } finally {
            // Cerramos el EntityManager
            if (em != null && em.isOpen()) {
                em.close();
            }
        }
    }
    
    /**
     * Elimina un libro de la base de datos por su ISBN.
     * 
     * @param isbn ISBN del libro a eliminar
     * @return true si la eliminación fue exitosa, false en caso contrario
     * @throws MiExcepcion Si hay algún error durante la eliminación
     */
    public boolean eliminar(String isbn) throws MiExcepcion {
        EntityManager em = null;
        EntityTransaction tx = null;
        
        try {
            em = HibernateUtil.getEntityManager(); // Obtenemos un EntityManager
            tx = em.getTransaction(); // Iniciamos una transacción
            tx.begin();
            Libro libro = em.find(Libro.class, isbn); // Buscamos el libro por su ISBN
            
            // Si el libro existe, lo eliminamos
            if (libro != null) {
                em.remove(libro);
                tx.commit();
                return true;
            } else {
                // Si el libro no existe, deshacemos la transacción
                tx.rollback();
                return false;
            }
        } catch (Exception e) {
            // Si hay un error, deshacemos la transacción
            if (tx != null && tx.isActive()) {
                tx.rollback();
            }
            throw new MiExcepcion("Error al eliminar libro: " + e.getMessage(), e);
        } finally {
            // Cerramos el EntityManager
            if (em != null && em.isOpen()) {
                em.close();
            }
        }
    }
    
    /**
     * Obtiene todos los libros de la base de datos.
     * 
     * @return Lista de todos los libros
     * @throws MiExcepcion Si hay algún error durante la consulta
     */
    public List<Libro> obtenerTodos() throws MiExcepcion {
        EntityManager em = null;
        
        try {
            em = HibernateUtil.getEntityManager(); // Obtenemos un EntityManager
            
            // Creamos una consulta JPQL
            TypedQuery<Libro> query = em.createQuery("SELECT l FROM Libro l", Libro.class);
            
            // Ejecutamos la consulta y devolvemos los resultados
            return query.getResultList();
        } catch (Exception e) {
            throw new MiExcepcion("Error al obtener todos los libros: " + e.getMessage(), e);
        } finally {
            // Cerramos el EntityManager
            if (em != null && em.isOpen()) {
                em.close();
            }
        }
    }
    
    /**
     * Obtiene un libro de la base de datos por su ISBN.
     * 
     * @param isbn ISBN del libro a buscar
     * @return Libro encontrado o null si no existe
     * @throws MiExcepcion Si hay algún error durante la consulta
     */
    public Libro obtenerPorIsbn(String isbn) throws MiExcepcion {
        EntityManager em = null;
        
        try {
            em = HibernateUtil.getEntityManager(); // Obtenemos un EntityManager
            
            // Buscamos el libro por su ISBN
            // find devuelve null si no encuentra la entidad
            return em.find(Libro.class, isbn);
        } catch (Exception e) {
            throw new MiExcepcion("Error al obtener libro por ISBN: " + e.getMessage(), e);
        } finally {
            // Cerramos el EntityManager
            if (em != null && em.isOpen()) {
                em.close();
            }
        }
    }
    
    /**
     * Obtiene libros por autor.
     * 
     * @param autor Nombre o parte del nombre del autor
     * @return Lista de libros que coinciden con el criterio
     * @throws MiExcepcion Si hay algún error durante la consulta
     */
    public List<Libro> obtenerPorAutor(String autor) throws MiExcepcion {
        EntityManager em = null;
        
        try {
            em = HibernateUtil.getEntityManager(); // Obtenemos un EntityManager
            
            // Creamos una consulta JPQL con parámetro
            TypedQuery<Libro> query = em.createQuery(
                    "SELECT l FROM Libro l WHERE l.autor LIKE :autor", Libro.class);
            
            // Establecemos el valor del parámetro
            // El % es un comodín que representa cualquier secuencia de caracteres
            query.setParameter("autor", "%" + autor + "%");
            
            // Ejecutamos la consulta y devolvemos los resultados
            return query.getResultList();
        } catch (Exception e) {
            throw new MiExcepcion("Error al obtener libros por autor: " + e.getMessage(), e);
        } finally {
            // Cerramos el EntityManager
            if (em != null && em.isOpen()) {
                em.close();
            }
        }
    }
}
```

### Ejercicio 6: Clase AutorDAO (con JPA)

**Descripción**: Esta clase implementa el patrón DAO para la entidad Autor, utilizando JPA para realizar operaciones CRUD en la base de datos. Demuestra cómo trabajar con relaciones entre entidades, como la relación uno-a-muchos entre Autor y Libro.

```java
package com.example.orm; // Define el paquete donde se encuentra la clase

import java.util.List; // Para trabajar con listas

import javax.persistence.EntityManager; // Para gestionar entidades JPA
import javax.persistence.EntityTransaction; // Para gestionar transacciones
import javax.persistence.TypedQuery; // Para consultas tipadas

/**
 * Clase que implementa el patrón DAO (Data Access Object) para la entidad Autor.
 * Utiliza JPA para realizar operaciones CRUD en la base de datos.
 * Demuestra cómo trabajar con relaciones entre entidades.
 */
public class AutorDAO {
    
    /**
     * Inserta un nuevo autor en la base de datos.
     * 
     * @param autor Autor a insertar
     * @return true si la inserción fue exitosa, false en caso contrario
     * @throws MiExcepcion Si hay algún error durante la inserción
     */
    public boolean insertar(Autor autor) throws MiExcepcion {
        EntityManager em = null;
        EntityTransaction tx = null;
        
        try {
            // Obtenemos un EntityManager
            em = HibernateUtil.getEntityManager();
            
            // Iniciamos una transacción
            tx = em.getTransaction();
            tx.begin();
            
            // Persistimos el autor
            em.persist(autor);
            
            // Confirmamos la transacción
            tx.commit();
            
            return true;
        } catch (Exception e) {
            // Si hay un error, deshacemos la transacción
            if (tx != null && tx.isActive()) {
                tx.rollback();
            }
            throw new MiExcepcion("Error al insertar autor: " + e.getMessage(), e);
        } finally {
            // Cerramos el EntityManager
            if (em != null && em.isOpen()) {
                em.close();
            }
        }
    }
    
    /**
     * Actualiza un autor existente en la base de datos.
     * 
     * @param autor Autor con los nuevos datos
     * @return true si la actualización fue exitosa, false en caso contrario
     * @throws MiExcepcion Si hay algún error durante la actualización
     */
    public boolean actualizar(Autor autor) throws MiExcepcion {
        EntityManager em = null;
        EntityTransaction tx = null;
        
        try {
            // Obtenemos un EntityManager
            em = HibernateUtil.getEntityManager();
            
            // Iniciamos una transacción
            tx = em.getTransaction();
            tx.begin();
            
            // Actualizamos el autor
            // merge devuelve la entidad gestionada
            Autor autorActualizado = em.merge(autor);
            
            // Confirmamos la transacción
            tx.commit();
            
            return autorActualizado != null;
        } catch (Exception e) {
            // Si hay un error, deshacemos la transacción
            if (tx != null && tx.isActive()) {
                tx.rollback();
            }
            throw new MiExcepcion("Error al actualizar autor: " + e.getMessage(), e);
        } finally {
            // Cerramos el EntityManager
            if (em != null && em.isOpen()) {
                em.close();
            }
        }
    }
    
    /**
     * Elimina un autor de la base de datos por su ID.
     * 
     * @param id ID del autor a eliminar
     * @return true si la eliminación fue exitosa, false en caso contrario
     * @throws MiExcepcion Si hay algún error durante la eliminación
     */
    public boolean eliminar(Long id) throws MiExcepcion {
        EntityManager em = null;
        EntityTransaction tx = null;
        
        try {
            // Obtenemos un EntityManager
            em = HibernateUtil.getEntityManager();
            
            // Iniciamos una transacción
            tx = em.getTransaction();
            tx.begin();
            
            // Buscamos el autor por su ID
            Autor autor = em.find(Autor.class, id);
            
            // Si el autor existe, lo eliminamos
            if (autor != null) {
                em.remove(autor);
                tx.commit();
                return true;
            } else {
                // Si el autor no existe, deshacemos la transacción
                tx.rollback();
                return false;
            }
        } catch (Exception e) {
            // Si hay un error, deshacemos la transacción
            if (tx != null && tx.isActive()) {
                tx.rollback();
            }
            throw new MiExcepcion("Error al eliminar autor: " + e.getMessage(), e);
        } finally {
            // Cerramos el EntityManager
            if (em != null && em.isOpen()) {
                em.close();
            }
        }
    }
    
    /**
     * Obtiene todos los autores de la base de datos.
     * 
     * @return Lista de todos los autores
     * @throws MiExcepcion Si hay algún error durante la consulta
     */
    public List<Autor> obtenerTodos() throws MiExcepcion {
        EntityManager em = null;
        
        try {
            // Obtenemos un EntityManager
            em = HibernateUtil.getEntityManager();
            
            // Creamos una consulta JPQL
            TypedQuery<Autor> query = em.createQuery("SELECT a FROM Autor a", Autor.class);
            
            // Ejecutamos la consulta y devolvemos los resultados
            return query.getResultList();
        } catch (Exception e) {
            throw new MiExcepcion("Error al obtener todos los autores: " + e.getMessage(), e);
        } finally {
            // Cerramos el EntityManager
            if (em != null && em.isOpen()) {
                em.close();
            }
        }
    }
    
    /**
     * Obtiene un autor de la base de datos por su ID.
     * 
     * @param id ID del autor a buscar
     * @return Autor encontrado o null si no existe
     * @throws MiExcepcion Si hay algún error durante la consulta
     */
    public Autor obtenerPorId(Long id) throws MiExcepcion {
        EntityManager em = null;
        
        try {
            // Obtenemos un EntityManager
            em = HibernateUtil.getEntityManager();
            
            // Buscamos el autor por su ID
            // find devuelve null si no encuentra la entidad
            return em.find(Autor.class, id);
        } catch (Exception e) {
            throw new MiExcepcion("Error al obtener autor por ID: " + e.getMessage(), e);
        } finally {
            // Cerramos el EntityManager
            if (em != null && em.isOpen()) {
                em.close();
            }
        }
    }
    
    /**
     * Obtiene autores por nombre o apellidos.
     * 
     * @param nombre Nombre o parte del nombre/apellidos a buscar
     * @return Lista de autores que coinciden con el criterio
     * @throws MiExcepcion Si hay algún error durante la consulta
     */
    public List<Autor> obtenerPorNombre(String nombre) throws MiExcepcion {
        EntityManager em = null;
        
        try {
            // Obtenemos un EntityManager
            em = HibernateUtil.getEntityManager();
            
            // Creamos una consulta JPQL con parámetros
            TypedQuery<Autor> query = em.createQuery(
                    "SELECT a FROM Autor a WHERE a.nombre LIKE :nombre OR a.apellidos LIKE :nombre", 
                    Autor.class);
            
            // Establecemos los valores de los parámetros
            // El % es un comodín que representa cualquier secuencia de caracteres
            query.setParameter("nombre", "%" + nombre + "%");
            
            // Ejecutamos la consulta y devolvemos los resultados
            return query.getResultList();
        } catch (Exception e) {
            throw new MiExcepcion("Error al obtener autores por nombre: " + e.getMessage(), e);
        } finally {
            // Cerramos el EntityManager
            if (em != null && em.isOpen()) {
                em.close();
            }
        }
    }
    
    /**
     * Añade un libro a un autor existente.
     * 
     * @param autorId ID del autor
     * @param libro Libro a añadir
     * @return true si la operación fue exitosa, false en caso contrario
     * @throws MiExcepcion Si hay algún error durante la operación
     */
    public boolean agregarLibro(Long autorId, LibroConAutor libro) throws MiExcepcion {
        EntityManager em = null;
        EntityTransaction tx = null;
        
        try {
            // Obtenemos un EntityManager
            em = HibernateUtil.getEntityManager();
            
            // Iniciamos una transacción
            tx = em.getTransaction();
            tx.begin();
            
            // Buscamos el autor por su ID
            Autor autor = em.find(Autor.class, autorId);
            
            // Si el autor existe, añadimos el libro
            if (autor != null) {
                // Establecemos la relación bidireccional
                autor.addLibro(libro);
                
                // Actualizamos el autor
                em.merge(autor);
                
                // Confirmamos la transacción
                tx.commit();
                return true;
            } else {
                // Si el autor no existe, deshacemos la transacción
                tx.rollback();
                return false;
            }
        } catch (Exception e) {
            // Si hay un error, deshacemos la transacción
            if (tx != null && tx.isActive()) {
                tx.rollback();
            }
            throw new MiExcepcion("Error al agregar libro a autor: " + e.getMessage(), e);
        } finally {
            // Cerramos el EntityManager
            if (em != null && em.isOpen()) {
                em.close();
            }
        }
    }
}
```

### Ejercicio 7: Clase MiExcepcion

**Descripción**: Esta clase representa una excepción personalizada para la aplicación, que permite encapsular y propagar errores específicos de manera controlada. Es especialmente útil para manejar errores relacionados con la base de datos y convertir excepciones técnicas en mensajes más comprensibles para el usuario.

```java
package com.example.orm; // Define el paquete donde se encuentra la clase

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
     * 
     * @param mensaje Mensaje descriptivo del error
     * @param causa Excepción original que causó el error
     */
    public MiExcepcion(String mensaje, Throwable causa) {
        super(mensaje, causa);
    }
}
```

### Ejercicio 8: Clase PruebasORM (con main)

**Descripción**: Esta clase contiene el método main y métodos para probar todas las funcionalidades implementadas en las clases anteriores. Aquí se realizan pruebas de operaciones CRUD utilizando JPA y Hibernate, demostrando cómo trabajar con entidades y relaciones en un contexto de mapeo objeto-relacional.

```java
package com.example.main; // Define el paquete donde se encuentra la clase principal

import java.util.List; // Para trabajar con listas

import com.example.orm.Autor; // Importamos la clase Autor
import com.example.orm.HibernateUtil; // Importamos la clase de utilidad Hibernate
import com.example.orm.Libro; // Importamos la clase Libro
import com.example.orm.LibroConAutor; // Importamos la clase LibroConAutor
import com.example.orm.LibroDAO; // Importamos la clase DAO para Libro
import com.example.orm.AutorDAO; // Importamos la clase DAO para Autor
import com.example.orm.MiExcepcion; // Importamos nuestra excepción personalizada

/**
 * Clase principal para probar las funcionalidades de ORM con JPA y Hibernate.
 * Contiene el método main y métodos para probar cada aspecto del mapeo objeto-relacional.
 */
public class PruebasORM {
    
    /**
     * Método principal que ejecuta las pruebas.
     * @param args Argumentos de línea de comandos (no utilizados)
     */
    public static void main(String[] args) {
        try {
            // Probamos las diferentes operaciones con entidades
            probarLibroSimple();
            probarAutorConLibros();
            
            // Cerramos las factorías al finalizar
            HibernateUtil.shutdown();
            
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
     * Prueba operaciones CRUD con la entidad Libro.
     * @throws MiExcepcion Si hay algún error durante las pruebas
     */
    private static void probarLibroSimple() throws MiExcepcion {
        System.out.println("\n=== Pruebas con Libro Simple ===");
        
        // Creamos un objeto DAO para Libro
        LibroDAO libroDAO = new LibroDAO();
        
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
        System.out.println("Insertando libros...");
        boolean resultado1 = libroDAO.insertar(libro1);
        boolean resultado2 = libroDAO.insertar(libro2);
        
        // Mostramos los resultados
        System.out.println("Inserción de libro 1: " + (resultado1 ? "Exitosa" : "Fallida"));
        System.out.println("Inserción de libro 2: " + (resultado2 ? "Exitosa" : "Fallida"));
        
        // Consultamos todos los libros
        System.out.println("\nConsultando todos los libros...");
        List<Libro> libros = libroDAO.obtenerTodos();
        
        // Mostramos los libros obtenidos
        System.out.println("Libros en la base de datos:");
        for (Libro libro : libros) {
            System.out.println("  " + libro);
        }
        
        // Consultamos un libro por su ISBN
        System.out.println("\nConsultando libro por ISBN...");
        String isbn = "9788401352836"; // ISBN de "El Quijote"
        Libro libro = libroDAO.obtenerPorIsbn(isbn);
        
        // Mostramos el libro obtenido
        if (libro != null) {
            System.out.println("Libro con ISBN " + isbn + ":");
            System.out.println("  " + libro);
            
            // Modificamos algunos datos del libro
            System.out.println("\nActualizando libro...");
            libro.setTitulo("Don Quijote de la Mancha");
            libro.setEditorial("Real Academia Española");
            libro.setNumPaginas(1250);
            
            // Actualizamos el libro en la base de datos
            boolean resultadoActualizacion = libroDAO.actualizar(libro);
            
            // Mostramos el resultado
            System.out.println("Actualización: " + (resultadoActualizacion ? "Exitosa" : "Fallida"));
            
            // Consultamos el libro actualizado
            Libro libroActualizado = libroDAO.obtenerPorIsbn(isbn);
            
            // Mostramos el libro después de la actualización
            System.out.println("Libro después de actualizar:");
            System.out.println("  " + libroActualizado);
        } else {
            System.out.println("No se encontró un libro con ISBN " + isbn);
        }
        
        // Eliminamos un libro
        System.out.println("\nEliminando libro...");
        String isbnEliminar = "9788420412146"; // ISBN de "Cien años de soledad"
        boolean resultadoEliminacion = libroDAO.eliminar(isbnEliminar);
        
        // Mostramos el resultado
        System.out.println("Eliminación: " + (resultadoEliminacion ? "Exitosa" : "Fallida"));
        
        // Consultamos todos los libros después de la eliminación
        System.out.println("\nConsultando todos los libros después de la eliminación...");
        libros = libroDAO.obtenerTodos();
        
        // Mostramos los libros obtenidos
        System.out.println("Libros en la base de datos:");
        for (Libro l : libros) {
            System.out.println("  " + l);
        }
    }
    
    /**
     * Prueba operaciones con relaciones entre entidades (Autor y LibroConAutor).
     * 
     * @throws MiExcepcion Si hay algún error durante las pruebas
     */
    private static void probarAutorConLibros() throws MiExcepcion {
        System.out.println("\n=== Pruebas con Autor y Libros (Relaciones) ===");
        
        // Creamos objetos DAO
        AutorDAO autorDAO = new AutorDAO();
        
        // Creamos algunos autores de ejemplo
        Autor autor1 = new Autor("Miguel", "de Cervantes", "Española", 1547);
        Autor autor2 = new Autor("Gabriel", "García Márquez", "Colombiana", 1927);
        
        // Insertamos los autores en la base de datos
        System.out.println("Insertando autores...");
        boolean resultado1 = autorDAO.insertar(autor1);
        boolean resultado2 = autorDAO.insertar(autor2);
        
        // Mostramos los resultados
        System.out.println("Inserción de autor 1: " + (resultado1 ? "Exitosa" : "Fallida"));
        System.out.println("Inserción de autor 2: " + (resultado2 ? "Exitosa" : "Fallida"));
        
        // Consultamos todos los autores
        System.out.println("\nConsultando todos los autores...");
        List<Autor> autores = autorDAO.obtenerTodos();
        
        // Mostramos los autores obtenidos
        System.out.println("Autores en la base de datos:");
        for (Autor autor : autores) {
            System.out.println("  " + autor);
        }
        
        // Creamos algunos libros y los asociamos a los autores
        System.out.println("\nCreando libros y asociándolos a autores...");
        
        // Obtenemos los IDs de los autores insertados
        Long idAutor1 = autor1.getId();
        Long idAutor2 = autor2.getId();
        
        // Creamos libros para el autor 1
        LibroConAutor libro1 = new LibroConAutor("9788401352836", "El Quijote", 1605, 
                                                "Alfaguara", 863);
        
        LibroConAutor libro2 = new LibroConAutor("9788420412123", "Novelas Ejemplares", 1613, 
                                                "Cátedra", 350);
        
        // Creamos libros para el autor 2
        LibroConAutor libro3 = new LibroConAutor("9788420412146", "Cien años de soledad", 1967, 
                                                "Cátedra", 471);
        
        LibroConAutor libro4 = new LibroConAutor("9788420412456", "El amor en los tiempos del cólera", 1985, 
                                                "Debolsillo", 490);
        
        // Añadimos los libros a los autores
        autorDAO.agregarLibro(idAutor1, libro1);
        autorDAO.agregarLibro(idAutor1, libro2);
        autorDAO.agregarLibro(idAutor2, libro3);
        autorDAO.agregarLibro(idAutor2, libro4);
        
        // Consultamos los autores con sus libros
        System.out.println("\nConsultando autores con sus libros...");
        
        // Obtenemos el autor 1 con sus libros
        Autor autorConLibros1 = autorDAO.obtenerPorId(idAutor1);
        
        // Mostramos el autor y sus libros
        if (autorConLibros1 != null) {
            System.out.println("Autor: " + autorConLibros1.getNombre() + " " + autorConLibros1.getApellidos());
            System.out.println("Libros:");
            for (LibroConAutor libro : autorConLibros1.getLibros()) {
                System.out.println("  " + libro.getTitulo() + " (" + libro.getAnioPublicacion() + ")");
            }
        }
        
        // Obtenemos el autor 2 con sus libros
        Autor autorConLibros2 = autorDAO.obtenerPorId(idAutor2);
        
        // Mostramos el autor y sus libros
        if (autorConLibros2 != null) {
            System.out.println("\nAutor: " + autorConLibros2.getNombre() + " " + autorConLibros2.getApellidos());
            System.out.println("Libros:");
            for (LibroConAutor libro : autorConLibros2.getLibros()) {
                System.out.println("  " + libro.getTitulo() + " (" + libro.getAnioPublicacion() + ")");
            }
        }
        
        // Buscamos autores por nombre
        System.out.println("\nBuscando autores por nombre...");
        List<Autor> autoresPorNombre = autorDAO.obtenerPorNombre("García");
        
        // Mostramos los autores encontrados
        System.out.println("Autores que contienen 'García':");
        for (Autor autor : autoresPorNombre) {
            System.out.println("  " + autor.getNombre() + " " + autor.getApellidos());
        }
    }
}
```

### Archivo persistence.xml

**Descripción**: Este archivo de configuración XML define la unidad de persistencia para JPA, especificando la conexión a la base de datos, las propiedades de Hibernate y las clases de entidad. Se coloca en el directorio META-INF del classpath.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<persistence xmlns="http://xmlns.jcp.org/xml/ns/persistence"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/persistence
                                 http://xmlns.jcp.org/xml/ns/persistence/persistence_2_2.xsd"
             version="2.2">
    
    <!-- Unidad de persistencia para la biblioteca -->
    <persistence-unit name="bibliotecaPU" transaction-type="RESOURCE_LOCAL">
        
        <!-- Proveedor de persistencia (Hibernate) -->
        <provider>org.hibernate.jpa.HibernatePersistenceProvider</provider>
        
        <!-- Clases de entidad -->
        <class>com.example.orm.Libro</class>
        <class>com.example.orm.Autor</class>
        <class>com.example.orm.LibroConAutor</class>
        
        <!-- Propiedades de la unidad de persistencia -->
        <properties>
            <!-- Propiedades de conexión a la base de datos -->
            <property name="javax.persistence.jdbc.driver" value="com.mysql.cj.jdbc.Driver"/>
            <property name="javax.persistence.jdbc.url" value="jdbc:mysql://localhost:3306/biblioteca?serverTimezone=UTC"/>
            <property name="javax.persistence.jdbc.user" value="root"/>
            <property name="javax.persistence.jdbc.password" value="password"/>
            
            <!-- Propiedades de Hibernate -->
            <property name="hibernate.dialect" value="org.hibernate.dialect.MySQL8Dialect"/>
            <property name="hibernate.show_sql" value="true"/>
            <property name="hibernate.format_sql" value="true"/>
            
            <!-- Estrategia de generación de esquema -->
            <property name="hibernate.hbm2ddl.auto" value="update"/>
        </properties>
    </persistence-unit>
</persistence>
```
