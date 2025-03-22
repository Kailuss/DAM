---
banner: "![[pmdm.jpg]]"
banner_y: 0.42
cssclasses:
- table-clean
number headings: _.1.1.
---

# **TEMA 4.** <br>Persistencia


| Anexos     |
| --- |
| [Tema 4 PMDP. Anexo](Tema%204%20PMDP.%20Anexo.md) |
| [Tarea PMDM04](../Práctica/Tareas/Tarea%20PMDM04.md) |


## 1. Persistencia en Android: ficheros y SQLite

### 1.1. **Introducción**

En este módulo se exploran los mecanismos de almacenamiento de datos en Android e iOS. En Android, se cubre el manejo de ficheros y el uso de SQLite para bases de datos. También se presentan los proveedores de contenidos, que permiten el intercambio de información entre aplicaciones. En iOS, se aborda el uso de ficheros plist, SQLite, User Defaults y Core Data.

### 1.2. **Manejo de ficheros tradicionales en Android**

Android permite el uso de ficheros tradicionales, aunque existen alternativas más avanzadas como SQLite y SharedPreferences.

#### Apertura de ficheros

Para abrir un fichero en Android, se utiliza `FileOutputStream` y `FileInputStream`. El fichero se almacena en la carpeta de la aplicación y puede ser accedido mediante el shell de adb.

```java
// Abrir un fichero de salida privado a la aplicación
FileOutputStream fos = openFileOutput("fichero.txt", Context.MODE_PRIVATE);
// Abrir un fichero de entrada
FileInputStream fis = openFileInput("fichero.txt");
```

El fichero abierto utilizando `openFileOutput` se guarda en la carpeta `/data/data/[paquete]/files/`, donde `[paquete]` es el nombre del paquete de la aplicación. Es importante cerrar el fichero después de su uso con `fos.close()` o `fis.close()`.

#### Ficheros como recursos

Los ficheros pueden añadirse como recursos en la carpeta `/res/raw/`. Estos ficheros son de solo lectura y se accede a ellos mediante `openRawResource`.

```java
Resources myResources = getResources();
InputStream myFile = myResources.openRawResource(R.raw.fichero);
```

Este método es útil para almacenar datos estáticos como diccionarios o configuraciones.

#### Operar con ficheros

Se pueden usar clases como `DataInputStream` y `DataOutputStream` para leer y escribir en ficheros. Estas clases permiten manejar diferentes tipos de datos, como enteros y cadenas.

```java
FileOutputStream fos = openFileOutput("fichero.txt", Context.MODE_PRIVATE);
String cadenaOutput = "Contenido del fichero\n";
DataOutputStream dos = new DataOutputStream(fos);
dos.writeBytes(cadenaOutput);
fos.close();

FileInputStream fin = openFileInput("fichero.txt");
DataInputStream dis = new DataInputStream(fin);
String string = dis.readLine();
fin.close();
```

#### Almacenar datos en la tarjeta de memoria

Para escribir en la tarjeta SD, se utiliza `Environment.getExternalStorageDirectory()` y `FileWriter`. Es necesario añadir el permiso `WRITE_EXTERNAL_STORAGE` en el archivo `Manifest.xml`.

```java
try {
    File raiz = Environment.getExternalStorageDirectory();
    if (raiz.canWrite()) {
        File file = new File(raiz, "fichero.txt");
        BufferedWriter out = new BufferedWriter(new FileWriter(file));
        out.write("Mi texto escrito desde Android\n");
        out.close();
    }
} catch (IOException e) {
    Log.e("FILE I/O", "Error en la escritura de fichero: " + e.getMessage());
}
```

### 1.3. **Base de datos SQLite**

SQLite es un gestor de bases de datos relacional ligero y de código abierto. En Android, SQLite se implementa como una librería C, lo que reduce dependencias externas y simplifica la sincronización.

#### Content Values

Para insertar filas en una tabla, se utiliza la clase `ContentValues`. SQLite es débilmente tipado, lo que permite flexibilidad en el manejo de datos.

```java
ContentValues nuevaFila = new ContentValues();
nuevaFila.put("nombre", "Juan");
nuevaFila.put("edad", 25);
db.insert("usuarios", null, nuevaFila);
```

#### Cursores

Los cursores son punteros a los resultados de una consulta. Permiten navegar por los resultados y extraer valores específicos.

