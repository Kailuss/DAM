---
number headings: first-level 2, max 4, skip ^skipped, _.1.1.
banner: "![[../../../_Media/Banners/vecteezy_yellow-and-white-background-with-a-wave-pattern-the-yellow_53887306.jpg]]"
banner_y: 0.64
cssclasses:
  - table-clean
---

# **TEMA 2.1.** Sistemas ERP-CRM. Explotación y adecuación

## Introducción ^skipped

Una vez realizada la implantación técnica de un ERP, el software ya debería estar en condiciones de ser utilizado por la organización para dar salida a las necesidades. Pero esto no suele ocurrir, ya que las organizaciones, aunque en muchas ocasiones se adaptan al máximo al ERP, tienen necesidades que el ERP no cubre.  

Por este motivo, para todos los ERP se necesitan profesionales programadores que sean capaces de adecuarlos a las necesidades de la organización. Dado que hay un gran abanico de ERP-CRM y es imposible abarcar las tecnologías que cada uno de ellos utiliza, hemos tenido que decidirnos por uno, para llevar a la práctica lo que hay que hacer en cualquier puesta en explotación de un ERP-CRM. El producto elegido ha sido el ERP-CRM de código abierto Odoo, en su versión 13.  

Esta unidad está destinada a introducirnos en la arquitectura MVC (patrón modelo-vista-controlador) facilitada por el *framework* OpenObject en el que se basa Odoo, y se ha estructurado en dos bloques.  

El apartado "**Explotación y adecuación. Odoo**" introduce los conceptos básicos que hay que tener en cuenta en un proceso de explotación y adecuación. Es muy importante conocer la base de datos de nuestro ERP, ya que ayuda a identificar dónde está la información, y a poder extraerla de manera lógica. Se aprenderá a generar un usuario de la base de datos con privilegios de lectura, y usarlo para extraer datos del ERP. Con esta información se pueden generar informes, cuadros de mando o similar.  

El segundo apartado, "**Desarrollo de módulos en Odoo**", profundiza en el diseño del modelo de datos en OpenObject y su implementación en la base de datos PostgreSQL. Se estudiará en detalle la sintaxis y las normas para generar un módulo de Odoo totalmente funcional. Primero se generará un diagrama UML del módulo, para, a continuación, generar el modelo en lenguaje Python, las vistas en formato XML y algunas nociones del controlador.  

El seguimiento de esta unidad presupone que el alumno es conocedor de:  

- La implantación técnica de Odoo. Su conocimiento se adquiere en la unidad "Implantación técnica de sistemas ERP-CRM: Odoo" del módulo profesional *Sistemas de gestión empresarial*.  
- El lenguaje XML. Su conocimiento se adquiere en el módulo profesional *Lenguajes de marcas y sistemas de gestión de la información*.  
- La programación orientada a objetos. Su conocimiento se adquiere en las unidades formativas relativas a programación orientada a objetos del módulo profesional *Programación*.  
- El lenguaje Python. Realmente no es necesario un conocimiento muy profundo, ya que todas las funciones aplicadas están convenientemente explicadas, pero es importante tener la base en programación orientada a objetos para entender las explicaciones.  

Para lograr un buen aprendizaje es necesario estudiar los contenidos en el orden indicado, sin saltarse ningún apartado. Cuando se hace referencia a algún anexo del web, hay que dirigirse a él y estudiarlo. Una vez estudiados los contenidos del material en papel y del material web, se deben desarrollar las actividades web.  

## Resultados de aprendizaje ^skipped

Al finalizar esta unidad el alumno/a:  

1. Realiza operaciones de gestión y consulta de la información siguiendo las especificaciones de diseño y utilizando las herramientas proporcionadas por los sistemas ERP-CRM y soluciones de inteligencia de negocios (BI).  
   - Utiliza herramientas y lenguajes de consulta y manipulación de datos proporcionados por los sistemas ERP-CRM.  
   - Genera formularios.  
   - Exporta datos.  
   - Automatiza las extracciones de datos mediante procesos.  
   - Documenta las operaciones realizadas y las incidencias observadas.  

2. Desarrolla componentes para un sistema ERP-CRM analizando y utilizando el lenguaje de programación incorporado.  
   - Reconoce las sentencias del lenguaje propio del sistema ERP-CRM.  
   - Utiliza los elementos de programación del lenguaje para crear componentes de manipulación de datos.  
   - Modifica componentes de software para añadir nuevas funcionalidades al sistema.  
   - Integra los nuevos componentes de software en el sistema ERP-CRM.  
   - Verifica el funcionamiento correcto de los componentes creados.  
   - Documenta todos los componentes creados o modificados.  

## 1. Explotación y adecuación. Odoo  

La explotación y adecuación del ERP de una organización es una tarea imprescindible, ya que garantiza que el software se mantenga en condiciones de ser utilizado por la organización para dar salida a sus necesidades. Para poder llevarlo a cabo, por un lado hay que identificar las necesidades (tarea propia de consultores) y, por otro, tener un conocimiento profundo del ERP, tanto en las funcionalidades que facilita (tarea de consultores e implantadores) como en las cuestiones técnicas vinculadas al ERP (tarea de analistas y programadores).  

Nuestra tarea como **programadores** consistirá en conocer la arquitectura del ERP y las herramientas de desarrollo que se deben utilizar para poder hacer el traje a medida que necesita la organización. El gran abanico de arquitecturas y de herramientas vinculadas a los ERP hace imposible efectuar un aprendizaje estándar de explotación y adecuación de ERP y, por tanto, nos centraremos en aclarar los puntos clave que hay que tener en cuenta y los pondremos en práctica sobre la **versión 13 de Odoo.**  

Odoo es un software de gestión empresarial desarrollado sobre el *framework* OpenObject de tipo **RAD** (*Rapid Application Development*). La facilidad de los entornos RAD radica en que el desarrollo de aplicaciones es muy simple para el programador, de manera que con poco esfuerzo se pueden obtener aplicaciones de altas prestaciones.  

El OpenObject facilita diversos componentes que permiten construir la aplicación:  

- La **capa ORM** (*Object Relational Mapping*), entre los objetos Python y la base de datos PostgreSQL. El diseñador-programador no efectúa el diseño de la base de datos; únicamente diseña clases, para las cuales la capa ORM de OpenObject efectuará el mapeo sobre el SGBD PostgreSQL.  
- Una **arquitectura MVC** (modelo-vista-controlador) en la que el modelo reside en los datos de las clases diseñadas con Python, la vista reside en los formularios, listas, calendarios, gráficos... definidos en archivos XML y el controlador reside en los métodos, definidos en las clases, que proporcionan la lógica de negocio.  
- Un **sistema de flujos de trabajo** o *workflows*.  
- **Diseñadores de informes.**  
- Facilidades de **traducción** de la aplicación a diversos idiomas.  

Nuestro objetivo es conocer cómo se diseña e implementa el modelo de datos en OpenObject. Antes, sin embargo, habrá que profundizar en el conocimiento de la **base de datos** de una empresa de Odoo, con dos finalidades:  

- Conocer la relación existente entre sus elementos (tablas y columnas) y los elementos que observamos en cualquiera de los formularios e informes de Odoo.  
- Saber cómo acceder a los datos de la empresa atacando directamente la base de datos.  

Una vez conocida la estructura de una base de datos de Odoo, podemos adentrarnos en el **diseño del modelo** en Odoo, y lo hacemos en dos fases:  

1. Utilizamos la herramienta de diagramación Dia, que posibilita la generación de un diagrama UML y a partir de la herramienta nos iniciamos en el diseño del modelo de datos de Odoo.  
2. Nos adentramos en el diseño del modelo de datos de Odoo utilizando el lenguaje Python.  

La gran diversidad de funcionamientos de las empresas hace que sea altamente improbable que un ERP esté ideado para dar salida a todas las **necesidades empresariales.** Cuando se detecta una funcionalidad no cubierta por el ERP, hay tres caminos para encontrar una solución. Por un lado, se puede adecuar el ERP para dar respuesta a las funcionalidades requeridas. Por otro, se puede adecuar el funcionamiento de la empresa a las funcionalidades facilitadas por el ERP. O bien un tercer camino, basado en la combinación de los dos caminos anteriores.  

La detección de las **funcionalidades de la empresa no admitidas** por el ERP que se quiere implantar es una de las tareas principales en el proceso de consultoría.  

El hecho que la empresa cambie su funcionamiento para **adaptarse al ERP**, aunque parezca muy brusco, es una solución que se adopta en muchas ocasiones, sobre todo cuando los consultores son capaces de demostrar a los responsables de la organización que el nuevo funcionamiento tiene claras ventajas respecto a los métodos empleados en aquel momento por la empresa.  

Hay que tener en cuenta que, a veces, la empresa puede haber establecido sus funcionamientos --en tiempos pasados-- coaccionada por las posibilidades del sistema informático vigente en aquel momento, y estos funcionamientos han devenido, con el paso del tiempo, maneras de hacer fundamentales e intocables en la organización. En estas ocasiones, la mano izquierda de los consultores e implantadores es fundamental para llevar a cabo la implantación del ERP con éxito.  

Sin embargo, no siempre se pueden adecuar los métodos de la empresa a las funcionalidades facilitadas por el ERP y, en consecuencia, hay que adecuar el ERP, hecho que puede comportar la necesidad de desarrollar módulos específicos que se puedan acoplar al ERP y/o retocar módulos (formularios e informes) del ERP.  

La adecuación de un ERP a través del **desarrollo de módulos específicos** se puede llevar a cabo, en principio, con cualquier lenguaje de programación y accediendo directamente a la base de datos del ERP. Hacerlo así, sin embargo, comporta **inconvenientes.**  

- Acceder directamente a la base de datos implica tener un conocimiento total de la base de datos y de las relaciones existentes entre sus componentes. Estas relaciones pueden cambiar en una actualización del ERP.  
- Los módulos desarrollados con un lenguaje de programación ajeno al ERP implican tener piezas fuera del ERP, excepto si somos capaces de emular la interfaz del ERP y de introducir las nuevas opciones en el árbol de menús del ERP.  

El **retoque de módulos** (formularios e informes) del ERP también tiene inconvenientes:  

- Solo es posible si disponemos del código fuente del ERP (opción válida en software de código abierto).  
- Los retoques efectuados han de garantizar su continuidad en futuras actualizaciones del ERP sin necesidad de volverlos a desarrollar.  

Los diversos inconvenientes presentados nos llevan a la necesidad de conocer y utilizar los métodos de desarrollo y/o retoque de módulos del ERP facilitados por el fabricante. Además, hay que efectuar los procesos de **actualización de datos** (altas, bajas y modificaciones) a través de las reglas de negocio del ERP, que tienen en cuenta todas las implicaciones, y nunca con accesos directos a la base de datos.  

