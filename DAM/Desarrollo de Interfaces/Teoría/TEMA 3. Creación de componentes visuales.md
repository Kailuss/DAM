---
number headings: max 2, _.1.1.
obsidianUIMode: preview
banner: "![[di.jpg]]"
banner_y: 0.85
cssclasses:
  - table-clean
---

# **TEMA 3.** <br>Creación de componentes visuales

| Anexos                                                          |     
| --------------------------------------------------------------- | 
| [Resumen Tema 3](Resúmenes/Resumen%20Tema%203.md)               |
| [Componentes Swing](Resúmenes/Resumen%20Componentes%20Swing.md) |
| [Tarea DI03](../Práctica/Tareas/Tarea%20DI03.md)                     |

![Lectura MP3](Lectura_Tema_3_Creación_de_componentes_visuales.mp3)

## 1. Concepto de componente y sus características

Un **componente software** es una clase reutilizable que puede manipularse mediante herramientas de desarrollo visual. Su **estado** se almacena en **propiedades** modificables para adaptarlo a distintas aplicaciones. Su **comportamiento** se define por los **eventos** a los que responde y los **métodos** que ejecuta.

Los eventos representan las acciones del usuario sobre los componentes. Un subconjunto de atributos y métodos conforma la **interfaz** del componente. Para su distribución, se empaqueta con todo lo necesario para su funcionamiento independiente.

Para que una clase sea un componente, debe cumplir:

- **Modificabilidad.** Adaptable a distintas aplicaciones.
- **Persistencia.** Capaz de conservar el estado de sus propiedades.
- **Introspección.** Permite a un IDE reconocer sus elementos de diseño y devolver información sobre ellos.
- **Gestor de eventos.** Capacidad de responder a acciones del usuario.

**Ventajas del desarrollo basado en componentes**

- Desarrollo más rápido y económico.
- Reducción de errores, gracias a controles de calidad previos.

**Aplicación en interfaces gráficas**

Los controles de una interfaz visual cumplen con las características de los componentes: son reutilizables, modificables (color, tamaño, etc.), persistentes tras el cierre de la interfaz y tienen una interfaz de métodos y propiedades accesibles. Además, responden a eventos como clics del ratón.

## 2. Elementos de un componente: propiedades y atributos

Un componente define su estado mediante **atributos**, que son variables internas con un nombre y tipo de dato específicos. Normalmente, los atributos son privados y solo se usan dentro de la clase.

![[DAM/Desarrollo de Interfaces/Teoría/Imágenes/03/Editor de propiedades.jpg]]

Las **propiedades** son atributos accesibles desde fuera de la clase y forman parte de la interfaz del componente, afectando su apariencia o comportamiento.

![[Selector de color.jpg]]

Suelen estar asociadas a un atributo interno y se pueden modificar mediante métodos específicos:

- **Getter.** Permite leer el valor de la propiedad.

	```java
    public <TipoPropiedad> get<NombrePropiedad>()
    ```

	Para propiedades booleanas:

	```java
    public boolean is<NombrePropiedad>()
    ```

- **Setter.** Permite establecer el valor de la propiedad.

	```java
    public void set<NombrePropiedad>(<TipoPropiedad> valor)
    ```

	Si una propiedad no tiene `set`, es de solo lectura.

Ejemplo para una propiedad `color` en un botón:

```java
public void setColor(String color)
public String getColor()
```

### Modificar gráficamente el valor de una propiedad con un editor

Los entornos de desarrollo identifican automáticamente propiedades a través de los métodos `get/set` mediante **introspección.** Pueden editar valores de tipos básicos y clases como `Color` o `Font`, pero para propiedades más complejas (ej. `Cliente`) se requiere un **editor de propiedades** personalizado.

Un **editor de propiedad** permite modificar visualmente valores específicos dentro de un IDE. Para crearlo en Java, se implementa la interfaz, `PropertyEditor`, siguiendo la convención:

```java
public <Propiedad>Editor implements PropertyEditor {…}
```

La clase `PropertyEditorSupport` facilita la creación de editores para tipos básicos, `Color` y `Font`. Una vez creados, se empaquetan con el componente para que el entorno los use automáticamente al editar la propiedad en la hoja de propiedades del IDE.

Cuando un componente se selecciona en un panel:

1. El IDE usa `getters` para mostrar los valores actuales.
2. Si se cambia una propiedad, se invoca el `setter`, actualizando su valor y posiblemente su apariencia.

**Ejemplo de definición de un editor para la propiedad `direccion`:**

