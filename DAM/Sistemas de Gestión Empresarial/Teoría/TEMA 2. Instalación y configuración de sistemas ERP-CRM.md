---
number headings: first-level 2, max 3, skip ^skipped, _.1.1.
banner_y: 0.6
banner: "![[../../../_Media/Banners/vecteezy_yellow-and-white-background-with-a-wave-pattern-the-yellow_53887306.jpg]]"
---

# **TEMA 2.** Instalación y configuración de sistemas ERP-CRM

![[Mapa conceptual SGE02.canvas]]

## 1. Introducción

> [!done] Caso práctico 
> Ada y María, tras investigar el mercado de los ERP, concluyen que desarrollar un sistema desde cero es costoso y poco práctico. En su lugar, optan por utilizar un ERP ya existente, especialmente uno de código abierto, que reduce costes de licencias y permite centrarse en la personalización. Ada, con su mente pragmática, decide que su empresa, BK Programación, se encargará de la implantación y adaptación del ERP, e incluso desarrollará módulos personalizados para clientes exigentes. María, por su parte, está emocionada por la flexibilidad que ofrecen estas soluciones. Juntas, se lanzan a explorar las opciones disponibles. 

En un entorno empresarial cada vez más competitivo y globalizado, la información se ha convertido en un valor diferencial clave. Las empresas necesitan mejorar continuamente sus procesos de gestión para responder mejor a las demandas de los clientes, reducir plazos de entrega y controlar inventarios. Aquí es donde entran en juego los **Sistemas de Planificación de Recursos Empresariales (ERP)**, que ofrecen una gestión **integrada** y **flexible** de todos los recursos de la empresa.

- **Integrada.** Los procesos están interconectados, evitando duplicidades e incongruencias en los datos. Por ejemplo, un nuevo cliente puede generar un pedido, que a su vez se convierte en una factura.
- **Flexible.** Se adaptan a los flujos de trabajo de la empresa, a diferencia de los programas cerrados con menos posibilidades de personalización.

La elección del ERP adecuado depende de una evaluación detallada de las soluciones disponibles, considerando su nivel de integración, flexibilidad y coste. En este contexto, el **software libre** ha ganado relevancia como una alternativa viable frente a las soluciones propietarias de grandes multinacionales como SAP u Oracle.

### 1.1. **Tipos de licencia**

El software libre se basa en principios éticos que permiten su uso, modificación y redistribución sin restricciones. Algunas de las licencias más comunes son:

- **GPL (General Public License).** Permite la redistribución y modificación del software, siempre que se mantenga bajo los mismos términos. Es utilizada por **OpenERP.**
- **BSD.** Permite la libre redistribución y modificación, incluso como software no libre. Solo exige dar crédito a los autores.
- **MPL (Mozilla Public License).** Permite la copia, modificación y distribución limitada, manteniendo el control sobre las creaciones. Es utilizada por **Openbravo ERP.**
- **Software semilibre.** Permite uso, copia y modificación sin fines lucrativos, pero con restricciones.
- **Software privativo.** Prohíbe el uso, redistribución o modificación sin autorización. Es utilizado por **SAP** y los módulos comerciales de **Openbravo ERP.**

### 1.2. **El software libre en el mercado de los ERPs**

El modelo de negocio del software libre ha transformado la industria de los ERP. En lugar de pagar por licencias, las empresas pagan por servicios de implantación, mantenimiento y soporte. Esto reduce costes iniciales y ofrece mayor flexibilidad.

**Ventajas del software libre.**
- **Reducción de costes.** No hay que pagar por licencias.
- **Libertad de modificación.** Las empresas pueden adaptar el software a sus necesidades.
- **Comunidad de soporte.** Foros y comunidades ofrecen ayuda y soluciones.

**Desventajas.**
- **Falta de garantías.** Las actualizaciones y correcciones dependen de la comunidad.
- **Tiempo de respuesta.** Puede haber retrasos en la resolución de problemas.

Algunos ERP de software libre destacados son **Openbravo** y **OpenERP**, que ofrecen soluciones robustas y flexibles para la planificación empresarial.

### 1.3. **ERPs de software libre**

#### Openbravo ERP
- **Origen.** Desarrollado por profesores de la Universidad de Navarra.
- **Arquitectura.** Cliente/servidor web, escrito en Java.
- **Bases de datos.** Soporta Oracle y PostgreSQL.
- **Versiones.**
  - **Community Edition.** Gratuita y de código abierto.
  - **Network Edition.** Versión comercial con módulos adicionales.

