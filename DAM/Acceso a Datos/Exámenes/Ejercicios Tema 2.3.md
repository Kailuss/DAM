# Ejercicios TEMA 2.3: JSON y Jackson

## Instrucciones

1. Crea un proyecto para hacer los ejercicios o aprovecha el del bloque de ejercicios anterior.
2. Crea un paquete donde guardarás todas las clases creadas en estos ejercicios.
3. Crea otro paquete con una clase con main. Desde esta clase prueba todos los métodos creados en los ejercicios.
4. Crea una excepción para tratar los errores propios de la aplicación (o reaprovecha la del bloque anterior).
5. Propaga las excepciones hasta el main y tratándolas allí.

## Ejercicios

### Ejercicio 1: Clase Persona

**Descripción**: Esta clase representa una entidad Persona con atributos básicos como nombre, apellidos y edad. Se utilizará para demostrar la serialización y deserialización de objetos Java a JSON y viceversa utilizando la biblioteca Jackson.

```java
package com.example.json; // Define el paquete donde se encuentra la clase

import com.fasterxml.jackson.annotation.JsonIgnore; // Para ignorar propiedades en la serialización
import com.fasterxml.jackson.annotation.JsonProperty; // Para personalizar nombres de propiedades en JSON

/**
 * Clase que representa una persona con atributos básicos.
 * Se utilizará para demostrar la serialización/deserialización con Jackson.
 */
public class Persona {
    
    // Atributos de la clase
    private String nombre; // Nombre de la persona
    private String apellidos; // Apellidos de la persona
    private int edad; // Edad de la persona
    
    /**
     * Constructor por defecto.
     * Necesario para la deserialización de JSON a objeto.
     * Jackson utiliza este constructor al crear objetos desde JSON.
     */
    public Persona() {
        // Constructor vacío requerido por Jackson
    }
    
    /**
     * Constructor con parámetros.
     * Permite crear objetos Persona con valores iniciales.
     * 
     * @param nombre Nombre de la persona
     * @param apellidos Apellidos de la persona
     * @param edad Edad de la persona
     */
    public Persona(String nombre, String apellidos, int edad) {
        this.nombre = nombre;
        this.apellidos = apellidos;
        this.edad = edad;
    }
    
    /**
     * Obtiene el nombre de la persona.
     * La anotación @JsonProperty personaliza el nombre de la propiedad en JSON.
     * 
     * @return Nombre de la persona
     */
    @JsonProperty("first_name") // En JSON aparecerá como "first_name" en lugar de "nombre"
    public String getNombre() {
        return nombre;
    }
    
    /**
     * Establece el nombre de la persona.
     * La anotación @JsonProperty debe coincidir con la del getter.
     * 
     * @param nombre Nuevo nombre de la persona
     */
    @JsonProperty("first_name")
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    /**
     * Obtiene los apellidos de la persona.
     * La anotación @JsonProperty personaliza el nombre de la propiedad en JSON.
     * 
     * @return Apellidos de la persona
     */
    @JsonProperty("last_name") // En JSON aparecerá como "last_name" en lugar de "apellidos"
    public String getApellidos() {
        return apellidos;
    }
    
    /**
     * Establece los apellidos de la persona.
     * La anotación @JsonProperty debe coincidir con la del getter.
     * 
     * @param apellidos Nuevos apellidos de la persona
     */
    @JsonProperty("last_name")
    public void setApellidos(String apellidos) {
        this.apellidos = apellidos;
    }
    
    /**
     * Obtiene la edad de la persona.
     * 
     * @return Edad de la persona
     */
    public int getEdad() {
        return edad;
    }
    
    /**
     * Establece la edad de la persona.
     * 
     * @param edad Nueva edad de la persona
     */
    public void setEdad(int edad) {
        this.edad = edad;
    }
    
    /**
     * Calcula si la persona es mayor de edad.
     * La anotación @JsonIgnore evita que este método se incluya en la serialización.
     * 
     * @return true si la persona es mayor de edad, false en caso contrario
     */
    @JsonIgnore // Este método no se incluirá en el JSON
    public boolean esMayorDeEdad() {
        return edad >= 18;
    }
    
    /**
     * Devuelve una representación en texto de la persona.
     * Útil para depuración y visualización.
     * 
     * @return Representación en texto de la persona
     */
    @Override
    public String toString() {
        return "Persona{" +
                "nombre='" + nombre + '\'' +
                ", apellidos='" + apellidos + '\'' +
                ", edad=" + edad +
                ", mayorDeEdad=" + esMayorDeEdad() +
                '}';
    }
}
```

