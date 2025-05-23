---
tags:
- DAM
- SGE
cssclasses:
- dam-sge
- table-clean
banner: "![[sge.jpg]]"
---

# **TEMA 5.** <br>Desarrollo de componentes
| Anexos |
| - |
| [Tarea SGE05](../Práctica/Tareas/Tarea%20SGE05.md) |

## 1. Técnicas y estándares. <br>Modelo-Vista-Controlador

El Modelo-Vista-Controlador (MVC) divide una aplicación en tres componentes:

- **Modelo.** Los datos de la aplicación.
- **Vista.** La interfaz de usuario.
- **Controlador.** Define cómo la interfaz reacciona a las entradas del usuario.

Esta separación permite modificar la interfaz sin afectar los datos y viceversa.

En OpenERP, el MVC se implementa así:

- **Modelo.** Tablas de la base de datos.
- **Vista.** Archivos XML que definen la interfaz.
- **Controlador.** Objetos Python.

El controlador tiene acceso completo al modelo y la vista, mientras que:

- El modelo notifica a la vista cuando los datos cambian.
- La vista tiene acceso limitado al controlador para minimizar dependencias.

### 1.1. **Especificaciones técnicas para el desarrollo de componentes**

OpenERP usa una arquitectura cliente-servidor con los protocolos **XML-RPC** y **NET-RPC** para comunicación remota. XML-RPC codifica llamadas en XML sobre HTTP, mientras que NET-RPC, basado en Python, es más rápido.

El framework **OpenObject** permite desarrollo rápido (RAD) e incluye:

- ORM (mapeo objeto-relacional).
- Arquitectura MVC.
- Diseñador de informes.
- Herramientas de Business Intelligence.
- Cliente de escritorio y web.

![cover](../../../_Media/Imágenes/SGE/Arquitectura_componentes.png)

### 1.2. **Especificaciones funcionales para el desarrollo de componentes**

OpenERP consta de un núcleo (**base**) y módulos adicionales como:

| Módulo | Función|
|----------|----------------------------------|
| account| Gestión contable y financiera. |
| product| Productos y tarifas. |
| purchase | Gestión de compras.|
| sale | Gestión de ventas. |
| mrp| Planificación de recursos. |
| crm| Relación con clientes/proveedores|

Para crear un módulo, se debe:

1. Crear una carpeta en `addons`.
2. Incluir los archivos:
 - `__init__.py`: Inicio del módulo.
 - `__terp__.py` o `__openerp__.py`: Metadatos.
 - `nombre_modulo.py`: Definición de objetos (Python).
 - `nombre_modulo_nombre_objeto.xml`: Vistas (XML).

El archivo `__terp__.py` debe contener:

```python
{
"name": "Nombre del módulo",
"version": "1.0",
"description": "Descripción",
"author": "Autor",
"website": "URL",
"license": "GPL",
"depends": ["base"],
"init_xml": [],
"installable": True
}
```

## 2. Técnicas de optimización de consultas y acceso a grandes volúmenes de información

Para mejorar el rendimiento, es clave optimizar consultas a la base de datos. Algunas técnicas incluyen:

- **Diseño de tablas.** Evitar duplicidad y aprovechar almacenamiento.
- **Campos.** Ajustar el espacio asignado.
- **Índices.** Aceleran búsquedas, pero no deben usarse en exceso. Se recomiendan para:
- Campos usados frecuentemente en búsquedas.
- Claves ajenas.
- **Optimización SQL.** Mejorar sentencias de selección, inserción y actualización.
- **Mantenimiento de la BD.** Ejecutar comandos de limpieza y análisis.

### 2.1. **Operaciones de consulta. Herramientas**

Para optimizar PostgreSQL:

1. Cambiar al usuario `postgres`:

 ```bash
 sudo su postgres
 ```

2. Acceder al monitor interactivo (`psql`):

 ```bash
 psql
 ```

