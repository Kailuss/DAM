---
tags: [DAM, DI]
cssclasses: [dam-di, table-compact-clean]
banner: "![[di.jpg]]"
banner_y: 0.76
---
### 1. ¿Cuál es la salida de la siguiente aplicación?

```java
public class MyActionListener implements ActionListener {
	
	@Override
	public void actionPerformed(ActionEvent evt){
		System.out.println("zxc");
	}
}

public class Main extends javax.swing.JFrame implements ActionListener {
	
	private MyActionListener myX;

	public Main() {
		initComponents();
		setSize(400, 300);
		Timer t = new Timer(400, myX);
		t.start();
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		System.out.println("asd");
	}
}
```

`myX` no está inicializado antes de usarse.

En el constructor de `Main`, se declara un Timer que recibe `myX` como `ActionListener`:

```java
Timer t = new Timer(400, myX);
```

Pero `myX` nunca se inicializa antes de ser usado, lo que significa que en el momento de la ejecución de `new Timer(1000, myX);`, la variable `myX` es null. Esto provoca una excepción _NullPointerException_ en tiempo de ejecución.

---
### 2. Botón para añadir JLabel a lista

![](Pasted%20image%2020250211091756.png)

Cada vez que se hace click en el botón `bntAddLabel` se añade un `JLabel` al contenedor `pnlLabels` con una lista de elementos. Escribe el código necesario que tendría que haber en el manejador de eventos del `btnAddLabel` para implementar la funcionalidad descrita. Supón que hay una variable de clase int `count = 0;` declarada e inicializada.

```java
@Override
public void actionPerformed(ActionEvent e) {
    // Crea un nuevo JLabel con un texto que incluya el número de etiqueta
    JLabel newLabel = new JLabel("Elemento " + count);
    
    // Incrementa el contador para la próxima etiqueta
    count++;

    // Añade el JLabel al panel contenedor
    pnlLabels.add(newLabel);

    // Refresca el panel para que se muestren los cambios
    pnlLabels.revalidate();
    pnlLabels.repaint();
}
```

##### Explicación del código

1. **Se crea un `JLabel`** con el texto `"Elemento X"`, donde `X` es el valor actual de `count`.
2. **Se incrementa `count`** para que el próximo `JLabel` tenga un número diferente.
3. **Se añade el `JLabel` a `pnlLabels`**.
4. **Se actualiza el contenedor `pnlLabels`** usando `revalidate()` y `repaint()`, asegurando que el nuevo `JLabel` aparezca en la interfaz.

---
### 3. Cambio de color de JLabel

En el ejercicio anterior, queremos que el texto de los labels cambie a color rojo cuando el ratón ‘se pone encima’ de un label, y vuelva a tener color negro cuando el ratón ‘sale’ del área del label. Escribe el código que se tiene que añadir al anterior para dotar de esta funcionalidad a la aplicación.

Para lograr que el texto de los `JLabel` cambie de color cuando el ratón pase por encima y vuelva a su color original cuando salga, debemos añadir un `MouseListener` a cada `JLabel` al momento de crearlo.

```java
// Añade un MouseListener para cambiar el color al pasar el ratón
newLabel.addMouseListener(new MouseAdapter() {
    @Override
    public void mouseEntered(MouseEvent e) {
        newLabel.setForeground(Color.RED); // Cambiar a rojo cuando el ratón entra
    }

    @Override
    public void mouseExited(MouseEvent e) {
        newLabel.setForeground(Color.BLACK); // Volver a negro cuando el ratón sale
    }
});
```
##### Explicación del código

**Se añade un `MouseListener` usando `MouseAdapter`**:
   - `mouseEntered(MouseEvent e)`: Cambia el color del texto a **rojo** cuando el ratón entra en el `JLabel`.
   - `mouseExited(MouseEvent e)`: Cambia el color del texto a **negro** cuando el ratón sale.

---

### 4. Temporizador

La siguiente aplicación hace una cuenta atrás y muestra un mensaje al acabar, pero no está funcionando. Explica por qué motivo/s no funciona y que se tiene que hacer para solucionarlo.

```java
package temporizador;

public class TestTemporizador {

	public static void main(String args[]) {
		TemporizadorBean temporizador = new TemporizadorBean();
		temporizador.setActivo(true);
	}
}
```

