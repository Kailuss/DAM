---
tags: [DAM, PSP]
cssclasses:
  - dam-psp
  - table-compact-clean
banner: "![[psp.jpg]]"
banner_y: 0.25
number headings: max 2, _.1.
---

# Guion **PSP05**

## 1. Parte SQL

### Ejercicio 1: Creación de tipo y tabla

```sql
-- Crear el esquema
CREATE SCHEMA "ut5-practica";
GRANT ALL PRIVILEGES ON SCHEMA "ut5-practica" TO tu_usuario;

-- Crear el tipo de datos personalizado
CREATE TYPE "ut5-practica".tipo_conexion AS (
    sgbd VARCHAR(50),
    ip_dominio VARCHAR(100),
    puerto INTEGER
);

-- Crear la tabla servidors
CREATE TABLE "ut5-practica".servidors (
    codigo VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    usuarios_permitidos VARCHAR(50)[] NOT NULL,
    activo BOOLEAN NOT NULL,
    conexion "ut5-practica".tipo_conexion NOT NULL
);
```

### Ejercicio 2: Consultas y modificaciones

```sql
-- Insertar tres servidores con datos completos
INSERT INTO "ut5-practica".servidors VALUES (
    'SRV001',
    'Servidor Principal',
    ARRAY['admin', 'usuario1', 'usuario2'],
    true,
    ('PostgreSQL', '192.168.1.100', 5432)::"ut5-practica".tipo_conexion
);

INSERT INTO "ut5-practica".servidors VALUES (
    'SRV002',
    'Servidor Secundario',
    ARRAY['admin', 'usuario3'],
    true,
    ('MySQL', '192.168.1.101', 3306)::"ut5-practica".tipo_conexion
);

INSERT INTO "ut5-practica".servidors VALUES (
    'SRV003',
    'Servidor de Backup',
    ARRAY['admin'],
    false,
    ('Oracle', '192.168.1.102', 1521)::"ut5-practica".tipo_conexion
);

-- Añadir un nuevo usuario a un servidor
UPDATE "ut5-practica".servidors 
SET usuarios_permitidos = array_append(usuarios_permitidos, 'nuevo_usuario')
WHERE codigo = 'SRV001';

-- Modificar un nombre de usuario en un servidor
UPDATE "ut5-practica".servidors 
SET usuarios_permitidos = array_replace(usuarios_permitidos, 'usuario1', 'usuario_modificado')
WHERE codigo = 'SRV001';

-- Cambiar el puerto de conexión de un servidor
UPDATE "ut5-practica".servidors 
SET conexion = (conexion).sgbd, (conexion).ip_dominio, 5433
WHERE codigo = 'SRV001';
```

## 2. Parte JDBC

### Estructura de proyectos

```plaintext
ut5-practica-component/
  src/
    main/
      java/
        com/ejemplo/component/
          model/
            Servidor.java
            TipoConexion.java
          dao/
            ServidorDAO.java
            DatabaseConnection.java
          exceptions/
            ServidorException.java
      resources/
  pom.xml

ut5-practica-consola/
  src/
    main/
      java/
        com/ejemplo/consola/
          MainConsola.java
  pom.xml

ut5-practica-gui/
  src/
    main/
      java/
        com/ejemplo/gui/
          MainGUI.java
          ServidorForm.java
  pom.xml
```

### Ejercicio 3: POJOs

**Servidor.java**
```java
package com.ejemplo.component.model;

import java.util.Arrays;

public class Servidor {
    private String codigo;
    private String nombre;
    private String[] usuariosPermitidos;
    private boolean activo;
    private TipoConexion conexion;

    public Servidor(String codigo, String nombre, String[] usuariosPermitidos, 
                   boolean activo, TipoConexion conexion) throws ServidorException {
        setCodigo(codigo);
        setNombre(nombre);
        setUsuariosPermitidos(usuariosPermitidos);
        setActivo(activo);
        setConexion(conexion);
    }

    // Getters y setters con validaciones
    public void setCodigo(String codigo) throws ServidorException {
        if (codigo == null || codigo.trim().isEmpty()) {
            throw new ServidorException("El código no puede ser nulo o vacío");
        }
        if (codigo.length() > 20) {
            throw new ServidorException("El código no puede tener más de 20 caracteres");
        }
        this.codigo = codigo;
    }

    // ... otros setters con validaciones similares

    @Override
    public String toString() {
        return "Servidor{" +
                "codigo='" + codigo + '\'' +
                ", nombre='" + nombre + '\'' +
                ", usuariosPermitidos=" + Arrays.toString(usuariosPermitidos) +
                ", activo=" + activo +
                ", conexion=" + conexion +
                '}';
    }
}
```

