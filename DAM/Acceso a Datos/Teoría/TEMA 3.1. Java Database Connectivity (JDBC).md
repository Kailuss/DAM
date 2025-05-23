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

# **TEMA 3.1.** <br>Java Database Connectivity (JDBC)

## 1. Java ↔ Bases de datos  

Java, como la mayoría de lenguajes de programación, no incorpora directamente mecanismos para conectarse a bases de datos. Si queremos hacerlo necesitamos unas bibliotecas especializadas, llamadas drivers o conectores, que normalmente proporciona el desarrollador de la base de datos.  

Estos *drivers* deben incluirse en nuestra aplicación.  

Cada desarrollador de bases de datos tiene libertad absoluta para diseñar su conector: clases, métodos, etc.  

Si queremos que nuestra aplicación utilice una determinada base de datos, tendremos que aprender a usar su conector.

![](../../../_Media/Imágenes/AD/JDBC-Drivers.png)

Y si después de un tiempo necesitamos cambiar de base de datos, tendremos que aprender cómo funciona el nuevo conector y rehacer todo lo necesario de nuestra aplicación.  

**Afortunadamente hay una solución: JDBC.**  

## 2. Java Database Connectivity  

**JDBC es una API de Java que facilita la tarea de conectar nuestra aplicación con una base de datos.**  

Esta API actúa como puente, como interfaz, entre nuestra aplicación y el driver de la base de datos que estamos utilizando, de manera que nuestra aplicación no tendrá que interactuar en ningún momento con el *driver* de la base de datos, solo utilizará la API JDBC.  

La gran mayoría de bases de datos relacionales tienen su driver adaptado para funcionar con JDBC.  

De esta manera, el desarrollador de aplicaciones solo tiene que aprender a utilizar JDBC y podrá acceder a prácticamente cualquier base de datos relacional.  

Si cambiamos de base de datos, como mucho tendremos que modificar alguna sentencia SQL, pero en general la aplicación no tendrá que modificarse.  

La API JDBC está incluida en Java, solo tendremos que añadir a la aplicación el driver de la base de datos.  

## 3. Esquema de uso  

Para utilizar esta API siempre seguiremos la misma secuencia:  

1. Instalar el controlador.  
2. Obtener una conexión con la base de datos.  
3. Crear una sentencia con el SQL que queremos ejecutar y ejecutarla.  
4. Si se trata de una consulta:  
   - Tratar las distintas filas que nos devuelve la consulta una a una.  
5. Liberar todos los recursos.  

Todas las clases que utilizaremos serán de los paquetes `java.sql` y `javax.sql`.  

### 3.1. **Instalar el controlador  **

1. Aunque pueda parecer obvio, lo primero que debemos hacer es conseguir el controlador *JDBC* para la base de datos con la que queremos trabajar. Normalmente lo podremos encontrar en la web del desarrollador de la base de datos. O lo podemos instalar utilizando Maven, Gradle, etc.  

2. Guardamos el controlador en un directorio de nuestro ordenador, si está comprimido lo descomprimimos. Normalmente el controlador JDBC estará dentro de un archivo JAR.  

3. Añadimos el JAR al classpath de la aplicación, nunca debemos añadir el .zip. En NetBeans o Eclipse será suficiente con añadir el JAR o la carpeta a las librerías del proyecto.  

### 3.2. **Obtener una conexión con la base de datos  **

Para obtener una conexión debemos utilizar el método estático `getConnection` de la clase `DriverManager`. Nos devolverá un objeto de la clase `Connection` a partir del cual podremos trabajar con la base de datos.  

La URL dependerá de cada DBMS, hay que consultar la documentación. Por ejemplo:  

- MySQL: `jdbc:mysql://<servidor>[<puerto>]/<base de datos>?parámetros`  
  Ejemplo: `jdbc:mysql://localhost:3306/aspirantes?user=usuario&password=secreto`  

- Oracle: `jdbc:oracle:thin:@//[HOST][:PORT]/SERVICE`  
  Ejemplo: `jdbc:oracle:thin:@//localhost:1521/Oracle?user=usuario&password=secreto`  

Otras versiones de este método son:  

```java
Connection con = DriverManager.getConnection(url, user, password);
Connection con = DriverManager.getConnection(url, propiedades);
// donde propiedades es un objeto de la clase Properties, similar a un
// HashMap donde clave y valor son String. Si hay muchos elementos en el query string
// conviene utilizarlo.
```  

### 3.3. **Crear una sentencia con el SQL que queremos ejecutar y ejecutarla  **