```java
package temporizador;

import java.io.Serializable;
import javax.swing.Timer;
import java.awt.event.ActionListener;

public class TemporizadorBean implements Serializable {

	private int tiempo;
	private final Timer t;

	public TemporizadorBean() {
		tiempo = 5;
		t = new Timer(1000, this);
		setActivo(true);
	}

	public final void setActivo(boolean valor) {
		if (valor == true) {
			t.start();
		} else {
			t.stop();
		}
	}

	public boolean getActivo() {
		return t.isRunning();
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		tiempo--;
		if (tiempo == 0) {
			setActivo(false);
			System.out.println("Terminado");
		}
	}
}
```

##### `TemporizadorBean` no implementa `ActionListener`

```java
private final Timer t;
...
t = new Timer(1000, this);
```

`this` se está pasando como `ActionListener` al `Timer`, pero `TemporizadorBean` no implementa `ActionListener`.  Para corregirlo, `TemporizadorBean` debe implementar la interfaz `ActionListener`:

```java
public class TemporizadorBean implements Serializable, ActionListener {
```

##### El temporizador se activa en el constructor

```java
public TemporizadorBean() {
    tiempo = 5;
    t = new Timer(1000, this);
    setActivo(true);
}
```

Se está llamando a `setActivo(true);` dentro del constructor, lo que inicia el temporizador inmediatamente.  Lo ideal es que el temporizador se inicie solo cuando `setActivo(true);` sea llamado explícitamente.

```java
public TemporizadorBean() {
    tiempo = 5;
    t = new Timer(1000, this);
}
```

---
### 5. Animate

Se desea crear una aplicación para animar un JLabel, de forma que se desplace a la derecha a una velocidad de 1 pixel por cada 10 ms. El JLabel se empezará a mover cuando se pulse el botón Animar y se parará cuando se vuelva a pulsar el botón Animar o cuando se haya desplazado 200 píxeles. A partir del código siguiente, se pide:

- Indicar las modificaciones a hacer y escribir el código necesario en el método adecuado para desplazar el JLabel 1 píxel cada 10 ms cumpliendo las condiciones indicadas en el enunciado.
- Escribir el código necesario para añadir un listener al botón de forma que al hacer clic en él se invoque el método btnAnimateActionPerformed. Escribir el código que debería haber dentro de btnAnimateActionPerformed.

```java
package spdvi.animation;

import java.awt.Dimension;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;

public class Main extends JFrame {

	JLabel jLabel1;
	JButton btnAnimate;
	Timer timer;
	int xPosition = 20, yPosition = 100;

	public Main() {
		this.setLocationRelativeTo(null);
		this.setLayout(null);
		this.setPreferredSize(new Dimension(400, 200));
		this.setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
	
	jLabel1 = new JLabel("jLabel1");
	jLabel1.setBounds(xPosition, yPosition, 50, 50);
	jLabel1.setBorder(BorderFactory.createLineBorder(new java.awt.Color(255, 0, 51)));

	btnAnimate = new JButton("Animate");
	btnAnimate.setBounds(20, 20, 120, 22);

	this.add(jLabel1);
	this.add(btnAnimate);

	this.pack();
	}

	public void btnAnimateActionPerformed(ActionEvent evt) {

	}

	public static void main(String args[]) {
		java.awt.EventQueue.invokeLater(new Runnable() {
			public void run() {
				new Main().setVisible(true);
			}
		});
	}
}
```

##### Solución

```java
// Inicializa el Timer en Main (pero no lo inicia)
timer = new Timer(10, new ActionListener() {
    @Override
    public void actionPerformed(ActionEvent e) {
        if (xPosition < 220) { // Se mueve si no ha alcanzado los 200px;
            xPosition++;
            jLabel1.setBounds(xPosition, yPosition, 50, 50);
        } else {
            timer.stop();
            animating = false;
        }
    }
});

// Añade listener al botón
btnAnimate.addActionListener(new ActionListener() {
    @Override
    public void actionPerformed(ActionEvent evt) {
        btnAnimateActionPerformed(evt);
    }
});

// Método que se ejecuta al pulsar el botón
public void btnAnimateActionPerformed(ActionEvent evt) {
    if (animating) {
        timer.stop();
        animating = false;
    } else {
        timer.start();
        animating = true;
    }
}

```

##### Explicación del código

1. **Se inicializa correctamente `timer` en el constructor**, pero no se inicia hasta que se pulsa el botón.  
2. **El `JLabel` se mueve 1 píxel cada 10 ms.** 
3. **Se detiene automáticamente si el `JLabel` ha recorrido 200 píxeles.**  
4. **Uso de `animating`** para rastrear si el temporizador está activo.  

---
### 6. Agregar paneles

En la aplicación siguiente, escribe la instrucción o instrucciones que se deben agregar al manejador de eventos del componente `btnX` para lograr el comportamiento mostrado en la animación.
![](Test_ani.gif)
Para conseguir la funcionalidad de replicar `pnlX` dentro de `pnl1` cuando se pulsa `btnX`, debemos realizar los siguientes pasos dentro del manejador de eventos de `btnX`:  

