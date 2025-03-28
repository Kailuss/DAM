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

# **TEMA 4.** <br>Implantación de <br>sistemas ERP-CRM

| Anexos |
| - |
| [Resumen Tema 4 SGE](Resúmenes/Resumen%20Tema%204%20SGE.md) |
| [Tarea SGE03 y SGE04](../Práctica/Tareas/Tarea%20SGE03%20y%20SGE04.md) |
## 1. Introducción

En la actualidad, existe una amplia oferta de software de planificación de recursos empresariales (ERP). Estos sistemas se diferencian por su tipo de licencia, módulos, sistemas operativos compatibles, entre otros factores. La elección del ERP adecuado es crucial para el éxito de su implantación. Determinará si el sistema se adapta a las necesidades de la empresa.

Para garantizar una elección acertada, es necesario realizar un **análisis de necesidades.** Este análisis identifica los procesos clave de la empresa y los requisitos que el ERP debe cumplir. Puede ser realizado por consultoras externas, que emiten un informe con recomendaciones para la implantación.

Las fases principales de un proceso de selección, implantación y puesta en marcha de un ERP son:

1. **Selección del ERP.** Identificar los procesos clave de la empresa, las tareas repetitivas que pueden automatizarse y los módulos del ERP que mejor se adapten a las necesidades.
2. **Fase de implantación.** Realizar los cambios y adaptaciones necesarios en la aplicación. Es fundamental una planificación detallada.
3. **Fase de puesta en marcha.** Instalación del programa en el entorno de producción y resolución de problemas iniciales.
4. **Cierre y finalización del proyecto.** Revisión final del sistema para asegurar su correcto funcionamiento.

El **software como servicio (SaaS)** es una opción popular para pequeñas empresas. Ofrece un sistema completo de gestión con un costo mensual que incluye servidores, mantenimiento, hosting y soporte.

### 1.1. **Tipos y necesidades de las empresas**

Las necesidades de una empresa varían según su tipo y sector. Los ERP están diseñados de manera modular para adaptarse a diferentes tipos de empresas:

- **Pequeña y mediana empresa (PYME).** Necesitan módulos para la gestión de clientes, proveedores, productos, compras, ventas y almacén.
- **Sector servicios.** Requieren un módulo de gestión de proyectos para el control y seguimiento de tareas.
- **Tiendas y restaurantes.** Utilizan terminales de punto de venta (TPV) para gestionar ventas, categorías de productos y métodos de pago.
- **Ayuntamientos.** Implantan ERP para la gestión de proyectos, contabilidad, compras, recursos humanos y atención al ciudadano.
- **Venta telefónica.** Priorizan un módulo de CRM para registrar y gestionar la información de los clientes.

## 2. Selección del sistema ERP y módulos a utilizar

La selección del ERP y sus módulos requiere un **análisis previo** de los procesos de la empresa. Este análisis debe identificar:

- Los procesos clave de cada área o departamento.
- Las tareas que no se realizan, se realizan mal o consumen demasiado tiempo.
- La información que fluye entre áreas y los medios utilizados (correo electrónico, papel, etc.).

El análisis permite obtener presupuestos ajustados. Facilita la toma de decisiones sobre qué ERP y módulos utilizar. Los módulos pueden ser:

- **Módulo base.** Incluye las funcionalidades mínimas para operar.
- **Módulos precargados.** Disponibles para instalación inmediata.
- **Módulos no precargados.** Requieren descarga e instalación manual.

En el caso de empresas españolas, es esencial instalar los **módulos de localización española.** Estos incluyen funcionalidades específicas como:

- Ventas.
- Compras.
- Productos.
- Almacén.
- Contabilidad.
- Facturación.
- Plan contable.

### 2.1. **Análisis inicial**

El análisis inicial es la base para la selección del ERP. Debe cubrir:

- **Estructura de la información.** Identificar los datos maestros necesarios para el funcionamiento del sistema.
- **Procesos de negocio.** Estudiar las tareas de cada área y cómo se comunican entre sí.
- **Informes necesarios.** Detallar los informes que el ERP debe generar.
- **Traspaso de información.** Planificar la migración de datos desde los sistemas actuales al ERP.
- **Planificación de la implantación.** Gestionar el proyecto de implantación de manera sistemática.

### 2.2. **Carga de módulos**

Una vez seleccionados los módulos necesarios, se procede a su instalación. Si los módulos no están precargados, se deben descargar desde Internet y cargarlos en el sistema. Para ello, se utilizan sistemas de control de versiones como **Bazaar.** Este permite acceder a las últimas versiones de los módulos.

