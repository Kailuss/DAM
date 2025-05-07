---
tags: [DAM, SGE]
cssclasses:
  - dam-sge
  - table-clean
banner: "![[sge.jpg]]"
number headings: max 4, _.1.
---

# **Tema 5.1.** <br>Desarrollo avanzado

**Introducción**

La explotación y adecuación de un sistema ERP-CRM implica conocer las herramientas de desarrollo que el propio ERP-CRM proporciona. En el caso de Odoo, es necesario conocer los mecanismos que ofrece el framework OpenObject, en el cual se basa el desarrollo de OpenERP.

Una vez se conoce la arquitectura MVC del framework OpenObject y se sabe interpretar el modelo, la vista y el controlador de los módulos facilitados por OpenERP, y se es capaz de diseñar nuevos, hay que profundizar en otros mecanismos importantes que proporciona OpenObject: herencia —utilizada para la adaptación de módulos existentes—, seguridad, carga masiva de datos, generación de traducciones idiomáticas, diseño de informes, diseño de cuadros de mando, entre otros. Para ello, hemos estructurado la unidad en dos apartados.

El apartado “Odoo: desarrollo avanzado” tiene como objetivo conocer los mecanismos avanzados de diseño que proporciona OpenObject. Así, veremos cómo aplicar la herencia en el diseño de modelos y vistas, cómo definir políticas de seguridad, cómo preparar cargas masivas de datos y cómo generar traducciones idiomáticas.

El apartado “Reporting & BI” está destinado al diseño de informes y cuadros de mando y tendrá dos enfoques: uno interno, generando informes y cuadros de mando que se integren en Odoo, y otro externo, utilizando una de las herramientas BI más potentes actualmente, que permite generar informes y cuadros de mando conectándose a cualquier origen de datos.

El diseño de informes integrados en Odoo se basa en el uso del lenguaje QWeb, muy sencillo y potente, que permite utilizar unas etiquetas especiales con el prefijo `t-`, que enriquecen la web con campos de Odoo. Mediante el programa `wkhtmltopdf` convertiremos la web generada en un documento PDF listo para imprimir.

Respecto al uso de alguna herramienta BI para generar informes y cuadros de mando conectándose a cualquier fuente de datos, y en particular a la base de datos PostgreSQL de una empresa gestionada por Odoo, se ha elegido la versión comunitaria de JasperReports Server. Esta elección se debe a que la herramienta de diseño de informes es la misma (JasperStudio) que se usará para diseñar informes integrables en Odoo, aprovechando así el esfuerzo. Desafortunadamente, el diseño de cuadros de mando no está disponible en la versión comunitaria de JasperReports Server, pero la empresa JasperSoft permite instalar una versión de prueba de la edición Enterprise, totalmente operativa durante treinta días, que sí permite diseñarlos.

El seguimiento de esta unidad presupone que el alumno ya conoce:

1. La implantación técnica de Odoo. Este conocimiento se adquiere en la unidad “Sistemas ERP-CRM. Implantación” del módulo profesional Sistemas de gestión empresarial.
2. La implementación del patrón modelo-vista-controlador facilitado por el framework OpenObject, en el que se basa Odoo. Este conocimiento se adquiere en la unidad “Sistemas ERP-CRM. Explotación y adecuación – I” del módulo profesional Sistemas de gestión empresarial.
3. El lenguaje XML. Este conocimiento se adquiere en el módulo profesional Lenguajes de marcas y sistemas de gestión de la información.
4. La programación orientada a objetos. Este conocimiento se adquiere en el módulo profesional Programación.
5. El lenguaje Python.

Para lograr un buen aprendizaje, es necesario estudiar los contenidos en el orden indicado, sin saltarse ningún apartado. Cuando se haga referencia a algún anexo de la web, se debe acceder y estudiarlo. Una vez estudiados los contenidos del material impreso y del material web, se deben realizar las actividades propuestas en la web.

**Resultados de aprendizaje**

Al finalizar esta unidad, el alumno/a:

1. Realiza operaciones de gestión y consulta de la información siguiendo las especificaciones de diseño y utilizando las herramientas proporcionadas por los sistemas ERP-CRM y soluciones de inteligencia de negocio (BI).
	
	- Utiliza herramientas y lenguajes de consulta y manipulación de datos proporcionados por los sistemas ERP-CRM.
	- Genera formularios.
	- Genera informes, tanto desde el sistema ERP-CRM como desde soluciones BI.
	- Genera cuadros de mando, tanto desde el sistema ERP-CRM como desde soluciones BI.
	- Exporta informes.
	- Utiliza las funcionalidades de acceso centralizado que proporcionan las soluciones BI.
	- Documenta las operaciones realizadas y las incidencias observadas.
		
2. Adapta sistemas ERP-CRM identificando los requerimientos de un supuesto empresarial y utilizando las herramientas proporcionadas por los mismos.
	
	- Identifica las posibilidades de adaptación del ERP-CRM.
	- Adapta definiciones de campos, tablas y vistas de la base de datos del ERP-CRM.
	- Adapta consultas.
	- Adapta interfaces de entrada de datos y de procesos.
	- Personaliza informes y cuadros de mando.
	- Adapta procedimientos almacenados del servidor.
	- Realiza pruebas.
	- Documenta las operaciones realizadas y las incidencias observadas.

Perfecto, aquí tienes la traducción al castellano de la siguiente sección:

## 1. Odoo: desarrollo avanzado

Una vez se domina la generación de módulos en Odoo, es importante conocer otros conceptos que, aunque secundarios, dotan al módulo de la funcionalidad necesaria para su uso en una empresa.

Los conceptos de desarrollo avanzado que hay que conocer son:

- **Esquema de seguridad.** ayuda a controlar el acceso al módulo, creando grupos y definiendo las atribuciones de cada uno de ellos.
- **Herencia.** permite modificar el núcleo de Odoo para adaptarlo a las necesidades de la empresa, pero sin modificar el código fuente del ERP.
- **Datos de ejemplo.** facilitan la comprensión del funcionamiento del módulo a usuarios noveles, mediante la incorporación de datos de muestra.
- **Traducción del módulo.** dado que en las empresas es habitual que tengan sucursales en diferentes países, se incluye la posibilidad de traducir el módulo, de forma que cada usuario pueda visualizarlo en el idioma configurado en su perfil.
- **Generación de informes y BI.** una de las grandes ventajas de utilizar un ERP es el almacenamiento masivo de información en una única base de datos. Tomar toda esa información y presentarla de una forma que aporte valor añadido a la toma de decisiones es vital en cualquier empresa.

### 1.1. **Seguridad en Odoo**

La información que se almacena dentro de un ERP es muy sensible, por lo que es necesario controlar completamente su acceso. Por ello, la seguridad es un punto muy importante en el desarrollo de cualquier módulo. En este apartado se generará un esquema de seguridad basado en diferentes grupos de usuarios, para posteriormente otorgar a cada grupo los privilegios que correspondan.

#### 1.1.1. Usuarios, grupos y permisos en Odoo

Odoo dispone de un sistema de privilegios basado en grupos. Por el hecho de pertenecer a un grupo, un usuario tiene derecho a acceder a ciertas funcionalidades u otras.

Por ejemplo, se presentará el módulo de ventas (`sales`). Para conocer los diferentes accesos posibles hay que activar el modo desarrollador y acceder al módulo de configuración, en la sección de usuarios.

Una vez se accede a la vista del grupo, pueden encontrarse las siguientes opciones:

- **Usuarios miembros del grupo.** lista de usuarios que forman parte del grupo, con posibilidad de añadir nuevos.
- **Grupos de los que se heredan características.** lista de grupos de los que este grupo incorpora todas sus características sin necesidad de especificarlas nuevamente.
- **Menús específicos a los que este usuario tiene acceso.**
- **Permisos sobre las clases.** se especifican todas las clases sobre las que el usuario tiene algún tipo de privilegio, y cuáles son: ver, editar, crear o eliminar.
- **Reglas que limitan el acceso a registros de una clase.** por ejemplo, en el grupo de ventas “Usuario: solo mostrar documentos propios”, las reglas determinan que un usuario solo puede acceder a los documentos que él mismo ha generado.

