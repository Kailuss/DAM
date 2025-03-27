---
number headings: _.1.1.
tags: [Focus, PMDM, Tarea]
obsidianUIMode: preview
banner: "![[pmdm.jpg]]"
banner_y: 0.42
cssclasses:
  - table-compact-clean
---

# **TEMA 1.3** <br> Programación Asíncrona <br>en Dart

## 1. Futures: Operaciones Asíncronas Básicas

Introduce el manejo de operaciones asíncronas mediante `Future`, mostrando cómo ejecutar tareas que toman tiempo sin bloquear el hilo principal.

```dart
import 'dart:async';

// Función para simular una operación de red
Future<String> fetchData(String url) {
  return Future.delayed(
    Duration(seconds: 2), 
    () => 'Datos recuperados de: $url'
  );
}

// Función con Future tipado con manejo de errores
Future<String> fetchDataWithValidation(String url) async {
  if (url.isEmpty) {
    throw ArgumentError('La URL no puede estar vacía');
  }
  
  return Future.delayed(
    Duration(seconds: 1), 
    () => url.toUpperCase()
  );
}

void main() {
  print('🚀 Iniciando operaciones asíncronas');

  // Método básico con .then()
  fetchData('https://ejemplo.com').then((resultado) {
    print('Resultado 1: $resultado');
  }).catchError((error) {
    print('Error en la solicitud: $error');
  });

  // Método con manipulación adicional
  fetchDataWithValidation('https://api.ejemplo.com')
    .then((datosModificados) {
      print('Resultado 2: $datosModificados');
    })
    .catchError((error) {
      print('Error en validación: $error');
    });

  print('⏳ Continuando con otras tareas');
}
```

|     |     |
| --- | --- |
| **Future.delayed**| Simula operaciones que tardan tiempo (como peticiones HTTP).|
| **.then()**| Maneja el resultado cuando la Future se completa.|
| **Async/await (implícito)**| La palabra `async` marca funciones asíncronas, pero aquí se usa `.then()` para mayor claridad.|

**Ejemplo de salida:**

```terminal
Inicio del programa
Fin del programa (no espera las Futures)
Petición a: https://ejemplo.com
Petición a: HTTPS://EJEMPLO.COM
```

## 2. Async/Await: Flujo Asíncrono Secuencial

Profundiza en el uso de `async/await` para escribir código asíncrono de forma secuencial y legible.

```dart
import 'dart:async';

// Simula una operación de obtención de usuario
Future<String> getUserProfile(String userId) async {
  await Future.delayed(Duration(seconds: 1));
  return 'Perfil de usuario: $userId';
}

// Simula una operación de obtención de datos adicionales
Future<String> getUserDetails(String userId) async {
  await Future.delayed(Duration(seconds: 1));
  return 'Detalles extra para usuario: $userId';
}

Future<void> fetchUserInformation(String userId) async {
  try {
    print('🔍 Iniciando búsqueda de información');
    
    // Recuperación secuencial de datos
    final perfil = await getUserProfile(userId);
    print(perfil);

    final detalles = await getUserDetails(userId);
    print(detalles);

    print('✅ Información completada');
  } catch (error) {
    print('❌ Error en recuperación: $error');
  }
}

void main() async {
  await fetchUserInformation('user123');
}
```

|     |     |
| --- | --- |
| **`async`** |Marca una función como asíncrona (retorna `Future<T>`).|
| **`await`** |Pausa la ejecución hasta que la `Future` se complete.|
| Ventaja |Código más legible que anidar `.then()`.|

**Ejemplo de salida:**

```terminal
Inicio
ID: 1
ID: 3
Fin
ID: 2
```

## 3. Comparativa: <br>Futures vs Async/Await

| Característica       | Futures con `.then()`        | Async/Await                  |
|----------------------|------------------------------|------------------------------|
| **Legibilidad**      | Menos legible (anidación)    | Similar a código síncrono    |
| **Flujo**            | Encadenamiento               | Secuencial                   |
| **Uso típico**       | Callbacks simples            | Lógica compleja              |
| **Ejemplo**         | `future.then((data) => ...)` | `var data = await future;`   |

```dart
import 'dart:async';

class DataService {
  // Método con Future tradicional
  Future<String> fetchDataWithThen(String endpoint) {
    return Future.delayed(
      Duration(seconds: 2), 
      () => 'Datos de $endpoint'
    ).then((data) => data.toUpperCase());
  }

  // Método equivalente con async/await
  Future<String> fetchDataWithAwait(String endpoint) async {
    await Future.delayed(Duration(seconds: 2));
    return 'Datos de ${endpoint.toUpperCase()}';
  }
}

void main() async {
  final service = DataService();

  // Demostración de ambos métodos
  service.fetchDataWithThen('api/usuarios')
    .then(print)
    .catchError((error) => print('Error: $error'));

  final resultadoAwait = await service.fetchDataWithAwait('api/productos');
  print(resultadoAwait);
}
```

## 3. Gestión de Errores

