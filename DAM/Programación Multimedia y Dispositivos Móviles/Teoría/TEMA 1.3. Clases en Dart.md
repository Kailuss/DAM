---
number headings: max 3, _.1.1., skip ^sk
tags: [DAM, PMDM]
banner: "![[pmdm.jpg]]"
banner_y: 0.42
cssclasses: [dam-pmdm, table-compact-clean]
---

# **TEMA 1.2** <br>Clases en Dart

## 1. Clases Básicas
|Concepto|Sintaxis|Ejemplo|Descripción|
|---|---|---|---|
|**Declaración**|`class NombreClase { ... }`|`class Persona { ... }`|Define la estructura de un objeto|
|**Constructor básico**|`Clase(this.param1, this.param2)`|`Persona(this.nom, this.cognoms)`|Inicializa atributos directamente|
|**Constructor nombrado**|`Clase.nombreConstructor()`|`PersonaAmbEdat.senseEdat()`|Permite múltiples formas de crear instancias|
|**Null safety**|`late Tipo variable`|`late String nom`|Variable no-nula con inicialización diferida|
|**Métodos**|`tipoRetorno nombre() { ... }`|`void esMajor() { ... }`|Acciones que puede realizar la clase|

```dart
class Persona {
  // Propiedades
  String nombre;
  int edad;
  
  // Constructor básico
  Persona(this.nombre, this.edad);

  // Constructor con parámetros nombrados y opcionales
  Persona.conEdadPredeterminada({
    required this.nombre, 
    this.edad = 0
  });

  // Método personalizado
  void presentarse() {
    print('Hola, soy $nombre y tengo $edad años');
  }

  // Sobrescribir método toString
  @override
  String toString() => 'Persona(nombre: $nombre, edad: $edad)';
}

void ejemploPersona() {
  var persona1 = Persona('Carlos', 35);
  persona1.presentarse();

  var persona2 = Persona.conEdadPredeterminada(nombre: 'María');
  print(persona2);
}
```

|Métodos útiles| | 
|-|-|
|`toString()`|Personalizar la representación en string.|
|`esMajor()`|Comparar objetos basados en atributos.|  

## 2. Herencia y Polimorfismo
|Concepto|Sintaxis|Ejemplo|Descripción|
|---|---|---|---|
|**Clase abstracta**|`abstract class Nombre { ... }`|`abstract class Animal { ... }`|No se puede instanciar, solo heredar|
|**Herencia**|`class Hijo extends Padre`|`class Heroi extends Personatge`|Extiende funcionalidad|
|**Polimorfismo**|`@override`|`@override void emetreSo()`|Redefine métodos de la clase padre|
|**Constructor con `super`**|`Hijo() : super(param)`|`Heroi(String nom) : super(nom)`|Llama al constructor padre|

```dart
// Clase abstracta base
abstract class Figura {
  double calcularArea();
  
  void describir() {
    print('Área: ${calcularArea()}');
  }
}

// Clases que heredan de Figura
class Circulo extends Figura {
  double radio;

  Circulo(this.radio);

  @override
  double calcularArea() => 3.14 * radio * radio;
}

class Rectangulo extends Figura {
  double base;
  double altura;

  Rectangulo(this.base, this.altura);

  @override
  double calcularArea() => base * altura;
}

void ejemploHerencia() {
  List<Figura> figuras = [
    Circulo(5),
    Rectangulo(4, 6)
  ];

  for (var figura in figuras) {
    figura.describir();
  }
}
```

## 3. Mixins
|Concepto|Sintaxis|Ejemplo|Descripción|
|---|---|---|---|
|**Definición**|`mixin Nombre { ... }`|`mixin Volar { void volar() }`|Agrupa comportamientos|
|**Uso**|`class Clase with Mixin1, Mixin2`|`class Delfi with Nadar`|Añade capacidades a clases|
|**Restricciones**|No puede usar `super`|-|Limitaciones en acceso a herencia|