Además, para cada grupo en particular, pueden encontrarse todas las reglas y todos los permisos del ERP en el menú **Configuración > Técnico > Seguridad.**

#### 1.1.2. Incorporar un esquema de seguridad en nuestro módulo

Nos interesa saber cómo incorporar esquemas de seguridad en los módulos que diseñamos, de forma que cuando se instalen ya exista, como mínimo, un grupo de privilegios definido. Así el administrador solo tendrá que asignar los usuarios.

Un esquema de seguridad básico de un módulo de Odoo se define en dos archivos, que suelen (aunque no obligatoriamente) ubicarse en una carpeta llamada `security` y que deben referenciarse en el archivo `__manifest__.py` del módulo. Estos archivos son:

- **Archivo XML**, que contiene la definición de los grupos (y opcionalmente: usuarios, menús y reglas de negocio asignadas a cada grupo), que suele llamarse `security.xml`.
- **Archivo CSV**, que contiene los privilegios de cada grupo sobre los distintos objetos del módulo, y que se debe llamar obligatoriamente `ir.model.access.csv`. Podría ser un XML, pero como contiene una tabla de estructura fija, es más sencillo en formato CSV.

##### Ejemplo básico de `security.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
  <data noupdate="1">
    <record id="idCategoria" model="ir.module.category">
      <field name="name">nombreGrupo</field>
      <field name="description">Descripción...</field>
    </record>
    <record id="idGrupo" model="res.groups">
      <field name="name">nombreGrupo</field>
      <field name="category_id" ref="..."/>
      <field name="implied_ids" eval="..."/>
      <field name="users" eval="..."/>
    </record>
    <record id="idUsuario" model="res.users">
      <!-- Inclusión de usuarios en el grupo -->
    </record>
    <record id="idRegla" model="ir.rule">
      <!-- Definición de reglas de negocio y asignación a grupos y/o compañías -->
    </record>
  </data>
</odoo>
```

El atributo `noupdate="1"` indica que si se actualiza el módulo, no se debe reinstalar el esquema de seguridad (para no sobrescribir la configuración que haya hecho el administrador). Si se quiere que sí se reinstale, se pone `"0"`. Si hay partes que deben sobrescribirse y otras no, se usan dos elementos `<data>` distintos, uno con `noupdate="1"` y otro con `noupdate="0"`.

**Ejemplo para añadir usuarios a un grupo:**

```xml
<field name="users" eval="[(4, ref('base.user_admin'))]"/>
```

Esta sintaxis sirve para añadir registros a campos `One2many` o `Many2many`.

##### Archivo `ir.model.access.csv`

Contiene los privilegios de los grupos sobre los objetos del módulo.

**Primera línea (obligatoria):**

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
```

**Ejemplo de línea de configuración:**

```csv
access_manteni_modelo,modelo access,model_manteni_objeto,grupo_usuarios,1,1,1,0
```

Significado:

- `id`: identificador único (sin puntos).
- `name`: nombre descriptivo (puede tener puntos).
- `model_id:id`: nombre del objeto precedido por `model_`.
- `group_id:id`: identificador del grupo.
- `perm_read`, `perm_write`, `perm_create`, `perm_unlink`: permisos (1=permitido, 0=no).

Estos CSV se rellenan fácilmente con hojas de cálculo como LibreOffice Calc.

### 1.2. **Herencia en Odoo**

El mecanismo de herencia permite a los programadores adaptar módulos existentes garantizando que las actualizaciones no provoquen comportamientos inesperados. Como consultores de Odoo, es muy habitual que un cliente nos pida añadir nuevos campos, ocultar otros, modificarlos o incluso cambiar métodos. Y aunque, como Odoo es de código abierto, podríamos modificar directamente el módulo original, **no es recomendable.** Para eso existe el mecanismo de herencia, que permite hacer estos cambios de forma segura.

La herencia puede aplicarse en los tres componentes del patrón modelo-vista-controlador:

- **En el modelo.** permite ampliar clases existentes o diseñar nuevas clases basadas en ellas.
- **En la vista.** permite modificar vistas existentes o crear nuevas.
- **En el controlador.** permite sobrescribir métodos existentes o crear nuevos.

---