3. Comandos útiles:
 - `\h`: Ayuda.
 - `\l`: Listar bases de datos.
 - `\c [nombre_bd]`: Conectarse a una BD.
 - `\d`: Mostrar tablas.
 - `\d [nombre_tabla]`: Describir una tabla.
 - `VACUUM VERBOSE ANALYZE [tabla]`: Limpiar y analizar.
 - `\q`: Salir.

### 2.2. **Sistemas batch inputs**

Los **batch inputs** permiten transferir grandes volúmenes de datos a un ERP. Existen dos métodos:

- **Método clásico (asíncrono).**
- Procesa datos y actualiza después.
- Genera un archivo de log para errores.

- **Call transaction (síncrono).**
- Procesa datos en línea (rápido para pocos registros).
- No genera log.

Un proceso batch-input tiene dos fases:

1. **Generación.** Creación del archivo con datos.
2. **Procesamiento.** Ejecución y actualización de la BD.

## 3. Lenguaje proporcionado por los sistemas ERP-CRM

OpenERP utiliza **Python**, un lenguaje de programación moderno y orientado a objetos creado por Guido van Rossum en los años 90. Es de código abierto (compatible con GPL) y destaca por su sintaxis sencilla y cercana al lenguaje natural. Organizaciones como Google, NASA y Yahoo lo utilizan en sus sistemas.

### 3.1. **Características y sintaxis del lenguaje**

Python tiene las siguientes características clave:

- **Interpretado.** Se ejecuta mediante un intérprete que genera bytecode (`.pyc` o `.pyo`).
- **Tipado dinámico.** El tipo de variable se determina en tiempo de ejecución.
- **Fuertemente tipado.** No permite conversiones implícitas entre tipos.
- **Multiplataforma.** Compatible con Linux, Windows, Mac, etc.
- **Orientado a objetos.** Organiza código en clases y objetos.

Ejemplo básico ("Hola mundo"):

```python
print('Hola mundo')
```

Para ejecutarlo:

1. Directamente en el intérprete (comando `python` en terminal).
2. Guardado en un archivo (ej. `programa.py`) y ejecutado con `python programa.py`.

**Sintaxis destacada.**
- Comentarios: `# Esto es un comentario`.
- Sangría: Define bloques de código (no usa llaves `{}`).
- Funciones:

```python
def mi_funcion(param1, param2):
# Código
return resultado
```

### 3.2. **Declaración de datos. Tipos básicos**

Python no requiere declarar variables explícitamente. Tipos principales:

| Tipo| Ejemplo |
|-------------|-----------------------------|
| Entero| `a = 5` |
| Real| `b = 3.14`|
| Complejo| `c = 2 + 3j`|
| Cadena| `texto = "Hola"`|
| Booleano| `verdadero = True`|

**Operadores comunes**
- **Aritméticos:**:
- `+` (suma), `-` (resta), `*` (multiplicación), `/` (división).
- `**` (exponente), `%` (módulo), `//` (división entera).
- **Booleanos**:
- `and`, `or`, `not`.
- **Relacionales:**
- `==` (igualdad), `!=` (desigualdad).
- `<` (menor que), `>` (mayor que).
- `<=` (menor o igual), `>=` (mayor o igual).

```python
# Aritméticos
resultado = 10 + 3 * 2# 16

# Booleanos
es_valido = (edad >= 18) and (tiene_licencia == True)

# Relacionales
if precio != 0:
descuento = precio * 0.1
```

### 3.3. **Estructuras de programación. Colecciones**

Principales estructuras de datos:

1. **Listas.** Ordenadas y mutables.

 ```python
 lista = [1, "dos", True, [3, 4]]
 print(lista[1])# Salida: "dos"
 ```

2. **Tuplas.** Inmutables.

 ```python
 tupla = (1, "a", False)
 print(tupla[0])# Salida: 1
 ```

3. **Diccionarios.** Pares clave-valor.

 ```python
 dic = {"nombre": "Ana", "edad": 30}
 print(dic["nombre"])# Salida: "Ana"
 ```