#### OpenERP
- **Origen.** Creado por Fabien Pinckaers en Bélgica.
- **Lenguaje.** Escrito en Python.
- **Base de datos.** Utiliza PostgreSQL.
- **Modelo de negocio.** Basado en servicios de soporte y mantenimiento.

Ambas soluciones son excelentes opciones para empresas que buscan alternativas de software libre. En este curso, utilizaremos **Ubuntu** (distribución GNU/Linux) para la instalación y configuración de estos ERP.

## 2. Instalación y configuración del sistema ERP-CRM

> [!done] Caso práctico 
> María, siempre curiosa, descubre los **webinars**, esos seminarios online que parecen ser la nueva forma de aprender sin salir de casa. Asiste a un par de ellos y sale con más preguntas que respuestas, pero también con una idea más clara de cómo funcionan los ERP. Ada, impresionada por el entusiasmo de María, sugiere instalar dos ERP destacados para probarlos en vivo. María, emocionada, ya se imagina como la "influencer" de los ERP en BK Programación. 

El proceso de instalación y configuración de un ERP implica varias tareas clave:

✔ **Diseño de la instalación**

- **Análisis de necesidades.** Identificar las necesidades de la empresa y cómo el ERP puede resolverlas.
- **Adaptación de tablas, datos, formularios e informes.** Definir qué elementos del ERP deben personalizarse.

✔ **Instalación de equipos servidores y clientes**

- **Requisitos de hardware.** Asegurarse de que el hardware cumple con los requisitos mínimos.
- **Opción SaaS.** Contratar servicios en la nube para acceder a los recursos de forma remota.

✔ **Instalación del software**

- **Instalación del ERP.** Seguir los pasos del instalador proporcionado por el fabricante.
- **Software adicional.** Instalar bases de datos y otros componentes necesarios.

✔ **Adaptación y configuración del programa**

- **Configuración inicial.** Ajustar parámetros como usuarios, permisos y módulos.
- **Personalización.** Adaptar el ERP a los procesos específicos de la empresa.

✔ **Migración de datos**

- **Importación de datos.** Trasladar información de clientes, proveedores, contabilidad, etc., desde el sistema antiguo al nuevo ERP.
- **Procesos manuales.** En caso de que no sea posible automatizar la migración.

✔ **Realización de pruebas**

- **Pruebas de funcionamiento.** Verificar que el ERP funciona correctamente.
- **Coexistencia con el sistema antiguo.** Durante un período de transición, ambos sistemas pueden operar en paralelo.

✔ **Documentación del sistema**

- **Manuales y guías.** Crear documentación para los usuarios.
- **Difusión interna.** Publicar la documentación en la intranet, correo electrónico, etc.

✔ **Formación de usuarios**

- **Formación inicial.** Capacitar a los responsables del proyecto.
- **Formación para usuarios finales.** Enseñar a los empleados cómo utilizar el ERP.

### 2.1. **Tipos de instalación: Monopuesto y Cliente/Servidor**

La instalación de un sistema ERP/CRM puede variar según la plataforma y el tipo de ERP utilizado. Los tipos de instalación más comunes son:

1. **Instalación mediante máquina virtual.**
   - La aplicación y sus dependencias se proporcionan en una máquina virtual lista para usar.
   - **Uso.** Ideal para evaluaciones iniciales, no recomendada para entornos de producción.

2. **Instalación de paquetes bajo entorno gráfico.**
   - Se utilizan asistentes gráficos para instalar el software y resolver dependencias.
   - **Uso.** Adecuado para entornos de producción, aunque los paquetes pueden no estar actualizados.

3. **Instalación personalizada.**
   - Se descargan los paquetes fuente desde la web y se instalan manualmente mediante comandos.
   - **Uso.** Permite mayor control, pero es más complejo.

4. **Acceso en línea (SaaS).**
   - No se requiere instalación local. Se accede al ERP a través de un servidor remoto.
   - **Uso.** Ideal para empresas que prefieren externalizar la infraestructura.

Además, los ERP pueden funcionar de dos formas:

- **Monopuesto.** La base de datos, los programas y la aplicación cliente están en el mismo equipo. Se utiliza la dirección `localhost` para la conexión.
- **Cliente/Servidor.** La aplicación cliente se ejecuta en un equipo distinto al servidor, que almacena los datos y los programas. Se utiliza la dirección IP del servidor para la conexión.

### 2.2. **Procesos de instalación y servicios de acceso al sistema**

