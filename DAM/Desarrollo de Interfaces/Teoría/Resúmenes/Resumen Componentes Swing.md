---
tags: [DAM, DI]
cssclasses: [dam-di, table-compact-clean]
banner: "![[di.jpg]]"
banner_y: 0.76
---

# Resumen Componentes Swing

## 1. Componentes básicos

### Etiquetas (JLabel)

Se usan para mostrar texto en la interfaz. No son interactivos.

```java
JLabel etiqueta = new JLabel("Hola Mundo");
```

### Campos de texto (JTextField)

Cuadro de texto de una sola línea donde el usuario puede escribir datos.

```java
JTextField campoTexto = new JTextField("Escribe aquí");
```

### Áreas de texto (JTextArea)

Caja de texto multilínea para escribir párrafos.

```java
JTextArea areaTexto = new JTextArea("Texto largo...");
```

### Botones (JButton)

Área que el usuario puede pulsar para ejecutar una acción.

```java
JButton boton = new JButton("Haz clic");
```

### Botones de radio (JRadioButton)

Permiten elegir solo una opción de un grupo.

```java
JRadioButton radioButton1 = new JRadioButton("Opción 1");
JRadioButton radioButton2 = new JRadioButton("Opción 2");
```

### Cuadros de verificación (JCheckBox)

Permite seleccionar varias opciones.

```java
JCheckBox checkBox = new JCheckBox("Aceptar términos");
```

### Listas (JList)

Muestra un conjunto de elementos de los cuales se puede seleccionar uno o más.

```java
String[] items = {"Elemento 1", "Elemento 2"};
JList<String> lista = new JList<>(items);
```

### JComboBox

Lista desplegable que permite seleccionar un ítem.

```java
JComboBox<String> comboBox = new JComboBox<>(items);
```

## 2. Ventanas y diálogos

### JFrame

Ventana principal con barra de título.

```java
JFrame ventana = new JFrame("Ventana Principal");
ventana.setSize(400, 300);
ventana.setVisible(true);
```

### JDialog (modal)

Ventana de diálogo que bloquea la ventana principal hasta ser cerrada.

```java
JDialog dialogo = new JDialog(ventana, "Diálogo Modal", true);
dialogo.setSize(300, 200);
dialogo.setVisible(true);
```

### JDialog (no modal)

Ventana de diálogo que no bloquea la ventana principal.

```java
JDialog dialogoNoModal = new JDialog(ventana, "Diálogo No Modal");
dialogoNoModal.setSize(300, 200);
dialogoNoModal.setVisible(true);
```

## 3. Contenedores

### JPanel

Panel que agrupa otros componentes.

```java
JPanel panel = new JPanel();
panel.add(boton);
ventana.add(panel);
```

### JMenuBar y JMenu

Barra de menús y menú dentro de ella.

```java
JMenuBar menuBar = new JMenuBar();
JMenu menu = new JMenu("Archivo");
menuBar.add(menu);
```

### JToolBar

Barra de herramientas con iconos.

```java
JToolBar barraHerramientas = new JToolBar();
barraHerramientas.add(boton);
```

## 4. Layouts (Diseño de componentes)

Los `Layouts` en Swing definen cómo se distribuyen los componentes dentro de un contenedor.

### BorderLayout

Coloca los componentes en los bordes de la ventana (norte, sur, este, oeste, centro).

```java
ventana.setLayout(new BorderLayout());
ventana.add(boton, BorderLayout.SOUTH);
```

### GridLayout

Organiza los componentes en una rejilla de filas y columnas.

```java
ventana.setLayout(new GridLayout(2, 2));
ventana.add(boton);
```

### FlowLayout

Coloca los componentes de izquierda a derecha.

```java
ventana.setLayout(new FlowLayout());
ventana.add(boton);
```

### MigLayout

MigLayout es un gestor de diseño flexible y potente para Swing. Es más versátil que los gestores predeterminados ya que permite alineaciones precisas, control sobre tamaños y distribución dinámica.

Características principales

- Adapta automáticamente el tamaño de los componentes.
- Soporta alineaciones avanzadas y anidación de componentes.
- Permite definir márgenes, relleno y espaciado fácilmente.
- Usa una sintaxis basada en cadenas para definir la disposición.

``` java
ventana.setLayout(new MigLayout("wrap 2", "[grow, fill]10[grow, fill]", "[][]"));

JButton btn1 = new JButton("Botón 1");
JButton btn2 = new JButton("Botón 2");
JButton btn3 = new JButton("Botón 3");

ventana.add(btn1, "span 2");  
ventana.add(btn2);
ventana.add(btn3);
```

`wrap 2` → Define que hay 2 columnas y cada fila se ajustará automáticamente.

`[grow, fill]10[grow, fill]` → Ambas columnas crecen con el contenido y tienen un margen de 10px.

`span 2` → Hace que el primer botón ocupe ambas columnas.

## 5. Propiedades

### background

Establece el color de fondo.

```java
boton.setBackground(Color.RED);
```

### font

Establece la fuente del texto.

```java
etiqueta.setFont(new Font("Arial", Font.BOLD, 16));
```

### text

Modifica el texto que se muestra.

```java
etiqueta.setText("Nuevo Texto");
```

### toolTipText

Muestra un texto emergente al pasar el ratón sobre el componente.

```java
boton.setToolTipText("Haz clic para continuar");
```

## 6. Métodos comunes de componentes

### JFrame

Métodos para manipular la ventana.

```java
ventana.setSize(400, 300);
ventana.setTitle("Ventana Ejemplo");
ventana.setVisible(true);
```

### JButton

Métodos para manipular botones.

```java
boton.setEnabled(true);  // Activa el botón
```

### JTextArea

Métodos para manipular el texto.

```java
areaTexto.setText("Nuevo texto");
```

## 7. Eventos y Escuchadores (Listeners)

### ActionListener

Para responder a acciones como clics de botones.

```java
boton.addActionListener(new ActionListener() {
  public void actionPerformed(ActionEvent e) {
    System.out.println("Botón pulsado");
  }
});
```

### MouseListener

Para eventos del ratón (mouseClicked, mouseEntered, mouseExited).

```java
panel.addMouseListener(new MouseAdapter() {
  public void mouseClicked(MouseEvent e) {
    System.out.println("Ratón clickeado");
  }
});
```

### FocusListener

Para detectar cuándo un componente recibe o pierde el foco.

```java
campoTexto.addFocusListener(new FocusAdapter() {
  public void focusGained(FocusEvent e) {
    System.out.println("Campo de texto en foco");
  }
});
```

## 8. Elementos de un Componente: Propiedades y Atributos

### Getter y Setter

Los getters leen el valor de una propiedad y los setters establecen su valor.

```java
public String getColor() { return this.color; }
public void setColor(String color) { this.color = color; }
```

Si la propiedad es booleana, el getter se escribe con el prefijo `is`:

```java
public boolean isActivo() { return activo; }
```

## 9. Creación de Componentes

Para crear un componente, debes implementar la interfaz `Serializable` y tener un constructor sin argumentos.

```java
public class TemporizadorBean extends JLabel implements Serializable {
    private PropertyChangeSupport propertySupport;

    public TemporizadorBean() {
        propertySupport = new PropertyChangeSupport(this);
    }
}
```
