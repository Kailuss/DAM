---
number headings: first-level 0, start-at 1, max 2, _.1., auto, contents ^toc, skip ^skipped
tags:
  - Contenido/DI
---
![Lectura MP3](Lectura_Tema_1_Confección_de_interfaces.mp3)
## 1. Elaboración de interfaces de usuario

La interfaz de usuario es el elemento que permite al usuario comunicarse con una aplicación. Actualmente, el desarrollo de aplicaciones requiere dedicar un tiempo significativo a planificar, analizar, diseñar, implementar y probar las interfaces, ya que son esenciales para que el usuario interactúe con la aplicación y realice las funciones para las que fue diseñada.

**Tipos de interfaces de usuario:**

1. **Textuales**: La comunicación se realiza mediante órdenes escritas en un intérprete de comandos.
2. **Gráficas**: Utilizan elementos visuales como iconos y menús, manejados normalmente con un ratón u otro dispositivo apuntador. Son las más comunes y han facilitado el acceso a la informática para usuarios noveles.
3. **Táctiles**: Permiten interactuar a través de pantallas táctiles que reaccionan al contacto con elementos apuntadores o dedos. Son frecuentes en dispositivos móviles, terminales de venta y diseño gráfico.

En esta unidad, se estudiará la creación de interfaces gráficas, formadas por ventanas o formularios que contienen elementos visuales llamados controles o componentes. Estos elementos permiten al usuario dar órdenes o recibir información al interactuar con ellos.

---
## 2. Componentes

Una interfaz gráfica combina diversos elementos gráficos, llamados componentes o controles, para que el usuario pueda realizar peticiones y recibir resultados de la aplicación. Cada componente tiene características específicas y cumple funciones concretas.

### 2.1. Componentes típicos

- **Etiquetas**: Textos fijos en la interfaz, no interactivos.
- **Campos de texto**: Cuadros de una sola línea para ingresar datos.
- **Áreas de texto**: Cuadros de varias líneas para escribir párrafos.
- **Botones**: Áreas rectangulares que ejecutan acciones al pulsarse.
- **Botones de radio**: Botones circulares agrupados que permiten seleccionar un único elemento. El botón marcado se representa con un círculo.
- **Cuadros de verificación**: Rectángulos que se marcan con un tic para seleccionar opciones. Pueden seleccionarse varios a la vez.
- **Imágenes**: Elementos gráficos que aportan información visual.
- **Password**: Campos de texto donde los caracteres aparecen ocultos para proteger información confidencial.
- **Listas**: Cuadros con un conjunto de datos para elegir uno o varios.
- **Listas desplegables**: Combinan cuadro de texto y lista. Permiten escribir un dato o seleccionarlo de una lista oculta que puede desplegarse.
---
### 2.2. Bibliotecas de componentes

Los componentes suelen estar agrupados en bibliotecas, que también permiten crear nuevos componentes personalizados. Estas bibliotecas son colecciones de clases utilizadas en proyectos para desarrollar interfaces gráficas. La elección de una biblioteca depende del lenguaje de programación o el entorno de desarrollo.

**Bibliotecas destacadas:**

1. **Java Foundation Classes (JFC)**:
    - **AWT**: Primera biblioteca de Java para interfaces gráficas. Multiplataforma, pero con componentes dependientes de código nativo. Actualmente en desuso.
    - **Swing**: Biblioteca posterior y multiplataforma sin código nativo. Deriva de AWT; muchos componentes tienen nombres similares, con una "J" añadida (por ejemplo, `Button` en AWT es `JButton` en Swing). Es el estándar actual en Java.