Para ejecutar una sentencia SQL lo primero que debemos hacer es crear un objeto `Statement` a partir de la conexión establecida en el punto anterior.  

```java
Statement st = con.createStatement();
```  

El siguiente paso depende del tipo de sentencia SQL que queremos ejecutar. Si se trata de una consulta:  

```java
ResultSet rs = st.executeQuery("SELECT * FROM empleados");
```  

Este método ejecuta el `SELECT` en la base de datos y nos devuelve un objeto `ResultSet`, un cursor. Si lo que queremos es ejecutar una instrucción `INSERT`, `DELETE`, `UPDATE` o una DDL:  

```java
int filasAfectadas = st.executeUpdate("DELETE FROM empleados");
```  

Nos devuelve el número de filas afectadas o cero si se trata de instrucciones DDL como `CREATE TABLE`.  

**Las sentencias SQL deben ser válidas para el DBMS donde las ejecutamos, de forma que si cambiamos de DBMS seguramente tendremos que retocar algunas de estas sentencias.**  

### 3.4. **Tratar las filas devueltas por la consulta  **

Si hemos ejecutado una consulta `SELECT`, habremos recogido el resultado dentro de un objeto `ResultSet`. Podemos ver este objeto como un cursor de PL.  

El `executeQuery` devuelve el `ResultSet` situado antes de la primera fila, exactamente igual que un cursor. Para acceder a la siguiente fila debemos ejecutar el método `next`, que devuelve `false` cuando ha llegado al final de la consulta.  

```java
while (rs.next()) { // ejecutará el while mientras queden filas
```  

Una vez situado el `ResultSet` en la fila, debemos recuperar las columnas una a una. Para hacerlo debemos saber el tipo de cada columna y su nombre o la posición que ocupa dentro del `SELECT` (la primera posición es 1). Por ejemplo, si hemos ejecutado la consulta:  

```sql
SELECT codigo, CONCAT(apellidos, ", ", nombre) AS nombre_completo FROM EMPLEADOS
```  

Podemos recuperar los datos de la siguiente manera:  

```java
int codigo = rs.getInt(1); // Posición del campo dentro de la cláusula SELECT
int codigo = rs.getInt("codigo"); // Nombre o alias del campo
String nombre = rs.getString(2); // Posición del campo dentro de la cláusula SELECT
String nombre = rs.getString("nombre_completo"); // Nombre o alias del campo
```  

### 3.5. **Cerrar los recursos abiertos  **

Al terminar de utilizar un objeto `ResultSet`, `Statement` o `Connection`, deberíamos cerrarlo para así liberar los recursos que utilizan.  

Todos estos objetos tienen un método `close()` que libera los recursos:  

```java
if (rs != null) rs.close();
if (st != null) st.close();
if (con != null) con.close();
```  

Al cerrar un `Statement` se cerrarán todos los `ResultSet` que dependen de él.  
Al cerrar una `Connection` se cerrarán todos los `Statement` que dependen de ella.  
Aun así, es mejor cerrarlos manualmente uno a uno cuando terminemos de usarlos.  

Los métodos `close()` de estos objetos también lanzan una excepción `SQLException`.  

**Las clases `Connection`, `Statement` y `ResultSet` implementan la interfaz `AutoCloseable`. Esto significa que se pueden utilizar con el try-with-resources.**  

### 3.6. **Paréntesis: try-with-resources  **

Esta variante del `try` declara recursos, objetos que el programa debe cerrar cuando ya no los necesite más. Se asegura que los objetos declarados se cierren, tanto si el bloque de código del `try` lanza excepciones como si no.  

Se pueden utilizar como recursos cualquier objeto que implemente la interfaz `AutoCloseable`. Disponible a partir de Java 7.  

```java
try (Connection con = DriverManager.getConnection(url);
     Statement st = con.createStatement();
     ResultSet rs = st.executeQuery("SELECT * FROM empleados");) {
    while (rs.next()) {
        System.out.println(rs.getInt(1));
    }
}
```  

Evidentemente, pueden haber tantos bloques `catch` como sean necesarios. Antes de ejecutarse, sin embargo, se cerrarán los recursos declarados en el `try`.  

## 4. Clases de JDBC  

Las clases más habituales de JDBC son las siguientes.  

### 4.1. **Connection  **

Este objeto representa la conexión con la base de datos. Nos permite, entre otras cosas:  

- Crear objetos como:  
  - `Statement`,  
  - `PreparedStatement`,  
  - `CallableStatement`, etc.  
