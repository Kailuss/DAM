---
tags: [AD, DAM]
cssclasses:
  - dam-ad
  - table-clean
banner: "![[ad.jpg]]"
banner_y: 0.32
---

# **Resumen TEMA 3.2.** <br>Java Records

## 1. Conceptos clave
- **Records.** Tipo especial de clase en Java (desde versión 14, estable en 16)
- **Propósito.** Modelar datos inmutables de forma concisa
- **Característica principal.** Inmutabilidad automática (atributos final)

## 2. Sintaxis básica

```java
public record Persona(String nombre, int edad) {}
```

Equivale a una clase tradicional con:

- Campos finales privados
- Constructor canónico
- Métodos de acceso (sin "get")
- equals(), hashCode(), toString()

## 3. Instanciación y uso

```java
Persona p = new Persona("Juan", 30);
System.out.println(p.nombre()); // "Juan"
System.out.println(p); // Persona[nombre=Juan, edad=30]
```

## 4. Constructores

### 4.1. **Constructor compacto (validación)**

```java
public record Persona(String nombre, int edad) {
    public Persona {
        if (edad < 0) 
            throw new IllegalArgumentException("Edad no válida");
    }
}
```

### 4.2. **Constructor personalizado**

```java
public record Persona(String nombre, int edad) {
    public Persona(String nombre) {
        this(nombre, 18); // Llama al constructor canónico
    }
}
```

## 5. Métodos adicionales

```java
public record Persona(String nombre, int edad) {
    // Método de instancia
    public String nombreEnMayusculas() {
        return nombre.toUpperCase();
    }
    
    // Método estático
    public static Persona crearRecienNacido(String nombre) {
        return new Persona(nombre, 0);
    }
}
```

## 6. Miembros estáticos

```java
public record Persona(String nombre, int edad) {
    private static final int EDAD_DEFAULT = 18;
    
    public Persona(String nombre) {
        this(nombre, EDAD_DEFAULT);
    }
    
    public static int getEdadDefault() {
        return EDAD_DEFAULT;
    }
}
```

## 7. Serialización

```java
public record Persona(String nombre, int edad) implements Serializable {
    @Serial
    private static final long serialVersionUID = 1L;
}
```

## 8. Restricciones importantes
1. **No pueden heredar** de otras clases
2. **Son final** (no se pueden extender)
3. **Atributos son inmutables** (final)
4. **No pueden declarar campos de instancia** adicionales
5. **Constructores solo pueden lanzar** unchecked exceptions

## 9. Ejemplo completo

```java
public record Producto(
    String codigo, 
    String descripcion, 
    double precio
) implements Serializable {
    @Serial
    private static final long serialVersionUID = 1L;
    
    private static final double IVA = 0.21;
    
    public Producto {
        if (precio <= 0) {
            throw new IllegalArgumentException("Precio no válido");
        }
    }
    
    public double precioConIva() {
        return precio * (1 + IVA);
    }
    
    public static Producto crearProductoBasico(String codigo) {
        return new Producto(codigo, "Producto estándar", 10.0);
    }
}
```

## 10. Buenas prácticas
- Usar para DTOs y modelos de datos simples
- No añadir lógica compleja (mantener su propósito simple)
- Ideal para datos que viajan entre capas de la aplicación
- Preferir sobre POJOs cuando la inmutabilidad es deseable

## 11. Comparación con clases tradicionales

| Característica       | Record          | Clase tradicional |
|----------------------|----------------|-------------------|
| Inmutabilidad        | Automática     | Manual            |
| Boilerplate          | Mínimo         | Mucho             |
| Herencia             | No             | Sí                |
| Campos adicionales   | No             | Sí                |
| Constructores        | Limitados      | Flexibles         |