```java
Cursor cursor = db.query("usuarios", null, null, null, null, null, null);
if (cursor.moveToFirst()) {
    do {
        String nombre = cursor.getString(cursor.getColumnIndex("nombre"));
        int edad = cursor.getInt(cursor.getColumnIndex("edad"));
    } while (cursor.moveToNext());
}
cursor.close();
```

#### Trabajar con bases de datos SQLite

Es recomendable crear una clase auxiliar para interactuar con la base de datos. Esta clase debe incluir métodos para crear, abrir y cerrar la base de datos, así como para realizar operaciones como inserción, borrado y actualización.

```java
public class MiAdaptadorBD {
    private SQLiteDatabase db;
    private final Context contexto;
    private MiHelperBD dbHelper;

    public MiAdaptadorBD(Context contexto) {
        this.contexto = contexto;
        dbHelper = new MiHelperBD(contexto, "mibasededatos.db", null, 1);
    }

    public MiAdaptadorBD open() throws SQLException {
        db = dbHelper.getWritableDatabase();
        return this;
    }

    public void close() {
        dbHelper.close();
    }

    public long insertar(String nombre, int edad) {
        ContentValues valores = new ContentValues();
        valores.put("nombre", nombre);
        valores.put("edad", edad);
        return db.insert("usuarios", null, valores);
    }
}
```

#### La clase SQLiteOpenHelper

`SQLiteOpenHelper` es una clase abstracta que facilita la creación, apertura y actualización de bases de datos. Implementa métodos como `onCreate` y `onUpgrade` para manejar la creación y actualización de la base de datos.

```java
public class MiHelperBD extends SQLiteOpenHelper {
    private static final String CREAR_TABLA = "CREATE TABLE usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, edad INTEGER);";

    public MiHelperBD(Context contexto, String nombre, SQLiteDatabase.CursorFactory factory, int version) {
        super(contexto, nombre, factory, version);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL(CREAR_TABLA);
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int versionAnterior, int versionNueva) {
        db.execSQL("DROP TABLE IF EXISTS usuarios");
        onCreate(db);
    }
}
```

#### Crear una base de datos sin SQLiteHelper

También es posible crear una base de datos sin usar `SQLiteHelper` mediante `openOrCreateDatabase` y `execSQL`.

```java
SQLiteDatabase db = openOrCreateDatabase("mibasededatos.db", Context.MODE_PRIVATE, null);
db.execSQL("CREATE TABLE usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, edad INTEGER);");
```

#### Realizar una consulta

El método `query` de `SQLiteDatabase` permite realizar consultas. Los resultados se devuelven como un objeto `Cursor`.

```java
Cursor cursor = db.query("usuarios", new String[]{"nombre", "edad"}, "edad > ?", new String[]{"20"}, null, null, "nombre ASC");
```

#### Extraer resultados de un cursor

Para extraer datos de un cursor, se utilizan métodos como `moveToFirst` y `getString`.

```java
if (cursor.moveToFirst()) {
    do {
        String nombre = cursor.getString(0);
        int edad = cursor.getInt(1);
    } while (cursor.moveToNext());
}
cursor.close();
```

#### Añadir, actualizar y borrar filas

La clase `SQLiteDatabase` proporciona métodos como `insert`, `update` y `delete` para manipular datos en la base de datos.

```java
ContentValues valores = new ContentValues();
valores.put("nombre", "Juan");
valores.put("edad", 30);
db.update("usuarios", valores, "id = ?", new String[]{"1"});

db.delete("usuarios", "id = ?", new String[]{"1"});
```

## 2. Persistencia en Android: ficheros y SQLite

### 2.1. **Uso de ficheros**

En este ejercicio se crea una aplicación que almacena cadenas en un fichero de texto. El fichero se abre en modo `MODE_APPEND` para añadir nuevas cadenas al final.

```java
FileOutputStream fos = openFileOutput("fichero.txt", Context.MODE_APPEND);
DataOutputStream dos = new DataOutputStream(fos);
dos.writeBytes("Nueva cadena\n");
fos.close();
```

### 2.2. **Persistencia con ficheros (*)**

Se modifica la aplicación para que el contenido del `TextView` se mantenga al reiniciar la aplicación.