- Controlar las transacciones:  
  - `setAutoCommit`: establece si se hace un `commit` después de cada instrucción o no. Por defecto está en `true`.  
  - `commit`: realiza un `commit`.  
  - `rollback`: realiza un `rollback`, completo o hasta un `savePoint`.  
  - `savePoint`: establece un `savePoint` con nombre o sin nombre, `setSavePoint`, `releaseSavePoint`.  

### 4.2. **Statement  **

Este objeto representa una sentencia SQL. Se crea a partir de `Connection`:  

```java
Statement st = con.createStatement();
```  

Para ejecutar sentencias SQL en la base de datos, `Statement` nos proporciona los siguientes métodos:  

- **`executeQuery("SELECT")`.** Ejecuta consultas `SELECT`. Devuelve un objeto `ResultSet` con el cual podemos recorrer los resultados.  
- **`executeUpdate("INSERT")`.** Permite ejecutar cualquier tipo de sentencia SQL que no sea `SELECT`. Devuelve un entero que indica las filas afectadas si se trata de un `INSERT`, `UPDATE` o `DELETE`, o cero si es otra sentencia.  

### 4.3. **ResultSet  **

Representa el cursor devuelto por un método `Statement.executeQuery`. Sus características dependerán en buena medida de los parámetros que se hayan utilizado al crear el `Statement`.  

Inicialmente, el cursor está posicionado antes de la primera fila. Una buena manera de recorrer el cursor es:  

```java
while (rs.next()) {
    int codigo = rs.getInt("identificador");
    ...
}
```  

`rs.next()` devuelve `false` al llegar al final del cursor. Para cada fila, debemos recuperar los distintos campos con un método `getXxx()`, donde `Xxx` es el tipo de la columna. Podemos recuperarlo poniendo el nombre de la columna o la posición que ocupa dentro de la lista de columnas devueltas por la consulta (peligroso si se modifica esta lista).  

### 4.4. **PreparedStatement  **

Si tenemos que repetir la misma sentencia SQL varias veces con valores diferentes, podemos utilizar este objeto. La base de datos pre-compilará la sentencia y, por cada ejecución, solo tendrá que cambiar los parámetros, con lo que el rendimiento será mejor.  

De paso, hacemos que el **código sea menos vulnerable a ataques de inyección de código.** Por tanto, siempre que tengamos que incluir en la sentencia datos recibidos del usuario, es aconsejable utilizar un `PreparedStatement`.  

Al definir la cadena que contiene la sentencia SQL, debemos poner un `?` donde irá cada uno de los parámetros:  

```java
String actualizaSalarios = "UPDATE empleados SET salario=? WHERE codigoEmpleado=?";
```  

Luego creamos el objeto a partir de `Connection`:  

```java
PreparedStatement sueldos = con.prepareStatement(actualizaSalarios);
```  

En este momento ya tenemos la sentencia pre-compilada en el DBMS. Para utilizarla, debemos asignar valores a los parámetros:  

```java
sueldos.setDouble(1, 956.32); // Sustituirá el primer ? de la cadena por 956.32
sueldos.setInt(2, 2345); // Sustituirá el segundo ? de la cadena por 2345
int n = sueldos.executeUpdate(); // Ejecuta la sentencia con los valores proporcionados.
```  

### 4.5. **SQLException  **

Cuando JDBC encuentra un error durante su interacción con el DBMS, lanza una excepción del tipo `SQLException` que contiene:  

- La descripción del error. Se puede recuperar con `SQLException.getMessage()`.  
- `SQLStateCode`. Una cadena de cinco caracteres alfanuméricos que han sido estandarizados. Se recupera con `SQLException.getSQLState()`.  
- El código de error. Depende de la implementación del driver y debería ser el mismo que muestra el DBMS, el típico `ORA-8234`. Se recupera con `SQLException.getErrorCode()`.  

**Advertencias**  

Una advertencia es un error no lo suficientemente grave para detener el programa, alerta al usuario de que algo no ha ido tan bien como debería. Los objetos `Connection`, `Statement`, `ResultSet`, etc., pueden devolver advertencias. Las recuperamos así:  

```java
SQLWarning warning = stmt.getWarning(); // Recupera la primera advertencia
warning = warning.getNextWarning(); // Recupera la siguiente o null
```  

## 5. Transacciones  

De manera informal, podríamos definir una transacción como un conjunto de sentencias SQL que se deben ejecutar todas o ninguna. Por ejemplo, para hacer una transferencia bancaria, debemos restar dinero al que paga y sumárselo al que cobra. No puede ser que solo hagamos una de las dos.  

Por defecto, JDBC hace un `commit` después de cada sentencia. Para evitarlo, debemos cambiar:  

```java
con.setAutoCommit(false);
```  