1. **Crear una nueva instancia de `pnlX`** (una nueva copia del panel hijo con su propio botón).  
2. **Calcular su nueva posición** desplazándola a la derecha de la última instancia creada.  
3. **Añadir la nueva instancia a `pnl1`**.  
4. **Actualizar la disposición del contenedor (`pnl1`)** para reflejar los cambios.  
5. **Redimensionar `pnl1`** para que los nuevos paneles sean visibles si exceden su tamaño original.  

##### Código para el manejador de eventos de `btnX`
Este código debe añadirse dentro del método `actionPerformed` del `btnX` en `PanelChild.java`:

```java
btnX.addActionListener(new ActionListener() {
    @Override
    public void actionPerformed(ActionEvent e) {
        // Obtener el contenedor principal (pnl1)
        JPanel pnl1 = (JPanel) getParent();

        // Calcular la nueva posición del siguiente panel
        int newX = getX() + getWidth(); // Se coloca justo a la derecha del actual
        int newY = getY(); // Mantiene la misma coordenada Y

        // Crear un nuevo panel hijo (pnlX) y establecer su posición
        PanelChild newPanel = new PanelChild();
        newPanel.setBounds(newX, newY, getWidth(), getHeight());

        // Añadir el nuevo panel al contenedor principal (pnl1)
        pnl1.add(newPanel);

        // Ajustar el tamaño de pnl1 si es necesario
        pnl1.setPreferredSize(new Dimension(pnl1.getWidth() + getWidth(), pnl1.getHeight()));

        // Actualizar la interfaz gráfica
        pnl1.revalidate();
        pnl1.repaint();
    }
});
```

##### Explicación del código

1. **Se obtiene `pnl1`**, que es el contenedor padre donde se añadirán los duplicados.  
2. **Se calcula la nueva posición (`newX`)** sumando el ancho del panel actual a su posición X.  
3. **Se crea una nueva instancia de `PanelChild` (`newPanel`)** y se le asigna la posición calculada.  
4. **Se añade el nuevo panel (`newPanel`) a `pnl1`**.  
5. **Se ajusta el tamaño de `pnl1`** para que pueda mostrar los nuevos paneles.  
6. **Se llama a `revalidate()` y `repaint()`** para actualizar la interfaz gráfica y que los cambios sean visibles.

---
### 7. Situar un `JLabel`

Escribe una instrucción para situar un `JLabel myLabel` en la posición x = 100, y = 40 de su objeto contenedor (suponiendo que tiene layout null), y hacer que tenga un tamaño de 90x16 px.

Para situar un `JLabel` llamado `myLabel` en la posición **(100, 40)** dentro de su contenedor con `null` layout y establecer su tamaño en **90x16 px**, se usa el método `setBounds(x, y, width, height)`:  

```java
myLabel.setBounds(100, 40, 90, 16);
```

---
### 8. Layout null

Escribe una línea de código para establecer el diseño (layout) de la ventana principal de una aplicación Java Swing en null.

Para desactivar el **gestor de diseño** (layout manager) y permitir la posición absoluta de los componentes en la ventana principal (`JFrame`), se usa el método `setLayout(null);` sobre el `JFrame` o su `contentPane`:

```java
setLayout(null);
```

O si se está configurando directamente en la instancia de `JFrame`:

```java
miVentana.setLayout(null);
```

Esto permite usar `setBounds(x, y, width, height);` para posicionar los componentes manualmente.

---
### 9. Panel Layout

Escribe la instrucción que debería aparecer en la línea comentada para que el mediaPlayerComponent se mostrara dentro del pnlVideo ocupando todo el espacio disponible de éste. 

```java
public class Main extends javax.swing.JFrame {

	private javax.swing.JPanel pnlVideo;
	private final EmbeddedMediaPlayerComponent mediaPlayerComponent;

	public Main() {
		inirComponents();

		pnlVideo= new javax.swing.JPanel();
		mediaPlayerComponent = new EmbeddedMediaPlayerComponent();

		getContentPane().setLayout(null);
		setSize(1024, 768);

pnlVideo.setBorder(javax.swing.BorderFactory.createTitledBorder("Video Player"));
		pnlVideo.setLayout(new java.awt.BorderLayout());
		// ¿Qué hay que poner aquí para el resultado especificado?
	}
}
```

