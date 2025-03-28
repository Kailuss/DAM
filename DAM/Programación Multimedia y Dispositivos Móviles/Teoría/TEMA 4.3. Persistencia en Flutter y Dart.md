---
tags: [DAM, PMDM]
cssclasses: [dam-pmdm, table-compact-clean]
banner: "![[pmdm.jpg]]"
banner_y: 0.42
---

# **TEMA 4.3.** <br>Persistencia en Flutter y Dart

## 1. Iniciar un proyecto y crear preferencias

Para gestionar la persistencia de datos en Flutter, se usa el paquete `shared_preferences`. Este permite almacenar pequeñas configuraciones de usuario de manera local, como el estado de un tema oscuro o la última página visitada. Es útil cuando se quiere mantener la configuración entre sesiones sin necesidad de una base de datos completa.

### 1.1. **Configuración inicial**

Para empezar, añade la dependencia en `pubspec.yaml`:

```yaml
dependencies:
  shared_preferences: ^2.0.13
```

### 1.2. **Creación de preferencias**

Para almacenar y recuperar datos, se usa la API de `shared_preferences`, que actúa como un almacenamiento clave-valor.

```dart
import 'package:shared_preferences/shared_preferences.dart';

class PreferenciasUsuario {
  static Future<void> guardarTema(bool esOscuro) async {
    try {
      final prefs = await SharedPreferences.getInstance();
      await prefs.setBool('darkMode', esOscuro);
    } catch (e) {
      print('Error al guardar preferencias: $e');
    }
  }

  static Future<bool> cargarTema() async {
    try {
      final prefs = await SharedPreferences.getInstance();
      return prefs.getBool('darkMode') ?? false;
    } catch (e) {
      print('Error al cargar preferencias: $e');
      return false; // Valor predeterminado en caso de error
    }
  }
}
```

### 1.3. **Tipos de datos soportados**

`shared_preferences` soporta varios tipos de datos básicos:

```dart
// Guardar diferentes tipos de datos
await prefs.setString('nombre', 'Usuario');
await prefs.setInt('edad', 25);
await prefs.setDouble('altura', 1.75);
await prefs.setStringList('favoritos', ['Flutter', 'Dart']);

// Recuperar datos
final nombre = prefs.getString('nombre') ?? 'Anónimo';
final edad = prefs.getInt('edad') ?? 0;
final altura = prefs.getDouble('altura') ?? 0.0;
final favoritos = prefs.getStringList('favoritos') ?? [];

// Eliminar preferencias
await prefs.remove('nombre');
await prefs.clear(); // Elimina todas las preferencias
```

### 1.4. **Patrón Singleton para preferencias**

Implementar un patrón Singleton para asegurar una única instancia de `PreferenciasUsuario`:

```dart
class PreferenciasUsuario {
  static final PreferenciasUsuario _instancia = PreferenciasUsuario._internal();
  
  factory PreferenciasUsuario() {
    return _instancia;
  }
  
  PreferenciasUsuario._internal();
  
  late SharedPreferences _prefs;
  
  Future<void> inicializar() async {
    _prefs = await SharedPreferences.getInstance();
  }
  
  // Métodos para acceder a las preferencias
  Future<void> guardarTema(bool esOscuro) async {
    try {
      await _prefs.setBool('darkMode', esOscuro);
    } catch (e) {
      print('Error al guardar tema: $e');
    }
  }
  
  bool obtenerTema() {
    return _prefs.getBool('darkMode') ?? false;
  }
}
```

## 2. Uso de preferencias

Las preferencias almacenadas pueden recuperarse y aplicarse en la interfaz de usuario para personalizar la experiencia del usuario. A continuación, se muestra cómo cargar el estado del tema antes de aplicar el diseño.

```dart
bool temaOscuro = await PreferenciasUsuario.cargarTema();
```

Se puede usar en `MaterialApp` para que el tema se ajuste automáticamente:

```dart
MaterialApp(
  themeMode: temaOscuro ? ThemeMode.dark : ThemeMode.light,
)
```