Luego podremos utilizar:  

```java
con.commit(); // Guarda la transacción
con.rollback(); // Revierte la transacción
```  

También podemos utilizar `savepoints`:  

```java
SavePoint punto1 = con.setSavePoint();
con.rollback(punto1);
con.releaseSavePoint(punto1); // Anula el punto
```  

Por ejemplo, queremos insertar una nueva nacionalidad en la base de datos y una serie de autores asociados a esta nueva nacionalidad. Evidentemente, si falla la nacionalidad, no podremos insertar los autores:  

```java
try (Connection con = DriverManager.getConnection(url, propiedades);
     PreparedStatement stNacionalidad = con.prepareStatement("INSERT INTO NACIONALIDADES VALUES(?)");
     PreparedStatement stAutores = con.prepareStatement("INSERT INTO AUTORES(id_AUT, NOM_AUT, FK_NACIONALIDAD) VALUES (?, ?, ?)")) {
    con.setAutoCommit(false); // No puede estar dentro del try(). Eliminamos el autocommit

    try {
        // Asignamos valor al parámetro
        stNacionalidad.setString(1, nacionalidad.getNacionalidad());

        // Insertamos en la tabla nacionalidades
        stNacionalidad.executeUpdate();

        // Insertamos los autores asociados a la nueva nacionalidad
        for (Autor autor : autores) {
            stAutores.setInt(1, autor.getIdAutor());
            stAutores.setString(2, autor.getNombreAutor());
            stAutores.setString(3, autor.getNacionalidad().getNacionalidad());
            stAutores.executeUpdate();
        }

        // Si llegamos aquí, todo ha ido bien, podemos hacer el commit
        con.commit();

    } catch (SQLException e) {
        // Revertimos la transacción
        con.rollback();

        // Ya hemos capturado la SQLException y no seguirá propagándose
        // Si queremos avisar del error, debemos lanzar una nueva excepción
        throw new JDBCException("Transacción con errores. Rollback.");
    }
}
```  

Si todo va bien, al terminar de insertar los autores llegaremos a ejecutar el `commit`. En cambio, si hay un error, no se llegará al `commit`, entrará en el `catch` y ejecutará el `rollback`.  

## 6. VO, DO, DTO, POJO  

Siguiendo las características de encapsulación de los lenguajes orientados a objetos, cuando una aplicación Java debe acceder a una base de datos, suele delegar todo lo relacionado con ella a una o varias clases, que se dedican exclusivamente a interactuar con la base de datos, mientras que el tratamiento de datos, la interacción con el usuario, etc., se deja a otras clases.  

Para transferir la información entre las clases de bases de datos y las demás, se suelen crear objetos que solo tienen los atributos necesarios, los getters y setters (no siempre) de estos atributos y un constructor completo. Los métodos que interactúan con la base de datos suelen devolver, o recibir como parámetros, objetos o colecciones de objetos de este tipo.  

Aunque no sean exactamente lo mismo, podemos decir que los siguientes nombres hacen referencia al mismo concepto:  

- **VO (Value Object), DO (Data Object).** En principio son inmutables, no cambian.  
- **DTO (Data Transfer Object).** Pensados para transferir datos entre aplicaciones, son serializables.  
- **POJO (Plain Old Java Object).** Cualquier objeto Java sin ningún requerimiento especial: implementación de interfaces, descendencia de una superclase concreta, etc.  

Un ejemplo de clase de este tipo podría ser el siguiente:  

La clase `Localidad` tiene tres atributos, un constructor que recibe como parámetros los valores de estos atributos, y los getters necesarios para recuperar sus valores.  

Como se supone que los datos no se modificarán, no se han programado los setters.  

La clase tampoco dispone de ningún método adicional, su único objetivo es mantener la información del objeto.  

```java
public class Localidad {
    private String codigoLocalidad;
    private String nombreLocalidad;
    private String codigoIsla;

    public Localidad(String codigoLocalidad, String nombreLocalidad, String codigoIsla) {
        this.codigoLocalidad = codigoLocalidad;
        this.nombreLocalidad = nombreLocalidad.replace("\"", "");
        this.codigoIsla = codigoIsla;
    }

    public String getNombreLocalidad() {
        return nombreLocalidad;
    }

    public String getCodigoLocalidad() {
        return codigoLocalidad;
    }

    public String getCodigoIsla() {
        return codigoIsla;
    }
}
```  

## 7. Java Records  

Los Java Records, presentes desde la versión 17 de Java, permiten definir de manera muy sencilla estructuras para mantener datos inmutables, es decir, que no pueden cambiar.  

