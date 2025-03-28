---
number headings: max 3, _.1.1., skip ^sk
tags: [DAM, PMDM]
banner: "![[pmdm.jpg]]"
banner_y: 0.42
cssclasses: [dam-pmdm, table-compact-clean]
---

# **TEMA 1.1.** <br>Estructuras de Control

## 1. Condicionales
Este ejemplo introduce las estructuras condicionales básicas en Dart, mostrando tres formas de manejar decisiones en el código.

```dart
void main() {
  var nombre = 2;

  // 1. If simple de una línea
  if (nombre == 2) print('El nombre és igual a 2'); // Condición básica
  
  // 2. If-elseif-else tradicional
  if(nombre > 5){
    print('Mayor que 5');
  } else if (nombre < 5){       // Else if para múltiples condiciones
    print('Menor que 5');
  } else {
    print('Es exactamente 5');  // Else final
  }

  // 3. Operador ternario (if-else en una línea)
  nombre == 2 ? print('Es 2') : print('No es 2'); // Forma compacta
}
```


| Mejores usos    |     |
| --- | --- |
| **If simple** | Para ejecuciones condicionales de una sola acción.    |
| **If-elseif-else** | Permite manejar múltiples caminos de ejecución. |
| **Ternario** | Ideal para asignaciones o ejecuciones simples basadas en una condición.|

## 2. Bucles
Muestra tres formas diferentes de iterar sobre colecciones en Dart, cada una con sus ventajas específicas.

```dart
void main() {
  var animals = ['perro', 'gato', 'elefante'];

  // 1. For clásico (con índice)
  for (var i = 0; i < animals.length; i++) {
    print('Animal ${i+1}: ${animals[i]}'); // Acceso por índice
  }

  // 2. ForEach (estilo funcional)
  animals.forEach((animal) => print(animal)); // Función anónima

  // 3. For-in (iteración directa)
  for (var animal in animals) {  // Más legible
    print(animal.toUpperCase()); // Transformación
  }
}
```

| Tipo de bucle      | Mejor uso                  | Ejemplo                  |
|------------|----------------------------|--------------------------|
| **For**    | Necesidad de índice        | `for (var i=0; i<10; i++)` |
| **ForEach**| Funciones anónimas         | `list.forEach(print)`    |
| **For-in** | Legibilidad en colecciones | `for (var item in list)` |

## 3. Switch-Case
Demuestra cómo manejar múltiples casos de forma más limpia que con múltiples if-else.

```dart
int diaSemana(String nombreDia) {
  switch (nombreDia) {
    case 'lunes':    // Caso concreto
      return 0;
    case 'martes':
      return 1;
    // ... otros días ...
    default:         // Caso por defecto
      return -1; 
  }
}

// Versión alternativa usando listas
int diaSemana2(String nombreDia) => 
    ['lunes','martes',...].indexOf(nombreDia); // Más conciso
```

| Puntos clave    |     |
| --- | --- |
| **Break obligatorio** | Cada `case` debe terminar con `break` (a menos que sea un fallthrough intencional).|
| **Default**|Maneja todos los casos no especificados.|
| **Alternativa con listas**|Para casos simples, usar `indexOf` puede ser más eficiente.|

## 4. While/Do-While
Explica la diferencia entre evaluar la condición antes o después de ejecutar el bloque.

```dart
void main() {
  var alumnos = ['Ana', 'Juan', 'Pep'];
  var i = 0;
  var encontrado = false;

  // 1. While (evalúa primero)
  while (!encontrado && i < alumnos.length) {
    if (alumnos[i] == 'Pep') {
      encontrado = true;
      print('¡Encontrado en posición $i!');
    }
    i++;
  }

  // 2. Do-While (ejecuta al menos una vez)
  i = 0;
  do {
    print('Buscando... ${alumnos[i]}');
    i++;
  } while (i < alumnos.length);
}
```

**Diferencias clave:**

| Característica | While                      | Do-While              |
|----------------|----------------------------|-----------------------|
| **Evaluación** | Condición antes del bloque | Condición después     |
| **Garantía**   | Cero ejecuciones posibles  | Mínimo una ejecución  |

## 5. Conclusión General

Estas estructuras son fundamentales para:

1. **Controlar el flujo** del programa (if/switch).
2. **Repetir tareas** eficientemente (bucles).
3. **Manejar casos complejos** de forma legible.

**Recomendaciones:**
- Usar **ternarios** para condiciones simples.
- Preferir **for-in** para iterar colecciones.
- Emplear **switch** cuando hay más de 3 casos fijos.
- Elegir **do-while** cuando se requiera al menos una ejecución.