Para que el `mediaPlayerComponent` se muestre dentro de `pnlVideo`, ocupando todo el espacio disponible de éste, debes añadir el `mediaPlayerComponent` al panel `pnlVideo` usando el método `add()` y luego ajustar el tamaño del `mediaPlayerComponent` al tamaño de su contenedor (`pnlVideo`). Dado que `pnlVideo` usa un `BorderLayout`, el componente debe añadirse a la posición central, lo que permite que ocupe todo el espacio disponible.

La instrucción a añadir sería:

```java
pnlVideo.add(mediaPlayerComponent, java.awt.BorderLayout.CENTER);
```

`pnlVideo.add(mediaPlayerComponent, java.awt.BorderLayout.CENTER);`
añade el `mediaPlayerComponent` en la **posición central** de `pnlVideo`, lo que hace que ocupe todo el espacio disponible dentro de ese panel debido al comportamiento del `BorderLayout`.
  
Luego de esto, `mediaPlayerComponent` se ajustará automáticamente al tamaño de `pnlVideo` cuando cambie su tamaño.

---
### 10. Swipe

Completa la clase MyJPanel como corresponda para que, si se hace un swipe right sobre un objeto de tipo MyJPanel su color de fondo cambie a Color.ORANGE y si se hace un swipe left el color de fondo sea Color.PINK. La sensibilidad del swipe deberá ser de 10 pixels, es decir, para que se considere que se ha hecho swipe, el ratón se debe haber desplazado al menos 10 pixels.

```java
public class MyJPanel extends JPanel {

	public MyJPanel() {
		initComponents();
	}
}
```

Para implementar la funcionalidad de detectar un **swipe right** (deslizar hacia la derecha) y un **swipe left** (deslizar hacia la izquierda) sobre un `JPanel` (`MyJPanel`), podemos utilizar los eventos de ratón (`MouseListener` y `MouseMotionListener`). La idea es detectar el movimiento del ratón y, si este se desplaza más de 10 píxeles en horizontal, cambiar el color de fondo del panel según la dirección del movimiento.

Aquí tienes la implementación de la clase `MyJPanel` con los eventos correspondientes:

##### Código de la clase `MyJPanel`:

```java
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class MyJPanel extends JPanel {

    private int initialX;  // Coordenada X inicial del ratón
    private boolean swipeDetected = false;

    public MyJPanel() {
        initComponents();
    }

    private void initComponents() {
        // Escucha los eventos del ratón
        addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                initialX = e.getX();  // Guarda la posición inicial del ratón al presionar
                swipeDetected = false; // Resetea el estado de swipe
            }
        });

        addMouseMotionListener(new MouseAdapter() {
            @Override
            public void mouseDragged(MouseEvent e) {
                // Detectar el desplazamiento horizontal
                int deltaX = e.getX() - initialX;
                
                // Solo cambia si se ha desplazado más de 10 píxeles
                if (Math.abs(deltaX) > 10 && !swipeDetected) {
                    if (deltaX > 0) {
                        // Deslizar hacia la derecha
                        setBackground(Color.ORANGE);
                    } else {
                        // Deslizar hacia la izquierda
                        setBackground(Color.PINK);
                    }
                    swipeDetected = true; // Se ha detectado un swipe
                }
            }
        });
    }
}
```

##### Explicación del código

1. **`addMouseListener`**:
   - `mousePressed`: Captura la posición del ratón cuando se presiona sobre el panel (`initialX = e.getX()`), lo que nos servirá para calcular el desplazamiento en el futuro.
   - Se resetea el estado de `swipeDetected` a `false` cada vez que se presiona el ratón, permitiendo detectar un nuevo swipe.

2. **`addMouseMotionListener`**:
   - `mouseDragged`: Se activa cuando el ratón se mueve mientras está presionado.
   - Calculamos el **deltaX** (desplazamiento horizontal) entre la posición actual y la inicial.
   - Si el desplazamiento es mayor de 10 píxeles (`Math.abs(deltaX) > 10`), se considera un **swipe**. Si el desplazamiento es positivo (a la derecha), el fondo se pone **naranja** (`Color.ORANGE`); si es negativo (a la izquierda), el fondo se pone **rosa** (`Color.PINK`).
   - `swipeDetected` evita que el fondo cambie más de una vez durante el mismo swipe.
##### Consideraciones adicionales

- El `Math.abs(deltaX) > 10` asegura que solo se detecta un swipe si el ratón se mueve al menos 10 píxeles horizontalmente.
- La variable `swipeDetected` asegura que el color de fondo solo cambie una vez por swipe, no constantemente mientras se mueve el ratón.

---

