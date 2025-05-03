## Understanding the Requirements

This exam asks you to create a Flutter application with the following features:

1. Login system with local credential storage
2. Home screen with a list of dishes from Firebase
3. Detail view for each dish
4. Map functionality to show restaurant location

Let's start by creating the project structure and implementing each component one by one.

## Project Creation

First, let's create a new Flutter project called `examen_final_primerllintage`:

```
flutter create examen_final_primerllintage
cd examen_final_primerllintage
```

Now let's implement the required functionality step by step.

## Exercise 1: Login System

For the login system, we'll need:

- Shared preferences to store credentials locally
- Authentication logic
- Redirection based on login status

Let's start with the dependencies needed in our `pubspec.yaml`:

```yaml
name: examen_final_primerllintage
description: "Examen Final Flutter"
publish_to: 'none'
version: 1.0.0+1

environment:
  sdk: '>=3.0.0 <4.0.0'

dependencies:
  flutter:
    sdk: flutter
  cupertino_icons: ^1.0.2
  shared_preferences: ^2.2.0
  http: ^1.1.0
  firebase_core: ^2.15.1
  firebase_database: ^10.2.5
  google_maps_flutter: ^2.5.0

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^2.0.0

flutter:
  uses-material-design: true
  assets:
    - assets/images/

```

Now let's create the main file structure:

```dart
import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'screens/login_screen.dart';
import 'screens/home_screen.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  
  // Initialize Firebase
  await Firebase.initializeApp(
    options: const FirebaseOptions(
      apiKey: "AIzaSyDQjM2d1wZNUq4JpfAUKJtlCPFuM5FrBJQ",
      authDomain: "examen-practic-sim.firebaseapp.com",
      databaseURL: "https://examen-practic-sim-default-rtdb.europe-west1.firebasedatabase.app",
      projectId: "examen-practic-sim",
      storageBucket: "examen-practic-sim.appspot.com",
      messagingSenderId: "443262985841",
      appId: "1:443262985841:web:a18f5f6c3fafc83b9d33e0"
    ),
  );
  
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Examen Final',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const AuthenticationWrapper(),
    );
  }
}

// Stateful widget to check authentication status
class AuthenticationWrapper extends StatefulWidget {
  const AuthenticationWrapper({super.key});

  @override
  State<AuthenticationWrapper> createState() => _AuthenticationWrapperState();
}

class _AuthenticationWrapperState extends State<AuthenticationWrapper> {
  bool _isLoading = true;
  bool _isAuthenticated = false;

  @override
  void initState() {
    super.initState();
    _checkAuthStatus();
  }

  // Check if user is authenticated
  Future<void> _checkAuthStatus() async {
    final prefs = await SharedPreferences.getInstance();
    // Check if user credentials are stored
    final username = prefs.getString('username');
    final password = prefs.getString('password');
    
    setState(() {
      _isAuthenticated = username != null && password != null;
      _isLoading = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    if (_isLoading) {
      // Show loading spinner while checking authentication
      return const Scaffold(
        body: Center(
          child: CircularProgressIndicator(),
        ),
      );
    } else {
      // Return appropriate screen based on authentication status
      return _isAuthenticated ? const HomeScreen() : const LoginScreen();
    }
  }
}

```

Now let's create the login screen:

```dart
import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'home_screen.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  // Controllers for text fields
  final _usernameController = TextEditingController();
  final _passwordController = TextEditingController();
  
  // Form key for validation
  final _formKey = GlobalKey<FormState>();
  
  // Login state
  bool _isLoading = false;
  String _errorMessage = '';

  @override
  void dispose() {
    // Clean up controllers when widget is disposed
    _usernameController.dispose();
    _passwordController.dispose();
    super.dispose();
  }

  // Login function
  Future<void> _login() async {
    // Validate form
    if (!_formKey.currentState!.validate()) return;
    
    setState(() {
      _isLoading = true;
      _errorMessage = '';
    });
    
    try {
      // Perform login - In a real app this would check against a server
      // For this exam, we'll just store credentials locally
      final username = _usernameController.text.trim();
      final password = _passwordController.text.trim();
      
      // Simple validation - not empty fields
      if (username.isEmpty || password.isEmpty) {
        setState(() {
          _errorMessage = 'Por favor, introduce usuario y contraseña.';
          _isLoading = false;
        });
        return;
      }
      
      // For the exam purposes, we'll accept any non-empty credentials
      // In a real application, you would verify these against a database
      
      // Store credentials locally
      final prefs = await SharedPreferences.getInstance();
      await prefs.setString('username', username);
      await prefs.setString('password', password);
      
      // Navigate to home screen
      if (!mounted) return;
      Navigator.of(context).pushReplacement(
        MaterialPageRoute(builder: (context) => const HomeScreen()),
      );
    } catch (e) {
      setState(() {
        _errorMessage = 'Error al iniciar sesión. Inténtalo de nuevo.';
        _isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    // Using a StatefulWidget because we need to manage the login state
    return Scaffold(
      appBar: AppBar(
        title: const Text('Iniciar Sesión'),
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              // Username field
              TextFormField(
                controller: _usernameController,
                decoration: const InputDecoration(
                  labelText: 'Usuario',
                  border: OutlineInputBorder(),
                ),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Por favor, introduce un usuario';
                  }
                  return null;
                },
              ),
              const SizedBox(height: 16),
              
              // Password field
              TextFormField(
                controller: _passwordController,
                decoration: const InputDecoration(
                  labelText: 'Contraseña',
                  border: OutlineInputBorder(),
                ),
                obscureText: true,
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Por favor, introduce una contraseña';
                  }
                  return null;
                },
              ),
              const SizedBox(height: 16),
              
              // Error message
              if (_errorMessage.isNotEmpty)
                Padding(
                  padding: const EdgeInsets.only(bottom: 16),
                  child: Text(
                    _errorMessage,
                    style: const TextStyle(color: Colors.red),
                  ),
                ),
              
              // Login button
              ElevatedButton(
                onPressed: _isLoading ? null : _login,
                child: _isLoading
                    ? const SizedBox(
                        width: 20,
                        height: 20,
                        child: CircularProgressIndicator(strokeWidth: 2),
                      )
                    : const Text('Iniciar Sesión'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

```

Now let's implement the home screen which will show the list of dishes:

```dart
import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:firebase_database/firebase_database.dart';
import '../models/plat.dart';
import 'login_screen.dart';
import 'plat_detail_screen.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  // List to store plats
  List<Plat> _plats = [];
  bool _isLoading = true;
  String _errorMessage = '';

  @override
  void initState() {
    super.initState();
    _loadPlats();
  }

  // Load plats from Firebase
  Future<void> _loadPlats() async {
    setState(() {
      _isLoading = true;
      _errorMessage = '';
    });

    try {
      // Get reference to the database
      final ref = FirebaseDatabase.instance.ref();
      // Get snapshot of plats
      final snapshot = await ref.child('plats').get();

      if (snapshot.exists) {
        // Convert the data to a list of Plat objects
        final plats = <Plat>[];
        final data = snapshot.value as Map<dynamic, dynamic>;
        
        data.forEach((key, value) {
          final platData = Map<String, dynamic>.from(value as Map);
          platData['id'] = key;
          plats.add(Plat.fromJson(platData));
        });

        setState(() {
          _plats = plats;
          _isLoading = false;
        });
      } else {
        setState(() {
          _errorMessage = 'No hay platos disponibles';
          _isLoading = false;
        });
      }
    } catch (e) {
      setState(() {
        _errorMessage = 'Error al cargar los platos: $e';
        _isLoading = false;
      });
    }
  }

  // Logout function
  Future<void> _logout() async {
    // Show confirmation dialog
    final confirmed = await showDialog<bool>(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Cerrar sesión'),
        content: const Text('¿Estás seguro de que quieres cerrar sesión?'),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(context).pop(false),
            child: const Text('Cancelar'),
          ),
          ElevatedButton(
            onPressed: () => Navigator.of(context).pop(true),
            child: const Text('Cerrar sesión'),
          ),
        ],
      ),
    );

    if (confirmed == true) {
      // Remove stored credentials
      final prefs = await SharedPreferences.getInstance();
      await prefs.remove('username');
      await prefs.remove('password');

      // Navigate back to login screen
      if (!mounted) return;
      Navigator.of(context).pushReplacement(
        MaterialPageRoute(builder: (context) => const LoginScreen()),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    // Using a StatefulWidget because we load data from Firebase
    return Scaffold(
      appBar: AppBar(
        title: const Text('Menú de Platos'),
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        actions: [
          // Logout button
          IconButton(
            icon: const Icon(Icons.logout),
            onPressed: _logout,
            tooltip: 'Cerrar sesión',
          ),
        ],
      ),
      body: _isLoading
          ? const Center(child: CircularProgressIndicator())
          : _errorMessage.isNotEmpty
              ? Center(child: Text(_errorMessage))
              : _plats.isEmpty
                  ? const Center(child: Text('No hay platos disponibles'))
                  : RefreshIndicator(
                      onRefresh: _loadPlats,
                      child: ListView.builder(
                        itemCount: _plats.length,
                        itemBuilder: (context, index) {
                          final plat = _plats[index];
                          return GestureDetector(
                            onTap: () {
                              // Navigate to detail screen when tapped
                              Navigator.of(context).push(
                                MaterialPageRoute(
                                  builder: (context) => PlatDetailScreen(plat: plat),
                                ),
                              );
                            },
                            child: Card(
                              margin: const EdgeInsets.symmetric(
                                horizontal: 16.0,
                                vertical: 8.0,
                              ),
                              child: ListTile(
                                // Title with plat name
                                title: Text(
                                  plat.nom,
                                  style: const TextStyle(fontWeight: FontWeight.bold),
                                ),
                                // Image on the right
                                trailing: SizedBox(
                                  width: 80,
                                  height: 80,
                                  child: plat.foto != null
                                      ? Image.network(
                                          plat.foto!,
                                          fit: BoxFit.cover,
                                          errorBuilder: (context, error, stackTrace) {
                                            // Show default image on error
                                            return Image.asset(
                                              'assets/images/default_food.png',
                                              fit: BoxFit.cover,
                                            );
                                          },
                                        )
                                      : Image.asset(
                                          'assets/images/default_food.png',
                                          fit: BoxFit.cover,
                                        ),
                                ),
                              ),
                            ),
                          );
                        },
                      ),
                    ),
    );
  }
}

```

