---
number headings: first-level 0, start-at 1, max 3, _.1., auto, contents ^toc, skip ^skipped
tags: []
---
## 1. ORM: Object Relational Mapping

La gestión de datos en programación orientada a objetos se realiza a través de la manipulación de objetos, que casi siempre son valores compuestos. Un objeto suele tener varios atributos que pueden ser otros objetos con sus propios atributos.

Las bases de datos relacionales solo pueden almacenar valores escalares, como cadenas de caracteres o números enteros, y organizarlos en tablas.

El programador debe convertir los valores representados en forma de objetos en valores simples o agrupados para almacenarlos en la base de datos y, además, implementar el proceso inverso. Alternativamente, podría trabajar únicamente con valores escalares, perdiendo así las ventajas de la programación orientada a objetos.

Para aprovechar el potencial de la programación orientada a objetos y evitar el proceso de conversión de objeto a registro de base de datos y viceversa, se ha creado la automatización de este proceso mediante el mapeo objeto-relacional. Este proceso define las correspondencias entre objetos y sus atributos, y entre tablas y sus columnas.

En teoría, la misión de un paquete ORM, una vez configurado, es que el programador trabaje con los objetos de su lenguaje y se olvide por completo de la base de datos. No debería preocuparse por realizar 'selects' o 'updates', sino en crear objetos y acceder a sus atributos. El ORM sería el encargado de determinar cuándo es necesario realizar un 'select' o un 'insert', construir la consulta, ejecutarla y devolver el objeto solicitado.

En la práctica, siempre hay cierta presencia del paquete ORM, nunca es completamente transparente y puede introducir penalizaciones en el rendimiento de la aplicación.

**Los objetivos reales de utilizar una herramienta ORM son:**

- Ahorrar tiempo
- Simplificar el desarrollo (la herramienta ORM absorbe la parte compleja que antes realizaba el desarrollador)
- Incrementar el rendimiento y la escalabilidad
- Disminuir la complejidad en la arquitectura

La crítica más común hacia estos paquetes se basa en el origen del problema: traducir los objetos a un modelo relacional. Si existen bases de datos orientadas a objetos que no necesitan esta traducción, ¿por qué no utilizarlas? Estas bases de datos no definen tablas, sino tipos, haciendo innecesario el mapeo. Sin embargo, estas bases de datos nunca han sido muy populares.

---

## 2. Java Persistence API

La API de persistencia de Java proporciona a los desarrolladores una herramienta de mapeo objeto-relacional para utilizar bases de datos relacionales dentro de aplicaciones Java. Consta de cuatro componentes:

- La API de persistencia
- Metadatos para el mapeo objeto-relacional
- El Java Persistence Query Language (JPQL), un lenguaje de consultas similar a SQL pero utilizando los objetos de la aplicación en lugar de las tablas de la base de datos
- La API Criteria, otra forma de realizar consultas en la base de datos

JPA es una especificación, define clases, interfaces y métodos, pero no los implementa. Para utilizarla en un proyecto es necesario utilizar alguna librería que la implemente. Las más conocidas son Hibernate y EclipseLink.

---

### 2.1. Unidad de persistencia

Una unidad de persistencia es una colección de propiedades con un nombre único que se utiliza en una aplicación para gestionar determinadas entidades (las clases que representan la base de datos) y cómo se almacenan en la base de datos.

Para utilizar JPA en una aplicación es necesaria al menos una unidad de persistencia. Se pueden definir varias, pero todas deben tener un nombre único.

Las unidades de persistencia se definen en el archivo 'persistence.xml', que suele ubicarse en el directorio META-INF.

Algunas de las propiedades que se definen en una unidad de persistencia son:

- Las clases de entidad gestionadas por la unidad de persistencia
- La información del DataSource del servidor

