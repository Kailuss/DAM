---
tags: [AD, DAM]
cssclasses:
  - dam-ad
  - table-clean
banner: "![[ad.jpg]]"
banner_y: 0.32
number headings: off
---

# **AD.** Examen de Mayo

## Ejercicio 1.1.

Escribe un método que reciba un objeto de la clase entidad `Colleccio` que encontrarás al final del enunciado. El método debe devolver (hacer return) los libros de la colección.

- Debe Utilizar JPA
- Debe crear su propio entity manager
- No puede usar el método find ni una consulta jpql

### Material necesario

Clase `Colleccio` como entidad JPA:

```java name=Colleccio.java
@Entity
@Table(name= "COLLECTIONS")
public class Colleccio {
	@id
	@Column(name = "COLLECCIO", nullable = false, length = 100)
	private String colleccio;
	
	@OneToMAny(mappedBy = "fkColleccio")
	private Set<Llibre> llibres;

	public String getColleccio() {
		return colleccio;
	}

	public void setColleccio(String colleccio) {
		this.colleccio = colleccio;
	}

	public Set<Llibre> getLlibres() {
		return llibres;
	}

	public void setLlibres(Set<Llibre> llibres) {
		this.llibres = llibres;
	}

	public Colleccio() {
		llibres = new LinkedHasSet<>();
	}
}
```

### Solución

```java
import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.Persistence;

import java.util.Set;

public class ColleccioService {

    // Método que devuelve los libros de una colección
    public Set<Llibre> obtenerLibrosDeColleccio(Colleccio colleccio) {
        // Crear el EntityManagerFactory y el EntityManager
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("miUnidadDePersistencia");
        EntityManager em = emf.createEntityManager();

        try {
            // Iniciar una transacción
            em.getTransaction().begin();

            // Obtener la referencia directa del objeto Colleccio desde el contexto de persistencia
            Colleccio colleccioPersistente = em.getReference(Colleccio.class, colleccio.getColleccio());

            // Recuperar los libros de la colección
            Set<Llibre> llibres = colleccioPersistente.getLlibres();

            // Confirmar la transacción
            em.getTransaction().commit();

            // Devolver los libros
            return llibres;
        } catch (Exception e) {
            // Manejar posibles excepciones y hacer rollback si ocurre un error
            if (em.getTransaction().isActive()) {
                em.getTransaction().rollback();
            }
            throw e;
        } finally {
            // Cerrar el EntityManager
            em.close();
            emf.close();
        }
    }
}
```

### Explicación del código

- **EntityManagerFactory y EntityManager**: Se crean manualmente para gestionar la persistencia.
- **`getReference`**: Obtiene un proxy de la entidad sin ejecutar una consulta explícita.
- **Transacciones**: Se aseguran de que las operaciones estén controladas.
- **Cierre de recursos**: El `EntityManager` y `EntityManagerFactory` se cierran correctamente en el bloque `finally`.

## Ejercicio 1.2.

En nuestro servidor MongoDB tenemos una colección llamada `aspirants` con documentos como el que puedes ver en el anexo.

Escribe la consulta que escribirías en el shell de MongoDB para recuperar exclusivamente el NIF, el nombre y los apellidos de los aspirantes, ordenados por apellidos y nombre de forma ascendente.

```json name=aspirante.json
{
	"nif": "12007493F",
	"nom": "Bortomeu",
	"llinatges": "Villalonga Forteza",
	"adreça": "Sol 3",
	"codiPostal": "07865",
	"localitat": {
		"idLocalitat": "07057004",
		"nomLocalitat": "CALOGNGE",
		"illa": {
			"idIlla": "071",
			"nomIlla": "Mallorca"
		}
	}
}
```

### Solución

```shell
db.aspirants.find(
    {}, // Sin filtro, devuelve todos los documentos
    { nif: 1, nom: 1, llinatges: 1, _id: 0 } // Selecciona los campos deseados y excluye _id
).sort(
    { llinatges: 1, nom: 1 } // Orden ascendente por apellidos y nombre
);
```

