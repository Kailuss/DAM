---
tags: [DAM, PMDM]
cssclasses: [dam-pmdm, table-compact-clean]
banner: "![[pmdm.jpg]]"
banner_y: 0.42
---
# Ejercicios de **Dart**

## 1. Filtrado de listas

**Ejercicio 1 - Filtrado básico**

Este ejercicio introduce el manejo básico de listas y estructuras de control en Dart. A través de un bucle `for-in`, se filtran los números menores a 5 de una lista predefinida. La versión compacta con _lista por comprensión_ demuestra la sintaxis concisa de Dart para operaciones comunes, destacando cómo simplificar código manteniendo legibilidad. Se enfatiza:

- Iteración sobre colecciones.
- Uso de condicionales dentro de bucles.
- Generación de listas dinámicas en una sola línea.

```dart
void main() {
  List<int> numeros = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];

  // Método tradicional con for-in
  for (var numero in numeros) {
    if (numero < 5) {
      print(numero);
    }
  }
  
  // Versión compacta con lista por comprensión
  print([for (var numero in numeros) if (numero < 5) numero]);
}
```

**Conceptos clave:**
- Iteración con `for-in`
- Condicionales dentro de bucles
- Listas por comprensión (generación de listas en una línea)
- Sintaxis concisa de Dart

## 2. Trabajo con listas y conjuntos

**Ejercicio 2 - Intersección de listas**

El ejercicio contrasta dos enfoques para encontrar elementos comunes entre listas:

1. **Método tradicional:** Usa bucles anidados y un `Set` para evitar duplicados, ideal para entender flujos de control y estructuras de datos básicas.
2. **Método eficiente:** Aprovecha la clase `Set` y su método `intersection`, mostrando cómo las estructuras de datos optimizadas simplifican operaciones complejas.

**Objetivo:** Enseñar la importancia de elegir el algoritmo adecuado y cómo Dart ofrece herramientas nativas para manejo de colecciones.

```dart
void main() {
  List<int> lista1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
  List<int> lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 89];
  Set<int> resultado = {};

  // Método tradicional con bucles
  for (var i in lista1) {
    for (var j in lista2) {
      if (i == j) {
        resultado.add(i);
      }
    }
  }
  print(resultado.toList());

  // Método eficiente usando conjuntos
  print(Set.from(lista1).intersection(Set.from(lista2)).toList());
}
```

**Conceptos clave:**
- `Set`: Colección de elementos únicos
- `intersection`: Método que encuentra elementos comunes entre conjuntos
- Conversión entre listas y conjuntos

## 3. Estructuras de control y operadores ternarios

**Ejercicio 3 - Palíndromos**

Se aborda la manipulación de cadenas y el uso de operadores ternarios:

- `split('')`, `reversed`, y `join('')` para invertir una cadena.
- Comparación directa entre la cadena original y la invertida.
- Operador ternario como alternativa limpia a condicionales `if-else`.  

**Clave:** Demuestra cómo Dart trata las cadenas como listas de caracteres y promueve código expresivo.

```dart
void main() {
  String input = 'aeiea';
  String revInput = input.split('').reversed.join('');
  
  // Operador ternario
  input == revInput
      ? print("La cadena ${input} es un palíndromo")
      : print("La cadena ${input} no es un palíndromo");
}
```

**Conceptos clave:**
- `split('')`: Divide la cadena en una lista de caracteres
- `reversed`: Invierte el orden de la lista
- `join('')`: Vuelve a unir los caracteres en una cadena
- Operador ternario: Forma compacta de escribir condicionales `condición ? valor_si_verdadero : valor_si_falso`

## 4. Encontrar el máximo valor

**Ejercicio 4 - Máximo de tres números**

Comparación de valores y manejo de listas:

- **Enfoque condicional:** Uso de `if-else` para comparar variables individuales, ideal para principiantes.
- **Enfoque con listas:** Métodos `sort()` y `last` para encontrar el máximo en una colección, mostrando la potencia de las operaciones integradas.  