```dart
// Mixins para agregar funcionalidades
mixin Volador {
  void volar() {
    print('Estoy volando');
  }
}

mixin Nadador {
  void nadar() {
    print('Estoy nadando');
  }
}

// Clase que usa mixins
class Pato extends Ave with Volador, Nadador {
  void hacerSonido() {
    print('¡Cuac!');
  }
}

void ejemploMixins() {
  var miPato = Pato();
  miPato.volar();
  miPato.nadar();
  miPato.hacerSonido();
}
```

> [!note] Regla
> Los mixins no pueden tener constructores. 

---
**Herencia vs. Interfaces**

|Característica|Herencia (`extends`)|Mixins (`with`)|
|---|---|---|
|**Reutilización**|Jerarquía única|Múltiple|
|**Constructor**|Requiere `super`|No permitido|
|**Uso típico**|"Es un" (relación)|"Puede" (capacidad)|

## 4. Getters y Setters

|Concepto|Sintaxis|Ejemplo|Descripción|
|---|---|---|---|
|**Getter**|`Tipo get nombre { ... }`|`double get area => _costat * _costat`|Acceso controlado a atributos|
|**Setter**|`set nombre(valor) { ... }`|`set area(double a) => _costat = sqrt(a)`|Validación/modificación al asignar|
|**Atributo privado**|`_nombre`|`double _costat`|Solo accesible dentro de la clase|

```dart
class Rectangulo {
  // Propiedades privadas
  double _base;
  double _altura;

  // Constructor
  Rectangulo(this._base, this._altura);

  // Getters
  double get area => _base * _altura;
  double get base => _base;
  double get altura => _altura;

  // Setters con validación
  set base(double valor) {
    if (valor > 0) {
      _base = valor;
    } else {
      throw ArgumentError('La base debe ser positiva');
    }
  }

  // Método de ejemplo
  void escalarForma(double factor) {
    _base *= factor;
    _altura *= factor;
  }
}

void ejemploGettersSetter() {
  var rectangulo = Rectangulo(5, 3);
  print('Área inicial: ${rectangulo.area}');
  
  rectangulo.base = 10;
  print('Nueva área: ${rectangulo.area}');
}
```

## 5. Métodos y Propiedades Estáticas

| Concepto | |
| - | - |
| **Propiedades estáticas**|`static final Color vermell = Color(255, 0, 0)`. | 
| **Métodos estáticos**|`static Color mescla(Color a, Color b)`. |
| **No requieren instancia**|Se accede directamente desde la clase. |

```dart
class Calculadora {
  // Propiedad estática
  static const double pi = 3.14159;

  // Método estático
  static double calcularAreaCirculo(double radio) {
    return pi * radio * radio;
  }

  // Método estático de utilidad
  static int sumar(int a, int b) => a + b;
}

void ejemploEstaticos() {
  print('Área de círculo: ${Calculadora.calcularAreaCirculo(5)}');
  print('Suma: ${Calculadora.sumar(10, 20)}');
}

void main() {
  ejemploPersona();
  ejemploHerencia();
  ejemploMixins();
  ejemploGettersSetter();
  ejemploEstaticos();
}
```


## 6. Resumen

| Concepto               | Ejemplo                      | Descripción                              |
|------------------------|------------------------------|------------------------------------------|
| **Clases básicas**     | `Persona(this.nom)`          | Constructores y atributos.               |
| **Herencia**           | `class Heroi extends Personatge` | Extiende funcionalidad.              |
| **Mixins**             | `with Volar, Nadar`          | Reutiliza código sin herencia.           |
| **Getters/Setters**    | `get area => _costat * _costat` | Controla acceso a atributos.         |
| **Miembros estáticos** | `static Color vermell`       | Pertenece a la clase, no a instancias.   |
| **Polimorfismo**       | `@override emetreSo()`       | Múltiples comportamientos para un método.|

```dart
// Clase base
abstract class Animal {
  void ferSo();
}
// Mixin
mixin Volar { void volar() => print('Volant'); }
// Subclase con mixin
class Ocelle extends Animal with Volar {
  @override
  void ferSo() => print('Xiulet');
}
```
