---
tags: [DAM, SGE]
cssclasses:
  - dam-sge
  - table-clean
banner: "![[sge.jpg]]"
number headings: off
---

# Examen SGE

## Instalación y configuración de Odoo en Linux Server  

1. **PostgreSQL**  

   ```bash
   # Instalar PostgreSQL (gestor de bases de datos)
   sudo apt install postgresql -y
   
   # Crear un superusuario con los mismos permisos que el usuario actual
   sudo -u postgres createuser -s $USER
   
   # Iniciar el servicio de PostgreSQL
   sudo service postgresql start
   ```

2. **Dependencias**  

   ```bash
   # Instalar Git para control de versiones
   sudo apt install git
   
   # Instalar herramientas de desarrollo para Python 3
   sudo apt install python3-dev python3-pip python3-wheel python3-venv
   
   # Instalar librerías necesarias para compilación y conexión con PostgreSQL
   sudo apt install build-essential libpq-dev libxslt-dev libzip-dev libldap2-dev libsasl2-dev libssl-dev
   ```

3. **Clonar repositorio de Odoo**  

   ```bash
   # Descargar solo la rama 18.0 de Odoo (último commit, sin historial completo)
   git clone https://github.com/odoo/odoo.git -b 18.0 --depth=1
   ```

4. **Entorno virtual**  

   ```bash
   # Crear un entorno virtual de Python en la ruta especificada
   python3 -m venv ~/odoo18/env18
   
   # Activar el entorno virtual
   source ~/odoo18/env18/bin/activate
   
   # Actualizar pip (gestor de paquetes de Python)
   pip install -U pip
   
   # Instalar dependencias listadas en requirements.txt
   pip install -r ~/odoo18/odoo/requirements.txt
   
   # Instalar Odoo en modo editable (-e permite modificar el código sin reinstalar)
   pip install -e ~/odoo15/odoo
   ```

5. **Alias y ejecución**  

   ```bash
   # Editar el archivo de configuración de bash
   nano ~/.bashrc
   
   # Añadir alias para ejecutar Odoo directamente desde cualquier ubicación
   alias odoo='~/odoo18/env18/bin/python ~/odoo18/odoo/odoo-bin'
   
   # Recargar la configuración de bash
   source ~/.bashrc
   
   # Programar Odoo para que se ejecute al iniciar el sistema (usando crontab)
   crontab -e
   @reboot ~/odoo18/env18/bin/python ~/odoo18/odoo/odoo-bin
   ```

## Comandos SQL y PSQL  

1. **Conexión y consultas básicas**  

   ```sql
   -- Conectarse a la base de datos (PowerShell/psql)
   .\psql -h ip -U mpc -d mpcdb
   
   -- Desconectarse
   .\q
   
   -- Buscar empleados cuyo nombre contenga la letra "s"
   SELECT name FROM hr_employee WHERE name LIKE '%s%';
   
   -- Contar vehículos con más de 3 puertas
   SELECT COUNT(*) FROM fleet_vehicle WHERE doors > 3;
   
   -- Calcular promedio de puertas en vehículos
   SELECT AVG(doors) FROM fleet_vehicle;
   ```

2. **Permisos de usuario**  

   ```sql
   -- Crear usuario con contraseña y fecha de caducidad
   CREATE USER Juan WITH PASSWORD 'Juanito69' VALID UNTIL '2025-03-31';
   
   -- Dar todos los permisos sobre la tabla hr_employee al usuario ODOO
   GRANT ALL ON TABLE public.hr_employee TO ODOO;
   
   -- Revocar permiso de ejecución de una función al usuario g1
   REVOKE EXECUTION ON FUNCTION myfunc FROM g1;
   
   -- Revocar permiso de lectura sobre la tabla fleet al usuario James
   REVOKE SELECT ON TABLE public.fleet FROM James;
   ```

3. **Roles**  

   ```sql
   -- Crear un rol llamado 'test'
   CREATE ROLE test;
   
   -- Dar permiso para crear tablas al rol 'test'
   GRANT CREATE TABLE TO test;
   
   -- Asignar el rol 'test' al usuario 'Juan'
   GRANT test TO Juan;
   
   -- Revocar permiso de crear tablas al rol 'test'
   REVOKE CREATE TABLE FROM test;
   
   -- Eliminar el rol 'test'
   DROP ROLE test;
   
   -- Otorgar permisos específicos con capacidad de delegación
   GRANT SELECT (name, job_title), UPDATE (name, age) ON public.hr_employee TO Juan WITH GRANT OPTION;
   ```

