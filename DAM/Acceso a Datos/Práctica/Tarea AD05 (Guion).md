---
tags: [AD, DAM]
cssclasses:
  - dam-ad
  - table-compact-clean
banner: "![[ad.jpg]]"
banner_y: 0.32
number headings: off
---

# Tarea **AD05**

## Parte 1: Script SQL

Primero, creemos el script SQL para las operaciones de la base de datos:

```sql
-- 1. Crear un nuevo esquema
CREATE SCHEMA "ut5-practica";

-- Asegurarnos de usar el esquema
SET search_path TO "ut5-practica";

-- 2. Ejercicio 1: Crear tipo de datos personalizado
CREATE TYPE "ut5-practica".tipo_conexion AS (  
    sgbd VARCHAR(50),  
    ip_dominio VARCHAR(100),  
    puerto INTEGER  
);

-- Crear la tabla servidors
CREATE TABLE "ut5-practica".servidores (  
    codigo VARCHAR(20) PRIMARY KEY,  
    nombre VARCHAR(100) NOT NULL,  
    usuarios_permitidos VARCHAR(50)[] NOT NULL,  
    activo BOOLEAN NOT NULL,  
    conexion "ut5-practica".tipo_conexion NOT NULL  
);

-- Ejercicio 2: Insertar y modificar datos

-- 1. Insertar tres servidores con datos completos
INSERT INTO "ut5-practica".servidores VALUES (  
    'S001', 'Servidor Principal',  
    ARRAY['admin', 'usuario1', 'usuario2'], true,  
    ('PostgreSQL', '192.168.1.100', 5432)::"ut5-practica".tipo_conexion  
);  
  
INSERT INTO "ut5-practica".servidores VALUES (  
    'S002',  
    'Servidor Pruebas',  
    ARRAY['admin', 'usuario3'], true,  
    ('MySQL', '192.168.1.101', 3306)::"ut5-practica".tipo_conexion  
);  
  
INSERT INTO "ut5-practica".servidores VALUES (  
    'S003', 'Servidor Respaldo',  
    ARRAY['admin'], false,  
    ('Oracle', '192.168.1.102', 1521)::"ut5-practica".tipo_conexion  
);

-- 2. Añadir un nuevo usuario a un servidor
UPDATE "ut5-practica".servidores 
SET usuarios = array_append(usuarios, 'user055')
WHERE codigo = 'S001';

-- 3. Modificar un nombre de usuario en un servidor
UPDATE "ut5-practica".servidores 
SET usuarios = array_replace(usuarios, 'tester003', 'tester064')
WHERE codigo = 'SRV002';

-- 4. Cambiar el puerto de conexión de un servidor
UPDATE "ut5-practica".servidores 
SET conexion.puerto = 1522
WHERE codigo = 'S003';

-- Consulta para verificar los cambios
SELECT * FROM servidores;
```

## Parte 2: Proyecto ut5-practica-component

Creemos el proyecto de componentes con POJOs y operaciones de base de datos:

### Clase POJO

```java
package com.ut5.model;

import java.util.Arrays;
import java.util.Objects;

public class Servidor {
    private String codigo;
    private String nombre;
    private String[] usuarios;
    private boolean activo;
    private DbConnection conexion;

    public Servidor() {
    }

    public Servidor(String codigo, String nombre, String[] usuarios, boolean activo, DbConnection conexion) {
        setCodigo(codigo);
        setNombre(nombre);
        setUsuarios(usuarios);
        this.activo = activo;
        setConexion(conexion);
    }

    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        if (codigo == null || codigo.trim().isEmpty()) {
            throw new IllegalArgumentException("El código no puede ser nulo o vacío");
        }
        if (codigo.length() > 20) {
            throw new IllegalArgumentException("El código no puede tener más de 20 caracteres");
        }
        this.codigo = codigo;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        if (nombre == null || nombre.trim().isEmpty()) {
            throw new IllegalArgumentException("El nombre no puede ser nulo o vacío");
        }
        if (nombre.length() > 100) {
            throw new IllegalArgumentException("El nombre no puede tener más de 100 caracteres");
        }
        this.nombre = nombre;
    }

    public String[] getUsuarios() {
        return usuarios;
    }

    public void setUsuarios(String[] usuarios) {
        if (usuarios == null || usuarios.length == 0) {
            throw new IllegalArgumentException("Debe haber al menos un usuario");
        }
        this.usuarios = usuarios;
    }

    public boolean isActivo() {
        return activo;
    }

    public void setActivo(boolean activo) {
        this.activo = activo;
    }

    public DbConnection getConexion() {
        return conexion;
    }

    public void setConexion(DbConnection conexion) {
        if (conexion == null) {
            throw new IllegalArgumentException("La conexión no puede ser nula");
        }
        this.conexion = conexion;
    }

    @Override
    public String toString() {
        return "Servidor{" +
                "codigo='" + codigo + '\'' +
                ", nombre='" + nombre + '\'' +
                ", usuarios=" + Arrays.toString(usuarios) +
                ", activo=" + activo +
                ", conexion=" + conexion +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Servidor servidor = (Servidor) o;
        return codigo.equals(servidor.codigo);
    }

    @Override
    public int hashCode() {
        return Objects.hash(codigo);
    }
}
```