```java
@Override
protected void onSaveInstanceState(Bundle outState) {
    super.onSaveInstanceState(outState);
    outState.putString("texto", textView.getText().toString());
}

@Override
protected void onRestoreInstanceState(Bundle savedInstanceState) {
    super.onRestoreInstanceState(savedInstanceState);
    textView.setText(savedInstanceState.getString("texto"));
}
```

### 2.3. **Base de datos: SQLiteOpenHelper**

Se implementa una clase `SQLiteOpenHelper` para manejar una base de datos de usuarios. Se completan los métodos `onCreate` y `onUpgrade`.

```java
public class MiHelperBD extends SQLiteOpenHelper {
    private static final String CREAR_TABLA = "CREATE TABLE usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT);";

    public MiHelperBD(Context contexto, String nombre, SQLiteDatabase.CursorFactory factory, int version) {
        super(contexto, nombre, factory, version);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL(CREAR_TABLA);
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int versionAnterior, int versionNueva) {
        db.execSQL("DROP TABLE IF EXISTS usuarios");
        onCreate(db);
    }
}
```

### 2.4. **Base de datos: inserción y borrado**

Se implementan métodos para insertar y borrar usuarios en la base de datos utilizando sentencias SQL precompiladas.

```java
public int insertar(String nombre) {
    ContentValues valores = new ContentValues();
    valores.put("nombre", nombre);
    return db.insert("usuarios", null, valores);
}

public boolean eliminar(long id) {
    return db.delete("usuarios", "id = ?", new String[]{String.valueOf(id)}) > 0;
}
```

### 2.5. **Base de datos: probar nuestro adaptador**

Se añade código en la actividad principal para eliminar, insertar y listar usuarios en la base de datos.

```java
MiAdaptadorBD adaptador = new MiAdaptadorBD(this);
adaptador.open();
adaptador.eliminarTodos();
adaptador.insertar("Juan");
adaptador.insertar("Ana");
Cursor cursor = adaptador.obtenerTodos();
// Mostrar los datos en un TextView
adaptador.close();
```

### 2.6. **Base de datos: cambios en la base de datos (*)**

Se modifica el nombre de una columna en la base de datos y se soluciona el error resultante.

```java
// Cambiar el nombre de la columna en el método onUpgrade
@Override
public void onUpgrade(SQLiteDatabase db, int versionAnterior, int versionNueva) {
    db.execSQL("ALTER TABLE usuarios RENAME COLUMN nombre TO nombres");
}
```

## 3. Persistencia en Android: proveedores de contenidos y SharedPreferences

### 3.1. **Shared Preferences**

`SharedPreferences` es un mecanismo ligero para almacenar datos en pares clave-valor. Se utiliza para guardar preferencias y estados de la aplicación.

#### Guardar Shared Preferences

Se utiliza `SharedPreferences.Editor` para modificar y guardar preferencias.

```java
SharedPreferences prefs = getSharedPreferences("MisPreferencias", Context.MODE_PRIVATE);
SharedPreferences.Editor editor = prefs.edit();
editor.putString("nombre", "Juan");
editor.putInt("edad", 25);
editor.commit();
```

#### Leer Shared Preferences

Se accede a las preferencias mediante `getSharedPreferences` y se obtienen valores con métodos como `getBoolean` y `getString`.

```java
SharedPreferences prefs = getSharedPreferences("MisPreferencias", Context.MODE_PRIVATE);
String nombre = prefs.getString("nombre", "Desconocido");
int edad = prefs.getInt("edad", 0);
```

#### Interfaces para Shared Preferences

Android proporciona una plataforma basada en XML para crear interfaces gráficas de preferencias.

```xml
<PreferenceScreen xmlns:android="http://schemas.android.com/apk/res/android">
    <CheckBoxPreference
        android:key="mostrar_notificaciones"
        android:title="Mostrar notificaciones"
        android:defaultValue="true" />
</PreferenceScreen>
```

#### Definiendo una pantalla de preferencias con un layout en XML

Se define un layout XML para la actividad de preferencias, utilizando elementos como `PreferenceCategory` y `CheckBoxPreference`.

```xml
<PreferenceScreen xmlns:android="http://schemas.android.com/apk/res/android">
    <PreferenceCategory android:title="Configuración">
        <CheckBoxPreference
            android:key="mostrar_notificaciones"
            android:title="Mostrar notificaciones"
            android:defaultValue="true" />
    </PreferenceCategory>
</PreferenceScreen>
```

