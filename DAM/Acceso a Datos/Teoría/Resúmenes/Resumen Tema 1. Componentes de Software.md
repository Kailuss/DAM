---
banner: "![[ad.jpg]]"
banner_y: 0.32
number headings: max 3, _.1.1.
tags:
  - DAM
  - AD
cssclasses:
  - table-compact-clean
  - dam-ad
---

# **Resumen Tema 1.** <br>Componentes de Software

Este tema aborda los fundamentos de los **_componentes de software_**, explorando su definición, importancia y las fases necesarias para su construcción. Se introduce el concepto de tratar el software como un producto mecánico, donde cada componente es una pieza independiente que puede ser ensamblada y reemplazada fácilmente. Además, se detallan las etapas clave en el desarrollo de componentes, como la especificación, implementación, empaquetado y despliegue, junto con consejos prácticos para su diseño y organización, como el uso del patrón **_Modelo-Vista-Controlador (MVC)_** y la estructuración del código en paquetes.

## 1. Introducción

Al diseñar una aplicación, las opciones dependen de sus características. Para aplicaciones simples, como un bloc de notas, un solo programa puede manejar todas las tareas. Sin embargo, en aplicaciones más complejas, el número de clases aumenta. Para facilitar la integración de estas clases, surgió el concepto de **_componente de software_**, que trata el software como un producto mecánico, diseñado por partes que encajan y pueden ser reemplazadas fácilmente.

## 2. Definición de componente

Los **_componentes de software_** son unidades ejecutables e independientes que forman parte de una aplicación. Tienen una funcionalidad y una forma de interactuar bien definidas, lo que permite su ensamblaje con otros componentes sin modificar su código interno. Ejemplos claros son los **_plugins_** o extensiones, como diccionarios en navegadores o reproductores multimedia. Otro ejemplo son los **_Drivers JDBC_**, componentes de bajo nivel que permiten construir otros más específicos.

## 3. Fases de construcción de los componentes de software

La construcción de un componente implica varias fases: **_especificación_**, **_implementación_**, **_empaquetado_** y **_despliegue_**.

### 3.1. Especificación de componentes de software

El primer paso es definir claramente las operaciones del componente, los datos que utilizará, etc. Esto puede hacerse mediante lenguajes de diseño como **_UML_** o comentarios en el código como **_Javadoc_**. Si se permiten diferentes implementaciones (por ejemplo, para bases de datos relacionales y documentales), es recomendable definir **_interfaces_**.

### 3.2. Implementación de componentes de software

La implementación se refiere a la codificación de la especificación. En Java, esto se realiza mediante clases que implementan las interfaces definidas. Es importante evitar crear **_megaclasses_** y distribuir la funcionalidad entre varias clases.

### 3.3. Empaquetado de los componentes

El empaquetado facilita la reutilización del componente. En Java, esto se logra agrupando todos los archivos en un archivo **_JAR_**, que incluye clases compiladas, recursos y un archivo **_manifest.mf_** con información sobre el componente.

### 3.4. Despliegue de los componentes de software

En Java, desplegar un componente es tan sencillo como incluir el archivo **_JAR_** en el **_classpath_** de la aplicación. En otros lenguajes, el proceso puede ser más complejo, requiriendo instaladores específicos.

## 4. Consejos prácticos

### 4.1. Modelo-Vista-Controlador (MVC)

El patrón **_MVC_** divide el código de la aplicación en tres capas: **_Modelo_** (gestiona los datos), **_Vista_** (maneja la interacción con el usuario) y **_Controlador_** (implementa la lógica de la aplicación). Este patrón facilita la reutilización y el mantenimiento del código.

### 4.2. Componentes

Cada parte del **_MVC_** puede estar formada por uno o más componentes. Si son reutilizables, es recomendable desarrollarlos en proyectos separados y distribuirlos como archivos **_JAR_**. Si son específicos de una aplicación, pueden desarrollarse dentro del mismo proyecto.

### 4.3. Paquetes

Los proyectos pueden crecer en tamaño, por lo que es importante organizar el código en **_paquetes_**. La nomenclatura estándar sugiere que los paquetes comiencen con el nombre del dominio de internet de la organización al revés, seguido del nombre del proyecto. Por ejemplo:

```java
net.programadores.blocnotes.model
net.programadores.blocnotes.vista
net.programadores.blocnotes.controlador
```

Esta estructura facilita la gestión del código en proyectos grandes.