**TipoConexion.java**
```java
package com.ejemplo.component.model;

public class TipoConexion {
    private String sgbd;
    private String ipDominio;
    private int puerto;

    public TipoConexion(String sgbd, String ipDominio, int puerto) throws ServidorException {
        setSgbd(sgbd);
        setIpDominio(ipDominio);
        setPuerto(puerto);
    }

    // Getters y setters con validaciones
    public void setPuerto(int puerto) throws ServidorException {
        if (puerto <= 0 || puerto > 65535) {
            throw new ServidorException("El puerto debe estar entre 1 y 65535");
        }
        this.puerto = puerto;
    }

    // ... otros setters con validaciones
}
```

### Ejercicio 4: Clase de operaciones con la base de datos

**ServidorDAO.java**
```java
package com.ejemplo.component.dao;

import com.ejemplo.component.model.Servidor;
import com.ejemplo.component.model.TipoConexion;
import com.ejemplo.component.exceptions.ServidorException;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class ServidorDAO {
    private Connection connection;

    public ServidorDAO(Connection connection) {
        this.connection = connection;
    }

    public List<Servidor> getAllServidores() throws ServidorException {
        List<Servidor> servidores = new ArrayList<>();
        String sql = "SELECT codigo, nombre, usuarios_permitidos, activo, " +
                     "(conexion).sgbd, (conexion).ip_dominio, (conexion).puerto " +
                     "FROM \"ut5-practica\".servidors";

        try (Statement stmt = connection.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
            
            while (rs.next()) {
                String[] usuarios = (String[]) rs.getArray("usuarios_permitidos").getArray();
                TipoConexion conexion = new TipoConexion(
                    rs.getString("sgbd"),
                    rs.getString("ip_dominio"),
                    rs.getInt("puerto")
                );
                
                Servidor servidor = new Servidor(
                    rs.getString("codigo"),
                    rs.getString("nombre"),
                    usuarios,
                    rs.getBoolean("activo"),
                    conexion
                );
                servidores.add(servidor);
            }
        } catch (SQLException e) {
            throw new ServidorException("Error al recuperar servidores: " + e.getMessage());
        }
        return servidores;
    }

    public Servidor getServidorByCodigo(String codigo) throws ServidorException {
        // Implementación similar a getAllServidores pero con WHERE codigo=?
    }

    public void insertServidor(Servidor servidor) throws ServidorException {
        // Implementación para insertar un nuevo servidor
    }

    public void removeUsuarioFromServidor(String codigoServidor, String usuario) throws ServidorException {
        // Implementación para eliminar un usuario de un servidor
    }

    public void updateConexionServidor(String codigoServidor, TipoConexion nuevaConexion) throws ServidorException {
        // Implementación para modificar los datos de conexión
    }
}
```

### Ejercicio 5: Clase de consola

**MainConsola.java**
```java
package com.ejemplo.consola;

import com.ejemplo.component.dao.ServidorDAO;
import com.ejemplo.component.model.Servidor;
import com.ejemplo.component.model.TipoConexion;
import com.ejemplo.component.exceptions.ServidorException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.util.List;

public class MainConsola {
    public static void main(String[] args) {
        String url = "jdbc:postgresql://localhost:5432/tu_basedatos";
        String user = "tu_usuario";
        String password = "tu_contraseña";
        
        try (Connection conn = DriverManager.getConnection(url, user, password)) {
            ServidorDAO servidorDAO = new ServidorDAO(conn);
            
            // Probar getAllServidores
            System.out.println("=== Todos los servidores ===");
            List<Servidor> servidores = servidorDAO.getAllServidores();
            servidores.forEach(System.out::println);
            
            // Probar getServidorByCodigo
            System.out.println("\n=== Servidor SRV001 ===");
            Servidor servidor = servidorDAO.getServidorByCodigo("SRV001");
            System.out.println(servidor);
            
            // Probar updateConexionServidor
            System.out.println("\n=== Actualizando conexión de SRV001 ===");
            TipoConexion nuevaConexion = new TipoConexion("PostgreSQL", "192.168.1.100", 5433);
            servidorDAO.updateConexionServidor("SRV001", nuevaConexion);
            System.out.println("Actualización exitosa");
            
        } catch (ServidorException e) {
            System.err.println("Error en operación con servidor: " + e.getMessage());
        } catch (SQLException e) {
            System.err.println("Error de conexión a la base de datos: " + e.getMessage());
        }
    }
}
```