### Ejercicio 2: Clase Direccion

**Descripción**: Esta clase representa una dirección postal con atributos como calle, número, código postal, etc. Se utilizará junto con la clase Persona para demostrar la serialización y deserialización de objetos anidados con Jackson.

```java
package com.example.json; // Define el paquete donde se encuentra la clase

/**
 * Clase que representa una dirección postal.
 * Se utilizará para demostrar la serialización/deserialización de objetos anidados.
 */
public class Direccion {
    
    // Atributos de la clase
    private String calle; // Nombre de la calle
    private int numero; // Número de la dirección
    private String piso; // Piso (puede incluir letra, por eso es String)
    private String ciudad; // Ciudad
    private String codigoPostal; // Código postal (String porque puede empezar por 0)
    
    /**
     * Constructor por defecto.
     * Necesario para la deserialización de JSON a objeto.
     */
    public Direccion() {
        // Constructor vacío requerido por Jackson
    }
    
    /**
     * Constructor con parámetros.
     * Permite crear objetos Direccion con valores iniciales.
     * 
     * @param calle Nombre de la calle
     * @param numero Número de la dirección
     * @param piso Piso (puede incluir letra)
     * @param ciudad Ciudad
     * @param codigoPostal Código postal
     */
    public Direccion(String calle, int numero, String piso, String ciudad, String codigoPostal) {
        this.calle = calle;
        this.numero = numero;
        this.piso = piso;
        this.ciudad = ciudad;
        this.codigoPostal = codigoPostal;
    }
    
    /**
     * Obtiene el nombre de la calle.
     * 
     * @return Nombre de la calle
     */
    public String getCalle() {
        return calle;
    }
    
    /**
     * Establece el nombre de la calle.
     * 
     * @param calle Nuevo nombre de la calle
     */
    public void setCalle(String calle) {
        this.calle = calle;
    }
    
    /**
     * Obtiene el número de la dirección.
     * 
     * @return Número de la dirección
     */
    public int getNumero() {
        return numero;
    }
    
    /**
     * Establece el número de la dirección.
     * 
     * @param numero Nuevo número de la dirección
     */
    public void setNumero(int numero) {
        this.numero = numero;
    }
    
    /**
     * Obtiene el piso.
     * 
     * @return Piso (puede incluir letra)
     */
    public String getPiso() {
        return piso;
    }
    
    /**
     * Establece el piso.
     * 
     * @param piso Nuevo piso
     */
    public void setPiso(String piso) {
        this.piso = piso;
    }
    
    /**
     * Obtiene la ciudad.
     * 
     * @return Ciudad
     */
    public String getCiudad() {
        return ciudad;
    }
    
    /**
     * Establece la ciudad.
     * 
     * @param ciudad Nueva ciudad
     */
    public void setCiudad(String ciudad) {
        this.ciudad = ciudad;
    }
    
    /**
     * Obtiene el código postal.
     * 
     * @return Código postal
     */
    public String getCodigoPostal() {
        return codigoPostal;
    }
    
    /**
     * Establece el código postal.
     * 
     * @param codigoPostal Nuevo código postal
     */
    public void setCodigoPostal(String codigoPostal) {
        this.codigoPostal = codigoPostal;
    }
    
    /**
     * Devuelve una representación en texto de la dirección.
     * Útil para depuración y visualización.
     * 
     * @return Representación en texto de la dirección
     */
    @Override
    public String toString() {
        return "Direccion{" +
                "calle='" + calle + '\'' +
                ", numero=" + numero +
                ", piso='" + piso + '\'' +
                ", ciudad='" + ciudad + '\'' +
                ", codigoPostal='" + codigoPostal + '\'' +
                '}';
    }
}
```

### Ejercicio 3: Clase PersonaCompleta

**Descripción**: Esta clase extiende la clase Persona añadiendo una dirección y una lista de aficiones. Se utilizará para demostrar la serialización y deserialización de objetos complejos con relaciones y colecciones utilizando Jackson.

