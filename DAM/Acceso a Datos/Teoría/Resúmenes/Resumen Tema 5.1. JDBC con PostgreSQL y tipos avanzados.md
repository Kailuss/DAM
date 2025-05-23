---
tags:
  - DAM
  - AD
cssclasses:
  - dam-ad
  - table-clean
banner: "![[ad.jpg]]"
banner_y: 0.32
---

# **Resumen TEMA 5.1.** <br>JDBC con PostgreSQL y tipos avanzados

## Conceptos clave
- **JDBC con PostgreSQL**: Adaptación para trabajar con tipos avanzados
- **Tipos soportados**: Booleanos, arrays y tipos definidos por usuario
- **Conversión de tipos**: Mecanismos para transformar entre tipos PostgreSQL y Java

## 1. Conexión a PostgreSQL
```java
String url = "jdbc:postgresql://daw.paucasesnovescifp.cat:5432/usuaridb?user=usuari&password=seCret_25";
try (Connection con = DriverManager.getConnection(url)) {
    // Operaciones con la BD
}
```

## 2. Manejo de tipos Boolean

### Recuperar valores boolean
```java
ResultSet rs = stmt.executeQuery("SELECT recomanaria FROM proves.\"Clients\"");
while (rs.next()) {
    boolean recomienda = rs.getBoolean("recomanaria");
}
```

### Insertar/actualizar valores boolean
```java
PreparedStatement pstmt = con.prepareStatement(
    "UPDATE proves.\"Clients\" SET recomanaria=? WHERE id=?");
pstmt.setBoolean(1, true);
pstmt.setInt(2, 5);
pstmt.executeUpdate();
```

## 3. Manejo de Arrays

### Recuperar arrays desde PostgreSQL
```java
ResultSet rs = stmt.executeQuery("SELECT emails FROM proves.\"Clients\"");
while (rs.next()) {
    Array sqlArray = rs.getArray("emails");
    String[] emails = (String[]) sqlArray.getArray();
    sqlArray.free(); // Liberar recursos
}
```

### Insertar arrays en PostgreSQL
```java
// Método 1: Usando Statement (menos seguro)
stmt.executeUpdate(
    "INSERT INTO proves.\"Clients\" VALUES(5, 'Nombre', '{\"email1@test.com\",\"email2@test.com\"}')");

// Método 2: Usando PreparedStatement (recomendado)
String[] emailsArray = {"email1@test.com", "email2@test.com"};
Array emails = con.createArrayOf("VARCHAR", emailsArray);

PreparedStatement pstmt = con.prepareStatement(
    "INSERT INTO proves.\"Clients\"(id, nombre, emails) VALUES(?, ?, ?)");
pstmt.setInt(1, 5);
pstmt.setString(2, "Nombre");
pstmt.setArray(3, emails);
pstmt.executeUpdate();
```

## 4. Manejo de Tipos Definidos por Usuario

### POJO para tipos personalizados
```java
public class Telefon implements PGobject {
    public static final String sqlType = "\"proves\":\"t_telefon\"";
    
    private String tipus;
    private String numero;
    
    // Constructor, getters y setters
    
    @Override
    public void setValue(String value) {
        // Parsear cadena (tipo,numero)
        String[] parts = value.substring(1, value.length()-1).split(",");
        this.tipus = parts[0].replace("\"", "");
        this.numero = parts[1].replace("\"", "");
    }
    
    @Override
    public String getValue() {
        return String.format("(\"%s\",\"%s\")", tipus, numero);
    }
    
    // Otros métodos requeridos por PGobject
}
```

### Configuración y uso

#### Registrar tipo personalizado
```java
PGConnection pgCon = (PGConnection) con;
pgCon.addDataType(Telefon.sqlType, Telefon.class);
```

#### Recuperar objetos personalizados
```java
PreparedStatement pstmt = con.prepareStatement(
    "SELECT telefon FROM proves.\"Clients\" WHERE id=?");
pstmt.setInt(1, 5);

ResultSet rs = pstmt.executeQuery();
if (rs.next()) {
    Telefon telefon = (Telefon) rs.getObject("telefon");
}
```

#### Insertar/actualizar objetos personalizados
```java
Telefon nuevoTel = new Telefon("Móvil", "666112233");

PreparedStatement pstmt = con.prepareStatement(
    "UPDATE proves.\"Clients\" SET telefon=? WHERE id=?");
pstmt.setObject(1, nuevoTel);
pstmt.setInt(2, 5);
pstmt.executeUpdate();
```

## Buenas prácticas

1. **Siempre usar PreparedStatement** para evitar inyección SQL
2. **Liberar recursos** (Array.free()) cuando ya no se necesiten
3. **Manejar correctamente los tipos PGobject**:
   - Implementar todos los métodos requeridos
   - Registrar tipos antes de usarlos
4. **Usar try-with-resources** para manejo automático de cierre
5. **Validar datos** antes de conversiones

## Ejemplo completo
```java
public class PostgreSQLJDBCExample {
    public static void main(String[] args) {
        String url = "jdbc:postgresql://localhost:5432/mydb?user=postgres&password=secret";
        
        try (Connection con = DriverManager.getConnection(url)) {
            // Registrar tipo personalizado
            PGConnection pgCon = (PGConnection) con;
            pgCon.addDataType(Telefon.sqlType, Telefon.class);
            
            // Insertar cliente con array y tipo personalizado
            String[] emails = {"cliente@test.com", "cliente@work.com"};
            Array sqlArray = con.createArrayOf("VARCHAR", emails);
            Telefon tel = new Telefon("Trabajo", "934455667");
            
            PreparedStatement pstmt = con.prepareStatement(
                "INSERT INTO proves.\"Clients\"(nombre, emails, telefon) VALUES(?,?,?)");
            pstmt.setString(1, "Cliente Ejemplo");
            pstmt.setArray(2, sqlArray);
            pstmt.setObject(3, tel);
            pstmt.executeUpdate();
            
            // Recuperar datos
            pstmt = con.prepareStatement(
                "SELECT nombre, emails, telefon FROM proves.\"Clients\" WHERE nombre=?");
            pstmt.setString(1, "Cliente Ejemplo");
            
            ResultSet rs = pstmt.executeQuery();
            while (rs.next()) {
                String nombre = rs.getString("nombre");
                Array emailsRec = rs.getArray("emails");
                Telefon telefon = (Telefon) rs.getObject("telefon");
                
                System.out.println(nombre + " - " + telefon.getNumero());
                emailsRec.free();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
```