### Clase DbConnection

```java
package com.ut5.model;

import java.util.Objects;

public class DbConnection {
    private String sgbd;
    private String ipDominio;
    private int puerto;

    public DbConnection() {
    }

    public DbConnection(String sgbd, String ipDominio, int puerto) {
        setSgbd(sgbd);
        setIpDominio(ipDominio);
        setPuerto(puerto);
    }

    public String getSgbd() {
        return sgbd;
    }

    public void setSgbd(String sgbd) {
        if (sgbd == null || sgbd.trim().isEmpty()) {
            throw new IllegalArgumentException("El SGBD no puede ser nulo o vacío");
        }
        if (sgbd.length() > 50) {
            throw new IllegalArgumentException("El SGBD no puede tener más de 50 caracteres");
        }
        this.sgbd = sgbd;
    }

    public String getIpDominio() {
        return ipDominio;
    }

    public void setIpDominio(String ipDominio) {
        if (ipDominio == null || ipDominio.trim().isEmpty()) {
            throw new IllegalArgumentException("La IP o dominio no puede ser nulo o vacío");
        }
        if (ipDominio.length() > 255) {
            throw new IllegalArgumentException("La IP o dominio no puede tener más de 255 caracteres");
        }
        this.ipDominio = ipDominio;
    }

    public int getPuerto() {
        return puerto;
    }

    public void setPuerto(int puerto) {
        if (puerto <= 0 || puerto > 65535) {
            throw new IllegalArgumentException("El puerto debe estar entre 1 y 65535");
        }
        this.puerto = puerto;
    }

    @Override
    public String toString() {
        return "DbConnection{" +
                "sgbd='" + sgbd + '\'' +
                ", ipDominio='" + ipDominio + '\'' +
                ", puerto=" + puerto +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        DbConnection that = (DbConnection) o;
        return puerto == that.puerto &&
                Objects.equals(sgbd, that.sgbd) &&
                Objects.equals(ipDominio, that.ipDominio);
    }

    @Override
    public int hashCode() {
        return Objects.hash(sgbd, ipDominio, puerto);
    }
}
```

### Clase Database Manager