### 3.4. **Sentencias del lenguaje**

**Condicionales.**

```python
if edad >= 18:
print("Mayor de edad")
else:
print("Menor de edad")
```

**Bucles.**
- `while`:

```python
i = 1
while i <= 5:
print(i)
i += 1
```

- `for`:

```python
for elemento in ["a", "b", "c"]:
print(elemento)
```

### 3.5. **Llamadas a funciones**

Ejemplo de función con retorno:

```python
def cuadrado(num):
return num ** 2

print(cuadrado(4))# Salida: 16
```

### 3.6. **Clases y objetos**

Definición de clase y objeto:

```python
class Persona:
def __init__(self, nombre, edad):
self.nombre = nombre
self.edad = edad

def es_mayor(self):
return self.edad >= 18

persona1 = Persona("Juan", 25)
print(persona1.es_mayor())# Salida: True
```

### 3.7. **Módulos y paquetes**

- **Módulo.** Archivo `.py` con código reusable.

```python
import math
print(math.sqrt(16))# Salida: 4.0
```

- **Paquete.** Directorio con módulos y archivo `__init__.py`.

### 3.8. **Librerías de funciones (APIs)**

Bibliotecas estándar útiles:

- `os`: Funciones del sistema operativo.
- `sys`: Configuración del intérprete.
- `datetime`: Manejo de fechas/horas.
- `math`: Operaciones matemáticas.

### 3.9. **Inserción, modificación y eliminación de datos en objetos**

En OpenERP, los módulos se estructuran en:

1. `__init__.py`: Inicialización.
2. `__terp__.py`: Metadatos (nombre, versión, dependencias).
3. `nombre_modulo.py`: Clases (modelos y controladores).
4. `nombre_modulo_view.xml`: Vistas (interfaz).

Ejemplo de `__terp__.py`:

```python
{
"name": "mi_modulo",
"version": "1.0",
"depends": ["base"],
"author": "Nombre",
"data": ["vista.xml"]
}
```

**Alternativa.** Usar el módulo `base_module_record` para grabar acciones y generar módulos automáticamente.

## 4. Entornos de desarrollo y herramientas para sistemas ERP-CRM

Un entorno de desarrollo integrado (IDE) proporciona todas las herramientas necesarias para programar eficientemente, incluyendo editores especializados, navegadores de archivos, compiladores y depuradores. Para Python y OpenERP, existen varias opciones:

### 4.1. **Depuración de programas**

Python incluye el depurador **pdb** en su biblioteca estándar, que permite:

- Establecer puntos de ruptura (*breakpoints*).
- Ejecución paso a paso.
- Inspección de variables.

**Ejemplo de uso básico de pdb.**

```python
import pdb

def funcion_problematica():
a = 1
pdb.set_trace()# Punto de depuración
b = a / 0
return b
```

En entornos gráficos como **IDLE** (incluido con Python), la depuración ofrece:

- **Go.** Continuar hasta el siguiente breakpoint.
- **Step.** Ejecutar línea por línea.
- **Over.** Saltar llamadas a funciones.
- **Out.** Salir de la función actual.

### 4.2. **Manejo de errores**

Python maneja errores mediante excepciones con bloques `try-except`.

**Ejemplo sin manejo de errores.**

```python
def dividir(a, b):
return a / b

dividir(3, 0)# ZeroDivisionError
```

**Ejemplo con manejo de errores.**

```python
try:
resultado = dividir(3, 0)
except ZeroDivisionError:
print("Error: División por cero")
except Exception as e:
print(f"Error inesperado: {e}")
```

**Tipos comunes de excepciones.**

| Excepción | Causa típica |
| - | - |
| `ZeroDivisionError` | División por cero. |
| `FileNotFoundError` | Archivo no encontrado. |
| `KeyError`| Clave no existe en diccionario.|
| `ValueError`| Valor inapropiado. |

**Buena práctica.**
- Especifique el tipo de excepción en `except` (evite `except` genérico).
- Use `finally` para código que deba ejecutarse siempre (ej. cerrar archivos).