Hay que tener en cuenta, también, que a veces puede ser conveniente acceder a los datos en modo consulta para extraer información. En estos casos, teniendo conocimiento de la estructura de la base de datos, el acceso directo a la base de datos puede ser adecuado, con la precaución de que la estructura puede cambiar en futuras actualizaciones del ERP.  

**Cuando la organización necesita informes que el ERP no facilita...**  

Si la necesidad de los informes es **puntual**, es perfectamente lícito desarrollarlos con cualquier herramienta, accediendo directamente a la base de datos, y ejecutarlos para conseguir el resultado esperado. No tenemos ninguna necesidad de incorporarlos como opciones de menú del ERP ni de guardarlos para posteriores ejecuciones. En caso de guardarlos, somos conscientes de que después de haber actualizado el ERP, puede ser necesario revisar su diseño ante posibles cambios en la base de datos.  

Si la necesidad de los informes es **periódica**, es lógico desarrollarlos con las herramientas que facilite el ERP, utilizando sus reglas de negocio, e incorporándolos como nuevas opciones de menú dentro del ERP. En este caso, ante una actualización del ERP, es muy posible que las reglas de negocio evocadas continúen existiendo (a pesar de que haya cambiado la estructura de la base de datos) y, en consecuencia, nuestro informe continúe funcionando.  

A veces, dentro de las organizaciones hay personas que, posiblemente por carencias de buenas soluciones BI vinculadas al ERP, necesitan acceder a la base de datos para extraer información (modo consulta) y, desde las herramientas ofimáticas que dominan (bases de datos ofimáticas y hojas de cálculo), desarrollar informes y cuadros de mando (*dashboards*) adecuados a sus necesidades.  

En este caso, el acceso directo (modo consulta) a la base de datos también es lógico, aunque el usuario debe ser consciente de que sus montajes se pueden ver afectados ante una actualización del ERP.  

Estos razonamientos nos llevan a las **conclusiones** siguientes:  

- Hay que conocer la estructura de la base de datos del ERP y posibilitar accesos en modo consulta, para extraer información que pueda ser gestionada desde herramientas externas.  
- Hay que conocer la gestión de reglas de negocio del ERP.  
- Hay que conocer las herramientas recomendadas por el fabricante del ERP para el desarrollo y/o retoque de módulos del ERP, hecho que puede ir acompañado del conocimiento de lenguajes de programación.  

### 1.1. **La base de datos de Odoo**

La gestión de una empresa puede hacer necesario, en un determinado momento, el acceso a la base de datos del ERP para obtener información en un formato no facilitado por el ERP. Por ello, es importante conocer el diseño de la BD (base de datos) del ERP y, en nuestro caso, de Odoo.  

En Odoo no hay un diseño explícito de la base de datos, sino que la **base de datos de una empresa de Odoo** es el resultado del mapeo del diseño de clases del ERP hacia el SGBD PostgreSQL, que es el que proporciona la persistencia necesaria para los objetos.  

En consecuencia, Odoo no facilita ningún diseño entidad-relación sobre la base de datos de una empresa ni tampoco ningún diagrama del modelo relacional. No obstante, si nos interesa disponer de un modelo relacional, se encuentran muchas herramientas que nos lo pueden construir a partir de la base de datos implementada en el SGBD PostgreSQL.  

#### 1.1.1. Paso previo: conexión a la base de datos mediante pgadmin (vídeo)  

Tanto si estamos trabajando con la instalación de Odoo *all in one* para Windows, como si nos estamos conectando a un servidor externo, es importante poder establecer una conexión con la base de datos para facilitar su comprensión.  

A continuación podemos ver un vídeo donde se explica esta conexión para los dos casos descritos anteriormente con el cliente pgadmin.  