**Mensaje:** Dart permite resolver un problema de múltiples formas, según legibilidad o eficiencia.

```dart
void main() {
  var maximo;
  int a = 1;
  int b = 2;
  int c = 4;

  // Método con comparaciones
  if (a > b) {
    maximo = a;
  } else {
    maximo = b;
  }
  if (c > maximo) {
    maximo = c;
  }
  print(maximo);

  // Método usando listas
  List numeros = [a, b, c, 4, 5, 2, 1];
  numeros.sort();
  print(numeros.last);
}
```

**Conceptos clave:**
- Comparación de valores
- Uso de listas para operaciones múltiples
- Método `sort()` y propiedad `last`

## 5. Manipulación de listas y bucles

**Ejercicio 5 - Filtrar elementos pares**

Filtrado de listas basado en índices:

- Uso de un contador (`i`) para verificar posiciones pares.  
- Listas por comprensión con condiciones complejas.  

**Relevancia:** Introduce el concepto de "índice" en colecciones y cómo combinarlo con condiciones.

```dart
void main() {
  List<int> numeros = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100];
  List<int> resultado = [];

  // Método tradicional
  int indice = 0;
  for (var numero in numeros) {
    if (++indice % 2 == 0) {
      resultado.add(numero);
    }
  }
  print(resultado);
  
  // Método compacto con lista por comprensión
  print([for (var numero in numeros) if (++indice % 2 == 0) numero]);
}
```

**Conceptos clave:**
- Incremento de contadores (`++indice`)
- Operador módulo (`%`) para determinar pares
- Listas por comprensión

## 6. Números primos y generación aleatoria

**Ejercicio 6 - Números primos**

Algoritmos matemáticos y optimización:

- Función `esPrimo` que verifica divisibilidad hasta `√n` (eficiencia).
- Generación de listas con divisores usando comprensión.
- Operador ternario para resultados legibles.  
    **Foco:** Cómo Dart facilita implementar lógica matemática con sintaxis clara.

```dart
import 'dart:math';

void main() {
  final random = Random();
  int numeroAleatorio = random.nextInt(100);
  compruebaPrimo(numeroAleatorio);
}

void compruebaPrimo(int numero) {
  // Generamos lista de divisores
  List<int> divisores = [
    for (var i = 1; i <= numero; i++)
      if (numero % i == 0) i
  ];

  // Comprobamos si es primo (solo divisible por 1 y sí mismo)
  divisores.length == 2
      ? print('El número: ${numero} es primo')
      : print('El número: ${numero} no es primo');
}
```

**Conceptos clave:**
- Generación de números aleatorios con `Random()`
- Concepto matemático de número primo
- Generación de listas con condiciones

## 7. Manipulación de cadenas

**Ejercicio 7 - Invertir frase**

Manipulación avanzada de cadenas:

- `split(' ')` divide la frase en palabras.    
- `reversed` invierte el orden de la lista.
- `join(' ')` reconstruye la cadena.  
    **Objetivo:** Mostrar cadenas como colecciones y métodos encadenados para transformaciones complejas.

```dart
void main() {
  String frase = 'El meu nom és Jaume';
  invertirFrase(frase);
}

void invertirFrase(String frase) {
  /* 
  1. Separamos la cadena en una lista de palabras
  2. Invertimos el orden de la lista
  3. Unimos las palabras con espacios
  */
  String resultado = frase.split(" ").reversed.toList().join(" ");
  print(resultado);
}
```

**Conceptos clave:**
- `split(" ")`: Divide la cadena por espacios
- `reversed`: Invierte el orden de la lista
- `join(" ")`: Une elementos con separador

## 8. Generación de contraseñas seguras

**Ejercicio 8 - Generador de contraseñas**

Seguridad y aleatoriedad:

- `Random.secure()` para generación criptográfica.
- Codificación `base64UrlEncode` para strings seguros.
- `shuffle()` para mezclar caracteres.  

