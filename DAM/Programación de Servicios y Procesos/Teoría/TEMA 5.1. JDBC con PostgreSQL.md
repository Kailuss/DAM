---
tags: [DAM, PSP]
cssclasses:
  - dam-psp
  - table-compact-clean
banner: "![[psp.jpg]]"
banner_y: 0.26
---

# **TEMA 5.1.** <br>JDBC con PostgreSQL <br>y tipos avanzados

En las últimas versiones, JDBC incorpora métodos y clases que permiten utilizar los nuevos tipos de datos. Seguiremos utilizando PostgreSQL para practicar estos conceptos.

## 1. Conexión

La ventaja de JDBC es que requiere muy pocos cambios al migrar entre sistemas gestores de bases de datos. Uno de los ajustes necesarios es modificar la URL. Por ejemplo, se reemplaza el protocolo `jdbc:mysql` por `jdbc:postgresql`, y es probable que también haya que cambiar el puerto, del `3306` de MySQL al `5432` de PostgreSQL.

Ejemplo de URL:  

```java
jdbc:postgresql://daw.paucasesnovescifp.cat:5432/usuaridb?user=usuari&password=seCret_25
```

En el resto del código, si no se utilizan características específicas del tema, no será necesario realizar cambios significativos.

## 2. Boolean

### 2.1. **Recuperar una columna boolean**

El objeto `ResultSet` incluye el método `getBoolean`, que devuelve un valor del tipo primitivo `boolean`.

Ejemplo:  

```java
try (Connection con = ...;
     Statement smt = con.createStatement();
     ResultSet rs = smt.executeQuery("select * from proves.\"Clients\"");) {
    while (rs.next()) {
        boolean recomanaria = rs.getBoolean("recomanaria");
        ...
    }
}
```

### 2.2. **Asignar o modificar una columna boolean**

En `executeUpdate`, se pueden utilizar cualquiera de los valores válidos. El objeto `PreparedStatement` proporciona el método `setBoolean(int index, boolean valor)`.

Ejemplo:  

```java
try (Connection con = ...;
     PreparedStatement stmt = con.prepareStatement("update proves.\"Clients\" set recomanari=? where id=?");) {
    stmt.setBoolean(1, true);
    stmt.setInt(2, 5);
    stmt.executeUpdate();
} catch (SQLException e) {
    ...
}
```

## 3. Arrays

No es posible trabajar directamente con arrays en la base de datos. Se debe utilizar la clase `java.sql.Array` como intermediario, realizando conversiones entre el array Java y este tipo de objeto.

### 3.1. **Recuperar un array**

El objeto `ResultSet` incluye el método `getArray`, que devuelve una referencia a un objeto del tipo `java.sql.Array`.

Ejemplo:  

```java
ResultSet rs = stmt.executeQuery();
while (rs.next()) {
    Array ref = rs.getArray("emails");
    String[] emails = (String[]) ref.getArray();
    ref.free();
}
```

**Importante.** El método `getArray` devuelve una referencia al array dentro de la base de datos, pero aún no se ha recuperado. Para obtener los datos y convertirlos a objetos Java, se debe realizar un casting.

### 3.2. **Insertar una fila con una columna de tipo array**

Si se utiliza `Statement`, se genera una cadena con la instrucción SQL. El array se representa como una cadena SQL entre llaves, con cada elemento del tipo correspondiente.

Ejemplo con `Statement`:  

```sql
insert into proves."Clients" values(5, 'Armando Adistancia', '{"ad@mail.net","ad@mail.org"}', false, null, null, null);
```

Para mayor seguridad y eficiencia, se recomienda utilizar `PreparedStatement`:

1. Crear un objeto `java.sql.Array` a partir de la conexión:  

```java
String[] temp = {"ad@mail.net", "ad@mail.org"};
java.sql.Array emails = con.createArrayOf("VARCHAR", temp);
```

2. Crear el `PreparedStatement` y utilizar el método `setArray`:  

```java
PreparedStatement st = con.prepareStatement("insert into proves.\"Clients\" values(?, ?, ?, ?, ?, ?, ?)");
st.setArray(3, emails);
st.executeUpdate();
```

## 4. Tipos definidos por el usuario

PostgreSQL permite definir nuevos tipos que pueden utilizarse para columnas de tablas. Para recuperar estas columnas, es necesario crear un POJO que represente el tipo definido.

### 4.1. **Recuperar un objeto de la base de datos**