El proceso de instalación de un ERP depende del sistema operativo utilizado (Windows, Linux, etc.). En general, los pasos son:

1. **Instalación del ERP.**
   - En Windows, se utiliza un archivo autoinstalable.
   - En Linux, se accede a los ERP a través de los repositorios de la distribución (por ejemplo, Ubuntu).

2. **Instalación y configuración del servidor de bases de datos.**
   - Se instala y configura la base de datos que contendrá la información de la empresa.

3. **Instalación de los servicios de acceso para los clientes.**
   - Se configuran los servicios para que los clientes puedan acceder al ERP, ya sea a través de un navegador web o una aplicación de escritorio.

**Ejemplo de instalación.**
- **Openbravo.** Se instala mediante el Gestor de Paquetes Synaptic en Ubuntu.
- **OpenERP.** Se instala el servidor y el servicio de acceso de escritorio en Ubuntu.

### 2.3. **Parámetros de configuración: descripción, tipología y uso**

Tras la instalación, es necesario configurar el ERP para garantizar su correcto funcionamiento. Los parámetros de configuración más comunes son:

1. **Conexión con servidores.** Configuración del cliente para conectarse al servidor (local o remoto).

2. **Acceso a la base de datos.** Parámetros para acceder a la base de datos (usuario, contraseña, dirección IP).

3. **Configuración del idioma.** Cambiar el idioma de la aplicación mediante archivos de configuración o módulos específicos.

4. **Archivos de localización del país.** Adaptar el sistema a las leyes y necesidades del país (por ejemplo, el Plan General Contable español).

**Ejemplo.**
- **Openbravo.** No requiere configuración adicional tras la instalación. Se accede a través del navegador web.
- **OpenERP.** Requiere configurar el acceso a la base de datos y al servidor, tanto para el cliente de escritorio como para el cliente web.

### 2.4. **Configuración del servidor y de la base de datos**

Para configurar el servidor y la base de datos en OpenERP, se siguen estos pasos:

1. **Editar el archivo de configuración de la base de datos.** Modificar el archivo `pg_hba.conf` para permitir conexiones con autenticación MD5.

2. **Reiniciar el servidor de la base de datos.**- Ejecutar el comando `sudo /etc/init.d/postgresql-8.4 restart`.

3. **Crear un usuario en la base de datos.** Crear un usuario (por ejemplo, `userbd`) con una contraseña (por ejemplo, `userbdpass`).

4. **Modificar los parámetros de conexión en el archivo de configuración del servidor.** Editar el archivo `openerp-server.conf` para configurar el nombre de la base de datos, usuario, contraseña y archivo de registro.

5. **Reiniciar el servidor OpenERP.** Ejecutar `sudo /etc/init.d/openerp-server restart`.

### 2.5. **Servicio de acceso para el cliente de escritorio**

Para configurar el cliente de escritorio en OpenERP:

1. **Conectar al servidor.**
   - Introducir la dirección IP del servidor (o `localhost` si es una instalación monopuesto).
   - Especificar el puerto (por ejemplo, 8070 para NET-RPC o 8069 para XML-RPC).

1. **Crear una nueva base de datos.** Especificar el nombre de la base de datos, el idioma (español) y la contraseña del administrador.

2. **Iniciar el asistente de instalación.** Seleccionar el perfil mínimo y configurar los datos de la empresa.

3. **Crear usuarios.** Crear usuarios adicionales además del administrador.

### 2.6. **Servicio de acceso para el cliente web**

Para configurar el cliente web en OpenERP:

1. **Editar el archivo de configuración.** Modificar el archivo `openerp-web.conf` para especificar la dirección IP del servidor y el puerto (por ejemplo, 8080).

2. **Iniciar el cliente web.** Ejecutar el script `./openerp-web.py` en el directorio de instalación.

3. **Acceder al ERP.** Abrir el navegador y conectarse a la dirección `http://IP_Servidor:8080`.
   - Introducir el usuario y la contraseña para acceder a la aplicación.

### 2.7. **Actualización del sistema ERP/CRM**

Las actualizaciones de los sistemas ERP/CRM pueden ser:

1. **Automáticas.** Para versiones secundarias o parches (por ejemplo, de 6.0.15 a 6.0.16).

2. **Manuales.**
   - Para cambios de versión principales (por ejemplo, de 6.0.15 a 7.0.0).
   - Requieren la instalación manual de la nueva versión y, en algunos casos, un traspaso de datos.

