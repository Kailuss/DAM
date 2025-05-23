---
tags:
  - DAM
  - AD
cssclasses:
  - dam-ad
  - table-clean
banner: "![[ad.jpg]]"
banner_y: 0.32
---

# **TEMA 1.** <br> Componentes de Software
## 1. Introducción

Al diseñar una aplicación, tenemos varias opciones según sus características. Por ejemplo, si la aplicación no necesita recursos externos, basta con un solo programa que realice todas las tareas. Un ejemplo podría ser el bloc de notas.

A medida que las aplicaciones se vuelven más complejas, el número de clases aumenta. Para facilitar la integración de estas clases, surgió el concepto de ***componente de software*.** La idea es tratar el software como un producto mecánico: un coche se diseña por partes, de modo que cada una encaje con las demás y pueda ser cambiada fácilmente.

De manera similar, se organizan las clases de una aplicación en componentes independientes, permitiendo la creación y ensamblaje final de manera eficiente.

## 2. Definición de componente

Siguiendo con el ejemplo del coche, podemos definir cuándo un conjunto de piezas se considera un componente y cuándo no. Los ***componentes de software*** son unidades ejecutables e independientes que forman parte de una aplicación. Tienen una funcionalidad y una forma de interactuar bien definidas, lo que permite su ensamblaje con otros componentes sin modificar su código interno. Además, en cualquier momento pueden ser sustituidos por otro componente equivalente con la misma funcionalidad.

Un ejemplo claro de componentes de software son los ***plugins*** o extensiones. Por ejemplo, instalar un diccionario en un navegador o un reproductor multimedia para visualizar ciertos formatos de video. Estos plugins son unidades independientes que se integran en una aplicación sin necesidad de modificar su código. Su instalación es sencilla y pueden ser reemplazados por versiones más eficientes o actualizadas.

Los componentes no siempre son tan independientes. Algunos son esenciales para el funcionamiento de las aplicaciones. Un ejemplo son los ***Drivers JDBC***, que son componentes de bajo nivel utilizados para construir otros componentes más específicos. Cumplen con todos los requisitos de un componente: son unidades ejecutables, tienen una funcionalidad definida y pueden ser ensamblados o intercambiados fácilmente.

## 3. Fases de construcción de los componentes de software

La construcción de un componente de software implica varias fases: ***especificación***, ***implementación***, ***empaquetado*** y ***despliegue*.** Cada una de estas fases tiene características específicas que deben ser consideradas para garantizar la calidad del componente.

### 3.1. **Especificación de componentes de software**

El primer paso es definir claramente las operaciones que el componente implementará, los datos que utilizará, etc. Estas descripciones pueden realizarse mediante lenguajes de diseño como ***UML*** o utilizando comentarios en el código, como ***Javadoc*.**

Si se permiten diferentes implementaciones del componente (por ejemplo, una para bases de datos relacionales como PostgreSQL y otra para bases de datos documentales como MongoDB), es recomendable definir una o más ***interfaces*** con las operaciones que ofrecerá el componente. Luego, se implementan clases que cumplan con estas interfaces, cada una adaptada a un tipo de base de datos.

Es crucial documentar el código de manera detallada, especialmente en los componentes. Esto incluye:

- Describir las entradas de datos de cada operación.
- Especificar el tipo de resultado y cómo se obtiene.
- Indicar las condiciones bajo las cuales se producirán errores y qué excepciones se lanzarán.
- Describir los requisitos necesarios para el correcto funcionamiento de cada operación.

Por ejemplo, si un componente tiene una operación para calcular el número de ventas de un comercial en un período determinado, la documentación debe indicar que las fechas deben ser correctas y coherentes para que la operación funcione correctamente.

### 3.2. **Implementación de componentes de software**

La implementación se refiere a la codificación de la especificación. Una misma especificación puede implementarse de varias maneras. En Java, esto se realiza mediante una o más clases que implementen las interfaces u operaciones definidas en el componente. Es importante evitar crear ***megaclasses*** que concentren toda la funcionalidad. En su lugar, se debe distribuir la funcionalidad entre varias clases para reducir la complejidad.

### 3.3. **Empaquetado de los componentes**

El empaquetado facilita la reutilización del componente. En Java, esto se logra agrupando todos los archivos del componente en un archivo ***JAR*.** Este archivo puede incluir clases compiladas, recursos como imágenes, y un archivo descriptivo llamado ***manifest.mf*.** El archivo ***manifest.mf*** contiene información sobre el componente, como las bibliotecas requeridas para su ejecución.

Incluir el archivo JAR en el ***classpath*** de la aplicación permite su uso inmediato. Este proceso es sencillo en la mayoría de los IDEs, que ofrecen opciones para agregar el JAR al proyecto.

### 3.4. **Despliegue de los componentes de software**

En aplicaciones Java, desplegar un componente es tan sencillo como incluir el archivo ***JAR*** en el ***classpath*** de la aplicación. La mayoría de los IDEs ofrecen opciones para hacer esto desde sus menús. Sin embargo, en otros lenguajes, el despliegue puede ser más complejo, requiriendo la creación de instaladores específicos para cada plataforma.

## 4. Consejos prácticos

### 4.1. **Modelo-Vista-Controlador (MVC)**

Al diseñar una aplicación, es recomendable separar el código en partes más pequeñas para facilitar su desarrollo y mantenimiento. Un ejemplo es el patrón de diseño ***MVC*** (Modelo-Vista-Controlador), que divide el código de la aplicación en tres capas:

- ***Modelo*.** Clases que gestionan los datos de la aplicación, como las que representan filas de una tabla en una base de datos.
- ***Vista*.** Clases que manejan la interacción con el usuario, como ventanas en aplicaciones de escritorio o páginas web.
- ***Controlador*.** Clases que implementan la lógica de la aplicación, gestionando las acciones del usuario y la interacción con el modelo.

Este patrón permite que los cambios en una capa no afecten directamente a las otras, facilitando la reutilización y el mantenimiento del código.

### 4.2. **Componentes**

Cada una de estas partes (Modelo, Vista, Controlador) puede estar formada por uno o más componentes. Si estos componentes son reutilizables en otras aplicaciones, es recomendable desarrollarlos en proyectos separados y distribuirlos como archivos ***JAR*.** Si son específicos de una aplicación en particular, pueden desarrollarse dentro del mismo proyecto.

### 4.3. **Paquetes**

Los proyectos, ya sean para una aplicación completa o para un componente específico, pueden crecer en tamaño y contener muchas clases e interfaces. Es importante organizar el código en ***paquetes*** para facilitar su localización y evitar conflictos de nombres. Los paquetes generan espacios de nombres, donde el nombre completo de una clase incluye el nombre del paquete como prefijo.

La nomenclatura estándar sugiere que los paquetes comiencen con el nombre del dominio de internet de la organización al revés, seguido del nombre del proyecto y una estructura que ayude a identificar su contenido. Por ejemplo:

```java
// Ejemplo de nomenclatura de paquetes
net.programadores.blocnotes.model
net.programadores.blocnotes.vista
net.programadores.blocnotes.controlador
```

Otra posible organización podría ser:

```java
// Ejemplo alternativo de organización de paquetes
net.programadores.gestio.personal
net.programadores.gestio.clients
net.programadores.gestio.inventari
```

Esta estructura permite una clara identificación de las clases y facilita la gestión del código en proyectos grandes.