```dart
import 'dart:async';

class NetworkService {
  Future<String> fetchResource(String url) async {
    // Simulación de error aleatorio
    final randomDelay = Duration(seconds: 1 + DateTime.now().second % 3);
    
    return Future.delayed(randomDelay, () {
      if (url.contains('error')) {
        throw Exception('Fallo en la solicitud de red');
      }
      return 'Contenido de: $url';
    });
  }

  Future<void> processResources(List<String> urls) async {
    for (final url in urls) {
      try {
        final contenido = await fetchResource(url);
        print('✅ Procesado: $contenido');
      } catch (error) {
        print('❌ Error en $url: $error');
        // Continúa con el siguiente recurso
        continue;
      }
    }
  }
}

void main() async {
  final service = NetworkService();
  
  await service.processResources([
    'https://api.ejemplo.com/data1',
    'https://error.ejemplo.com',
    'https://api.ejemplo.com/data2'
  ]);
}
```

## 4. Errores Comunes en Programación Asíncrona y sus Soluciones

### 1. **Error de Tipo: Olvidar `await`**

**Problema Incorrecto:**

```dart
Future<String> getUserData(String userId) async {
  return 'Datos del usuario $userId';
}

void main() {
  // Error: userData es un Future<String>, no un String
  var userData = getUserData('user123');
  print(userData); // Imprime: Instance of 'Future<String>'
}
```

**Solución Correcta:**

```dart
void main() async {
  // Usar await para obtener el valor real
  var userData = await getUserData('user123');
  print(userData); // Imprime: Datos del usuario user123
}
```

### 2. **Error de Contexto: Falta de `async` en Función**

**Problema Incorrecto:**

```dart
// Función que intenta usar await sin ser async
void processData() {
  final result = await fetchData(); // Error de compilación
  print(result);
}
```

**Solución Correcta:**

```dart
// Añadir async y convertir a Future
Future<void> processData() async {
  final result = await fetchData(); // Correcto
  print(result);
}
```

### 3. **Error de Manejo: Ignorar Excepciones en Futures**

**Problema Incorrecto:**

```dart
Future<String> riskyOperation() async {
  // Operación que puede fallar
  throw Exception('Algo salió mal');
}

void main() {
  riskyOperation(); // Error no manejado
}
```

**Solución Correcta:**

```dart
void main() async {
  try {
    await riskyOperation(); // Manejo de excepción
  } catch (error) {
    print('Error capturado: $error');
  }
}
```

### 4. **Error de Concurrencia: Ejecución Secuencial Innecesaria**

**Problema Ineficiente:**

```dart
Future<void> fetchMultipleData() async {
  // Ejecución secuencial que ralentiza el proceso
  final data1 = await fetchFirstData();
  final data2 = await fetchSecondData();
  final data3 = await fetchThirdData();
}
```

**Solución Optimizada:**

```dart
Future<void> fetchMultipleData() async {
  // Ejecución concurrente con Future.wait
  final results = await Future.wait([
    fetchFirstData(),
    fetchSecondData(),
    fetchThirdData()
  ]);
}
```

### 5. **Error de Timeout: Operaciones de Larga Duración**

**Problema sin Control de Tiempo:**

```dart
Future<String> longRunningTask() async {
  // Tarea que podría colgar indefinidamente
  await Future.delayed(Duration(hours: 1));
  return 'Tarea completada';
}
```

**Solución con Timeout:**

```dart
Future<String> longRunningTask() async {
  try {
    return await Future.delayed(
      Duration(hours: 1), 
      () => 'Tarea completada'
    ).timeout(Duration(minutes: 5));
  } on TimeoutException catch (e) {
    print('Tarea excedió el tiempo límite');
    rethrow;
  }
}
```

### Consejos Generales de Prevención

1. **Siempre usar `async/await` juntos**
	
	- `async` en la declaración de función
	- `await` para esperar Futures
2. **Manejo Consistente de Errores**
	
	- Usar `try/catch` en operaciones asíncronas
	- No ignorar excepciones potenciales
3. **Considerar Concurrencia**
	
	- Usar `Future.wait()` para tareas independientes
	- Evitar bloqueos innecesarios
4. **Establecer Timeouts**
	
	- Controlar operaciones de larga duración
	- Prevenir cuelgues de aplicación

### Patrón Recomendado de Manejo Asíncrono

```dart
Future<void> ejemploManejoAsíncrono(String parametro) async {
  try {
    // Operaciones con timeout y manejo de errores
    final resultado = await operacionPrincipal(parametro)
      .timeout(
        Duration(seconds: 10), 
        onTimeout: () => manejarTimeout()
      );
    
    // Procesamiento del resultado
    print('Resultado: $resultado');
  } on TimeoutException {
    print('Operación excedió el tiempo límite');
  } catch (error) {
    print('Error inesperado: $error');
  } finally {
    // Limpieza o acciones finales
    limpiarRecursos();
  }
}
```

## 5. Conclusiones y Mejores Prácticas

- Usa `Future` para operaciones asíncronas simples
- Prefiere `async/await` para lógicas más complejas
- Siempre maneja posibles errores con `try/catch`
- Usa `await` únicamente dentro de funciones `async`
- Recuerda que el código asíncrono no bloquea la ejecución principal

**Consejos Adicionales:**

- Evita anidar múltiples `.then()` (callback hell)
- Utiliza `Future.wait()` para operaciones paralelas
- Considera timeout y cancelación en operaciones de red