```java
package com.example.json; // Define el paquete donde se encuentra la clase

import java.util.ArrayList; // Para la lista de aficiones
import java.util.List; // Interfaz de lista

import com.fasterxml.jackson.annotation.JsonInclude; // Para controlar la inclusión de propiedades nulas
import com.fasterxml.jackson.annotation.JsonInclude.Include; // Opciones de inclusión

/**
 * Clase que extiende Persona añadiendo dirección y aficiones.
 * Demuestra la serialización/deserialización de objetos complejos con Jackson.
 * La anotación @JsonInclude indica que solo se incluirán propiedades no nulas en el JSON.
 */
@JsonInclude(Include.NON_NULL) // Solo incluye propiedades no nulas en el JSON
public class PersonaCompleta extends Persona {
    
    // Atributos adicionales
    private Direccion direccion; // Dirección de la persona (objeto anidado)
    private List<String> aficiones; // Lista de aficiones (colección)
    
    /**
     * Constructor por defecto.
     * Necesario para la deserialización de JSON a objeto.
     * Inicializa la lista de aficiones.
     */
    public PersonaCompleta() {
        // Inicializamos la lista de aficiones vacía
        aficiones = new ArrayList<>();
    }
    
    /**
     * Constructor con parámetros básicos.
     * Llama al constructor de la clase padre (Persona) e inicializa la lista de aficiones.
     * 
     * @param nombre Nombre de la persona
     * @param apellidos Apellidos de la persona
     * @param edad Edad de la persona
     */
    public PersonaCompleta(String nombre, String apellidos, int edad) {
        // Llamamos al constructor de la clase padre
        super(nombre, apellidos, edad);
        // Inicializamos la lista de aficiones vacía
        aficiones = new ArrayList<>();
    }
    
    /**
     * Constructor completo con todos los parámetros.
     * 
     * @param nombre Nombre de la persona
     * @param apellidos Apellidos de la persona
     * @param edad Edad de la persona
     * @param direccion Dirección de la persona
     * @param aficiones Lista de aficiones
     */
    public PersonaCompleta(String nombre, String apellidos, int edad, 
                          Direccion direccion, List<String> aficiones) {
        // Llamamos al constructor de la clase padre
        super(nombre, apellidos, edad);
        this.direccion = direccion;
        this.aficiones = aficiones;
    }
    
    /**
     * Obtiene la dirección de la persona.
     * 
     * @return Dirección de la persona
     */
    public Direccion getDireccion() {
        return direccion;
    }
    
    /**
     * Establece la dirección de la persona.
     * 
     * @param direccion Nueva dirección de la persona
     */
    public void setDireccion(Direccion direccion) {
        this.direccion = direccion;
    }
    
    /**
     * Obtiene la lista de aficiones de la persona.
     * 
     * @return Lista de aficiones
     */
    public List<String> getAficiones() {
        return aficiones;
    }
    
    /**
     * Establece la lista de aficiones de la persona.
     * 
     * @param aficiones Nueva lista de aficiones
     */
    public void setAficiones(List<String> aficiones) {
        this.aficiones = aficiones;
    }
    
    /**
     * Añade una afición a la lista de aficiones.
     * Método de conveniencia para añadir aficiones individualmente.
     * 
     * @param aficion Afición a añadir
     */
    public void addAficion(String aficion) {
        // Si la lista no está inicializada, la creamos
        if (aficiones == null) {
            aficiones = new ArrayList<>();
        }
        // Añadimos la afición a la lista
        aficiones.add(aficion);
    }
    
    /**
     * Devuelve una representación en texto de la persona completa.
     * Incluye la información de la clase padre (Persona) y los atributos adicionales.
     * 
     * @return Representación en texto de la persona completa
     */
    @Override
    public String toString() {
        return "PersonaCompleta{" +
                "nombre='" + getNombre() + '\'' +
                ", apellidos='" + getApellidos() + '\'' +
                ", edad=" + getEdad() +
                ", mayorDeEdad=" + esMayorDeEdad() +
                ", direccion=" + direccion +
                ", aficiones=" + aficiones +
                '}';
    }
}
```

### Ejercicio 4: Clase JsonUtils

**Descripción**: Esta clase de utilidad proporciona métodos para convertir objetos Java a JSON y viceversa utilizando la biblioteca Jackson. Incluye métodos para trabajar con archivos JSON y para manipular estructuras de datos JSON directamente.