JDBC incluye el método `getObject` en la clase `ResultSet`, que permite recuperar objetos de la base de datos. Cuando se trabaja con PostgreSQL, este método devuelve un objeto de tipo `PGobject`.

Pasos para recuperar un objeto:

1. Crear un POJO que implemente la interfaz `PGobject`.  
   - Incluir los métodos `getValue()` y `setValue(String)`.  
   - Definir un atributo de clase con el nombre del tipo en la base de datos:  

	 ```java
     public static final String sqlType = "\"proves\":\"t_telefon\"";
     ```  

   - Inicializar el atributo `type` de `PGobject` en los constructores.

2. Configurar la conexión para que reconozca la clase Java asociada al tipo de la base de datos:  

```java
PGConnection conPG = (PGConnection) con;
conPG.addDataType(Telefon.sqlType, Telefon.class);
```

3. Recuperar el objeto con `getObject` y realizar un casting:  

```java
Telefon telefon = (Telefon) rs.getObject("telefon");
```

Ejemplo completo:  

```java
try (Connection con = DriverManager.getConnection("jdbc:postgresql://192.168.56.103:5432/demo?user=postgres&password=seCret_24");
     PreparedStatement stmt = con.prepareStatement("select telefon from proves.\"Clients\" where id = ?");) {
    PGConnection conPG = (PGConnection) con;
    conPG.addDataType(Telefon.sqlType, Telefon.class);
    stmt.setInt(1, 5);
    try (ResultSet rs = stmt.executeQuery();) {
        while (rs.next()) {
            Telefon telefon = (Telefon) rs.getObject(1);
            if (telefon != null) {
                System.out.println("telefon = " + telefon);
            }
        }
    }
} catch (SQLException e) {
    System.out.println("e.getMessage() = " + e.getMessage());
}
```

### 4.2. **Método setValue()**

El objeto guardado en la base de datos llega al driver como una cadena de texto. El driver crea un objeto de la clase mapeada y llama a su método `setValue`, pasándole esta cadena. Este método debe parsear la cadena e inicializar los atributos del objeto.

Formato de la cadena:  

- Encerrada entre paréntesis `()`.  
- Valores separados por comas.  
- Cadenas de texto entre comillas dobles `" "`.

Ejemplo de implementación:  

```java
public abstract class TractaValors {
    public static String[] parseValue(String value) {
        value = value.replaceAll(",\\)", ",null)");
        value = value.replaceAll("\\(,", "(null,");
        value = value.replaceAll(", ,", ",null,");
        String valor = value.substring(1, value.length() - 1);
        valor = tractaComes(valor);
        String[] atributs = valor.split(",");
        for (int i = 0; i < atributs.length; i++) {
            if ("null".equalsIgnoreCase(atributs[i])) {
                atributs[i] = null;
            } else if (atributs[i].charAt(0) == '\"' && atributs[i].charAt(atributs[i].length() - 1) == '\"') {
                atributs[i] = atributs[i].substring(1, atributs[i].length() - 1);
                atributs[i] = recuperaComes(atributs[i]);
            }
        }
        return atributs;
    }
}
```

### 4.3. **Insertar o modificar un objeto en la base de datos**

Para insertar o modificar una fila con un campo de tipo objeto, se recomienda utilizar `PreparedStatement`.

Pasos:  

1. Crear el objeto Java.  
2. Pasarlo al `PreparedStatement` con `setObject`. Este método utiliza `getValue()` para obtener los datos del objeto como cadena.

Ejemplo:  

```java
try (Connection con = DriverManager.getConnection("jdbc:postgresql://192.168.56.103:5432/demo?user=postgres&password=seCret_25");
     PreparedStatement stmt = con.prepareStatement("update proves.\"Clients\" set telefon=? where id=?");) {
    Telefon telefon = new Telefon("974456528", "Casa platja");
    PGConnection conPG = (PGConnection) con;
    conPG.addDataType(Telefon.sqlType, Telefon.class);
    stmt.setObject(1, telefon);
    stmt.setInt(2, 5);
    stmt.executeUpdate();
} catch (SQLException e) {
    System.out.println("Error: " + e.getMessage());
}
```

### 4.4. **Método getValue()**

Este método debe devolver los valores de los atributos del objeto en el formato utilizado por el driver.

Ejemplo:  

```java
@Override
public String getValue() {
    String resultat = "(\"" + tipus + "\",";
    resultat += numero + ")";
    return resultat;
}
```

Los atributos de tipo `String` deben encerrarse entre comillas dobles, mientras que los de otros tipos no las requieren.