#### 1.2.1. Herencia en el modelo

Existen **tres tipos de herencia** en el modelo de Odoo:

1. **Herencia de clase.** Se modifica una clase existente añadiendo o quitando funcionalidades (atributos, métodos…). Es la más común.
2. **Herencia de prototipo.** Se crea una nueva clase basada en otra, con nombre distinto, pero heredando sus atributos y métodos.
3. **Herencia por delegación.** Se vincula una nueva clase con una o más existentes. Al crear un nuevo objeto, también se crean los de las clases enlazadas.

---

**Ejemplo:** Herencia de clase

Archivo `partner.py`:

```python
class Partner(models.Model):
    _inherit = 'res.partner'

    machinery_seller = fields.Boolean(string="Machinery seller", default=False)
```

- Se hereda `res.partner`.
- Se añade un nuevo campo booleano.
- Este campo se mapea en la misma tabla PostgreSQL que el objeto original.

Una vez instalado el módulo, este campo se incorpora automáticamente a la base de datos.

---

**Ejemplo:** Herencia de prototipo

Archivo `hr.py`:

```python
class Department(models.Model):
    _name = "hr.department"
    _description = "HR Department"
    _inherit = ['mail.thread']
```

- Se crea una clase nueva `hr.department`.
- Hereda funcionalidad de `mail.thread`.
- Se crea una tabla nueva en PostgreSQL.

---

**Ejemplo:** Herencia por delegación

Archivo `product.py`:

```python
class ProductProduct(models.Model):
    _name = "product.product"
    _description = "Product"
    _inherits = {'product.template': 'product_tmpl_id'}
```

- Cada vez que se crea un producto, también se crea automáticamente un `product.template`.
- El campo `product_tmpl_id` enlaza ambas clases.

#### 1.2.2. Herencia en la vista

Cuando aplicamos herencia a una clase, se pueden reutilizar las vistas del objeto padre. Sin embargo, puede interesar tener una versión personalizada. En ese caso, lo mejor es **heredar la vista existente y modificarla**, en lugar de sustituirla por completo.

El diseño de una vista heredada es igual que el de una normal, salvo que se debe añadir el siguiente elemento:

```xml
<field name="inherit_id" ref="id_xml_vista_padre"/>
```

Si la vista original está en otro módulo:

```xml
<field name="inherit_id" ref="nombre_modulo.id_xml_vista_padre"/>
```

Cuando el motor de Odoo detecta una vista heredada, busca en el elemento `<arch>` las instrucciones para modificarla. Las modificaciones se hacen sobre etiquetas existentes usando el atributo `position`.

**Posiciones disponibles:**

- `inside` (por defecto): añade el contenido dentro de la etiqueta.
- `after`: lo coloca después de la etiqueta.
- `before`: lo coloca antes.
- `replace`: sustituye completamente el contenido.
	
##### Modificación de un campo

Reemplazar el contenido de un campo:

```xml
<field name="arch" type="xml">
  <field name="campo" position="replace">
    <field name="nuevo_campo" ... />
  </field>
</field>
```

Eliminar un campo:

```xml
<field name="arch" type="xml">
  <field name="campo" position="replace"/>
</field>
```

Añadir un campo antes o después:

```xml
<field name="arch" type="xml">
  <field name="campo" position="before">
    <field name="nuevo_campo" .../>
  </field>
</field>
```

```xml
<field name="arch" type="xml">
  <field name="campo" position="after">
    <field name="nuevo_campo" .../>
  </field>
</field>
```

Modificar múltiples campos a la vez:

```xml
<field name="arch" type="xml">
  <data>
    <field name="campo1" position="after">
      <field name="nuevo_campo1"/>
    </field>
    <field name="campo2" position="replace"/>
    <field name="campo3" position="before">
      <field name="nuevo_campo3"/>
    </field>
  </data>
</field>
```

**Ejemplo real.** en el módulo de ejemplo `manteni`, se usa el archivo `partner.xml` para añadir un campo booleano (`machinery_seller`) a la vista de la clase `res.partner`.

#### 1.2.3. Herencia en el controlador