```java
package com.example.json; // Define el paquete donde se encuentra la clase

import java.io.File; // Para trabajar con archivos
import java.io.IOException; // Para manejar excepciones de E/S
import java.util.List; // Para trabajar con listas

import com.fasterxml.jackson.core.JsonProcessingException; // Para excepciones específicas de procesamiento JSON
import com.fasterxml.jackson.core.type.TypeReference; // Para referencias de tipo genérico
import com.fasterxml.jackson.databind.JsonNode; // Para trabajar con nodos JSON
import com.fasterxml.jackson.databind.ObjectMapper; // Clase principal de Jackson para mapeo de objetos
import com.fasterxml.jackson.databind.SerializationFeature; // Para configurar características de serialización

/**
 * Clase de utilidad para trabajar con JSON usando Jackson.
 * Proporciona métodos para convertir entre objetos Java y JSON.
 */
public class JsonUtils {
    
    // ObjectMapper es thread-safe, podemos tener una instancia estática
    private static final ObjectMapper objectMapper = new ObjectMapper();
    
    // Bloque estático para configurar el ObjectMapper
    static {
        // Configuramos el ObjectMapper para que formatee el JSON de manera legible
        objectMapper.enable(SerializationFeature.INDENT_OUTPUT);
    }
    
    /**
     * Convierte un objeto Java a una cadena JSON.
     * 
     * @param objeto Objeto a convertir
     * @return Cadena JSON
     * @throws MiExcepcion Si hay algún error durante la conversión
     */
    public static String objetoAJson(Object objeto) throws MiExcepcion {
        try {
            // Convertimos el objeto a una cadena JSON formateada
            return objectMapper.writeValueAsString(objeto);
        } catch (JsonProcessingException e) {
            // Si hay un error, lanzamos nuestra excepción personalizada
            throw new MiExcepcion("Error al convertir objeto a JSON: " + e.getMessage(), e);
        }
    }
    
    /**
     * Convierte una cadena JSON a un objeto Java del tipo especificado.
     * 
     * @param <T> Tipo genérico del objeto a devolver
     * @param json Cadena JSON
     * @param clase Clase del objeto a crear
     * @return Objeto Java del tipo especificado
     * @throws MiExcepcion Si hay algún error durante la conversión
     */
    public static <T> T jsonAObjeto(String json, Class<T> clase) throws MiExcepcion {
        try {
            // Convertimos la cadena JSON a un objeto del tipo especificado
            return objectMapper.readValue(json, clase);
        } catch (JsonProcessingException e) {
            // Si hay un error, lanzamos nuestra excepción personalizada
            throw new MiExcepcion("Error al convertir JSON a objeto: " + e.getMessage(), e);
        }
    }
    
    /**
     * Convierte una cadena JSON a una lista de objetos del tipo especificado.
     * 
     * @param <T> Tipo genérico de los objetos de la lista
     * @param json Cadena JSON que representa un array
     * @param typeReference Referencia de tipo para la lista
     * @return Lista de objetos del tipo especificado
     * @throws MiExcepcion Si hay algún error durante la conversión
     */
    public static <T> List<T> jsonALista(String json, TypeReference<List<T>> typeReference) throws MiExcepcion {
        try {
            // Convertimos la cadena JSON a una lista de objetos del tipo especificado
            // TypeReference es necesario para preservar la información de tipo genérico
            return objectMapper.readValue(json, typeReference);
        } catch (JsonProcessingException e) {
            // Si hay un error, lanzamos nuestra excepción personalizada
            throw new MiExcepcion("Error al convertir JSON a lista: " + e.getMessage(), e);
        }
    }
    
    /**
     * Guarda un objeto Java como archivo JSON.
     * 
     * @param objeto Objeto a guardar
     * @param rutaArchivo Ruta del archivo donde guardar el JSON
     * @throws MiExcepcion Si hay algún error durante la escritura
     */
    public static void guardarComoJson(Object objeto, String rutaArchivo) throws MiExcepcion {
        try {
            // Creamos un objeto File con la ruta especificada
            File archivo = new File(rutaArchivo);
            
            // Escribimos el objeto como JSON en el archivo
            // writeValue escribe el objeto formateado según la configuración del ObjectMapper
            objectMapper.writeValue(archivo, objeto);
            
            System.out.println("Objeto guardado como JSON en: " + rutaArchivo);
        } catch (IOException e) {
            // Si hay un error, lanzamos nuestra excepción personalizada
            throw new MiExcepcion("Error al guardar objeto como JSON: " + e.getMessage(), e);
        }
    }
    
    /**
     * Carga un objeto Java desde un archivo JSON.
     * 
     * @param <T> Tipo genérico del objeto a cargar
     * @param rutaArchivo Ruta del archivo JSON
     * @param clase Clase del objeto a crear
     * @return Objeto Java del tipo especificado
     * @throws MiExcepcion Si hay algún error durante la lectura
     */
    public static <T> T cargarDesdeJson(String rutaArchivo, Class<T> clase) throws MiExcepcion {
        try {
            // Creamos un objeto File con la ruta especificada
            File archivo = new File(rutaArchivo);
            
            // Verificamos que el archivo existe
            if (!archivo.exists()) {
                throw new MiExcepcion("El archivo no existe: " + rutaArchivo);
            }
            
            // Leemos el archivo JSON y lo convertimos a un objeto del tipo especificado
            T objeto = objectMapper.readValue(archivo, clase);
            
            System.out.println("Objeto cargado desde JSON: " + rutaArchivo);
            return objeto;
        } catch (IOException e) {
            // Si hay un error, lanzamos nuestra excepción personalizada
            throw new MiExcepcion("Error al cargar objeto desde JSON: " + e.getMessage(), e);
        }
    }
    
    /**
     * Convierte una cadena JSON a un árbol de nodos JSON.
     * Útil para manipular JSON de estructura desconocida o dinámica.
     * 
     * @param json Cadena JSON
     * @return Nodo raíz del árbol JSON
     * @throws MiExcepcion Si hay algún error durante la conversión
     */
    public static JsonNode jsonAArbol(String json) throws MiExcepcion {
        try {
            // Convertimos la cadena JSON a un árbol de nodos JsonNode
            // JsonNode permite navegar y manipular la estructura JSON
            return objectMapper.readTree(json);
        } catch (JsonProcessingException e) {
            // Si hay un error, lanzamos nuestra excepción personalizada
            throw new MiExcepcion("Error al convertir JSON a árbol: " + e.getMessage(), e);
        }
    }
    
    /**
     * Convierte un árbol de nodos JSON a una cadena JSON.
     * 
     * @param nodo Nodo raíz del árbol JSON
     * @return Cadena JSON
     * @throws MiExcepcion Si hay algún error durante la conversión
     */
    public static String arbolAJson(JsonNode nodo) throws MiExcepcion {
        try {
            // Convertimos el árbol de nodos JsonNode a una cadena JSON formateada
            return objectMapper.writeValueAsString(nodo);
        } catch (JsonProcessingException e) {
            // Si hay un error, lanzamos nuestra excepción personalizada
            throw new MiExcepcion("Error al convertir árbol a JSON: " + e.getMessage(), e);
        }
    }
}
```