#### Controles nativos para preferencias

Android incluye controles como `CheckBoxPreference`, `EditTextPreference` y `ListPreference` para manejar preferencias.

```xml
<EditTextPreference
    android:key="nombre_usuario"
    android:title="Nombre de usuario"
    android:defaultValue="Anónimo" />
```

#### Actividades de preferencias

Se crea una subclase de `PreferenceActivity` para mostrar la pantalla de preferencias.

```java
public class MisPreferencias extends PreferenceActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        addPreferencesFromResource(R.xml.preferencias);
    }
}
```

#### Shared Preference Change Listeners

Se implementa `OnSharedPreferenceChangeListener` para detectar cambios en las preferencias.

```java
public class MainActivity extends Activity implements OnSharedPreferenceChangeListener {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(this);
        prefs.registerOnSharedPreferenceChangeListener(this);
    }

    @Override
    public void onSharedPreferenceChanged(SharedPreferences prefs, String key) {
        if (key.equals("mostrar_notificaciones")) {
            boolean mostrar = prefs.getBoolean(key, true);
            // Actualizar la interfaz
        }
    }
}
```

### 3.2. **Proveedores de contenidos**

Los proveedores de contenidos permiten compartir datos entre aplicaciones mediante URIs.

#### Proveedores nativos

Android incluye proveedores nativos para acceder a datos como contactos, calendarios y multimedia.

```java
Cursor cursor = getContentResolver().query(ContactsContract.Contacts.CONTENT_URI, null, null, null, null);
```

#### Proveedores propios: crear un nuevo proveedor de contenidos

Se crea un proveedor de contenidos personalizado extendiendo la clase `ContentProvider`.

```java
public class MiProveedor extends ContentProvider {
    @Override
    public boolean onCreate() {
        // Inicializar la base de datos
        return true;
    }

    @Override
    public Cursor query(Uri uri, String[] projection, String selection, String[] selectionArgs, String sortOrder) {
        // Realizar la consulta
        return null;
    }

    @Override
    public Uri insert(Uri uri, ContentValues values) {
        // Insertar un nuevo registro
        return null;
    }

    @Override
    public int update(Uri uri, ContentValues values, String selection, String[] selectionArgs) {
        // Actualizar un registro
        return 0;
    }

    @Override
    public int delete(Uri uri, String selection, String[] selectionArgs) {
        // Borrar un registro
        return 0;
    }

    @Override
    public String getType(Uri uri) {
        // Devolver el tipo MIME
        return null;
    }
}
```

#### Proveedores propios: crear la interfaz de consultas

Se implementan los métodos `query`, `insert`, `update` y `delete` en el proveedor de contenidos.

```java
@Override
public Cursor query(Uri uri, String[] projection, String selection, String[] selectionArgs, String sortOrder) {
    SQLiteQueryBuilder queryBuilder = new SQLiteQueryBuilder();
    queryBuilder.setTables("usuarios");

    switch (uriMatcher.match(uri)) {
        case TODAS_FILAS:
            break;
        case UNA_FILA:
            queryBuilder.appendWhere("id = " + uri.getPathSegments().get(1));
            break;
    }

    Cursor cursor = queryBuilder.query(db, projection, selection, selectionArgs, null, null, sortOrder);
    cursor.setNotificationUri(getContext().getContentResolver(), uri);
    return cursor;
}
```

#### Proveedores propios: tipo MIME

Se define el tipo MIME para los datos devueltos por el proveedor.

```java
@Override
public String getType(Uri uri) {
    switch (uriMatcher.match(uri)) {
        case TODAS_FILAS:
            return "vnd.android.cursor.dir/vnd.es.ua.jtech.proveedor.usuarios";
        case UNA_FILA:
            return "vnd.android.cursor.item/vnd.es.ua.jtech.proveedor.usuarios";
        default:
            throw new IllegalArgumentException("URI no soportada: " + uri);
    }
}
```

#### Proveedores propios: registrar el proveedor

El proveedor de contenidos se registra en el archivo `AndroidManifest.xml`.

```xml
<provider
    android:name=".MiProveedor"
    android:authorities="es.ua.jtech.proveedor" />
```

#### Content Resolvers

Se utiliza `ContentResolver` para realizar consultas y operaciones sobre proveedores de contenidos.

