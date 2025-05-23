# 10 Exámenes Prácticos Integrales

## Examen 1: Sistema de Gestión de Biblioteca

**Tiempo estimado**: 2-3 horas

**Descripción**: Desarrollar una aplicación para gestionar los préstamos de libros en una biblioteca.

**Requisitos**:

1. Crear una base de datos con las siguientes tablas:
   - Libros (id, título, autor, año, disponible)
   - Usuarios (id, nombre, email, teléfono)
   - Préstamos (id, libro_id, usuario_id, fecha_préstamo, fecha_devolución)

2. Implementar las siguientes funcionalidades:
   - Registrar nuevos libros y usuarios
   - Realizar préstamos y devoluciones
   - Consultar disponibilidad de libros
   - Listar préstamos activos por usuario
   - Guardar un registro de operaciones en un archivo de texto

3. Requisitos técnicos:
   - Utilizar JDBC para la conexión a la base de datos
   - Implementar transacciones para las operaciones de préstamo/devolución
   - Utilizar PreparedStatement para todas las consultas
   - Implementar manejo de excepciones personalizado
   - Utilizar flujos con buffer para el registro de operaciones

**Entregables**:
- Código fuente completo
- Script SQL para crear la base de datos
- Archivo README con instrucciones de uso

## Examen 2: Conversor de Datos JSON-XML

**Tiempo estimado**: 2-3 horas

**Descripción**: Desarrollar una aplicación que permita convertir datos entre formatos JSON y XML, con persistencia en base de datos.

**Requisitos**:

1. Implementar las siguientes funcionalidades:
   - Cargar datos desde archivos JSON o XML
   - Convertir datos de JSON a XML y viceversa
   - Almacenar los datos convertidos en una base de datos relacional
   - Recuperar datos de la base de datos y exportarlos en el formato deseado
   - Mantener un historial de conversiones realizadas

2. Requisitos técnicos:
   - Utilizar Jackson para el procesamiento de JSON
   - Utilizar JAXB o similar para el procesamiento de XML
   - Implementar un modelo de datos con al menos 3 clases relacionadas
   - Utilizar JDBC para la persistencia en base de datos
   - Implementar manejo de archivos con Path y Files
   - Utilizar flujos para la lectura/escritura de archivos

**Entregables**:
- Código fuente completo
- Ejemplos de archivos JSON y XML para pruebas
- Documentación de la API desarrollada

## Examen 3: Sistema de Inventario con MongoDB

**Tiempo estimado**: 2-3 horas

**Descripción**: Desarrollar una aplicación de gestión de inventario utilizando MongoDB como base de datos.

**Requisitos**:

1. Implementar las siguientes funcionalidades:
   - Registrar productos con categorías, precios y stock
   - Registrar proveedores y asociarlos a productos
   - Realizar movimientos de inventario (entradas/salidas)
   - Generar informes de stock por categoría
   - Buscar productos por diferentes criterios
   - Exportar datos de inventario a JSON

2. Requisitos técnicos:
   - Utilizar el driver de MongoDB para Java
   - Implementar mapeo de documentos a clases POJO
   - Utilizar agregaciones para los informes
   - Implementar índices para optimizar consultas
   - Utilizar Jackson para la exportación a JSON
   - Implementar manejo de excepciones personalizado

**Entregables**:
- Código fuente completo
- Documentación de la estructura de datos en MongoDB
- Manual de usuario básico

## Examen 4: Aplicación de Gestión de Pedidos con ORM

**Tiempo estimado**: 2-3 horas

**Descripción**: Desarrollar una aplicación para gestionar pedidos de una tienda online utilizando JPA/Hibernate.

**Requisitos**:

1. Implementar las siguientes entidades:
   - Cliente (id, nombre, email, dirección)
   - Producto (id, nombre, descripción, precio, stock)
   - Pedido (id, cliente, fecha, estado)
   - DetallePedido (id, pedido, producto, cantidad, precio_unitario)

