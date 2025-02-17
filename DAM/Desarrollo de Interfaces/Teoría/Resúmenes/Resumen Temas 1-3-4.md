---
number headings: first-level 0, start-at 1, max 2, _.1., auto, contents ^toc, skip ^skipped
tags: []
---
# TEMA 1. Confección de interfaces

![Lectura MP3](Lectura_Resumen_Temas_1-3-4.mp3)

---
## 1. Tipos de interfaces de usuario

- **Textuales** → Comunicación por medio de inserción de texto por órdenes.
- **Gráficas** → Elementos visuales con los que se interacciona.
- **Táctiles** → Comunicación mediante dispositivo táctil.

---
## 2. Componentes

Un **componente** es un objeto con representación gráfica, que se muestra en pantalla y con el que se puede interactuar.

#### 2.1. Java Foundation Classes (JFC)

- **AWT** → Primera biblioteca para crear interfaces gráficas.
- **Swing** → Componentes multiplataforma derivados de AWT (ejemplo: `JButton`).

---
## 3. Contenedores

#### 3.1. Contenedor de nivel superior

- **JFrame** → Formulario con título, botones de min/max y barra de menú.
- **JDialog** → Formulario para solicitar información al usuario (modal o no modal).

#### 3.2. Contenedores secundarios

- **JPanel** → Contenedor intermedio para colocar controles.
- **JMenu** → Creación de menús de opciones.
- **JToolBar** → Contiene iconos de acceso a opciones de la aplicación.
- **JTabbedPane** → Distribuye elementos en pestañas.
- **JScrollPane** → Permite desplazar el contenido.
- **JInternalFrame** → Ventanas hijas dentro de la ventana principal.
- **JSplitPane** → Divide la ventana en dos áreas visualizables.

#### 3.3. Otros contenedores secundarios

- **JOptionPane** → Ventana de confirmación con botones.
- **JFileChooser** → Permite seleccionar archivos del sistema.
- **JColorChooser** → Selector de color.

---
## 4. Layouts

Un **layout** define cómo se organizan los componentes en la interfaz.

- **BorderLayout** → Ubica componentes en `Norte`, `Sur`, `Este`, `Oeste` y `Centro`.
- **GridLayout** → Organiza por filas y columnas.
- **GridBagLayout** → Similar a `GridLayout`, pero permite el uso de más de una celda.
- **CardLayout** → Permite alternar entre distintos paneles en ejecución.
- **BoxLayout** → Organiza los componentes en fila o columna.
- **FlowLayout** → Alinea los componentes de izquierda a derecha.
- **GroupLayout** → Permite definir la posición exacta de los componentes.
- **SpringLayout** → Flexible, permite especificar los límites de los componentes.

---
## 5. Diálogos modales y no modales

Un **diálogo modal** bloquea la interacción con otras ventanas hasta que se cierre.

```java
JDialog dialogo_Modal = new JDialog(ventana, true);
```

Un **diálogo no modal** permite interactuar con otras ventanas simultáneamente.

```java
JDialog dialogo_NoModal = new JDialog(ventana, false);
```


# TEMA 3. Creación de componentes visuales

---
## 1. Características de un componente

Un componente se define por su **estado**, almacenado en propiedades que pueden modificarse. Los **eventos** son acciones provocadas por el usuario sobre los componentes.

---
## 2. Propiedades y atributos de un componente

Las propiedades pueden afectar la apariencia o el comportamiento de un componente.

#### 2.1. Getter y Setter

- **Getter**: Obtiene el valor de una propiedad.
  ```java
  public String getColor() { return this.color; }
  ```
- **Setter**: Establece el valor de una propiedad.
  ```java
  public void setColor(String color) { this.color = color; }
  ```
- **Propiedad de solo lectura** (sin setter):
  ```java
  public boolean isTieneSombra() { return tieneSombra; }
  ```

---
## 3. Eventos y asociación de acciones

Los **eventos** son acciones generadas por el usuario sobre un componente.

- **ActionEvent** → Ocurre cuando se presiona un botón.
- **MouseEvent** → Ocurre cuando se interactúa con el ratón.
- **KeyEvent** → Ocurre al presionar o soltar una tecla.
- **FocusEvent** → Un componente gana o pierde el foco.

Ejemplo de **ActionListener**:

```java
boton.addActionListener(new ActionListener() {
    public void actionPerformed(ActionEvent e) {
        System.out.println("Botón pulsado");
    }
});
```


# TEMA 4. Usabilidad 

---
## 1. Concepto de usabilidad

La **usabilidad** se refiere a qué tan fácil es para un usuario interactuar con la interfaz.

- **Útil** → Debe cumplir con las tareas para las que fue diseñada.
- **Fácil de usar** → Debe ser eficiente y minimizar errores.
- **Fácil de aprender** → Debe ser intuitiva.
- **Consistencia** → Las acciones deben comportarse de la misma manera en toda la aplicación.

---
## 2. Pruebas de usabilidad

- **Evaluación heurística** → Comparación de la interfaz con principios de diseño.
- **Revisión de normas** → Verificación de cumplimiento de estándares.
- **Inspección de consistencia** → Uniformidad en la interfaz.
- **Caminata cognitiva** → Simulación del recorrido del usuario en tareas específicas.

---
## 3. Diseño visual

- **Color** → Uso limitado de colores apagados y contrastes adecuados.
- **Disposición de elementos** → Debe ser lógica y clara.
- **Mensajes** → Cortos, directos y con gramática clara.

---
## 4. Elementos clave de la interfaz

#### 4.1. Menús
- **Menús de barra** → Ubicados en la parte superior.
- **Menús contextuales** → Aparecen al hacer clic derecho.

#### 4.2. Ventanas
Las ventanas pueden minimizarse, maximizarse y moverse según las necesidades del usuario.

#### 4.3. Atajos de teclado
Permiten aumentar la eficiencia en acciones frecuentes.

#### 4.4. Colores
- No más de **4-5 colores** en una ventana.
- Uso de colores para **indicaciones** (rojo para errores, verde para confirmaciones).

#### 4.5. Iconos
- **Claridad** → Deben representar su función.
- **Consistencia** → Mismo estilo en toda la interfaz.

#### 4.2. Fuentes
Deben ser **legibles** y proporcionales a la pantalla.

---
## 5. Diseño de la secuencia de control

1. Crear la interfaz dibujando los controles.
2. Establecer las propiedades de los objetos.
3. Escribir el código de respuesta a eventos.
4. Guardar el proyecto y generar el ejecutable.