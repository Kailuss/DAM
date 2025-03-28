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

# **TEMA 3.** <br>Organización, consulta y <br>tratamiento de la información

| Anexos |
| - |
| [Resumen Tema 3](Resúmenes/Resumen%20Tema%203%20SGE.md) |
| [Tarea SGE03 y SGE04](../Práctica/Tareas/Tarea%20SGE03%20y%20SGE04.md) |

## 1. Organización y consulta de la información

Hemos explorado las funcionalidades básicas de dos ERPs ampliamente utilizados. A partir de ahora, nos centraremos en OpenERP. Esto se debe a su módulo base más sencillo, compuesto por Empresas y Administración.

La base de datos de un ERP es extensa. Almacena tablas, vistas, funciones y disparadores que operan sobre los datos. Para manejar esta gran cantidad de información, es esencial establecer normativas de organización. Por ejemplo, el uso de prefijos para identificar módulos o definir campos obligatorios en las tablas. Esto garantiza el correcto funcionamiento de la aplicación.

En sistemas orientados a objetos, los datos se acceden a través de objetos. Por ejemplo, en OpenERP, `res.partner` se usa para acceder a datos de colaboradores. `account.invoice` se usa para facturas. Cada objeto tiene un prefijo que indica su módulo. Los métodos que actúan sobre estos objetos requieren un parámetro. Este especifica el recurso o registro afectado. Por ejemplo, para enviar un correo a los colaboradores 1 y 5 en `res.partner`, se usaría: `res.partner.send_email(..., [1,5], ...)`.

En resumen, un objeto es cualquier elemento de la aplicación. Permite acceder a sus datos.

### 1.1. **Tablas y vistas de la base de datos**

Un objeto en OpenERP contiene todos los elementos de la aplicación. Estos incluyen tablas, disparadores, formularios, informes y ventanas. Para acceder a estos objetos, se utiliza la opción **Administración/Estructura de la base de datos/Objetos.** En Openbravo, los metadatos se gestionan en el módulo **Diccionario de Datos.** Este centraliza formularios, informes, procesos, tablas y campos.

Para acceder al cliente web de OpenERP, se debe usar la dirección IP del servidor. Esta se configura en `openerp-web.conf` y se ejecuta el script `openerp-web.py`. Si la IP del servidor cambia, es necesario actualizarla en el archivo de configuración.

Las tablas son estructuras de datos organizadas en filas (registros) y columnas (campos). Por ejemplo, en OpenSQL, la tabla `res.users` almacena datos de usuarios. Estos incluyen nombre, login y contraseña. Cuando la base de datos es demasiado compleja, se utilizan vistas. Estas son "tablas virtuales" que muestran un subconjunto de datos. Las vistas tienen la misma estructura que las tablas. Se accede a ellas mediante consultas.

Para administrar la base de datos, se pueden usar herramientas gráficas como **pgAdmin III** para PostgreSQL. Al conectarse, se deben proporcionar datos como el nombre de la conexión, la dirección IP del servidor, el puerto (normalmente 5432), la base de datos inicial (`postgres`), el nombre de usuario (`userbd`) y la contraseña.

### 1.2. **Consultas de acceso a datos**

Las consultas de acceso a datos permiten extraer información de tablas y vistas. Estas consultas devuelven un conjunto de registros basado en los criterios especificados. Los pasos para crear una consulta son:

1. Seleccionar las tablas o vistas sobre las que actuará la consulta.
2. Establecer relaciones entre tablas y vistas si la aplicación no las proporciona.
3. Seleccionar los campos a mostrar.
4. Ejecutar la consulta.

Las consultas pueden actuar sobre una o varias tablas o vistas. Pueden guardarse para su uso posterior. Se pueden construir escribiendo código en un lenguaje como SQL. También mediante asistentes gráficos para consultas menos complejas.

## 2. Visualización de la información