La herencia en el controlador es un mecanismo habitual, ya que lo usamos muchas veces de forma casi inconsciente al sobrescribir métodos de la capa ORM en el diseño de los módulos.

En Python se recomienda usar la función `super()` para invocar el método original de la clase base cuando se sobrescribe en una clase derivada, en lugar de llamar directamente al método con `NombreClase.metodo(self, ...)`.

**Ejemplo** (archivo `hr_employee.py`):

```python
@api.model
def create(self, vals):
    if vals.get('name') == 'Godzilla':
        raise ValidationError("¡No puedes contratar a Godzilla!")
    res = super().create(vals)
    # lógica adicional
    return res
```

Este fragmento sobrescribe el método `create`. Primero realiza una comprobación personalizada (en este caso absurda pero ilustrativa), y después invoca el método original con `super()`.

**Consideraciones al sobrescribir métodos**

- A veces, **se quiere sustituir totalmente** el método de la clase base, sin aprovechar nada del original: simplemente no se llama a `super()`.
- En otras ocasiones, **sí interesa aprovechar la lógica original.** entonces se llama explícitamente a `super()` dentro del método redefinido.

### 1.3. **Datos de ejemplo**

En ocasiones es necesario hacer una **carga masiva de datos** en los objetos de un módulo. Esto puede deberse a:

- La necesidad de incluir información imprescindible (por ejemplo, tipos de IVA de un país en un módulo de contabilidad).
- La inclusión de datos de demostración.
	
**Importante:** esta carga **no debe hacerse directamente sobre la base de datos**, ya que podría provocar malfuncionamientos. Odoo proporciona mecanismos para ello mediante archivos **CSV** (para un solo modelo) o **XML** (para múltiples modelos).

#### 1.3.1. Archivos CSV

- El nombre del archivo debe coincidir con el objeto (tabla).
- La primera línea debe contener obligatoriamente los nombres de los campos.
- Las siguientes líneas contienen los datos a insertar.

#### 1.3.2. Archivos XML

Plantilla genérica:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<odoo>
  <data noupdate="1">
    <record id="idRecurso" model="nombre_objeto">
      <field name="campo1">valor</field>
      <field name="campo2">valor</field>
    </record>
    <record id="otroRecurso" model="otro_objeto">
      <field name="campo1">valor</field>
      ...
    </record>
  </data>
</odoo>
```

- El atributo `noupdate="1"` indica que **no debe sobreescribirse al actualizar el módulo.** Si se quiere que siempre se sobreescriba, se pone `noupdate="0"`.
- Si hay datos que sí deben sobrescribirse y otros que no, se usan dos bloques `<data>` separados.

**Incluir los archivos en el `__manifest__.py`:**

```python
'data': [
    'data/datos_basicos.xml'
],
'demo': [
    'data/datos_demo.xml'
],
```

- Lo que va en `data` es obligatorio para el módulo.
- Lo que va en `demo` es solo para demostración.

#### 1.3.3. Ejemplo práctico de datos XML

```xml
<odoo>
  <data>
    <!-- Departamento -->
    <record id="dep_maintenance" model="hr.department">
      <field name="name">Mantenimiento</field>
    </record>

    <!-- Puestos -->
    <record id="job_maintenance_manager" model="hr.job">
      <field name="name">Jefe de mantenimiento</field>
      <field name="department_id" ref="dep_maintenance"/>
    </record>

    <record id="job_maintenance_officer" model="hr.job">
      <field name="name">Técnico de mantenimiento</field>
      <field name="department_id" ref="dep_maintenance"/>
    </record>
  </data>
</odoo>
```

#### 1.3.4. Ejemplo con campos Many2many (sintaxis `eval`)

```xml
<record id="workorder1" model="manteni.workorder">
  <field name="date_begin" eval="datetime.today()"/>
  <field name="description">Mantenimiento ordinario eléctrico</field>
  <field name="employee_id" ref="employee_paco"/>
  <field name="employee_user_id" ref="user_paco"/>
  <field name="machine_ids" eval="[(6, 0, [ref('torno1'), ref('torno2')])]"/>
  <field name="program_id" ref="program0"/>
  <field name="state">opened</field>
  <field name="name">Preventivo eléctrico tornos</field>
  <field name="type">preventive</field>
