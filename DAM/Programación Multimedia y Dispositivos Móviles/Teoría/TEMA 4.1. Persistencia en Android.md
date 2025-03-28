---
tags: [DAM, PMDM]
cssclasses: [dam-pmdm, table-compact-clean]
banner: "![[pmdm.jpg]]"
banner_y: 0.42
---

# **TEMA 4.1.** <br>Persistencia en Android

## 1. Ficheros y SQLite

### 1.1. **Manejo de ficheros tradicionales en Android**

#### Apertura y operación con ficheros
Android permite el uso de ficheros tradicionales mediante `FileOutputStream` y `FileInputStream`. Los ficheros se almacenan en la carpeta privada de la aplicación (`/data/data/[paquete]/files/`). Es importante cerrar los flujos después de su uso.

```java
// Abrir un fichero de salida
FileOutputStream fos = openFileOutput("fichero.txt", Context.MODE_PRIVATE);
// Abrir un fichero de entrada
FileInputStream fis = openFileInput("fichero.txt");
fos.close();
fis.close();

// Ejemplo de escritura y lectura con DataOutputStream/DataInputStream
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

#### Ficheros como recursos
Los ficheros en `/res/raw/` son de solo lectura y se acceden mediante `openRawResource`.

```java
Resources myResources = getResources();
InputStream myFile = myResources.openRawResource(R.raw.fichero);
```

#### Almacenamiento en tarjeta SD
Requiere el permiso `WRITE_EXTERNAL_STORAGE` en el `Manifest.xml`.

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

### 1.2. **Base de datos SQLite**

#### Creación y manejo de la base de datos
Se recomienda usar `SQLiteOpenHelper` para gestionar la creación y actualización de la base de datos.

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

#### Operaciones con la base de datos
Inserción, consulta, actualización y borrado de datos.

```java
// Insertar datos con ContentValues
ContentValues nuevaFila = new ContentValues();
nuevaFila.put("nombre", "Juan");
nuevaFila.put("edad", 25);
db.insert("usuarios", null, nuevaFila);

// Consultar datos con Cursor
Cursor cursor = db.query("usuarios", null, null, null, null, null, null);
if (cursor.moveToFirst()) {
    do {
        String nombre = cursor.getString(cursor.getColumnIndex("nombre"));
        int edad = cursor.getInt(cursor.getColumnIndex("edad"));
    } while (cursor.moveToNext());
}
cursor.close();

// Actualizar datos
ContentValues valores = new ContentValues();
valores.put("nombre", "Juan");
valores.put("edad", 30);
db.update("usuarios", valores, "id = ?", new String[]{"1"});

// Borrar datos
db.delete("usuarios", "id = ?", new String[]{"1"});
```

#### Clase auxiliar para manejar la base de datos
Una clase adaptadora facilita el manejo de la base de datos.

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


## 2. Proveedores de contenidos y SharedPreferences

### 2.1. SharedPreferences

#### Guardar y leer preferencias
Almacena datos en pares clave-valor.

```java
// Guardar preferencias
SharedPreferences prefs = getSharedPreferences("MisPreferencias", Context.MODE_PRIVATE);
SharedPreferences.Editor editor = prefs.edit();
editor.putString("nombre", "Juan");
editor.putInt("edad", 25);
editor.commit();

// Leer preferencias
String nombre = prefs.getString("nombre", "Desconocido");
int edad = prefs.getInt("edad", 0);
```

#### Pantalla de preferencias con XML
Define una interfaz de preferencias en un archivo XML.

```xml
<PreferenceScreen xmlns:android="http://schemas.android.com/apk/res/android">
    <PreferenceCategory android:title="Configuración">
        <CheckBoxPreference
            android:key="mostrar_notificaciones"
            android:title="Mostrar notificaciones"
            android:defaultValue="true" />
        <EditTextPreference
            android:key="nombre_usuario"
            android:title="Nombre de usuario"
            android:defaultValue="Anónimo" />
    </PreferenceCategory>
</PreferenceScreen>
```

#### Actividad de preferencias
Muestra las preferencias definidas en XML.

```java
public class MisPreferencias extends PreferenceActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        addPreferencesFromResource(R.xml.preferencias);
    }
}
```

#### Detección de cambios en preferencias
Implementa `OnSharedPreferenceChangeListener` para reaccionar a cambios.

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

### 2.2. **Proveedores de contenidos**

#### Proveedores nativos
Acceso a datos como contactos o calendarios.

```java
Cursor cursor = getContentResolver().query(ContactsContract.Contacts.CONTENT_URI, null, null, null, null);
```

#### Crear un proveedor personalizado
Extiende `ContentProvider` y define los métodos CRUD.

```java
public class MiProveedor extends ContentProvider {
    @Override
    public boolean onCreate() {
        // Inicializar la base de datos
        return true;
    }

    @Override
    public Cursor query(Uri uri, String[] projection, String selection, String[] selectionArgs, String sortOrder) {
        SQLiteQueryBuilder queryBuilder = new SQLiteQueryBuilder();
        queryBuilder.setTables("usuarios");

        Cursor cursor = queryBuilder.query(db, projection, selection, selectionArgs, null, null, sortOrder);
        cursor.setNotificationUri(getContext().getContentResolver(), uri);
        return cursor;
    }

    @Override
    public Uri insert(Uri uri, ContentValues values) {
        long id = db.insert("usuarios", null, values);
        return ContentUris.withAppendedId(uri, id);
    }

    @Override
    public int update(Uri uri, ContentValues values, String selection, String[] selectionArgs) {
        return db.update("usuarios", values, selection, selectionArgs);
    }

    @Override
    public int delete(Uri uri, String selection, String[] selectionArgs) {
        return db.delete("usuarios", selection, selectionArgs);
    }

    @Override
    public String getType(Uri uri) {
        return "vnd.android.cursor.dir/vnd.es.ua.jtech.proveedor.usuarios";
    }
}
```

#### Registrar el proveedor en el Manifest
Declara el proveedor en `AndroidManifest.xml`.

```xml
<provider
    android:name=".MiProveedor"
    android:authorities="es.ua.jtech.proveedor" />
```

#### Uso de ContentResolver
Realiza operaciones sobre el proveedor.

```java
ContentResolver cr = getContentResolver();
ContentValues valores = new ContentValues();
valores.put("nombre", "Juan");
cr.insert(MiProveedor.CONTENT_URI, valores);

Cursor cursor = cr.query(MiProveedor.CONTENT_URI, null, null, null, null);
```