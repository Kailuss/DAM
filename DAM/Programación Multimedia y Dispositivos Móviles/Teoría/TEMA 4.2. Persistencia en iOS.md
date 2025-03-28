---
number headings: max 3, _.1.1., skip ^sk
tags: [DAM, PMDM]
banner: "![[pmdm.jpg]]"
banner_y: 0.42
cssclasses: [dam-pmdm, table-compact-clean]
---

# **TEMA 4.2.** <br>Persistencia en iOS

## 1. Ficheros y SQLite

### 1.1. **Ficheros plist (Property Lists)**

#### Lectura de ficheros plist

Los ficheros plist son archivos XML utilizados para almacenar datos de configuración. Se pueden leer desde el bundle principal de la aplicación.

```objective-c
NSString *path = [[NSBundle mainBundle] pathForResource:@"configUsuario" ofType:@"plist"];
NSDictionary *diccionario = [[NSDictionary alloc] initWithContentsOfFile:path];
NSString *nombre = [diccionario objectForKey:@"nombre"];
```

#### Escritura de ficheros plist

Para escribir datos en un fichero plist, se utiliza el directorio de documentos de la aplicación.

```objective-c
NSString *documentsPath = [NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES) objectAtIndex:0];
NSString *filePath = [documentsPath stringByAppendingPathComponent:@"configUsuario.plist"];
[diccionario writeToFile:filePath atomically:YES];
```

#### Ejemplo práctico con UITableView

Se puede cargar datos desde un plist y mostrarlos en una tabla.

```objective-c
NSString *path = [[NSBundle mainBundle] pathForResource:@"series" ofType:@"plist"];
NSDictionary *diccionario = [[NSDictionary alloc] initWithContentsOfFile:path];
NSArray *series = [diccionario objectForKey:@"series"];
```

### 1.2. **SQLite**

#### Configuración inicial

SQLite es una base de datos relacional ligera que se almacena en un único fichero.

#### Consultas básicas

Ejemplo de consulta para recuperar datos de una tabla.

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

#### Visualización en UITableView

Los datos recuperados pueden mostrarse en una tabla.

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

#### Ejemplo con series

Implementación similar para mostrar series desde SQLite.

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

## 2. User Defaults y Core Data

### 2.1. **User Defaults**

#### Almacenamiento básico

User Defaults es adecuado para pequeñas cantidades de datos.

```objective-c
NSUserDefaults *defaults = [NSUserDefaults standardUserDefaults];
[defaults setObject:@"Juan" forKey:@"nombre"];
[defaults setInteger:25 forKey:@"edad"];
[defaults synchronize];
```

#### Recuperación de datos

Los datos almacenados pueden recuperarse fácilmente.

```objective-c
NSString *nombre = [defaults stringForKey:@"nombre"];
int edad = [defaults integerForKey:@"edad"];
```

#### Ejemplo práctico

Uso para almacenar información del dispositivo y contador de inicios.

```objective-c
NSUserDefaults *defaults = [NSUserDefaults standardUserDefaults];
[defaults setObject:[[UIDevice currentDevice] name] forKey:@"nombreDispositivo"];
[defaults setInteger:[defaults integerForKey:@"vecesArrancado"] + 1 forKey:@"vecesArrancado"];
[defaults synchronize];
```

### 2.2. **Core Data**

#### Configuración inicial

Core Data proporciona un framework completo para la gestión de datos.

#### Creación de entidades

Ejemplo de creación de una entidad Persona.

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

#### Relaciones entre entidades

Creación de entidades relacionadas.

```objective-c
NSManagedObject *detallePersona = [NSEntityDescription insertNewObjectForEntityForName:@"DetallePersona" inManagedObjectContext:context];
[detallePersona setValue:@"Calle Falsa, 123" forKey:@"direccion"];
[detallePersona setValue:@"Alicante" forKey:@"localidad"];
[detallePersona setValue:@"España" forKey:@"pais"];
[detallePersona setValue:@"965656565" forKey:@"telefono"];
[detallePersona setValue:persona forKey:@"datosPersona"];
[persona setValue:detallePersona forKey:@"detalle"];
```

#### Consultas con NSFetchRequest

Recuperación de datos almacenados.

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

#### Clases generadas automáticamente

Uso de clases generadas para las entidades.

```objective-c
Persona *persona = [NSEntityDescription insertNewObjectForEntityForName:@"Persona" inManagedObjectContext:context];
persona.nombre = @"Juan";
persona.apellidos = @"Martinez";
persona.edad = [NSNumber numberWithInt:28];
```

#### Migraciones

Gestión de cambios en el modelo de datos.

```objective-c
NSDictionary *options = [NSDictionary dictionaryWithObjectsAndKeys:
    [NSNumber numberWithBool:YES], NSMigratePersistentStoresAutomaticallyOption,
    [NSNumber numberWithBool:YES], NSInferMappingModelAutomaticallyOption,
    nil];
if (![__persistentStoreCoordinator addPersistentStoreWithType:NSSQLiteStoreType configuration:nil URL:storeURL options:options error:&error]) {
    NSLog(@"Error al migrar: %@", [error localizedDescription]);
}
```

#### Ejemplo con series

Modelo más complejo con relaciones.

```objective-c
Serie *serie = [NSEntityDescription insertNewObjectForEntityForName:@"Serie" inManagedObjectContext:context];
serie.titulo = @"Breaking Bad";
serie.anyo = [NSNumber numberWithInt:2008];
DetalleSerie *detalle = [NSEntityDescription insertNewObjectForEntityForName:@"DetalleSerie" inManagedObjectContext:context];
detalle.sinopsis = @"Un profesor de química se convierte en fabricante de metanfetamina.";
detalle.duracion = [NSNumber numberWithInt:60];
serie.detalle = detalle;
```