En entornos de producción, las actualizaciones deben planificarse cuidadosamente, considerando el impacto en los procesos de la empresa y la necesidad de formación adicional para los usuarios.

## 3. Tipos de módulos. Características funcionales. Descripción e Interconexión

> [!done] Caso práctico 
> *Con Ada fuera por una reunión, María y Juan se ponen manos a la obra. María explica a Juan la diferencia entre el **módulo base** (el núcleo del ERP) y los **módulos adicionales** (como compras, ventas, almacén, contabilidad, etc.). Juan, que siempre ha sido más de "prueba y error", se emociona al descubrir que pueden adaptar el ERP a diferentes tipos de empresas. Además, los clientes del sector servicios están pidiendo a gritos un módulo CRM para gestionar llamadas y contactos.*

Un sistema ERP está compuesto por **módulos**, que son programas diseñados para cubrir funciones específicas dentro de la aplicación. Estos módulos pueden instalarse durante la configuración inicial o añadirse posteriormente según las necesidades de la empresa. Las características principales de los módulos incluyen:

- **Instalación y desinstalación mediante asistentes.**
- **Configuración o parametrización** para adaptarse al entorno de producción.
- **Generación de informes** específicos para cada módulo.
- **Niveles de seguridad** que restringen el acceso a ciertos módulos.
- **Interconexión entre módulos**, lo que permite compartir información sin duplicar datos.
- **Personalización de menús** según las necesidades del usuario.

### 3.1. **Módulo base**

El **módulo base** es el núcleo del ERP y contiene las funcionalidades esenciales para que la aplicación funcione. Algunas de las características principales del módulo base son:

- **Configuración de la aplicación.** Ajustes iniciales para el funcionamiento del sistema.
- **Gestión de datos maestros.** Introducción y mantenimiento de datos básicos (clientes, proveedores, productos, etc.).
- **Establecimiento del idioma.** Configuración del idioma de la aplicación.
- **Seguridad.** Gestión de usuarios y permisos de acceso.
- **Administración de módulos.** Instalación y desinstalación de módulos adicionales.

**Ejemplos de módulos base.**
- **Openbravo.** Incluye funcionalidades de gestión de ventas y comercial.
- **OpenERP.** Compuesto por los módulos **Empresas** (ficha de cliente) y **Administración** (para añadir más funcionalidades).

Además del módulo base, existen **módulos adicionales** que amplían las capacidades del ERP, como:

- **Gestión contable y financiera.**
- **Compras, ventas y almacén.**
- **Facturación.**
- **Gestión de personal.**
- **Gestión de relaciones con el cliente (CRM).**

### 3.2. **Gestión contable y financiera**

Este módulo automatiza y centraliza todas las operaciones contables de la empresa. Está integrado con otros módulos (compras, ventas, etc.) para evitar duplicidades y garantizar la coherencia de los datos.

**Funcionalidades principales.**
- **Contabilidad general y analítica.**
- **Gestión de impuestos.**
- **Presupuestos.**
- **Facturas de clientes y proveedores.**
- **Extractos de cuentas bancarias.**
- **Informes contables.**

**Ejemplo.** Si un cliente es marcado como moroso, el módulo contable bloquea cualquier acción relacionada con él hasta que se resuelva la situación.

### 3.3. **Compras, Ventas y Almacén**

#### Módulo de Compras

Gestiona las operaciones de compra, desde la solicitud de presupuestos hasta la recepción de productos.

**Funcionalidades.**
- Seguimiento de tarifas de proveedores.
- Generación automática de pedidos de compra.
- Gestión de entregas parciales.
- Reclamaciones a proveedores.

#### Módulo de Ventas

Gestiona las operaciones de venta, desde la creación de pedidos hasta la facturación.

**Funcionalidades.**
- Creación y revisión de pedidos de venta.
- Confirmación de envíos.
- Gestión de formas de pago y fechas de facturación.
- Generación automática de albaranes.

#### Módulo de Almacén

Controla las existencias de productos en el almacén.

**Funcionalidades.**
- Definición de múltiples almacenes.
- Gestión de niveles de stock y rotación de inventario.
- Traspasos entre almacenes.
- Codificación y numeración de productos.

### 3.4. **Facturación**

Este módulo se encarga de la generación de facturas, albaranes y otros documentos relacionados con la facturación.

**Funcionalidades.**
- Configuración de formas de pago (contado, transferencia, pagaré, etc.).
- Generación automática de facturas desde pedidos o albaranes.
- Gestión de recibos, órdenes de pago y transferencias.
- Importación de extractos bancarios.
- Envío telemático de remesas al banco.

