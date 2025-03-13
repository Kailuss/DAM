---
number headings: first-level 2, max 4, skip ^skipped, _.1.1.
---

# **Resumen Tema 2.1.**  <br>Sistemas ERP-CRM.  <br>Explotación y adecuación

Este documento proporciona una guía completa para la explotación y adecuación de sistemas ERP-CRM, con un enfoque práctico en Odoo. Se cubren desde la gestión de la base de datos hasta el desarrollo de módulos personalizados, incluyendo la creación de modelos, vistas y controladores. El uso de herramientas como **pgAdmin**, **Dia**, y **PyCharm** facilita el proceso de desarrollo y adaptación del ERP a las necesidades específicas de una organización.

## Introducción ^skipped

Este documento aborda la explotación y adecuación de sistemas ERP-CRM, centrándose en el software de código abierto **Odoo (versión 13).** Se divide en dos bloques principales:

1. **Explotación y adecuación de Odoo.** Se enfoca en la gestión de la base de datos, la extracción de datos y la generación de informes.
2. **Desarrollo de módulos en Odoo.** Profundiza en el diseño de modelos de datos, la creación de vistas y el controlador, utilizando el patrón **MVC (Modelo-Vista-Controlador).**

El documento asume que el lector tiene conocimientos previos en:

- Implantación técnica de Odoo.
- Lenguaje XML.
- Programación orientada a objetos.
- Lenguaje Python (aunque no es necesario un conocimiento profundo).

## Resultados de aprendizaje ^skipped

Al finalizar esta unidad, el alumno será capaz de:

1. **Gestionar y consultar información** utilizando herramientas ERP-CRM y soluciones de inteligencia de negocios (BI).
2. **Desarrollar componentes** para sistemas ERP-CRM, modificando y creando funcionalidades adicionales.

## 1. Explotación y adecuación. Odoo

### 1.1. **La base de datos de Odoo**

Odoo utiliza **PostgreSQL** como sistema de gestión de bases de datos (SGBD). La base de datos se genera a partir del mapeo de clases Python diseñadas en Odoo, lo que significa que no hay un diseño explícito de la base de datos, sino que se deriva del modelo de clases.

#### 1.1.1. Conexión a la base de datos mediante pgAdmin

Se explica cómo conectar a la base de datos de Odoo utilizando **pgAdmin**, una herramienta gráfica para administrar PostgreSQL.

#### 1.1.2. Identificar las tablas

Odoo permite identificar las tablas y columnas de la base de datos a través de los nombres de las clases Python y sus atributos. Por ejemplo, la clase `hr.employee.category` se mapea a la tabla `hr_employee_category` en PostgreSQL.

#### 1.1.3. Acceso de solo lectura a la base de datos

Se recomienda crear usuarios con privilegios de solo lectura para consultas no previstas, utilizando herramientas como **pgAdmin** o **dBeaver.**

#### 1.1.4. Acceso a PostgreSQL desde aplicaciones clientes

Se muestran ejemplos de conexión a la base de datos desde herramientas como **dBeaver** y **LibreOffice Base.**

## 2. Desarrollo de módulos en Odoo

### 2.1. **Generación de un entorno de desarrollo con el IDE PyCharm**

Se recomienda utilizar **PyCharm** como entorno de desarrollo para Odoo, debido a su soporte para Python y su facilidad para realizar *debugging*.

### 2.2. **Descripción del módulo de ejemplo: "manteni"**

Se presenta un módulo de ejemplo llamado **"manteni"**, que gestiona el mantenimiento de máquinas en una empresa, diferenciando entre **mantenimiento preventivo** y **correctivo.**

### 2.3. **Creación de un módulo desde cero**

Se explica cómo crear un módulo vacío en Odoo utilizando el comando `odoo-bin scaffold`. Un módulo incluye:

- **Modelo.** Definido en Python.
- **Vista.** Definida en XML.
- **Controlador.** Métodos en Python que gestionan la lógica de negocio.

### 2.4. **El modelo de Odoo**

El modelo de datos se diseña utilizando **diagramas UML** con la herramienta **Dia.** Luego, se implementa en Python, definiendo clases y campos.

#### 2.4.1. Diseño de clases con Dia

Se utiliza **Dia** para crear diagramas UML que representan las clases del módulo, como `manteni.workorder` (órdenes de trabajo) y `manteni.machine` (máquinas).

#### 2.4.2. models.py

El archivo `models.py` contiene la definición de las clases del módulo. Se definen atributos de clase y campos, como `Char`, `Integer`, `Float`, y campos relacionales como `Many2one`, `One2many`, y `Many2many`.

#### 2.4.3. Atributos de clase

Los atributos de clase, como `_name`, `_rec_name`, y `_order`, permiten personalizar el comportamiento de las clases.

#### 2.4.4. Campos posibles en Odoo

Se describen los tipos de campos disponibles en Odoo, como campos básicos (`Char`, `Boolean`, `Integer`) y campos avanzados (`Text`, `Selection`, `Date`, `Datetime`, campos relacionales, campos calculados, etc.).

### 2.5. **La vista en Odoo**

Las vistas en Odoo permiten visualizar y editar la información. Se definen en archivos XML y se estructuran en diferentes tipos:

- **Vista de lista o árbol.** Muestra registros en forma de tabla.
- **Vista de formulario.** Muestra un solo registro con un diseño más estético.
- **Vista de gráficos.** Muestra información en forma de gráficos (barras, líneas, etc.).
- **Vista de calendario.** Muestra eventos en un calendario.
- **Vista de búsqueda.** Permite crear criterios de búsqueda.

### 2.6. **El controlador en Odoo**

El controlador gestiona la lógica de negocio y la interacción con la base de datos. Odoo proporciona métodos ORM (Object-Relational Mapping) para crear, modificar, eliminar y buscar registros.

#### 2.6.1. Métodos ORM más comunes
- **`create(vals_list)`.** Crea registros.
- **`write(vals)`.** Modifica registros.
- **`browse([ids])`.** Recupera registros por ID.
- **`search(args)`.** Busca registros según criterios.
- **`unlink()`.** Elimina registros.

#### 2.6.2. Los decoradores

Los decoradores modifican el comportamiento de las funciones:

- **`@api.depends`.** Indica que un campo calculado depende de otros campos.
- **`@api.constrains`.** Verifica condiciones antes de guardar un registro.
- **`@api.onchange`.** Cambia un valor automáticamente cuando otro campo cambia.
