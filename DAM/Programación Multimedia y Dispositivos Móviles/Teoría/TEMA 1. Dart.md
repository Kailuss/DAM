---
number headings: off
tags:
  - DAM
  - PMDM
banner: "![[pmdm.jpg]]"
banner_y: 0.42
cssclasses:
  - dam-pmdm
  - table-compact-clean
---

# **TEMA 1.** <br> Introducción a Dart


| **Subtemas** |
| --- |
| **[TEMA 1.1. Tipos de Datos](TEMA%201.1.%20Tipos%20de%20Datos.md)** |
| **[TEMA 1.2. Estructuras de Control](TEMA%201.2.%20Estructuras%20de%20Control.md)** |
| **[TEMA 1.3. Clases en Dart](TEMA%201.3.%20Clases%20en%20Dart.md)** |
| **[TEMA 1.4. Programación Asíncrona en Dart](TEMA%201.4.%20Programación%20Asíncrona%20en%20Dart.md)** |

| Anexos |
| --- |
| [Tarea PMDM01](../Práctica/Tareas/Tarea%20PMDM01.md) |
| [Ejercicios de Dart](../Práctica/Ejercicios%20de%20Dart.md) |


## Conceptos básicos 


|     |     |
| --- | --- |
| **Estructura mínima de un programa** |Todo programa en Dart requiere una función `main()` como punto de entrada.  
| **Comentarios** |Muestra cómo escribir comentarios de una línea (`//`) y multilínea (`/* ... */`), incluyendo anidación de estos últimos.  
| **Salida básica** |Uso de `print()` para mostrar mensajes en la consola.  

```dart
// Programa de ejemplo con comentarios
void main() {
  // Comentario de una línea
  
  /*
    Comentario multilínea
    Podemos anidar comentarios
    /*
      Como este comentario interno
    */
  */
  
  print('¡Hola, mundo de Dart!');
}
```