Next, let's create the Plat model:

```dart
class Plat {
  final String id;
  final String nom;
  final String descripcio;
  final String tipus;
  final bool disponible;
  final String restaurant;
  final String geo;
  final String? foto;

  Plat({
    required this.id,
    required this.nom,
    required this.descripcio,
    required this.tipus,
    required this.disponible,
    required this.restaurant,
    required this.geo,
    this.foto,
  });

  // Factory constructor to create a Plat from JSON
  factory Plat.fromJson(Map<String, dynamic> json) {
    return Plat(
      id: json['id'] ?? '',
      nom: json['nom'] ?? '',
      descripcio: json['descripcio'] ?? '',
      tipus: json['tipus'] ?? '',
      disponible: json['disponible'] ?? false,
      restaurant: json['restaurant'] ?? '',
      geo: json['geo'] ?? '0,0',
      foto: json['foto'],
    );
  }

  // Convert Plat to a Map for Firebase
  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'nom': nom,
      'descripcio': descripcio,
      'tipus': tipus,
      'disponible': disponible,
      'restaurant': restaurant,
      'geo': geo,
      'foto': foto,
    };
  }

  // Get latitude and longitude from geo string
  List<double> get geoCoordinates {
    final parts = geo.split(',');
    if (parts.length == 2) {
      try {
        final lat = double.parse(parts[0]);
        final lng = double.parse(parts[1]);
        return [lat, lng];
      } catch (e) {
        // Return default coordinates if parsing fails
        return [0.0, 0.0];
      }
    }
    return [0.0, 0.0];
  }
}

```

Now let's create the detail screen for each dish:

```dart
import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import '../models/plat.dart';
import 'map_screen.dart';

class PlatDetailScreen extends StatelessWidget {
  final Plat plat;

  const PlatDetailScreen({super.key, required this.plat});

  @override
  Widget build(BuildContext context) {
    // Using a StatelessWidget because the detail view doesn't change state
    return Scaffold(
      appBar: AppBar(
        title: Text(plat.nom),
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Image
              Center(
                child: Container(
                  height: 200,
                  width: double.infinity,
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(12),
                  ),
                  child: ClipRRect(
                    borderRadius: BorderRadius.circular(12),
                    child: plat.foto != null
                        ? Image.network(
                            plat.foto!,
                            fit: BoxFit.cover,
                            errorBuilder: (context, error, stackTrace) {
                              return Image.asset(
                                'assets/images/default_food.png',
                                fit: BoxFit.cover,
                              );
                            },
                          )
                        : Image.asset(
                            'assets/images/default_food.png',
                            fit: BoxFit.cover,
                          ),
                  ),
                ),
              ),
              const SizedBox(height: 24),
              
              // Name
              Text(
                plat.nom,
                style: Theme.of(context).textTheme.headlineMedium?.copyWith(
                      fontWeight: FontWeight.bold,
                    ),
              ),
              const SizedBox(height: 8),
              
              // Disponible
              Row(
                children: [
                  const Text(
                    'Disponible: ',
                    style: TextStyle(fontWeight: FontWeight.bold),
                  ),
                  Switch(
                    value: plat.disponible,
                    onChanged: null, // Read-only switch
                    activeColor: Colors.green,
                  ),
                ],
              ),
              const SizedBox(height: 16),
              
              // Descripción
              const Text(
                'Descripción:',
                style: TextStyle(fontWeight: FontWeight.bold, fontSize: 18),
              ),
              const SizedBox(height: 4),
              Text(plat.descripcio),
              const SizedBox(height: 16),
              
              // Tipo
              const Text(
                'Tipo:',
                style: TextStyle(fontWeight: FontWeight.bold, fontSize: 18),
              ),
              const SizedBox(height: 4),
              Text(plat.tipus),
              const SizedBox(height: 16),
              
              // Restaurant
              const Text(
                'Restaurante:',
                style: TextStyle(fontWeight: FontWeight.bold, fontSize: 18),
              ),
              const SizedBox(height: 4),
              Text(plat.restaurant),
              const SizedBox(height: 16),
              
              // Geo
              const Text(
                'Ubicación:',
                style: TextStyle(fontWeight: FontWeight.bold, fontSize: 18),
              ),
              const SizedBox(height: 4),
              Text(plat.geo),
              const SizedBox(height: 24),
              
              // Button to view on map
              SizedBox(
                width: double.infinity,
                child: ElevatedButton.icon(
                  onPressed: () {
                    // Navigate to map screen
                    Navigator.of(context).push(
                      MaterialPageRoute(
                        builder: (context) => MapScreen(plat: plat),
                      ),
                    );
                  },
                  icon: const Icon(Icons.location_on),
                  label: const Text('Ver en el mapa'),
                  style: ElevatedButton.styleFrom(
                    padding: const EdgeInsets.symmetric(vertical: 12),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

```