```java
package com.ut5.dao;

import com.ut5.model.DbConnection;
import com.ut5.model.Servidor;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

public class ServidorDAO {
    private static final String URL = "jdbc:postgresql://localhost:5432/postgres";
    private static final String USER = "postgres";
    private static final String PASSWORD = "postgres";
    private static final String SCHEMA = "\"ut5-practica\"";

    private Connection getConnection() throws SQLException {
        Connection conn = DriverManager.getConnection(URL, USER, PASSWORD);
        conn.setSchema(SCHEMA);
        return conn;
    }

    /**
     * Recupera todos los servidores de la base de datos
     */
    public List<Servidor> getAllServidores() throws SQLException {
        List<Servidor> servidores = new ArrayList<>();
        String sql = "SELECT * FROM servidors";
        
        try (Connection conn = getConnection();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
            
            while (rs.next()) {
                servidores.add(mapResultSetToServidor(rs));
            }
        }
        
        return servidores;
    }

    /**
     * Recupera un servidor por su código
     */
    public Servidor getServidorByCodigo(String codigo) throws SQLException {
        String sql = "SELECT * FROM servidors WHERE codigo = ?";
        
        try (Connection conn = getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            
            pstmt.setString(1, codigo);
            
            try (ResultSet rs = pstmt.executeQuery()) {
                if (rs.next()) {
                    return mapResultSetToServidor(rs);
                } else {
                    return null;
                }
            }
        }
    }

    /**
     * Inserta un nuevo servidor
     */
    public boolean insertServidor(Servidor servidor) throws SQLException {
        String sql = "INSERT INTO servidors (codigo, nombre, usuarios, activo, conexion) " +
                     "VALUES (?, ?, ?, ?, ROW(?, ?, ?))";
        
        try (Connection conn = getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            
            pstmt.setString(1, servidor.getCodigo());
            pstmt.setString(2, servidor.getNombre());
            pstmt.setArray(3, conn.createArrayOf("varchar", servidor.getUsuarios()));
            pstmt.setBoolean(4, servidor.isActivo());
            pstmt.setString(5, servidor.getConexion().getSgbd());
            pstmt.setString(6, servidor.getConexion().getIpDominio());
            pstmt.setInt(7, servidor.getConexion().getPuerto());
            
            int affectedRows = pstmt.executeUpdate();
            return affectedRows > 0;
        }
    }

    /**
     * Elimina un usuario de un servidor
     */
    public boolean deleteUsuarioFromServidor(String codigo, String usuario) throws SQLException {
        String sql = "UPDATE servidors SET usuarios = array_remove(usuarios, ?) WHERE codigo = ?";
        
        try (Connection conn = getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            
            pstmt.setString(1, usuario);
            pstmt.setString(2, codigo);
            
            int affectedRows = pstmt.executeUpdate();
            return affectedRows > 0;
        }
    }

    /**
     * Modifica los datos de conexión de un servidor
     */
    public boolean updateConexionServidor(String codigo, DbConnection conexion) throws SQLException {
        String sql = "UPDATE servidors SET conexion = ROW(?, ?, ?) WHERE codigo = ?";
        
        try (Connection conn = getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            
            pstmt.setString(1, conexion.getSgbd());
            pstmt.setString(2, conexion.getIpDominio());
            pstmt.setInt(3, conexion.getPuerto());
            pstmt.setString(4, codigo);
            
            int affectedRows = pstmt.executeUpdate();
            return affectedRows > 0;
        }
    }

    /**
     * Helper method to map a ResultSet to a Servidor object
     */
    private Servidor mapResultSetToServidor(ResultSet rs) throws SQLException {
        String codigo = rs.getString("codigo");
        String nombre = rs.getString("nombre");
        
        // Get the array of usuarios
        Array usuariosArray = rs.getArray("usuarios");
        String[] usuarios = (String[]) usuariosArray.getArray();
        
        boolean activo = rs.getBoolean("activo");
        
        // Get the connection data from the composite type
        PGobject pgObject = (PGobject) rs.getObject("conexion");
        String connectionStr = pgObject.getValue();
        
        // Parse the connection string (format: (sgbd,ip_dominio,puerto))
        connectionStr = connectionStr.substring(1, connectionStr.length() - 1); // Remove parentheses
        String[] connectionParts = connectionStr.split(",");
        
        String sgbd = connectionParts[0];
        String ipDominio = connectionParts[1];
        int puerto = Integer.parseInt(connectionParts[2]);
        
        DbConnection conexion = new DbConnection(sgbd, ipDominio, puerto);
        
        return new Servidor(codigo, nombre, usuarios, activo, conexion);
    }
}
```

## Parte 3: Proyecto ut5-practica-consola