```java
ContentResolver cr = getContentResolver();
Cursor cursor = cr.query(MiProveedor.CONTENT_URI, null, null, null, null);
```

#### Otras operaciones con Content Resolvers

Se realizan operaciones como inserción, borrado y actualización de datos mediante `ContentResolver`.

```java
ContentValues valores = new ContentValues();
valores.put("nombre", "Juan");
Uri nuevaUri = cr.insert(MiProveedor.CONTENT_URI, valores);

cr.delete(MiProveedor.CONTENT_URI, "id = ?", new String[]{"1"});

valores.put("nombre", "Ana");
cr.update(MiProveedor.CONTENT_URI, valores, "id = ?", new String[]{"1"});
```

## 4. Persistencia en Android: proveedores de contenidos y SharedPreferences

### 4.1. **Compartir datos entre actividades con Shared Preferences**

Se utiliza `SharedPreferences` para compartir datos entre dos actividades.

```java
SharedPreferences prefs = getSharedPreferences("MisPreferencias", Context.MODE_PRIVATE);
SharedPreferences.Editor editor = prefs.edit();
editor.putString("nombre", nombre);
editor.putInt("edad", edad);
editor.commit();
```

### 4.2. **Actividad de preferencias**

Se añade una actividad de preferencias para configurar la validación de un DNI.

```java
public class PreferenciasActivity extends PreferenceActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        addPreferencesFromResource(R.xml.preferencias);
    }
}
```

### 4.3. **Proveedor de contenidos propio**

Se implementa un proveedor de contenidos para acceder a una base de datos de usuarios.

```java
public class UsuariosProvider extends ContentProvider {
    @Override
    public boolean onCreate() {
        // Inicializar la base de datos
        return true;
    }

    @Override
    public Cursor query(Uri uri, String[] projection, String selection, String[] selectionArgs, String sortOrder) {
        // Realizar la consulta
        return null;
    }
}
```

### 4.4. **¿Por qué conviene crear proveedores de contenidos? (*)**

Los proveedores de contenidos permiten notificar cambios y actualizar automáticamente los componentes de la interfaz.

```java
cursor.setNotificationUri(getContext().getContentResolver(), uri);
```

## 5. Persistencia de datos en iOS: Ficheros y SQLite

### 5.1. **Introducción**

En iOS, la persistencia de datos se realiza mediante memoria flash. Los métodos principales son ficheros plist, SQLite, User Defaults y Core Data.

### 5.2. **Ficheros plist (Property Lists)**

Los ficheros plist son archivos XML utilizados para almacenar datos de configuración.

#### Leyendo datos desde ficheros plist

Se crea un fichero plist y se accede a sus datos mediante `NSDictionary`.

```objective-c
NSString *path = [[NSBundle mainBundle] pathForResource:@"configUsuario" ofType:@"plist"];
NSDictionary *diccionario = [[NSDictionary alloc] initWithContentsOfFile:path];
NSString *nombre = [diccionario objectForKey:@"nombre"];
```

#### Escribiendo datos en ficheros plist

Se escribe en un fichero plist almacenado en el directorio de documentos.

```objective-c
NSString *documentsPath = [NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES) objectAtIndex:0];
NSString *filePath = [documentsPath stringByAppendingPathComponent:@"configUsuario.plist"];
[diccionario writeToFile:filePath atomically:YES];
```

### 5.3. **SQLite**

SQLite es una base de datos relacional ligera que se almacena en un fichero.

#### Herramientas disponibles

Se utiliza SQLite Database Browser para crear y gestionar la base de datos.

#### Lectura de datos

Se implementa una clase para manejar la base de datos y se leen datos mediante consultas SQL.

```objective-c
NSString *query = @"SELECT * FROM personas";
sqlite3_stmt *statement;
if (sqlite3_prepare_v2(database, [query UTF8String], -1, &statement, NULL) == SQLITE_OK) {
    while (sqlite3_step(statement) == SQLITE_ROW) {
        NSString *nombre = [NSString stringWithUTF8String:(char *)sqlite3_column_text(statement, 1)];
        int edad = sqlite3_column_int(statement, 2);
    }
    sqlite3_finalize(statement);
}
```

#### Mostrando los datos en una tabla

Se muestra un listado de personas en una tabla `UITableView`.