Finally, let's implement the map screen to show the restaurant location:

```dart
import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import '../models/plat.dart';

class MapScreen extends StatefulWidget {
  final Plat plat;

  const MapScreen({super.key, required this.plat});

  @override
  State<MapScreen> createState() => _MapScreenState();
}

class _MapScreenState extends State<MapScreen> {
  late GoogleMapController _mapController;
  late LatLng _restaurantLocation;
  late Set<Marker> _markers;

  @override
  void initState() {
    super.initState();
    
    // Get coordinates from plat
    final coordinates = widget.plat.geoCoordinates;
    _restaurantLocation = LatLng(coordinates[0], coordinates[1]);
    
    // Set up markers
    _markers = {
      Marker(
        markerId: MarkerId(widget.plat.id),
        position: _restaurantLocation,
        infoWindow: InfoWindow(
          title: widget.plat.restaurant,
          snippet: widget.plat.nom,
        ),
      ),
    };
  }

  @override
  Widget build(BuildContext context) {
    // Using a StatefulWidget because we need to manage the Google Maps controller
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.plat.restaurant),
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
      ),
      body: GoogleMap(
        initialCameraPosition: CameraPosition(
          target: _restaurantLocation,
          zoom: 15,
        ),
        markers: _markers,
        onMapCreated: (GoogleMapController controller) {
          _mapController = controller;
        },
      ),
    );
  }
}

```

## Default image for dishes

Let's add a default image placeholder to the assets folder:

```dart
// This is a reference to create the assets/images folder and a default_food.png image
// You'll need to manually add an image file called default_food.png to this location
// or modify the code to use another default image

```

## Project Structure and Summary

Here's the structure we've created:

1. **Main App**
    
    - `main.dart`: Entry point with Firebase initialization and authentication check
2. **Models**
    
    - `plat.dart`: Model class for dishes with attributes like name, description, type, etc.
3. **Screens**
    
    - `login_screen.dart`: Login screen with username and password fields (Exercise 1)
    - `home_screen.dart`: Home screen showing list of dishes (Exercise 2.1)
    - `plat_detail_screen.dart`: Detail view of a selected dish (Exercise 2.2)
    - `map_screen.dart`: Google Maps view showing restaurant location (Exercise 3)
4. **Assets**
    
    - `assets/images/default_food.png`: Default image for dishes without photos

## Running the Project

To run this project:

1. Make sure you have the necessary dependencies installed
2. Add the `assets/images/default_food.png` file
3. Run the project with `flutter run`

## Notes on the Implementation

1. **Login System (Exercise 1)**
    
    - Uses SharedPreferences to store credentials locally
    - Checks for stored credentials on app start
    - Provides logout functionality
2. **Dish List (Exercise 2.1)**
    
    - Fetches dishes from Firebase
    - Displays dish name and image in a list
    - Shows default image when none is available
3. **Dish Detail (Exercise 2.2)**
    
    - Shows all dish attributes
    - Displays availability with a switch
    - Shows image with proper fallback to default
4. **Maps Integration (Exercise 3)**
    
    - Shows restaurant location on Google Maps
    - Creates a marker for the restaurant
    - Shows restaurant name in the marker info window

This implementation satisfies all the requirements of the exam while maintaining clean code organization and appropriate comments.