2. **Bibliotecas de Microsoft (C#, ASP, .NET)**:
    - **.NET Framework**: Incluye bibliotecas como ADO.NET, ASP.NET, Windows Forms y WPF (Windows Presentation Foundation) para desarrollar interfaces gráficas.
3. **Bibliotecas basadas en XML**:
    - Permiten crear interfaces traducibles a diferentes lenguajes de programación y luego integrarlas en la aplicación.
4. **Otras API destacadas**:
    - **DirectX**: Plataforma de Microsoft para manejar elementos multimedia, con API como Direct3D y DirectSound.
    - **GTK**: Biblioteca de GTK+ utilizada en GNOME. Compatible con lenguajes como C, C++, Java y Python. Maneja widgets como ventanas, etiquetas y pestañas.
    - **Qt**: Biblioteca de KDE, escrita en C++ e integrable en otros lenguajes. Usada en sistemas empotrados (automoción, aeronavegación, electrodomésticos).
---
## 3. Herramientas para la elaboración de interfaces

Las bibliotecas de componentes gráficos permiten crear aplicaciones a través de código, pero habitualmente se utilizan entornos integrados de desarrollo (IDE) para facilitar la tarea. Un IDE proporciona herramientas visuales para incorporar componentes de bibliotecas gráficas de forma sencilla e intuitiva, además de servir como medio de entrada para las acciones del usuario. Algunos de los IDE más utilizados son:

### 3.1. Principales IDE

1. **Microsoft Visual Studio**: Desarrollo de aplicaciones en escritorio, web y móviles usando .NET framework. Compatible con lenguajes como C++, C# y ASP, soportando Windows 7, 8, 10, aplicaciones web y RIA (Rich Internet Applications).
    
2. **NetBeans**: Distribuido por Oracle bajo licencia GNU GPL. Aunque está desarrollado en Java, permite crear aplicaciones en otros lenguajes como C++, PHP, Python y más.
    
3. **Eclipse**: Originalmente de IBM, ahora mantenido por la Fundación Eclipse. Destaca por su modularidad y ligereza, ofreciendo funcionalidades básicas con posibilidad de expansión mediante módulos. Incluye soporte para pruebas unitarias, control de versiones y asistentes para creación de proyectos.
    
4. **JDeveloper**: Entorno desarrollado por Oracle para Java y otros lenguajes como HTML, SQL y PHP. Desde la versión 9i se basa en Java, pero está menos utilizado tras la adquisición de Sun Microsystems por Oracle.
    
5. **Aptana Studio**: Basado en Eclipse, cuenta con un motor especializado para el desarrollo de interfaces web.
    
6. **Dreamweaver**: Herramienta para diseño de interfaces web que también soporta el desarrollo en ASP.NET, PHP, JavaScript, CSS y otros.
    
7. **Komodo Edit**: Sus características dependen de un intérprete de Python.

---
### 3.2. NetBeans

Para los contenidos de esta unidad, se propone NetBeans como IDE utilizando la biblioteca Swing para crear interfaces gráficas. Razones para elegir NetBeans:

- Permite desarrollar aplicaciones de escritorio, web y móviles.
- Distribuido bajo licencias CDDL y GPL2.
- Es multiplataforma y compatible con varios lenguajes.
- Facilita la colocación de componentes en la interfaz gráfica, permitiendo al desarrollador centrarse en el diseño mientras el IDE programa automáticamente la posición de los controles.
- Permite añadir componentes creados por otros desarrolladores a la paleta Swing/AWT.

**Configuración inicial de un proyecto en NetBeans:**

1. Crear un proyecto tipo **Java Application** y configurar datos principales (nombre, ubicación y clase principal).
2. Añadir un formulario Swing:
    - Clic derecho en **Source Packages** → **Nuevo** → **Swing GUI Forms** → **Formulario JFrame**.
    - Nombrar el formulario y finalizar.
3. Configurar la clase principal:
    - Clic derecho en el proyecto → **Propiedades** → **Ejecutar**.
    - Seleccionar la clase principal desde la opción **Main Class**.

---

## 4. Contenedores

Un **formulario** es una ventana básica que actúa como la base para aplicaciones gráficas, donde se añaden controles y componentes. Los contenedores organizan estos elementos, formando una jerarquía de distribución.

**Tipos de contenedores de nivel superior:**

- **JFrame**: Ventana estándar con botones de minimizar, maximizar y cerrar. Puede incluir una barra de menú.
- **JDialog**: Usado para interacciones con el usuario. Puede ser modal (bloquea otras ventanas).
- **JApplet**: Ventana ejecutada dentro de una página web.

**Ejemplo típico:** Crear una ventana principal con **JFrame** y usar **JDialog** para ventanas secundarias.

---
**Contenedores secundarios**

Se usan para distribuir controles en una ventana principal. Tipos principales:

1. **Paneles:**
    
    - **JPanel**: Contenedor genérico para organizar controles.
    - **JTabbedPane**: Divide elementos en pestañas.
    - **JSplitPane**: Muestra dos componentes con espacio dinámico.
    - **JScrollPane**: Agrega desplazamiento automático al contenido.
2. **Opciones específicas:**
    
    - **JOptionPane**: Diálogos prediseñados para mensajes (Aceptar, Cancelar, Sí/No).
    - **JFileChooser**: Selección de archivos.
    - **JColorChooser**: Selector de colores.
3. **Complementos visuales:**
    
    - **JMenu**: Creación de menús.
    - **JToolBar**: Iconos de acceso rápido.
    - **JInternalFrame**: Ventanas internas dentro de una ventana principal.

NetBeans facilita la incorporación de contenedores, generando automáticamente el código necesario.

---
## 5. Componentes de la interfaz

Los componentes o controles gráficos se anidan en contenedores para formar aplicaciones. Se dividen en:

- **Componentes pasivos:** muestran información (etiquetas, imágenes, listas, árboles).
- **Componentes activos:** recogen información del usuario (cuadros de texto, botones, listas de selección).

Cada componente se define por su clase (aspecto y funcionalidad) y su nombre (identificación en la aplicación). Sus propiedades son modificables, como el texto o color.

Los **Layouts** rigen la disposición de los componentes:

- Límites del formulario (norte, sur, este, oeste).
- Rejillas o disposición fluida (una o varias filas).

**Eventos:** Interacciones del usuario que provocan respuestas programadas mediante manejadores de eventos asociados a escuchadores.

**Ampliar:** [Documentación Swing en Oracle](https://docs.oracle.com/javase/tutorial/uiswing/).

---

### 5.1. Añadir y eliminar componentes

En NetBeans, los componentes se añaden desde la **paleta** (ubicada a la derecha del IDE), dividida en:

- **Contenedores Swing:** distribuyen y organizan controles.
- **Controles Swing:** permiten la interacción con el usuario.
- **Menús Swing:** crean menús complejos o contextuales.
- **Ventanas Swing:** agregan ventanas, diálogos, y paneles de opciones.

Para añadir un componente, seleccionarlo en la paleta y hacer clic en la interfaz. Para eliminarlo, seleccionarlo y pulsar "Supr" o "Suprimir" en el menú contextual.

---

### 5.2. Modificación de propiedades

Cada control tiene propiedades adaptables en el panel de propiedades, como:

- **Nombre:** Identifica el control en el código.
- **ToolTipText:** Muestra una breve descripción al usuario.

![](Desarrollo%20de%20Interfaces/Teoría/Imágenes/01/Editor%20de%20propiedades.jpg)

---

### 5.3. Añadir funcionalidad desde NetBeans

NetBeans genera automáticamente parte del código funcional, pero es necesario personalizarlo para que cumpla con las tareas específicas de la aplicación.

---

### 5.4. Ubicación y alineamiento de componentes

Los **Layouts** definen la disposición de los controles:

1. **BorderLayout:** Norte, Sur, Este, Oeste, Centro.
2. **GridLayout:** Rejilla (filas y columnas).
3. **GridBagLayout:** Rejilla flexible (celdas combinables).
4. **CardLayout:** Paneles intercambiables.
5. **BoxLayout:** Fila o columna ajustable.
6. **FlowLayout:** Izquierda a derecha, fila por fila.
7. **GroupLayout:** Disposición horizontal y vertical (NetBeans).
8. **SpringLayout:** Relaciones entre límites de los componentes.

NetBeans facilita la colocación de componentes con guías visuales y el diseño **GroupLayout**.

---

### 5.5. Enlace de componentes a bases de datos

Para vincular un formulario con datos de una base de datos:

1. **Preparativos:**
    - Instalar y ejecutar MySQL.
    - Crear la base de datos (ej.: Agenda).
    - Registrar el servidor MySQL en NetBeans.
2. **Crear proyecto:**
    - Crear proyecto Java sin clase principal.
    - Agregar un paquete para las clases generadas.
    - Añadir formulario de ejemplo/detalle.
3. **Conexión con la base de datos:**
    - Seleccionar la conexión con MySQL y la tabla (ej.: Contactos).
    - Configurar campos y áreas de detalle.
    - Finalizar el asistente.

El formulario incluirá una tabla (JTable) con tres columnas y campos enlazados mediante expresiones como `${SelectedElement.nombre_campo}`.

![](Formulario%20JTable.jpg)

---

#### 5.5.1. Formularios maestro-detalle

Permiten mostrar datos relacionados de varias tablas (ej.: contactos y sus correos). Proceso:

1. Seguir los pasos del apartado anterior hasta configurar las áreas de detalle.
2. Configurar tabla secundaria (ej.: CORREOS) con clave externa.

El formulario resultante mostrará dos tablas sincronizadas, gestionadas por listas generadas automáticamente.

![](Formulario%20Maestro-Detalle.jpg)