Pueden ser una buena alternativa a los POJOs si solo los vamos a utilizar para recoger la información de la base de datos o pasarla hacia la base de datos.  

En su versión más sencilla, un record se define poniendo como parámetros los atributos que queremos que tenga. Automáticamente se creará el constructor canónico (con parámetros para todos los atributos), métodos con el nombre de los atributos para acceder a sus valores, el `toString`, y el `equals` y el `hashCode`.  

El siguiente record sería el equivalente al POJO `Localidad` del ejemplo anterior:  

```java
public record Localidad(String codigoLocalidad, String nombreLocalidad, String codigoIsla) {}
```  

Sin escribir más código, tendremos los siguientes métodos y constructores:  

```java
public Localidad(String codigoLocalidad, String nombreLocalidad, String codigoIsla);
public final String toString();
public final int hashCode();
public final boolean equals(Object o);
public String codigoLocalidad();
public String nombreLocalidad();
public String codigoIsla();
```  

## 8. Procedimientos almacenados  

Un procedimiento almacenado es un procedimiento de la base de datos, por ejemplo, un procedimiento PL/SQL o un método Java almacenado en la base de datos.  

La clase que representa un procedimiento almacenado es `CallableStatement`. Su utilización es muy similar a la de un `PreparedStatement`.  

Por ejemplo, si queremos llamar a un procedimiento sin parámetros llamado `get_nacionalidades`:  

```java
try (Connection con = DriverManager.getConnection(url, propiedades);
     CallableStatement cs = con.prepareCall("{call get_nacionalidades()}");
     ResultSet rs = cs.executeQuery();) {
    while (rs.next()) {
        System.out.println(rs.getString(1));
    }
} catch (SQLException ex) {
    System.out.println("Error: " + ex.getMessage());
}
```  

El procedimiento nos devuelve un `ResultSet`. A partir de aquí, el tratamiento es exactamente el mismo que haríamos cuando ejecutamos un `Statement` o un `PreparedStatement`.  

En cambio, si el procedimiento que queremos ejecutar tiene parámetros, tendremos que seguir más o menos el mismo procedimiento que con `PreparedStatement`: Poner interrogantes en el lugar del parámetro y asignarle un valor.  

En los procedimientos almacenados, podemos definir los parámetros como:  

- De entrada (enviamos información al procedimiento).  
- De salida (utilizamos el parámetro para obtener información del procedimiento).  

Para llamar a un procedimiento que tiene un parámetro de entrada, lo haremos como con los `PreparedStatement`:  

```java
try (Connection con = DriverManager.getConnection(url, propiedades);
     CallableStatement cs = con.prepareCall("{call get_nacionalidades_por_nombre(?)}");
     cs.setString(1, parte);
     try (ResultSet rs = cs.executeQuery();) {
        while (rs.next()) {
            System.out.println(rs.getString(1));
        }
    }
} catch (SQLException ex) {
    System.out.println("Error: " + ex.getMessage());
}
```  

Si el procedimiento tiene un parámetro de salida, tendremos que registrar el tipo de este parámetro con el método `registerOutParameter`:  

```java
try (Connection con = DriverManager.getConnection(url, propiedades);
     CallableStatement cs = con.prepareCall("{call get_nacionalidades_por_nombre_cantidad(?,?)}");
     cs.setString(1, parte);
     cs.registerOutParameter(2, Types.INTEGER);
     cs.executeQuery();
     int cuenta = cs.getInt(2);
     System.out.println("cuenta = " + cuenta);
} catch (SQLException ex) {
    System.out.println("Error: " + ex.getMessage());
}
```  

Recuperaremos el parámetro de salida como si fuera una columna del `ResultSet`, con el método `getXXX()` del `CallableStatement`, donde `XXX` depende del tipo de los datos.  

Finalmente, hay procedimientos que, además de devolver un valor al parámetro de salida, también devuelven un `ResultSet`. En este caso, el tratamiento será la combinación de los dos anteriores:  

```java
try (Connection con = DriverManager.getConnection(url, propiedades);
     CallableStatement cs = con.prepareCall("{call get_nacionalidades_por_nombre_cantidadV2(?,?)}");) {
    cs.setString(1, parte);
    cs.registerOutParameter(2, Types.INTEGER);
    try (ResultSet rs = cs.executeQuery();) {
        while (rs.next()) {
            System.out.println(rs.getString(1));
        }
        int cuenta = cs.getInt(2);
        System.out.println("cuenta = " + cuenta);
    }
} catch (SQLException ex) {
    System.out.println("Error: " + ex.getMessage());
}
```