```java
package com.ut5.consola;

import com.ut5.dao.ServidorDAO;
import com.ut5.model.DbConnection;
import com.ut5.model.Servidor;

import java.sql.SQLException;
import java.util.List;

public class MainConsola {
    public static void main(String[] args) {
        ServidorDAO dao = new ServidorDAO();
        
        try {
            System.out.println("=== PROBANDO RECUPERAR TODOS LOS SERVIDORES ===");
            List<Servidor> servidores = dao.getAllServidores();
            for (Servidor srv : servidores) {
                System.out.println(srv);
            }
            
            System.out.println("\n=== PROBANDO RECUPERAR UN SERVIDOR POR CÓDIGO ===");
            Servidor servidor = dao.getServidorByCodigo("SRV001");
            if (servidor != null) {
                System.out.println("Servidor encontrado: " + servidor);
            } else {
                System.out.println("Servidor no encontrado");
            }
            
            System.out.println("\n=== PROBANDO INSERTAR UN NUEVO SERVIDOR ===");
            Servidor nuevoServidor = new Servidor(
                "SRV004",
                "Servidor MongoDB de Pruebas",
                new String[]{"mongo_admin", "db_test"},
                true,
                new DbConnection("MongoDB", "192.168.1.200", 27017)
            );
            
            boolean insertado = dao.insertServidor(nuevoServidor);
            System.out.println("Servidor insertado: " + insertado);
            
            System.out.println("\n=== PROBANDO ELIMINAR UN USUARIO DE UN SERVIDOR ===");
            boolean usuarioEliminado = dao.deleteUsuarioFromServidor("SRV002", "qa_tester");
            System.out.println("Usuario eliminado: " + usuarioEliminado);
            
            System.out.println("\n=== PROBANDO MODIFICAR DATOS DE CONEXIÓN ===");
            DbConnection nuevaConexion = new DbConnection("Oracle", "10.0.0.15", 1523);
            boolean conexionModificada = dao.updateConexionServidor("SRV003", nuevaConexion);
            System.out.println("Conexión modificada: " + conexionModificada);
            
            System.out.println("\n=== LISTADO FINAL DE SERVIDORES ===");
            servidores = dao.getAllServidores();
            for (Servidor srv : servidores) {
                System.out.println(srv);
            }
            
        } catch (SQLException e) {
            System.err.println("Error en la base de datos: " + e.getMessage());
            e.printStackTrace();
        } catch (IllegalArgumentException e) {
            System.err.println("Error en los datos: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("Error general: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
```

## Parte 4: Proyecto ut5-practica-gui

```java
package com.ut5.gui;

import com.ut5.dao.ServidorDAO;
import com.ut5.model.DbConnection;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.SQLException;

public class ServidorGUI extends JFrame {
    private JTextField txtCodigo;
    private JTextField txtSGBD;
    private JTextField txtIP;
    private JTextField txtPuerto;
    private JButton btnActualizar;
    private JLabel lblStatus;
    
    private ServidorDAO dao;
    
    public ServidorGUI() {
        dao = new ServidorDAO();
        initComponents();
    }
    
    private void initComponents() {
        setTitle("Actualizar Conexión de Servidor");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        
        JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(5, 2, 10, 10));
        panel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        
        panel.add(new JLabel("Código del Servidor:"));
        txtCodigo = new JTextField(20);
        panel.add(txtCodigo);
        
        panel.add(new JLabel("SGBD:"));
        txtSGBD = new JTextField(20);
        panel.add(txtSGBD);
        
        panel.add(new JLabel("IP/Dominio:"));
        txtIP = new JTextField(20);
        panel.add(txtIP);
        
        panel.add(new JLabel("Puerto:"));
        txtPuerto = new JTextField(20);
        panel.add(txtPuerto);
        
        lblStatus = new JLabel("");
        panel.add(lblStatus);
        
        btnActualizar = new JButton("Actualizar Servidor");
        btnActualizar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                actualizarServidor();
            }
        });
        panel.add(btnActualizar);
        
        add(panel);
    }
    
    private void actualizarServidor() {
        try {
            String codigo = txtCodigo.getText().trim();
            String sgbd = txtSGBD.getText().trim();
            String ip = txtIP.getText().trim();
            int puerto;
            
            // Validaciones
            if (codigo.isEmpty() || sgbd.isEmpty() || ip.isEmpty() || txtPuerto.getText().trim().isEmpty()) {
                mostrarError("Todos los campos son obligatorios");
                return;
            }
            
            try {
                puerto = Integer.parseInt(txtPuerto.getText().trim());
                if (puerto <= 0 || puerto > 65535) {
                    mostrarError("El puerto debe estar entre 1 y 65535");
                    return;
                }
            } catch (NumberFormatException ex) {
                mostrarError("El puerto debe ser un número válido");
                return;
            }
            
            // Crear objeto conexión
            DbConnection conexion = new DbConnection(sgbd, ip, puerto);
            
            // Actualizar en la base de datos
            boolean actualizado = dao.updateConexionServidor(codigo, conexion);
            
            if (actualizado) {
                mostrarMensaje("Servidor actualizado correctamente");
                limpiarCampos();
            } else {
                mostrarError("No se encontró un servidor con el código proporcionado");
            }
            
        } catch (SQLException ex) {
            mostrarError("Error de base de datos: " + ex.getMessage());
        } catch (IllegalArgumentException ex) {
            mostrarError("Error en los datos: " + ex.getMessage());
        } catch (Exception ex) {
            mostrarError("Error general: " + ex.getMessage());
        }
    }
    
    private void limpiarCampos() {
        txtCodigo.setText("");
        txtSGBD.setText("");
        txtIP.setText("");
        txtPuerto.setText("");
    }
    
    private void mostrarMensaje(String mensaje) {
        lblStatus.setText(mensaje);
        lblStatus.setForeground(Color.BLUE);
        JOptionPane.showMessageDialog(this, mensaje, "Información", JOptionPane.INFORMATION_MESSAGE);
    }
    
    private void mostrarError(String mensaje) {
        lblStatus.setText(mensaje);
        lblStatus.setForeground(Color.RED);
        JOptionPane.showMessageDialog(this, mensaje, "Error", JOptionPane.ERROR_MESSAGE);
    }
    
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new ServidorGUI().setVisible(true);
            }
        });
    }
}
```

