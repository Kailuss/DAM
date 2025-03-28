---
number headings: max 3, _.1.1., skip ^sk
tags:
  - DAM
  - SGE
banner: "![[sge.jpg]]"
cssclasses:
  - dam-sge
  - table-compact-clean
---

# **Resumen Tema 3.**  <br>Organización, consulta y tratamiento de la información

Este tema aborda cómo se organiza, consulta y trata la información en sistemas ERP (Enterprise Resource Planning), con un enfoque en OpenERP. A continuación, se presenta un resumen estructurado pero con explicaciones breves para facilitar la comprensión.

## 1. Organización y Consulta de la Información
- **Objetos en OpenERP.** Los datos se acceden a través de objetos, como `res.partner` para colaboradores o `account.invoice` para facturas. Cada objeto tiene un prefijo que indica su módulo.
  - *Ejemplo*: Para enviar un correo a los colaboradores 1 y 5, se usaría `res.partner.send_email(..., [1,5], ...)`.
  
- **Tablas y Vistas.** Las tablas almacenan datos en filas y columnas, mientras que las vistas son "tablas virtuales" que muestran un subconjunto de datos. 
  - *Herramientas*: Se pueden usar herramientas como **pgAdmin III** para gestionar bases de datos PostgreSQL.

- **Consultas de Acceso a Datos.** Permiten extraer información de tablas y vistas. Se pueden crear manualmente con SQL o mediante asistentes gráficos.
  - *Pasos*: Seleccionar tablas, establecer relaciones, elegir campos y ejecutar la consulta.

## 2. Visualización de la Información
- **Interfaces.** Los datos se muestran a través de interfaces, que pueden ser estáticas (no modificables) o dinámicas (modificables por el usuario, generalmente en XML).
  - *Ejemplo*: Un formulario XML en OpenERP para mostrar datos de colaboradores.

- **Tipos de Interfaces.**
  - **Formularios.** Muestran un solo registro.
  - **Árboles.** Muestran varios registros en formato de lista.
  - **Gráficos.** Presentan datos de manera visual para facilitar su comprensión.

- **Campos y Diseño.** Los campos son la información que se muestra en pantalla. Se pueden personalizar con elementos como separadores, pestañas, y campos de solo lectura o invisibles.

- **Menús.** Permiten acceder a los objetos. Se pueden asociar a acciones como abrir ventanas, imprimir informes o ejecutar asistentes.

- **Búsqueda de Información.** Los motores de búsqueda deben ser rápidos y efectivos, con opciones de búsqueda básica y avanzada.

- **Informes y Listados.** Mejoran la visualización de datos, como informes contables, albaranes, o etiquetas. Pueden adaptarse a la imagen corporativa de la empresa.

## 3. Tratamiento de la Información
- **Procesos Clave.** Incluyen contabilidad, operaciones de compra y venta, trazabilidad de productos, y producción.
  - *Ejemplo*: Para gestionar la contabilidad, se deben configurar cuentas contables, bancos, y diarios de compras y ventas.

- **Asistentes.** Facilitan tareas específicas, como la creación de cuentas contables o el envío de correos electrónicos. Suelen seguir un formato de "Siguiente, Siguiente, Aceptar".

- **Procedimientos Almacenados.** Son funciones que se ejecutan automáticamente en respuesta a eventos, como enviar un correo cuando un cliente realiza un pedido.
  - *Ejemplo en PostgreSQL*: Un procedimiento para seleccionar empresas de tipo "Sociedad Limitada".

## 4. Extracción de Datos en Sistemas ERP-CRM y Almacenes de Datos
- **Extracción de Datos.** Consiste en sacar información de una aplicación para procesarla en otra. Se puede hacer mediante consultas SQL, informes, o herramientas de Business Intelligence (BI).
  - *Herramientas*: Hojas de cálculo, almacenes de datos, y cubos multidimensionales.

- **Importación y Exportación.** Se utilizan formatos como CSV para mover datos entre sistemas. La importación permite introducir datos masivamente, mientras que la exportación extrae datos para su manipulación externa.

## 5. Evaluación del Rendimiento y Auditorías de Acceso a los Datos
- **Monitorización del Rendimiento.** Herramientas como **sar** en Linux permiten evaluar el uso del procesador, memoria, y discos.
  - *Ejemplo*: `sar 1 3` muestra el uso del procesador cada segundo durante 3 segundos.

- **Auditorías de Acceso.** Los logs registran la actividad del sistema, como accesos, errores, y comandos ejecutados. Son esenciales para identificar y resolver incidencias.
  - *Ejemplo*: En OpenERP, los logs se encuentran en `/var/log/openerp-server.log`.

- **Incidencias.** Los logs ayudan a identificar problemas, como intentos fallidos de inicio de sesión o errores en la ejecución de procesos.