2. Implementar las siguientes funcionalidades:
   - Gestión CRUD de clientes y productos
   - Crear pedidos con múltiples productos
   - Actualizar estado de pedidos (pendiente, enviado, entregado)
   - Consultar pedidos por cliente y estado
   - Generar informes de ventas por producto

3. Requisitos técnicos:
   - Utilizar JPA/Hibernate para el mapeo objeto-relacional
   - Implementar relaciones OneToMany y ManyToOne
   - Utilizar JPQL para consultas complejas
   - Implementar transacciones para las operaciones de pedido
   - Serializar pedidos completados a archivos JSON

**Entregables**:
- Código fuente completo
- Archivo persistence.xml configurado
- Documentación de las entidades y relaciones

## Examen 5: Sistema de Gestión Documental

**Tiempo estimado**: 2-3 horas

**Descripción**: Desarrollar una aplicación para gestionar documentos digitales con metadatos y categorización.

**Requisitos**:

1. Implementar las siguientes funcionalidades:
   - Almacenar documentos en el sistema de archivos
   - Registrar metadatos de documentos en base de datos
   - Categorizar documentos por tipo y etiquetas
   - Buscar documentos por diferentes criterios
   - Exportar metadatos a formato JSON
   - Generar un registro de actividad

2. Requisitos técnicos:
   - Utilizar Path y Files para la gestión de archivos
   - Implementar JDBC para la persistencia de metadatos
   - Utilizar flujos para la copia y movimiento de documentos
   - Implementar transacciones para operaciones que afecten a múltiples tablas
   - Utilizar Jackson para la exportación de metadatos
   - Implementar un sistema de logging con flujos de caracteres

**Entregables**:
- Código fuente completo
- Script SQL para crear la base de datos
- Documentación de la estructura de directorios y archivos

## Examen 6: Aplicación de Análisis de Datos con PostgreSQL ORDB

**Tiempo estimado**: 2-3 horas

**Descripción**: Desarrollar una aplicación para analizar datos de ventas utilizando características objeto-relacionales de PostgreSQL.

**Requisitos**:

1. Implementar las siguientes estructuras:
   - Tipo compuesto para Dirección (calle, ciudad, código postal)
   - Tipo compuesto para Contacto (nombre, teléfono, email)
   - Tabla Cliente con campos de tipos compuestos
   - Tabla Venta con array de productos vendidos
   - Herencia de tablas para diferentes tipos de clientes (particular, empresa)

2. Implementar las siguientes funcionalidades:
   - Registrar clientes y ventas
   - Consultar ventas por cliente y período
   - Analizar productos más vendidos
   - Exportar resultados a archivos CSV
   - Importar datos desde archivos JSON

3. Requisitos técnicos:
   - Utilizar JDBC para conectar con PostgreSQL
   - Implementar mapeo de tipos compuestos a clases Java
   - Utilizar PreparedStatement para consultas parametrizadas
   - Implementar manejo de arrays en PostgreSQL
   - Utilizar flujos para la exportación/importación de datos

**Entregables**:
- Código fuente completo
- Scripts SQL para crear tipos y tablas
- Documentación del modelo de datos

## Examen 7: Sistema de Gestión de Contenido Multimedia

**Tiempo estimado**: 2-3 horas

**Descripción**: Desarrollar una aplicación para gestionar contenido multimedia (imágenes, audio, video) con metadatos y categorización.

**Requisitos**:

1. Implementar las siguientes funcionalidades:
   - Importar archivos multimedia al sistema
   - Extraer y almacenar metadatos básicos (tamaño, formato, duración)
   - Categorizar contenido por tipo y etiquetas
   - Buscar contenido por diferentes criterios
   - Generar miniaturas para imágenes
   - Exportar catálogo en formato JSON