```java
public direccionEditor implements PropertyEditor {...}
```

---

#### Ejemplo de creación de un componente con un editor de propiedades

 Un **JavaBean** es un componente software reusable que puede ser manipulado visualmente mediante una herramienta gráfica.

Los editores de propiedades tienen dos propósitos fundamentales:

- Convertir el valor de las cadenas para ser mostrados adecuadamente conforme a las características de la propiedad.
- Validar los datos nuevos cuando son introducidos por el usuario.

Los pasos básicos para crear un editor de propiedades son:

1. Crear una clase que extienda `PropertyEditorSupport`.
2. Implementar los métodos `getAsText` y `setAsText` para transformar el tipo de dato de la propiedad en cadena de caracteres o viceversa.
3. Añadir los métodos necesarios para la clase.
4. Asociar el editor de propiedades a la propiedad en cuestión.

---

##### Definición del componente

Para ilustrar la implementación de un componente en NetBeans, se creará un campo de texto con propiedades modificables como **ancho**, **color** y **fuente.**

- **Ancho.** Propiedad de tipo entero.
- **Color.** Propiedad de tipo `Color`, con su propio editor.
- **Fuente.** Propiedad de tipo `Font`, con su propio editor.

**Creación del Proyecto**

1. Crear un proyecto de tipo **Java Application**, sin clase principal ni carpeta de bibliotecas. ![[Archivo nuevo.jpg]]
2. Añadir al proyecto un archivo de tipo **Componente JavaBeans.**
	
	- Seleccionar el proyecto > Botón derecho > Nuevo > Objeto JavaBeans.  
	- Asignar el nombre **ComponenteMiTexto** dentro del paquete **miscontroles.**
	- Finalizar la creación. ![[Componente nuevo.jpg]]
3. Acceder al código de la clase generada y eliminar el código introducido automáticamente por el IDE, dejando solo la estructura básica. ![[Componente código.jpg]]
4. Modificar la clase `ComponenteMiTexto` para que herede de `JTextField`.
	
**Definición de Propiedades**

Se definen las propiedades **ancho**, **color** y **fuente**, agregando los métodos `set` y `get`:

1. Desplegar el menú contextual sobre la clase y seleccionar **Insertar código** > **Agregar Propiedad.** ![[Insertar código.jpg]]
2. Definir las propiedades con visibilidad privada y generar los métodos `set` y `get`. ![[Agregar propiedad.jpg]]
3. Implementar los métodos de acceso y modificación en el código de la clase. ![[Métodos de acceso.jpg]]

---

##### Crear un editor de propiedades

Una vez creado el componente, se asocia un editor de propiedades mediante un objeto **BeanInfo.**

1. Seleccionar la clase `ComponenteMiTexto` en el panel de proyectos.
2. Seleccionar la opción **Editor BeanInfo.** ![[Editar BeanInfo.jpg]]
3. Crear un nuevo BeanInfo. ![[BeanInfo.jpg]]
4. En el panel de ficheros del proyecto aparecerá una nueva clase llamada `ComponenteMiTextoBeanInfo.java`.

Accediendo al diseñador, se pueden ver las propiedades y métodos del nuevo JavaBean creado.

---

##### Uso del componente

Una vez creado y construido el componente, es necesario agregarlo a la paleta de componentes. Para ello, seleccionamos la clase `ComponenteMiTexto`, accedemos al menú contextual y elegimos la opción **Herramientas > Añadir a la paleta.**

Aparecerá una ventana para seleccionar la categoría donde almacenarlo. Se recomienda la categoría **Beans Personalizados** para organizar los JavaBeans creados. ![[Categoría de paleta.jpg]]

Para probar el componente, creamos un nuevo proyecto de tipo aplicación Java, añadimos un `JFrame` y desde la paleta seleccionamos y agregamos nuestro componente al diseñador. Luego, accediendo a sus propiedades, podemos modificar atributos como **ancho, fuente y color.** ![[Componente de texto.jpg]]

### Propiedades simples e indexadas

- **Propiedad simple.** Representa un único valor (número, booleano, texto, etc.). Cuenta con métodos **getter** y **setter** para acceder a su valor.

```java
public real getPeso()
public void setPeso(real nuevoPeso)
```

Si falta alguno de estos métodos, la propiedad será solo de lectura o solo de escritura.

- **Propiedad indexada.** Representa un conjunto de elementos almacenados en un vector. Se accede a ellos mediante métodos para leer o modificar elementos individuales o el vector completo. ![[Componente.jpg]]