```objective-c
- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    static NSString *CellIdentifier = @"Cell";
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:CellIdentifier];
    if (cell == nil) {
        cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleSubtitle reuseIdentifier:CellIdentifier];
    }
    Persona *persona = [self.listaPersonas objectAtIndex:indexPath.row];
    cell.textLabel.text = persona.nombre;
    cell.detailTextLabel.text = [NSString stringWithFormat:@"%d años", persona.edad];
    return cell;
}
```

## 6. Persistencia de datos en iOS: Ficheros y SQLite

### 6.1. **Creando y leyendo un fichero plist**

Se crea un fichero plist con datos de series y se muestran en una tabla.

```objective-c
NSString *path = [[NSBundle mainBundle] pathForResource:@"series" ofType:@"plist"];
NSDictionary *diccionario = [[NSDictionary alloc] initWithContentsOfFile:path];
NSArray *series = [diccionario objectForKey:@"series"];
```

### 6.2. **Implementar vista de detalle de la serie**

Se muestra información adicional de cada serie en una vista de detalle.

```objective-c
- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath {
    Serie *serie = [self.series objectAtIndex:indexPath.row];
    DetalleSerieViewController *detalleVC = [[DetalleSerieViewController alloc] initWithSerie:serie];
    [self.navigationController pushViewController:detalleVC animated:YES];
}
```

### 6.3. **(*) Uso básico de una base de datos SQLite**

Se crea una aplicación similar a la anterior, pero utilizando SQLite como método de persistencia.

```objective-c
NSString *query = @"SELECT * FROM series";
sqlite3_stmt *statement;
if (sqlite3_prepare_v2(database, [query UTF8String], -1, &statement, NULL) == SQLITE_OK) {
    while (sqlite3_step(statement) == SQLITE_ROW) {
        NSString *titulo = [NSString stringWithUTF8String:(char *)sqlite3_column_text(statement, 1)];
        int anyo = sqlite3_column_int(statement, 2);
    }
    sqlite3_finalize(statement);
}
```

## 7. Persistencia de datos en iOS: User Defaults y Core Data

### 7.1. **Introducción**

Se presentan User Defaults y Core Data como métodos de persistencia en iOS.

### 7.2. **User Defaults**

User Defaults es un método sencillo para almacenar pequeñas cantidades de datos.

#### Guardar y leer datos

Se utiliza `NSUserDefaults` para guardar y leer datos como nombres y edades.

```objective-c
NSUserDefaults *defaults = [NSUserDefaults standardUserDefaults];
[defaults setObject:@"Juan" forKey:@"nombre"];
[defaults setInteger:25 forKey:@"edad"];
[defaults synchronize];

NSString *nombre = [defaults stringForKey:@"nombre"];
int edad = [defaults integerForKey:@"edad"];
```

### 7.3. **Core Data**

Core Data es un método avanzado para almacenar datos complejos.

#### Creando el proyecto

Se crea un proyecto con Core Data y se define un modelo de datos.

```objective-c
NSManagedObjectContext *context = [self managedObjectContext];
NSManagedObject *persona = [NSEntityDescription insertNewObjectForEntityForName:@"Persona" inManagedObjectContext:context];
[persona setValue:@"Juan" forKey:@"nombre"];
[persona setValue:@"Martinez" forKey:@"apellidos"];
[persona setValue:[NSNumber numberWithInt:28] forKey:@"edad"];
NSError *error;
if (![context save:&error]) {
    NSLog(@"Error al guardar: %@", [error localizedDescription]);
}
```

#### Definiendo el modelo de datos

Se crean entidades como `Persona` y `DetallePersona` con atributos y relaciones.

```objective-c
NSManagedObject *detallePersona = [NSEntityDescription insertNewObjectForEntityForName:@"DetallePersona" inManagedObjectContext:context];
[detallePersona setValue:@"Calle Falsa, 123" forKey:@"direccion"];
[detallePersona setValue:@"Alicante" forKey:@"localidad"];
[detallePersona setValue:@"España" forKey:@"pais"];
[detallePersona setValue:@"965656565" forKey:@"telefono"];
[detallePersona setValue:persona forKey:@"datosPersona"];
[persona setValue:detallePersona forKey:@"detalle"];
```

#### Probando el modelo

Se insertan datos en el modelo y se muestran en la consola.

