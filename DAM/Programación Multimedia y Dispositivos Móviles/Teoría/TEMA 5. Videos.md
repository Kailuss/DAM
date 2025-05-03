---
tags: [DAM, PMDM]
cssclasses: [dam-pmdm, table-compact-clean]
banner: "![[pmdm.jpg]]"
banner_y: 0.42
---
# **TEMA 5.** Videos

## 1. Introducción

#### Introducción a la Aplicación
- Se desarrollará una aplicación similar a una **tienda de segunda mano** utilizando una plantilla llamada **productos app.**
- La primera etapa consiste en crear un nuevo repositorio y analizar la plantilla proporcionada.

#### Estructura de Login
- La plantilla incluye una **estructura de login** y un sistema de **validación de formularios** que debe analizarse detenidamente.
- Se recomienda centrarse en la validación y la recuperación de valores de cada campo del formulario.
```dart
final _formKey = GlobalKey<FormState>();

TextFormField(
  validator: (value) {
    if (value == null || value.isEmpty) {
      return 'Campo obligatorio';
    }
    return null;
  },
  onSaved: (value) => _email = value!,
)
```


#### Pantalla Principal
- La pantalla inicial de la aplicación mostrará tarjetas para cada producto, incluyendo su nombre, ID, disponibilidad y precio.
- Los productos se consultan a través de una **API REST**, y las imágenes se cargan desde URL de servidores de imágenes.

#### Funcionalidades del Producto
- Al hacer clic sobre un producto, se abre una página con detalles, incluyendo un botón para volver atrás y opciones para modificar la imagen, nombre, precio y disponibilidad.
- Se puede **guardar la información** del producto, incluyendo cambios en la disponibilidad.

#### Cargar Imágenes
- Los usuarios pueden subir imágenes desde la cámara o la galería del dispositivo.
- Las imágenes se cargan a un servidor, y se utiliza la URL resultante para mostrarlas en la aplicación.

#### Creación de Nuevos Productos
- La funcionalidad para crear un nuevo producto permite seleccionar imágenes de la galería e incluir detalles como el nombre, precio y disponibilidad.
- Se ha implementado un control para evitar la entrada de letras en campos numéricos y limitar decimales.

#### Conclusión
- La aplicación permite gestionar productos de manera eficiente, con un sistema de backend que crea IDs para cada producto.
- Se destaca la importancia de seguir las instrucciones para asegurar un buen funcionamiento de la aplicación.

## 2. Creación y uso de una base de datos en tiempo real con Firebase para backend

#### Creación de un Proyecto en Firebase
- El vídeo comienza con la creación de una cuenta en **Firebase**, que puede estar vinculada a una cuenta de **Google.** Una vez creada, se accede a la consola de Firebase para gestionar proyectos existentes o crear uno nuevo.
- Para crear un nuevo proyecto, se solicita un nombre y se puede optar por no activar **Google Analytics.** El proyecto se crea y se prepara un espacio de trabajo para este.

#### Configuración de la Base de Datos en Tiempo Real
- La funcionalidad principal de Firebase en esta aplicación es la creación de un **backend** mediante la **Real Time Database**, que permite hacer peticiones HTTP como GET y POST, similar a un servidor API REST.
- Se crea la **Real Time Database** seleccionando la localización más cercana y configurando las reglas de seguridad para permitir el acceso abierto durante la fase de prueba.

#### Estructura de Datos
- La base de datos utiliza una estructura de **clave-valor** similar a un archivo **JSON.** Se define un nodo llamado **products**, que contendrá una lista de productos con un ID único para cada producto.
- Cada producto incluye atributos como **nombre**, **imagen** (URL) y **precio** (formato double para decimales). Se pueden añadir múltiples productos con sus respectivos atributos.

#### Importación y Exportación de Datos
- Se puede importar o exportar datos en formato **JSON**, facilitando la gestión de la información en la base de datos. Esto permite una manipulación más eficiente de los datos.

#### Acceso a la API REST
- El vídeo muestra cómo acceder a la API REST creada mediante **Postman**, donde se realiza una petición GET para obtener datos en formato JSON. La URL de acceso incluye el nombre del nodo y la extensión.json.
- Firebase permite crear rápidamente una API operativa sin necesidad de autenticación, permitiendo operaciones como GET y POST para modificar elementos.

### 2.2. Implementación de un modelo y servicio para gestionar productos en una app Flutter

#### Introducción al Proyecto
- El proyecto se basa en una aplicación llamada **productos app completo**, que utiliza una plantilla de productos app con modificaciones para la visualización de tarjetas de producto .
- Cada tarjeta de producto incluye un **tac de reservado** que indica si el producto está reservado o no, así como el precio y la imagen del producto .

#### Implementación del Provider
- Se creará un **provider** para hacer peticiones al backend y recuperar información para llenar las tarjetas de producto .
- Se creará una nueva carpeta llamada **models** para gestionar los modelos de producto y un archivo para mapear la información que retorna el servidor .

#### Mapeo de Datos
- Se utilizará **Postman** para hacer peticiones REST y recuperar datos en formato JSON, que serán mapeados a las clases de producto .
- Se modificará el campo **available** a **false** en la base de datos para asegurar que los datos se recuperan correctamente .

#### Creación de Clases
- Se creará una clase de producto con atributos como **available**, **nombre**, **feature**, y **precio.** Se destacarán los campos que son **required** y aquellos que no lo son, como la imagen .
- Se creará una nueva carpeta llamada **services** para gestionar las clases que harán las peticiones al REST .

#### Configuración del Provider
- Se definirá una clase **products service** que contendrá la **base URL** para las peticiones y una lista inicial de productos que estará vacía .
- Se incluirá el provider en la aplicación mediante un **multiprovider** para gestionar múltiples instancias de providers .

#### Finalización de la Configuración
- Se creará un **stateless widget** para gestionar el estado de la aplicación, y se definirá el **child** del multiprovider para integrar el servicio de productos .
- Se realizarán pruebas para asegurar que la configuración funciona correctamente y que no hay errores en la implementación .

### Implementación de una petición HTTP asíncrona para obtener y mapear productos en Flutter

#### Importación de Dependencias
- Para comenzar a hacer la petición HTTP, es necesario importar dependencias de HTP o utilizar la extensión **papspect** para actualizar automáticamente las dependencias   .
- Se puede introducir el nombre de la dependencia y ejecutar el **Slatter Packet** para obtener la última versión disponible   .

#### Creación del Constructor y Métodos
- Se creará un constructor que llamará a un método asíncrono llamado **products**   .
- Se introducirá una variable para saber cuánto está cargando, inicializada en **true**   .

#### Desarrollo de la Petición
- Se creará una variable **SRL** que contendrá la **authority** y el **send point** de la URL creada anteriormente   .
- Se importará el paquete **http** para tratar la respuesta, que será un **string** con formato JSON   .

#### Mapeo de la Respuesta
- La respuesta contendrá un identificador y el producto en formato clave-valor, que se mapeará a un string dinámico   .
- Se utilizará **JSON.convert** para hacer un **decode** de la respuesta   .

#### Acceso al Provider
- El servicio se llamará para llenar fichas de producto desde la página de inicio   .
- Se verificará que la conexión HTTP sea correcta, cambiando de **HTTP** a **HTTPS** si es necesario   .

#### Paso de Productos a la Lista
- Los productos se pasarán a la lista utilizando el **from map** obtenido   .
- Se creará un **forEach** para iterar sobre los productos y asignarles un ID opcional    .

#### Impresión de Resultados
- Finalmente, se podrá imprimir el nombre del primer producto de la lista para verificar que la petición se ha realizado correctamente   .