[Enlace al vídeo](https://player.vimeo.com/video/472569113)  

#### 1.1.2. Identificar las tablas  

Si surge la necesidad de detectar la tabla o las tablas donde reside una información determinada, es porque se conoce la existencia de esta información gestionada desde el ERP y, por tanto, se conoce algún formulario del ERP a través del cual se introduce la información. Odoo posibilita, mediante el cliente web, recuperar el nombre de la clase Python que define la información que se introduce a través de un formulario y el nombre de la dato miembro de la clase correspondiente a cada campo del formulario. Esta información permite llegar a la tabla y columna afectadas, teniendo en cuenta dos cuestiones:  

- Los **nombres de las clases Python de Odoo** siempre van en minúscula (se utiliza el guion bajo para hacer legibles los nombres compuestos) y siguen la nomenclatura `nombre_del_módulo.nombre1.nombre2.nombre3...`, en la que se utiliza el punto para indicar un cierto nivel de jerarquía. Cada clase Python de Odoo es mapeada en una tabla de PostgreSQL con muchas posibilidades de que su nombre coincida con el nombre de la clase, sustituyendo los puntos por guiones bajos.  
- Los **nombres de los atributos de una clase Python** siempre van en minúscula (se utiliza el guion bajo para hacer legibles los nombres compuestos). Cada dato miembro de una clase Python de Odoo que sea persistente (una clase puede tener datos miembros calculados no persistentes) es mapeado como un atributo en la correspondiente tabla de PostgreSQL con el mismo nombre.  

**Nombres de clases Odoo y tablas PostgreSQL correspondientes**  

Haremos un ejemplo para ver la correspondencia entre los nombres de clases Odoo y las correspondientes tablas PostgreSQL.  

La clase Python `hr.employee.category` está pensada para almacenar las diferentes categorías de empleados que hay en el departamento de recursos humanos. Si revisamos su código fuente, vemos que el nombre sigue las reglas mencionadas anteriormente (figura 1.1).  

**Figura 1.1.** Clase `hr.employee.category`  

Ahora iremos a la base de datos (usando pgadmin), esperando encontrar una tabla PostgreSQL con el mismo nombre, sustituyendo los puntos por guiones bajos (figura 1.2).  

**Figura 1.2.** Tabla `hr_employee_category` en la base de datos  

De esta manera, conociendo el nombre de la clase y el nombre del dato miembro, es muy posible conocer el nombre de la tabla y de la columna correspondientes.  

Se puede configurar el cliente web para que informe del nombre de la clase y del dato miembro, al situar el ratón sobre las etiquetas de los campos de los formularios. Esta opción se llama ***modo programador*.** Como se puede ver en la figura 1.3, se encuentra en el menú de configuración.  

**Figura 1.3.** Modo programador  

Una vez activado este modo, solo acercando el ratón al campo del formulario que nos interesa, veremos un *tooltip* con información.  

Para el campo dirección de correo electrónico obtenemos que se trata del campo `work_email` del objeto `hr.employee` y, por tanto, si necesitamos efectuar una consulta sobre la base de datos accediendo a la fecha del pedido, sabemos que tendremos que ir al campo `work_email` de la tabla `hr_employee` de la base de datos de PostgreSQL (figura 1.4 y figura 1.5).  

**Figura 1.4.** Campo dirección de correo electrónico  

**Figura 1.5.** `work_email` en la base de datos  

Para el campo categoría tenemos mucha más información, ya que se trata del campo relacional `category_ids` del objeto `hr.employee`, que hace referencia a la relación `hr.employee.category`. Con esta información, si necesitamos efectuar una consulta a la base de datos para acceder a la descripción de la tienda correspondiente al pedido, sabemos que tendremos que ir al campo `category_ids` de la tabla `hr_employee` y a través de este campo, estableceremos una relación (tendremos que ver cuál) con la clave primaria de la tabla `hr_employee_category` (figura 1.6).  

Destaca la relación Many2many, que veremos más adelante.  

**Figura 1.6.** 'Tooltip' con información  

Si queremos ver las relaciones que se establecen entre las tablas `hr_employee` y `hr_employee_category`, abrimos una herramienta que permita construir estas relaciones, en este caso, ***dbeaver*.** Este es el resultado (figura 1.7).  

**Figura 1.7.** Relaciones entre `hr_employee` y `hr_employee_category`  

Podemos ver que hay una tabla intermedia, con el nombre `employee_category_rel`, que hace de puente entre ambas tablas.  

#### 1.1.3. Acceso de solo lectura a la base de datos  

Las empresas suelen tener, entre sus responsables, usuarios finales que pueden efectuar **consultas no previstas** a la base de datos y que, para conseguirlo, pueden utilizar herramientas gráficas para elaborar consultas o, incluso, si son bastante hábiles, ejecutar consultas SQL desde una consola de acceso.  

En esta situación, hay que facilitar a los usuarios que lo necesiten un usuario para acceder al SGBD PostgreSQL con los privilegios de acceso, en modo consulta, a los objetos de la base de datos que corresponda. Se aconseja seguir dos **pasos.**  

1. Crear los usuarios del SGBD con las contraseñas que correspondan.  
2. Dar los privilegios de acceso adecuados a los usuarios que correspondan.  

El acceso a la base de datos por parte de usuarios finales debe ser de **solo lectura.**  

**Crear los usuarios del SGBD**  

Para crear los usuarios del SGBD utilizamos la herramienta de administración de PostgreSQL pgAdmin. Debemos conectarnos al SGBD PostgreSQL con un usuario con privilegio de creación de usuarios (rol CREATEROLE) del SGBD. Con estas dos cosas, podemos crear los usuarios del SGBD con las contraseñas que correspondan (figura 1.8).  

**Figura 1.8.** Usuario con CREATEROLE  

Una vez conectados con este usuario, procedemos a crear el usuario o los usuarios que tendrán **derechos de consulta.** En este caso haremos un usuario para el jefe de recursos humanos, y otro para el jefe de administración. La figura 1.9 muestra la pantalla que facilita pgAdmin para crear un nuevo usuario (botón secundario del ratón sobre el nodo *Login Roles* del *Object Browser* y seleccionar la opción *New Login Role*).  

**Figura 1.9.** 'New login role'  

**Distinción entre usuarios, grupos de usuarios y roles en PostgreSQL**  

La herramienta pgAdmin muestra unificados los términos Login Role y Group Role. Si damos una mirada a la documentación del lenguaje SQL de PostgreSQL vemos la existencia de las instrucciones `create user` (para la creación de usuarios) y `create group` (para la creación de grupos de usuarios).  

PostgreSQL utilizaba los conceptos usuarios y grupos de usuarios en versiones anteriores a la 8.1, versión en la que sustituyó estos conceptos por el concepto de rol con dos variantes (rol que puede iniciar sesión, Login Role, y rol que no puede iniciar sesión Group Role) e introdujo la nueva instrucción SQL `create role`.  

Para mantener la compatibilidad con el conjunto de instrucciones SQL de las versiones anteriores a la 8.1 mantuvo la existencia de las instrucciones `create user` y `create group`, de manera que `create user` equivale a la creación de un Login Role y `create group` equivale a la creación de un Group Role.  

**Dar privilegios de acceso**  

Supongamos que queremos crear un usuario de la base de datos jefe del departamento de Recursos Humanos. Nos interesa que este usuario pueda conectarse a la base de datos mediante una interfaz web, como una aplicación BI, pero es vital que no pueda hacer cambios en la base de datos. Primero generaremos este usuario, y a continuación elegiremos las tablas que necesita consultar, y le daremos permisos de solo lectura.  

Crearemos, por tanto, un ***login role*** para este usuario. Nos colocamos en los roles y hacemos clic en el botón derecho (figura 1.10).  

**Figura 1.10.** Creación del usuario para Recursos Humanos  

La asignación de privilegios se efectúa sobre cada objeto y, a través de pgAdmin, para dar privilegios a un objeto determinado hay que situarse sobre el nombre del objeto, dentro del *Object Browser*, editar sus propiedades (con el botón secundario del ratón) e ir a la pestaña *Privileges*.  

Los **privilegios** se pueden conceder (figura 1.11):  

- En cuanto a la base de datos (para permitir o no el acceso).  
- En cuanto al esquema (para utilizarlo y/o crear objetos en él).  
- En cuanto a los objetos de la base de datos (tablas, vistas, funciones, disparadores...).  
- Incluso, en cuanto a las columnas de las tablas y vistas, para dar privilegios de acceso a columnas, hay que situarse sobre la columna y editar sus propiedades.  

**Figura 1.11.** Edición de privilegios de una columna en PostgreSQL  

Por tanto, daremos privilegios de solo lectura a la tabla `hr_employee` al usuario creado para las consultas del departamento de Recursos Humanos. Seleccionaremos la tabla, iremos a sus propiedades, y en la pestaña *Seguridad* indicaremos que tiene privilegios de lectura (figura 1.12).  

**Figura 1.12.** Privilegios de lectura asignados al usuario  

Si por motivos de eficiencia se prefiere utilizar sentencias SQL en lugar de la ventana gráfica, en PgAdmin se puede hacer de manera muy sencilla (figura 1.13).  

**Figura 1.13.** Asignación de privilegios por sentencia  

La **documentación de PostgreSQL** se encuentra en [www.postgresql.org/docs](http://www.postgresql.org/docs) y para nosotros tiene interés dar una mirada a la parte sobre los *Database Roles* y los *Privileges*, así como a las órdenes SQL `grant`, `revoke` y `create role`.  

**Comprobación de privilegios**  

Una manera rápida de ver, desde pgAdmin, los privilegios concedidos a un objeto, es situarnos sobre el objeto y ver, en la parte derecha de la pantalla, el contenido de la **propiedad ACL** (*Access Control List*); como se muestra en la figura 1.14.  

**Figura 1.14.** Comprobación de privilegios para la tabla `hr_employee`  

De la misma manera que hemos visto la lista ACL sobre la tabla `hr_employee`, podemos situarnos sobre cualquier objeto de la base de datos (esquema, tabla, vista, columna...) y tendremos acceso a la lista ACL de los privilegios concedidos sobre aquel objeto.  

Imaginemos el caso en que una tabla no tiene definida la lista ACL; esto supondrá un **agujero de seguridad**, ya que en principio permite el acceso a cualquier usuario. Para que no haya ningún privilegio de acceso, la lista ACL debería mostrar el valor `{}`.  

Podemos conseguirlo añadiendo cualquier usuario al esquema de seguridad, guardando y volviendo a editar para borrar el usuario. Cuando registremos el cambio, veremos que el valor de ACL es `{}`. La situación ideal es tener definidos los privilegios de solo un grupo reducido de usuarios. En la figura 1.15 podemos revisar los tres casos.  

**Figura 1.15.** Diferentes esquemas de seguridad para la tabla `hr_department`  

Un punto muy importante a tener en cuenta en la gestión de privilegios de PostgreSQL es **conocer los privilegios existentes**, de forma automática, después de la creación de una base de datos (ver la figura 1.16). Hay que saber que:  

- La base de datos se crea con ACL no definida, hecho que permite que cualquier usuario del servidor PostgreSQL pueda abrir sesión en aquella base de datos.  
- PostgreSQL facilita el rol `public`, que engloba a todos los usuarios de forma automática.  
- PostgreSQL facilita, a todas las bases de datos, el esquema `public`, propiedad del usuario que ha creado la base de datos, y con privilegios de utilización del esquema (`usage`) y creación de objetos (`create`) al rol `public` (es decir, a cualquier usuario). Así, si observamos la propiedad ACL del esquema `public` de una base de datos creada por el usuario `odoo`, vemos el valor `{odoo=UC/odoo, =UC/odoo}` que debemos leer como: el usuario `odoo` tiene privilegios UC (`usage+create`) y el rol `public` (no aparece a la izquierda del símbolo `=`) tiene privilegios UC (`usage+create`) y que en ambos casos han sido concedidos por el usuario `odoo` (valor que aparece después del símbolo `/`).  

**Figura 1.16.** ACL del esquema `public`  

Un usuario cualquiera, por el hecho de pertenecer al rol `public`, tiene acceso UC sobre el esquema `public` de cualquier base de datos. Esto implica que puede ver la relación (nombres) de todos los objetos existentes en el esquema (tablas, vistas...), ver la descripción de cualquier objeto (tablas, vistas...) y crear nuevos objetos dentro del esquema, pero no puede acceder a los contenidos de las tablas ni vistas, excepto si el propietario de estos objetos le concede acceso.  

En caso de que tengamos que facilitar acceso a la base de datos correspondiente a una empresa de PostgreSQL a **nuevos usuarios** y no nos interese mantener esta situación, debemos hacer lo siguiente:  

- Definiremos el valor de la propiedad ACL de la base de datos e indicaremos los usuarios a los que se facilita el privilegio de conexión.  
- Modificaremos el valor de la propiedad ACL del esquema `public`, eliminaremos la asignación de privilegios al rol `public` y asignaremos la utilización (solo `usage`) del esquema `public` a los usuarios o roles correspondientes. Esta acción ejecutada mientras el servidor está encendido puede provocar que Odoo no pueda conectarse con la base de datos hasta que se reinicie el servidor.  
- Asignaremos los privilegios (normalmente de lectura) a los usuarios o roles correspondientes sobre los objetos (tablas, vistas, columnas...) que interesen.  

#### 1.1.4. Acceso a PostgreSQL desde aplicaciones clientes (vídeo)  

En muchas ocasiones será necesario configurar estaciones de trabajo para que algunas aplicaciones instaladas puedan conectarse con el SGBD PostgreSQL para acceder a los datos almacenados. Este es el caso de las herramientas ofimáticas actuales, que suelen facilitar la conectividad con los SGBD a través de conectores ODBC o JDBC que hay que tener instalados en la máquina desde donde se quiere utilizar la herramienta ofimática.  

A continuación se ofrecen dos vídeos con ejemplos prácticos de conexión:  

- **Conexión desde dBeaver** para conocer las relaciones entre las diferentes tablas. Creación de un usuario con acceso de solo lectura.  

[Enlace al vídeo](https://player.vimeo.com/video/472575228)  

- **Conexión desde LibreOffice Base** a la base de datos para la creación de una estación de consulta a la base de datos.  

[Enlace al vídeo](https://player.vimeo.com/video/472577762)  

## 2. Desarrollo de módulos en Odoo  

El desarrollo de módulos en Odoo es indispensable para poder adecuar el ERP a las necesidades de implantación en una organización. Para aprender cómo desarrollar módulos en Odoo los **pasos** serán los siguientes:  

1. Crear un entorno de desarrollo utilizando el IDE Pycharm.  
2. Generar el diagrama UML del módulo que queremos crear. Conocer la herramienta de diagramación Dia, que nos permitirá crear este diagrama de clases.  
3. Conocer la estructura de los módulos de Odoo y comenzar a desarrollar.  

**Conocimientos básicos del lenguaje UML y de Python**  

Para diseñar diagramas con la herramienta Dia, es conveniente tener unos conocimientos básicos del lenguaje UML, de nivel similar a los adquiridos en el módulo de Programación.  

Al mismo tiempo, para desarrollar módulos de Odoo son necesarios unos conocimientos básicos del lenguaje Python. Fundamentalmente, nuestra tarea será entender el código para poder replicarlo; trabajo adecuado para cualquier programador, aunque esté especializado en otro lenguaje.  

### 2.1. **Generación de un entorno de desarrollo con el IDE Pycharm (vídeo)**

Una de las necesidades de cualquier implantador es disponer de un buen entorno de desarrollo, donde poder hacer un *debug* rápido y cómodo. Para estas tareas existen los **IDE** (*Integrated Development Environment*). En estos materiales se utilizará el **IDE Pycharm**, por los siguientes motivos:  

- Es un IDE especializado en Python, y por tanto nos ofrece un corrector sintáctico, muy apropiado para cuando no dominamos Python.  
- Tiene una versión *community*, y por tanto gratuita.  
- Hay muchas referencias a la instalación de Odoo mediante Pycharm, muy importante para poder resolver errores en la instalación.  

Para describir con detalle la confección del entorno de desarrollo, puedes ver el siguiente vídeo:  

[Enlace al vídeo](https://player.vimeo.com/video/472580019)  

### 2.2. **Descripción del módulo de ejemplo: "manteni"**

Para llevar a cabo el mantenimiento de las máquinas de una industria, es muy interesante contar con un programa que almacene toda la información que se va generando. Partimos de la siguiente situación: cada máquina que se adquiere por parte de una empresa sufrirá un desgaste a lo largo de su vida útil. Para conseguir alargar esta vida y evitar paradas se llevará a cabo un mantenimiento. Distinguimos dos tipos diferentes de mantenimiento:  

- **Mantenimiento preventivo.** consiste en ciertas medidas que ayudarán a evitar los problemas con el maquinario (por ejemplo, renovar el grasa de las máquinas con partes rotativas una vez a la semana). El fabricante aconseja cuáles son las actuaciones, y su periodicidad, aunque muchas veces es la experiencia de los operarios la que hace diseñar el mantenimiento preventivo.  
- **Mantenimiento correctivo.** consiste en reparar los problemas que van surgiendo. Es inevitable, aunque se debe intentar reducir tanto como se pueda.  

Cada vez que se lleva a cabo el mantenimiento de una máquina, sea preventivo o correctivo, se llenará una orden de trabajo, que contendrá información sobre qué máquina o máquinas están implicadas, el trabajador que ha llevado a cabo el mantenimiento, la fecha de inicio y de finalización...  

Además, podemos definir más conceptos en el ámbito de mantenimiento preventivo:  

- **Gama de mantenimiento.** es una lista de tareas, o instrucciones, que se deben llevar a cabo en una máquina, con una determinada periodicidad, y relativo a un tema en concreto. Una gama puede ser común a muchas máquinas, aunque sus modelos o propósitos sean diferentes.  
- **Instrucción de mantenimiento.** cada una de las tareas de las que está hecha una gama de mantenimiento.  

Pondremos un ejemplo de gama de mantenimiento: gama de mantenimiento eléctrico para las máquinas de una empresa.  

- **Periodicidad.** bimensual.  
- **Instrucciones.**  
  - Medida de rigidez dieléctrica.  
  - Verificar curvas de disparo.  
  - Revisión de línea de tierra, conexiones y medición de resistencia.  
  - Comprobación funcionamiento protecciones del transformador.  
- **Máquinas a las que se aplica** (dentro de la fábrica):  
  - Transformador TR-001  
  - Transformador TR-002  
  - Grupo electrógeno GE-001  

### 2.3. **Creación de un módulo desde cero**

Una vez expuesto el problema inicial, nos dedicaremos a crear un módulo de Odoo que pueda resolver estas necesidades.  

Un módulo incluye todos los elementos del patrón **modelo-vista-controlador**, que es la base de desarrollo de Odoo (figura 2.1):  

- El modelo: se define en lenguaje Python, y son los objetos que declararemos, y se traducirán en tablas PostgreSQL.  
- La vista: la definiremos en lenguaje XML.  
- El controlador: podremos diseñar métodos en lenguaje Python que controlan el funcionamiento de Odoo.  

**Figura 2.1.** Modelo-vista-controlador  

El primer paso será **crear un módulo vacío.** El archivo `odoo-bin`, que sirve para poner en marcha el servidor, puede recibir el parámetro `scaffold`, que crea un módulo vacío.  

Le tendremos que decir cómo se llama el módulo, y dónde colocarlo (figura 2.2).  

```bash
odoo-bin scaffold <module name> <where to put it>
```  

**Figura 2.2.** Creación de un módulo vacío en Odoo mediante `odoo-bin scaffold`  

Esta instrucción nos creará toda la estructura de archivos y carpetas de un módulo vacío (figura 2.3).  

**Figura 2.3.** Archivos y carpetas de un módulo nuevo  

#### 2.3.1. Archivos de presentación de un módulo  

Comenzaremos por los dos archivos que aparecen en la carpeta raíz del módulo, `__init__.py` y `__manifest__.py`.  

El archivo `__init__.py` (dos guiones bajos antes y después de `init`) identifica el módulo como un programa Python. Se colocan todos los archivos Python que hay que cargar para la ejecución del programa. Por defecto se cargan los controladores y modelos. Véalo:  

```python
# -*- coding: utf-8 -*-

from . import controllers
from . import models
```  

Por su parte, el archivo `__manifest__.py` debe estar ubicado en la raíz de la carpeta del módulo y debe tener el formato de un diccionario de Python (figura **??**). Es el responsable de determinar:  

- Nombre, descripción, autores, licencia, versión, categoría... del módulo.  
- Los archivos XML que se analizarán durante el arranque del servidor Odoo.  
- Las dependencias con otros módulos.  

Los valores del diccionario Python que contiene este archivo son los siguientes:  

| Valores | Descripción |
| ------- | ----------- |
| `name` | nombre del módulo en inglés. |
| `summary` | descripción del propósito del módulo en una frase. |
| `description` | texto que describe el módulo. |
| `author` | autor del módulo. |
| `website` | web del autor del módulo. |
| `category` | categoría a la que pertenece el módulo. Texto separado por barras `/` con la ruta jerárquica de las categorías. |
| `version` | versión del módulo. |
| `depends` | lista Python de los módulos de los que depende este módulo. |
| `data` | lista Python de los nombres de archivos XML en instalar/actualizar el módulo. La ruta de los archivos debe ser relativa a la carpeta donde se encuentra el módulo. |
| `demo` | lista de Python de nombres de archivos XML que se cargan si se ha instalado Odoo con los datos de demostración o ejemplo. Las rutas de los archivos deben ser relativas al directorio donde está el módulo. |

Los diccionarios de Python se definen entre `{}` y las palabras clave separadas por comas. Las listas se definen entre `[]` y sus valores también van separados por comas.  

**Ejemplo del archivo `__manifest__.py` del módulo manteni**  

```python
# -*- coding: utf-8 -*-
{
    'name': "manteni",
    'summary': """
        Example module made to teach Odoo""",
    'description': """
        Example module made to teach Odoo
        Industrial maintenance
    """,
    'author': "Mikel López Villarroya",
    'website': "http://www.github.com/mlvillarroya",
    'category': 'Industrial',
    'version': '0.1',
    'depends': ['base', 'hr'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/partner.xml',
        'views/views.xml',
        'views/templates.xml',
        'report/manteni_report.xml',
        'data/data.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
```  

### 2.4. **El modelo de Odoo**

Una vez presentado el desarrollo de módulos en Odoo, se llevará a cabo el primer paso importante: la **creación del modelo.** Esta tarea es crítica, ya que proporciona los fundamentos sobre los que se levantará todo el módulo. Es por ello que el primer paso será hacer el diseño teórico del módulo, mediante un **diagrama UML**; se utilizará la herramienta **DIA.** A continuación, se determinarán los archivos básicos a modificar para crear este modelo.  

#### 2.4.1. Diseño de clases con Dia  

Dia es una aplicación gráfica de propósito general para la creación de diagramas, desarrollada como parte del proyecto GNOME. Está construida de forma modular, con diferentes paquetes de formas para diferentes necesidades. A nosotros nos interesa esta herramienta para **diseñar los diagramas UML** de los módulos de Odoo que queremos desarrollar.  

Ya que hemos comenzado a definir las necesidades para el módulo de mantenimiento, crearemos a continuación, ahora con Dia, su diagrama UML. Ponemos en marcha la herramienta Dia y abrimos el archivo proporcionado (figura 2.4).  

**Figura 2.4.** Diagrama UML para el módulo manteni  

La herramienta Dia permite desarrollar diversos tipos de diagrama y, como nos interesan los diagramas UML, tendremos que tener seleccionada la opción UML en la caja de herramientas de la parte izquierda de la pantalla de Dia.  

**Herramientas para crear diagramas UML**  

En una situación como la presentada, a la hora de desarrollar un diagrama UML, es muy lógico pensar en un diseño que contenga clases para modelar los conceptos orden de trabajo, máquina, gama e instrucción.  

- Clase `manteni.workorder`, para modelar las **órdenes de trabajo.**  
- Clase `manteni.machine`, para modelar las **máquinas.**  
- Clase `manteni.program`, para modelar las **gamas de mantenimiento.**  
- Clase `manteni.program.instruction`, para modelar las **instrucciones.**  

Una primera mirada al diagrama permite introducir una serie de **conceptos** para módulos de Odoo, con las siguientes indicaciones:  

- Todos los elementos de un diagrama hay que escribirlos en inglés (incluso las etiquetas y los textos informativos). Si nos interesa tenerlos en catalán o castellano, utilizaremos posteriormente las herramientas de traducción que facilita Odoo.  
- Todas las clases se nombran en minúsculas y se recomienda incorporar, como prefijo, el nombre del módulo al que pertenecen.  
- Los nombres de módulos, clases y miembros de las clases deben ser escritos en minúscula con guiones bajos para hacer legibles los nombres compuestos.  
- La nomenclatura indicada es la que marca Odoo y, como ya debéis saber, es diferente de las nomenclaturas recomendadas en otros entornos de POO, como es el caso del lenguaje Java.  

Dado que los nombres de las clases del ejemplo tienen el prefijo `manteni`, deducimos que se trata del diagrama de un módulo llamado `manteni`.  

Otro detalle es la **nomenclatura de la clase** para las instrucciones, `manteni.program.instruction`. A la hora de crear las clases estamos dando información sobre la jerarquía subyacente, ya que las instrucciones son parte de las gamas.  

En el diagrama también observamos que entre las clases hay unos **conectores** (asociaciones entre clases) de carácter informativo y nos sirven únicamente como documentación gráfica:  

- Una gama puede contener diversas instrucciones.  
- Cada orden de trabajo contiene solo una gama. Una gama puede asociarse a muchas órdenes de trabajo.  
- Cada orden de trabajo puede aplicarse a diversas máquinas. Una máquina puede verse afectada por diversas órdenes de trabajo.  
- Cada orden de trabajo será efectuada por un trabajador. Un trabajador puede tener asociadas diversas órdenes de trabajo.  
- Cada máquina ha sido adquirida a un proveedor (`partner`). Cada proveedor nos puede vender diversas máquinas.  

**Ejemplo de diseño de un diagrama UML**  

Para describir con detalle la confección de un diagrama UML mediante un ejemplo diferente, puedes ver el siguiente vídeo:  

[Enlace al vídeo](https://player.vimeo.com/video/472581624)  

#### 2.4.2. models.py  

Una vez hemos diseñado el diagrama, comenzaremos con el desarrollo del código del modelo de Odoo. Abriremos el archivo `models.py`. El modelo de Odoo contendrá todos los objetos (clases) que se han definido anteriormente con DIA. Toda la información se introducirá en la carpeta `models`. Esta carpeta contendrá como mínimo dos archivos:  

- `__init__.py`, donde se mencionan todos los archivos que contiene la carpeta, y serán importados para crear el módulo.  
- `models.py`, donde se generarán todas las clases que componen el módulo.  

El archivo `models.py` contiene, como hemos dicho, la definición del modelo del módulo de Odoo. Para definir un objeto (clase de Odoo), hay que definir una clase de Python y posteriormente instanciarla.  

Como primer paso en la creación del modelo es muy interesante revisar el archivo `models.py` generado con un módulo vacío.  

**Ejemplo del archivo `models.py` para un módulo vacío**  

```python
# -*- coding: utf-8 -*-

# from odoo import models, fields, api

# class nom_modul(models.Model):
#     _name = 'nom_modul.nom_modul'
#     _description = 'nom_modul.nom_modul'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
```  

Como podemos ver, tenemos diversas partes:  

- **Inicialización**, especificando que la codificación es `utf-8`.  
- **Importación de los módulos Python que necesitaremos.** En caso de que se tengan que importar más, se tendrá que hacer en esta sección (por ejemplo, el módulo `datetime`).  
- **Definición de las clases.** A continuación se irán definiendo una a una las clases que habíamos propuesto en el diagrama UML.  

El siguiente paso será diseñar las clases. Dividiremos la creación de las clases en la definición de atributos de clase y definición de los campos de la clase.  

#### 2.4.3. Atributos de clase  

Los atributos de clase ayudan a editar ciertas características de la clase. Solo hay uno **obligatorio**, el atributo `_name`. El resto son **opcionales.** Aparte del atributo `_name` obligatorio, podemos encontrar, entre otros, los siguientes:  

| Atributo | Descripción |
| -------- | ----------- |
| `_rec_name` | Todas las clases por defecto tendrán un campo llamado `name` que almacenará el nombre de cada registro, que se utilizará para los campos relacionales. En caso de querer almacenar como nombre otro campo diferente, se indicará en `_rec_name`. |
| `_inherit` | Para trabajar el mecanismo de herencia. Se tratará más adelante en este manual. |
| `_order` | Permite declarar el campo que se utilizará para ordenar los registros cuando se haga una búsqueda sin especificar un orden concreto. |
| `_auto` | Define si se debe crear una tabla de la base de datos con la información de la clase. Es `True` por defecto. |
| `_table` | En caso de no querer que se genere el nombre de tabla por defecto (nombre de la clase sustituyendo los puntos por guiones bajos), nombre que tendrá. |
| `_sql_constraints` | Condiciones SQL que queremos que se revisen como medida de seguridad. Por ejemplo, nos permite verificar que en el registro añadido no estamos introduciendo un valor ya existente. |

#### 2.4.4. Campos posibles en Odoo  

Una vez indicados los atributos de la clase, se procede a definir los diferentes campos. Estos campos se tendrán que adaptar a la definición UML realizada previamente, y pueden ser de diversos tipos; diferenciamos entre:  

- **Campos básicos**  
- **Campos avanzados**  

Los **campos básicos** son campos simples que contienen información que se almacena en la base de datos. Pueden ser de diversos tipos (numérico, carácter, texto, fecha...). Algunos de los **parámetros comunes** (todos son opcionales) a cualquier campo básico son:  

| Parámetro | Descripción |
| --------- | ----------- |
| `string` | Texto que verán los usuarios relacionado con el campo. Si no se incluye, los usuarios verán el nombre del campo. Si se coloca como primer parámetro solo hay que poner el nombre, sin la etiqueta. |
| `help` | Tooltip con ayuda que verán los usuarios. |
| `readonly` | Campo de solo lectura (`False` por defecto). |
| `required` | Campo obligatorio (`False` por defecto). |
| `index` | Generar un índice en la base de datos (`False` por defecto). |
| `default` | Valor por defecto que toma el campo. Se puede utilizar un valor concreto o llamar a una función (que se describirá después en el mismo archivo), para el cálculo. |
| `groups` | Lista separada por comas de los grupos con acceso a este campo. |

Los **tipos de campos** que se pueden utilizar en Odoo son:  

| Tipo | Descripción |
| ---- | ----------- |
| `Char` | Campo básico de texto. Tiene dos parámetros: `size` (tamaño máximo del campo) y `translate` (activa la traducción del campo si lo ponemos como `True`). |
| `Boolean` | Campo booleano. |
| `Integer` | Campo entero. |
| `Float` | Número en formato coma flotante. Tiene un parámetro: `digits` (un par de números `(total, decimal)`, que representan la precisión del número flotante). |

Es obligatorio e importante que en todas las clases se defina un campo llamado `name` de tipo `Char`, ya que se utilizará para hacer referencia a la clase cuando se cruzan **campos relacionales.**  

En la figura 2.5 puedes ver la clase `manteni.machine` del módulo "manteni", que contiene diversos campos básicos.  

**Figura 2.5.** Clase `manteni.machine`  

En cuanto a los **campos avanzados**, los más sencillos serían los siguientes (figura 2.6):  

| Tipo | Descripción |
| ---- | ----------- |
| `Text` | Similar a `Char`, pero utilizado para cadenas más largas. No se indica el tamaño, y se muestra en pantalla mediante una caja multilínea. Tiene un parámetro: `translate` (activa la traducción del campo si lo ponemos como `True`). |
| `Selection` | Crea un *combo* desplegable para elegir un valor. Tiene un parámetro obligatorio: `selection` (valores posibles del campo. Se presentan como una lista de pares `(valor, texto)`, separados por comas). |

**Figura 2.6.** Campos `text` y `selection` en la clase `manteni.workorder`  

Hay **otros campos avanzados**, como:  

- Campos de fecha y hora (`Date` y `Datetime`)  
- Campos relacionales (`relational`)  
- Campos pseudorelacionales (`pseudo-relational`)  
- Campos calculados (`computed`)  
- Campos relacionados (`related`)  

**Campos de fecha y hora (`date` y `datetime`)**  

Este tipo de campo son muy importantes en Odoo, ya que sirven para **almacenar fechas y horas.** Además de poder definir y almacenar fechas y horas, podemos utilizar métodos para operar (calcular edades, sumar o restar fechas...).  

Para **introducir un valor** en un campo del tipo `date` o `datetime`, lo podemos hacer mediante:  

- Un string en el formato correcto (`YYYY-MM-DD` o `YYYY-MM-DD HH:MM:SS`)  
- Un objeto Python tipo `date` o `datetime`  
- `False` o `none`  

Si no estamos seguros de estar asignando un valor correcto a una fecha, podemos usar el método `to_date()` o `to_datetime()`.  

Otro método muy útil es `today()`, ya que nos permite introduir la fecha actual, por ejemplo como valor por defecto de un campo de fecha (figura 2.7).  

**Figura 2.7.** Campo de fecha en la clase `manteni.machine`  

**Campos relacionales (`relational`)**  

Entre las clases de Odoo se pueden establecer **tres tipos de relaciones**, similares a las del modelo entidad-relación para las bases de datos. Estas relaciones se definen mediante los atributos referenciales siguientes:  

- `Many2one`  
- `One2many`  
- `Many2many`  

**Many2one.**  
**Representa una relación hacia una clase padre.** Muchos objetos de la clase que contiene el atributo pueden estar relacionados con el mismo objeto de la clase padre.  

Como ejemplo, la relación entre la clase `workorder` y la clase `program` es `Many2one`, ya que cada orden de trabajo solo tiene una gama de mantenimiento asociada (figura 2.8).  

**Figura 2.8.** Relación "Many2one" entre la clase "workorder" y la clase "program"  

Odoo muestra los campos `Many2one` acompañados por una lista para seleccionar el objeto de la clase padre. Esto obliga a que la clase referenciada por el campo `Many2one` contenga el campo `name` (figura 2.9).  

**Figura 2.9.** Widget desplegable asociado a un campo `Many2one`  

Para definir un atributo `Many2one` en Odoo podemos utilizar (entre otros) los siguientes parámetros (figura 2.10):  

| Parámetro | Descripción |
| --------- | ----------- |
| `comodel_name` (obligatorio) | Nombre de la clase destino. |
| `domain` (opcional) | Permite filtrar para no ver todos los valores. |
| `ondelete` (opcional) | Qué hacer cuando se borra el registro referido. Los valores posibles son `set_null`, `restrict` y `cascade`. |

**Figura 2.10.** Definición del campo `Many2one program_id`  

**One2many.**  
**Representa una relación hacia una clase hija.** Un objeto de la clase que contiene el atributo puede estar relacionado con muchos objetos de la clase hija. Cada atributo `One2many` debe ser complementario de un atributo `Many2one` que debe estar obligatoriamente en la clase hija.  

Volvemos a la definición del módulo. Cada instrucción pertenece a una gama de mantenimiento, y una gama puede tener más de una instrucción. Por tanto, teniendo en cuenta las definiciones, habrá un campo `One2many` en la clase de las gamas (`manteni.program`), y un campo `Many2one` correspondiente y necesario en la clase de las instrucciones (`manteni.instruction`); como puedes ver en la figura 2.11.  

**Figura 2.11.** Relaciones `One2many` y `Many2one` entre las clases `program` e `instruction`  

Odoo muestra para los campos `One2many` una lista con todos los objetos relacionados, y la posibilidad de añadir más (figura 2.12).  

**Figura 2.12.** Widget de lista asociado a un campo `One2many`  

Para definir un atributo `One2many` en Odoo podemos utilizar (entre otros) los siguientes parámetros (figura 2.13):  

| Parámetro | Descripción |
| --------- | ----------- |
| `comodel_name` (obligatorio) | Nombre de la clase destino. |
| `inverse_name` (obligatorio) | Nombre del campo inverso `Many2one` que se encuentra en la clase destino. |
| `domain` (opcional) | Permite filtrar para no ver todos los valores. |

**Figura 2.13.** Definición del campo `Many2one instruction_ids`  

La existencia de un **atributo** `One2many` implica que debe haber un **atributo** `Many2one` correspondiente. Sin embargo, la existencia de un atributo `Many2one` no implica que deba haber un atributo `One2many`.  

**Many2many.**  
**Representa una relación de muchos a muchos entre dos objetos.** Cada objeto de una clase A puede estar relacionado con muchos objetos de la clase B y cada objeto de la clase B puede estar relacionado con muchos objetos de la clase A.  

En nuestro caso, en una orden de trabajo se puede pedir el mantenimiento de diversas máquinas, y una máquina aparecerá en diversas órdenes de trabajo, a medida que va sufriendo averías (figura 2.14).  

**Figura 2.14.** Relaciones `Many2many` `workorder` y `machine`  

Odoo muestra para los campos `Many2many` una lista con todos los objetos relacionados, y la posibilidad de añadir más, igual que en `One2many` (figura 2.15).  

**Figura 2.15.** Widget de lista asociado a un campo `Many2many`  

Para definir un atributo `Many2many` en Odoo podemos utilizar (entre otros) los siguientes parámetros (figura 2.16):  

| Parámetro | Descripción |
| --------- | ----------- |
| `comodel_name` (obligatorio) | Nombre de la clase destino. |
| `relation` (opcional) | Nombre de la tabla de la base de datos que contendrá la relación entre las dos clases. |
| `column1` (opcional) | Nombre de la columna referida para el registro de la clase actual. |
| `column2` (opcional) | Nombre de la columna referida para el registro de la clase destino. |
| `domain` (opcional) | Permite filtrar para no ver todos los valores. |

**Figura 2.16.** Definición del campo `Many2many machine_ids`  

**Campos pseudorelacionales (`pseudo-relational`)**  

Este es un tipo especial (y muy poco utilizado) de campos relacionales, donde no se genera ninguna clave foránea en la base de datos, solo un integer que relaciona el campo con su origen.  

Hay dos tipos diferentes de campos de este tipo:  

- `Reference`  
- `Many2onereference`  

**Campos calculados (`computed`)**  

Quizás nos interesa crear un campo que, en lugar de utilizar un valor almacenado en la base de datos, se genere **mediante un cálculo.** Por ejemplo, podríamos calcular de forma dinámica la edad de un trabajador de la empresa mediante su fecha de nacimiento y el día actual. De esta manera, sin necesidad de ocupar espacio en la base de datos tendríamos un dato actualizado y utilizable en cada momento.  

Hacen referencia a un método que se tendrá que definir a continuación en lenguaje Python.  

Como ejemplo podemos ver el cálculo de la fecha del primer mantenimiento, que se encuentra en la clase `machine` (figura 2.17).  

**Figura 2.17.** Campo calculado `date_first_maintenance`  

De la figura anterior, cabe destacar que:  

- En primer lugar, se encuentra un bucle `for record in self`, ya que el objeto a calcular puede ser un conjunto de registros, no solo uno (por ejemplo, si queremos mostrar las fechas de todas las máquinas en una tabla).  
- Se recoge el campo `date_begin`, que es un campo de tipo `date`.  
- Se usa la función `timedelta` de la librería `datetime` de Python para crear un objeto de tipo `date` con las horas de mantenimiento, y poderlo añadir a la fecha inicial.  

**Campos relacionados (`related`)**  

El último tipo de campo avanzado es el relacionado. Los campos relacionados sirven para **obtener un valor de otro modelo**, siguiendo las relaciones entre atributos. Esto evita tener que duplicar información en la base de datos.  

Por ejemplo, en la clase `manteni.machine` hemos creado el campo `suplier_id`, que hace referencia a la tabla `res_partner`. Si además del nombre de la empresa quisiéramos mostrar su dirección, podríamos utilizar un campo `related`, que usase `suplier_id` para consultar en la tabla `res_partner` sin necesidad de duplicar la información (figura 2.18).  

**Figura 2.18.** Campo relacionado en el módulo `manteni`  

**Ejemplo de creación del modelo de un módulo**  

Para describir con detalle la confección del modelo de un módulo mediante un ejemplo diferente, puedes ver el siguiente vídeo:  

[Enlace al vídeo](https://player.vimeo.com/video/472582195)  

### 2.5. **La vista en Odoo**

Odoo es un software de gestión empresarial desarrollado sobre el *framework* OpenObject de tipo RAD (*Rapid Application Development*) que facilita una arquitectura MVC (modelo-vista-controlador) para los desarrollos. Una vez se domina el diseño del modelo de datos de una aplicación desarrollada sobre OpenObject, como es el caso de Odoo, hay que entrar en el conocimiento del diseño de la vista y del controlador. En las aplicaciones desarrolladas sobre el *framework* OpenObject, el concepto vista engloba las **pantallas** que permiten exponer la información al usuario (llamadas *vistas* o *views*) para visualizarla y/o editarla, y los menús, que facilitan un acceso organizado a las vistas. En consecuencia, debemos aprender a diseñar las vistas (*views*) y los menús (figura 2.19).  

**Figura 2.19.** Vista de la ficha de un trabajador (módulo de Recursos Humanos)  

Por tanto, diremos que las **vistas de Odoo** son las pantallas que facilitan el acceso del usuario a la información, tanto para consultarla como para modificarla (altas, bajas y modificaciones). Las vistas son dinámicas y se construyen en tiempo de ejecución a partir de descripciones XML accesibles desde el cliente, hecho que posibilita, incluso, su modificación en tiempo de ejecución.  

#### 2.5.1. Declaración de la vista  

La descripción de las vistas debe residir en un **archivo XML** que debe estar referenciado desde el apartado `data` del archivo descriptor del módulo `__manifest__.py`. Así, en el módulo de ejemplo "manteni" observamos la presencia del archivo llamado `views.xml` y en el archivo `__manifest__.py` encontramos la línea (figura 2.20):  

**Figura 2.20.** Línea de carga del archivo `views.xml` en `__manifest__.py`  

El nombre del archivo XML en el que residen las vistas puede ser cualquiera, pero es altamente recomendable utilizar el nombre genérico "views.xml" o una combinación en la que aparezca el nombre del módulo y algo que indique su contenido (por ejemplo, "manteni.xml" o "manteni_views.xml").  

#### 2.5.2. Sintaxis genérica y tipos de vistas  

Más allá de los diferentes tipos de vistas que podamos encontrar, hay una sintaxis genérica **común a cualquier vista.**  

Los campos que admite esta **declaración genérica** (entre otros), son los siguientes:  

| Campo | Descripción |
| ----- | ----------- |
| `name` (obligatorio) | Nombre de la vista. |
| `model` | Clase a la que hace referencia esta vista. |
| `priority` | Prioridad para cargar la vista. Si Odoo tiene que cargar varias vistas, elegirá la que tenga un número de prioridad más bajo. |
| `arch` | Descripción específica de la vista. **Esta es la parte en la que cada tipo de vista específico tendrá su sintaxis.** |
| `groups_id` | Qué grupos de Odoo podrán ver esta vista. |
| `inherit_id` | Veremos el concepto de herencia más adelante. |

La sintaxis mínima de la declaración de una vista será similar a:  

```xml
<record model="ir.ui.view" id="view_id">
    <field name="name">Nombre_de_la_vista</field>
    <field name="model">Objeto_al_que_hace_referencia</field>
    <field name="arch" type="xml">
        <!-- Aquí va el contenido específico de la vista -->
        <VIEW_TYPE>
            <VIEW_SPECIFICATIONS/>
        </VIEW_TYPE>
        <!-- Fin del contenido específico de la vista -->
    </field>
</record>
```  

Esta **sintaxis genérica** es común a todos los diferentes tipos de vistas, y por tanto hay que entenderla.  

Además, como hemos dicho, hay diferentes **tipos de vistas**, cada una con su sintaxis y especificaciones; como:  

- Vista de lista o árbol  
- Vista de formulario  
- Vista de gráficos  
- Vista de calendario  
- Vista de búsqueda  

**Vista de lista o árbol**  

Este tipo de vistas consiste en una distribución de líneas con el objetivo de **facilitar la visualización** y/o edición de un conjunto de recursos de un objeto. Igual que para el resto de vistas, generaremos el código estándar a partir del atributo `arch`, personalizando la siguiente línea:  

```xml
<field name="arch" type="xml">
    <tree atributos...>
        <diferentes etiquetas>
    </tree>
</field>
```  

Hay, entre otros, los siguientes **atributos.**  

| Atributo | Descripción |
| -------- | ----------- |
| `editable` | Por defecto, para editar una lista hacemos clic sobre una de las líneas, y se abrirá el formulario definido para la edición. Sin embargo, el atributo `editable` nos permite hacerlo sobre la misma lista. Puede tomar los valores `top` o `bottom`. |
| `default_order` | Cambia el orden por defecto por uno personalizado. |
| `decoration - {\$ name}` | Permite cambiar el color de las líneas de la lista, en función de una variable determinada. Se introduce una expresión Python para ser evaluada. `{\$ Name}` puede ser sustituido por los valores siguientes: valores html (por ejemplo `bf`, `font-weight: bold`, `it`, `font-style: italic`) o etiquetas predeterminadas (`danger`, `info`, `muted`, `primary`, `success`, `warning`). |
| `create`, `edit`, `delete` | Permite desactivar estas funciones si el atributo se coloca a valor `False`. |

Bajo la **etiqueta `<tree>`** podemos encontrar los siguientes elementos:  

| Elemento | Descripción |
| -------- | ----------- |
| `button` | Muestra un botón. Entre otros lleva los atributos: `icon` (icono del botón), `string` (texto del botón), `type` (tipo del botón: `workflow`, `object`, `action`), `states` (hace el botón invisible si no se cumple la condición), `confirm` (mensaje de confirmación para su aceptación). |
| `Field` | El elemento más habitual. Muestra un campo. Entre otros lleva los atributos: `name` (nombre del campo), `string` (texto de la columna, por defecto la etiqueta del campo), `invisible` (se tiene en cuenta para Odoo, pero no aparece en la lista. Imprescindible si el campo es una de las condiciones para cambiar la decoración de la tabla), `groups` (grupos que pueden ver el campo). |

**Ejemplo de vista de lista o árbol**  

En la figura 2.22 y la figura 2.21 puedes ver la vista creada para la clase `manteni.machine`.  

**Figura 2.21.** Vista de lista de la clase `manteni.machine`  

**Figura 2.22.** Código para la vista de lista de la clase `manteni.machine`  

**Vista de formulario**  

La vista de formulario está pensada para **mostrar la información de un solo registro.** A diferencia de la vista de lista, que es claramente funcional, la vista de formulario tiene un importante componente estético: es clave ordenar la información de manera clara y agradable. Igual que para el resto de vistas, generaremos el código estándar a partir del atributo `arch`, personalizando la siguiente línea:  

```xml
<field name="arch" type="xml">
    <form atributos...>
        <diferentes etiquetas>
    </form>
</field>
```  

En estas vistas diferenciaremos los componentes estructurales (sirven para fijar la estética del formulario) y los componentes semánticos (indican qué campos saldrán en el formulario).  

**Componentes estructurales.**  
Estos componentes están pensados para proveer ayuda visual al formulario. Son los siguientes:  

| Componente | Descripción |
| ---------- | ----------- |
| `sheet` | Se coloca debajo de la etiqueta `<form>`, y sirve para crear una hoja, que hace el formulario más *responsive* (adaptable a pantallas de diferentes tamaños). |
| `header` | Es la cabecera del formulario, que en edición avanzada se utiliza para colocar botones o marcadores de estado. |
| `group` | Es muy importante para la vista "form", ya que permite definir la estructura de columnas del formulario. Dentro de un grupo se crean dos columnas diferentes, de manera que si colocamos una etiqueta `<field>`, mostrará el nombre del campo en una columna y su valor en otra. El número de columnas que tiene un grupo puede personalizarse mediante el atributo `col`. Se puede colocar una etiqueta `<group>` dentro de otra, de manera que subdividimos el formulario en diferentes columnas (ver la figura 2.23 y la figura 2.24). |

**Figura 2.23.** Grupos dentro de otro grupo en la vista `form`  

**Figura 2.24.** Resultado en Odoo del código de la figura anterior  

| Componente | Descripción |
| ---------- | ----------- |
| `notebook` | Define una sección con pestañas. Cada pestaña será un elemento con la etiqueta `<page>`. |
| `page` | Su atributo más importante es `string` (obligatorio), que da el título de cada pestaña (figura 2.25). |

**Figura 2.25.** Uso de `notebook` y `page` en la vista de empleado  

| Componente | Descripción |
| ---------- | ----------- |
| `newline` | Crea una nueva fila a partir de la etiqueta. |
| `separator` | Pequeña línea horizontal (solo tiene un efecto estético). |

**Componentes semánticos.**  
Estos componentes permiten la interacción con el sistema Odoo. Son los botones y los campos. Los botones se comportan de la misma manera que los de la vista de lista, y por tanto no se volverán a comentar. Nos centramos, pues, en los campos `<field>`.  

Hay diferentes atributos que pueden acompañar a los campos `<field>`. Los principales son:  

| Atributo | Descripción |
| -------- | ----------- |
| `name` | Es obligatorio e indica el nombre del campo. |
| `widget` | Los diferentes tipos de campos se muestran de diferente manera por defecto. Con este atributo se puede obligar a cambiar el aspecto. Presentamos algunos ejemplos de los widgets por defecto para diferentes tipos de campos (figura 2.26, figura 2.27, figura 2.28 y figura 2.29): |

**Figura 2.26.** Widget por defecto para los campos tipo `Select`  

**Figura 2.27.** Widget por defecto para los campos tipo `Date`  

**Figura 2.28.** Widget por defecto para los campos tipo `Many2one`  

**Figura 2.29.** Widget por defecto para los campos tipo `One2many` y `Many2many`  

| Atributo | Descripción |
| -------- | ----------- |
| `class` | Tenemos la posibilidad de añadir clase CSS, de manera que podemos cambiar cómo se muestran los diferentes campos. Algunos ejemplos: `oe_inline` (cancela un salto de línea entre dos campos), `oe_left`, `oe_right` (hace flotar el contenido en la dirección indicada), `oe_read_only`, `oe_edit_only` (hace que el campo solo se muestre en el modo indicado: lectura o edición). |
| `groups` | Restringe la visualización del campo a ciertos grupos (figura 2.30). |

**Figura 2.30.** Ítem de menú del módulo `manteni` restringido al grupo `manteni_manager`  

| Atributo | Descripción |
| -------- | ----------- |
| `domain` | Para campos relacionales, determina los valores que deben mostrarse, ocultando el resto. |
| `context` | Sirve para crear filtros, enviando los campos implicados y la igualdad que deben cumplir (figura 2.31). |

**Figura 2.31.** Uso de `domain` y `context` en una vista `search` del módulo `manteni`  

| Atributo | Descripción |
| -------- | ----------- |
| `readonly` | Hace el campo de solo lectura. |
| `required` | Hace el campo obligatorio. |
| `nolabel` | Evita mostrar la etiqueta, cuando el campo está dentro de un `<group>`. |
| `help` | Muestra un tooltip con un texto de ayuda. |

**Vista de gráficos**  

Esta vista está pensada para **visualizar información de manera gráfica.** Igual que para el resto de vistas, generaremos el código estándar a partir del atributo `arch`, personalizando la siguiente línea:  

```xml
<field name="arch" type="xml">
    <graph atributos...>
        <diferentes etiquetas>
    </graph>
</field>
```  

Se pueden utilizar **dos atributos**, ninguno de ellos obligatorio. Son los siguientes:  

| Atributo | Descripción |
| -------- | ----------- |
| `type` | A elegir entre `bar` (por defecto), `pie` y `line` el tipo de gráfico que se utilizará. |
| `stacked` | Solo para los gráficos de barras (`bar`). Agrupa las barras. |

La única etiqueta permitida dentro de los gráficos es `<field>`. Puede tener los siguientes atributos:  

| Atributo | Descripción |
| -------- | ----------- |
| `name` (obligatorio) | El nombre del campo que utilizaremos para la vista. |
| `title` (opcional) | Texto que se muestra encima del gráfico. |
| `type` | Indica para qué se utilizará el campo. Puede tener los valores: `row` (el campo se utilizará para agrupar, eje X), `col` (solo se utiliza para tablas), `measure` (el campo servirá para cuantificar los campos agrupados, eje Y). |
| `interval` | Para los campos tipo `date` o `datetime`, agrupa según el intervalo indicado (`day`, `week`, `month`, `quarter` o `year`). |

**Ejemplo de vista de gráficos**  

Como ejemplo, se puede ver el gráfico generado en el módulo `hr_attendance`, que muestra las asistencias de los trabajadores de la empresa. Como campos agrupadores tenemos `employee_id` y `check_in`, es decir, presentará en el eje X los trabajadores que han comunicado su entrada. Como campo de medida tenemos `worked_hours`, es decir, irá sumando en el eje Y las horas de asistencia de cada trabajador (figura 2.32 y figura 2.33):  

**Figura 2.32.** Gráfico generado automáticamente para la clase `hr_attendance`  

**Figura 2.33.** Código fuente de la vista de gráfico para la clase `hr_attendance`  

**Vista de calendario**  

Esta vista está pensada para **visualizar información en forma de calendario.** Igual que para el resto de vistas, generaremos el código estándar a partir del atributo `arch`, personalizando la siguiente línea:  

```xml
<field name="arch" type="xml">
    <calendar atributos...>
        <diferentes etiquetas>
    </calendar>
</field>
```  

Los **atributos** que se pueden utilizar (entre otros), son:  

| Atributo | Descripción |
| -------- | ----------- |
| `date_start` (obligatorio) | Campo que definirá la fecha de inicio de cada evento. |
| `date_stop` | Campo que definirá la fecha de finalización de cada evento. |
| `date_delay` | Alternativo a `date_stop`. Campo que definirá la duración de un evento. |
| `color` | Indica el campo para hacer la segmentación por colores. Todos los registros con el mismo valor en este campo compartirán color en el calendario. |
| `all_day` | Boolean que indica si los eventos serán siempre de todo el día. |
| `mode` | Indicamos el modo por defecto del calendario: `day`, `week` o `month`. |

**Ejemplo de vista de calendario**  

A continuación, puedes ver la vista del calendario (figura 2.34) y el código para la vista (figura 2.35) para la clase `manteni.workorder`.  

**Figura 2.34.** Vista de calendario de la clase `manteni.workorder`  

**Figura 2.35.** Código para la vista de lista de la clase `manteni.workorder`  

**Vista de búsqueda**  

Esta vista está pensada para crear criterios de búsqueda en las vistas de lista. Igual que para el resto de vistas, generaremos el código estándar a partir del atributo `arch`, personalizando la siguiente línea:  

```xml
<field name="arch" type="xml">
    <search atributos...>
        <diferentes etiquetas>
    </search>
</field>
```  

Podemos crear cuatro funcionalidades diferentes:  

| Funcionalidad | Descripción |
| ------------- | ----------- |
| `field` | Indica en qué campo debe buscar cuando introducimos un texto en el cuadro de búsqueda. Odoo hará la búsqueda mediante el criterio escrito en el *textbox*, buscando en todos los fields que se han introducido con la operación AND. Se pueden añadir (entre otros), los siguientes atributos: `name` (nombre del campo), `string` (etiqueta del campo), `operator` (indica el operador que utilizará Odoo para buscar. Por ejemplo, cuando buscamos en un campo de texto, Odoo generará una búsqueda del tipo `[(name, ilike, valor_introducido)]`. Si añadimos el atributo `operator` podemos cambiar este `ilike` por defecto por otro operador), `filter_domain` (permite definir completamente la búsqueda que queremos hacer. Acepta una lista con una tabla Python de tres elementos `(name, operator, provided_value)`), `context` (permite incluir condiciones), `groups` (hace visible el campo solo a grupos de usuarios concretos). |
| `filter` | Es una especie de interruptor en la vista de búsqueda. Solo se puede habilitar o deshabilitar. Aplicará directamente un criterio establecido y mostrará los resultados directamente. Entre otros, puede tener los siguientes atributos: `string` (obligatorio, el texto que se mostrará), `domain` (crea el dominio de búsqueda para mostrar en pantalla), `date` (nombre de un campo tipo `date` o `datetime`. Crea un submenú con diversas opciones temporales), `context` (diccionario de Python que se mezcla con el dominio, para crear el dominio de búsqueda. Se utiliza mucho cuando queremos hacer una agrupación), `help` (tooltip de ayuda que se mostrará), `groups` (grupos que pueden utilizar el filtro). |
| `separator` | Sirve para separar grupos de filtros. |
| `group` | Sirve para separar grupos de filtros, más fácil de leer que el *separator*. |

**Ejemplo de vista de búsqueda**  

A continuación, puedes ver la vista de búsqueda (figura 2.36) y el código para la vista (figura 2.37) para la clase `manteni.workorder`.  

**Figura 2.36.** Vista de búsqueda de la clase `manteni.workorder`  

**Figura 2.37.** Código para la vista de búsqueda de la clase `manteni.workorder`  

**Otras vistas**  

Hay más tipos de vistas en Odoo, cuyas descripciones se pueden encontrar en la documentación oficial de Odoo:  

- `Activity`  
- `Cohort` (solo disponible en Odoo Enterprise)  
- `Dashboard` (solo disponible en Odoo Enterprise)  
- `Gantt` (solo disponible en Odoo Enterprise)  
- `Kanban`  
- `Map` (solo disponible en Odoo Enterprise)  
- `Pivot`  

#### 2.5.3. Acciones  

Las acciones definen el comportamiento del sistema en respuesta a una acción: login, pulsar un botón, seleccionar un valor... Para declarar una acción se tendrá que indicar el nombre y el tipo. Hay diversos **tipos.**  

| Tipo | Descripción |
| ---- | ----------- |
| `ir.actions.act_window` | Abrir una ventana. |
| `ir.actions.act_url` | Abrir un web. |
| `ir.actions.server` | Ejecutar un método en el servidor. |
| `ir.actions.report.xml` | Ejecutar un informe. |
| `ir.actions.client` | Ejecutar una acción implementada enteramente en el cliente. |
| `ir.cron` | Acciones ejecutadas automáticamente y periódicamente por el servidor. |

**Acciones "ir.actions.act_window"**  

La más común de las acciones sirve para abrir una ventana de visualización de un modelo mediante sus vistas. Definirá el conjunto de vistas que se pueden abrir (figura 2.38).  

Los **campos** (entre otros), son:  

| Campo | Descripción |
| ----- | ----------- |
| `res_model` | Clase de la que proviene la acción. |
| `view_mode` | Lista separada por comas de las vistas disponibles, poniendo como primera la que queremos que aparezca por defecto. |
| `context` (opcional) | Información adicional que pasamos a la vista. |
| `domain` (opcional) | Dominio de filtrado que pasamos a las vistas. |

**Figura 2.38.** Código para la acción de abrir la ventana de la clase `manteni.workorder`  

#### 2.5.4. Generación de menús  

Para generar un menú en un módulo de Odoo, utilizaremos la etiqueta **`<menuitem>`**, que llamará a una acción que llamará a las respectivas vistas.  

Los **valores específicos** de cada menú son:  

| Valor | Descripción |
| ----- | ----------- |
| `name` | Es el título del menú, es opcional; si no lo ponemos en el menú, tomará el nombre de la acción que ejecuta. |
| `id` | Contiene el identificador XML del menú; debe ser único dentro del módulo. |
| `action` | Identificador de la acción que ejecuta el menú. Si no especificamos la acción, el sistema entiende que se trata de un menú raíz y por tanto que contiene otros menús y/o opciones. El diseño de la correspondiente acción depende del tipo de ejecución que lleva asociada (abrir ventana, ejecutar informe, arrancar un asistente...). |
| `web_icon` | Icono que muestra el cliente web en la pantalla de instalación del módulo. |
| `parent` | Identificador del menú padre al que pertenece. Si no lo especificamos, el sistema entiende que se trata de un menú raíz (menú principal). |
| `groups` | Grupo de usuarios que pueden ver el menú. Si queremos especificar más de un grupo, hay que separarlos por comas (`groups = "admin, user"`). |

**Ejemplo de la generación de menús para el módulo `manteni`**  

```xml
<!-- Top menu item -->
<menuitem
    name="Maintenance"
    id="manteni.menu_root"
    web_icon="manteni,static/description/icon.png" groups="group_manteni_user"/>
<!-- menu categories -->
<menuitem name="Config" id="manteni.menu_3" parent="manteni.menu_root" sequence="4"
    groups="group_manteni_manager"/>
<!-- actions -->
<menuitem name="Workorders" id="manteni.menu_1a" parent="manteni.menu_root" sequence="1"
    action="manteni.workorder_action_window" groups="group_manteni_user"/>
<menuitem name="Calendar" id="manteni.menu_1b" parent="manteni.menu_root" sequence="3"
    action="manteni.workorder_calendar_action_window"
    groups="group_manteni_manager"/>
<menuitem name="Machine list" id="manteni.menu_2_1" parent="manteni.menu_3" sequence="5"
    action="manteni.machine_action_window"/>
<menuitem name="Program list" id="manteni.menu_2_2" parent="manteni.menu_3" sequence="6"
    action="manteni.program_action_window"/>
<menuitem id="res_partner_menu"
    parent="manteni.menu_3"
    action="action_machinery_seller_form"
    sequence="7" groups="group_manteni_manager"/>
```  

**Ejemplo de creación de las vistas de un módulo (vídeo)**  

Para describir con detalle la confección de las vistas de un módulo mediante un ejemplo diferente, puedes ver el siguiente vídeo.  

[Enlace al vídeo](https://player.vimeo.com/video/473780744)  

### 2.6. **El controlador en Odoo**

Odoo es un *software* muy maduro y que proporciona los métodos para, entre otros, crear, modificar y borrar registros. Aunque el lenguaje que hay debajo es Python, el desarrollador no debe obsesionarse con este lenguaje, ya que se parte de una gran base. La capa ORM de OpenObject facilita un conjunto de métodos que se encargan del mapeo entre los objetos Python y las tablas de PostgreSQL. Así, disponemos de métodos para crear, modificar, eliminar y buscar registros en la base de datos. Estos métodos son utilizados de manera automática por OpenObject en la ejecución de los diversos tipos de vista que OpenObject nos permite diseñar.  

En ocasiones, sin embargo, puede ser necesario **alterar la acción automática** de búsqueda--creación--modificación--eliminación facilitada por OpenObject y, entonces, tendremos que sobrescribir los correspondientes métodos en nuestras clases.  

Como ejemplo de esta necesidad, podemos considerar el caso de la gestión de recursos humanos (clase `hr.employee`) dentro del archivo `hr.py` del módulo `hr` de Odoo. Si le damos una mirada, al final de la clase encontramos el diseño, entre otros, de los métodos `unlink` (eliminar) y `write` (modificar). Cada uno de ellos ejecuta un conjunto de comprobaciones y/o acciones y, si todo es correcto, invoca la llamada de los correspondientes métodos `unlink`, `create` y `write` de la capa ORM. Así, el método `unlink` (eliminación de trabajadores) elimina también el registro de la clase `resource` asociado al trabajador antes de borrar el registro de su tabla.  

**Redefinición de los métodos `write` y `unlink` para la clase "hr.employee"**  

```python
def write(self, vals):
    if 'address_home_id' in vals:
        account_id = vals.get('bank_account_id') or self.bank_account_id.id
        if account_id:
            self.env['res.partner.bank'].browse(account_id).partner_id = vals['address_home_id']
    if vals.get('user_id'):
        vals.update(self._sync_user(self.env['res.users'].browse(vals['user_id'])))
    res = super(HrEmployeePrivate, self).write(vals)
    if vals.get('department_id') or vals.get('user_id'):
        department_id = vals['department_id'] if vals.get('department_id') else self[:1].department_id.id
        # When added to a department or changing user, subscribe to the channels auto-subscribed by department
        self.env['mail.channel'].sudo().search([
            ('subscription_department_ids', 'in', department_id)
        ])._subscribe_users()
    return res

def unlink(self):
    resources = self.mapped('resource_id')
    super(HrEmployeePrivate, self).unlink()
    return resources.unlink()
```  

#### 2.6.1. Métodos ORM más comunes  

**Método `create(vals_list)` → `records`.** Crea uno o varios registros para el objeto donde se define. Como parámetro de entrada se tendrá que poner un diccionario o una lista de diccionarios (si se quiere añadir más de un campo) con los valores que se quieren escribir.  

El **formato del diccionario** o lista de diccionarios debe ser el siguiente:  
`[{'field_name': field_value, ...}, ...]`  

**Método `write(vals)`.** Tomando un registro o conjunto de registros, modifica un campo o conjunto de campos con los valores introducidos. Si se trata de más de un registro, todos serán modificados con los mismos valores para los campos. Como parámetro de entrada se tendrá que poner un diccionario con los valores que se quieren modificar. El formato será `{'campo1': valor1, 'campo2': "valor2"}`, etc.  

**Método `browse([ids])` → `records`.** Usando como entrada un identificador o una lista de números identificadores, nos devuelve los registros de la clase que coinciden con este identificador.  

**Método `search(args[, offset=0][, limit=None][, order=None][, count=False])`.** Devuelve un subconjunto de registros coincidentes con los parámetros de la búsqueda. Puede tener los parámetros:  

| Parámetro | Descripción |
| --------- | ----------- |
| `args` | Un dominio de búsqueda. Si está vacío tomará todos los registros. |
| `offset` (int) | Número de resultados que debe ignorar. |
| `limit` (int) | Número de resultados máximo que debe dar (*default: all*). |
| `order` (str) | Texto para ordenar los resultados. |
| `count` (bool) | Si su valor es `True`, solo devuelve el número de resultados coincidentes (default: `False`). |

**Ejemplo del método `search`**  

Supongamos que queremos buscar todos los trabajadores de una empresa, contenidos en el objeto `company`. Podremos usar la expresión: `search([('company_id', '=', company.id)])`.  

Esta expresión puede encontrarse en el archivo `hr_employee.py` de la clase `hr_presence`.  

**Método `unlink()`.** Borra el registro o registros indicados.  

#### 2.6.2. Los decoradores  

Tal como ocurre en el modelo de Odoo con los campos calculados, a veces se tienen que desarrollar funciones para modificar o ampliar las funcionalidades de Odoo.  

Si revisamos el código fuente, encontraremos sentencias que comienzan con una "@" encima de estas funciones. Son los decoradores. Los decoradores permiten **modificar la manera de comportarse de una función** (figura 2.39).  

**Figura 2.39.** Decorador en la clase "hr_employee"  

Los decoradores más interesantes para el desarrollo de módulos en Odoo son:  

- `@api.depends`  
- `@api.constrains`  
- `@api.onchange`  

**`@api.depends`**  

Este decorador puede completar la función de un campo calculado, indicando cuándo se debe realizar este cálculo, es decir, de qué otros campos depende.  

Como ejemplo tenemos la función `_amount_all` del módulo de compras (código fuente: tinyurl.com/yce2vu4r). Para una compra, la función de actualización de las cantidades subtotal, total de impuestos y total solo se "dispara" cuando cambia el campo `price_total` de la clase `order_line`.  

Destacaremos también que `@api.depends` puede hacer depender una función de un campo que pertenece a una clase diferente de la en la que está la función.  

**Uso del decorador `@api.depends`**  

```python
@api.depends('order_line.price_total')
def _amount_all(self):
    for order in self:
        amount_untaxed = amount_tax = 0.0
        for line in order.order_line:
            amount_untaxed += line.price_subtotal
            amount_tax += line.price_tax
        order.update({
            'amount_untaxed': order.currency_id.round(amount_untaxed),
            'amount_tax': order.currency_id.round(amount_tax),
            'amount_total': amount_untaxed + amount_tax,
        })
```  

**`@api.constrains`**  

Este decorador sirve para verificar ciertas condiciones antes de guardar un registro en la base de datos.  

En la clase `Contract` del módulo de Recursos Humanos (código fuente tinyurl.com/yck3mnbt) hay una función con este tipo de decorador. Antes de guardar un contrato hay que asegurarse de que la fecha de inicio no es más alta que la fecha de finalización. Para ello se genera esta función.  

```python
@api.constrains('date_start', 'date_end')
def _check_dates(self):
    if self.filtered(lambda c: c.date_end and c.date_start > c.date_end):
        raise ValidationError(_('Contract start date must be earlier than contract end date.'))
```  

**`@api.onchange`**  

A veces puede resultarnos útil cambiar un valor antes de manera inmediata, dependiendo del valor que ha tomado otro campo de la misma clase, para ello utilizamos las funciones `onchange`.  

Los campos calculados, definidos anteriormente, no necesitan una función `onchange`, ya que se actualizan automáticamente. Esto es una novedad respecto a versiones anteriores.  

Para la clase `manteni.workorder` hay dos funciones de este tipo. La primera actualiza la fecha de finalización de la orden de trabajo si se elige el estado `closed` en la fecha actual. La segunda busca el identificador de usuario de un trabajador cuando cambiamos el empleado que llevará a cabo la orden de trabajo.  

```python
@api.onchange('state')
def _onchange_state(self):
    if self.state == 'closed':
        self.date_end=date.today()

@api.onchange('employee_id')
def _onchange_employee_id(self):
    self.employee_user_id=self.employee_id.resource_id.user_id
```  

**Ejemplo de trabajo con el controlador de un módulo (vídeo)**  

Para describir con detalle la creación de funciones y la modificación del controlador en Odoo mediante un ejemplo diferente puedes ver este vídeo.  

[Enlace al vídeo](https://player.vimeo.com/video/473779714)
