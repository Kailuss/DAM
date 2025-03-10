---
number headings: first-level 1, max 3, skip ^skipped, _.1.1.
banner: "![[../../../_Media/Banners/vecteezy_yellow-and-white-background-with-a-wave-pattern-the-yellow_53887306.jpg]]"
banner_y: 0.48
cssclasses:
  - table-clean
---

# **TEMA 3.1.** PostgreSQL
## 1. Gestión de privilegios en las BBDD de PostgreSQL

Un punto muy importante a tener en cuenta en la gestión de privilegios de PostgreSQL es conocer los privilegios existentes, de forma automática, después de la creación de una base de datos. Es importante saber que:

- La base de datos se crea con ACL (Access Control List) no definida, lo que permite que cualquier usuario del servidor PostgreSQL pueda abrir sesión en esa base de datos.
- PostgreSQL facilita el rol **public** que engloba a todos los usuarios de forma automática.
- PostgreSQL facilita, a todas las bases de datos, el esquema **public**, propiedad del usuario que ha creado la base de datos, y con privilegios de utilización del esquema (usage) y creación de objetos (create) al rol **public** (es decir, a cualquier usuario). Así, si observamos la propiedad ACL del esquema public de una base de datos creada por el usuario user1, veiem el valor {user1=UC/user1, =UC/user1} que hem de llegir com: l’usuari user1 té privilegis UC (usage+create) i el rol public (no apareix a l’esquerra del símbol =) té privilegis UC (usage+create) i que en ambdós casos han estat concedits per l’usuari user1 (valor que apareix després del símbol /).

## 2. El cliente psql

Para conectarse con un servidor, se requiere, obviamente, un programa cliente. Con la distribución de PostgreSQL se incluye un cliente, **psql**, que permite la introducción interactiva de órdenes en modo texto.

Antes de intentar conectarnos con el servidor, debemos asegurarnos de que está funcionando y que admite conexiones, locales (el SGBD se está ejecutando en la misma máquina que intenta la conexión) o remotas.

La siguiente orden permite conocer las bases de datos residentes en el servidor:

```bash
usuario@localhost:~$ psql -l
```

Para hacer una conexión, se requieren los siguientes datos:

- **Servidor.** Si no se especifica, se utiliza **localhost.**
- **Usuario.** Si no se especifica, se utiliza el nombre de usuario Unix que ejecuta el **psql.**
- **Base de datos.**

Diferentes ejemplos de conexión:

```bash
usuario@localhost:~$ psql -d nombre_basedatos
usuario@localhost:~$ psql nombre_basedatos
usuario@localhost:~$ psql -d demo -U nombre_usuario
usuario@localhost:~$ psql demo nombre_usuario
usuario@localhost:~$ psql -h nombre_servidor.org -U nombre_usuario -d nombre_basedatos
```

A partir del fragmento anterior, el cliente **psql** mostrará algo similar a lo siguiente:

``` terminal
Welcome to psql, the PostgreSQL interactive terminal.

Type: \copyright for distribution terms
\h for help with SQL commands
\? for help on internal slash commands
\g or terminate with semicolon to execute query
\q to quit

nombre_basedatos=#
```

El símbolo `#` significa que **psql** está listo para leer la entrada del usuario. Las sentencias SQL se envían directamente al servidor para interpretarlas, las órdenes internas tienen la forma `\orden` y ofrecen opciones que no están incluidas en SQL y son interpretadas internamente por **psql.**

### 2.1. **Indicadores de estado**

Los indicadores de estado del **psql** son:

| Indicador | Significado                                             |
| --------- | ------------------------------------------------------- |
| =#        | Espera una nueva sentencia                              |
| \#        | La sentencia aún no se ha terminado con `;` o `\g`      |
| "#        | Hay una cadena en comillas dobles que no se ha cerrado  |
| '#        | Hay una cadena en comillas simples que no se ha cerrado |
| (#        | Hay un paréntesis que no se ha cerrado                  |

### 2.2. **Órdenes de consulta de información**

El cliente **psql** ofrece diversas alternativas para obtener información sobre la estructura de nuestra base de datos. Algunas órdenes de mucha utilidad son:

| Orden        | Descripción                                    |
| ------------ | ---------------------------------------------- |
| `\l`         | Lista las bases de datos                       |
| `\dt`        | Describe las tablas de la base de datos en uso |
| `\ds`        | Lista las secuencias                           |
| `\di`        | Lista los índices                              |
| `\dv`        | Lista las vistas                               |
| `\dp` o `\z` | Lista los privilegios sobre las tablas         |
| `\da`        | Lista las funciones de agregados               |
| `\df`        | Lista las funciones                            |
| `\i archivo` | Ejecuta las órdenes del archivo                |
| `\H`         | Cambia el modo de salida a HTML                |
| `\! orden`   | Ejecuta una orden del sistema operativo        |
| `\du`        | Lista todos los usuarios y sus privilegios     |

## 3. Usuarios, grupos y roles en PostgreSQL

### 3.1. **Usuarios**

Conceptualmente, los usuarios de la base de datos están totalmente separados de los usuarios del sistema de explotación (el sistema operativo sobre el que se ha instalado el servidor de base de datos). Se llamará **usuario** a las aplicaciones y personas de la organización que utilizan un conjunto de datos de la BD de la organización.

### 3.2. **Grupos**

Los grupos ya vienen predefinidos por el sistema, lo único que podemos hacer es asignar usuarios a los grupos que ya tienen unos ciertos permisos establecidos y no modificables. Los grupos más comunes que podemos encontrar en los SGBD más comercializados son:

- **Administrador de sistema.** Es el usuario que tiene acceso a todas las bases de datos y dispone de todos los recursos. Es el nivel más alto y más poderoso de todo el sistema.
- **Administrador de las bases de datos.** Es el usuario que tiene acceso a todos los recursos de una base de datos específica. Puede hacer modificaciones en todos los objetos de la base de datos específica.
- **Administrador de seguridad.** Tiene el poder de dar o restringir el acceso a cualquier usuario dentro del SGBD.
- **Operaciones de control.** Es el grupo de usuarios que tiene permitido hacer las copias de seguridad o las restauraciones del sistema.

### 3.3. **Los roles**

PostgreSQL administra los permisos de acceso a la base de datos utilizando el concepto de **roles.** Un rol puede ser entendido como un usuario de base de datos, o un grupo de usuarios, dependiendo de cómo se establezca este rol. Un rol puede ser propietario de los objetos de la base de datos (por ejemplo, tablas) y puede asignar privilegios de los objetos de los que es propietario a otros roles para controlar quién tiene acceso a esos objetos. Además, es posible la concesión de la pertenencia de un rol a otro rol, lo que permite a un miembro del rol utilizar los privilegios asignados a otro rol. Podemos ver, pues, que permite implementar el concepto de herencia de privilegios.

**Cualquier rol puede actuar como un usuario, grupo, o ambas cosas.**

Para determinar el conjunto de roles existentes, es necesario examinar el catálogo del sistema; en concreto, la tabla **pg_roles.**

```postgresql
nombre_basedatos =# SELECT rolname FROM pg_roles;
```

## 4. Autorizaciones: grupos y roles

Además de poder dar permisos de utilización de los diferentes recursos del sistema de manera individual a cada usuario, nuestro SGBD dispone de varias herramientas que permiten:

- Dar privilegios a un determinado rol al cual se asignarán los usuarios (todos los usuarios que ejerzan este rol heredarán los privilegios y permisos de este).
- Gestionar diversos grupos preestablecidos del SGBD.

Encontrarás SGBD que solo implementan una de las dos herramientas y otros que las implementan ambas. Ahora aprenderemos las diferencias entre ambas herramientas y cómo utilizarlas.

## 5. Creación de usuarios, grupos de usuarios y roles

Las instrucciones que pueden usarse para la creación de usuarios, grupos de usuarios y roles son las siguientes:

| Instrucción | Uso |
|-------------|-----|
| `CREATE USER` | Para la creación de usuarios |
| `ALTER USER` | Para modificar los atributos de los usuarios |
| `DROP USER` | Para dar de baja un usuario |
| `CREATE GROUP` | Para la creación de grupos de usuarios |
| `ALTER GROUP` | Para modificar los atributos del grupo |
| `DROP GROUP` | Para dar de baja un grupo |
| `CREATE ROLE` | Para la creación de roles |
| `ALTER ROLE` | Para modificar los atributos de un rol |
| `DROP ROLE` | Para dar de baja un rol |

**Nota.** Es importante diferenciar entre `CREATE USER`, que es una instrucción SQL, y `createuser`, que es una sentencia que se puede ejecutar desde el intérprete de comandos una vez se ha instalado PostgreSQL.

**Nota.** Es importante diferenciar entre `DROP USER`, que es una instrucción SQL, y `dropuser`, que es una sentencia que se puede ejecutar desde el intérprete de comandos una vez se ha instalado PostgreSQL.

## 6. Atributos de usuario

Algunos de los atributos que definen los privilegios de los usuarios, grupos de usuarios y de los roles en PostgreSQL son:

| Permiso | Significado | Instrucción |
|---------|-------------|-------------|
| `LOGIN` / `NOLOGIN` | Puede conectarse | `CREATE USER` / `CREATE ROLE` |
| `INHERIT` / `NOINHERIT` | Hereda permisos de los roles padres | `CREATE ROLE` |
| `SUPERUSER` | Superusuario | `CREATE ROLE` |
| `CREATEDB` / `NOCREATEDB` | Puede crear bases de datos | `CREATE USER` / `CREATE ROLE` |
| `CREATEUSER` / `NOCREATEUSER` | Puede crear roles | `CREATE USER` / `CREATE ROLE` |

> [!note] Nota
>  Es una buena práctica crear un rol que tenga los privilegios `CREATEDB` y `CREATEROLE`, pero que no sea un superusuario, y luego utilizar este rol para todas las tareas de bases de datos y otros roles. Este enfoque evita los peligros de operar como un superusuario para las tareas que realmente no lo requieren.

## 7. Contraseñas

Las contraseñas son útiles solo si el método de autenticación del cliente requiere que el usuario proporcione una contraseña cuando se conecta a la base de datos. Los métodos de autenticación MD5 permiten hacer un buen uso de las contraseñas. Las contraseñas de bases de datos son independientes de las contraseñas del sistema operativo.

```postgresql
nombre_basedatos=# CREATE ROLE nombre_del_rol PASSWORD 'la_contraseña';
```

## 8. Miembros de un rol

Los miembros de un rol pueden utilizar los privilegios de la función de dos maneras:

1. **SET ROLE.** Para convertirse temporalmente en ese nuevo grupo. En este estado, la sesión de base de datos tiene acceso a los privilegios de la función de grupo en lugar del rol asignado originalmente al inicio de sesión, y cualquier objeto de base de datos creado se considerará propiedad del grupo, no del rol de inicio de sesión.
2. **INHERIT.** Los miembros de un rol que pueden heredar pueden hacer uso de los privilegios de los roles de los que son miembros de manera automática, incluyendo los privilegios heredados por los roles.

## 9. Ejemplo de creación y uso de roles

```postgresql
nombre_basedatos=# CREATE ROLE usuario LOGIN INHERIT;
nombre_basedatos=# CREATE ROLE admin NOINHERIT;
nombre_basedatos=# CREATE ROLE gestor NOINHERIT;
nombre_basedatos=# GRANT admin TO usuario;
nombre_basedatos=# GRANT gestor TO admin;
```

Inmediatamente después de conectarnos a la base de datos con el rol **usuario**, podremos hacer uso de los privilegios concedidos directamente a **usuario**, además de los privilegios concedidos a **admin**, porque **usuario** "hereda" los privilegios de **admin.** En cambio, **admin** no hereda los privilegios de **gestor**, y en consecuencia tampoco **usuario.**

Si después hacemos:
```postgresql
nombre_basedatos=# SET ROLE admin;
```

Nuestra sesión tendría uso exclusivo de los privilegios concedidos a **admin**, pero no de los que hemos concedido a **usuario.**

Si ahora hacemos:

```postgresql
nombre_basedatos=# SET ROLE gestor;
```

La sesión tendrá uso exclusivo de los privilegios concedidos a **gestor**, pero ninguno de los que se conceden a **usuario** ni a **admin.**

El conjunto de privilegios originales se puede restaurar con cualquiera de estas acciones:

```postgresql
nombre_basedatos=# SET ROLE usuario;
nombre_basedatos=# SET ROLE NONE;
nombre_basedatos=# RESET ROLE;
```

## 10. Privilegios y permisos en PostgreSQL

Cuando se crea un objeto, este es asignado a un propietario. El propietario normalmente es el mismo usuario que ha ejecutado la orden de creación.

Para la mayoría de los objetos, el estado inicial es aquel en el que el propietario (o un superusuario) puede hacer algo con ese objeto. Para permitir que otros usuarios utilicen el objeto, es necesario otorgarle privilegios.

Existen diferentes privilegios.

### Privilegios sobre bases de datos ^skipped

En PostgreSQL hay tres tipos de privilegios sobre bases de datos:

| Privilegio | Uso |
|------------|-----|
| `CREATE`   | Permite crear nuevos esquemas en la base de datos. |
| `CONNECT`  | Permite al usuario conectarse a la base de datos especificada. Este privilegio se comprueba en el inicio de conexión (además de comprobar que no se infringe ninguna de las restricciones impuestas en el archivo de configuración `pg_hba.conf`). |
| `TEMPORARY` | Permite crear tablas temporales durante el uso de la base de datos especificada. |

```postgresql
GRANT { { CREATE | CONNECT | TEMPORARY | TEMP } [...] | ALL [ PRIVILEGES ] }
ON DATABASE nombre_basedatos [, ...]
TO { [ GROUP ] nombre_rol | PUBLIC } [, ...] [ WITH GRANT OPTION ]
```

Por otro lado, es importante recordar que una base de datos puede estar formada por diferentes esquemas. Así pues, se pueden otorgar privilegios sobre estos. Estos son:

| Privilegio | Uso |
|------------|-----|
| `SELECT`   | Permite seleccionar datos de una vista o tabla dada. |
| `INSERT`   | Permite insertar datos en una vista/tabla. |
| `UPDATE`   | Permite actualizar datos de una tabla o vista. |
| `DELETE`   | Permite eliminar datos de una tabla dada. |
| `ALL`      | Permite realizar las acciones anteriores sobre una tabla/vista en concreto. |
| `REFERENCES` | Permite referenciar mediante restricciones de clave foránea a una tabla de la cual el usuario no es propietario. |

```postgresql
GRANT { { SELECT | INSERT | UPDATE | REFERENCES } ( COLUMN [, ...] ) [...] | ALL [ PRIVILEGES ] ( COLUMN [, ...] ) }
ON [ TABLE ] nombre_tabla [...]
TO { [ GROUP ] nombre_rol | PUBLIC } [, ...] [ WITH GRANT OPTION ]
```

## 11. Privilegios de tablas

Los privilegios que se pueden dar sobre las tablas están relacionados con todas las acciones que se pueden realizar sobre las tablas y vistas, que son:

| Privilegio | Uso |
|------------|-----|
| `SELECT`   | Permite seleccionar datos de una vista o tabla dada. |
| `INSERT`   | Permite insertar datos en una vista/tabla. |
| `UPDATE`   | Permite actualizar datos de una tabla o vista. |
| `DELETE`   | Permite eliminar datos de una tabla dada. |
| `ALL`      | Permite realizar las acciones anteriores sobre una tabla/vista en concreto. |
| `REFERENCES` | Permite referenciar mediante restricciones de clave foránea a una tabla de la cual el usuario no es propietario. |

```postgresql
GRANT { { SELECT | INSERT | UPDATE | REFERENCES } ( COLUMN [, ...] ) [...] | ALL [ PRIVILEGES ] ( COLUMN [, ...] ) }
ON [ TABLE ] nombre_tabla [...]
TO { [ GROUP ] nombre_rol | PUBLIC } [, ...] [ WITH GRANT OPTION ]
```

## 12. Privilegios de objetos de bases de datos

Los objetos de una base de datos están formados por todas las estructuras que se pueden crear, que son:

- Bases de datos
- Espacio para tablas (tablespace)
- Tablas
- Índices
- Triggers (disparadores)

Quien tenga permiso sobre los objetos de la base de datos podrá crear estructuras de la base de datos.

```postgresql
GRANT { { SELECT | INSERT | UPDATE | DELETE | TRUNCATE | REFERENCES | TRIGGER } [...] | ALL [ PRIVILEGES ] }
ON { [ TABLE ] nombre_tabla [...] | ALL TABLES IN SCHEMA nombre_esquema [...] }
TO { [ GROUP ] nombre_rol | PUBLIC } [, ...] [ WITH GRANT OPTION ]
```

Especificar privilegios sobre espacios de tablas:

```postgresql
GRANT { CREATE | ALL [ PRIVILEGES ] }
ON TABLESPACE nombre_tablespace [...]
TO { [ GROUP ] nombre_rol | PUBLIC } [, ...] [ WITH GRANT OPTION ]
```

Especificar privilegios sobre secuencias:

```sql
GRANT { { USAGE | SELECT | UPDATE } [...] | ALL [ PRIVILEGES ] }
ON { SEQUENCE nombre_secuencia [...] | ALL SEQUENCES IN SCHEMA nombre_esquema [...] }
TO { [ GROUP ] nombre_rol | PUBLIC } [, ...] [ WITH GRANT OPTION ]
```

### 12.1. Retirar privilegios

Para retirar los privilegios concedidos anteriormente, tenemos la sentencia `REVOKE`. Se trata de formar las mismas órdenes que cuando damos un permiso, pero ahora cambiaremos la palabra `GRANT` por `REVOKE`. Si un objeto es eliminado de la base de datos, automáticamente también se pierden los privilegios sobre el objeto.

Debes estar muy atento cuando retires privilegios si estos han sido otorgados con `WITH GRANT OPTION`, ya que la retirada de un privilegio a un usuario que haya dado privilegios a otros usuarios implica que todos ellos pierdan el permiso para utilizar el recurso. Esto se conoce como retirada de permiso en cascada. Así pues, evita dar privilegios con la opción `WITH GRANT OPTION`.

Se debe hacer una última consideración respecto al hecho de crear exclusiones en grupos de usuarios a la hora de dar o quitar permisos. Imagina que quieres dar privilegios a todos los usuarios del SGBD excepto a uno (o unos cuantos). Una manera de hacerlo sería:

```sql
GRANT DELETE ON Libros TO PUBLIC;
REVOKE DELETE ON Libros FROM usuario;
```

Debes tener presente que este tipo de acciones no están permitidas en todos los SGBD. Así pues, deberás consultar el manual del sistema gestor para saber si es una forma viable de hacer exclusiones de grupos de usuarios o buscar formas alternativas de hacer este tipo de acciones.

## 13. Tipos de datos PostgreSQL

PostgreSQL incluye un conjunto importante de tipos de datos que se adaptan a muchas aplicaciones. Los usuarios también pueden definir sus propios tipos de datos. La mayoría de los tipos predefinidos de datos tienen nombres y semántica bastante obvia. Algunos de los tipos de datos utilizados con frecuencia son `integer` para números enteros, `numeric` para números reales, `text` para cadenas de caracteres, `date` para fechas, `time` para valores de tiempo del día, y `timestamp` para valores que contienen la fecha y la hora.

### 13.1. Tipos lógicos ^skipped

PostgreSQL incorpora el tipo lógico `boolean`, también llamado `bool`. Ocupa un byte de espacio de almacenamiento y puede almacenar los valores `falso` y `verdadero`.

| Valor | Nombre |
|-------|--------|
| Falso | `false`, `'f'`, `'n'`, `'no'`, `0` |
| Verdadero | `true`, `'t'`, `'y'`, `'yes'`, `1` |

PostgreSQL soporta los operadores lógicos siguientes: `AND`, `OR` y `NOT`.

Aunque los operadores de comparación se aplican sobre prácticamente todos los tipos de datos proporcionados por PostgreSQL, dado que su resultado es un valor lógico, describiremos su comportamiento a continuación:

| Operador | Descripción |
|----------|-------------|
| `>`      | Mayor que |
| `<`      | Menor que |
| `<=`     | Menor o igual que |
| `>=`     | Mayor o igual que |

## 14. Tipos numéricos

PostgreSQL dispone de los tipos enteros `smallint`, `int` y `bigint`, que se comportan como lo hacen los enteros en muchos lenguajes de programación.

Los números con punto flotante, de los tipos `real` y `double precision`, almacenan cantidades con decimales. Una característica de los números de punto flotant