```java
public <TipoProp>[] get<NombreProp>()
public void set<NombreProp> (<TipoProp>[] p)
public <TipoProp> get<NombreProp>(int posicion)
public void set<NombreProp> (int posicion, <TipoProp> p)
```

### Propiedades compartidas y restringidas

Una **propiedad compartida o ligada** permite notificar a otros objetos cuando su valor cambia. Para ello, se genera un `PropertyChangeEvent` que informa a los oyentes registrados sobre la modificación.

Los métodos utilizados para registrar y eliminar oyentes de cambios de propiedad son:

```java
public void addPropertyChangeListener(PropertyChangeListener l)
public void removePropertyChangeListener(PropertyChangeListener l)
```

Para notificar cambios en una propiedad específica, se utilizan métodos personalizados con el nombre de la propiedad:

```java
public void addPropertyNameListener(PropertyChangeListener l)
public void removePropertyNameListener(PropertyChangeListener l)
```

Los objetos que implementan `PropertyChangeListener` deben definir el método `propertyChange()`, que se invoca cuando cambia la propiedad.

Una **propiedad restringida** funciona de manera similar a una propiedad compartida, pero los oyentes pueden vetar los cambios de valor. Para ello, los objetos registrados deben implementar `VetoableChangeListener` y el método `vetoableChange()`, donde pueden lanzar una excepción `PropertyVetoException` si rechazan el cambio.

Los métodos de registro para propiedades restringidas incluyen:

```java
public void addPropertyVetoableListener(VetoableChangeListener l)
public void removePropertyVetoableListener(VetoableChangeListener l)
public void addPropertyNameListener(VetoableChangeListener l)
public void removePropertyNameListener(VetoableChangeListener l)
```

## 3. Eventos. Asociación de acciones a eventos

Los componentes pueden reaccionar ante acciones del usuario, como clics o pulsaciones de teclas, generando eventos que pueden ser capturados y procesados. También pueden lanzar eventos para que sean gestionados por otros objetos.

Para manejar eventos:

- Crear una clase para los eventos.
- Definir una interfaz para el oyente (listener) con un método para procesar el evento.
- Incluir métodos para añadir y eliminar oyentes, almacenándolos en una estructura de datos como `ArrayList` o `LinkedList`:

```java
public void add<Nombre>Listener(<Nombre>Listener l)
public void remove<Nombre>Listener(<Nombre>Listener l)
```

- Recorrer la lista de oyentes y llamar al método de procesamiento del evento en cada uno.

## 4. Introspección y Reflexión

La **introspección** permite a las herramientas de desarrollo detectar dinámicamente las propiedades, métodos y eventos de un componente, facilitando su uso en entornos visuales.

La **reflexión** es una técnica que permite inspeccionar una clase en tiempo de ejecución para conocer sus métodos y propiedades, generalmente identificando los métodos `get` y `set`.

Para mejorar la introspección, se puede usar una clase `BeanInfo`, que describe explícitamente las características del componente para que las herramientas de desarrollo las reconozcan. ![[Asociación de acciones a eventos.png]]

## 5. Persistencia del componente

La **persistencia** permite almacenar el estado de un objeto para recuperarlo posteriormente. Para ello, se usa la **serialización**, que convierte un objeto en un formato que puede ser almacenado y restaurado.

**Tipos de serialización en Java**

1. **Serialización automática.** Implementando `java.io.Serializable`, Java maneja automáticamente el proceso. Consideraciones:
	
	- La clase debe tener un **constructor sin argumentos.**
		
	- Se serializan todos los campos excepto los marcados como `static` o `transient`.
		
	- Se pueden personalizar los métodos `writeObject(ObjectOutputStream out)` y `readObject(ObjectInputStream in)`.
		
2. **Serialización programada.** Implementando `java.io.Externalizable`, el programador define cómo guardar y recuperar el objeto mediante los métodos `writeExternal()` y `readExternal()`. También requiere un **constructor sin argumentos.**

## 6. Otras tecnologías para la creación de componentes visuales

Existen diversas tecnologías para la creación de componentes visuales además de **JavaBeans.**

- **JavaBeans (Oracle).** Estándar de Java que permite crear componentes reutilizables. Debe implementar `Serializable` y contar con un constructor sin argumentos.
	
- **COM y DCOM (Microsoft).** Tecnología que permite crear componentes con interfaces bien definidas, reutilizables en distintos entornos y lenguajes.
	
- **CORBA (OMG).** Permite la interoperabilidad entre aplicaciones escritas en distintos lenguajes mediante una interfaz común (IDL).