### 3.5. **Gestión de Personal**

Este módulo gestiona las nóminas, contratos, horarios y otros aspectos relacionados con los empleados.

**Funcionalidades.**
- Gestión de empleados y calendario de vacaciones.
- Control de contratos y beneficios.
- Gestión de ausencias y rendimiento.
- Cálculo de comisiones por ventas.

### 3.6. **Gestión de las relaciones con el cliente (CRM)**

El módulo CRM centraliza toda la información relacionada con los clientes, optimizando los procesos de gestión comercial.

**Funcionalidades.**
- Creación de fichas de clientes.
- Segmentación de clientes (reales y potenciales).
- Gestión de llamadas y calendario de encuentros.
- Seguimiento de campañas de marketing.
- Herramientas de productividad (editor de documentos, envíos masivos por correo, etc.).
- Estadísticas y análisis de datos.

**Ejemplo.** OpenERP incluye un módulo CRM independiente, mientras que Openbravo integra estas funcionalidades en los módulos de ventas y facturación.

### 3.7. **Introducción a la instalación y configuración de módulos**

La instalación de módulos adicionales permite ampliar las funcionalidades del ERP. Un módulo clave es el de **localización del país**, que adapta el sistema a las leyes y normas específicas de cada región.

**Ejemplo de localización española.**
- **Plan General Contable Español.**
- **Tipos de IVA.**
- **Validación de datos** (CIF, NIF, cuentas bancarias).
- **Datos maestros** (provincias de España).
- **Traducción al español.**

#### Instalación en Openbravo
1. Acceder al menú **Configuración General/Aplicación/Gestión de módulos/Añadir módulos.**
2. Buscar el módulo de localización española y hacer clic en **Instalar ahora.**
3. Configurar el idioma español en **Opciones de sesión.**

#### Instalación en OpenERP
- Se detallará en unidades posteriores.

## 4. Asistencia técnica remota en el sistema ERP-CRM

> [!done] Caso práctico 
> *Ada, siempre un paso adelante, les pide a María y Juan que investiguen soluciones de **soporte remoto** para atender a clientes lejanos sin tener que viajar. María, que ya se siente cómoda con los webinars, sugiere usar herramientas como **VNC** para conectarse a los equipos de los clientes. Juan, mientras tanto, imagina cómo sería trabajar en pijama desde casa mientras resuelve problemas técnicos. Ada les recuerda que, aunque suene divertido, el soporte remoto es una solución seria para mejorar la atención al cliente.* 

La **asistencia técnica remota** permite controlar un equipo desde otro dispositivo, como si estuviéramos físicamente frente a él. Esta herramienta es especialmente útil en situaciones como:

- **Revisión de prácticas o resolución de dudas.** Un profesor puede conectarse al ordenador de un alumno para revisar su trabajo.
- **Asistencia técnica a clientes.** Las empresas pueden ofrecer soporte inmediato sin necesidad de desplazamientos, reduciendo costes.

Para realizar estas conexiones, se utilizan programas basados en el protocolo **VNC (Virtual Network Computing)**, que sigue una estructura cliente/servidor:

- **Cliente.** El equipo desde el que se controla el servidor.
- **Servidor.** El equipo que se desea controlar.

Al ejecutar la aplicación VNC en el cliente, se abre una ventana que muestra el escritorio del servidor, permitiendo visualizar archivos, ejecutar programas y realizar configuraciones como si se estuviera físicamente frente al equipo.

### 4.1. **Instalación y configuración en servidores Ubuntu**

Para configurar el soporte remoto en servidores Ubuntu, se pueden utilizar aplicaciones como **VINO** (servidor) y **RealVNC** o **TightVNC** (cliente). Los pasos generales son:

1. **Instalar el servidor VNC.**
   - Ejecutar el comando: `sudo apt-get install vino`.
2. **Configurar el servidor.**
   - Establecer una contraseña de conexión.
   - Habilitar el acceso remoto en las opciones de configuración.
3. **Conectar desde el cliente.**
   - Ejecutar el visor VNC (por ejemplo, `vncviewer`).
   - Introducir la dirección IP del servidor y la contraseña.

### 4.2. **Instalación y configuración en servidores Windows**

En Windows, una de las aplicaciones más utilizadas es **UltraVNC**, que incluye tanto el cliente como el servidor.

**Pasos para configurar el servidor.**
1. **Instalar UltraVNC.**
2. **Ejecutar el servidor.**
   - Acceder a `Inicio/Programas/UltraVNC/UltraVNC server`.
