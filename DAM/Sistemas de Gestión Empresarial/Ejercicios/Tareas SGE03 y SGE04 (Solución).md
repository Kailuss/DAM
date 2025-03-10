---
number headings: off
---

# Tareas SGE03 y SGE04 (Solución)

Para resolver la tarea SGE 03-04, se deben seguir los pasos detallados en el enunciado. A continuación, se presenta una guía paso a paso para cada apartado:

## Apartado A. Odoo a través de pgAdmin y psql

### A1. **Instalación de pgAdmin y psql**
1. **Instalar PostgreSQL** en la máquina anfitriona (Windows, macOS o Linux). Durante la instalación, selecciona las herramientas **pgAdmin** y **psql**.
2. Verifica la instalación:
   - Abre **pgAdmin** desde el menú de aplicaciones.
   - Abre una terminal y ejecuta `psql --version` para confirmar que **psql** está instalado.

### A2. **Conexión con la base de datos de Odoo**
1. **Conectar con la base de datos de Odoo.**
   - En **pgAdmin**, crea una nueva conexión:
	 - Host: IP de la máquina virtual Ubuntu Server.
	 - Puerto: 5432 (por defecto para PostgreSQL).
	 - Usuario: `odoo` (o el usuario configurado en Odoo).
	 - Contraseña: La contraseña configurada.
   - En **psql**, usa el siguiente comando:

	 ```bash
     psql -h <IP_Ubuntu_Server> -U odoo -d <nombre_base_datos>
     ```

2. **Listar nombres de empleados.**
   - En **psql.**

	 ```sql
     SELECT name FROM hr_employee;
     ```

   - En **pgAdmin**, ejecuta la misma consulta en la herramienta de consultas.

### A3. **Instalación del módulo flota (fleet) y consultas**
1. **Instalar el módulo flota.**
   - En Odoo, ve a **Apps** y busca "Fleet". Instala el módulo.
2. **Realizar consultas.**
   - a) Empleados con al menos una "s" en el nombre:

	 ```sql
     SELECT name FROM hr_employee WHERE name LIKE '%s%';
     ```

   - b) Número de coches:

	 ```sql
     SELECT COUNT(*) FROM fleet_vehicle;
     ```

   - c) Coches con más de 3 puertas:

	 ```sql
     SELECT COUNT(*) FROM fleet_vehicle WHERE doors > 3;
     ```

   - d) Número promedio de puertas:

	 ```sql
     SELECT AVG(doors) FROM fleet_vehicle;
     ```

### A4. **Explicación de sentencias SQL**
1. `GRANT ALL on table public.hr_employee to odoo;`  
   Otorga todos los privilegios (SELECT, INSERT, UPDATE, DELETE, etc.) sobre la tabla `hr_employee` al usuario `odoo`.

2. `REVOKE EXECUTION on function myfunc FROM g1;`  
   Revoca el permiso de ejecutar la función `myfunc` al grupo `g1`.

3. `REVOKE SELECT on table public.fleet FROM james;`  
   Revoca el permiso de SELECT sobre la tabla `fleet` al usuario `james`.

4. `CREATE ROLE test;`  
   Crea un nuevo rol llamado `test`.

5. `GRANT CREATE TABLE to test;`  
   Otorga al rol `test` el privilegio de crear tablas.

6. `GRANT test TO user1;`  
   Asigna el rol `test` al usuario `user1`.

7. `REVOKE CREATE TABLE FROM test;`  
   Revoca el privilegio de crear tablas al rol `test`.

8. `DROP ROLE test;`  
   Elimina el rol `test`.

9. `GRANT SELECT(name, job_title), UPDATE(name, age) ON public.hr_employee TO odoo WITH GRANT OPTION;`  
   Otorga al usuario `odoo` permisos de SELECT sobre `name` y `job_title`, y de UPDATE sobre `name` y `age`, con la opción de otorgar estos permisos a otros usuarios.

### A5. **Creación de roles y usuarios en pgAdmin**
1. **Crear rol `r_empl`.**

   ```sql
   CREATE ROLE r_empl;
   GRANT SELECT(name, job_title) ON hr_employee TO r_empl;
   ```

2. **Crear rol `rw_empl`.**

   ```sql
   CREATE ROLE rw_empl;
   GRANT SELECT, UPDATE(name, job_title) ON hr_employee TO rw_empl WITH GRANT OPTION;
   ```

3. **Crear usuarios `usu1` y `usu2`.**

   ```sql
   CREATE USER usu1 WITH PASSWORD 'password1' VALID UNTIL '2024-03-31';
   CREATE USER usu2 WITH PASSWORD 'password2' VALID UNTIL '2024-03-31';
   GRANT r_empl TO usu1;
   GRANT rw_empl TO usu2;
   ```

4. **Verificar privilegios.**
   - En **psql**, usa `\dp hr_employee`.
   - En **pgAdmin**, revisa los privilegios en la pestaña "Privileges" de la tabla `hr_employee`.

### A6. **Explicación de privilegios**
1. `{odoo=UC/postgres, =UC/postgres, rrhh_dep=rwx/postgres}`  
   - `odoo` tiene permisos de USAGE y CREATE.
   - El rol público (`=`) tiene permisos de USAGE y CREATE.
   - El rol `rrhh_dep` tiene permisos de lectura, escritura y ejecución.

2. `{g1=r/postgres, g2=rw/postgres, g3=arw/postgres, g4=arwdDxt/postgres}`  
   - `g1` tiene permiso de lectura.
   - `g2` tiene permisos de lectura y escritura.
   - `g3` tiene permisos de inserción, lectura y escritura.
   - `g4` tiene todos los permisos (inserción, lectura, escritura, eliminación, etc.).

3. `{}`  
   No hay privilegios asignados.

4. `{usu1=a/postgres, usu2=r/postgres, usu3=r*Dd*t/toni}`  
   - `usu1` tiene permiso de inserción.
   - `usu2` tiene permiso de lectura.
   - `usu3` tiene permisos de lectura, eliminación y ejecución.

### A7. **Uso de psycopg2 en Python**
1. **Instalar psycopg2.**

   ```bash
   pip install psycopg2
   ```

2. **Conectar a la base de datos.**

   ```python
   import psycopg2
   conn = psycopg2.connect(
       dbname="<nombre_bd>",
       user="odoo",
       password="<contraseña>",
       host="<IP_Ubuntu_Server>"
   )
   cursor = conn.cursor()
   ```

3. **Dibujar histograma.**
   - Consulta los productos y categorías.
   - Usa `matplotlib` para crear el histograma.

### A8. **Instalación de PyCharm o Visual Studio**
1. **Instalar PyCharm Pro** o **Visual Studio** en la máquina anfitriona.
2. **Acceder a la carpeta `addons` de Odoo.**
   - Usa una conexión SSH o comparte carpetas entre la máquina virtual y la anfitriona.
3. **Sigue el vídeo** para instalar el módulo plantilla.

## Formato de entrega
- Guarda el documento en formato PDF.
- Nombra el archivo siguiendo el formato indicado:  
  `apellido1_apellido2_nombre_SGE03_Tarea.pdf`.