Los datos almacenados en objetos se muestran al usuario a través de interfaces. Cada objeto tiene su propia interfaz. Esta varía según el tipo de información que se presenta. Por ejemplo, los datos de empresas no se muestran de la misma manera que los de facturas. Las interfaces pueden ser:

- **Estáticas.** Se crean dentro del código de la aplicación y no pueden modificarse.
- **Dinámicas.** Pueden ser modificadas por el usuario. Su descripción se almacena en un lenguaje de descripción de datos como XML.

Las interfaces dinámicas se construyen a partir de la descripción XML de la pantalla del cliente. No es necesario ser experto en XML. Muchas aplicaciones permiten crear estas descripciones de manera gráfica. Por ejemplo, en OpenERP, una interfaz para introducir y consultar datos de colaboradores se define así:

```xml
<?xml version="1.0" encoding="utf-8"?>
<form string="Partner">
	<field name="name"/>
	<field name="title"/>
	<field name="ref"/>
	<field name="lang"/>
	<field name="customer"/>
	<field name="supplier"/>
</form>
```

Este código define una interfaz con seis campos: nombre, título, código, idioma, y dos campos booleanos. Estos indican si es cliente o proveedor.

### 2.1. **Interfaces de entrada de datos y de procesos. Formularios y Gráficos**

Se pueden definir una o varias interfaces para cada objeto. Estas describen qué campos se muestran y cómo se distribuyen. Los tipos de interfaces más comunes son:

- **Formularios.** Muestran un solo registro. Los campos se distribuyen de izquierda a derecha y de arriba abajo.
- **Árboles.** Muestran varios registros en modo lista. Útil para búsquedas y visualización de múltiples registros.
- **Gráficos.** Presentan datos en formatos visuales para una mejor comprensión.

En OpenERP, las interfaces se pueden personalizar de dos maneras:

1. **Escribiendo código XML.** Desde el menú **Administración/Personalización/Interfaz de usuario/Vistas.**
2. **Mediante el cliente web.** Usando el **Administrador de Vistas**, accesible desde **Personalizar/Gestionar Vistas.**

Una vez modificada la vista, basta con cerrar y reabrir la pestaña para ver los cambios.

### 2.2. **Definición de campos**

Los objetos están formados por campos. Estos son la información que se muestra en pantalla. Por ejemplo, una vista de tipo formulario con dos campos (nombre y título) se define así:

```xml
<?xml version="1.0"?> 
<form string="Empresa">
     <field name="name"/>
     <field name="title"/>
</form> 
```

Los campos se distribuyen en el orden en que se declaran en el archivo XML. Un tipo especial de campo es el **one2many.** Este refleja una relación de uno a muchos entre dos objetos. Por ejemplo, el campo `address` en `res.partner` está enlazado con `res.partner.address`. Esto significa que una empresa puede tener muchas direcciones.

Además de los campos, existen elementos de diseño como:

- **separator.** Agrega una línea de separación.
- **notebook.** Distribuye los campos en pestañas.
- **colspan.** Extiende un campo a través de varias columnas.
- **readonly.** Establece un campo como solo lectura.
- **invisible.** Oculta el campo y su etiqueta.
- **password.** Reemplaza la entrada con símbolos "•".

### 2.3. **Menús**

Para acceder a los objetos, es necesario definir menús y las acciones asociadas. Los menús se pueden editar seleccionando uno y haciendo clic en **Cambiar.** Para crear un menú secundario, se indica cuál es el menú padre del que depende.

Las acciones asociadas a los menús pueden ser:

- **Window.** Abre una vista en una nueva ventana.
- **Report.** Imprime un informe.
- **Wizard.** Ejecuta un asistente para realizar un proceso.

Al crear un menú, se debe especificar el tipo de acción asociada. Por ejemplo, para una acción que abre una vista, se deben introducir datos como el nombre de la acción, el tipo (`ir.actions.act_window`), y los detalles de la vista.

