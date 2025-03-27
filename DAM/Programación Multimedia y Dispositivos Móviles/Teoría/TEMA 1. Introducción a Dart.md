---
number headings: max 2, _.1.1.
tags:
  - Focus
  - PMDM
  - Tarea
obsidianUIMode: preview
banner: "![[pmdm.jpg]]"
banner_y: 0.42
cssclasses:
  - table-compact-clean
---

# **TEMA 1.** <br> Introducción a Dart

## 1. Introducción 
1. **Estructura mínima de un programa.** Todo programa en Dart requiere una función `main()` como punto de entrada.  
2. **Comentarios.** Muestra cómo escribir comentarios de una línea (`//`) y multilínea (`/* ... */`), incluyendo anidación de estos últimos.  
3. **Salida básica.** Uso de `print()` para mostrar mensajes en la consola.  

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

## 2. Tipos de Datos en Dart

### 2.1. **Introducción a los Tipos Básicos**

|Tipo|Ejemplo|Descripción|
|---|---|---|
|`int`|`3`|Enteros|
|`double`|`0.05`|Decimales (no existe `float`)|
|`bool`|`true`/`false`|Valores booleanos|
|`String`|`'Hola'`|Cadenas de texto|
|`int?`|`null`|Entero anulable (null safety)|

```dart
void ejemploTiposDatos() {
  // Tipos básicos con nombres descriptivos
  int edad = 30;                  // Número entero
  double altura = 1.75;           // Número decimal
  bool esEstudiante = true;       // Valor booleano
  String nombre = 'María';        // Cadena de texto
  
  // Null safety
  int? telefono;                  // Puede ser nulo
  
  // Imprimir valores
  print('Nombre: $nombre');
  print('Edad: $edad');
  print('Altura: $altura metros');
  print('Estudiante: $esEstudiante');
}
```

> [!note] Nota
> - Todas las variables son objetos en Dart (incluso los tipos primitivos).  
> - Métodos útiles: `x.ceil()` (redondear arriba), `x.floor()` (redondear abajo). 

### 2.2. **Inferencia de Tipos y `dynamic`**

|Concepto|Ejemplo|Comportamiento|
|---|---|---|
|`var`|`var a = 7`|Infiere tipo (`int`)|
|`dynamic`|`dynamic c = 'texto'`|Tipo flexible (cambiable)|
|`num`|`num x = 5`|Superclase de `int` y `double`|

```dart
void ejemploInferenciaTipos() {
  // Inferencia con var
  var contador = 7;               // Inferido como int
  var mensaje = 'Hola';           // Inferido como String
  
  // dynamic permite cambiar tipo
  dynamic valorVariable = 'texto';
  valorVariable = 42;             // Ahora es un número
  
  // Tipo num como superclase
  num valorNumerico = 5;          // Puede ser int o double
  valorNumerico = 5.5;            // Cambio a double
}
```

> [!note] Nota
> Una vez inferido el tipo con `var`, no se puede cambiar (ej. `var a = 7` no puede ser `a = 7.0`).  

### 2.3. **Conversión de Tipos**

|Operación|Ejemplo|Resultado|
|---|---|---|
|Número → String|`5.toString()`|`"5"`|
|String → Número|`int.parse('123')`|`123` (int)|
|String → Decimal|`double.parse('3.14')`|`3.14` (double)|

```dart
void ejemploConversionTipos() {
  // Conversión de tipos
  String edadComoTexto = '25';
  int edadNumerica = int.parse(edadComoTexto);     // Texto a número
  
  double precioDecimal = double.parse('19.99');    // Texto a decimal
  
  String precioTexto = 45.toString();              // Número a texto
  
  print('Edad numérica: $edadNumerica');
  print('Precio decimal: $precioDecimal');
  print('Precio como texto: $precioTexto');
}
```

> [!note] Nota
> `parse` lanza una excepción si la cadena no es un número válido.  

### 2.4. **Interpolación y Cadenas**

|Sintaxis|Ejemplo|Resultado|
|---|---|---|
|`'$variable'`|`'Tengo $euros €'`|`"Tengo 45.7 €"`|
|`'${expresión}'`|`'Total: ${euros + 5} €'`|`"Total: 50.7 €"`|
|`"""`|`"""Línea 1\nLínea 2"""`|Texto multilínea|

```dart
void ejemploInterpolacion() {
  String nombre = 'Carlos';
  int edad = 35;
  double salario = 2500.50;
  
  // Interpolación simple y con expresiones
  String mensaje1 = 'Mi nombre es $nombre';
  String mensaje2 = 'Tengo ${edad + 1} años';
  String mensaje3 = 'Salario: ${salario * 1.1} €';
  
  print(mensaje1);
  print(mensaje2);
  print(mensaje3);
  
  // Cadenas multilínea
  String textoLargo = '''
    Línea 1
    Línea 2
    Nombre: $nombre
  ''';
  
  print(textoLargo);
}
```