Ejemplo de configuración en 'persistence.xml':

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<!-- El elemento raíz, con las definiciones de los espacios de nombres, el esquema y la versión -->
<persistence xmlns="https://jakarta.ee/xml/ns/persistence"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xsi:schemaLocation="https://jakarta.ee/xml/ns/persistence
 https://jakarta.ee/xml/ns/persistence/persistence_3_2.xsd"
 version="3.1">
    <!-- Definición de una unidad de persistencia. Puede haber más de una. Debe tener un nombre -->
    <persistence-unit name="Biblioteca-PU">
        <!-- Qué librería utiliza JPA, en este caso Hibernate -->
        <provider>org.hibernate.jpa.HibernatePersistenceProvider</provider>
        <!-- Si queremos que la unidad gestione todas las entidades no es necesario poner nada -->
        <!-- Si queremos especificar qué entidades utilizará esta unidad las definimos aquí -->
        <class>cat.paucasesnovescifp.model.Autor</class>
        <!-- Queremos que las que no estén listadas se incluyan o no -->
        <exclude-unlisted-classes>true</exclude-unlisted-classes>
        <!-- Propiedades de la unidad de persistencia -->
        <properties>
            <!-- Propiedades de la conexión -->
            <property name="jakarta.persistence.jdbc.url" 
value="jdbc:mysql://192.168.56.95:3306/biblioteca"/>
            <property name="jakarta.persistence.jdbc.user" value="usuari"/>
            <property name="jakarta.persistence.jdbc.password" value="seCret_19"/>
            <!-- Para hacer pruebas ponemos 1 para no sobrecargar el servidor -->
            <property name="hibernate.connection.pool_size" value="1"/>
            <!-- Propiedades para depuración. Así como está veremos por la consola las consultas SQL que
 se generan. Nunca en producción -->
            <property name="hibernate.show_sql" value="true"/>
            <property name="hibernate.format_sql" value="true"/>
            <!-- Cómo queremos que se comporte Hibernate con la base de datos al arrancar-->
            <!-- Con none no hace nada -->
            <!-- Con create crea la base de datos a partir de las entidades al arrancar la aplicación-->
            <property name="hbm2ddl.auto" value="none"/>
        </properties>
    </persistence-unit>
 </persistence>
```

---
### 2.2. Clases de entidad

Ya hemos dicho que si utilizamos JPA tendremos objetos en nuestras aplicaciones que representarán las tuplas de la base de datos. Las clases que definen estos objetos se llaman **clases de entidad**.

Una clase de entidad es un **POJO** (Plain Old Java Object) con un constructor sin parámetros que representa una tabla de la base de datos dentro de la aplicación.

Esta clase tendrá un atributo por cada campo de la base de datos que queramos utilizar, con el correspondiente `getter` y `setter`.

Las entidades deben implementar los métodos `equals` y `hashCode`.

Cada clase de entidad debe **mapearse** con una tabla y cada atributo de la clase con un campo de la tabla. De esta manera, el paquete ORM será capaz de llenar objetos Java con el resultado de una consulta y de generar un **update**, **insert** o **delete** con los datos de un objeto Java.

#### 2.2.1 Anotaciones

El mapeo, tanto en la clase como en los atributos, se realiza mediante anotaciones. Algunas de las anotaciones más habituales son:

- **@Entity.** Marca la clase como entidad. Se coloca encima de la definición de la clase.
- **@Table(name = "AUTORS", schema="biblioteca", catalog="").** Define a qué tabla se mapea la clase. Se coloca después de la anotación **@Entity**.
- **@Column(name = "NOM_AUT").** Define a qué campo de la tabla se asocia el atributo declarado justo después. Puede incluir otros atributos, como **nullable** o **length**.
- **@Id.** Define el atributo como clave primaria de la tabla.

Por ejemplo, la tabla **AUTORS** podría mapearse a la clase **Autor** de la siguiente manera:

```java
@Entity
@Table(name = "AUTORS", schema = "biblioteca")
public class Autor {
    @Id
    @Column(name = "ID_AUT")
    private Integer id;

    @Column(name = "NOM_AUT")
    private String nombre;