### Explicación

- **`find`**:
    - El primer parámetro `{}` indica que no hay filtrado (se consideran todos los documentos).
    - El segundo parámetro `{ nif: 1, nom: 1, llinatges: 1, _id: 0 }` selecciona únicamente los campos `nif`, `nom`, y `llinatges`, excluyendo el campo `_id`.
- **`sort`**:
    - `{ llinatges: 1, nom: 1 }` ordena los resultados de forma ascendente (`1`) primero por `llinatges` y después por `nom`.

Este comando en el shell devolverá únicamente los campos solicitados en el orden deseado.

## Ejercicio 2.
Utiliza JPA para realizar este ejercicio. No uses JPQL. Tienes las entidades necesarias después del enunciado.

Crea una clase Controlador con un método que reciba el identificador de un actor y devuelva una lista con las películas en las que interviene. Esta clase no puede mostrar nada por pantalla.

Si tienes tiempo crea otra clase `main` que llame a este método y muestre esta lista por pantalla.

**Datos de conexión para este ejercicio**
- Servidor: `daw.paucasesnovescifp.cat`
- Puerto: `3306`
- Base de datos: `sakila`
- Usuario: `usuario`
- Contraseña: `seCret_24`

### Clase `actor`

```java
import cat.paucasesnovescifp.spaadmaig25.entitats.sakila.FilmActor;
import jakarta.persistence.*;
import org.hibernate.annotations.ColumnDefault;

import java.time.Instant;
import java.util.LinkedHashSet;
import java.util.Set;

@Entity
@Table(name = "actor")

public class Actor {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "actor_id", columnDefinition = "smallint UNSIGNED not null")
    private Integer id;

    @Column(name = "first_name", nullable = false, length = 45)
    private String firstName;

    @Column(name = "last_name", nullable = false, length = 45)
    private String lastName;

    @ColumnDefault("CURRENT_TIMESTAMP")
    @Column(name = "last_update", nullable = false)
    private Instant lastUpdate;

    @OneToMany(mappedBy = "actor")
    private Set<FilmActor> filmActors = new LinkedHashSet<>();

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public Instant getLastUpdate() {
        return lastUpdate;
    }

    public void setLastUpdate(Instant lastUpdate) {
        this.lastUpdate = lastUpdate;
    }

    public Set<FilmActor> getFilmActors() {
        return filmActors;
    }

    public void setFilmActors(Set<FilmActor> filmActors) {
        this.filmActors = filmActors;
    }
}
```

### Clase `Film`
```java
import jakarta.persistence.*;
import org.hibernate.annotations.ColumnDefault;

import java.math.BigDecimal;

@Entity
@Table(name = "film")
public class Film {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "film_id", columnDefinition = "smallint UNSIGNED not null")
    private Integer id;

    @Column(name = "title", nullable = false)
    private String title;

    @Lob
    @Column(name = "description")
    private String description;

//    @ManyToOne(fetch = FetchType.LAZY, optional = false)
//    @JoinColumn(name = "language_id", nullable = false)
//    private Language language;

    @ColumnDefault("'3'")
    @Column(name = "rental_duration", columnDefinition = "tinyint UNSIGNED not null")
    private Short rentalDuration;

    @ColumnDefault("4.99")
    @Column(name = "rental_rate", nullable = false, precision = 4, scale = 2)
    private BigDecimal rentalRate;

    @ColumnDefault("19.99")
    @Column(name = "replacement_cost", nullable = false, precision = 5, scale = 2)
    private BigDecimal replacementCost;

//    @ColumnDefault("CURRENT_TIMESTAMP")
//    @Column(name = "last_update", nullable = false)
//    private Instant lastUpdate;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

//    public Language getLanguage() {
//        return language;
//    }

//    public void setLanguage(Language language) {
//        this.language = language;
//    }

    public Short getRentalDuration() {
        return rentalDuration;
    }

    public void setRentalDuration(Short rentalDuration) {
        this.rentalDuration = rentalDuration;
    }

    public BigDecimal getRentalRate() {
        return rentalRate;
    }

    public void setRentalRate(BigDecimal rentalRate) {
        this.rentalRate = rentalRate;
    }

    public BigDecimal getReplacementCost() {
        return replacementCost;
    }

    public void setReplacementCost(BigDecimal replacementCost) {
        this.replacementCost = replacementCost;
    }

//    public Instant getLastUpdate() {
//        return lastUpdate;
//    }
//
//    public void setLastUpdate(Instant lastUpdate) {
//        this.lastUpdate = lastUpdate;
//    }

    public Film() {
    }

    public Film(Integer id, String title) {
        this.id = id;
        this.title = title;
    }

    @Override
    public String toString() {
        return "Film{" +
                "id=" + id +
                ", title='" + title + '\'' +
                ", description='" + description + '\''  +
                ", rentalDuration=" + rentalDuration +
                ", rentalRate=" + rentalRate +
                ", replacementCost=" + replacementCost +
                '}';
    }

}
```