### 2.4. **Búsqueda de información**

La búsqueda de información es un aspecto crucial en las aplicaciones ERP. Los motores de búsqueda deben ser rápidos y efectivos. Normalmente, se incluyen:

- **Búsquedas básicas.** Sobre campos principales.
- **Búsquedas avanzadas.** Para campos más específicos.

En OpenERP, los criterios de búsqueda se introducen en la parte superior de la ventana. Los resultados se muestran en una vista de tipo árbol. También se pueden aplicar filtros para reducir los registros mostrados.

### 2.5. **Informes y listados de la aplicación**

Los informes y listados son una forma de mejorar la visualización de los datos. Algunos ejemplos incluyen:

- Informes contables.
- Albaranes y pedidos.
- Recibos y reclamaciones.
- Informes estadísticos.
- Generación de etiquetas.
- Informes de agrupamiento.

Estos informes pueden utilizarse tal como se proporcionan. También pueden adaptarse a la imagen corporativa de la empresa. En OpenERP, los módulos adicionales que contienen informes suelen llevar la etiqueta "report" en su nombre.

## 3. Tratamiento de la información

El tratamiento de la información en un ERP se realiza a través de diversos procesos. Antes de ejecutar cualquier proceso, es necesario introducir la información básica de la compañía. Por ejemplo, para gestionar la contabilidad, se deben configurar cuentas contables, cuentas bancarias, diarios de compras, ventas y caja. También definir los impuestos.

Si el módulo de contabilidad está instalado, al crear una empresa cliente o proveedor, se deben asociar cuentas contables específicas. Estas incluyen las de cobro al cliente o pago al proveedor. Por lo tanto, es esencial tener estas cuentas configuradas antes de dar de alta clientes y proveedores. Lo mismo aplica para los productos.

Además, es necesario introducir información mínima en objetos como:

- **Título.** Define el tipo de empresa o el tratamiento para una persona de contacto. El campo "Dominio" distingue entre "Empresa" y "Contacto".
- **Función.** Listado de cargos o funciones de las personas de contacto.
- **Provincias.** Listado de provincias por país.

Esta información es fundamental para introducir datos de empresas. Se accede desde el menú **Empresas/Configuración.**

### 3.1. **Cálculos: pedidos, albaranes, facturas, asientos predefinidos, trazabilidad y producción**

Entre los procesos clave de un ERP destacan:

- **Contabilidad.** Incluye operaciones económicas, determinación de costes y presupuestos. Se proporcionan asientos predefinidos. Estos agilizan la introducción de datos sin necesidad de conocimientos contables avanzados.
- **Operaciones de compra.**
  - Crear una orden de compra.
  - Recibir los bienes.
  - Controlar la factura de compra.
  - Registrar el pago al proveedor.
- **Operaciones de venta.**
  - Crear una orden de venta y recibir la conformidad del cliente.
  - Preparar los bienes, realizar el albarán y la entrega.
  - Realizar la factura de venta.
  - Registrar el cobro al cliente.
- **Trazabilidad.** Seguimiento del producto desde su entrada hasta su salida.

No todas las empresas necesitan utilizar todos los procesos del ERP. Algunas pueden usarlo solo como CRM o para contabilidad. Sin embargo, su verdadera potencia se alcanza con la integración de todas sus funciones.

### 3.2. **Utilización de asistentes**

Los asistentes son herramientas que facilitan la realización de tareas específicas en la aplicación. Suelen ser pantallas flotantes con un formato de "Siguiente, Siguiente, Aceptar". En estas, se introduce la información necesaria para completar una tarea.

Algunos ejemplos de asistentes son:

- **Asistente de configuración.** Para tareas iniciales de instalación.
- **Asistente para crear cuentas contables.** A partir de una plantilla.
- **Asistente para enviar correos electrónicos.** A uno o varios clientes.
- **Asistente para tareas masivas.** Como facturar todos los albaranes pendientes.