    // Getters, setters, equals, hashCode, ...
}
```

Faltarían los **getters**, **setters**, etc. Con las anotaciones que hemos utilizado, el ORM será capaz de saber:

- Que esta clase es una entidad.
- A qué tabla corresponde esta clase de entidad.
- Qué atributo representa la clave primaria de la tabla.
- A qué columna de la tabla se asocia cada atributo de la clase.

Por lo tanto, podrá generar los **selects**, **inserts**, etc., necesarios para relacionar los objetos de esta clase con las correspondientes filas de la base de datos.

---

#### 2.2.2 Relaciones entre tablas

Cuando dos tablas de la base de datos están relacionadas con una relación 1 a n, esta relación debe mantenerse entre las entidades que representan dichas tablas. Normalmente se representa de la siguiente forma:

- En el lado n de la relación, la clase de entidad tiene un atributo de la clase de entidad del otro lado de la relación.
- En el lado 1 de la relación, la clase de entidad tiene un atributo que es una lista de la clase de entidad del otro lado de la relación.

Por ejemplo, si en la base de datos tenemos una relación entre Autor y Nacionalitat:

- La clase de entidad Autor tendrá un atributo cuyo tipo será la clase de entidad Nacionalitat.
- La clase de entidad Nacionalitat tendrá un atributo que será una lista de objetos de la clase Autor.

Esto permite navegar en ambos sentidos de la relación. Sin embargo, puede que solo interese que Autor tenga un atributo Nacionalitat sin necesidad de que Nacionalitat tenga la lista de autores asociados, o viceversa.

```java
public class Autor {
    private Integer id;
    private String nomAut;
    private Nacionalitat nacionalitat;
}

