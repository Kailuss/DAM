---
tags: [DAM, SGE]
cssclasses: [dam-sge, table-compact-clean]
banner: "![[sge.jpg]]"
---

# **TEMA 1.** <br>Identificación de <br>sistemas ERP-CRM



## 1. Introducción a la gestión empresarial

Una empresa existe siempre que obtenga beneficios, ya que estos le permiten crecer y desarrollarse. Para ser competitiva, una empresa debe gestionar eficientemente sus recursos. Sin embargo, es importante diferenciar entre empresas privadas y públicas: mientras las primeras buscan maximizar beneficios, las segundas priorizan ofrecer servicios a la sociedad.

Uno de los principales objetivos de cualquier empresa es **satisfacer las necesidades del cliente.** Gracias a la innovación y las nuevas tecnologías, es posible identificar y atender a los clientes de manera más eficiente, lo que contribuye a la obtención de beneficios.

### 1.1. **Evolución de la informática de gestión empresarial**

Los sistemas informáticos han evolucionado para facilitar el tratamiento automático de la información. A continuación, se presenta una clasificación según su evolución:

1. **Sistemas de procedimiento de transacciones.** Gestionan la información relacionada con las transacciones de la empresa (almacenamiento, modificación y recuperación de datos).
2. **Sistemas de automatización de oficinas.** Incluyen herramientas como procesadores de texto, hojas de cálculo y gestores de correo electrónico para apoyar el trabajo administrativo.
3. **Sistemas de planificación de recursos (ERP).** Integran la información y los procesos de una organización en un solo sistema. Cubren áreas como producción, ventas, compras, logística, contabilidad, gestión de proyectos, inventarios, etc.
4. **Sistemas expertos.** Aplicaciones que resuelven problemas complejos emulando el comportamiento de un experto humano. Son una rama de la inteligencia artificial.

### 1.2. **Organización de una empresa y sus relaciones externas**

Una empresa necesita relacionarse con su entorno para desarrollar su actividad con éxito. Los entornos que afectan a una empresa pueden clasificarse en:

- **Entorno próximo.** Incluye factores como mano de obra, proveedores, entidades financieras y organismos oficiales.
- **Entorno general.** Afecta directa o indirectamente a la gestión de la empresa.

Para gestionar esta información de manera eficiente, muchas empresas optan por implementar sistemas de planificación de recursos empresariales (ERP), que centralizan y automatizan la información.

## 2. ERP-CRM

Los **sistemas de planificación de recursos empresariales (ERP)** integran y automatizan las prácticas de negocio relacionadas con los aspectos operativos de una empresa. Están compuestos por módulos que gestionan áreas como nóminas, finanzas, contabilidad, logística, inventarios y pedidos. Estos módulos comparten información, lo que permite una gestión completa y eficiente.

### 2.1. **Revisión de ERP actuales**

Los ERP tienen sus raíces en los sistemas de planificación de requerimientos de materiales (MRP) desarrollados durante la Segunda Guerra Mundial. En los años 80, evolucionaron a MRP II, abarcando más áreas de la empresa. En los años 90, surgieron los ERP modernos, que integran áreas como recursos humanos, finanzas y gestión de proyectos.

Actualmente, el mercado de ERP está dominado por empresas como **SAP**, **Oracle** y **Microsoft.** En España, destacan soluciones como **Navision** y **Axapta.** Además, existen ERP de **código abierto** como **OpenERP**, **Openbravo** y **Tiny ERP.**

Una tendencia reciente es el **Software como Servicio (SaaS)**, que permite acceder a los ERP a través de la red, sin necesidad de instalaciones locales.

### 2.2. **Características de los ERP**

Los ERP se caracterizan por:

1. **Integración.** Centralizan la información en una base de datos única, facilitando el flujo de datos entre módulos.
2. **Modularidad.** Cada módulo corresponde a un área funcional de la empresa (ventas, compras, contabilidad, etc.).
3. **Adaptabilidad.** Permiten personalizar el sistema para adaptarse a las necesidades específicas de la empresa.

### 2.3. **Ventajas e inconvenientes de los ERP**

**Ventajas.**
- Resuelven problemas de gestión de información.
- Aumentan la eficiencia operativa.
- Mejoran las relaciones con proveedores y clientes.
- Reducen costes operativos.

**Inconvenientes.**
- Requieren una inversión inicial significativa.
- Implican cambios en los procesos y la organización de la empresa.
- Necesitan mantenimiento y actualizaciones constantes.

### 2.4. **Concepto CRM**

Los **sistemas de gestión de relaciones con clientes (CRM)** surgieron en los años 90 como una evolución de los ERP. Su objetivo es gestionar las interacciones con los clientes, mejorar su satisfacción y fidelidad, y optimizar las estrategias de marketing y ventas.

### 2.5. **Revisión de CRM actuales**

Los CRM actuales se dividen en:

1. **Aplicaciones electrónicas para canales de distribución.** Mejoran la coordinación con los clientes.
2. **Centros de atención telefónica (call centers).** Ofrecen soporte y resolución de problemas.
3. **Autoservicio.** Permiten a los clientes gestionar sus propias solicitudes.
4. **Gestión electrónica de ventas.** Proporcionan información para entender mejor las necesidades del cliente.

### 2.6. **Características de los CRM**

Los CRM se caracterizan por:

- **Integración de datos.** Unifican la información de diferentes áreas (ventas, marketing, finanzas).
- **Toma de decisiones en tiempo real.** Proporcionan información útil para optimizar las estrategias comerciales.
- **Personalización.** Permiten adaptar el sistema sin modificar el código fuente.

### 2.7. **Ventajas e inconvenientes de los CRM**