Ejemplo: Instalación de los módulos de localización española en OpenERP:

1. **Instalar Bazaar.** Desde Synaptic o mediante el comando `sudo apt-get install bzr`.
2. **Descargar los módulos.** Utilizar Bazaar para descargar los módulos `l10n_ES_pyme_install` y `l10n_ES_pyme_custom`.
3. **Copiar los módulos.** Mover los módulos descargados a la carpeta `addons` del ERP.
4. **Actualizar la lista de módulos.** Verificar que los módulos aparecen en la lista de módulos disponibles.

### 2.3. **Comprobación de módulos**

Tras descargar y copiar los módulos, se realiza una comprobación. Asegura que todas las dependencias están disponibles. Los pasos incluyen:

- Copiar los módulos dependientes a la carpeta `addons`.
- Actualizar la lista de módulos.
- Verificar que los módulos están en estado "No instalado".

### 2.4. **Selección de módulos**

Finalmente, se instalan los módulos seleccionados. Por ejemplo, para instalar `l10n_ES_pyme_install`:

1. Acceder al menú **Administración/Administración de Módulos/Módulos.**
2. Buscar el módulo y programarlo para la instalación.
3. Aplicar las actualizaciones programadas.

Durante la instalación, se ejecuta un asistente de configuración. Ayuda a establecer los parámetros iniciales, como la creación de provincias y la configuración de contabilidad.

## 3. Implantación en la empresa

Una vez seleccionado el ERP y la empresa encargada de su implantación, es crucial gestionar el proyecto de manera sistemática y controlada. La fase de implantación no solo incluye la adaptación del ERP a los requerimientos de la empresa. También incluye:

- **Formación de usuarios.**
- **Traspaso de datos.**
- **Configuración del programa.**
- **Pruebas de los usuarios.**
- **Pruebas definitivas y revisión de la configuración.**

Todas estas etapas deben estar planificadas. Esto minimiza riesgos como:

- Finalización fuera del plazo previsto.
- Sobrepasar el presupuesto asignado.
- Funcionamiento no esperado de la aplicación.
- Acontecimientos imprevistos que afecten el desarrollo del proyecto.

Además, es fundamental gestionar el cambio organizacional. La resistencia de los usuarios a adoptar nuevos métodos de trabajo puede llevar al fracaso del proyecto.

### 3.1. **Consultas necesarias para obtener información**

Durante la implantación, el proveedor del ERP es responsable de:

- **Diseño y adaptación del programa.**
- **Puesta en marcha.**
- **Soporte en la etapa final del proyecto.**

Si el análisis inicial fue exhaustivo, gran parte de la información recopilada servirá para definir los requerimientos de la implantación. Las consultas más comunes incluyen:

- **Datos de la empresa.**
- **Clientes.**
- **Proveedores.**
- **Productos.**
- **Almacén.**
- **Información de compra y venta.** Tarifas, formas de pago, etc.
- **Información financiera.** Plan contable, impuestos, etc.

### 3.2. **Crear objetos. Tablas y vistas que es preciso adaptar**

El primer paso es estudiar la información que se introducirá en la aplicación. Esto puede implicar:

- **Añadir campos a objetos existentes.**
- **Crear nuevos objetos.**
- **Gestionar múltiples bases de datos** (una por empresa).

Para crear una nueva base de datos, se accede al menú **Base de Datos.** Para crear nuevos objetos, se utiliza el menú **Administración/Personalización/Estructura de la base de datos/Objetos.** Al crear un objeto, se deben definir:


|     |     |
| --- | --- |
| **Nombre del objeto.** |Nombre en la aplicación.|
| **Objeto.** |Nombre en la base de datos.|
| **Descripción de los campos.** |Lista de campos del objeto.|
| **Tipo de los campos.** |Tipo de dato (texto, fecha, etc.).|
| **Permisos de acceso.** |Derechos de acceso por parte de los usuarios.|

En OpenERP, los objetos pueden ser tablas o vistas en la base de datos. Por ejemplo, el objeto **Estadísticas de Servidor** es una vista llamada `report_smtp_server` en la base de datos.

### 3.3. **Creación de formularios personalizados**

Los formularios son interfaces para la entrada y visualización de datos. En OpenERP, se implementan mediante vistas. Estas pueden ser de tipo formulario, árbol o gráficos. Las vistas se pueden modificar de dos formas:

1. **Cambiando el código XML.** Desde el menú **Administración/Personalización/Interfaz de usuario/Vistas.**
2. **Utilizando el Administrador de vistas.** Accediendo al objeto correspondiente y seleccionando **Personalizar/Gestionar Vistas.**

### 3.4. **Creación de informes y gráficos personalizados**

OpenERP incluye informes predefinidos en todos los módulos. También permite crear informes personalizados. Los tipos de informes más comunes son:

- **Informes estadísticos.** Dinámicos, cambian según las opciones seleccionadas. Se crean con el módulo `base_report_creator`.
- **Documentos imprimibles.** Generados en formato PDF. Se pueden modificar con herramientas como OpenOffice.org.

Para crear documentos imprimibles, se puede:

1. **Utilizar el lenguaje de programación de la aplicación.**
2. **Usar herramientas ofimáticas** para modificar plantillas.
3. **Usar un motor de informes gráfico** como Jasper Reports con iReports.

### 3.5. **Manejar plantillas de documentos**

Para personalizar informes en OpenERP, se utiliza OpenOffice.org con la extensión **OpenERP Report Designer.** Los pasos son:

1. **Instalar el módulo `base_report_designer`.**
2. **Instalar la extensión de OpenOffice.org.**

Una vez instalados, se pueden:

- Conectar con el servidor.
- Abrir informes existentes.
- Añadir nuevos campos.
- Crear nuevos informes.
- Enviar informes al servidor.

Los informes se generan en formato RML (Report Markup Language). Este describe cómo se imprimirán las páginas.

### 3.6. **Exportación de datos**

Los informes creados con OpenOffice.org se pueden exportar a formato RML. Este es un lenguaje basado en XML para la generación de documentos impresos. Los pasos para exportar un informe son:

1. Acceder al menú **OpenERP Report Designer/Export to RML.**
2. Guardar el archivo RML en el directorio `addons` del servidor, dentro de la carpeta `report` del módulo correspondiente.

### 3.7. **Traspaso de datos**

El traspaso de datos es una fase crítica en la implantación del ERP. Implica migrar la información del sistema antiguo al nuevo ERP. Las tareas incluyen:

- **Unificar el formato y contenido de los datos.**
- **Eliminar duplicidades.**
- **Mejorar la codificación de la información.**
- **Guardar los datos en un archivo con el formato de exportación elegido.**
- **Introducir datos de tablas secundarias.**
- **Realizar el proceso de importación.**

En OpenERP, los archivos CSV deben tener campos separados por punto y coma (`;`). El separador de texto debe ser comillas dobles (`"`). Además, la primera fila debe contener los nombres de los campos en el idioma configurado en la aplicación.

### 3.8. **Planificación de la implantación**

La planificación del proyecto de implantación debe detallar todas las tareas, responsables y áreas afectadas. Las figuras clave en este proceso son:


|     |     |
| --- | --- |
| **Dirección o responsables de la empresa.** |Toman decisiones y deben estar plenamente implicados.|
| **Jefe de proyecto.** |Valida, verifica y actúa como interlocutor entre los miembros del equipo.|
| **Responsable de migración de datos.** |Conoce el sistema antiguo y las necesidades del nuevo.|
| **Equipo de consultoría.** |Realiza el análisis inicial, propone soluciones, instala y configura el sistema, forma a los usuarios y desarrolla módulos a medida.|

Las etapas principales del proceso de implantación son:

1. **Análisis de procesos y enfoque de la solución.**
2. **Planificación del proyecto** (tiempos y costes).
3. **Instalación, traspaso de datos y formación.**
4. **Consultoría, formación e instalación de módulos a medida.**
5. **Pruebas** (manteniendo el sistema antiguo en paralelo).
6. **Puesta en marcha.**
7. **Revisión de funcionalidades y ajustes.**
8. **Finalización del proyecto.**

## 4. Configuración del sistema

La configuración del sistema ERP implica establecer todos los parámetros necesarios. Estos deben ajustarse a las necesidades de la empresa. Incluye la adaptación de informes, consultas y otros objetos. También la personalización de la interfaz y la gestión de los derechos de acceso.

Una de las tareas más importantes es el **control de acceso a la información.** Garantiza la seguridad del sistema. Para ello, es fundamental establecer una política de usuarios. Esta asigna permisos específicos a cada área o función, evitando riesgos como cambios no autorizados o incongruencias en la base de datos.

### 4.1. **Control de acceso**

En OpenERP, el control de acceso se gestiona mediante **usuarios y grupos.** Cada usuario puede pertenecer a uno o más grupos. Esto determina:

- **Qué menús puede visualizar.**
- **A qué tablas de la base de datos puede acceder.**