4. **Lectura de privilegios**  

   ```sql
   -- Mostrar privilegios de una tabla específica
   \dp public.hr_employee
   
   -- Listar usuarios y roles
   \du
   
   -- Listar tablas disponibles
   \dt
   
   -- Mostrar estructura de una tabla
   \d nombre_tabla
   
   -- Listar funciones almacenadas
   \df
   
   -- Ver información de conexión actual
   \conninfo
   ```

5. **Ejemplos avanzados de permisos**  

   ```sql
   -- Permitir a Odoo usar y crear objetos en el esquema público
   GRANT USAGE, CREATE ON SCHEMA public TO odoo;
   
   -- Permitir a todos los usuarios (PUBLIC) usar y crear en esquema público
   GRANT USAGE, CREATE ON SCHEMA public TO PUBLIC;
   
   -- Dar permisos de lectura, actualización e inserción al grupo RRHH
   GRANT SELECT, UPDATE, INSERT ON hr_employee TO rrhh_dep;
   ```

## Conexión a PostgreSQL y visualización de datos  

1. **Instalación**  

   ```bash
   # Instalar librerías para conexión a PostgreSQL y visualización de datos
   pip install psycopg2 psycopg2-binary pandas matplotlib
   ```

2. **Script completo**  

   ```python
   import psycopg2  # Librería para conexión con PostgreSQL
   import pandas as pd  # Manipulación de datos en formato tabular
   import matplotlib.pyplot as plt  # Generación de gráficos

   # Establecer conexión con la base de datos
   conn = psycopg2.connect(
       host="192.168.1.147",  # Dirección del servidor
       database="mpcdb",       # Nombre de la base de datos
       user="mpc",             # Usuario
       password="admin"        # Contraseña
   )
   cur = conn.cursor()  # Crear cursor para ejecutar consultas

   # Consulta 1: Productos por categoría
   cur.execute("""
       SELECT c.name AS category_name, COUNT(p.id) AS num_products
       FROM lunch_product p
       JOIN lunch_product_category c ON p.category_id = c.id
       GROUP BY c.name
       ORDER BY num_products DESC;
   """)
   
   # Convertir resultados a DataFrame de pandas
   df = pd.DataFrame(cur.fetchall(), columns=['category_name', 'num_products'])
   
   # Limpiar nombres de categorías (eliminar formato diccionario)
   df['category_name'] = df['category_name'].apply(
       lambda x: x.get('es_AR', 'Desconocido') if isinstance(x, dict) else x
   )

   # Configurar gráfico de barras
   plt.figure(figsize=[12,6])
   plt.bar(
       df['category_name'], 
       df['num_products'], 
       color='skyblue', 
       edgecolor='black'
   )
   plt.xlabel('Categoría de Producto', fontsize=12)
   plt.ylabel('Número de Productos', fontsize=12)
   plt.title('Cantidad de productos por categoria', fontsize=14)
   plt.xticks(rotation=45, ha='right')  # Rotar etiquetas para mejor legibilidad
   plt.grid(axis='y', linestyle='--', alpha=0.7)  # Líneas de guía horizontales
   plt.show()

   # Consulta 2: Histograma de precios
   cur.execute("SELECT price FROM lunch_product WHERE price IS NOT NULL;")
   df_precios = pd.DataFrame(cur.fetchall(), columns=['price'])
   df_precios['price'] = df_precios['price'].astype(float)  # Convertir a numérico

   # Configurar histograma
   plt.figure(figsize=[12, 6])
   plt.hist(
       df_precios['price'], 
       bins=30,                  # Número de intervalos
       color='orange', 
       edgecolor='black', 
       alpha=0.7                # Transparencia
   )
   plt.xlabel('Precio del Producto', fontsize=12)
   plt.ylabel('Cantidad de Productos', fontsize=12)
   plt.title('Histograma de Precios', fontsize=14)
   plt.grid(axis='y', linestyle='--', alpha=0.7)
   plt.show()

   conn.close()  # Cerrar conexión con la base de datos
   ```

## Desarrollo de módulos en Odoo  

1. **Configuración inicial**  

   ```bash
   # Navegar al directorio de Odoo
   cd /home/mpc/odoo18
   
   # Ejecutar Odoo con archivo de configuración específico
   ./env18/bin/python ~odoo18/odoo/odoo-bin -c odoo.conf -d mpcdb
   
   # Crear estructura básica de un módulo llamado "mpc2425"
   ./odoo-bin scaffold mpc2425 custom_addons
   
   # Dar permisos completos al directorio de Odoo
   sudo chmod -R 777 odoo
   ```