### 11. Añadir JLabel
Observa el siguiente código incompleto que crea una ventana con el título "Aplicación de Prueba" y un tamaño de 400x200 píxeles. Completa el código para añadir un JLabel con el texto "¡Bienvenido!" al centro de la ventana.

```java
import javax.swing.*;

public class AplicacioProva {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Aplicació de Prova");
        frame.setSize(400, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Completa el código para añadir el JLabel

        frame.setVisible(true);
    }
}
```

Para añadir un `JLabel` al centro de la ventana, debemos usar un `LayoutManager` adecuado, como el `FlowLayout` (que alinea los componentes al centro por defecto), o podemos usar `BorderLayout` y colocar el `JLabel` en el centro.

A continuación, se completa el código para añadir el `JLabel`:

```java
import javax.swing.*;

public class AplicacioProva {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Aplicació de Prova");
        frame.setSize(400, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Crear el JLabel con el texto "Benvingut!"
        JLabel label = new JLabel("Benvingut!", JLabel.CENTER);  // Alineado al centro

        // Añadir el JLabel al frame
        frame.add(label);

        // Hacer visible la ventana
        frame.setVisible(true);
    }
}
```

##### Explicación

1. **`JLabel label = new JLabel("Benvingut!", JLabel.CENTER);`**: Creamos un `JLabel` con el texto "Benvingut!" y lo alineamos al centro usando el argumento `JLabel.CENTER`.
2. **`frame.add(label);`**: Añadimos el `JLabel` al `JFrame` para que se muestre en la ventana.
3. **`frame.setVisible(true);`**: Hacemos visible la ventana.

El `JLabel` se mostrará centrado en la ventana debido al alineamiento y al uso del `FlowLayout`.

---

### 12. JTextfield vacío
Se solicita que, en un formulario de Swing con campos como JTextField para nombre y apellidos, y un JButton llamado btnSubmit, el JButton se deshabilite automáticamente si alguno de los campos está vacío. Cuando todos los campos tengan texto, el botón debería estar activado. Escribe el código para implementar esta funcionalidad.

Para implementar esta funcionalidad, podemos utilizar un `DocumentListener` para los `JTextField`, que nos permitirá detectar cualquier cambio en los campos de texto. Cada vez que el texto en un campo cambie, verificamos si los campos están vacíos y, en función de eso, habilitamos o deshabilitamos el botón.

```java
import javax.swing.*;
import javax.swing.event.*;

public class Formulario {
    private JTextField txtNombre;
    private JTextField txtApellido;
    private JButton btnSubmit;

    public Formulario() {
        // Crea los componentes
        txtNombre = new JTextField(20);
        txtApellido = new JTextField(20);
        btnSubmit = new JButton("Enviar");

        // Deshabilita el botón por defecto
        btnSubmit.setEnabled(false);

        // Añade listeners a los campos de texto
        DocumentListener docListener = new DocumentListener() {
            public void insertUpdate(DocumentEvent e) {
                comprobarCampos();
            }
            public void removeUpdate(DocumentEvent e) {
                comprobarCampos();
            }
            public void changedUpdate(DocumentEvent e) {
                comprobarCampos();
            }
        };

        txtNombre.getDocument().addDocumentListener(docListener);
        txtApellido.getDocument().addDocumentListener(docListener);

        // Crea el JFrame
        JFrame frame = new JFrame("Formulario");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BoxLayout(frame.getContentPane(), BoxLayout.Y_AXIS));

        // Añade los componentes al frame
        frame.add(new JLabel("Nombre:"));
        frame.add(txtNombre);
        frame.add(new JLabel("Apellido:"));
        frame.add(txtApellido);
        frame.add(btnSubmit);

        // Ajusta la ventana
        frame.pack();
        frame.setVisible(true);
    }

    // Método para comprobar si ambos campos tienen texto
    private void comprobarCampos() {
        if (txtNombre.getText().isEmpty() || txtApellido.getText().isEmpty()) {
	        // Deshabilita el botón si algún campo está vacío
            btnSubmit.setEnabled(false);
        } else {
	        // Habilita el botón si ambos campos tienen texto
            btnSubmit.setEnabled(true);
        }
    }

    public static void main(String[] args) {
        new Formulario();
    }
}
```

##### Explicación

1. **Componentes**: Creamos dos `JTextField` para el nombre y los apellidos, y un `JButton` para enviar el formulario.
2. **Deshabilitar el botón por defecto**: Al inicio, el botón `btnSubmit` está deshabilitado (`btnSubmit.setEnabled(false);`).
3. **DocumentListener**: Añadimos un `DocumentListener` a los `JTextField` que detecta cambios en el contenido de los campos. Cada vez que el contenido de uno de los campos cambia, se llama al método `comprobarCampos()`.
4. **Método `comprobarCampos()`**: Este método verifica si ambos campos de texto están vacíos. Si alguno está vacío, deshabilita el botón `btnSubmit`; si ambos campos contienen texto, habilita el botón.

