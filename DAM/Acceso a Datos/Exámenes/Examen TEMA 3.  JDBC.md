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

# **Examen TEMA 3.** <br>JDBC

### Examen Práctico - Nivel Básico
**Tiempo estimado.** 2 horas

**Instrucciones.** Implementa operaciones CRUD básicas con JDBC.

**Ejercicio.**
1. Crea una aplicación para gestionar una tabla de empleados con las siguientes funcionalidades:
   - Conectar a una base de datos H2 o PostgreSQL
   - Crear la tabla de empleados si no existe
   - Implementar operaciones CRUD (Crear, Leer, Actualizar, Eliminar)
   - Consultar empleados por departamento

2. Requisitos técnicos:
   - Utiliza PreparedStatement para todas las operaciones
   - Implementa manejo adecuado de recursos y excepciones
   - Documenta el código

3. Entrega:
   - Código fuente de la aplicación
   - Script SQL para crear la base de datos
   - Documentación de uso

### Examen Práctico - Nivel Avanzado
**Tiempo estimado.** 4 horas

**Instrucciones.** Desarrolla una aplicación de gestión de pedidos con transacciones.

**Ejercicio.**
1. Crea una aplicación para gestionar pedidos con las siguientes funcionalidades:
   - Gestionar productos, clientes y pedidos
   - Implementar transacciones para asegurar la integridad de los datos
   - Utilizar batch updates para operaciones masivas
   - Implementar consultas complejas con joins

2. Requisitos técnicos:
   - Utiliza transacciones para operaciones que afecten a múltiples tablas
   - Implementa batch updates para mejorar el rendimiento
   - Utiliza ResultSet para navegar por los resultados de consultas
   - Documenta el código

3. Entrega:
   - Código fuente de la aplicación
   - Script SQL para crear la base de datos
   - Documentación del diseño y uso