</record>
```

- La sintaxis `[(6, 0, [...])]` borra los valores existentes y añade los nuevos (común en campos One2many o Many2many).

### 1.4. **Traducción del módulo**

Las buenas prácticas en Odoo indican que los módulos deben desarrollarse siempre en **inglés**, aunque no estén destinados a utilizarse en ese idioma. Una vez finalizado el desarrollo, el módulo puede traducirse fácilmente a múltiples idiomas.

En este material se utiliza el formato `.po` y el software gratuito **Poedit.**

#### 1.4.1. Poedit

**Poedit** es un editor libre, de código abierto y multiplataforma para catálogos Gettext, usados en los procesos de localización.

- Usa la biblioteca `wxWidgets`.
- Licencia MIT.
- Tiene una versión gratuita y otra de pago, que permite, por ejemplo, traducción automática.

Puedes descargarlo desde su [web oficial](https://poedit.net/). Hay versiones para **Windows, macOS y Linux.**

#### 1.4.2. Preparación de los archivos de traducción

Para empezar la traducción, hay que **generar los archivos `.po`** que se editarán con Poedit. Existen dos formas:

- Crear una plantilla genérica (`.pot`) y a partir de ella crear los distintos idiomas.
- Descargar directamente un archivo `.po` ya generado para el idioma deseado.

Ambos métodos son equivalentes.

**Pasos desde Odoo:**

1. Ir a **Configuración > Traducciones > Exportar traducción** (modo desarrollador activado).
2. Elegir el idioma:
	- “Nuevo idioma” genera una plantilla vacía (`.pot`).
	- Un idioma existente genera un archivo `.po` ya con texto traducible.
3. Elegir el formato **PO** para usar en Poedit.
4. Seleccionar el módulo del que se quiere generar el archivo (o dejar en blanco para exportar todos los módulos instalados).
5. Descargar el archivo generado.

#### 1.4.3. Traducción del módulo con Poedit

1. Abrir Poedit.
2. Seleccionar "Editar una traducción existente" o "Crear una nueva desde plantilla".
3. Cargar el archivo `.po` o `.pot` previamente descargado.
4. Traducir cada una de las cadenas de texto detectadas por Odoo.

Poedit va mostrando una a una las frases a traducir, permitiendo guardarlas a medida que se avanza.

#### 1.4.4. Incorporar la traducción en Odoo

Una vez finalizada y guardada la traducción:

1. Coloca el archivo `.po` dentro de una carpeta llamada `i18n` en el módulo correspondiente.
2. Reinicia el servidor.
3. Actualiza el módulo.

Odoo detectará el archivo de traducción automáticamente y aplicará los textos traducidos al idioma del usuario, si está disponible.

## 2. 'Reporting' & BI

Como habrás comprobado, las soluciones informáticas para la gestión comercial incluyen un conjunto predefinido de informes y cuadros de mando, e incluso permiten generar nuevos.

Sin embargo, hay organizaciones que necesitan una **gran cantidad de informes y cuadros de mando personalizados**, distintos de los que ofrece el sistema. Para estos casos, existen en el mercado muchas herramientas que permiten generar este tipo de información adaptada a las necesidades de la empresa.

También puede darse el caso de que sea necesario acceder a **otras fuentes de datos externas**, como cuando se tiene un ERP y un CRM conectados pero con bases de datos diferentes. Normalmente, estas conexiones no son posibles desde el propio sistema de gestión empresarial, por lo que conviene conocer **herramientas BI externas.**

### 2.1. **Reporting externo: JasperReports y JasperStudio**

**JasperReports** es un motor muy potente de generación de informes. Su versión "community" (libre) se distribuye bajo licencia **LGPL.** Está programado en Java y tiene las siguientes características:

- Soporte para múltiples **orígenes de datos** (bases de datos, XML, CSV, etc.).
- Permite generar informes en pantalla, impresora o archivos en muchos formatos: **PDF, RTF, XML, XLS, CSV, HTML, DOCX, OpenOffice....**
- Posibilidad de incluir **gráficos**, **subinformes** y **filtros** (parámetros) para personalizar los informes en tiempo de ejecución.
- Puede integrarse con aplicaciones desarrolladas en distintos lenguajes (Java, PHP, etc.).

**JasperStudio** es una interfaz gráfica de código abierto (basada en Eclipse) para diseñar informes `.jrxml`, que se conectan a las mismas fuentes de datos que JasperReports. Sus ventajas:

- Permite diseñar informes complejos con gráficos, subinformes, etc.
- Facilita la conexión con bases de datos vía JDBC, XML, Hibernate, CSV, etc.
- Incorpora JasperReports, por lo que puede generar los informes directamente.
- Publica los informes en los mismos formatos que JasperReports.

**Pasos para trabajar con JasperReports:**

1. Instalar **JasperReports Server** en la máquina deseada (puede ser la misma que la base de datos, o distinta en red, o en contenedor Docker).
2. Instalar **JasperStudio** en los ordenadores que diseñarán los informes.
3. Configurar en el servidor los **usuarios, roles y accesos a datos.**
4. Diseñar los informes con JasperStudio y **subirlos al servidor**, asignando los permisos adecuados.
5. (En versión Enterprise) diseñar cuadros de mando directamente desde la interfaz web.

#### 2.1.1. Instalación y configuración de JasperServer y JasperStudio (vídeo)

El sistema propuesto de trabajo es el siguiente:

- Un **servidor JasperReports** ubicado en una máquina diferente a la de Odoo.
- Un **servidor de base de datos** (MariaDB o MySQL), que en este caso estará en la misma máquina que JasperReports, aunque esto no es obligatorio.
- Un **servidor PostgreSQL** con la base de datos de Odoo.
- Un **cliente** con JasperStudio instalado, que se encargará de diseñar los informes y subirlos al servidor JasperReports.
- Una vez funcionando, **cualquier cliente** (dentro o fuera de la red) podrá acceder al servidor y generar informes.

Este diseño permite trabajar con distintas fuentes de datos y diseñar informes complejos en JasperStudio que luego se ejecutan directamente en JasperServer.

> En el documento se incluye un vídeo con todo el proceso de instalación y configuración:
> 
> 📽 [Vídeo de instalación y configuración de JasperServer y JasperStudio](https://player.vimeo.com/video/473785895)

#### 2.1.2. Creación de informes con JasperStudio y generación desde JasperServer (vídeo)

Una vez instalado todo el sistema, el proceso para generar informes con JasperStudio y publicarlos en JasperServer es el siguiente:

1. **Desde el cliente**, se diseña la consulta SQL que recupera la información necesaria desde la base de datos (por ejemplo, de PostgreSQL).
2. Se introduce la consulta en **JasperStudio**, que se conecta al servidor de base de datos y valida la consulta.
3. JasperStudio genera el diseño visual del informe.
4. Se conecta al origen de datos para construir el informe con datos reales.
5. Se **sube el informe al servidor JasperReports**, donde se asignan permisos de acceso.

Una vez publicado, **cualquier cliente** puede generar el informe haciendo clic, e incluso se pueden crear **filtros dinámicos (parámetros)** para personalizar la información.

> Vídeo explicativo disponible:
> 
> 📽 [Creación de informes con JasperStudio](https://player.vimeo.com/video/473786004)

### 2.2. **Generación de informes nativos de Odoo**

Esta opción consiste en **crear informes directamente dentro de Odoo** utilizando HTML/QWeb. Funciona de forma similar al diseño de una vista.

El proceso es:

1. Crear un archivo `.xml` que define el diseño del informe usando **QWeb.**
2. Convertir ese HTML a **PDF** con la herramienta `wkhtmltopdf`.
3. El informe aparece disponible en la vista del modelo correspondiente con un botón de “Imprimir”.

**Ejemplo:**  
En la vista de `sale.order`, al hacer clic en “Imprimir” se puede guardar o ver un PDF generado con el contenido del pedido, incluyendo cabecera y pie de página con los datos de la empresa.

#### 2.2.1. Edición de la plantilla genérica

Odoo permite dos niveles de configuración para los informes:

- **Configuración básica.**
	- Elegir entre 4 modelos de plantilla.
	- Editar logo, fuente y colores.
	- Añadir eslogan y mensaje en el pie de página.
	- Accesible desde “Configuración”.
- **Configuración avanzada** (modo desarrollador):
	- Acceso completo al código de la plantilla para personalizarla o clonar una nueva.
		
#### 2.2.2. Creación de un informe sobre una clase

Pasos:

1. Crear una carpeta `report` dentro del módulo.
2. Crear un archivo XML con el nombre `nombre_modulo_report.xml`.
3. Definir un `<report>` con estos atributos:

```xml
<report
  id="account_invoices"
  model="account.invoice"
  string="Invoices"
  name="account.report_invoice"
  report_type="qweb-pdf"
  print_report_name="object._get_report_filename()"
  attachment_use="True"
  attachment="(object.state in ('open','paid')) and ('INV'+(object.number or '').replace('/','')+'.pdf')"
