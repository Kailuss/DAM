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

# Tareas SGE03 y SGE04

[Tarea SGE03 y SGE04 (Solución)](Tarea%20SGE03%20y%20SGE04%20(Solución).md)

> [!summary] 
> **Curso.** 2º Grupo S2PD  
**Ciclo.** CFGS en Desarrollo de Aplicaciones Multiplataforma (DAM) - modalidad a distancia  
**Módulo.** Sistemas de Gestión Empresarial (modalidad a distancia) 

## 1. Enunciado

Esta tarea trata de conocer la base de datos del ERP escogido para estudiar: **Odoo.** La base de datos que se utiliza en Odoo es **PostgreSQL.** Para poder realizar acciones directamente en la base de datos, se pueden usar diferentes programas, por ejemplo **PgAdmin IV** (interfaz gráfica) o **psql** (línea de comandos). Además, se pueden utilizar otros programas compatibles con bases de datos **PostgreSQL** como **DBeaver** o **DataGrip**, y conectar con la base de datos utilizando conectores.  

Por ejemplo, si utilizamos el lenguaje de programación **Python**, podemos utilizar la librería **psycopg2** para conectar con la base de datos **PostgreSQL.** En esta práctica conectaremos con la base de datos y gestionaremos los usuarios y sus privilegios mediante el sublenguaje **DCL** de SQL y las herramientas gráficas que nos proporcionan los clientes de acceso a la base de datos. Finalmente, se realizará una instalación de un **IDE** como **Microsoft Visual Studio** o **PyCharm Pro** para instalar un módulo “plantilla” en Odoo.

### Apartado A. Odoo a través de pgAdmin y psql

1. **Instala** pgAdmin y psql en tu máquina anfitriona (puedes optar por realizar la instalación de un servidor PostgreSQL que incluye ambas herramientas).

2. **Conecta con la BBDD** de Odoo generada en el servidor PostgreSQL de la máquina virtual Ubuntu Server instalada en la tarea 2.  
   - Accede a la base de datos de Odoo y lista los nombres de los empleados.  
   - Realiza esta acción mediante psql y utilizando pgAdmin, por separado.  
   - Para ello, instala previamente el módulo de empleados en Odoo y utiliza una base de datos de empresa con datos de ejemplo.

3. **Instala el módulo flota (fleet)** y realiza consultas en la base de datos de Odoo mediante psql (desde la máquina anfitriona):  
   - a) Busca todos los empleados cuyo nombre tenga al menos una "s".  
   - b) Cuenta el número de coches de la empresa.  
   - c) Cuenta los coches que tengan más de 3 puertas.  
   - d) Cuenta el número de puertas promedio de los coches.

4. **Explica el significado** de las siguientes sentencias SQL:  
   - `GRANT ALL on table public.hr_employee to odoo;`  
   - `REVOKE EXECUTION on function myfunc FROM g1;`  
   - `REVOKE SELECT on table public.fleet FROM james;`  
   - `CREATE ROLE test;`  
   - `GRANT CREATE TABLE to test;`  
   - `GRANT test TO user1;`  
   - `REVOKE CREATE TABLE FROM test;`  
   - `DROP ROLE test;`  
   - `GRANT SELECT(name, job_title), UPDATE(name, age) ON public.hr_employee TO odoo WITH GRANT OPTION;`  

5. **Usando pgAdmin**, dentro de la base de datos de Odoo:  
   - a) Genera un rol `r_empl` y asigna privilegios de lectura a los campos `name` y `job_title` de la tabla `hr_employee`.  
   - b) Genera otro rol `rw_empl` con permisos de lectura y modificación sobre `name` y `job_title`, y con derecho a otorgar estos privilegios a otros usuarios.  
   - c) Genera dos usuarios `usu1` y `usu2` con contraseña que caduque el 31 de marzo de 2024 y asigna cada usuario a uno de los roles creados.  
   - d) Verifica los privilegios asignados mediante psql (`\dp hr_employee`) y con pgAdmin.

6. **Explica el significado** de los siguientes privilegios en la tabla `hr_employee` de Odoo vistos en pgAdmin. Escribe la sentencia SQL para otorgar estos privilegios:  
   - `{odoo=UC/postgres, =UC/postgres, rrhh_dep=rwx/postgres}`  
   - `{g1=r/postgres, g2=rw/postgres, g3=arw/postgres, g4=arwdDxt/postgres}`  
   - `{}`  
   - `{usu1=a/postgres, usu2=r/postgres, usu3=r*Dd*t/toni}`  

7. **Usa psycopg2** para conectar con la base de datos de Odoo utilizando **Python.**  
   - Dibuja un **histograma** de los productos del módulo de comedor (número de productos por categoría y histograma de precios).  
   - Puedes usar los siguientes ejemplos de referencia:  
	 - [Ejemplo 1](https://sites.google.com/paucasesnovescifp.cat/sge-dam-2122/p%C3%A0gina-principal/sql-to-dataframe)  
	 - [Ejemplo 2](https://github.com/tonibois/SQL_through_python/blob/main/PostgreSQL_from_python.ipynb)  

8. **Instala PyCharm Pro o Microsoft Visual Studio** en la máquina anfitriona.  
   - Accede a la carpeta **addons** de Odoo instalada en la máquina virtual Ubuntu Server.  
   - Sigue los pasos del vídeo para instalar el módulo plantilla.  
   - [Vídeo](https://www.youtube.com/watch?v=6VsatsosCDI)  

## 2. Criterios de puntuación (Total 10 puntos)

- **A1.** 1 punto  
- **A2.** 1 punto  
- **A3.** 1 punto  
- **A4.** 1 punto  
- **A5.** 1 punto  
- **A6.** 1 punto  
- **A7.** 2 puntos  
- **A8.** 2 puntos  

Un formato deficiente de la práctica puede descontar 1 punto en la nota final.

## 3. Indicaciones de entrega

Una vez realizada la tarea, se elaborará un único documento con las respuestas correspondientes.  

- **Formato de nombre del archivo.**  
  `apellido1_apellido2_nombre_SIGxx_Tarea`  
- No usar la letra "ñ", tildes ni caracteres especiales.  

**Ejemplo de nombre correcto.**  
Para la alumna **Begoña Sánchez Mañas**, la tarea de la unidad 2 del módulo **SI** se llamaría:  

`sanchez_manas_begona_SI02_Tarea`