```objective-c
NSFetchRequest *fetchRequest = [[NSFetchRequest alloc] init];
NSEntityDescription *entity = [NSEntityDescription entityForName:@"Persona" inManagedObjectContext:context];
[fetchRequest setEntity:entity];
NSArray *fetchedObjects = [context executeFetchRequest:fetchRequest error:&error];
for (NSManagedObject *info in fetchedObjects) {
    NSLog(@"Nombre: %@", [info valueForKey:@"nombre"]);
    NSLog(@"Apellidos: %@", [info valueForKey:@"apellidos"]);
    NSLog(@"Edad: %d", [[info valueForKey:@"edad"] intValue]);
}
```

#### Generando los modelos automáticamente

Se generan clases automáticamente para las entidades del modelo.

```objective-c
Persona *persona = [NSEntityDescription insertNewObjectForEntityForName:@"Persona" inManagedObjectContext:context];
persona.nombre = @"Juan";
persona.apellidos = @"Martinez";
persona.edad = [NSNumber numberWithInt:28];
```

#### Creando la vista de tabla

Se muestra un listado de personas en una tabla `UITableView`.

```objective-c
- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    static NSString *CellIdentifier = @"Cell";
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:CellIdentifier];
    if (cell == nil) {
        cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleSubtitle reuseIdentifier:CellIdentifier];
    }
    Persona *persona = [self.listaPersonas objectAtIndex:indexPath.row];
    cell.textLabel.text = persona.nombre;
    cell.detailTextLabel.text = [NSString stringWithFormat:@"%d años", [persona.edad intValue]];
    return cell;
}
```

#### Migraciones de bases de datos con Core Data

Se explica cómo realizar migraciones de bases de datos en Core Data.

```objective-c
NSDictionary *options = [NSDictionary dictionaryWithObjectsAndKeys:
    [NSNumber numberWithBool:YES], NSMigratePersistentStoresAutomaticallyOption,
    [NSNumber numberWithBool:YES], NSInferMappingModelAutomaticallyOption,
    nil];
if (![__persistentStoreCoordinator addPersistentStoreWithType:NSSQLiteStoreType configuration:nil URL:storeURL options:options error:&error]) {
    NSLog(@"Error al migrar: %@", [error localizedDescription]);
}
```

## 8. Persistencia de datos en iOS: User Defaults y Core Data

### 8.1. **Usando las variables de usuario (User Defaults)**

Se utiliza `NSUserDefaults` para almacenar datos del dispositivo y el número de veces que se ha arrancado la aplicación.

```objective-c
NSUserDefaults *defaults = [NSUserDefaults standardUserDefaults];
[defaults setObject:[[UIDevice currentDevice] name] forKey:@"nombreDispositivo"];
[defaults setInteger:[defaults integerForKey:@"vecesArrancado"] + 1 forKey:@"vecesArrancado"];
[defaults synchronize];
```

### 8.2. **Diseñando un modelo de datos sencillo con Core Data**

Se diseña un modelo de datos con dos tablas relacionadas y se muestran los datos en una tabla.

```objective-c
NSManagedObjectContext *context = [self managedObjectContext];
Serie *serie = [NSEntityDescription insertNewObjectForEntityForName:@"Serie" inManagedObjectContext:context];
serie.titulo = @"Breaking Bad";
serie.anyo = [NSNumber numberWithInt:2008];
DetalleSerie *detalle = [NSEntityDescription insertNewObjectForEntityForName:@"DetalleSerie" inManagedObjectContext:context];
detalle.sinopsis = @"Un profesor de química se convierte en fabricante de metanfetamina.";
detalle.duracion = [NSNumber numberWithInt:60];
serie.detalle = detalle;
```

### 8.3. **(*) Migrando datos con Core Data**

Se modifica el modelo de datos y se realiza una migración para evitar errores.

```objective-c
NSDictionary *options = [NSDictionary dictionaryWithObjectsAndKeys:
    [NSNumber numberWithBool:YES], NSMigratePersistentStoresAutomaticallyOption,
    [NSNumber numberWithBool:YES], NSInferMappingModelAutomaticallyOption,
    nil];
if (![__persistentStoreCoordinator addPersistentStoreWithType:NSSQLiteStoreType configuration:nil URL:storeURL options:options error:&error]) {
    NSLog(@"Error al migrar: %@", [error localizedDescription]);
}
```