## 3. Creación de un Provider para gestionar el estado del Dark Mode

Para una mejor gestión del estado global en la aplicación, se recomienda utilizar el paquete `provider`. Este permite compartir el estado entre múltiples widgets sin necesidad de usar `setState` de forma local.

### 3.1. **Instalación del paquete**

En `pubspec.yaml`, añade la dependencia:

```yaml
dependencies:
  provider: ^6.0.0
```

### 3.2. **Implementación del Provider**

La siguiente clase `TemaProvider` gestiona el estado del tema y permite cambiarlo dinámicamente.

```dart
import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

class TemaProvider with ChangeNotifier {
  final PreferenciasUsuario _preferencias;
  bool _esOscuro = false;

  bool get esOscuro => _esOscuro;

  TemaProvider(this._preferencias) {
    _cargarTema();
  }

  void _cargarTema() async {
    _esOscuro = _preferencias.obtenerTema();
    notifyListeners();
  }

  void cambiarTema() async {
    _esOscuro = !_esOscuro;
    await _preferencias.guardarTema(_esOscuro);
    notifyListeners();
  }
  
  @override
  void dispose() {
    // Liberar recursos si es necesario
    super.dispose();
  }
}
```

### 3.3. **Inyección de dependencias**

Para inicializar correctamente los providers, se recomienda usar inyección de dependencias:

```dart
Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  
  final preferencias = PreferenciasUsuario();
  await preferencias.inicializar();
  
  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => TemaProvider(preferencias)),
        ChangeNotifierProvider(create: (_) => NavigationProvider()),
      ],
      child: MyApp(),
    ),
  );
}
```

### 3.4. **Uso en la aplicación**

Para integrarlo en la aplicación, se envuelve el `MaterialApp` con `ChangeNotifierProvider`.

```dart
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      themeMode: Provider.of<TemaProvider>(context).esOscuro 
          ? ThemeMode.dark 
          : ThemeMode.light,
      darkTheme: ThemeData.dark(),
      theme: ThemeData.light(),
      home: HomePage(),
    );
  }
}
```

## 4. Escaneo de QR

Flutter permite la lectura de códigos QR mediante bibliotecas como `qr_code_scanner`. Esto es útil para aplicaciones que requieren autenticación rápida o almacenamiento de información mediante códigos QR.

### 4.1. **Instalación del paquete**

```yaml
dependencies:
  qr_code_scanner: ^1.0.0
```

### 4.2. **Implementación de escaneo**

El siguiente código implementa una vista de escaneo de QR con gestión adecuada del ciclo de vida.

```dart
import 'package:flutter/material.dart';
import 'package:qr_code_scanner/qr_code_scanner.dart';

class QRScanPage extends StatefulWidget {
  @override
  _QRScanPageState createState() => _QRScanPageState();
}

class _QRScanPageState extends State<QRScanPage> {
  final GlobalKey qrKey = GlobalKey(debugLabel: 'QR');
  QRViewController? controller;
  String? resultado;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Escanear QR')),
      body: Column(
        children: [
          Expanded(
            flex: 5,
            child: QRView(
              key: qrKey,
              onQRViewCreated: _onQRViewCreated,
            ),
          ),
          Expanded(
            child: Center(child: Text(resultado ?? 'Escanea un código QR')),
          ),
        ],
      ),
    );
  }

  void _onQRViewCreated(QRViewController controller) {
    this.controller = controller;
    controller.scannedDataStream.listen((scanData) {
      setState(() {
        resultado = scanData.code;
      });
    });
  }

  @override
  void dispose() {
    controller?.dispose();
    super.dispose();
  }

  @override
  void reassemble() {
    super.reassemble();
    if (controller != null) {
      // Gestionar problemas específicos de la cámara en hot reload
      // En Android puede ser necesario pausar la cámara
      // En iOS puede ser necesario reanudarla
    }
  }
}
```

## 5. Provider para Bottom Navigation Bar

Para gestionar la navegación entre pantallas con `BottomNavigationBar`, es recomendable usar `provider` en lugar de `setState`.

