---
number headings: auto, first-level 2, max 3, contents ^toc, skip ^skipped, start-at 1, _.1.1.
---

# Resumen Tema SGE04

Este tema aborda el proceso de selección, implantación y puesta en marcha de sistemas ERP (Enterprise Resource Planning) y CRM (Customer Relationship Management). A continuación, se presenta un resumen estructurado con explicaciones breves para facilitar la comprensión.

## 1. Introducción
- **Elección del ERP.** La selección del ERP adecuado es crucial para el éxito de su implantación. Se debe realizar un **análisis de necesidades** para identificar los procesos clave de la empresa y los requisitos que el ERP debe cumplir.
  - *Fases principales*: Selección del ERP, implantación, puesta en marcha y cierre del proyecto.
  
- **Software como Servicio (SaaS).** Es una opción popular para pequeñas empresas, ya que ofrece un sistema completo de gestión con un costo mensual que incluye servidores, mantenimiento, hosting y soporte.

- **Tipos de Empresas.** Las necesidades varían según el tipo de empresa. Por ejemplo, las PYME necesitan módulos para gestión de clientes, proveedores y productos, mientras que los ayuntamientos requieren módulos para contabilidad y atención al ciudadano.

## 2. Selección del Sistema ERP y Módulos a Utilizar
- **Análisis Previo.** Es necesario identificar los procesos clave de la empresa, las tareas que consumen demasiado tiempo y la información que fluye entre áreas.
  - *Módulos*: Pueden ser base, precargados o no precargados. Para empresas españolas, es esencial instalar los **módulos de localización española**, que incluyen funcionalidades específicas como contabilidad y facturación.

- **Carga de Módulos.** Los módulos se pueden descargar e instalar manualmente. Por ejemplo, en OpenERP, se utiliza **Bazaar** para descargar módulos como `l10n_ES_pyme_install`.
  - *Pasos*: Instalar Bazaar, descargar módulos, copiarlos a la carpeta `addons` y actualizar la lista de módulos.

- **Comprobación y Selección de Módulos.** Tras la descarga, se verifica que todas las dependencias estén disponibles y se instalan los módulos seleccionados.

## 3. Implantación en la Empresa
- **Fases de Implantación.** Incluyen la formación de usuarios, traspaso de datos, configuración del programa y pruebas. Es fundamental gestionar el cambio organizacional para evitar la resistencia de los usuarios.
  - *Riesgos*: Finalización fuera de plazo, sobrepasar el presupuesto o funcionamiento no esperado del sistema.

- **Consultas Necesarias.** Durante la implantación, el proveedor del ERP debe recopilar información sobre clientes, proveedores, productos, almacén y datos financieros.

- **Creación de Objetos y Formularios.** Se pueden añadir campos a objetos existentes o crear nuevos objetos. Los formularios se implementan mediante vistas en XML, que pueden ser de tipo formulario, árbol o gráficos.
  - *Ejemplo*: En OpenERP, se puede modificar un formulario desde el menú **Administración/Personalización/Interfaz de usuario/Vistas.**

- **Informes y Gráficos Personalizados.** OpenERP permite crear informes personalizados, como informes estadísticos o documentos imprimibles en PDF. Se pueden modificar con herramientas como OpenOffice.org.

- **Traspaso de Datos.** Es una fase crítica que implica migrar la información del sistema antiguo al nuevo ERP. Los datos deben estar en formato CSV, con campos separados por punto y coma.

- **Planificación del Proyecto.** Debe detallar todas las tareas, responsables y áreas afectadas. Las figuras clave incluyen al jefe de proyecto, el responsable de migración de datos y el equipo de consultoría.

## 4. Configuración del Sistema
- **Control de Acceso.** En OpenERP, el control de acceso se gestiona mediante usuarios y grupos. Cada usuario puede pertenecer a uno o más grupos, lo que determina qué menús y tablas puede visualizar.
  - *Ejemplo*: Un grupo **Comercial** puede tener acceso solo a menús relacionados con ventas.

- **Cambiar la Apariencia del Sistema.** Se puede personalizar la organización de menús y la página de bienvenida. Sin embargo, estos cambios pueden requerir formación adicional para los usuarios.

- **Copias de Seguridad.** Es esencial planificar copias de seguridad para proteger la información. En OpenERP, se utiliza el módulo **auto_backup** para programar copias de seguridad automáticas.

## 5. Puesta en Marcha y Finalización del Proyecto
- **Pruebas Definitivas.** Se pueden realizar pruebas en paralelo (trabajar con ambos sistemas) o bloquear el sistema antiguo y poner en marcha el nuevo ERP directamente.
  - *Elección del método*: Depende de la confianza en las pruebas realizadas.

- **Factores de Éxito.** El éxito de la implantación depende del liderazgo del proyecto, la dotación de medios y la implicación de la organización.
  - *Causas de Fracaso*: Falta de liderazgo, resistencia al cambio, consultores inexpertos, software poco flexible o falta de recursos.