**Ventajas.**
- Reducen costes y mejoran la oferta.
- Identifican clientes potenciales.
- Mejoran el servicio al cliente.
- Aumentan las ventas y la retención de clientes.

**Inconvenientes.**
- Requieren un esfuerzo económico y organizativo significativo.
- Implican cambios en los procesos de negocio.
- Dependen de la formación y compromiso del personal.

### 2.8. **Requisitos de los sistemas ERP-CRM**

Para garantizar el éxito de la implantación de un ERP o CRM, es necesario:

1. **Análisis previo.** Definir objetivos, recursos, costes y alcance funcional.
2. **Proyecto de implantación.** Incluir desarrollos de software, parametrizaciones y formación del personal.
3. **Seguimiento y control.** Monitorear el cumplimiento de los objetivos y ajustar el sistema según sea necesario.
## 3. Arquitectura de un sistema ERP-CRM

La arquitectura de un sistema ERP-CRM se basa en dos elementos técnicos clave: una **base de datos relacional** y una **arquitectura cliente-servidor.** Esta estructura permite gestionar y compartir información de manera eficiente entre los diferentes módulos del sistema.

- **Arquitectura cliente-servidor.** Los clientes (usuarios) solicitan servicios al servidor, como acceso a datos o procesamiento de consultas. El servidor gestiona estas solicitudes y controla el acceso a la base de datos compartida.
- **Base de datos relacional.** Es el modelo más utilizado en los sistemas gestores de bases de datos. Permite almacenar, actualizar y eliminar datos de manera estructurada, facilitando la integración entre los módulos del ERP.

El módulo de CRM dentro de un ERP permite a la empresa identificar las necesidades de los clientes y optimizar las estrategias de entrega de productos y servicios.

### 3.1. **Estructura funcional en un sistema ERP**

Los sistemas ERP están diseñados de forma **modular**, lo que permite a cada empresa seleccionar los módulos que mejor se adapten a sus necesidades. La base de datos central capta información de diferentes aplicaciones y la distribuye a los módulos correspondientes.

Los módulos de un ERP se clasifican según los procesos de negocio que apoyan:

1. **Procesos de manufactura.** Incluyen compras, gestión de inventarios, planificación de producción y mantenimiento de equipos.
2. **Procesos de ventas y marketing.** Herramientas para la gestión de ventas, procesamiento de pedidos y facturación.
3. **Procesos financieros y contables.** Gestión de flujos financieros, contabilidad, cuentas por pagar y cobrar, y costes de producción.
4. **Procesos de recursos humanos.** Registro de personal, control de tiempos, cálculo de nóminas y beneficios.

### 3.2. **Extensiones referentes al sistema ERP**

Además de las funciones básicas, los ERP pueden incluir extensiones que amplían sus capacidades:

1. **CRM (Customer Relationship Management).** Gestiona las relaciones con los clientes.
2. **HCM (Human Capital Management).** Controla el rendimiento y la gestión del personal.
3. **SCM (Supply Chain Management).** Administra la cadena de suministro.
4. **PLM (Product Lifecycle Management).** Gestiona el ciclo de vida de los productos, desde su diseño hasta su lanzamiento y evolución.

## 4. Software compatible. Configuración

La elección del sistema operativo y la configuración de la plataforma son aspectos críticos para la implantación de un ERP. Los factores a considerar incluyen:

- **Experiencia previa** de la empresa con sistemas operativos.
- **Disponibilidad de servicios** que el sistema operativo ofrece al ERP.
- **Coste de la inversión** en el nuevo sistema operativo.

### 4.1. **Sistemas operativos libres o propietarios**

- **Unix.** Fue el sistema operativo preferido para la instalación de ERP debido a su seguridad y capacidad de procesamiento a gran escala.
- **Windows.** Desde la versión 2000, se ha adaptado a las exigencias de los ERP, siendo una opción popular.
- **Linux.** Es una alternativa de código abierto que reduce costes de licencias, aunque su soporte puede ser menos amplio que el de Windows o Unix.

La elección del sistema operativo debe basarse en un análisis detallado de las necesidades de la empresa y no condicionarse únicamente por el ERP.

### 4.2. **Sistemas gestores de bases de datos**

Las bases de datos más utilizadas en los ERP son compatibles con los principales fabricantes, como **IBM**, **Oracle** y **Microsoft.** La elección de la base de datos debe adecuarse al ERP, no al revés. Una base de datos bien integrada permite:

- Introducir información una sola vez.
- Distribuir datos en tiempo real a todos los módulos del sistema.
- Evitar la superposición de información.

### 4.3. **Configuración de la plataforma**

La configuración de la plataforma para un ERP varía según el tipo de sistema y el sistema operativo utilizado. Los pasos generales incluyen:

1. **Disponer de un servidor.** Con las prestaciones necesarias para ejecutar el ERP.
2. **Instalar la base de datos.** Y conectarla con el ERP.
3. **Instalar los módulos necesarios.** Seleccionar los módulos del ERP que se adapten a las necesidades de la empresa.
4. **Configurar los clientes.** Para que accedan al servidor y realicen sus solicitudes.

### 4.4. **Verificación de la instalación y configuración**

Antes de instalar un ERP, es necesario:

1. **Elegir un sistema operativo.** Como Linux (RedHat, Debian), Unix (FreeBSD, Solaris) o Windows Server.
2. **Instalar y configurar la base de datos.** Cada ERP puede requerir una base de datos específica.
3. **Seguir las pautas de instalación.** Proporcionadas por el fabricante del ERP, que suelen incluir la ubicación de la base de datos, usuario, contraseña y puerto de comunicaciones.