public class Nacionalitat {
   private String nacionalitat;
   private ArrayList<Autor> autors;
}
```

---

#### 2.2.3 Fetch: Recuperación de datos asociados por una relación

Se puede definir el tipo de Fetch (eager o lazy) para determinar el momento en que se cargan los objetos del otro lado de la relación. Se define en las anotaciones que mapean las relaciones como @ManyToMany, @OneToMany, @ManyToOne, @OneToOne.

Tipos de fetch:

- **Eager (Ansioso).** Al cargar la entidad, también se carga la lista con las entidades asociadas del otro lado de la relación. Si la lista no es muy grande, la penalización no es significativa. Sin embargo, si la lista es grande, el tiempo y la memoria necesarios para mantenerla pueden afectar al rendimiento. Además, puede ocurrir que se cargue la lista y no se utilice. Si cada entidad de la lista tiene otras listas asociadas, también se cargarán, lo que puede llevar a cargar toda la base de datos.
- **Lazy (Perezoso).** La lista con las entidades del lado n de la relación se carga al acceder a la lista desde la aplicación. Puede causar problemas si el EntityManager ya no está activo.

Valores por defecto:

- OneToMany: LAZY. Ejemplo: la lista de autores de una nacionalidad.
- ManyToOne: EAGER. Ejemplo: la nacionalidad de un autor.
- ManyToMany: LAZY. Ejemplo: los libros de un autor (un libro puede tener más de un autor).
- OneToOne: EAGER.

---
### 2.3. Contexto de persistencia: Entity Manager

El contexto de persistencia se refiere al entorno en el que se crea una entidad recuperándola de la base de datos, modificando sus datos, etc. Es el contexto en el que se relaciona un objeto de una clase de entidad con los datos correspondientes en la base de datos.

Es importante tener en cuenta que, salvo para la creación de una entidad y la correspondiente inserción en la base de datos, todas las demás operaciones que involucren la entidad y la base de datos deben realizarse dentro del mismo contexto de persistencia.

El objeto JPA que gestiona el contexto es el EntityManager. Este objeto proporciona los métodos para modificar la base de datos desde los objetos Java.

El EntityManager, entre otras cosas, mantiene una conexión con la base de datos, por lo que debe permanecer activo el menor tiempo posible.

Un atributo de una entidad marcado como LAZY solo puede recuperarse cuando el EntityManager que ha recuperado el objeto está activo.

Ejemplo de uso en una aplicación de escritorio:

```java
try (EntityManagerFactory emf = 
        Persistence.createEntityManagerFactory("Biblioteca-PU");
     EntityManager em = emf.createEntityManager()) {

    Autor ramon = em.find(Autor.class, 1);
    System.out.println("ramon = " + ramon); 
}
```

Para no ocupar conexiones al servidor de bases de datos cuando no se están utilizando, se recomienda crear y cerrar el EntityManager cada vez que se necesite realizar una operación en la base de datos. EntityManager implementa Autocloseable, por lo que puede utilizarse dentro del try() y se cerrará automáticamente.

Algunos métodos importantes de EntityManager son:

- `.find(Class clase, Object id)`: Realiza un select en la tabla mapeada y devuelve el objeto de la clase especificada con el identificador proporcionado.
- `.persist(Object x)`: Inserta los datos del objeto x en la tabla mapeada.
- `.merge(Object x)`: Realiza un update de los datos del objeto x en la tabla mapeada. También devuelve una copia del objeto relacionada con el contexto de persistencia actual.
- `.remove(Object x)`: Realiza un delete de la fila en la tabla mapeada que tenga como identificador el valor del atributo del objeto marcado con @Id.

Si el EntityManager con el que se recuperó el objeto ya no está activo, primero se debe realizar un merge para volver a asociar el objeto con la base de datos.

```java
Autor referenciat = em.merge(autor);
em.remove(referenciat);
```

---

#### 2.3.1 Transacciones

Por defecto, el EntityManager tiene la propiedad autocommit de las conexiones a la base de datos en false, por lo que deben gestionarse desde el propio código.

Todas las operaciones que impliquen modificaciones en los datos (todas excepto las consultas) deben incluirse dentro de una transacción.

Para ello, se obtiene un objeto EntityTransaction del EntityManager con el método getTransaction(). Algunos métodos importantes de este objeto son:

- `.begin()`: Inicia una transacción.
- `.commit()`: Finaliza la transacción haciendo permanentes los cambios en la base de datos.
- `.rollback()`: Finaliza la transacción deshaciendo los cambios en la base de datos.
- `.setRollbackOnly()`: Define la transacción de manera que solo pueda finalizar con un rollback.
- `.getRollbackOnly()`: Devuelve el valor de esta propiedad de la transacción.

El mismo objeto EntityTransaction puede utilizarse para realizar varias transacciones sucesivas.

Ejemplo de uso en una aplicación de escritorio:

```java
try (EntityManagerFactory emf = 
        Persistence.createEntityManagerFactory("Biblioteca-PU");
     EntityManager em = emf.createEntityManager()) {

    Autor ramon = em.find(Autor.class, 1);
    ramon.setNomAut("Llull, Ramon2");

    EntityTransaction transaccio = em.getTransaction();

    try {
        transaccio.begin();
        transaccio.commit();
    } catch (Exception e) {
        if (transaccio.isActive()) {
            transaccio.rollback();
        }
    }
}
```

> [!importante] 
> Todos los objetos que se encuentran en el contexto de persistencia y que han sido modificados desde que se recuperaron, se actualizan cuando se hace el commit, aunque no se haya ejecutado explícitamente persist, merge, etc. 

---
### 2.4. Ciclo de vida de una entidad

El ciclo de vida de una entidad en JPA incluye varios estados:

- **New.** El objeto se acaba de crear y solo reside en memoria; no está relacionado con la base de datos.
- **Managed.** El objeto en memoria está relacionado con la base de datos. Se alcanza este estado al recuperarlo de la base de datos o al asociarlo nuevamente mediante persist o merge. Solo en este estado se pueden recuperar los atributos marcados con fetch LAZY.
- **Removed.** Se ha indicado al EntityManager que se quiere borrar el objeto de la base de datos.
- **Detached.** El objeto ha perdido la relación con el contexto de persistencia, por ejemplo, porque se ha cerrado el EntityManager.

---

### 2.5. Definición de las clases de entidad

Normalmente, se define una clase de entidad para cada tabla de la base de datos que se quiera utilizar. La única excepción son las tablas que implementan relaciones n-m: si no almacenan información adicional, se pueden omitir.

Para utilizarlas con un ORM, las tablas de la base de datos deben tener una clave primaria.

En cada clase se define un atributo para cada campo de la tabla que se quiera utilizar. No es necesario tener todos los campos, aunque no se puede omitir ninguno obligatorio.

Los tipos de los atributos deben ser adecuados al tipo de datos del campo de la tabla. No todo puede ser String.

Los atributos que representan una relación con otra entidad serán del tipo de la entidad relacionada, no del tipo de la clave primaria de dicha entidad. Por ejemplo, si un libro tiene un atributo que hace referencia a su editor, este atributo será de la clase Editor, no de tipo int aunque ese sea el tipo del identificador en la base de datos.

Ejemplo de la tabla AUTORS en la base de datos y su representación en un POJO:

```java
public class Autor {
    private Integer id;
    private String nomAut;
    private Instant dnaixAut;
    private Nacionalitat fkNacionalitat;