### 2.5. **Colecciones: Listas, Sets y Maps**

#### 2.5.1. Listas

Las listas son colecciones ordenadas y modificables. Pueden contener elementos duplicados.

| Operación/Método       | Ejemplo                      | Descripción                                                                 | Resultado                     |
|------------------------|------------------------------|-----------------------------------------------------------------------------|-------------------------------|
| **Creación**           | `List<int> nums = [1, 2, 3];`| Crea una lista de enteros.                                                  | `[1, 2, 3]`                   |
| **Añadir elemento**    | `nums.add(4);`               | Añade un elemento al final.                                                 | `[1, 2, 3, 4]`                |
| **Eliminar elemento**  | `nums.remove(2);`            | Elimina la primera ocurrencia del valor `2`.                                | `[1, 3, 4]`                   |
| **Acceso por índice**  | `nums[0];`                   | Obtiene el primer elemento.                                                 | `1`                           |
| **Longitud**          | `nums.length;`               | Devuelve el número de elementos.                                            | `3`                           |
| **Condicionales**     | `[1, 2, if (nums.length > 2) 3];` | Añade `3` solo si la lista `nums` tiene más de 2 elementos.           | `[1, 2, 3]` (si `nums.length > 2`) |
| **Generación dinámica**| `[for (int i = 0; i < 3; i++) i];` | Genera una lista `[0, 1, 2]` usando un bucle `for`.                  | `[0, 1, 2]`                   |
| **`addAll()`**       | `nums.addAll([4, 5]);`       | Añade múltiples elementos.                                                  | `[1, 2, 3, 4, 5]`             |
| **`insert()`**       | `nums.insert(1, 10);`        | Inserta `10` en la posición `1`.                                            | `[1, 10, 2, 3]`               |
| **`removeAt()`**         | `nums.removeAt(0);`          | Elimina el elemento en la posición `0`.                                     | `[2, 3]`                       |
| **`shuffle()`**           | `nums.shuffle();`            | Mezcla la lista aleatoriamente.                                             | Ej: `[3, 1, 2]`                |

*) Los maps preservan el orden de inserción en versiones recientes de Dart.

```dart
void ejemploListas() {
  // Creación y manipulación de listas
  List<String> frutas = ['manzana', 'plátano', 'naranja'];
  
  // Añadir elementos
  frutas.add('uva');
  frutas.addAll(['kiwi', 'pera']);
  
  // Operaciones
  print('Primera fruta: ${frutas[0]}');
  print('Número de frutas: ${frutas.length}');
  
  // Lista dinámica con condiciones
  bool tieneFrutasTropicales = true;
  var listaFrutas = [
    'manzana',
    'pera',
    if (tieneFrutasTropicales) 'mango',
    for (var i = 1; i <= 3; i++) 'fruta$i'
  ];
  
  print('Lista dinámica: $listaFrutas');
}
```

---

#### 2.5.2. Sets

Los sets son colecciones no ordenadas de elementos únicos.

| Operación/Método       | Ejemplo                      | Descripción                                                                 | Resultado                     |
|------------------------|------------------------------|-----------------------------------------------------------------------------|-------------------------------|
| **Creación**           | `Set<int> conjunto = {1, 2};`| Crea un set de enteros.                                                     | `{1, 2}`                      |
| **Añadir elemento**    | `conjunto.add(3);`           | Añade `3` al set.                                                           | `{1, 2, 3}`                   |
| **Eliminar elemento**  | `conjunto.remove(1);`        | Elimina el valor `1`.                                                       | `{2, 3}`                       |
| **Contiene elemento**  | `conjunto.contains(2);`      | Verifica si el set contiene `2`.                                            | `true`                         |
| **Unión de sets**      | `conjunto.union({3, 4});`    | Combina dos sets, eliminando duplicados.                                    | `{1, 2, 3, 4}`                 |
| **Intersección**       | `conjunto.intersection({2, 3});` | Devuelve elementos comunes.                                             | `{2, 3}`                       |

```dart
void ejemploSets() {
  // Creación y operaciones con sets
  Set<String> coloresPrimarios = {'rojo', 'azul', 'amarillo'};
  
  // Añadir elementos
  coloresPrimarios.add('verde');
  
  // Operaciones de conjuntos
  Set<String> coloresSecundarios = {'verde', 'naranja', 'violeta'};
  
  var unionColores = coloresPrimarios.union(coloresSecundarios);
  var interseccionColores = coloresPrimarios.intersection(coloresSecundarios);
  
  print('Unión de colores: $unionColores');
  print('Intersección de colores: $interseccionColores');
}
```

---

#### 2.5.3. Maps

Los maps son colecciones clave-valor, ideales para representar datos estructurados.

