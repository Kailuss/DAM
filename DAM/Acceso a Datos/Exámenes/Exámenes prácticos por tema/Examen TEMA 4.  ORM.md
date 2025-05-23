---
tags:
  - DAM
  - AD
cssclasses:
  - dam-ad
  - table-clean
banner: "![[ad.jpg]]"
banner_y: 0.32
number headings: off
---

# **Examen TEMA 4.** <br>ORM

### Examen Práctico - Nivel Básico
**Tiempo estimado.** 2 horas

**Instrucciones.** Implementa un mapeo básico de entidades con JPA.

**Ejercicio.**
1. Crea una aplicación para gestionar una biblioteca con las siguientes entidades:
   - Libro (id, título, año, autor)
   - Autor (id, nombre, nacionalidad)
   - Implementa operaciones CRUD para ambas entidades
   - Consulta libros por autor

2. Requisitos técnicos:
   - Utiliza JPA con Hibernate
   - Define las entidades con anotaciones
   - Implementa una relación ManyToOne entre Libro y Autor
   - Documenta el código

3. Entrega:
   - Código fuente de la aplicación
   - Archivo de configuración persistence.xml
   - Documentación de uso

### Examen Práctico - Nivel Avanzado
**Tiempo estimado.** 4 horas

**Instrucciones.** Desarrolla una aplicación con relaciones complejas y consultas JPQL.

**Ejercicio.**
1. Crea una aplicación para gestionar un sistema educativo con las siguientes entidades:
   - Estudiante (id, nombre, email)
   - Curso (id, nombre, descripción)
   - Profesor (id, nombre, especialidad)
   - Implementa relaciones ManyToMany entre Estudiante y Curso
   - Implementa relación OneToMany entre Profesor y Curso
   - Implementa consultas JPQL complejas

2. Requisitos técnicos:
   - Utiliza JPA con Hibernate
   - Define las entidades con anotaciones
   - Implementa consultas JPQL parametrizadas
   - Gestiona adecuadamente el ciclo de vida de las entidades
   - Documenta el código

3. Entrega:
   - Código fuente de la aplicación
   - Archivo de configuración persistence.xml
   - Documentación del diseño y uso

## TEMA 5: ORDB con PostgreSQL

### Examen Práctico - Nivel Básico
**Tiempo estimado.** 2 horas

**Instrucciones.** Implementa tipos compuestos y consultas básicas en PostgreSQL.

**Ejercicio.**
1. Crea una aplicación para gestionar direcciones y personas con las siguientes funcionalidades:
   - Definir un tipo compuesto para Dirección
   - Crear una tabla Persona que utilice el tipo Dirección
   - Implementar operaciones CRUD
   - Consultar personas por ciudad

2. Requisitos técnicos:
   - Utiliza PostgreSQL y JDBC
   - Crea scripts SQL para definir tipos y tablas
   - Mapea el tipo compuesto a una clase Java
   - Documenta el código

3. Entrega:
   - Código fuente de la aplicación
   - Scripts SQL
   - Documentación de uso

### Examen Práctico - Nivel Avanzado
**Tiempo estimado.** 4 horas

**Instrucciones.** Desarrolla una aplicación con herencia de tablas y tipos complejos.

**Ejercicio.**
1. Crea una aplicación para gestionar un sistema de ventas con las siguientes funcionalidades:
   - Implementar herencia de tablas para diferentes tipos de productos
   - Utilizar arrays y tipos compuestos para características de productos
   - Implementar consultas avanzadas con funciones específicas de PostgreSQL
   - Gestionar transacciones complejas

2. Requisitos técnicos:
   - Utiliza PostgreSQL y JDBC
   - Crea scripts SQL para definir la estructura
   - Mapea tipos complejos a clases Java
   - Implementa procedimientos almacenados
   - Documenta el código

3. Entrega:
   - Código fuente de la aplicación
   - Scripts SQL
   - Documentación del diseño y uso

## TEMA 6: MongoDB y JSON

### Examen Práctico - Nivel Básico
**Tiempo estimado.** 2 horas

**Instrucciones.** Implementa operaciones básicas con JSON y MongoDB.

**Ejercicio.**
1. Crea una aplicación para gestionar una colección de películas con las siguientes funcionalidades:
   - Convertir objetos Java a JSON y viceversa usando Jackson
   - Conectar a MongoDB
   - Implementar operaciones CRUD básicas
   - Consultar películas por género y director

2. Requisitos técnicos:
   - Utiliza la biblioteca Jackson para manipulación de JSON
   - Utiliza el driver de MongoDB para Java
   - Implementa manejo adecuado de excepciones
   - Documenta el código

3. Entrega:
   - Código fuente de la aplicación
   - Ejemplos de documentos JSON
   - Documentación de uso

### Examen Práctico - Nivel Avanzado
**Tiempo estimado.** 4 horas

**Instrucciones.** Desarrolla una aplicación con operaciones avanzadas en MongoDB.

**Ejercicio.**
1. Crea una aplicación para gestionar un blog con las siguientes funcionalidades:
   - Gestionar usuarios, artículos y comentarios
   - Implementar operaciones CRUD para todas las entidades
   - Utilizar referencias entre documentos
   - Implementar agregaciones para estadísticas
   - Utilizar índices para optimizar consultas

2. Requisitos técnicos:
   - Utiliza el driver de MongoDB para Java
   - Implementa mapeo de documentos a clases POJO
   - Utiliza operaciones de agregación
   - Implementa paginación de resultados
   - Documenta el código

3. Entrega:
   - Código fuente de la aplicación
   - Ejemplos de documentos JSON
   - Documentación del diseño y uso
