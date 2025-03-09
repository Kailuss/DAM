---
number headings: first-level 0, start-at 1, max 2, _.1., auto, contents ^toc, skip ^skipped
obsidianUIMode: preview
banner: "![[../../../../Banners/ad.jpg]]"
banner_y: 0.19
---

# Resumen Tema AD04
## 1. ORM: Object Relational Mapping

La gestión de datos en programación orientada a objetos se realiza mediante la manipulación de objetos, que suelen ser valores compuestos con múltiples atributos. Sin embargo, las bases de datos relacionales solo almacenan valores escalares (cadenas, números) organizados en tablas. Para evitar la conversión manual entre objetos y registros de la base de datos, se utiliza el mapeo objeto-relacional (ORM), que automatiza este proceso.

El ORM permite al programador trabajar con objetos sin preocuparse por las consultas SQL. En teoría, el ORM debería ser transparente, pero en la práctica siempre hay cierta presencia y puede afectar el rendimiento.

**Objetivos del ORM:**

- Ahorrar tiempo.
- Simplificar el desarrollo.
- Incrementar el rendimiento y escalabilidad.
- Reducir la complejidad arquitectónica.

Aunque existen bases de datos orientadas a objetos que no requieren mapeo, no han sido populares.

## 2. Java Persistence API (JPA)

JPA es una API de mapeo objeto-relacional para aplicaciones Java. Consta de:

- La API de persistencia.
- Metadatos para el mapeo.
- JPQL (Java Persistence Query Language), similar a SQL pero basado en objetos.
- La API Criteria para consultas.

JPA es una especificación, por lo que requiere implementaciones como Hibernate o EclipseLink.

### 2.1. **Unidad de persistencia**

Una unidad de persistencia es un conjunto de propiedades con un nombre único que gestiona entidades y su almacenamiento en la base de datos. Se define en el archivo `persistence.xml`, ubicado en `META-INF`. Este archivo especifica las clases de entidad, el DataSource, y otras propiedades como la URL de la base de datos, usuario, contraseña, y configuraciones de Hibernate.

Ejemplo de configuración en `persistence.xml`:

```xml
<persistence xmlns="https://jakarta.ee/xml/ns/persistence" version="3.1">
    <persistence-unit name="Biblioteca-PU">
        <provider>org.hibernate.jpa.HibernatePersistenceProvider</provider>
        <class>cat.paucasesnovescifp.model.Autor</class>
        <exclude-unlisted-classes>true</exclude-unlisted-classes>
        <properties>
            <property name="jakarta.persistence.jdbc.url" value="jdbc:mysql://192.168.56.95:3306/biblioteca"/>
            <property name="jakarta.persistence.jdbc.user" value="usuari"/>
            <property name="jakarta.persistence.jdbc.password" value="seCret_19"/>
            <property name="hibernate.connection.pool_size" value="1"/>
            <property name="hibernate.show_sql" value="true"/>
            <property name="hibernate.format_sql" value="true"/>
            <property name="hbm2ddl.auto" value="none"/>
        </properties>
    </persistence-unit>
</persistence>
```

### 2.2. **Clases de entidad**

Las clases de entidad son POJOs que representan tablas de la base de datos. Cada atributo de la clase se mapea a una columna de la tabla. Las entidades deben implementar `equals` y `hashCode`.

#### 2.2.1. Anotaciones

El mapeo se realiza mediante anotaciones:

- `@Entity`: Marca la clase como entidad.
- `@Table`: Especifica la tabla y esquema.
- `@Column`: Mapea un atributo a una columna.
- `@Id`: Define la clave primaria.
- `@GeneratedValue`: Indica que el valor se genera automáticamente.

Ejemplo de clase `Autor`:

```java
@Entity
@Table(name = "AUTORS", schema = "biblioteca")
public class Autor {
    @Id
    @Column(name = "ID_AUT", nullable = false)
    private Integer id;

    @Column(name = "NOM_AUT", length = 100)
    private String nombre;

    @Column(name = "DNAIX_AUT")
    private Instant dnaixAut;
}
```