3. **Establecer la contraseña.**
   - Hacer clic derecho en el icono del servidor y seleccionar `Admin Properties`.
   - Introducir la contraseña en el apartado `Authentication-VNC Password`.

**Pasos para conectar desde el cliente.**
1. Ejecutar el visor VNC (por ejemplo, `UltraVNC viewer`).
2. Introducir la dirección IP del servidor y la contraseña.

**Nota.** Si hay un cortafuegos (firewall), es posible que sea necesario desactivarlo temporalmente o abrir los puertos **5900-5999** en el router para permitir la conexión.

### 4.3. **Conexión remota por VNC inverso**

El **VNC inverso** es una variante en la que el servidor solicita la conexión al cliente, en lugar de ser el cliente quien se conecta al servidor. Esto es útil cuando hay restricciones de cortafuegos o problemas de conectividad.

**Pasos para configurar VNC inverso.**

1. **Ejecutar el visor VNC en modo escucha** (en el cliente):
   - En Ubuntu, abrir un terminal y ejecutar: `vncviewer –listen`.
2. **Ejecutar el servidor VNC** (en el equipo a controlar):
   - En Windows, acceder a `Inicio/Programas/UltraVNC/UltraVNC server`.
3. **Establecer la conexión desde el servidor.**
   - Hacer clic derecho en el icono del servidor y seleccionar `Add new client`.
   - Introducir la dirección IP del cliente seguida de `:0` (por ejemplo, `192.168.1.128:0`).

Si los puertos están correctamente configurados en el router, aparecerá una ventana en el cliente mostrando el escritorio del servidor.

## 5. Herramientas para la programación de sistemas ERP/CRM

> [!done] Caso práctico 
> Ada le encarga a Juan que investigue las **herramientas de programación** disponibles para desarrollar módulos personalizados en los ERP. Juan, que siempre ha sido un fanático de los atajos, descubre que herramientas como **NetBeans**, **Eclipse** y **iReport** pueden hacer su vida mucho más fácil. Ada le recuerda que el verdadero desafío es hacer que los módulos funcionen sin errores. 

Una vez dominada la instalación y configuración básica de un ERP/CRM, el siguiente paso es **desarrollar nuevos módulos** para añadir funcionalidades personalizadas. Para ello, se utilizan entornos de programación y herramientas específicas.

### 5.1. **Entornos de programación**

Los entornos de programación permiten desarrollar, probar y ejecutar módulos para el ERP/CRM. Algunos de los más utilizados son:

- **NetBeans.** Entorno de desarrollo integrado (IDE) que soporta múltiples lenguajes, como Java y PHP.
- **Eclipse.** IDE ampliamente utilizado para desarrollar aplicaciones en Java, aunque también soporta otros lenguajes.

Estos entornos suelen requerir la instalación de **plugins** o extensiones adicionales para soportar el lenguaje de programación utilizado por el ERP.

### 5.2. **Otras herramientas de programación**

Además de los entornos de desarrollo, existen otras herramientas útiles para la programación de sistemas ERP/CRM:

1. **Dia.**
   - Programa para crear diagramas, incluidos diagramas UML.
   - Permite crear módulos **uml-dia** escritos en Python, que pueden integrarse en OpenERP.

2. **Gedit.**
   - Editor de texto con soporte para programación.
   - Puede extenderse con plugins para facilitar la creación y modificación de módulos.

3. **OpenOffice.**
   - Paquete ofimático que permite crear y modificar informes del ERP.
   - Ideal para usuarios que desean personalizar informes sin necesidad de programación avanzada.

4. **iReport.**
   - Herramienta visual para diseñar informes en **JasperReports.**
   - Facilita la creación de informes complejos de manera intuitiva.

### 5.3. **Desarrollo de módulos personalizados**

El desarrollo de módulos personalizados implica:

1. **Identificar necesidades.** Determinar qué funcionalidades adicionales requiere la empresa.
2. **Diseñar el módulo.** Crear diagramas UML y definir la estructura del módulo.
3. **Programar el módulo.** Utilizar el entorno de desarrollo y las herramientas adecuadas.
4. **Integrar el módulo.** Añadir el nuevo módulo al ERP/CRM y realizar pruebas de funcionamiento.

**Ejemplo.** Si una empresa necesita un módulo específico para gestionar comisiones de ventas, se puede desarrollar un módulo personalizado en Python y integrarlo en OpenERP.