### Ejercicio 5: Clase PruebasJson (con main)

**Descripción**: Esta clase contiene el método main y métodos para probar todas las funcionalidades implementadas en las clases anteriores. Aquí se realizan pruebas de serialización, deserialización y manipulación de objetos JSON utilizando la biblioteca Jackson.

```java
package com.example.main; // Define el paquete donde se encuentra la clase principal

import java.util.ArrayList; // Para crear listas
import java.util.Arrays; // Para crear arrays
import java.util.List; // Interfaz de lista

import com.example.json.Direccion; // Importamos la clase Direccion
import com.example.json.JsonUtils; // Importamos la clase de utilidades JSON
import com.example.json.MiExcepcion; // Importamos nuestra excepción personalizada
import com.example.json.Persona; // Importamos la clase Persona
import com.example.json.PersonaCompleta; // Importamos la clase PersonaCompleta
import com.fasterxml.jackson.core.type.TypeReference; // Para referencias de tipo genérico
import com.fasterxml.jackson.databind.JsonNode; // Para trabajar con nodos JSON
import com.fasterxml.jackson.databind.node.ObjectNode; // Para modificar nodos JSON de tipo objeto

/**
 * Clase principal para probar las funcionalidades de JSON con Jackson.
 * Contiene el método main y métodos para probar cada aspecto de la serialización/deserialización.
 */
public class PruebasJson {
    
    /**
     * Método principal que ejecuta las pruebas.
     * 
     * @param args Argumentos de línea de comandos (no utilizados)
     */
    public static void main(String[] args) {
        try {
            // Definimos ruta base para los archivos JSON
            String rutaBase = "/tmp/pruebas_json/";
            
            // Creamos el directorio base si no existe
            new java.io.File(rutaBase).mkdirs();
            
            // Probamos las diferentes funcionalidades
            probarPersonaSimple(rutaBase);
            probarPersonaCompleta(rutaBase);
            probarListaPersonas(rutaBase);
            probarManipulacionJson();
            
        } catch (MiExcepcion e) {
            // Capturamos y mostramos cualquier excepción personalizada
            System.err.println("Error: " + e.getMessage());
            if (e.getCause() != null) {
                System.err.println("Causa: " + e.getCause().getMessage());
            }
            e.printStackTrace();
        }
    }
    
    /**
     * Prueba la serialización y deserialización de objetos Persona simples.
     * 
     * @param rutaBase Directorio base para los archivos JSON
     * @throws MiExcepcion Si hay algún error durante las pruebas
     */
    private static void probarPersonaSimple(String rutaBase) throws MiExcepcion {
        System.out.println("\n=== Pruebas con Persona Simple ===");
        
        // Creamos un objeto Persona
        Persona persona = new Persona("Juan", "Pérez", 25);
        
        // Convertimos el objeto a JSON y lo mostramos
        String json = JsonUtils.objetoAJson(persona);
        System.out.println("Persona como JSON:");
        System.out.println(json);
        
        // Guardamos el objeto como archivo JSON
        String rutaArchivo = rutaBase + "persona.json";
        JsonUtils.guardarComoJson(persona, rutaArchivo);
        
        // Cargamos el objeto desde el archivo JSON
        Persona personaCargada = JsonUtils.cargarDesdeJson(rutaArchivo, Persona.class);
        System.out.println("Persona cargada desde JSON: " + personaCargada);
        
        // Convertimos JSON a objeto
        Persona personaDesdeJson = JsonUtils.jsonAObjeto(json, Persona.class);
        System.out.println("Persona desde JSON: " + personaDesdeJson);
    }
    
    /**
     * Prueba la serialización y deserialización de objetos PersonaCompleta.
     * 
     * @param rutaBase Directorio base para los archivos JSON
     * @throws MiExcepcion Si hay algún error durante las pruebas
     */
    private static void probarPersonaCompleta(String rutaBase) throws MiExcepcion {
        System.out.println("\n=== Pruebas con Persona Completa ===");
        
        // Creamos un objeto Direccion
        Direccion direccion = new Direccion("Calle Mayor", 10, "2A", "Madrid", "28001");
        
        // Creamos una lista de aficiones
        List<String> aficiones = Arrays.asList("Leer", "Nadar", "Viajar");
        
        // Creamos un objeto PersonaCompleta
        PersonaCompleta persona = new PersonaCompleta("María", "García", 30, direccion, aficiones);
        
        // Convertimos el objeto a JSON y lo mostramos
        String json = JsonUtils.objetoAJson(persona);
        System.out.println("PersonaCompleta como JSON:");
        System.out.println(json);
        
        // Guardamos el objeto como archivo JSON
        String rutaArchivo = rutaBase + "persona_completa.json";
        JsonUtils.guardarComoJson(persona, rutaArchivo);
        
        // Cargamos el objeto desde el archivo JSON
        PersonaCompleta personaCargada = JsonUtils.cargarDesdeJson(rutaArchivo, PersonaCompleta.class);
        System.out.println("PersonaCompleta cargada desde JSON: " + personaCargada);
        
        // Probamos con un objeto que tiene atributos nulos
        PersonaCompleta personaIncompleta = new PersonaCompleta("Carlos", "Ruiz", 40);
        personaIncompleta.addAficion("Programar");
        
        // Convertimos el objeto a JSON y lo mostramos
        // Los atributos nulos no deberían aparecer debido a @JsonInclude(Include.NON_NULL)
        json = JsonUtils.objetoAJson(personaIncompleta);
        System.out.println("PersonaCompleta con atributos nulos como JSON:");
        System.out.println(json);
    }
    
    /**
     * Prueba la serialización y deserialización de listas de objetos.
     * 
     * @param rutaBase Directorio base para los archivos JSON
     * @throws MiExcepcion Si hay algún error durante las pruebas
     */
    private static void probarListaPersonas(String rutaBase) throws MiExcepcion {
        System.out.println("\n=== Pruebas con Lista de Personas ===");
        
        // Creamos una lista de personas
        List<Persona> personas = new ArrayList<>();
        personas.add(new Persona("Juan", "Pérez", 25));
        personas.add(new Persona("María", "García", 30));
        personas.add(new Persona("Carlos", "Ruiz", 40));
        
        // Convertimos la lista a JSON y la mostramos
        String json = JsonUtils.objetoAJson(personas);
        System.out.println("Lista de Personas como JSON:");
        System.out.println(json);
        
        // Guardamos la lista como archivo JSON
        String rutaArchivo = rutaBase + "lista_personas.json";
        JsonUtils.guardarComoJson(personas, rutaArchivo);
        
        // Convertimos JSON a lista de objetos
        // Necesitamos usar TypeReference para preservar la información de tipo genérico
        List<Persona> personasDesdeJson = JsonUtils.jsonALista(json, new TypeReference<List<Persona>>() {});
        System.out.println("Lista de Personas desde JSON:");
        for (Persona persona : personasDesdeJson) {
            System.out.println("  " + persona);
        }
    }
    
    /**
     * Prueba la manipulación directa de estructuras JSON.
     * 
     * @throws MiExcepcion Si hay algún error durante las pruebas
     */
    private static void probarManipulacionJson() throws MiExcepcion {
        System.out.println("\n=== Pruebas de Manipulación JSON ===");
        
        // Creamos un JSON de ejemplo
        String jsonOriginal = "{ \"nombre\": \"Juan\", \"edad\": 25, \"direccion\": { \"ciudad\": \"Madrid\" } }";
        System.out.println("JSON original:");
        System.out.println(jsonOriginal);
        
        // Convertimos el JSON a un árbol de nodos
        JsonNode raiz = JsonUtils.jsonAArbol(jsonOriginal);
        
        // Accedemos a valores del árbol
        String nombre = raiz.get("nombre").asText();
        int edad = raiz.get("edad").asInt();
        String ciudad = raiz.get("direccion").get("ciudad").asText();
        
        System.out.println("Valores extraídos del JSON:");
        System.out.println("  Nombre: " + nombre);
        System.out.println("  Edad: " + edad);
        System.out.println("  Ciudad: " + ciudad);
        
        // Modificamos el árbol (necesitamos convertir a ObjectNode para modificar)
        ObjectNode nodoObjeto = (ObjectNode) raiz;
        nodoObjeto.put("nombre", "María"); // Cambiamos el nombre
        nodoObjeto.put("edad", 30); // Cambiamos la edad
        nodoObjeto.put("activo", true); // Añadimos un nuevo campo
        
        // Modificamos el nodo anidado de dirección
        ObjectNode nodoDireccion = (ObjectNode) nodoObjeto.get("direccion");
        nodoDireccion.put("ciudad", "Barcelona"); // Cambiamos la ciudad
        nodoDireccion.put("codigoPostal", "08001"); // Añadimos el código postal
        
        // Convertimos el árbol modificado a JSON
        String jsonModificado = JsonUtils.arbolAJson(raiz);
        System.out.println("JSON modificado:");
        System.out.println(jsonModificado);
    }
}
```

### Clase `MiExcepcion` (excepción personalizada)

**Descripción**: Esta clase representa una excepción personalizada para la aplicación, que permite encapsular y propagar errores específicos de manera controlada.

```java
package com.example.json; // Define el paquete donde se encuentra la clase

/**
 * Excepción personalizada para la aplicación.
 * Extiende Exception para ser una excepción comprobada (checked).
 */
public class MiExcepcion extends Exception {
    
    /**
     * Constructor sin parámetros.
     * Llama al constructor de la clase padre.
     */
    public MiExcepcion() {
        super();
    }
    
    /**
     * Constructor con mensaje.
     * 
     * @param mensaje Mensaje descriptivo del error
     */
    public MiExcepcion(String mensaje) {
        super(mensaje);
    }
    
    /**
     * Constructor con mensaje y causa.
     * Útil para encapsular excepciones de bajo nivel.
     * 
     * @param mensaje Mensaje descriptivo del error
     * @param causa Excepción original que causó el error
     */
    public MiExcepcion(String mensaje, Throwable causa) {
        super(mensaje, causa);
    }
}
```