2. Requisitos técnicos:
   - Utilizar Path y Files para la gestión de archivos
   - Implementar serialización de objetos para metadatos complejos
   - Utilizar flujos de bytes para la manipulación de archivos binarios
   - Implementar una base de datos embebida (H2) para metadatos
   - Utilizar JDBC para la persistencia
   - Implementar Jackson para la exportación de catálogos

**Entregables**:
- Código fuente completo
- Documentación de la estructura de datos
- Manual de usuario básico

## Examen 8: Aplicación de Sincronización de Datos

**Tiempo estimado**: 2-3 horas

**Descripción**: Desarrollar una aplicación que sincronice datos entre una base de datos relacional y MongoDB.

**Requisitos**:

1. Implementar las siguientes funcionalidades:
   - Definir un modelo de datos común para ambas bases de datos
   - Leer datos de la base de datos relacional
   - Convertir y almacenar datos en MongoDB
   - Sincronizar cambios en ambas direcciones
   - Resolver conflictos de sincronización
   - Generar informes de sincronización

2. Requisitos técnicos:
   - Utilizar JDBC para la base de datos relacional
   - Implementar el driver de MongoDB para Java
   - Utilizar Jackson para la conversión de datos
   - Implementar transacciones para garantizar consistencia
   - Utilizar flujos para los informes de sincronización
   - Implementar manejo de excepciones personalizado

**Entregables**:
- Código fuente completo
- Scripts para crear la base de datos relacional
- Documentación del proceso de sincronización

## Examen 9: Sistema de Reservas con JPA y REST

**Tiempo estimado**: 2-3 horas

**Descripción**: Desarrollar una aplicación para gestionar reservas de recursos (salas, equipos, vehículos) con persistencia JPA y exportación REST.

**Requisitos**:

1. Implementar las siguientes entidades:
   - Recurso (id, nombre, tipo, disponible)
   - Usuario (id, nombre, email, departamento)
   - Reserva (id, recurso, usuario, fecha_inicio, fecha_fin, estado)

2. Implementar las siguientes funcionalidades:
   - Gestión CRUD de recursos y usuarios
   - Realizar y cancelar reservas
   - Verificar disponibilidad de recursos
   - Consultar reservas por usuario, recurso y período
   - Exportar datos de reservas en formato JSON para API REST

3. Requisitos técnicos:
   - Utilizar JPA/Hibernate para el mapeo objeto-relacional
   - Implementar relaciones entre entidades
   - Utilizar JPQL para consultas complejas
   - Implementar transacciones para las operaciones de reserva
   - Utilizar Jackson para la serialización a JSON
   - Implementar validación de reglas de negocio

**Entregables**:
- Código fuente completo
- Archivo persistence.xml configurado
- Documentación de la API REST

## Examen 10: Aplicación de ETL (Extract, Transform, Load)

**Tiempo estimado**: 2-3 horas

**Descripción**: Desarrollar una aplicación ETL que extraiga datos de diferentes fuentes, los transforme y los cargue en un destino unificado.

**Requisitos**:

1. Implementar las siguientes funcionalidades:
   - Extraer datos de archivos CSV, JSON y una base de datos relacional
   - Transformar y normalizar los datos según un esquema común
   - Cargar los datos en una base de datos MongoDB
   - Validar la integridad de los datos durante el proceso
   - Generar informes de procesamiento
   - Programar ejecuciones periódicas

2. Requisitos técnicos:
   - Utilizar flujos para la lectura de archivos
   - Implementar JDBC para la extracción de datos relacionales
   - Utilizar Jackson para el procesamiento de JSON
   - Implementar el driver de MongoDB para la carga de datos
   - Utilizar transacciones donde sea aplicable
   - Implementar manejo de errores y recuperación

**Entregables**:
- Código fuente completo
- Ejemplos de archivos de entrada
- Documentación del proceso ETL
- Informe de pruebas con diferentes conjuntos de datos