| Operación/Método       | Ejemplo                      | Descripción                                                                 | Resultado                     |
|------------------------|------------------------------|-----------------------------------------------------------------------------|-------------------------------|
| **Creación**           | `Map<String, int> edades = {'Ana': 25, 'Juan': 30};` | Crea un map con claves `String` y valores `int`.       | `{'Ana': 25, 'Juan': 30}`     |
| **Añadir entrada**     | `edades['Luisa'] = 28;`      | Añade una nueva clave-valor.                                                | `{'Ana': 25, 'Juan': 30, 'Luisa': 28}` |
| **Eliminar entrada**   | `edades.remove('Juan');`     | Elimina la entrada con clave `'Juan'`.                                      | `{'Ana': 25, 'Luisa': 28}`     |
| **Verificar clave**    | `edades.containsKey('Ana');` | Comprueba si existe la clave `'Ana'`.                                       | `true`                         |
| **Recorrer map**       | `edades.forEach((k, v) => print('$k: $v'));` | Itera sobre cada entrada.                                   | Imprime `Ana: 25`, `Luisa: 28` |
| **Métodos útiles:**    |                              |                                                                             |                               |
| `keys`                | `edades.keys;`               | Devuelve todas las claves.                                                  | `['Ana', 'Luisa']`             |
| `values`              | `edades.values;`             | Devuelve todos los valores.                                                 | `[25, 28]`                     |

```dart
void ejemploMaps() {
  // Creación y manipulación de maps
  Map<String, int> edadesPersonas = {
    'María': 28,
    'Juan': 35,
    'Ana': 22
  };
  
  // Añadir y modificar elementos
  edadesPersonas['Carlos'] = 40;
  edadesPersonas.remove('Juan');
  
  // Recorrer map
  edadesPersonas.forEach((nombre, edad) {
    print('$nombre tiene $edad años');
  });
  
  // Map dinámico
  var llaves = ['nombre', 'edad', 'ciudad'];
  var valores = ['Elena', 33, 'Madrid'];
  
  var personaMap = {
    for (var i = 0; i < llaves.length; i++)
      llaves[i]: valores[i]
  };
  
  print('Persona: $personaMap');
}
```

---

#### 2.5.4. Resumen de Colecciones

| Tipo      | Orden | Elementos Únicos | Uso Principal               | Ejemplo Típico               |
|-----------|-------|------------------|-----------------------------|-------------------------------|
| **Lista** | Sí    | No               | Secuencias ordenadas        | `[1, 2, 3]`                   |
| **Set**   | No    | Sí               | Eliminar duplicados         | `{1, 2, 3}`                    |
| **Map**   | No*   | Claves únicas    | Estructuras clave-valor     | `{'nombre': 'Ana', 'edad': 25}`|

### 2.6. **Condiciones y Booleanos**

```dart
void ejemploCondicionesBooleanos() {
  // Declaración de variables booleanas
  bool esEstudiante = true;
  bool tieneBeca = false;

  // Condicional simple
  if (esEstudiante) {
    print('Es estudiante');
  }

  // Condicional con else
  if (tieneBeca) {
    print('Tiene beca');
  } else {
    print('No tiene beca');
  }

  // Condiciones compuestas con operadores lógicos
  bool mayorDeEdad = true;
  int edad = 20;

  if (mayorDeEdad && edad >= 18) {
    print('Es mayor de edad');
  }

  // Operador ternario
  String estado = esEstudiante ? 'Estudiando' : 'No estudia';
  print('Estado: $estado');

  // Evaluación de cadenas vacías
  String nombre = '';
  if (nombre.isEmpty) {
    print('El nombre está vacío');
  }

  // Comparación de booleanos
  bool estaActivo = true;
  bool puedeAcceder = esEstudiante && estaActivo;

  if (puedeAcceder) {
    print('Puede acceder al sistema');
  }

  // Negación de booleanos
  bool tieneDeuda = false;
  if (!tieneDeuda) {
    print('No tiene deudas pendientes');
  }
}
```

### 2.7. **Runes y Emojis**

|Sintaxis|Ejemplo|Resultado|
|---|---|---|
|`\u{código}`|`'\u{1F697}'`|🚗|
|Clase `Runes`|`Runes('\u{1F680}')`|🚀 (como objeto)|

```dart
void ejemploRunes() {
  // Uso de runes y emojis
  var coche = '\u{1F697}';          // 🚗
  var cohete = Runes('\u{1F680}');  // 🚀
  
  print('Coche: $coche');
  print('Cohete: ${String.fromCharCodes(cohete)}');
}
```

### 2.8. **Resumen**
- **Tipos básicos:** `int`, `double`, `bool`, `String`, y null safety (`?`).  
- **Flexibilidad:** `var` (inferencia), `dynamic` (tipado dinámico), `num` (número genérico).  
- **Colecciones:**  
  - Listas (ordenadas, repetibles).  
  - Sets (únicos, no ordenados).  
  - Maps (clave-valor).  
- **Strings:** Interpolación, multilínea, y conversiones.  
- **Seguridad:** Condiciones solo con `bool`, manejo explícito de tipos. 