### Clase `FilmActor`
```java
import cat.paucasesnovescifp.spaadmaig25.entitats.sakila.Actor;
import cat.paucasesnovescifp.spaadmaig25.entitats.sakila.Film;
import cat.paucasesnovescifp.spaadmaig25.entitats.sakila.FilmActorId;
import jakarta.persistence.*;
import org.hibernate.annotations.ColumnDefault;

import java.time.Instant;

@Entity
@Table(name = "film_actor")

public class FilmActor {
    @EmbeddedId
    private FilmActorId id;

    @MapsId("actorId")
    @ManyToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "actor_id", nullable = false)
    private Actor actor;

    @MapsId("filmId")
    @ManyToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "film_id", nullable = false)
    private Film film;

    @ColumnDefault("CURRENT_TIMESTAMP")
    @Column(name = "last_update", nullable = false)
    private Instant lastUpdate;

    public FilmActorId getId() {
        return id;
    }

    public void setId(FilmActorId id) {
        this.id = id;
    }

    public Actor getActor() {
        return actor;
    }

    public void setActor(Actor actor) {
        this.actor = actor;
    }

    public Film getFilm() {
        return film;
    }

    public void setFilm(Film film) {
        this.film = film;
    }

    public Instant getLastUpdate() {
        return lastUpdate;
    }

    public void setLastUpdate(Instant lastUpdate) {
        this.lastUpdate = lastUpdate;
    }
}
```

### Clase `FilmAcrtorId`
```java
import jakarta.persistence.Column;
import jakarta.persistence.Embeddable;
import org.hibernate.Hibernate;

import java.io.Serializable;
import java.util.Objects;

@Embeddable
public class FilmActorId implements Serializable {
    private static final long serialVersionUID = 9220711675370055801L;
    @Column(name = "actor_id", columnDefinition = "smallint UNSIGNED not null")
    private Integer actorId;

    @Column(name = "film_id", columnDefinition = "smallint UNSIGNED not null")
    private Integer filmId;
  
    public Integer getActorId() {
        return actorId;
    }

    public void setActorId(Integer actorId) {
        this.actorId = actorId;
    }

    public Integer getFilmId() {
        return filmId;
    }

    public void setFilmId(Integer filmId) {
        this.filmId = filmId;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || Hibernate.getClass(this) != Hibernate.getClass(o)) return false;
        FilmActorId entity = (FilmActorId) o;
        return Objects.equals(this.actorId, entity.actorId) &&
                Objects.equals(this.filmId, entity.filmId);
    }

    @Override
    public int hashCode() {
        return Objects.hash(actorId, filmId);
    }
}
```