**Importante:** Enfatiza buenas prácticas en generación de datos aleatorios.

```dart
import 'dart:convert';
import 'dart:math';

void main() {
  int seguridad = 20;
  generarPassword(seguridad);
}

void generarPassword(int seguridad) {
  final random = Random.secure();
  List<int> listaEnteros = List.generate(seguridad, (_) => random.nextInt(255));
  List listaCaracteres = base64UrlEncode(listaEnteros).split('').toList();
  listaCaracteres.shuffle();
  print("Tu contraseña es: ${listaCaracteres.join('')}\n");
}
```

**Conceptos clave:**
- `Random.secure()`: Generador seguro de números aleatorios
- `base64UrlEncode`: Codificación segura de bytes a cadena
- `shuffle()`: Mezcla aleatoria de elementos

## 9. Patrones de impresión

**Ejercicio 9 - Tablero de juego**

Patrones y diseño con texto:

- Multiplicación de cadenas (`---` * 3) para crear líneas.
- Bucles para estructuras repetitivas.  

**Aplicación:** Ideal para entender cómo construir interfaces simples en consola.

```dart
void main() {
  imprimirTablero(3);
}

void imprimirTablero(int numeroCubos) {
  // Elementos básicos de diseño
  String lineas = " ---";
  String columnas = "|   ";

  // Bucle para imprimir filas y columnas
  for (var i = 0; i < numeroCubos; i++) {
    print(lineas * numeroCubos);
    print(columnas * (numeroCubos + 1));
  }

  // Añadimos la última línea inferior
  print("${lineas * numeroCubos}\n");
}
```

**Conceptos clave:**
- Multiplicación de cadenas (`" ---" * 3`)
- Bucles para patrones repetitivos
- Diseño de interfaces de texto simples

## 10. Programación orientada a objetos

**Ejercicio 10 - Sistema de nóminas**

Programación orientada a objetos:

- Clase abstracta `Trabajador` con métodos comunes.
- Herencia en `Administrativo` y `Comercial`.
- Polimorfismo con `@override` en `salarioNeto()`.  

**Mensaje:** Dart soporta herencia y abstracción para modelar problemas reales.

```dart
void main() {
  Administrativo maria = Administrativo();
  maria.nombre = 'Maria';
  maria.salario = 100;
  maria.retencion = 10;
  maria.imprimirNombre();
  maria.salarioNeto();
  
  Comercial aina = Comercial();
  aina.nombre = 'Aina';
  aina.salario = 100;
  aina.retencion = 10;
  aina.ventas = 5;
  aina.comision = 0.75;
  aina.imprimirNombre();
  aina.salarioNeto();
}

abstract class Trabajador {
  var id;
  String? nombre;
  double? salario, retencion;
  
  void imprimirNombre() {
    print('El nombre del trabajador/a es: $nombre');
  }
  
  void salarioNeto();
}

class Administrativo extends Trabajador {
  @override
  void salarioNeto() {
    var porcentaje = 1 - retencion! / 100;
    print('El salario neto de $nombre es: ${salario! * porcentaje}');
  }
}

class Comercial extends Trabajador {
  int? ventas;
  double? comision;
  
  @override
  void salarioNeto() {
    var porcentaje = 1 - retencion! / 100;
    var extra = ventas! * comision!;
    print('El salario neto de $nombre es: ${salario! * porcentaje + extra}');
  }
}
```

**Conceptos clave:**
- Clases abstractas y herencia
- Polimorfismo y anulación de métodos (`@override`)
- Variables nullable (`?`) y operador de afirmación nula (`!`)
- Cálculos con porcentajes

## 11. Formateo de tiempo

**Ejercicio 11 - Formato HH:MM:SS**

Funciones y parámetros:

- `StringBuffer` para construcción eficiente.
- Funciones auxiliares (`escribirConCero`) para evitar repetición.
- Parámetros nombrados y valores por defecto.  

**Clave:** Mejora de legibilidad y reutilización de código.

