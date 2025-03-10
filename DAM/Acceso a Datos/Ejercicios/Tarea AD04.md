---
number headings: first-level 0, max 2, skip ^skipped, _.1.1.
node_size: 16
obsidianUIMode: preview
tags:
  - Focus
---

# Tarea AD04

## 1. Introducción

Trabajaremos con una parte de una base de datos que utiliza una empresa concesionaria de autopistas de peaje. Para evitar atascos, esta empresa proporciona a sus clientes unos dispositivos, **ezPass**, que se instalan dentro del coche y permiten no detenerse en los peajes.

Cada cliente puede tener más de un dispositivo de este tipo y utilizarlo con varios vehículos. Por este motivo, existe la tabla **associate**, que relaciona un **ezPass** con un vehículo dentro de unas fechas determinadas.

La empresa guarda todos los viajes (**trip**) que realizan sus clientes para poder facturarlos a final de mes. Para cada viaje, entre otros datos, registra los peajes y los momentos de entrada y salida.

El diagrama de la base de datos es el siguiente:

![](../Teoría/Imágenes/Pasted%20image%2020250223174324.png)

## 2. Instrucciones

1. Crea un proyecto con tu IDE.
2. Incluye **Hibernate** y el **driver de MySQL**.
3. Distribuye el código en paquetes.
4. Crea una clase con **main**. En esta clase probaremos todos los métodos que se pidan en el enunciado.
    - Esta clase no puede interactuar directamente con la base de datos.
    - Es la única clase que puede mostrar algo por consola.
5. Utiliza **JPA** para resolver todos los ejercicios.

**Datos de conexión:**

- **Host:** davv.paucasesnovescifp.cat
- **Puerto:** 3306
- **Base de datos:** peatges
- **Usuario:** usuari
- **Contraseña:** seCret_24

> [!warning] **Importante:**  
> La base de datos se reinicia cada noche sobre las **tres de la madrugada**. Si, por ejemplo, hoy realizas **inserts** o **updates**, mañana no estarán.

## 3. Ejercicios

### Ejercicio 1 (2 puntos)

En un paquete creado específicamente para ello, crea una clase que gestione todas las operaciones con la base de datos.

- Debe tener un **atributo de instancia** para la unidad de persistencia que se va a utilizar. Este atributo **no puede ser null**.
- Debe tener un **método** para crear el `EntityManagerFactory` y el `EntityManager`, y otro método para cerrarlos.

Cuando uses esta clase, asegúrate de que siempre se llame al método que cierra las conexiones antes de finalizar el programa. Por ejemplo, usando un `try` y llamando al método de cierre en el `finally`.

El control de errores debe gestionarse mediante **una excepción propia** de la aplicación.

### Ejercicio 2 (4 puntos)

#### Ejercicio 2.1 (2 puntos)

- Crea una **entidad** llamada `Peatge` (peaje) que esté mapeada a la tabla `TOLLS` de la base de datos.
- Debe tener **atributos** para las dos columnas de la tabla y validar los datos: ambos atributos son **obligatorios**.
- En el esquema de la base de datos proporcionado al inicio se puede consultar la **longitud máxima** de estos campos.

El control de errores debe hacerse con **una excepción propia** de la aplicación.

#### Ejercicio 2.2 (2 puntos)

En la clase que centraliza las operaciones con la base de datos, crea los siguientes métodos:

- Un método que **reciba el identificador** de un peaje (`toll`) y **devuelva** ese peaje. Debe controlar que el **identificador no sea null**.
- Un método que **devuelva todos los peajes** ordenados alfabéticamente por el nombre. Utiliza una **NamedQuery** para implementarlo.

### Ejercicio 3 (4 puntos)

Añade al proyecto la clase de entidad `Trip` que encontrarás en el aula virtual.

Modifica la clase `Peatge` para que tenga **atributos** que representen:

- Los viajes que tienen este peaje como `inicio`.
- Los viajes que tienen este peaje como `final`.

En la clase que centraliza las operaciones con la base de datos:

#### Ejercicio 3.1 (2 puntos)

- Crea un **método** que reciba un objeto `Peatge` y un **booleano**, y devuelva la lista de **viajes** que tienen ese peaje como inicio o como final, dependiendo del valor del booleano.
    - Si el booleano es `true`, devolverá los viajes que tienen el peaje como `inicio`.
    - Si es `false`, devolverá los viajes que tienen el peaje como `final`.

**No puedes utilizar consultas** para implementar este método.

#### Ejercicio 3.2 (2 puntos)

Crea un **método** que reciba un objeto `Peatge` y devuelva una lista de los **viajes** que lo tienen tanto como inicio como final. Es muy raro que un viaje tenga el **mismo peaje** como inicio y como final, ya que normalmente no se entra y sale de la autopista por el **mismo peaje**.

Utiliza una **consulta JPQL** para implementar este método.

## 4. Entrega

Debes entregar en el **aula virtual**:

- Un **archivo ZIP** con el **proyecto completo**, no solo el código fuente.
- El **archivo JAR** del proyecto.

## 5. Evaluación

- Cada apartado indica la **puntuación** sobre 10.
- No respetar las **normas de nomenclatura o formato** de Java penalizará hasta un **10% de la nota** de cada ejercicio (por ejemplo, si un ejercicio vale **3 puntos**, se descontará hasta **0,3 puntos** por errores de formato).
- Esta práctica representa el **8,33% de la nota total** de actividades del curso.