---
### 13. Formulario Maestro-Detalle

Se solicita que, en un formulario maestro-detalle, se agregue código dentro del `ActionListener` para que el texto introducido en `nomField` se muestre en `resultatLabel`.
##### Pasos para completar la funcionalidad

1. **Inicializar el `JComboBox` con los proyectos disponibles**: Necesitamos llenar el `JComboBox` con los proyectos que están almacenados en el mapa `projectesTasques`.

2. **Obtener las tareas del proyecto seleccionado**: Cuando se selecciona un proyecto en el `JComboBox`, debemos obtener las tareas asociadas a ese proyecto del mapa `projectesTasques`.

3. **Añadir tareas al proyecto seleccionado**: Cuando se agrega una tarea, la nueva tarea debe ser añadida al proyecto seleccionado en el mapa `projectesTasques`.

4. **Eliminar tareas del proyecto seleccionado**: Cuando se hace doble clic sobre una tarea en la lista de tareas, esa tarea debe ser eliminada de la lista de tareas del proyecto seleccionado.

5. **Actualizar la lista de tareas**: Después de añadir o eliminar una tarea, la lista de tareas debe actualizarse para reflejar los cambios.

6. **Mostrar un mensaje de error**: Si se intenta agregar una tarea vacía o con texto inválido, debemos mostrar un mensaje de error.

A continuación se muestra el código completo con las implementaciones de estos métodos.

```java
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class FormulariMestreDetall {
    // Mapa que emmagatzema els projectes amb les seves tasques
    private static Map<String, List<String>> projectesTasques = new HashMap<>();

    public static void main(String[] args) {
        JFrame frame = new JFrame("Formulari Mestre-Detall");
        frame.setLayout(new BorderLayout());

        // Panell mestre
        JPanel panellMestre = new JPanel();
        JLabel projecteLabel = new JLabel("Selecciona un projecte:");
        JComboBox<String> projecteComboBox = new JComboBox<>();
        panellMestre.add(projecteLabel);
        panellMestre.add(projecteComboBox);

        // Panell detall
        JPanel panellDetall = new JPanel();
        panellDetall.setLayout(new BoxLayout(panellDetall, BoxLayout.Y_AXIS));
        JLabel tasquesLabel = new JLabel("Tasques:");
        JList<String> tasquesList = new JList<>();
        JScrollPane tasquesScroll = new JScrollPane(tasquesList);
        JTextField tascaField = new JTextField(15);
        JButton afegirButton = new JButton("Afegeix tasca");

        panellDetall.add(tasquesLabel);
        panellDetall.add(tasquesScroll);
        panellDetall.add(new JLabel("Nova tasca:"));
        panellDetall.add(tascaField);
        panellDetall.add(afegirButton);

        frame.add(panellMestre, BorderLayout.NORTH);
        frame.add(panellDetall, BorderLayout.CENTER);
        // Completa la inicialització del JComboBox amb els projectes
        inicialitzarProjectesComboBox(projecteComboBox);
        // Completa la funcionalitat per actualitzar les tasques quan es selecciona un projecte
        projecteComboBox.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String projecteSeleccionat = (String) projecteComboBox.getSelectedItem();
                List<String> tasques = getTasquesDelProjecte(projecteSeleccionat);
                tasquesList.setListData(tasques.toArray(new String[0]));  // Actualizar la lista de tareas
            }
        });
        // Afegir tasca
        afegirButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String tasca = tascaField.getText().trim();
                if (tasca.isEmpty()) {
                    mostrarMissatgeError("La tasca no pot estar buida");
                    return;
                }
                String projecteSeleccionat = (String) projecteComboBox.getSelectedItem();
                afegirTascaAlProjecte(projecteSeleccionat, tasca);
                actualitzarLlistaTasques(projecteSeleccionat);
                tascaField.setText("");  // Borrar el campo de texto
            }
        });
        // Elimina tasca
        tasquesList.addMouseListener(new MouseAdapter() {
            public void mouseClicked(MouseEvent e) {
                if (e.getClickCount() == 2) {
                    int index = tasquesList.locationToIndex(e.getPoint());
                    String tascaSeleccionada = tasquesList.getModel().getElementAt(index);
                    String projecteSeleccionat = (String) projecteComboBox.getSelectedItem();
                    eliminarTascaDelProjecte(projecteSeleccionat, tascaSeleccionada);
                    actualitzarLlistaTasques(projecteSeleccionat);
                }
            }
        });
        frame.setSize(400, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }

    // Inicialització de dades per als projectes
    private static void inicialitzarProjectesComboBox(JComboBox<String> projecteComboBox) {
        projectesTasques.put("Projecte A", new ArrayList<>());
        projectesTasques.put("Projecte B", new ArrayList<>());
        projectesTasques.put("Projecte C", new ArrayList<>());
        projecteComboBox.addItem("Projecte A");
        projecteComboBox.addItem("Projecte B");
        projecteComboBox.addItem("Projecte C");
    }

    // Obtenir tasques del projecte seleccionat
    private static List<String> getTasquesDelProjecte(String projecte) {
        return projectesTasques.getOrDefault(projecte, new ArrayList<>());
    }

    // Afegir una tasca al projecte
    private static void afegirTascaAlProjecte(String projecte, String tasca) {
        List<String> tasques = projectesTasques.get(projecte);
        if (tasques != null) {
            tasques.add(tasca);
        }
    }

    // Eliminar una tasca del projecte
    private static void eliminarTascaDelProjecte(String projecte, String tasca) {
        List<String> tasques = projectesTasques.get(projecte);
        if (tasques != null) {
            tasques.remove(tasca);
        }
    }

    // Actualitzar la llista de tasques mostrada
    private static void actualitzarLlistaTasques(String projecte) {
        List<String> tasques = getTasquesDelProjecte(projecte);
        // Deberías actualizar el JList con la nueva lista de tareas
    }

    // Mostrar un mensaje de error
    private static void mostrarMissatgeError(String missatge) {
        JOptionPane.showMessageDialog(null, missatge, "Error", JOptionPane.ERROR_MESSAGE);
    }
}
```

