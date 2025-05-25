---
tags: [DAM, SGE]
cssclasses:
  - dam-sge
  - table-compact-clean
banner: "![[sge.jpg]]"
number headings: off
---

# Tarea **SGE05**

## Detalles de la tarea de esta unidad

### Enunciado

Esta tarea trata de crear un módulo para una empresa o tarea concreta a libre elección, desarrollado mediante el uso del software de Odoo instalado en la Máquina virtual Ubuntu Server en prácticas anteriores. Es importante utilizar un IDE apropiado para manejar el código (por ejemplo Visual Studio).

## Apartado A. Creación del módulo personal  

### Requisitos del modelo

- **Idioma:** Inglés.  
- **Nombre del módulo:** Iniciales + curso (ej. `aog2425`).  
- **Estructura:** Seguir esquema de clases previamente elaborado.  
- **Archivo `__manifest__.py`:** Campos correctamente definidos.  
- **Clases:**  
  - Mínimo 3 clases conectadas con 2 atributos relacionales (`one2many`, `many2one`, `many2many`).  
  - Atributos: `boolean`, `date`, `integer`, `decimal` (al menos 1 calculado con `@api.onchange` o `@api.depends`).  
  - Campos: `text`, `char` (con descripciones de ayuda).  
  - Al menos 1 campo `selection`.  
  - Conexiones con módulos nativos de Odoo (empleados, proveedores, productos).  

  ### Vistas (`views.xml`)

- Mínimo 1 vista `<tree>` (o `<list>` en Odoo 18+) y 1 `<form>` por clase. *(Valorable: vistas Kanban)*.  
- Al menos 1 vista de calendario.  
- Vista de búsqueda con agrupamiento u ordenación por columna.  
- Acciones y menús:  
  - Acciones para abrir ventanas en cada clase.  
  - Menús superiores con acceso a los datos de cada clase.  
- Icono de instalación visible en la búsqueda de apps.  

### Recomendaciones adicionales

- Datos de ejemplo (5 tuplas por clase).  
- Traducciones (castellano/catalán) generadas con Poedit (`i18n`).  
- Grupos de seguridad con privilegios.  
- Informes Q-Web.  
- Mecanismos de herencia (MVC).  

## Apartado B. Guía de usuario del módulo
- Explicación resumida y clara del módulo, con ejemplos.  
- Documentación de operaciones e incidencias durante el desarrollo.  

### Formato del documento (PDF)  

- **Estructura:** Portada, índice automatizado (hipervínculos), paginación, títulos numerados (`1.`, `1.1.`, etc.).  
- **Contenido:**  
  - Portada con logo del centro, nombre del módulo, actividad, alumno y curso (2022/2023).  
  - Imágenes/tablas con pies numerados y referenciados en el texto.  
  - Anexos para contenido >50% de página.  
  - Bibliografía/webgrafía (norma APA).  
- **Estilo:**  
  - Fuente: Arial 12 (interlineado 1.5, márgenes 3 cm, texto justificado).  
  - Notas/encabezados/gráficos: Arial 10.  
  - Sin faltas de ortografía.   

## Entrega

### Criterios de puntuación (Total: 10 puntos)  

- **Apartado A:** 6 puntos.  
- **Apartado B:** 3 puntos.  
- **Presentación:** 1 punto.  

### Recursos necesarios 

- Ubuntu Server 22.04 LTS+ (MV).  
- Virtualizador (VirtualBox, VMware).  
- Odoo on premise (v16/v17) + PostgreSQL.  
- IDE: VS Code o PyCharm Professional.   

### Indicaciones de entrega  

- **Formato:** ZIP con carpeta del proyecto + PDF.  
- **Nombre del archivo:**  
  `apellido1_apellido2_nombre_SGE05_Tarea`  
  *(Ejemplo: `sanchez_manas_begona_SGE05_Tarea`)*  
- **Restricciones:** Sin `ñ`, tildes o caracteres especiales.