/>
```

4. Crear una plantilla con QWeb:

```xml
<template id="report_invoice">
  <t t-call="web.html_container">
    <t t-foreach="docs" t-as="o">
      <t t-call="web.external_layout">
        <div class="page">
          <h2>Título del informe</h2>
          <p>Este objeto se llama <span t-field="o.name"/></p>
        </div>
      </t>
    </t>
  </t>
</template>
```

#### 2.2.3. El lenguaje QWeb

**QWeb** es el motor de plantillas principal que utiliza Odoo, especialmente para generar páginas HTML y documentos PDF.

Se basa en XML con **etiquetas especiales que empiezan por `t-`**, que permiten insertar lógica y datos directamente en las vistas o informes.

##### Principales directivas QWeb

- **`t-field`.** inserta el valor de un campo del objeto.

	```xml
    <span t-field="o.name"/>
    ```

- **`t-esc`.** permite evaluar expresiones Python (más flexible que `t-field`).

	```xml
    <span t-esc="line.price_unit * line.quantity"/>
    ```

- **`t-if` / `t-elif` / `t-else`.** condiciones para mostrar contenido.

	```xml
    <t t-if="user.birthday == today()">¡Feliz cumpleaños!</t>
    <t t-elif="user.login == 'admin'">¡Bienvenido, maestro!</t>
    <t t-else="">¡Hola!</t>
    ```

- **`t-foreach`.** bucle para iterar colecciones.

	```xml
    <t t-foreach="doc.line_ids" t-as="line">
      <p t-field="line.name"/>
    </t>
    ```

##### Ejemplo práctico con `t-foreach` (informe de mantenimiento)

```xml
<table class="table table-striped">
  <thead>
    <tr><th>Máquinas</th></tr>
  </thead>
  <tbody>
    <tr t-foreach="doc.machine_ids" t-as="machine">
      <td><span t-field="machine.name"/></td>
    </tr>
  </tbody>