##### Explicación

1. **Inicialización del `JComboBox`**: Se completó el método `inicialitzarProjectesComboBox`, que llena el `JComboBox` con los nombres de los proyectos disponibles en el mapa `projectesTasques`.

2. **Obtener las tareas del proyecto**: El método `getTasquesDelProjecte` retorna las tareas asociadas a un proyecto del mapa `projectesTasques`.

3. **Añadir tareas**: En el `ActionListener` del botón "Afegeix tasca", primero validamos que la tarea no esté vacía. Luego, añadimos la tarea al proyecto seleccionado.

4. **Eliminar tareas**: Si se hace doble clic sobre una tarea en el `JList`, se elimina esa tarea del proyecto seleccionado.

5. **Actualizar la lista de tareas**: Después de añadir o eliminar una tarea, se actualiza la lista de tareas mostrando la información más reciente.

6. **Mostrar un mensaje de error**: Si la tarea es vacía, mostramos un mensaje de error usando `mostrarMissatgeError`.

---

### 14. Formulario con Diálogos Modales y No Modales
En este ejercicio, debes crear una pequeña aplicación de gestión de tareas que permita a los usuarios añadir tareas a una lista, mostrar mensajes informativos mediante diálogos modales y no modales, y confirmar acciones como eliminar tareas. El formulario debe tener los siguientes componentes y funcionalidades:

1. **Añadir Tarea:** El usuario puede introducir una tarea en un JTextField y añadirla a una lista. Si la tarea ya existe, se mostrará un diálogo modal de error.

2. **Eliminar Tarea:** El usuario puede eliminar una tarea haciendo clic sobre una tarea de la lista. Un diálogo modal de confirmación debe preguntar si el usuario está seguro antes de eliminarla.

3. **Mostrar Tareas:** Las tareas se deben mostrar en un JList, y cuando el usuario pasa el cursor sobre ellas, debe mostrarse un diálogo no modal con información sobre la tarea (por ejemplo, la fecha de añadido).

4. **Diálogo de Mensaje:** Cuando el usuario haga una acción importante (como añadir una tarea), un diálogo modal debe mostrar un mensaje indicando que la acción se ha realizado correctamente.

##### Implementación