2. **Estructura del módulo**  

	```
	my_module
	├── __init__.py
	├── __manifest__.py
	├── controllers
	│   ├── __init__.py
	│   └── controllers.py
	├── demo
	│   └── demo.xml
	├── models
	│   ├── __init__.py
	│   └── models.py
	├── security
	│   └── ir.model.access.csv
	└── views
	    ├── templates.xml
	    └── views.xml
	```

   - **Modelo (`models.py`)**  

	 ```python
     from odoo import models, fields, api

     class Student(models.Model):
         _name = 'mpc2425.student'  # Nombre técnico del modelo
         _description = 'Student'    # Descripción legible

         # Campos del modelo:
         name = fields.Char(string="Name", required=True)  # Texto obligatorio
         active = fields.Boolean(string="Active", default=True)  # Activo/inactivo
         date = fields.Datetime(string='Session Date', required=True)  # Fecha/hora
         duration = fields.Float(string='Duration (hours)', required=True)  # Número decimal
         
         # Campo de selección (opciones predefinidas)
         level = fields.Selection(
             selection=[
                 ('primary', 'Primary School'),
                 ('secondary', 'Secondary School')
             ],
             string='Level', 
             required=True,
             help="Education level of the student"  # Texto de ayuda
         )
         
         # Relación muchos-a-muchos con el modelo 'mpc2425.tutor'
         tutor_id = fields.Many2many(
             comodel_name='mpc2425.tutor',
             string='Tutors', 
             required=True,
             relation='tutoring_session_tutor_rel',  # Nombre de tabla intermedia
             column1='student_id',                   # Columna para este modelo
             column2='tutor_id'                      # Columna para el modelo relacionado
         )
         
         # Campo calculado automáticamente
         total_price = fields.Float(
             string="Total Price",
             compute="_compute_total_price",  # Función de cálculo
             store=True,                     # Almacenado en BD
             help='Total price of the tutoring session'
         )

         # Método para calcular el precio total
         @api.depends('duration', 'price_per_hour')  # Se ejecuta al cambiar estos campos
         def _compute_total_price(self):
             for rec in self:  # Recorre todos los registros
                 rec.total_price = rec.duration * rec.price_per_hour
     ```

   - **Vista (`tutor_views.xml`)**  

	 ```xml
     <odoo>
         <!-- Definición de vista de árbol (lista) -->
         <record id="view_tutor_tree" model="ir.ui.view">
             <field name="name">mpc2425.tutor.tree</field>  # Identificador
             <field name="model">mpc2425.tutor</field>      # Modelo asociado
             <field name="arch" type="xml">
                 <tree string="Tutors">                     # Tipo de vista
                     <field name="name"/>                   # Campos a mostrar
                     <field name="active"/>
                 </tree>
             </field>
         </record>

         <!-- Acción para abrir la vista -->
         <record id="action_tutor" model="ir.actions.act_window">
             <field name="name">Tutors</field>              # Nombre visible
             <field name="res_model">mpc2425.tutor</field>  # Modelo objetivo
             <field name="view_mode">tree,form</field>      # Vistas disponibles
         </record>

         <!-- Elemento de menú que dispara la acción -->
         <menuitem id="menu_tutor" name="Tutors" action="action_tutor" sequence="10"/>
     </odoo>
     ```

   - **Manifest (`__manifest__.py`)**  

	 ```python
     {
         'name': "mpc2425",                     # Nombre visible del módulo
         'summary': "Módulo de tutorías",       # Descripción corta
         'author': "Macia PC",                  # Autor
         'version': '1.0',                      # Versión semántica
         'depends': ['base', 'hr'],             # Módulos requeridos
         'data': [                             # Archivos a cargar
             'security/tutoring_security.xml',  # Configuración de seguridad
             'security/ir.model.access.csv',    # Permisos de acceso
             'views/tutor_views.xml',          # Definición de vistas
             'views/menu.xml',                 # Estructura de menú
         ],
         'application': True,                  # Es una aplicación (no módulo técnico)
     }
     ```

3. **Seguridad**  
   - **Grupos (`tutoring_security.xml`)**  

	 ```xml
     <odoo>
         <data noupdate="1">  # No actualizar si ya existe
             <!-- Definir grupo de seguridad -->
             <record id="group_tutor_user" model="res.groups">
                 <field name="name">Tutor User</field>  # Nombre visible
                 <field name="category_id" ref="base.group_user"/>  # Categoría
             </record>
         </data>
     </odoo>
     ```

   - **Permisos (`ir.model.access.csv`)**  

	 ```
     # Estructura: ID, Nombre, Modelo, Grupo, Lectura, Escritura, Creación, Eliminación
     access_tutor_tutoring_session,access_tutor_tutoring_session,model_mpc2425_tutoring_session,mpc2425.group_tutor_user,1,1,1,1
     ```