### 5.1. **Implementación del Provider**

```dart
class NavigationProvider with ChangeNotifier {
  int _paginaActual = 0;
  
  int get paginaActual => _paginaActual;
  
  void cambiarPagina(int indice) {
    _paginaActual = indice;
    notifyListeners();
  }
  
  @override
  void dispose() {
    // Liberar recursos si es necesario
    super.dispose();
  }
}
```

### 5.2. **Uso en la aplicación**

```dart
bottomNavigationBar: BottomNavigationBar(
  currentIndex: context.watch<NavigationProvider>().paginaActual,
  onTap: (index) => context.read<NavigationProvider>().cambiarPagina(index),
  items: const [
    BottomNavigationBarItem(icon: Icon(Icons.home), label: 'Inicio'),
    BottomNavigationBarItem(icon: Icon(Icons.map), label: 'Mapa'),
  ],
),
```

## 6. Opciones adicionales de persistencia

Además de `shared_preferences`, Flutter ofrece varias alternativas para persistencia de datos:

### 6.1. **SQLite con sqflite**

Para almacenamiento estructurado de datos:

```yaml
dependencies:
  sqflite: ^2.0.0
  path: ^1.8.0
```

Ejemplo básico:

```dart
import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';

class DatabaseHelper {
  static final DatabaseHelper _instancia = DatabaseHelper._internal();
  static Database? _database;
  
  factory DatabaseHelper() {
    return _instancia;
  }
  
  DatabaseHelper._internal();
  
  Future<Database> get database async {
    if (_database != null) return _database!;
    _database = await _iniciarDB();
    return _database!;
  }
  
  Future<Database> _iniciarDB() async {
    String path = join(await getDatabasesPath(), 'mi_app.db');
    return await openDatabase(
      path,
      version: 1,
      onCreate: (Database db, int version) async {
        await db.execute(
          'CREATE TABLE usuarios(id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER)'
        );
      }
    );
  }
  
  // Métodos CRUD
  Future<int> insertarUsuario(Map<String, dynamic> usuario) async {
    Database db = await database;
    return await db.insert('usuarios', usuario);
  }
  
  Future<List<Map<String, dynamic>>> obtenerUsuarios() async {
    Database db = await database;
    return await db.query('usuarios');
  }
}
```

### 6.2. **Almacenamiento de archivos**

Para almacenar archivos más grandes:

```yaml
dependencies:
  path_provider: ^2.0.9
```

Ejemplo básico:

```dart
import 'dart:io';
import 'package:path_provider/path_provider.dart';

class FileStorage {
  Future<String> get _localPath async {
    final directory = await getApplicationDocumentsDirectory();
    return directory.path;
  }
  
  Future<File> get _localFile async {
    final path = await _localPath;
    return File('$path/datos.txt');
  }
  
  Future<File> escribirDatos(String datos) async {
    final file = await _localFile;
    return file.writeAsString(datos);
  }
  
  Future<String> leerDatos() async {
    try {
      final file = await _localFile;
      String contenido = await file.readAsString();
      return contenido;
    } catch (e) {
      return 'Error al leer el archivo';
    }
  }
}
```

### 6.3. **Almacenamiento seguro**

Para datos sensibles como credenciales:

```yaml
dependencies:
  flutter_secure_storage: ^6.0.0
```

Ejemplo básico:

```dart
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

class SecureStorage {
  final _storage = FlutterSecureStorage();
  
  Future<void> guardarCredenciales(String usuario, String password) async {
    await _storage.write(key: 'username', value: usuario);
    await _storage.write(key: 'password', value: password);
  }
  
  Future<Map<String, String>> obtenerCredenciales() async {
    String? username = await _storage.read(key: 'username');
    String? password = await _storage.read(key: 'password');
    return {
      'username': username ?? '',
      'password': password ?? ''
    };
  }
  
  Future<void> eliminarCredenciales() async {
    await _storage.delete(key: 'username');
    await _storage.delete(key: 'password');
  }
}
```