```dart
// Versión con condicionales básicos
String hhmmssAntiguo(int h, int m, int s) {
  var buffer = StringBuffer();

  if (h < 10) buffer.write(0);
  buffer.write(h);
  if (m < 10) buffer.write(0);
  buffer.write(m);
  if (s < 10) buffer.write(0);
  buffer.write(s);
  return buffer.toString();
}

// Versión mejorada con función auxiliar
String hhmmss(int h, int m, int s) {
  var buffer = StringBuffer();

  void escribirConCero(int valor) {
    if (valor < 10) buffer.write(0);
    buffer.write(valor);
  }

  escribirConCero(h);
  buffer.write(':');
  escribirConCero(m);
  buffer.write(':');
  escribirConCero(s);

  return buffer.toString();
}

// Versión con parámetros nombrados y valores por defecto
String hhmmssNombrados({int h = 0, int m = 0, int s = 0}) {
  var buffer = StringBuffer();

  void escribirConCero(int valor) {
    if (valor < 10) buffer.write(0);
    buffer.write(valor);
  }

  escribirConCero(h);
  buffer.write(':');
  escribirConCero(m);
  buffer.write(':');
  escribirConCero(s);

  return buffer.toString();
}

void main() {
  print(hhmmss(1, 49, 11)); // 01:49:11
}
```

**Conceptos clave:**
- `StringBuffer` para construcción eficiente de cadenas
- Funciones auxiliares para evitar repetición de código
- Parámetros nombrados y valores por defecto
- Formateo de números con ceros a la izquierda

## 12. Números primos avanzados

**Ejercicio 12 - Operaciones con números primos**

**Concepto enseñado:**  
Algoritmos avanzados y optimización:

- Generación de primos con `while` (control preciso).    
- Identificación de primos gemelos (diferencia de 2).
- Listas de listas para estructuras complejas. 

**Foco:** Cómo manejar grandes conjuntos de datos eficientemente.

```dart
bool esPrimo(int n) {
  for (int d = 2; d * d <= n; d++) {
    if (n % d == 0) return false;
  }
  return n > 1;
}

// Muestra primos hasta llegar a N
void mostrarPrimos(int max) {
  for (int i = 0; i < max; i++) {
    if (esPrimo(i)) print(i);
  }
}

// Usando WHILE - Muestra los primeros n primos
List<int> listaNPrimos(int n) {
  List<int> primos = [];
  int i = 2;
  while (primos.length < n) {
    if (esPrimo(i)) primos.add(i);
    i++;
  }
  return primos;
}

// Muestra lista de primos usando for-in
void mostrarListaPrimos(int n) {
  for (var primo in listaNPrimos(n)) {
    print(primo);
  }
}

// Retorna lista de primos gemelos (diferencia de 2)
List<List<int>> parejasPrimos(int n) {
  var primos = listaNPrimos(n);
  List<List<int>> parejas = [];
  for (int i = 1; i < primos.length; i++) {
    if (primos[i] - primos[i - 1] == 2) {
      parejas.add([primos[i - 1], primos[i]]);
    }
  }
  return parejas;
}

void mostrarListaParejas(n) {
  for (var p in parejasPrimos(n)) {
    print('${p[0]} - ${p[1]}');
  }
}

void main() {
  // Ejemplos de uso:
  // print(esPrimo(6));
  // mostrarPrimos(100);
  // print(listaNPrimos(10));
  mostrarListaParejas(100);
}
```

**Conceptos clave:**
- Algoritmo eficiente para verificar primos (hasta √n)
- Uso de `while` para generación controlada
- Pares de primos gemelos (diferencia de 2)
- Compilación JIT y AOT en Dart (explicación en comentarios)

---

Todos los ejercicios enseñan a pensar en Dart como un lenguaje _multiparadigma_, combinando claridad para principiantes con herramientas avanzadas para problemas complejos. Se prioriza la legibilidad, eficiencia y uso adecuado de las estructuras del lenguaje.