### Ejercicio 6: Interfaz gráfica (ejemplo básico con Swing)

**ServidorForm.java**
```java
package com.ejemplo.gui;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import com.ejemplo.component.dao.ServidorDAO;
import com.ejemplo.component.model.TipoConexion;
import com.ejemplo.component.exceptions.ServidorException;
import java.sql.Connection;
import java.sql.DriverManager;

public class ServidorForm extends JFrame {
    private JTextField codigoField, sgbdField, ipField, puertoField;
    private JButton actualizarBtn;
    
    public ServidorForm() {
        setTitle("Actualizar Servidor");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridLayout(5, 2));
        
        add(new JLabel("Código del Servidor:"));
        codigoField = new JTextField();
        add(codigoField);
        
        add(new JLabel("SGBD:"));
        sgbdField = new JTextField();
        add(sgbdField);
        
        add(new JLabel("IP/Dominio:"));
        ipField = new JTextField();
        add(ipField);
        
        add(new JLabel("Puerto:"));
        puertoField = new JTextField();
        add(puertoField);
        
        actualizarBtn = new JButton("Actualizar");
        actualizarBtn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                actualizarServidor();
            }
        });
        add(actualizarBtn);
    }
    
    private void actualizarServidor() {
        String url = "jdbc:postgresql://localhost:5432/tu_basedatos";
        String user = "tu_usuario";
        String password = "tu_contraseña";
        
        try (Connection conn = DriverManager.getConnection(url, user, password)) {
            ServidorDAO servidorDAO = new ServidorDAO(conn);
            
            String codigo = codigoField.getText();
            String sgbd = sgbdField.getText();
            String ip = ipField.getText();
            int puerto = Integer.parseInt(puertoField.getText());
            
            TipoConexion conexion = new TipoConexion(sgbd, ip, puerto);
            servidorDAO.updateConexionServidor(codigo, conexion);
            
            JOptionPane.showMessageDialog(this, "Servidor actualizado correctamente", 
                "Éxito", JOptionPane.INFORMATION_MESSAGE);
            
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(this, "El puerto debe ser un número válido", 
                "Error", JOptionPane.ERROR_MESSAGE);
        } catch (ServidorException e) {
            JOptionPane.showMessageDialog(this, e.getMessage(), 
                "Error", JOptionPane.ERROR_MESSAGE);
        } catch (SQLException e) {
            JOptionPane.showMessageDialog(this, "Error de conexión a la base de datos: " + e.getMessage(), 
                "Error", JOptionPane.ERROR_MESSAGE);
        }
    }
    
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            ServidorForm form = new ServidorForm();
            form.setVisible(true);
        });
    }
}
```

## 3. Archivos POM.xml

### ut5-practica-component

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <groupId>com.ejemplo</groupId>
    <artifactId>ut5-practica-component</artifactId>
    <version>1.0-SNAPSHOT</version>
    
    <dependencies>
        <dependency>
            <groupId>org.postgresql</groupId>
            <artifactId>postgresql</artifactId>
            <version>42.2.24</version>
        </dependency>
    </dependencies>
</project>
```

### ut5-practica-consola

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <groupId>com.ejemplo</groupId>
    <artifactId>ut5-practica-consola</artifactId>
    <version>1.0-SNAPSHOT</version>
    
    <dependencies>
        <dependency>
            <groupId>com.ejemplo</groupId>
            <artifactId>ut5-practica-component</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
    </dependencies>
</project>
```

### ut5-practica-gui

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <groupId>com.ejemplo</groupId>
    <artifactId>ut5-practica-gui</artifactId>
    <version>1.0-SNAPSHOT</version>
    
    <dependencies>
        <dependency>
            <groupId>com.ejemplo</groupId>
            <artifactId>ut5-practica-component</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
    </dependencies>
</project>
```

## 4. Notas finales

1. Asegúrate de reemplazar "tu_usuario", "tu_contraseña" y "tu_basedatos" con tus credenciales reales de PostgreSQL.
2. Para compilar y empaquetar los proyectos, usa Maven (`mvn clean package`).
3. El proyecto GUI usa Swing como ejemplo, pero puedes usar JavaFX si lo prefieres.
4. Implementa todos los métodos faltantes en las clases DAO según las indicaciones del ejercicio.