```python
try:
archivo = open("datos.txt", "r")
contenido = archivo.read()
except FileNotFoundError:
print("Archivo no encontrado")
finally:
archivo.close() if 'archivo' in locals() else None
```

**Nota.** En OpenERP, el manejo robusto de errores es crítico para operaciones con la base de datos y transacciones.

## 5. Formularios e informes en sistemas ERP-CRM

### 5.1. **Arquitectura de formularios e informes**

Los formularios e informes en OpenERP se definen mediante archivos XML que describen su estructura y comportamiento. Estos archivos (normalmente llamados `nombre_modulo_view.xml`) contienen:

- **Vistas.** Definiciones de formularios, árboles (listas), búsquedas, etc.
- **Menús.** Accesos a las vistas.
- **Acciones.** Operaciones asociadas a los menús.

**Estructura básica de un archivo XML de vistas.**

```xml
<?xml version="1.0" encoding="utf-8"?>
<openerp>
<data>
<!-- Definición de vista de formulario -->
<record model="ir.ui.view" id="vista_id">
<field name="name">nombre_vista</field>
<field name="model">nombre_modelo</field>
<field name="arch" type="xml">
<form string="Título del Formulario">
<field name="campo1"/>
<field name="campo2"/>
</form>
</field>
</record>

<!-- Definición de menú -->
<menuitem 
id="menu_principal_id" 
name="Menú Principal"
sequence="10"/>

<!-- Definición de acción -->
<record model="ir.actions.act_window" id="accion_id">
<field name="name">Nombre Acción</field>
<field name="res_model">nombre_modelo</field>
<field name="view_mode">tree,form</field>
</record>
</data>
</openerp>
```

**Elementos clave.**
- `<record model="ir.ui.view">`: Define una vista (formulario, árbol, etc.).
- `<field name="arch" type="xml">`: Contiene la estructura XML de la vista.
- `<menuitem>`: Crea entradas en el menú de OpenERP.
- `<record model="ir.actions.act_window">`: Define acciones asociadas a menús.

### 5.2. **Herramientas para creación de formularios e informes**

**Para formularios.**
- Se utilizan archivos XML (como se muestra arriba).
- Herramientas como **Studio** (en Odoo) permiten diseñar formularios visualmente.

**Para informes.**
1. **Informes básicos.**
 - Usando el módulo `base_report_creator`.
 - Generación directa desde vistas de lista/árbol.

1. **Informes avanzados.**
 - **JasperReports.** Librería externa para diseños complejos.
	 - Requiere archivos `.jrxml` (definición del informe).
	 - Soporta múltiples formatos (PDF, HTML, Excel).
 - **QWeb.** Motor de plantillas integrado en Odoo (versiones modernas).
	 - Permite crear informes en XML/HTML.

**Ejemplo de informe con QWeb.**

```xml
<template id="report_ejemplo">
<t t-call="web.html_container">
<div class="header">
<h1>Informe de Ejemplo</h1>
</div>
<div class="body">
<p t-field="object.campo_relevante"/>
</div>
</t>
</template>
```

**Flujo típico para crear un informe.**
1. Definir el modelo de datos (en `nombre_modulo.py`).
2. Crear la plantilla del informe (XML/QWeb/Jasper).
3. Registrar el informe en `__manifest__.py` (versiones modernas) o `__openerp__.py`.

**Nota.** En versiones antiguas de OpenERP, los informes PDF usaban RML (Report Markup Language), pero ha sido reemplazado por tecnologías más modernas como QWeb.

### 5.3. **Integración con el módulo**

El archivo `__manifest__.py` (o `__openerp__.py`) debe incluir las vistas e informes:

```python
{
"name": "Mi Módulo",
"data": [
	"views/nombre_modulo_view.xml",
	"reports/informe_ejemplo.xml"
]
}
```

Estas herramientas permiten crear interfaces flexibles y reportes profesionales directamente integrados con los datos de OpenERP.