Por ejemplo, un grupo **Comercial** puede tener acceso solo a menús relacionados con ventas. No tendrá acceso a información contable. Los usuarios del Departamento de Ventas se asignan a este grupo, heredando sus permisos.

Para configurar los derechos de acceso:

1. **Definir grupos.** Crear grupos representativos de las funciones de la empresa (por ejemplo, **Responsable de Ventas**).
2. **Asignar usuarios a grupos.** Desde el menú **Administración/Usuarios.**
3. **Autorizar accesos a menús.** Desde el menú **Administración/Seguridad/Autorizar accesos a Menús.**

Además, se puede establecer un **control de acceso por objetos.** Este define qué acciones (leer, escribir, crear, eliminar) pueden realizar los usuarios sobre los datos. Se configura en el menú **Administración/Seguridad/Controles de acceso/Lista de controles de Acceso.**

### 4.2. **Cambiar la apariencia del sistema**

OpenERP permite personalizar la apariencia del sistema. Esto incluye la organización de menús y la página de bienvenida. Sin embargo, es importante valorar la necesidad de estos cambios. Pueden requerir formación adicional para los usuarios y actualización de la documentación.

Para modificar menús:

1. **Cliente web.** Usar el botón **Cambiar (Switch)** para editar menús.
2. **Cliente de escritorio.** Seleccionar un menú y usar **Formulario/Cambiar a Lista/Formulario.**

También se pueden crear **accesos directos** a menús frecuentes:

- **Cliente web.** Botón **Añadir.**
- **Cliente de escritorio.** Botón **suma** en el panel de **Atajos.**

Para personalizar la página de bienvenida y el menú principal por usuario:

1. Acceder al menú **Administración/Usuarios/Usuarios.**
2. Editar el usuario y seleccionar:
   - **Acción Inicial (Home Action).** Menú que se abre al iniciar sesión.
   - **Acción de Menú (Menu Action).** Menú principal.

### 4.3. **Realizar copias de seguridad**

La planificación de copias de seguridad es esencial para proteger la información de la empresa. En OpenERP, se utiliza el módulo **auto_backup** para programar copias de seguridad automáticas.

Pasos para configurar copias de seguridad:

1. **Instalar el módulo `auto_backup`.**
2. Activar la acción planificada **Backup scheduler** en el menú **Configuración/Acciones planificadas.**
3. Indicar la hora, frecuencia y repetición de las copias.
4. Configurar las bases de datos a respaldar en el menú **Configuración/Personalización/Configure Backup.**

## 5. Puesta en marcha y finalización del proyecto

La fase de puesta en marcha implica realizar pruebas definitivas de todos los módulos. Estas pruebas pueden realizarse de dos formas:

1. **Pruebas en paralelo.** Trabajar con ambos sistemas (antiguo y nuevo) para comparar resultados. Es costoso en tiempo y recursos.
2. **Bloqueo del sistema antiguo.** Poner en marcha el nuevo ERP directamente. Requiere pruebas exhaustivas previas.

La elección del método depende de la confianza en las pruebas realizadas. Tras un período de funcionamiento, se lleva a cabo la **finalización del proyecto.** Se revisa:

- Si se han alcanzado los objetivos.
- El funcionamiento adecuado de los módulos.
- La formación de los usuarios.
- El cumplimiento del presupuesto.
- La ausencia de errores o situaciones imprevistas.

### 5.1. **Factores de éxito de la implantación de un ERP**

El éxito de la implantación de un ERP depende de varios factores:

1. **Dirección del proyecto.** Liderazgo claro y compromiso del equipo directivo.
2. **Dotación de medios.** Recursos técnicos y humanos adecuados.
3. **Implicación de la organización.** Colaboración de todos los usuarios.

Las principales causas de fracaso incluyen:

- **Falta de liderazgo.** Objetivos poco claros o falta de compromiso.
- **Resistencia al cambio.** Desconfianza hacia los consultores o formación insuficiente.
- **Consultores inexpertos.** Falta de experiencia en implantaciones ERP.
- **Software poco flexible.** Limitaciones en la configuración o modificaciones.
- **Interfaz poco amigable.** Dificulta la adopción por parte de los usuarios.
- **Falta de funcionalidades.** Expectativas no cumplidas por el ERP.
- **Falta de recursos.** Insuficiencia de tiempo, personal o recursos técnicos.

Para evitar estos problemas, es crucial identificar y resolver los puntos críticos. También concienciar al personal sobre la importancia del cambio y garantizar una formación adecuada.
