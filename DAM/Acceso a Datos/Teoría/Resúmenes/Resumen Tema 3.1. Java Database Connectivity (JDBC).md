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
# **Resumen Tema 3.1.** <br>Java Database Connectivity (JDBC)

## 1. Conceptos clave
- **JDBC.** API de Java para conectar aplicaciones con bases de datos relacionales
- **Driver.** Componente específico para cada base de datos que implementa JDBC
- **Ventaja principal.** Permite cambiar de DBMS con mínimas modificaciones

## 2. Esquema básico de uso
1. **Instalar el controlador.** Añadir el JAR al classpath
2. **Obtener conexión.** 

```java
Connection con = DriverManager.getConnection(
  "jdbc:mysql://localhost:3306/bd?user=usr&password=pwd");
```

3. **Crear y ejecutar sentencia.**

```java
Statement st = con.createStatement();
ResultSet rs = st.executeQuery("SELECT * FROM empleados");
```

4. **Procesar resultados.**

```java
while(rs.next()) {
  int id = rs.getInt("id");
  String nombre = rs.getString("nombre");
}
```

5. **Cerrar recursos.**

```java
rs.close(); 
st.close(); 
con.close();
```

## 3. Clases principales

### 3.1. **Connection**
- Representa la conexión con la BD
- Métodos clave:

```java
con.setAutoCommit(false); // Para transacciones
con.commit();
con.rollback();
```

### 3.2. **Statement**
- Para ejecutar SQL estático:

```java
Statement st = con.createStatement();
int filas = st.executeUpdate("DELETE FROM productos");
```

### 3.3. **PreparedStatement**
- SQL parametrizado (mejor rendimiento y seguridad):

```java
PreparedStatement ps = con.prepareStatement(
  "INSERT INTO clientes VALUES (?, ?)");
ps.setInt(1, 101);
ps.setString(2, "Ana");
ps.executeUpdate();
```

### 3.4. **ResultSet**
- Contiene resultados de consultas:

```java
ResultSet rs = st.executeQuery("SELECT * FROM pedidos");
while(rs.next()) {
  Date fecha = rs.getDate("fecha_pedido");
}
```

## 4. Transacciones

Ejemplo completo:

```java
try {
  con.setAutoCommit(false);
  
  // Operación 1
  PreparedStatement ps1 = con.prepareStatement(
    "UPDATE cuentas SET saldo = saldo - ? WHERE id = ?");
  ps1.setDouble(1, 100.0);
  ps1.setInt(2, 123);
  ps1.executeUpdate();
  
  // Operación 2
  PreparedStatement ps2 = con.prepareStatement(
    "UPDATE cuentas SET saldo = saldo + ? WHERE id = ?");
  ps2.setDouble(1, 100.0);
  ps2.setInt(2, 456);
  ps2.executeUpdate();
  
  con.commit();
} catch(SQLException e) {
  con.rollback();
  throw new JDBCException("Error en transacción");
}
```

## 5. Procedimientos almacenados

```java
try (CallableStatement cs = con.prepareCall("{call obtener_clientes(?)}")) {
  cs.setString(1, "Madrid");
  ResultSet rs = cs.executeQuery();
  // Procesar resultados
}
```

## 6. Patrones de datos
- **POJO/DTO.** Clases simples para transferencia de datos
- **Record** (Java 17+):

```java
public record Empleado(int id, String nombre, double salario) {}
```

## 7. Buenas prácticas
- Usar siempre try-with-resources
- Utilizar PreparedStatement para evitar inyección SQL
- Cerrar recursos en orden inverso a su apertura
- Manejar adecuadamente las transacciones

## 8. Manejo de excepciones
- **SQLException.** Contiene:
  - Mensaje de error `getMessage()`
  - Código SQLState `getSQLState()`
  - Código específico del vendor `getErrorCode()`