Los asistentes deben permitir volver atrás o reejecutarse si se comete un error. En OpenERP, por ejemplo, se puede editar el estado de un asistente no iniciado. Esto permite volver a ejecutarlo desde el menú **Administración/Configuración/Asistente de configuración.**

### 3.3. **Procedimientos almacenados de servidor**

En ocasiones, es necesario ejecutar tareas automáticamente en respuesta a eventos en la aplicación. Por ejemplo, enviar un correo electrónico al cliente cada vez que realiza un pedido. O registrar el pedido en su historial. Estas acciones se pueden automatizar mediante:

- **Procedimientos almacenados.** Programas o funciones almacenados en la base de datos. Se ejecutan directamente o mediante disparadores.
- **Eventos de servidor.** Respuestas automáticas a sucesos en la aplicación. Se definen a nivel de objetos.

En PostgreSQL, un procedimiento almacenado se define con la siguiente sintaxis:

```sql
CREATE OR REPLACE FUNCTION nombre_funcion([argumentos]) 
RETURNS tipo AS 
$BODY$
  codigo  
$BODY$
LANGUAGE lenguaje;
```

Por ejemplo, para crear un procedimiento que seleccione empresas de tipo "Sociedad Limitada" (Ltd) en OpenERP:

```sql
CREATE OR REPLACE FUNCTION PRUEBA()
  RETURNS setof res_partner AS 
$BODY$
  SELECT * FROM res_partner WHERE title='Ltd';
$BODY$
LANGUAGE sql;
```

Para ejecutar el procedimiento, se utiliza:

```sql
SELECT prueba();
```

El resultado será un listado de todas las empresas de tipo "Sociedad Limitada". Muestra sus registros en filas con los campos correspondientes.

## 4. Extracción de datos en sistemas de ERP-CRM y almacenes de datos

La extracción de datos consiste en sacar información de una aplicación para ser procesada en otra. Este proceso puede realizarse mediante diversas herramientas y técnicas. Depende de la complejidad y el objetivo.

Un uso común es conectar herramientas ofimáticas (como hojas de cálculo o procesadores de texto) a la base de datos del ERP. Esto permite extraer y manipular datos. Sin embargo, existen procesos más avanzados, como los de **Business Intelligence (BI).** Estos realizan tres tareas principales:

1. **Transformar y combinar datos** para extraer información relevante.
2. **Convertirla en indicadores clave** para la toma de decisiones.
3. **Mostrarla en formatos gráficos** para facilitar su interpretación.

Según el origen de los datos y el tipo de información requerida, se pueden utilizar:

- **Consultas e informes.** Útiles cuando todos los datos están en una sola base de datos. Se extraen mediante consultas SQL. La aplicación puede proporcionar informes predefinidos o permitir la creación de informes personalizados.
- **Almacenes de datos.** Integran información de múltiples sistemas y bases de datos. Homogeneizan y centralizan los datos para su análisis.
- **Cubos multidimensionales.** Organizan datos en ejes y celdas. Permiten un análisis multidimensional. Pueden trabajar con bases de datos relacionales o multidimensionales.

En algunos casos, la extracción y manipulación de datos no se realiza en tiempo real. Esto se debe al gran volumen de información. Puede generar una leve discrepancia entre los datos manipulados y los datos reales de la base de datos.

### 4.1. **Importar y exportar datos**

Una forma común de extraer e introducir datos es mediante la importación y exportación. El formato más utilizado es **CSV** (valores separados por comas). Este representa datos en forma de tabla, con columnas separadas por comas y filas por saltos de línea.

- **Importación.** Permite introducir datos de manera masiva en la aplicación. Se seleccionan los campos a importar y se asocian a los objetos correspondientes. Puede realizarse en una sola tabla o en varias. Se utilizan separadores para indicar la tabla de destino.
- **Exportación.** Permite extraer datos desde un objeto específico. En OpenERP, por ejemplo, la exportación desde la vista formulario permite incluir más campos que desde la vista árbol.

