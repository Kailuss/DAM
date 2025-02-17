---
number headings: first-level 4, start-at 1, max 4, 1., auto, contents ^toc, skip ^skipped
tags: []
---
### Esquema de Estudio: TEMA 1. Confección de Interfaces

![Lectura MP3](DAM/Desarrollo%20de%20Interfaces/Teoría/Lecturas/Lectura_Resumen_Tema_1.mp3)

---
#### 1. Elaboración de Interfaces de Usuario
##### Definición
La interfaz de usuario permite la comunicación entre el usuario y la aplicación.
##### Tipos de interfaces
- **Textuales**: Comandos escritos.
- **Gráficas**: Iconos y menús (más comunes).
- **Táctiles**: Pantallas táctiles (dispositivos móviles, terminales de venta).

---
#### 2. Componentes
##### Componentes típicos
- **Etiquetas**: Textos fijos.
- **Campos de texto**: Entrada de datos (una línea).
- **Áreas de texto**: Entrada de párrafos.
- **Botones**: Ejecutan acciones.
- **Botones de radio**: Selección única.
- **Cuadros de verificación**: Selección múltiple.
- **Imágenes**: Información visual.
- **Password**: Campos de texto ocultos.
- **Listas**: Selección de datos.
- **Listas desplegables**: Combinan texto y lista.
##### Bibliotecas de componentes
- **Java Foundation Classes (JFC)**: AWT (en desuso) y Swing (estándar actual).
- **Bibliotecas de Microsoft**: .NET Framework (Windows Forms, WPF).
- **Bibliotecas basadas en XML**: Interfaces traducibles a diferentes lenguajes.
- **Otras API**: DirectX (multimedia), GTK (GNOME), Qt (KDE).

---
#### 3. Herramientas para la Elaboración de Interfaces
##### Principales IDE
- **Microsoft Visual Studio**: Desarrollo en .NET (C++, C#, ASP).
- **NetBeans**: Multiplataforma, compatible con Java, C++, PHP, Python.
- **Eclipse**: Modular, ligero, soporta pruebas unitarias y control de versiones.
- **JDeveloper**: Oracle, para Java, HTML, SQL, PHP.
- **Aptana Studio**: Especializado en interfaces web.
- **Dreamweaver**: Diseño web (ASP.NET, PHP, JavaScript).
- **Komodo Edit**: Depende de Python.
##### NetBeans
- **Ventajas**: Multiplataforma, facilita la colocación de componentes, genera código automáticamente.
- **Configuración inicial**:
  1. Crear proyecto **Java Application**.
  2. Añadir formulario **JFrame**.
  3. Configurar clase principal.

---
#### 4. Contenedores
##### Contenedores de nivel superior
- **JFrame**: Ventana estándar.
- **JDialog**: Diálogos (pueden ser modales).
- **JApplet**: Ejecución en páginas web.

##### Contenedores secundarios
- **JPanel**: Organización de controles.
- **JTabbedPane**: Pestañas.
- **JSplitPane**: Dos componentes con espacio dinámico.
- **JScrollPane**: Desplazamiento automático.
- **JOptionPane**: Diálogos prediseñados.
- **JFileChooser**: Selección de archivos.
- **JColorChooser**: Selector de colores.
- **JMenu**: Creación de menús.
- **JToolBar**: Iconos de acceso rápido.
- **JInternalFrame**: Ventanas internas.

---
#### 5. Componentes de la Interfaz
- **Componentes pasivos**: Muestran información (etiquetas, imágenes).
- **Componentes activos**: Recogen información (cuadros de texto, botones).
##### Añadir y eliminar componentes
- **Paleta de NetBeans**: Contenedores, controles, menús, ventanas.
- **Añadir**: Seleccionar y hacer clic en la interfaz.
- **Eliminar**: Seleccionar y pulsar "Supr".
##### Modificación de propiedades
- **Nombre**: Identificación en el código.
- **ToolTipText**: Descripción breve.
##### Añadir funcionalidad
- NetBeans genera código, pero es necesario personalizarlo.
##### Ubicación y alineamiento
- **Layouts**: BorderLayout, GridLayout, GridBagLayout, CardLayout, BoxLayout, FlowLayout, GroupLayout, SpringLayout.
- **GroupLayout**: Disposición horizontal y vertical en NetBeans.
##### Enlace a bases de datos
- **Preparativos**: Instalar MySQL, crear base de datos, registrar servidor en NetBeans.
- **Crear proyecto**: Añadir formulario y conectar con la base de datos.
- **Formularios maestro-detalle**: Mostrar datos relacionados de varias tablas.

---
### Resumen final
- Las interfaces gráficas son esenciales para la interacción usuario-aplicación.
- Los componentes (etiquetas, botones, listas) se organizan en contenedores (JFrame, JPanel).
- NetBeans es un IDE recomendado para desarrollar interfaces gráficas en Java con Swing.
- Los Layouts definen la disposición de los componentes en la interfaz.
- Es posible enlazar interfaces con bases de datos para mostrar y gestionar datos.