# Ejer

### Ejercicio 1.1 (1,5 puntos)

**Crear una clase con un método para guardar una lista de módulos en un fichero usando `DataStreams`**

```java
import java.io.DataOutputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.List;

public class ModulSerializer {

    public void guardarModulos(List<Modul> modulos, String ruta) throws IOException {
        try (DataOutputStream dos = new DataOutputStream(new FileOutputStream(ruta))) {
            dos.writeInt(modulos.size()); // escribimos la cantidad de módulos
            for (Modul m : modulos) {
                dos.writeUTF(m.getCodi());
                dos.writeUTF(m.getNom());
                dos.writeInt(m.getHores());
            }
        }
    }
}
```

> Este método recibe una lista de objetos `Modul` y una ruta, y guarda todos los módulos en el archivo usando `DataOutputStream`.

---

### Ejercicio 1.2 (1,5 puntos)

**Código Java para recuperar un campo de tipo definido por el usuario desde PostgreSQL**

Supongamos que tienes una tabla `servidors` con un campo del tipo `TServidor`, y que tienes una clase Java llamada `Servidor` que representa ese tipo.

```java
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import org.postgresql.util.PGobject;

public class ServidorDAO {

    public Servidor obtenerServidor(Connection conn, int id) throws SQLException {
        String sql = "SELECT servidor FROM servidors WHERE id = ?";
        try (PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, id);
            ResultSet rs = stmt.executeQuery();
            if (rs.next()) {
                PGobject pgObj = (PGobject) rs.getObject("servidor");
                String valor = pgObj.getValue();
                return parsearServidor(valor); // Convierte el valor a un objeto Servidor
            }
        }
        return null;
    }

    private Servidor parsearServidor(String valor) {
        // Aquí puedes usar una librería como Gson o Jackson si el tipo TServidor se guarda como JSON
        // Ejemplo usando Gson:
        // return new Gson().fromJson(valor, Servidor.class);
        return null; // Placeholder (esto debes implementarlo según cómo sea tu tipo de dato)
    }
}
```

> Este código obtiene un objeto del tipo definido por el usuario (como `TServidor`) desde la base de datos y lo convierte a un objeto Java. Necesitarás implementar `parsearServidor()` dependiendo del formato real (por ejemplo, JSON).

---

¿Te gustaría que te ayude a implementar también la función `parsearServidor()` con una librería como Gson o Jackson?