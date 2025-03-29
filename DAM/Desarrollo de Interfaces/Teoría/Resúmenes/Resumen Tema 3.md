---
tags: [DAM, DI]
cssclasses: [dam-di, table-compact-clean]
banner: "![[di.jpg]]"
banner_y: 0.72
---

# **Resumen Tema 3.** <br>Creación de Componentes Visuales

## 1. Concepto de Componente

### Definición

Clase reutilizable que puede manipularse visualmente.

### Características

| Característica | Descripción                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| **Estado**         | Almacenado en propiedades.                                                  |
| **Comportamiento** | Definido por eventos y métodos.                                             |
| **Interfaz**       | Subconjunto de atributos y métodos accesibles.                              |

### Requisitos

Modificabilidad, persistencia, introspección, gestión de eventos.

### Ventajas

| Ventaja                | Descripción                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| **Desarrollo rápido y económico** | Facilita la creación de aplicaciones de manera eficiente.                     |
| **Reducción de errores**    | Al ser reutilizable, disminuye la probabilidad de errores.                    |

## 2. Elementos de un Componente

### Propiedades y Atributos

| Elemento       | Descripción                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| **Atributos**      | Variables internas (privadas).                                              |
| **Propiedades**    | Atributos accesibles desde fuera (getter/setter).                           |

**Ejemplo:**

```java
public void setColor(String color)
public String getColor()
```

#### Editores de Propiedades

| Aspecto        | Descripción                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| **Propósito**      | Modificar valores de propiedades complejas.                                 |
| **Implementación** | Usar `PropertyEditorSupport` o `PropertyEditor`.                           |
| **Ejemplo**        | Editor para la propiedad `direccion`.                                      |

### Propiedades Simples e Indexadas

| Tipo           | Descripción                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| **Simples**        | Un único valor (getter/setter).                                             |
| **Indexadas**      | Conjunto de elementos (acceso por índice).                                  |

### Propiedades Compartidas y Restringidas

| Tipo           | Descripción                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| **Compartidas**    | Notifican cambios a otros objetos (`PropertyChangeListener`).               |
| **Restringidas**   | Permiten vetar cambios (`VetoableChangeListener`).                          |

## 3. Eventos

| Aspecto        | Descripción                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| **Definición**     | Acciones del usuario (clics, teclas) que generan respuestas.                |
| **Manejo de Eventos** | Crear clase para el evento, definir interfaz para el listener, añadir/eliminar oyentes. |

**Ejemplo:**

```java
public void add<Nombre>Listener(<Nombre>Listener l)
public void remove<Nombre>Listener(<Nombre>Listener l)
```

## 4. Introspección y Reflexión

| Aspecto        | Descripción                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| **Introspección**  | Detección dinámica de propiedades, métodos y eventos.                      |
| **Reflexión**      | Inspección de una clase en tiempo de ejecución.                            |
| **BeanInfo**       | Clase que describe explícitamente las características del componente.      |

## 5. Persistencia del Componente

| Tipo           | Descripción                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| **Serialización**  | Almacenamiento del estado de un objeto.                                     |
| **Automática**     | Implementar `Serializable`.                                                |
| **Programada**     | Implementar `Externalizable`.                                              |

## 6. Otras Tecnologías para Componentes Visuales

| Tecnología     | Descripción                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| **JavaBeans**      | Estándar de Java.                                                          |
| **COM/DCOM**       | Tecnología de Microsoft.                                                   |
| **CORBA**          | Interoperabilidad entre lenguajes.                                         |

## 7. Empaquetado de Componentes

| Aspecto        | Descripción                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| **Archivo JAR**    | Incluye clases, `BeanInfo`, recursos.                                      |
| **Manifiesto**     | Identifica clases como JavaBeans (`Java-Bean: True`).                      |
| **NetBeans**       | Genera automáticamente el JAR con **Limpiar y construir.**                 |

## 8. Creación de un Componente de Ejemplo: Temporizador Gráfico

### Estructura Básica

| Aspecto        | Descripción                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| **Herencia**       | Hereda de `JLabel`.                                                        |
| **Implementación** | Implementa `Serializable` y `ActionListener`.                              |

**Ejemplo:**

```java
public class TemporizadorBean extends JLabel implements Serializable, ActionListener {
    private Timer t;
    private int tiempo;
}
```

### Añadir Propiedades

| Aspecto        | Descripción                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| **Getter/Setter**  | Definir `getter` y `setter` para la propiedad `tiempo`.                    |

**Ejemplo:**

```java
public int getTiempo() { return tiempo; }
public void setTiempo(int tiempo) { this.tiempo = tiempo; }
```

### Implementar Comportamiento

| Aspecto        | Descripción                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| **Timer**          | Usar `Timer` para decrementar el tiempo.                                   |

**Ejemplo:**

```java
public void actionPerformed(ActionEvent e) {
    tiempo--;
    setText(Integer.toString(tiempo));
}
```

### Gestión de Eventos

| Aspecto        | Descripción                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| **Evento**         | Crear clase para el evento (`FinCuentaAtrasEvent`).                         |
| **Listener**       | Definir interfaz para el listener (`FinCuentaAtrasListener`).               |
| **Métodos**        | Añadir métodos para gestionar oyentes.                                     |

**Ejemplo:**

```java
public void addFinCuentaAtrasListener(FinCuentaAtrasListener receptor) {
    this.receptor = receptor;
}
```

### Uso en NetBeans

| Aspecto        | Descripción                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| **Generar JAR**    | Generar JAR y añadir a la paleta.                                          |
| **Manejo de Evento** | Ejemplo de manejo de evento:                                              |

**Ejemplo:**

```java
temporizadorBean1.addFinCuentaAtrasListener(ev -> {
    JOptionPane.showMessageDialog(null, "¡Tiempo agotado!");
});
```

## 9. Resumen final

| Aspecto        | Descripción                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| **Componente**     | Clase reutilizable con propiedades, eventos y métodos.                     |
| **Propiedades**    | Pueden ser simples, indexadas, compartidas o restringidas.                 |
| **Eventos**        | Permiten gestionar acciones del usuario.                                   |
| **Introspección**  | Facilita el uso de componentes en entornos visuales.                       |
| **Persistencia**   | Se logra mediante serialización.                                           |
| **JavaBeans**      | Estándar para crear componentes en Java.                                   |
| **NetBeans**       | Facilita la creación, empaquetado y uso de componentes visuales.           |