    // Getters, setters, equals y hashcode
}
```

Cada objeto de la clase de entidad representa una tupla (fila) de la tabla de la base de datos.

---

#### 2.5.1 Anotaciones de la clase

Para convertir un POJO en una clase de entidad se deben utilizar dos anotaciones principales:

- **@Entity.** Marca la clase como clase de entidad, indicando que el ORM la puede utilizar para representar datos de una tabla de la base de datos.
- **@Table.** Indica la tabla con la que se mapeará esta entidad. Si la clase tiene el mismo nombre que la tabla, no es necesaria esta anotación.

Ejemplo:

```java
@Entity
@Table(name = "AUTORS", schema = "biblioteca")
public class Autor {
    // Atributos y métodos
}
```

Atributos de la anotación @Table:

- **name.** El nombre de la tabla con la que se mapea la clase de entidad.
- **schema.** El esquema de la base de datos al cual pertenece la tabla.

---

#### 2.5.2 Anotaciones de los atributos / métodos

Al igual que se anotó la clase para indicar que es una entidad y con qué tabla se mapea, también se debe indicar para cada atributo de la clase con qué campo de la tabla se mapea.

Estas anotaciones se pueden colocar tanto en la definición del atributo como en sus getters, pero nunca en ambos al mismo tiempo. Se recomienda seguir siempre el mismo criterio (o en todos los atributos o en todos los getters).

- `@Basic`: Indica que el atributo se mapea a uno de los tipos predefinidos. Es opcional.
    
    ```java
    @Basic
    private String nomAut;
    ```
    
    - `optional`: Indica si el atributo es opcional o no. Por defecto es true. Si es un campo obligatorio, se debe poner en false.

---
- `@Column`: Especifica la columna de la tabla mapeada al atributo de la clase.
    
    ```java
    @Column(name = "COLLECCIO", nullable = false, length = 100)
    private String id;
    ```
    
    Atributos de la anotación @Column:
    
    - `name`: Nombre de la columna en la tabla. Es el único obligatorio.
    - `length`: Longitud de la columna.
    - `precision` y `scale`: Precisión y escala si es un campo numérico.
    - `unique`: Si la columna tiene una restricción de clave única. Por defecto es false.
    - `nullable`: Si la columna puede ser nula. Por defecto es true.
    - `insertable`: Si la columna se incluye en los inserts generados por el proveedor de persistencia. Por defecto es true.
    - `updatable`: Si la columna se incluye en los updates. Por defecto es true.

---
- `@Id`: Define el atributo que representa la clave primaria de la tabla.
    
    ```java
    @Id
    @Column(name = "ID_AUT", nullable = false)
    private Integer id;
    ```

---
- `@GeneratedValue`: Indica que el valor de la columna se genera automáticamente (por la base de datos).
    
    ```java
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Id
    @Column(name = "ID_AUT", nullable = false)
    private int idAut;
    ```
    
    Atributos de la anotación @GeneratedValue:
    
    - `strategy`: Cómo se generan los valores:
        - `AUTO`: Por defecto. El proveedor de persistencia elige la estrategia.
        - `IDENTITY`: La columna es auto-incremental.
        - `SEQUENCE`: Se genera a partir de una secuencia en la base de datos.
        - `TABLE`: El próximo valor se guarda en una tabla (que debe garantizar el bloqueo para evitar duplicados).
    - `generator`: Especifica el nombre del generador a utilizar (ej. el de la secuencia o el de la tabla).
- `@Transient`: Indica que un atributo no se almacenará en la base de datos.
    
    ```java
    @Transient
    private int numConsultes;
    ```
    
---
#### 2.5.3 Clausulas compuestas

Las clases con una clave primaria compuesta requieren un tratamiento especial. El identificador de la clase de entidad debe ser un atributo para poder comparar fácilmente dos objetos y determinar si representan la misma fila de la tabla o no.

Ejemplo de una clase de entidad con clave compuesta:

```java
@Embeddable
public class LliAutId implements Serializable {
    private static final long serialVersionUID = -3366967464064379516L;

