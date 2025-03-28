---
banner: "![[di.jpg]]"
banner_y: 0.76
number headings: max 2, _.1.1., skip ^sk
cssclasses:
  - dam-di
  - table-compact-clean
tags:
  - DAM
  - DI
---

# **Resumen Tema 1.** <br> Confección de Interfaces

## 1. Elaboración de Interfaces de Usuario

### Definición

La interfaz de usuario permite la comunicación entre el usuario y la aplicación.

### Tipos de interfaces

| Tipo       | Descripción                                                                 |
|------------|-----------------------------------------------------------------------------|
| **Textuales**       | Comandos escritos.                                                              |
| **Gráficas**        | Iconos y menús (más comunes).                                                   |
| **Táctiles**        | Pantallas táctiles (dispositivos móviles, terminales de venta).                 |

## 2. Componentes

### Componentes típicos

| Componente          | Descripción                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| **Etiquetas**               | Textos fijos.                                                                   |
| **Campos de texto**         | Entrada de datos (una línea).                                                   |
| **Áreas de texto**          | Entrada de párrafos.                                                            |
| **Botones**                 | Ejecutan acciones.                                                              |
| **Botones de radio**        | Selección única.                                                                |
| **Cuadros de verificación** | Selección múltiple.                                                             |
| **Imágenes**                | Información visual.                                                             |
| **Password**                | Campos de texto ocultos.                                                        |
| **Listas**                  | Selección de datos.                                                             |
| **Listas desplegables**     | Combinan texto y lista.                                                         |

### Bibliotecas de componentes

| Biblioteca               | Descripción                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| **Java Foundation Classes (JFC)** | AWT (en desuso) y Swing (estándar actual).                                      |
| **Bibliotecas de Microsoft**      | .NET Framework (Windows Forms, WPF).                                            |
| **Bibliotecas basadas en XML**    | Interfaces traducibles a diferentes lenguajes.                                  |
| **Otras API**                     | DirectX (multimedia), GTK (GNOME), Qt (KDE).                                    |

## 3. Herramientas para la Elaboración de Interfaces

### Principales IDE

| IDE               | Descripción                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| **Microsoft Visual Studio** | Desarrollo en .NET (C++, C#, ASP).                                             |
| **NetBeans**               | Multiplataforma, compatible con Java, C++, PHP, Python.                        |
| **Eclipse**                | Modular, ligero, soporta pruebas unitarias y control de versiones.             |
| **JDeveloper**             | Oracle, para Java, HTML, SQL, PHP.                                             |
| **Aptana Studio**          | Especializado en interfaces web.                                               |
| **Dreamweaver**            | Diseño web (ASP.NET, PHP, JavaScript).                                         |
| **Komodo Edit**            | Depende de Python.                                                             |

### NetBeans

| Aspecto            | Descripción                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| **Ventajas**               | Multiplataforma, facilita la colocación de componentes, genera código automáticamente. |
| **Configuración inicial**  | 1. Crear proyecto **Java Application.**<br>2. Añadir formulario **JFrame.**<br>3. Configurar clase principal. |

## 4. Contenedores

### Contenedores de nivel superior

| Contenedor | Descripción                                                                 |
|------------|-----------------------------------------------------------------------------|
| **JFrame**         | Ventana estándar.                                                               |
| **JDialog**        | Diálogos (pueden ser modales).                                                  |
| **JApplet**        | Ejecución en páginas web.                                                       |

### Contenedores secundarios

| Contenedor | Descripción                                                                 |
|------------|-----------------------------------------------------------------------------|
| **JPanel**         | Organización de controles.                                                      |
| **JTabbedPane**    | Pestañas.                                                                       |
| **JSplitPane**     | Dos componentes con espacio dinámico.                                           |
| **JScrollPane**    | Desplazamiento automático.                                                      |
| **JOptionPane**    | Diálogos prediseñados.                                                          |
| **JFileChooser**   | Selección de archivos.                                                          |
| **JColorChooser**  | Selector de colores.                                                            |
| **JMenu**          | Creación de menús.                                                              |
| **JToolBar**       | Iconos de acceso rápido.                                                        |
| **JInternalFrame** | Ventanas internas.                                                              |

## 5. Componentes de la Interfaz

| Tipo            | Descripción                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| **Componentes pasivos** | Muestran información (etiquetas, imágenes).                                     |
| **Componentes activos** | Recogen información (cuadros de texto, botones).                                |

### Añadir y eliminar componentes

| Acción         | Descripción                                                                 |
|----------------|-----------------------------------------------------------------------------|
| **Paleta de NetBeans** | Contenedores, controles, menús, ventanas.                                       |
| **Añadir**             | Seleccionar y hacer clic en la interfaz.                                        |
| **Eliminar**           | Seleccionar y pulsar "Supr".                                                   |

### Modificación de propiedades

| Propiedad   | Descripción                                                                 |
|-------------|-----------------------------------------------------------------------------|
| **Nombre**          | Identificación en el código.                                                   |
| **ToolTipText**     | Descripción breve.                                                             |

### Añadir funcionalidad

| Aspecto      | Descripción                                                                 |
|--------------|-----------------------------------------------------------------------------|
| **NetBeans**         | Genera código, pero es necesario personalizarlo.                                |

### Ubicación y alineamiento

| Layout       | Descripción                                                                 |
|--------------|-----------------------------------------------------------------------------|
| **BorderLayout**     | Disposición en bordes.                                                          |
| **GridLayout**       | Disposición en cuadrícula.                                                      |
| **GridBagLayout**    | Disposición flexible en cuadrícula.                                             |
| **CardLayout**       | Disposición en capas.                                                           |
| **BoxLayout**        | Disposición en caja.                                                            |
| **FlowLayout**       | Disposición en flujo.                                                           |
| **GroupLayout**      | Disposición horizontal y vertical en NetBeans.                                  |
| **SpringLayout**     | Disposición basada en restricciones.                                            |

### Enlace a bases de datos

| Paso         | Descripción                                                                 |
|--------------|-----------------------------------------------------------------------------|
| **Preparativos**     | Instalar MySQL, crear base de datos, registrar servidor en NetBeans.            |
| **Crear proyecto**   | Añadir formulario y conectar con la base de datos.                              |
| **Formularios maestro-detalle** | Mostrar datos relacionados de varias tablas.                              |

## 6. Resumen final

| Aspecto      | Descripción                                                                 |
|--------------|-----------------------------------------------------------------------------|
| **Interfaces gráficas** | Esenciales para la interacción usuario-aplicación.                             |
| **Componentes**       | Etiquetas, botones, listas, organizados en contenedores (JFrame, JPanel).       |
| **NetBeans**          | IDE recomendado para desarrollar interfaces gráficas en Java con Swing.         |
| **Layouts**           | Definen la disposición de los componentes en la interfaz.                       |
| **Enlace a bases de datos** | Permite mostrar y gestionar datos desde la interfaz.                        |
