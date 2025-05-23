---
tags: [AD, DAM]
cssclasses: [dam-ad, table-compact-clean]
banner: "![[ad.jpg]]"
banner_y: 0.32
---

# **Ejercicios TEMA 5.** <br>ORDB

## 1. Instrucciones

- **Opciones para realizar los ejercicios:**
  1. Servidor del instituto (consultar [Instrucciones del servidor PostgreSQL](https://fpadistancia.caib.es/mod/page/view.php?id=77493))
  2. Instalación local en máquina propia o virtual

- **Herramientas recomendadas:**  
  `PgAdmin` o cliente similar para gestión de bases de datos

- **Requisito de entrega:**  
  Guardar todas las instrucciones en un **script SQL**

## 2. Ejercicios con base de datos

### 2.1. **DDL (Data Definition Language)**
1. **Esquema:** Crear un schema para los ejercicios
2. **Tipo compuesto:** Definir tipo para datos de contacto (teléfono, email, twitter)
3. **Tabla Alumnos:**  
   - Campos: NIF (PK), nombre, apellidos, contacto  
   - Campo adicional: indicador de baja
4. **Tabla Ciclos:**  
   - Campos: código (PK), nombre
5. **Tabla Asignaturas:**  
   - Campos: código (PK), nombre, código_ciclo (FK)
6. **Tabla Matrícula:**  
   - Relación N:M entre Alumnos y Asignaturas  
   - Array para almacenar notas (enteras)

### 2.2. **DML (Data Manipulation Language)**
1. **Inserción de datos:**  
   - 2 alumnos  
   - 2 asignaturas  
   - Notas asociadas

1. **Consultas requeridas:**
   - Listado completo de alumnos  
   - Asignaturas por ciclo  
   - Alumnos por ciclo  
   - Notas de alumno en asignatura  
   - Añadir nota a alumno  
   - Alumnos con notas <5 en asignatura  
   - Búsqueda de alumno por email  
   - Alumnos sin twitter  
   - Actualización de teléfono

## 3. Base de datos de peajes (ezPass)

### 3.1. **Diagrama de base de datos**

![](../../../_Media/Imágenes/AD/Pasted%20image%2020250223174324.png)

### 3.2. **Instrucciones técnicas**
1. **Configuración de proyecto:**  
   - IDE con Hibernate + Driver MySQL  
   - Estructura por paquetes  
   - Clase main para pruebas (sin acceso directo a BD)

2. **Conexión JPA:**  
   - Host: `davv.paucasesnovescifp.cat`  
   - Puerto: `3306`  
   - BD: `peatges`  
   - Credenciales: usuari/seCret_24  

> [!warning] **Importante:**  
> La BD se reinicia diariamente a las 3:00 AM.  
> Los cambios no persisten al día siguiente.

## 4. Ejercicios prácticos

### 4.1. **Gestión de conexiones (2p)**
- **Clase especializada** con:  
  - Atributo para unidad de persistencia (no null)  
  - Métodos para abrir/cerrar `EntityManager`  
  - Control de errores con excepción propia  

### 4.2. **Entidad Peatge (4p)**
#### 4.2.1. Mapeo (2p)
- Entidad `Peatge` ↔ Tabla `TOLLS`  
- Validación: campos obligatorios con longitud máxima  
- Excepción propia para errores  

#### 4.2.2. Operaciones (2p)
- Búsqueda por ID (controlar null)  
- Listado ordenado (NamedQuery)  

### 4.3. **Relación con Viajes (4p)**
#### 4.3.1. Consulta sin queries (2p)
- Método que filtra viajes por:  
  - Peaje inicio (boolean=true)  
  - Peaje final (boolean=false)  

#### 4.3.2. Consulta JPQL (2p)
- Viajes con mismo peaje inicio/final  
- Implementación con JPQL  

## 5. Entrega
- **Archivo ZIP** con proyecto completo  
- **JAR** ejecutable  

## 6. Criterios de evaluación
- **Ponderación:** 8.33% nota final  
- **Penalizaciones:**  
  - Hasta 10% por errores de formato/nomenclatura  
  - Detalles por ejercicio en enunciado  

---

Aquí está la integración del enunciado con las soluciones SQL generadas anteriormente, organizado en un formato claro y profesional:

---

# **Ejercicios AD05.**  <br>Solución Integrada

## 1. Parte 1: Estructura de Base de Datos Educativa

### 1.1. **Esquema y Tipo de Contacto** <br>(Corresponde a Ejercicios 1.1-1.2 del SQL)

```sql
CREATE SCHEMA institut AUTHORIZATION professor;

CREATE TYPE institut.dades_contacte AS (
    telefon VARCHAR(12),
    email VARCHAR(75),
    twitter VARCHAR(50)
);
```

### 1.2. **Tablas Principales** <br>(Ejercicios 1.3-1.6)

```sql
-- Tabla Alumnos (con campo de baja)
CREATE TABLE institut."Alumnes" (
    nif VARCHAR(9) PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    llinatges VARCHAR(50) NOT NULL,
    contacte institut.dades_contacte,
    baixa BOOLEAN DEFAULT FALSE
);

-- Tabla Ciclos
CREATE TABLE institut."Cicles" (
    codi VARCHAR(3) PRIMARY KEY,
    nom VARCHAR(100) NOT NULL
);

-- Tabla Asignaturas
CREATE TABLE institut."Assignatures" (
    codi VARCHAR(5) PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    cicle VARCHAR(3) NOT NULL REFERENCES institut."Cicles"(codi)
);

-- Tabla Matrícula con array de notas
CREATE TABLE institut."Matricula" (
    nif VARCHAR(9) REFERENCES institut."Alumnes"(nif),
    assignatura VARCHAR(5) REFERENCES institut."Assignatures"(codi),
    notes INTEGER[],
    PRIMARY KEY (nif, assignatura)
);
```

## 2. Parte 2: Operaciones de Datos

### 2.1. **Inserciones** <br>(Ejercicio 2 del SQL)

```sql
-- Ciclo formativo
INSERT INTO institut."Cicles" VALUES 
('DAM', 'Desenvolupament Aplicacions Multiplataforma');

-- Asignaturas
INSERT INTO institut."Assignatures" VALUES 
('SPPRO', 'Programació', 'DAM'),
('SPBDD', 'Bases de Dades', 'DAM');

-- Alumnos
INSERT INTO institut."Alumnes" VALUES 
('12345678A', 'Anna', 'García', ROW('600111222', 'anna@mail.com', '@annag'), false),
('87654321B', 'Pere', 'Martí', ROW('611222333', 'pere@mail.com', NULL), false);

-- Matrículas
INSERT INTO institut."Matricula" VALUES 
('12345678A', 'SPPRO', ARRAY[7, 8, 6]),
('87654321B', 'SPBDD', ARRAY[5, 4, 9]);
```

### 2.2. **Consultas** <br>(Ejercicios 3.1-3.9)

| Requisito del Enunciado | Consulta SQL |
|-------------------------|-------------|
| 3.1. Todos los alumnos | `SELECT * FROM institut."Alumnes";` |
| 3.2. Asignaturas por ciclo | `SELECT * FROM institut."Assignatures" WHERE cicle = 'DAM';` |
| 3.3. Alumnos por ciclo | ```sql<br>SELECT a.* FROM institut."Alumnes" a<br>JOIN institut."Matricula" m ON a.nif = m.nif<br>JOIN institut."Assignatures" asig ON m.assignatura = asig.codi<br>WHERE asig.cicle = 'DAM';``` |
| 3.4. Notas de alumno | `SELECT notes FROM institut."Matricula" WHERE nif = '12345678A' AND assignatura = 'SPPRO';` |
| 3.5. Añadir nota | ```sql<br>UPDATE institut."Matricula"<br>SET notes = array_append(notes, 7)<br>WHERE nif = '12345678A' AND assignatura = 'SPPRO';``` |
| 3.6. Alumnos con nota <5 | ```sql<br>SELECT a.* FROM institut."Alumnes" a<br>JOIN institut."Matricula" m ON a.nif = m.nif<br>WHERE 5 > ANY(m.notes) AND m.assignatura = 'SPBDD';``` |
| 3.7. Buscar por email | `SELECT * FROM institut."Alumnes" WHERE (contacte).email = 'anna@mail.com';` |
| 3.8. Sin twitter | `SELECT * FROM institut."Alumnes" WHERE (contacte).twitter IS NULL;` |
| 3.9. Actualizar teléfono | ```sql<br>UPDATE institut."Alumnes"<br>SET contacte.telefon = '622333444'<br>WHERE nif = '87654321B';``` |

## 3. Parte 3: Sistema de Peajes (JPA/Hibernate)

### 3.1. **Clase de Gestión** <br>(Ejercicio 4.1)

```java
public class GestorPersistencia {
    private final String unidadPersistencia;
    
    public GestorPersistencia(String unidad) {
        this.unidadPersistencia = Objects.requireNonNull(unidad);
    }
    
    public EntityManager getEntityManager() throws PersistenciaException {
        try {
            EntityManagerFactory emf = Persistence.createEntityManagerFactory(unidadPersistencia);
            return emf.createEntityManager();
        } catch (Exception e) {
            throw new PersistenciaException("Error al crear EntityManager", e);
        }
    }
    
    public void cerrarRecursos(EntityManager em) {
        if (em != null && em.isOpen()) {
            em.close();
        }
    }
}
```

### 3.2. **Entidad Peatge** <br>(Ejercicio 4.2)

```java
@Entity
@Table(name = "TOLLS")
@NamedQuery(
    name = "Peatge.findAllOrdered",
    query = "SELECT p FROM Peatge p ORDER BY p.nombre"
)
public class Peatge {
    @Id
    @Column(name = "toll", length = 5, nullable = false)
    private String id;
    
    @Column(name = "name", length = 50, nullable = false)
    private String nombre;
    
    // Relaciones con Trip (Ejercicio 4.3)
    @OneToMany(mappedBy = "peajeInicio")
    private List<Trip> viajesInicio;
    
    @OneToMany(mappedBy = "peajeFin")
    private List<Trip> viajesFin;
    
    // Getters y setters
}
```