### Clase `Language`
```java
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import org.hibernate.annotations.ColumnDefault;

import java.time.Instant;

@Entity
@Table(name = "language")
public class Language {

    @Id
    @Column(name = "language_id", columnDefinition = "tinyint UNSIGNED not null")
    private Short id;

    @Column(name = "name", nullable = false, length = 20)
    private String name;

    @ColumnDefault("CURRENT_TIMESTAMP")
    @Column(name = "last_update", nullable = false)
    private Instant lastUpdate;
    
    public Short getId() {
        return id;
    }

    public void setId(Short id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Instant getLastUpdate() {
        return lastUpdate;
    }

    public void setLastUpdate(Instant lastUpdate) {
        this.lastUpdate = lastUpdate;
    }
}
```

### Solución
```java
package cat.paucasesnovescifp.spaadmaig25.controlador;

import cat.paucasesnovescifp.spaadmaig25.entitats.sakila.Actor;
import cat.paucasesnovescifp.spaadmaig25.entitats.sakila.Film;
import com.fasterxml.jackson.databind.ObjectMapper;
import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.Persistence;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Controlador {

    private final EntityManagerFactory emf;
    private final EntityManager em;

    // Constructor que inicializa la conexión con la base de datos
    public Controlador() {
        emf = Persistence.createEntityManagerFactory("sakilaPU");
        em = emf.createEntityManager();
    }

    /**
     * Devuelve una lista de películas en las que interviene un actor dado su identificador.
     *
     * @param actorId Identificador del actor.
     * @return Lista de películas.
     */
    public List<Film> obtenerPeliculasPorActor(int actorId) {
        List<Film> peliculas = new ArrayList<>();
        Actor actor = em.find(Actor.class, actorId);

        if (actor != null) {
            actor.getFilmActors().forEach(filmActor -> peliculas.add(filmActor.getFilm()));
        }

        return peliculas;
    }

    /**
     * Cierra las conexiones abiertas al EntityManager.
     */
    public void cerrarConexion() {
        if (em != null) em.close();
        if (emf != null) emf.close();
    }
}
```

```java
package cat.paucasesnovescifp.spaadmaig25.main;

import cat.paucasesnovescifp.spaadmaig25.controlador.Controlador;
import cat.paucasesnovescifp.spaadmaig25.entitats.sakila.Film;

import java.util.List;

public class Main {

    public static void main(String[] args) {
        Controlador controlador = new Controlador();

        // Obtener películas de un actor
        int actorId = 1; // Cambiar según el caso
        List<Film> peliculas = controlador.obtenerPeliculasPorActor(actorId);
        System.out.println("Películas del actor con ID " + actorId + ":");
        peliculas.forEach(System.out::println);

        // Cerrar conexiones
        controlador.cerrarConexion();
    }
}
```
## Ejercicio 3.
En la clase controlador del ejercicio anterior crea otro método que reciba una lista de objetos de la clase `Film` y la ruta de un archivo.

Debe guardar estos objetos dentro del archivo en formato `JSON`. Para facilitar las cosas pon como ruta el directorio actual `./films.json`.

Piensa que el archivo se utilizará para transmitir la información a otra máquina, no para que lo lea un humano. Si tienes tiempo, desde la clase con `main` llama a este método.

### Solución
```java
/**
 * Guarda una lista de objetos Film en un archivo JSON.
 *
 * @param films Lista de películas.
 * @param ruta  Ruta del archivo.
 */
public void guardarPeliculasEnJSON(List<Film> films, String ruta) {
    ObjectMapper mapper = new ObjectMapper();
    try {
        mapper.writeValue(new File(ruta), films);
    } catch (IOException e) {
        e.printStackTrace();
    }
}
```

```java
// main.java -> Guardar películas en JSON
String rutaJSON = "./films.json";
controlador.guardarPeliculasEnJSON(peliculas, rutaJSON);
System.out.println("Películas exportadas a " + rutaJSON);
```
## Ejercicio 4.1.
En tu base de datos PostgreSQL crea una tabla para guardar los datos de una notificación que debe enviar el sistema a un usuario. Esta tabla, además del identificador de la notificación, debe tener el texto que se mostrará, el identificador del usuario al que debe enviarse, si ya se ha enviado o no, y las distintas formas en las que se enviará, por ejemplo, por SMS, PUSH, por correo electrónico… De cada una de estas formas basa guardar una cadena que contenga su nombre.