Cada una de estas tecnologías busca la reutilización de componentes a través de la definición de interfaces claras y la ocultación de la implementación interna.

## 7. Empaquetado de componentes

Para distribuir un componente JavaBean, se empaqueta en un archivo **JAR** que incluye:  

- El componente (clases Java).  
- Objetos `BeanInfo` y `Customizer`.  
- Recursos como imágenes o clases auxiliares.  

El archivo **JAR** requiere un **manifiesto** (`.mf`) que identifique las clases como JavaBeans mediante `Java-Bean: True`. Ejemplo de creación manual usando la línea de comandos:  

```java  
jar cfm Componente.jar manifest.mf Componente.class ComponenteBeanInfo.class Imagen.png  
```  

En NetBeans, la opción **Limpiar y construir** genera automáticamente el JAR en la carpeta `/dist` del proyecto.  

Para añadir el componente a la paleta de NetBeans:  

3. Haz clic derecho en la paleta → **Administrador de paleta.**  
4. Selecciona la categoría (ej. *Componentes Personalizados*).  
5. Importa el archivo JAR. 
![[Administrador de paleta.jpg]]

## 8. Creación de un componente de ejemplo: Temporizador gráfico  

### Estructura básica del componente

El componente hereda de `JLabel` e implementa `Serializable` para cumplir con los requisitos de JavaBean:  

```java  
public class TemporizadorBean extends JLabel implements Serializable, ActionListener {  
    private Timer t;  
    private int tiempo;  

    public TemporizadorBean() {  
        tiempo = 5;  
        t = new Timer(1000, this); // Timer con intervalo de 1 segundo  
        setText(Integer.toString(tiempo));  
        t.start();  
    }  
}  
```  

### Añadir propiedades

La propiedad `tiempo` se define con métodos `get`/`set` para permitir la introspección. NetBeans facilita esto con la opción **Insertar Código → Agregar propiedad.**  

```java  
private int tiempo;  

public int getTiempo() {  
    return tiempo;  
}  

public void setTiempo(int tiempo) {  
    this.tiempo = tiempo;  
    setText(Integer.toString(tiempo)); // Actualiza la etiqueta  
    repaint();  
}  
```  

### Implementar el comportamiento

Se usa un `Timer` para decrementar el valor de `tiempo` cada segundo:  

```java  
@Override  
public void actionPerformed(ActionEvent e) {  
    tiempo--;  
    setText(Integer.toString(tiempo));  
    repaint();  

    if (tiempo == 0) {  
        t.stop();  
        // Lanzar evento de finalización  
        if (receptor != null) {  
            receptor.capturarFinCuentaAtras(new FinCuentaAtrasEvent(this));  
        }  
    }  
}  
```  

### Gestión de eventos

**Paso 1.** Crear una clase para el evento (hereda de `EventObject`):  

```java  
public class FinCuentaAtrasEvent extends EventObject {  
    public FinCuentaAtrasEvent(Object source) {  
        super(source);  
    }  
}  
```  

**Paso 2.** Definir una interfaz para el listener:  

```java  
public interface FinCuentaAtrasListener {  
    void capturarFinCuentaAtras(FinCuentaAtrasEvent ev);  
}  
```  

**Paso 3.** Añadir métodos para gestionar listeners en el componente:  

```java  
private FinCuentaAtrasListener receptor;  

public void addFinCuentaAtrasListener(FinCuentaAtrasListener receptor) {  
    this.receptor = receptor;  
}  

public void removeFinCuentaAtrasListener(FinCuentaAtrasListener receptor) {  
    this.receptor = null;  
}  
```  

### Uso en NetBeans

6. Genera el JAR con **Limpiar y construir.**  
7. Añade el componente a la paleta mediante el **Administrador de paleta.**  
8. En un formulario, arrastra el componente y gestiona su evento:  

```java  
// Ejemplo de manejo del evento en una aplicación  
temporizadorBean1.addFinCuentaAtrasListener(ev -> {  
    JOptionPane.showMessageDialog(null, "¡Tiempo agotado!");  
});  
```  

---

**Integración de recursos externos.**  
- El manifiesto y las imágenes deben incluirse en el JAR.  
- NetBeans detecta automáticamente propiedades y eventos gracias a la introspección.  

**Consejo clave.**  
- Usa herencia para reutilizar funcionalidad de componentes existentes (ej. `JLabel`).  
- Simplifica la gestión de eventos con las herramientas de NetBeans (ej. autogeneración de listeners).