#### 2.2.2. Relaciones entre tablas

Las relaciones entre tablas se mantienen en las entidades. Por ejemplo, en una relación 1-n entre `Autor` y `Nacionalitat`, la clase `Autor` tendrá un atributo de tipo `Nacionalitat`, y `Nacionalitat` tendrá una lista de `Autor`.

#### 2.2.3. Fetch: Recuperación de datos asociados

El tipo de fetch (eager o lazy) determina cuándo se cargan los objetos relacionados:

- **Eager**: Carga los objetos relacionados al recuperar la entidad.
- **Lazy**: Carga los objetos relacionados al acceder a ellos.

Por defecto, `@OneToMany` y `@ManyToMany` son lazy, mientras que `@ManyToOne` y `@OneToOne` son eager.

### 2.3. **Contexto de persistencia: Entity Manager**

El `EntityManager` gestiona el contexto de persistencia, donde se realizan operaciones como crear, modificar o eliminar entidades. Es importante mantener el `EntityManager` activo solo durante las operaciones necesarias.

Ejemplo de uso:

```java
try (EntityManagerFactory emf = Persistence.createEntityManagerFactory("Biblioteca-PU");
     EntityManager em = emf.createEntityManager()) {
    Autor ramon = em.find(Autor.class, 1);
    System.out.println("ramon = " + ramon);
}
```

Métodos importantes:

- `.find()`: Recupera una entidad por su ID.
- `.persist()`: Inserta una entidad.
- `.merge()`: Actualiza una entidad.
- `.remove()`: Elimina una entidad.

#### 2.3.1. Transacciones

Las operaciones que modifican datos deben realizarse dentro de una transacción. Se gestionan mediante `EntityTransaction`:

- `.begin()`: Inicia la transacción.
- `.commit()`: Confirma los cambios.
- `.rollback()`: Deshace los cambios.

Ejemplo:

```java
EntityTransaction transaccio = em.getTransaction();
try {
    transaccio.begin();
    transaccio.commit();
} catch (Exception e) {
    if (transaccio.isActive()) {
        transaccio.rollback();
    }
}
```

### 2.4. **Ciclo de vida de una entidad**

Un objeto de entidad puede estar en los siguientes estados:

- **New**: Recién creado, no relacionado con la base de datos.
- **Managed**: Relacionado con la base de datos.
- **Removed**: Marcado para eliminación.
- **Detached**: Perdió la relación con el contexto de persistencia.

### 2.5. **Definición de las clases de entidad**

Cada tabla de la base de datos se representa con una clase de entidad. Los atributos de la clase deben coincidir con los campos de la tabla, y los tipos deben ser adecuados. Las relaciones se representan con atributos de tipo entidad.

#### 2.5.1. Anotaciones de la clase

- `@Entity`: Marca la clase como entidad.
- `@Table`: Especifica la tabla y esquema.

#### 2.5.2. Anotaciones de los atributos

- `@Basic`: Mapea un atributo a un tipo predefinido.
- `@Column`: Especifica la columna de la tabla.
- `@Id`: Define la clave primaria.
- `@GeneratedValue`: Indica que el valor se genera automáticamente.
- `@Transient`: Indica que un atributo no se almacena en la base de datos.

#### 2.5.3. Claves compuestas

Para claves primarias compuestas, se define una clase separada con `@Embeddable` y se usa en la entidad con `@EmbeddedId`.

#### 2.5.4. Relaciones

Las relaciones entre tablas se mantienen en las entidades mediante anotaciones como `@OneToOne`, `@OneToMany`, `@ManyToOne`, y `@ManyToMany`. Las relaciones pueden ser unidireccionales o bidireccionales.

## 3. Consideraciones importantes

Si no se utiliza una entidad para representar una tabla intermedia en una relación n-m, el ORM actualizará automáticamente la tabla intermedia al modificar las entidades relacionadas.
