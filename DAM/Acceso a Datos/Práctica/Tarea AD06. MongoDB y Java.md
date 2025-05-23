---
tags: [AD, DAM]
cssclasses:
  - dam-ad
  - table-compact-clean
banner: "![[ad.jpg]]"
banner_y: 0.32
number headings: off
---
# **Tarea AD06.** <br>MongoDB y Java

## 1. Parte 1: MongoDB (4 puntos)

### 1.1. **Instrucciones iniciales**

1. Utiliza Compass u otro cliente MongoDB para realizar esta parte.
2. Crea una **colección** en la base de datos llamada `sakila`.  
	Importa en ella el contenido del archivo `sakilaPetit.json`.
3. Crea un documento con las respuestas a los ejercicios y súbelo al aula virtual.

### 1.2. **Ejercicios**

#### Ejercicio 1 (1 punto)

Muestra **solo la duración y el título** de todas las películas con una duración **mayor o igual a 90 minutos**, ordenadas por título.

> *Nota: La base de datos devuelve 33 resultados.*

#### Ejercicio 2 (1,5 puntos)

Muestra todas las **categorías** (id y nombre), **sin repeticiones.**

> *Nota: La base de datos devuelve 16 resultados.*

#### Ejercicio 3 (1,5 puntos)

Usa `aggregate` para mostrar el **identificador**, **título** y **descripción** de todas las películas en las que aparecen los actores con `actorId` igual a **1** o **10.**

> *Nota: La base de datos devuelve 4 resultados.*

## 2. Parte 2: MongoDB + Java (6 puntos)

### 2.1. **Requisitos iniciales**

- Lee todo el enunciado antes de comenzar.
- Crea dos proyectos (pueden o no usar Maven):

#### 1. ut6-practica-component

- Debe incluir el **driver de MongoDB.**
- Este proyecto es el **único** que puede acceder a la base de datos.
- **No puede interactuar con el usuario.**
- Su **.jar no debe ser ejecutable.**

#### 2. ut6-practica-gui

- Debe incluir el .**jar generado por `ut6-practica-component`.**
- Puedes usar **Swing**, **JavaFX**, **AWT**, etc., para la interfaz gráfica.
- Los errores deben tratarse con **una excepción personalizada.**

### 2.2. **ut6-practica-component (5 puntos)**

#### Ejercicio 2 (1 punto)

Crea tres clases **POJO.**

- **Actor:** con atributos `id`, `nombre`, `apellido`.
- **Categoria:** con atributos `id`, `valor`.
- **Film:** con atributos `id`, `título`, `descripción`, `año`, `duración`.

> Cada POJO debe incluir:
> - Constructor
> - Getters y setters
> - `equals`, `hashCode` y `toString`
> - Consejo: nombrar los identificadores como `id` facilitará la conversión desde MongoDB.

---

#### Ejercicio 3 (4 puntos)

Crea una clase que **centralice las operaciones con la base de datos.**  
No debe imprimir nada ni acceder al teclado.

**Atributos de la clase**

- URL de conexión
- Base de datos (sakila)
- Colección (films)

**Métodos requeridos**

##### 3.1 Recupera las **categorías.**  (1 punto)

> Devuelve una lista de objetos `Categoria` (esperados: 16).

##### 3.2 Recupera todos los **actores.** (1 punto)

> Devuelve una lista de objetos `Actor` (esperados: 157).

##### 3.3 Filtra películas por **actor** y **categoría** (2 puntos)

Recibe dos `Integer` como parámetros). Si alguno es `null`, **no debe tenerse en cuenta en el filtrado.**

> No se permite usar agregación.
> - Solo categoría 11: 9 resultados
> - Solo actor 162: 8 resultados
> - Ambos criterios: 1 resultado

### 2.3. **ut6-practica-gui (1 punto)**

#### Ejercicio 4 (1 punto)

- Incluye el .**jar del proyecto `ut6-practica-component`.**
- Crea una **interfaz gráfica sencilla** para probar los métodos del componente.
- Debe permitir al usuario **elegir una categoría y un actor** (por ejemplo, con menús desplegables).
- Al seleccionar una categoría o actor, se debe **actualizar la lista de películas mostradas**, llamando al método del **Ejercicio 3.3.**
- Se debe mostrar al menos:  
	`título`, `id`, y `descripción` de cada película (por ejemplo, en un `textArea`).
- Se debe incluir una opción de **"Todos"** para actores o categorías, que se traducirá a `null` en la consulta.

![](../../../_Media/Imágenes/AD/Pasted%20image%2020250503040530.png)

## 3. Entrega

Sube a Aula Virtual un ZIP que contenga:

1. Un documento con las **respuestas de la parte MongoDB.**
2. Un ZIP por cada uno de los **proyectos** (`component` y `gui`) con el proyecto completo.
3. Los .**jar** generados de ambos proyectos.

## 4. Evaluación

- Cada apartado indica su puntuación sobre 10.
- No seguir las **normas de nomenclatura y formato en Java** penalizará hasta un **10%** de la nota de ese ejercicio.
- Esta práctica representa el **8,33%** de la nota de actividades del curso.