    @Column(name = "FK_IDLLIB", nullable = false)
    private Integer fkIdllib;

    @Column(name = "FK_IDAUT", nullable = false)
    private Integer fkIdaut;

    // Getters, setters, equals y hashcode
}
```

Esta clase solo tiene atributos para los campos que forman la clave compuesta de la tabla. Estos campos no pueden ser nulos porque son parte del identificador.

La clase de entidad que utiliza esta clave compuesta se define de la siguiente manera:

```java
@Entity
@Table(name = "LLI_AUT", schema = "biblioteca")
public class LliAut {

    @EmbeddedId
    private LliAutId id;

    @MapsId(name="fkIdllib")
    @ManyToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "FK_IDLLIB", nullable = false)
    private Llibre fkIdllib;

    @MapsId("fkIdaut")
    @ManyToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "FK_IDAUT", nullable = false)
    private Autor fkIdaut;
}
```

En esta clase se utiliza el atributo de tipo `LliAutId` como clave compuesta y se definen relaciones `ManyToOne` con las entidades `Llibre` y `Autor`.

---
#### 2.5.4 Relaciones

Cuando una tabla de la base de datos tiene una clave foránea (foreign key) de otra tabla, esta relación debe mantenerse en las clases de entidad. Normalmente, esta clave foránea se representa con un atributo cuyo tipo es la clase referenciada.

Por defecto, las relaciones son unidireccionales, lo que permite acceder desde el lado n de una relación 1 a n hacia el lado 1, pero no al revés. Por ejemplo, desde un objeto de la clase Autor se puede acceder al objeto de la clase Nacionalitat asociado.

Si se quiere que la relación sea bidireccional, es decir, que desde un objeto de la clase Nacionalitat también se pueda acceder a los objetos relacionados de la clase Autor, es necesario añadir un atributo en ambas clases y configurar adecuadamente las anotaciones.

---
##### 3.1 Relación 1 - 1

En una relación uno a uno, una fila de una tabla está relacionada con una única fila de otra tabla.  
Por ejemplo, si un Comercial tiene asignado un único Cotxe y cada Cotxe está asignado a un único Comercial, se puede modelar de la siguiente forma:

- Se añade una clave foránea en la tabla Comercials que hace referencia a Cotxes.
- En la entidad que representa la tabla con la clave foránea, se crea un atributo de la clase que representa la otra tabla, con las siguientes anotaciones:

```java
@OneToOne(fetch = FetchType.LAZY, optional = false)
@JoinColumn(name = "COTXE_ID", nullable = false)
private Cotxe cotxe;
```

- `@OneToOne`: Indica que el atributo representa una relación uno a uno.
    
    - `fetch`: El tipo de fetch, puede ser EAGER (por defecto) o LAZY.
    - `optional`: Indica si el atributo puede ser nulo.
    - `cascade`: Especifica las operaciones en cascada, como update o delete.
- `@JoinColumn`: Especifica el nombre de la columna que mantiene la clave foránea.
    
    - `name`: El nombre de la columna en la tabla.
    - `referencedColumnName`: El nombre de la columna en la tabla referenciada (generalmente la clave primaria).
    - `unique`: Indica si la columna tiene una restricción de clave única (por defecto false).
    - `nullable`: Indica si la columna puede ser nula (por defecto true).
    - `insertable` y `updatable`: Indican si la columna se incluye en los inserts y updates generados.

Si se quiere que la relación sea bidireccional, en la clase Cotxe se añadiría un atributo de tipo Comercial con la siguiente anotación:

```java
@OneToOne(mappedBy="cotxe")
private Comercial comercial;
```

- `mappedBy`: Indica el nombre del atributo en la clase del otro lado de la relación que contiene el objeto de esta clase.

---

##### 2.6 Relación 1 - n

En una relación uno a muchos, una fila de una tabla está relacionada con varias filas de otra tabla.  
Por ejemplo, una Nacionalitat puede estar relacionada con varios Autors, pero cada Autor tiene solo una Nacionalitat.

- En el lado n de la relación (Autor), se añade un atributo del tipo de la clase que representa el lado 1 de la relación (Nacionalitat) con las siguientes anotaciones:

```java
@ManyToOne(fetch = FetchType.LAZY)
@JoinColumn(name = "FK_NACIONALITAT")
private Nacionalitat fkNacionalitat;
```

- `@ManyToOne`: Define la relación como muchos a uno, es decir, este atributo representa la parte n de una relación 1 a n.
    
    - `fetch`: El tipo de fetch, puede ser EAGER (por defecto) o LAZY.
    - `optional`: Indica si el atributo puede ser nulo.
    - `cascade`: Especifica las operaciones en cascada, como update o delete.
- `@JoinColumn`: Relaciona la columna de la tabla que implementa la clave foránea con la columna de la otra tabla que es la clave primaria.
    

Si la relación es bidireccional, en el lado 1 de la relación (Nacionalitat) se decora el atributo que representa la clave primaria con:

```java
@OneToMany(mappedBy = "fkNacionalitat")
private Collection<Autor> autors;
```

- `@OneToMany`: Indica que el atributo representa el lado 1 de una relación 1 - n.
    - `mappedBy`: Indica el atributo de la clase del otro lado de la relación que mantiene la información de la relación.
    - `fetch`: El tipo de fetch, puede ser EAGER (por defecto) o LAZY.
    - `cascade`: Especifica las operaciones en cascada, como update o delete.

---

##### 2.7 Relación n - m

En una relación muchos a muchos, cada fila de una tabla está relacionada con varias filas de otra tabla.  
Por ejemplo, un Libro puede estar relacionado con varios Temas, y un Tema puede estar relacionado con varios Libros.

Para mantener esta relación, se crea una tabla intermedia con las claves primarias de ambas tablas relacionadas.

Hay dos formas de modelar esta relación en JPA:

- Crear una entidad para la tabla intermedia y dos relaciones 1-n entre la tabla intermedia y cada una de las otras tablas. Esto es necesario si la tabla intermedia contiene información adicional.
- Crear directamente una relación n - m entre las dos clases de entidad, utilizando la anotación @ManyToMany.

Ejemplo de la segunda opción:

```java
@ManyToMany
@JoinTable(name = "LLI_TEMA",
    joinColumns = @JoinColumn(name = "FK_IDLLIB"),
    inverseJoinColumns = @JoinColumn(name = "FK_TEMA"))
