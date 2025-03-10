---
number headings: first-level 0, max 3, skip ^skipped, _.1.1.
obsidianUIMode: preview
banner: "![[di.jpg]]"
banner_y: 0.28
---

# Resumen Tema 3

![Lectura MP3](Lectura_Resumen_Tema_3.mp3)

## 1. Concepto de Componente
### 1.1. **Definición**

Clase reutilizable que puede manipularse visualmente.

### 1.2. **Características**
- **Estado.** Almacenado en propiedades.
- **Comportamiento.** Definido por eventos y métodos.
- **Interfaz.** Subconjunto de atributos y métodos accesibles.
### 1.3. **Requisitos**

Modificabilidad, persistencia, introspección, gestión de eventos.

### 1.4. **Ventajas**
- Desarrollo rápido y económico.
- Reducción de errores.

## 2. Elementos de un Componente
### 2.1. **Propiedades y Atributos**
- **Atributos.** Variables internas (privadas).
- **Propiedades.** Atributos accesibles desde fuera (getter/setter).
- **Ejemplo.**

	```java
    public void setColor(String color)
    public String getColor()
    ```

#### Editores de Propiedades
- **Propósito.** Modificar valores de propiedades complejas.
- **Implementación.** Usar `PropertyEditorSupport` o `PropertyEditor`.
- **Ejemplo.** Editor para la propiedad `direccion`.
### 2.2. **Propiedades Simples e Indexadas**
- **Simples.** Un único valor (getter/setter).
- **Indexadas.** Conjunto de elementos (acceso por índice).

### 2.3. **Propiedades Compartidas y Restringidas**
- **Compartidas.** Notifican cambios a otros objetos (`PropertyChangeListener`).
- **Restringidas.** Permiten vetar cambios (`VetoableChangeListener`).

## 3. Eventos
- **Definición.** Acciones del usuario (clics, teclas) que generan respuestas.
- **Manejo de Eventos.**
  - Crear clase para el evento.
  - Definir interfaz para el listener.
  - Añadir/eliminar oyentes.
  - Ejemplo:

	```java
    public void add<Nombre>Listener(<Nombre>Listener l)
    public void remove<Nombre>Listener(<Nombre>Listener l)
    ```

## 4. Introspección y Reflexión
- **Introspección.** Detección dinámica de propiedades, métodos y eventos.
- **Reflexión.** Inspección de una clase en tiempo de ejecución.
- **BeanInfo.** Clase que describe explícitamente las características del componente.

## 5. Persistencia del Componente
- **Serialización.** Almacenamiento del estado de un objeto.
- **Tipos.**
  - **Automática.** Implementar `Serializable`.
  - **Programada.** Implementar `Externalizable`.

## 6. Otras Tecnologías para Componentes Visuales
- **JavaBeans.** Estándar de Java.
- **COM/DCOM.** Tecnología de Microsoft.
- **CORBA.** Interoperabilidad entre lenguajes.

## 7. Empaquetado de Componentes
- **Archivo JAR.** Incluye clases, `BeanInfo`, recursos.
- **Manifiesto.** Identifica clases como JavaBeans (`Java-Bean: True`).
- **NetBeans.** Genera automáticamente el JAR con **Limpiar y construir**.

## 8. Creación de un Componente de Ejemplo: Temporizador Gráfico
### 8.1. **Estructura Básica**
- Hereda de `JLabel`.
- Implementa `Serializable` y `ActionListener`.
- Ejemplo:

	```java
    public class TemporizadorBean extends JLabel implements Serializable, ActionListener {
        private Timer t;
        private int tiempo;
    }
    ```

### 8.2. **Añadir Propiedades**
- Definir `getter` y `setter` para la propiedad `tiempo`.
- Ejemplo:

	```java
    public int getTiempo() { return tiempo; }
    public void setTiempo(int tiempo) { this.tiempo = tiempo; }
    ```

### 8.3. **Implementar Comportamiento**
- Usar `Timer` para decrementar el tiempo.
- Ejemplo:

	```java
    public void actionPerformed(ActionEvent e) {
        tiempo--;
        setText(Integer.toString(tiempo));
    }
    ```

### 8.4. **Gestión de Eventos**
- Crear clase para el evento (`FinCuentaAtrasEvent`).
- Definir interfaz para el listener (`FinCuentaAtrasListener`).
- Añadir métodos para gestionar oyentes.
- Ejemplo:

	```java
    public void addFinCuentaAtrasListener(FinCuentaAtrasListener receptor) {
        this.receptor = receptor;
    }
    ```

### 8.5. **Uso en NetBeans**
- Generar JAR y añadir a la paleta.
- Ejemplo de manejo de evento:

	```java
    temporizadorBean1.addFinCuentaAtrasListener(ev -> {
        JOptionPane.showMessageDialog(null, "¡Tiempo agotado!");
    });
    ```

## 9. Resumen final
- Un componente es una clase reutilizable con propiedades, eventos y métodos.
- Las propiedades pueden ser simples, indexadas, compartidas o restringidas.
- Los eventos permiten gestionar acciones del usuario.
- La introspección y reflexión facilitan el uso de componentes en entornos visuales.
- La persistencia se logra mediante serialización.
- JavaBeans es el estándar para crear componentes en Java.
- NetBeans facilita la creación, empaquetado y uso de componentes visuales.