Pon el DDL de la creación de la tabla en un archivo `.sql` en la raíz de la carpeta fuente del proyecto `src -> main -> java` si has utilizado maven o `src` si no lo has hecho.

**Datos de conexión**
- Servidor: `daw.paucasesnovescifp.cat`
- Puerto: `5432`
- Base de datos: *La utilizada en la práctica de PostgreSQL.*
- Usuario y contraseña: *Los usados en la práctica de PostgreSQL.*

### Solución

```sql
-- Creación de la tabla de notificaciones en PostgreSQL
CREATE TABLE notificaciones (
    id SERIAL PRIMARY KEY,
    texto TEXT NOT NULL,
    id_usuario INT NOT NULL,
    enviado BOOLEAN DEFAULT FALSE,
    medios_envio TEXT[]
);
```

## Ejercicio 4.2.
Modifica la clase `Notificacio` como creas conveniente de manera que pueda servir como POJO de la tabla creada antes.

En la clase `Controlador` crea un método que inserte una notificación en la base de datos y otro que devuelva todas las notificaciones.

Idealmente, prueba estos métodos desde la clase con `main`.

### Clase `Notificacio`

```java
public class Notificacio {
    private Integer id;
    private String text;
    private Integer idUsuari;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public Integer getIdUsuari() {
        return idUsuari;
    }

    public void setIdUsuari(Integer idUsuari) {
        this.idUsuari = idUsuari;
    }
}
```

### Solución

```java
package cat.paucasesnovescifp.spaadmaig25.entitats;

import java.util.List;

public class Notificacio {
    private Integer id;
    private String texto;
    private Integer idUsuario;
    private Boolean enviado;
    private List<String> mediosEnvio;

    // Getters y setters
    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getTexto() {
        return texto;
    }

    public void setTexto(String texto) {
        this.texto = texto;
    }

    public Integer getIdUsuario() {
        return idUsuario;
    }

    public void setIdUsuario(Integer idUsuario) {
        this.idUsuario = idUsuario;
    }

    public Boolean getEnviado() {
        return enviado;
    }

    public void setEnviado(Boolean enviado) {
        this.enviado = enviado;
    }

    public List<String> getMediosEnvio() {
        return mediosEnvio;
    }

    public void setMediosEnvio(List<String> mediosEnvio) {
        this.mediosEnvio = mediosEnvio;
    }
}
```

```java
package cat.paucasesnovescifp.spaadmaig25.controlador;

import cat.paucasesnovescifp.spaadmaig25.entitats.Notificacio;
import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.Persistence;

import java.util.List;

public class ControladorNotificaciones {

    private final EntityManagerFactory emf;
    private final EntityManager em;

    // Constructor que inicializa la conexión con la base de datos
    public ControladorNotificaciones() {
        emf = Persistence.createEntityManagerFactory("notificacionesPU");
        em = emf.createEntityManager();
    }

    /**
     * Inserta una nueva notificación en la base de datos.
     *
     * @param notificacio Notificación a insertar.
     */
    public void insertarNotificacion(Notificacio notificacio) {
        em.getTransaction().begin();
        em.persist(notificacio);
        em.getTransaction().commit();
    }

    /**
     * Devuelve todas las notificaciones de la base de datos.
     *
     * @return Lista de notificaciones.
     */
    public List<Notificacio> obtenerNotificaciones() {
        return em.createQuery("SELECT n FROM Notificacio n", Notificacio.class).getResultList();
    }

    /**
     * Cierra las conexiones abiertas al EntityManager.
     */
    public void cerrarConexion() {
        if (em != null) em.close();
        if (emf != null) emf.close();
    }
}
```

## Conceptos Iniciales

### ¿Qué es JPA?

JPA (Java Persistence API) es una especificación de Java que permite interactuar con bases de datos relacionales usando objetos Java. Te permite mapear clases Java a tablas de una base de datos, simplificando operaciones como insertar, actualizar o consultar datos.