</table>
```

#### 2.2.4. Lenguaje HTML en los informes

Para estructurar los informes se utiliza **HTML**, y Odoo permite el uso de clases de **Bootstrap 4**, un framework CSS muy extendido.

Bootstrap usa:

- **Contenedores** (`container`)
- **Filas** (`row`)
- **Columnas** (`col`), que pueden tener tamaños como `col-6`, `col-md-4`, etc.

Para quienes no quieran escribir el HTML a mano, se recomienda usar herramientas visuales como:

🛠 [LayoutIt!](https://www.layoutit.com/)

Que permiten diseñar con drag & drop y luego copiar el código generado.

#### 2.2.5. Ejemplo de creación de informe en Odoo (vídeo)

Una vez diseñado el informe:

1. Se incluye la ruta del archivo en el `__manifest__.py` para que se cargue al instalar el módulo.

	```python
    'data': [
        'report/nombre_modulo_report.xml',
    ],
    ```

2. Se reinicia el servidor y se actualiza el módulo.
3. Desde la vista del modelo correspondiente, el informe estará disponible con el botón **Imprimir.**

También se puede probar directamente accediendo por URL:

```
http://<servidor>/report/html/nombre_informe/id_registro
```

Ejemplo:

```
http://localhost:8069/report/html/manteni.report_workorder_view/2
```

> 🎬 [Vídeo: creación de informe en Odoo](https://player.vimeo.com/video/473782864)