Ambos procesos son sencillos. Permiten trabajar con herramientas ofimáticas o editores de texto para manipular los archivos generados.

## 5. Evaluación del rendimiento y auditorías de acceso a los datos

La administración de sistemas requiere herramientas para monitorizar y evaluar el rendimiento del servidor. También para auditar el acceso a los datos. Esto es crucial para identificar cuellos de botella, resolver problemas y garantizar la seguridad del sistema.

### 5.1. **Monitorización y evaluación del rendimiento**

Para evaluar el rendimiento del servidor, se utilizan herramientas que recopilan datos sobre el uso del procesador, la memoria, los dispositivos de entrada/salida y otros parámetros. Estos datos pueden obtenerse en tiempo real o almacenarse en archivos históricos para su análisis posterior.

Una herramienta común en sistemas Linux es **sar** (System Activity Reporter). Esta está incluida en el paquete **sysstat.** Para instalarla en distribuciones como Debian o Ubuntu, se utiliza:

```bash
$ sudo apt-get install sysstat
```

Ejemplo de uso para monitorizar el procesador:

```bash
$ sar 1 3
```

Este comando muestra tres valores del uso del procesador, capturados cada segundo. Otros parámetros útiles incluyen:

- **Memoria.** `sar -r`
- **Interfaces de red.** `sar -n DEV`
- **Discos.** `sar -d`

### 5.2. **Auditorías de control de acceso a los datos. Trazas del sistema (logs)**

La actividad del sistema y las aplicaciones se registra en archivos de **logs.** Estos se ubican generalmente en el directorio `/var/log` en sistemas Linux. Estos archivos almacenan información sobre accesos, comandos ejecutados, errores y otros eventos.

Para habilitar la captura periódica de datos con **sar**, se edita el archivo `/etc/default/sysstat`. Se activa la opción `ENABLED="true"`. Luego, se reinicia el servicio:

```bash
$ /etc/init.d/sysstat start
```

Los datos se almacenan en `/var/log/sysstat/saXX`, donde `XX` representa el día del mes. Para visualizar estos datos de manera gráfica, se puede usar la herramienta **Isag.**

### 5.3. **Incidencias: identificación y resolución**

Los logs son esenciales para identificar y resolver incidencias. Por ejemplo, en OpenERP, los registros del servidor se encuentran en `/var/log/openerp-server.log`. Un ejemplo de contenido del log podría ser:

```terminal
[2011-12-21 12:41:48,935][?] INFO:web-services:starting XML-RPC services, port 8069 
[2011-12-21 12:41:48,935][?] INFO:web-services:starting NET-RPC service, port 8070 
[2011-12-21 12:41:48,935][?] INFO:web-services:the server is running, waiting for connections... 
[2011-12-21 13:52:15,678][demobd] INFO:init:module base: loading objects 
[2011-12-21 13:52:15,678][demobd] INFO:init:module base: registering objects 
[2011-12-21 13:52:17,151][demobd] INFO:init:module base: loading objects 
[2011-12-21 13:52:17,342][demobd] INFO:init:module base_setup: loading objects 
[2011-12-21 13:52:17,342][demobd] INFO:init:module base_setup: registering objects 
[2011-12-21 13:52:17,722][demobd] INFO:web-service:bad login or password from 'admin' using database 'demobd' 
[2011-12-21 13:52:24,134][demobd] INFO:web-service:successful login from 'admin' using database 'demobd' 
[2011-12-21 13:53:15,009][demobd] INFO:web-service:successful login from 'admin' using database 'demobd' 
```

Este log muestra que el servidor está en ejecución. Ha habido un intento fallido de inicio de sesión y posteriormente un acceso exitoso. Los logs permiten identificar problemas y tomar medidas correctivas.