- **¿Qué necesitas para usar JPA?**
  - Una implementación como **Hibernate** o **EclipseLink.**
  - Configurar un archivo `persistence.xml` para definir la conexión a la base de datos.

### ¿Qué es un POJO?

Un POJO (Plain Old Java Object) es una clase Java sencilla que no depende de ningún framework específico ni extiende ninguna clase particular. El término fue acuñado para contrastar con las pesadas clases que requerían algunos frameworks empresariales.

#### Características principales

- **Simplicidad.** Son clases Java simples y ligeras.
- **Sin dependencias.** No dependen de bibliotecas externas.
- **Encapsulamiento.** Suelen seguir el principio de encapsulación con propiedades privadas y métodos getter/setter públicos.
- **Serializable.** A menudo implementan la interfaz `Serializable` para permitir su conversión a bytes.

#### Ejemplo de un POJO

```java
/**
 * Clase POJO que representa un estudiante.
 * Contiene solo propiedades, getters/setters y posiblemente un constructor.
 */
public class Estudiante {
    // Propiedades privadas
    private String nombre;
    private int edad;
    private String curso;
    
    // Constructor por defecto (no obligatorio pero común)
    public Estudiante() {
    }
    
    // Constructor parametrizado
    public Estudiante(String nombre, int edad, String curso) {
        this.nombre = nombre;
        this.edad = edad;
        this.curso = curso;
    }
    
    // Getters y setters
    public String getNombre() {
        return nombre;
    }
    
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    public int getEdad() {
        return edad;
    }
    
    public void setEdad(int edad) {
        this.edad = edad;
    }
    
    public String getCurso() {
        return curso;
    }
    
    public void setCurso(String curso) {
        this.curso = curso;
    }
}
```

En el contexto del examen, convertir la clase `Notificacio` a un POJO con mapeo JPA significa añadir las anotaciones JPA necesarias, pero manteniendo la estructura básica de un POJO con sus propiedades y métodos de acceso.

### Conceptos básicos de MongoDB

MongoDB es una base de datos NoSQL orientada a documentos que almacena datos en formato BSON (Binary JSON). A diferencia de las bases de datos relacionales, MongoDB no utiliza tablas y filas, sino colecciones y documentos.

**Elementos fundamentales:**

```
Base de datos → Colecciones → Documentos → Campos
```

#### 1. Shell de MongoDB

Es la interfaz de línea de comandos para interactuar con MongoDB. Las consultas se escriben en JavaScript.

```javascript
// Ejemplo de consulta básica
db.aspirantes.find()
```

#### 2. Método `find()`

Es el método principal para realizar consultas:

```javascript
// Sintaxis básica
db.coleccion.find(filtro, proyeccion)
```

- **filtro.** Condiciones que deben cumplir los documentos (equivalente al WHERE en SQL)
- **proyección.** Campos a incluir o excluir en el resultado

#### 3. Proyección de campos

```javascript
// Incluir solo ciertos campos (1 = incluir, 0 = excluir)
db.aspirantes.find(
    {}, // Sin filtro
    { nif: 1, nom: 1, llinatges: 1, _id: 0 } // Solo mostrar estos campos y ocultar _id
)
```

#### 4. Ordenación con `sort()`

```javascript
// Ordenar resultados (1 = ascendente, -1 = descendente)
db.aspirantes.find().sort({ llinatges: 1, nom: 1 })
```

### Consejos prácticos

1. **Comprobar la estructura.** Examina primero un documento para entender su estructura (con `db.aspirantes.findOne()`)

2. **Probar la consulta por partes.** Primero asegúrate de que el filtro funciona y luego añade proyección y ordenación

3. **Recuerda.** MongoDB es sensible a mayúsculas y minúsculas en nombres de campos

4. **Consultas anidadas.** Para consultar campos dentro de documentos anidados usa la notación de punto:

   ```javascript
   // Ejemplo (no necesario para el ejercicio)
   db.aspirantes.find({"localitat.illa.nomIlla": "Mallorca"})
   ```