private Set<Tema> temes = new LinkedHashSet<>();
```

- `@ManyToMany`: Indica que el atributo forma parte de una relación n - m.
    
    - `fetch`: Puede ser LAZY (por defecto) o EAGER.
- `@JoinTable`: Especifica la tabla intermedia que mantiene los datos de la relación.
    
    - `name`: Nombre de la tabla que implementa la relación n-m.
    - `joinColumns`: Nombre de las columnas que enlazan la tabla que representa la entidad con la tabla intermedia. Se utilizan anotaciones @JoinColumn para cada columna.
    - `inverseJoinColumns`: Las columnas de la tabla intermedia que representan el otro lado de la relación.

En el otro lado de la relación (en la clase Tema), se configura de forma más sencilla:

```java
@ManyToMany(mappedBy = "temes")
private Set<Llibre> llibres = new LinkedHashSet<>();
```

- `mappedBy`: Indica el nombre del atributo en la clase del otro lado de la relación que representa la relación (en este caso, temes).

---

## 3. Consideraciones importantes

Si no se utiliza una entidad para representar la tabla intermedia, el ORM actualizará dicha tabla con los valores del atributo creado en la entidad que representa la tabla N o la tabla M de la relación.

- Al añadir un tema a un libro, al actualizar el libro también se actualizará la tabla intermedia con la nueva relación.
- Al eliminar un tema o poner el atributo a null, al actualizar el libro se eliminarán las relaciones correspondientes en la tabla intermedia.

---