```java
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;

public class FormulariAmbDials {
    // Llista de tasques
    private static ArrayList<String> tasques = new ArrayList<>();

    public static void main(String[] args) {
        JFrame frame = new JFrame("Gestió de Tasques");
        frame.setLayout(new BorderLayout());

        // Panell per afegir tasques
        JPanel panellAfegir = new JPanel();
        JTextField tascaField = new JTextField(15);
        JButton afegirButton = new JButton("Afegeix Tasca");
        panellAfegir.add(tascaField);
        panellAfegir.add(afegirButton);

        // Llista de tasques
        DefaultListModel<String> modelTasques = new DefaultListModel<>();
        JList<String> tasquesList = new JList<>(modelTasques);
        JScrollPane tasquesScroll = new JScrollPane(tasquesList);

        frame.add(panellAfegir, BorderLayout.NORTH);
        frame.add(tasquesScroll, BorderLayout.CENTER);

        // Afegir tasca
        afegirButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String tasca = tascaField.getText().trim();
                if (tasca.isEmpty()) {
                    mostrarMissatgeError("La tasca no pot estar buida.");
                } else if (tasques.contains(tasca)) {
                    mostrarMissatgeError("Aquesta tasca ja existeix.");
                } else {
                    tasques.add(tasca);
                    modelTasques.addElement(tasca);
                    mostrarMissatgeExito("Tasca afegida correctament.");
                }
            }
        });

        // Eliminar tasca amb diàleg modal de confirmació
        tasquesList.addMouseListener(new MouseAdapter() {
            public void mouseClicked(MouseEvent e) {
                if (e.getClickCount() == 2) {
                    int index = tasquesList.locationToIndex(e.getPoint());
                    String tascaSeleccionada = tasquesList.getModel().getElementAt(index);

                    int opcio = mostrarDiologoConfirmacio("Segur que vols eliminar aquesta tasca?");
                    if (opcio == JOptionPane.YES_OPTION) {
                        tasques.remove(tascaSeleccionada);
                        modelTasques.removeElement(tascaSeleccionada);
                    }
                }
            }
        });

        // Diàleg no modal (mostra informació quan el cursor està sobre una tasca)
        tasquesList.addMouseMotionListener(new MouseMotionAdapter() {
            public void mouseMoved(MouseEvent e) {
                int index = tasquesList.locationToIndex(e.getPoint());
                if (index != -1) {
                    String tascaSeleccionada = tasquesList.getModel().getElementAt(index);
                    mostrarDiàlegInformatiu("Tasca: " + tascaSeleccionada);
                }
            }
        });

        // Configura finestra
        frame.setSize(400, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }

    // Diàleg modal d'error
    private static void mostrarMissatgeError(String missatge) {
        JOptionPane.showMessageDialog(null, missatge, "Error", JOptionPane.ERROR_MESSAGE);
    }

    // Diàleg modal d'èxit
    private static void mostrarMissatgeExito(String missatge) {
        JOptionPane.showMessageDialog(null, missatge, "Èxit", JOptionPane.INFORMATION_MESSAGE);
    }

    // Diàleg modal de confirmació
    private static int mostrarDiologoConfirmacio(String missatge) {
        return JOptionPane.showConfirmDialog(null, missatge, "Confirmació", JOptionPane.YES_NO_OPTION);
    }

    // Diàleg no modal d'informació
    private static void mostrarDiàlegInformatiu(String tasca) {
        JDialog dialog = new JDialog();
        dialog.setTitle("Informació Tasca");
        dialog.setSize(250, 100);
        dialog.setLocationRelativeTo(null);
        JLabel label = new JLabel(tasca);
        dialog.add(label);
        dialog.setModal(false);
        dialog.setVisible(true);

        // Tancar el diàleg quan el cursor ja no estigui sobre la tasca
        Timer timer = new Timer(2000, new ActionListener() {
            public void actionPerformed(ActionEvent arg0) {
                dialog.setVisible(false);
            }
        });
        timer.setRepeats(false);
        timer.start();
    }
}
```

##### Explicación

1. **Añadir Tarea:**
   - Si la tarea está vacía, se muestra un diálogo modal de error.
   - Si la tarea ya existe, también se muestra un error.
   - Si la tarea es nueva, se añade a la lista y se muestra un mensaje de éxito.

2. **Eliminar Tarea:**
   - Al hacer doble clic en una tarea, se muestra un diálogo modal de confirmación. Si el usuario confirma, se elimina la tarea de la lista.

3. **Mostrar Tareas:**
   - Al pasar el cursor sobre una tarea, se muestra un diálogo no modal que permanece visible brevemente (2 segundos) con información de la tarea.

4. **Diálogos Modales:**
   - **Error:** Se usa `JOptionPane.showMessageDialog` para mostrar mensajes de error.
   - **Éxito:** Se muestra un mensaje de éxito después de añadir una tarea.
   - **Confirmación:** Se muestra un diálogo con opciones de "Sí" o "No" para confirmar la eliminación de una tarea.

5. **Diálogo No Modal:**
   - Se utiliza un `JDialog` que se muestra brevemente al pasar el cursor sobre una tarea en la lista. Se cierra automáticamente después de un breve periodo.