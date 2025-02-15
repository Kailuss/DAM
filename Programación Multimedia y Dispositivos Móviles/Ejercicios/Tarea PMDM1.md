---
tags:
  - PMDM
  - Tarea
---
# Realiza los siguientes supuestos prácticos con Dart

Puedes utilizar el entorno que desees para ejecutarlo.

Se nos pide que programemos el sistema para gestionar un **rent a car** en la costa norte de Mallorca. Este rent a car alquila vehículos de diferentes tipos, **coches y motos**, a clientes. 

## Creación de la clase Cliente

Por lo que respecta a los clientes, solo nos interesa tener su ficha con todos sus datos y un método de pago. 

### Atributos:
- DNI (variable privada).
- Nombre completo.
- Correo electrónico.
- Teléfono.
- Número de tarjeta de crédito.

### Constructores:
- Un constructor con **DNI y nombre**. El resto de atributos tendrán valores por defecto (`null` o vacío).
- Un constructor con **todos sus atributos**.

### Métodos:
- Métodos `get` para todos los atributos.
- Métodos `set` para todos los atributos.
- Sobrescribe el método `toString`.

## Creación de las clases Coche y Moto

Las clases **Coche** y **Moto** compartirán ciertos atributos.

### Atributos:
- Matrícula.
- Marca.
- Modelo.
- Estado de alquiler (`boolean`, por defecto `false`).
- Cliente al que está alquilado (DNI).
- Kilometraje (por defecto `0`).
- **Moto**: adicionalmente, incluirá la cilindrada.

### Constructores:
- Constructor por defecto sin atributos.
- Constructor con solo la matrícula (el resto por defecto).
- Constructor con todos los atributos.

### Métodos:
- Métodos `get` de todos los atributos.
- Métodos `set` de todos los atributos.
- Sobrescribe el método `toString`.

## Creación de la clase abstracta Vehículo

Dado que Coche y Moto tienen atributos comunes, se propone la creación de una **clase abstracta `Vehículo`**.

### Métodos a implementar:
- `alquilar()`: cambia el estado de alquiler a `true`.
- `devolver()`: cambia el estado de alquiler a `false`.
- `estaAlquilado()`: devuelve si el vehículo está alquilado.
- `compareTo(Object a)`: compara el kilometraje de dos vehículos, **solo si son del mismo tipo** (dos coches o dos motos). Se recomienda el uso de **casting de objetos**.

## Implementación de la aplicación

### Pasos a seguir:
1. Crear **dos listas**, una de coches y otra de motos, de **5 posiciones cada una**.
2. Utilizar los diferentes **constructores** para crear e inicializar **5 coches y 5 motos** y almacenarlos en sus respectivas listas.
3. Crear uno o varios **clientes** para alquilar vehículos.
4. Realizar la **entrega** de algunos coches y motos utilizando el método `alquilar()`.
5. Contar cuántos **coches y motos están alquilados** y mostrar la cantidad total.
6. Identificar **el coche con más kilómetros** y **la moto con más kilómetros**, mostrando sus datos mediante `toString()`.

## Criterios de calificación

La calificación total es de **10 puntos**.

### Funcionamiento del programa (**6 puntos**):
- La aplicación debe funcionar correctamente sin errores.
- Cumplir con todos los apartados del enunciado.

### Diseño y estructura de clases (**3 puntos**):
- Correcta implementación de **clases y herencia**.

### Organización y documentación (**1 punto**):
- Código correctamente **comentado y organizado**.
- Separación en **funciones** cuando sea necesario.
- Organización adecuada en **directorios**.

### Video de demostración (**2 puntos**):
- Explicación clara del código y su ejecución.
- Duración máxima de **3 minutos**.

### Penalización:
- **Plagio** = 0 puntos.
- **Errores de compilación** = 0 puntos.
- **Ejecución incorrecta** = 0 puntos.

## Entrega de la práctica

El alumno debe adjuntar:
- Todo el **código fuente del proyecto**.
- Un **video corto** mostrando la ejecución de las actividades.
