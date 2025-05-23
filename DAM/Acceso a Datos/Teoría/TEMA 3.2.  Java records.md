---
tags: [AD, DAM]
cssclasses:
  - dam-ad
  - table-clean
banner: "![[ad.jpg]]"
banner_y: 0.32
---

# **TEMA 3.2.** <br>Java records  

En muchas situaciones necesitamos una clase que mantenga datos de la aplicación. En estos casos se suelen utilizar POJOs (Plain Old Java Objects), es decir, clases con atributos, constructores, getters y, a veces, setters.  

Java dispone de la palabra reservada `record`. Nos permite definir un tipo especial de clase pensado para simplificar el proceso de creación de clases para mantener datos inmutables. Esto último es importante: los datos no se podrán manipular.  

Un `record` automáticamente proporciona:  

- Un constructor con parámetros para todos los atributos.  
- Los atributos declarados como `private final`.  
- Getters para todos los atributos.  
- Los métodos `equals` y `hashCode` para poder compararlos. Utiliza los valores de todos los atributos.  
- El método `toString`.  

Los `record` no se pueden especializar, es decir, no podemos crear una relación de herencia entre diferentes `record`. 

## 1. Sintaxis de los records  

A continuación, tenéis la definición completa de un `record`:  

```java
public record Person(String name, int age) {}
```  

Con una línea de código tenemos definido el tipo `Person` con dos atributos, `name` y `age`, sus getters, el `equals`, etc. Es equivalente al siguiente código:  

```java
public final class Person {
    private final String name;
    private final int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String name() {
        return name;
    }

    public int age() {
        return age;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Person person = (Person) o;
        return age == person.age && Objects.equals(name, person.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, age);
    }

    @Override
    public String toString() {
        return "Person(" +
                "name='" + name + '\'' +
                ", age=" + age +
                ')';
    }
}
```

## 2. Instanciación  

Un `record` es un tipo especial de clase, por lo que para crear instancias del `record` utilizaremos `new` como con el resto de clases:  

```java
PersonRecord person = new PersonRecord("Alice", 30);
```  

## 3. Acceso a los atributos  

Los atributos son `private` y `final`, por lo que solo tendremos acceso de lectura. En este caso, los métodos de acceso no incluyen la palabra `get`, ya que no tenemos que distinguirlos de los setters porque no existen:  

```java
System.out.println("person.name() = " + person.name());
```  

## 4. Personalización del constructor  

Por defecto, el `record` crea un constructor con parámetros para todos los atributos, lo que se conoce como el constructor canónico.  

Podemos crear otros constructores con la única condición de que todos deben llamar al constructor canónico:  

```java
public record PersonRecord(String name, int age) {
    public PersonRecord(String name) {
        this(name, 0);
    }
}
```  

Si necesitamos validar los datos, por ejemplo, podemos utilizar lo que se denomina como constructor compacto: no hace falta indicar los parámetros ni los `()`:  

```java
public record PersonRecord(String name, int age) {
    public PersonRecord {
        if (age < 0) {
            throw new IllegalArgumentException("Age must be greater than or equal to 0");
        }
    }
}
```  

También se puede utilizar la forma más tradicional de programar el constructor canónico:  

```java
public record PersonRecord(String name, int age) {
    public PersonRecord(String name, int age) {
        if (age < 0) {
            throw new IllegalArgumentException("Age must be greater than or equal to 0");
        }
        this.name = name;
        this.age = age;
    }
}
```  

## 5. Excepciones  

Los constructores de los `record` no pueden utilizar *checked exceptions* (todas aquellas que son subclases de `Exception`). Sí pueden utilizar *unchecked exceptions*, como las subclases de `RuntimeException`.

## 6. Otros métodos  

En los `record` podemos programar otros métodos. No debería ser lo habitual, ya que los `record` están pensados para ser "transmisores" de datos. Además, son inmutables, por lo que no podemos cambiar los valores de sus atributos.  

```java
public record PersonRecordV2(String name, int age) {
    public int agePlusFive() {
        return age + 5;
    }
}
```

## 7. Miembros de clase  

Los `record` pueden tener definidos atributos y métodos de clase (`static`).  

```java
public record PersonRecordV2(String name, int age) {
    private static int DEFAULT_AGE = 18;

    public PersonRecordV2(String name) {
        this(name, DEFAULT_AGE);
    }

    public static int getDefaultAge() {
        return DEFAULT_AGE;
    }
}
```  

## 8. Serialización  

Si tenemos que enviar las instancias de un `record` por un `Stream`, el `record` deberá implementar `Serializable`.  

```java
public record PersonRecordV2(String name, int age) implements Serializable {
    @Serial
    private static final long serialVersionUID = 11;
}
```  

Como siempre que implementamos la interfaz `Serializable`, conviene añadir el atributo:  

```java
@Serial private static final long serialVersionUID = 11;
```  

Este atributo permite determinar si la versión de la clase con la que leemos un `stream` es la misma versión de la clase que se escribió en el `stream`.  