### Estructura del Proyecto y Archivos de Construcción

#### ut5-practica-component: pom.xml

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.ut5</groupId>
    <artifactId>ut5-practica-component</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>jar</packaging>

    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.postgresql</groupId>
            <artifactId>postgresql</artifactId>
            <version>42.6.0</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.8.1</version>
                <configuration>
                    <source>11</source>
                    <target>11</target>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-jar-plugin</artifactId>
                <version>3.2.0</version>
                <configuration>
                    <archive>
                        <manifest>
                            <addClasspath>true</addClasspath>
                        </manifest>
                    </archive>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

#### ut5-practica-consola: pom.xml

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.ut5</groupId>
    <artifactId>ut5-practica-consola</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>jar</packaging>

    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <dependency>
            <groupId>com.ut5</groupId>
            <artifactId>ut5-practica-component</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.8.1</version>
                <configuration>
                    <source>11</source>
                    <target>11</target>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-jar-plugin</artifactId>
                <version>3.2.0</version>
                <configuration>
                    <archive>
                        <manifest>
                            <addClasspath>true</addClasspath>
                            <mainClass>com.ut5.consola.MainConsola</mainClass>
                        </manifest>
                    </archive>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

#### ut5-practica-gui: pom.xml

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.ut5</groupId>
    <artifactId>ut5-practica-gui</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>jar</packaging>

    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <dependency>
            <groupId>com.ut5</groupId>
            <artifactId>ut5-practica-component</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.8.1</version>
                <configuration>
                    <source>11</source>
                    <target>11</target>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-jar-plugin</artifactId>
                <version>3.2.0</version>
                <configuration>
                    <archive>
                        <manifest>
                            <addClasspath>true</addClasspath>
                            <mainClass>com.ut5.gui.ServidorGUI</mainClass>
                        </manifest>
                    </archive>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

### Pasos para Construir y Ejecutar los Proyectos

1. Primero, debes crear el esquema y las tablas de la base de datos usando el script SQL proporcionado.
	
2. Crea tres proyectos Maven separados:
	
	- ut5-practica-component
	- ut5-practica-consola
	- ut5-practica-gui
3. Para cada proyecto, crea la estructura de directorios correspondiente:

	```shell
    src/main/java/com/ut5/...
    ```

4. Coloca cada archivo Java en su paquete correspondiente:
	
	- Para el proyecto component:
		- Paquete `com.ut5.model` para Servidor y DbConnection
		- Paquete `com.ut5.dao` para ServidorDAO
	- Para el proyecto consola:
		- Paquete `com.ut5.consola` para MainConsola
	- Para el proyecto GUI:
		- Paquete `com.ut5.gui` para ServidorGUI
5. Construye los proyectos en orden:
	
	- Primero construye ut5-practica-component
	- Luego construye ut5-practica-consola y ut5-practica-gui
6. Puedes ejecutar las aplicaciones de consola o GUI:

	```shell
    java -jar ut5-practica-consola-1.0-SNAPSHOT.jar
    java -jar ut5-practica-gui-1.0-SNAPSHOT.jar
    ```