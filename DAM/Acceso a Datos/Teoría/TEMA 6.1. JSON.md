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

# **TEMA 6.1.** <br>Bases de Datos Documentales. <br>JSON


| Anexos |
| --- |
|[TEMA 6.2. MongoDB](TEMA%206.2.%20MongoDB.md)|
|[TEMA 6.3. MongoDB y Java](TEMA%206.3.%20MongoDB%20y%20Java.md)|
|[Tarea AD06. MongoDB y Java](../Práctica/Tarea%20AD06.%20MongoDB%20y%20Java.md)|

**JSON** (*JavaScript Object Notation*) es un formato de intercambio de datos basado en una parte de la especificación de ECMAScript (JavaScript). Es un formato de texto independiente del lenguaje, aunque utiliza características de lenguajes tipo C (C++, Java, Python, etc.).  

Como formato de texto, siempre se encuentra dentro de una variable de tipo texto o como literal entre comillas. Es una alternativa a XML, siendo más fácil de entender y escribir para humanos, y más eficiente en espacio.  

**Ejemplo de objeto JSON.**  
`{"nombre": "Joan", "edad": 4}`  

**Equivalente en XML.**  
`<persona><nombre>Joan</nombre><edad>4</edad></persona>`  

JSON se basa en dos estructuras comunes: *objetos* y *arrays*.  

## 1. Valores  

Un **valor** en JSON puede ser:  

| Tipo de valor         | Ejemplo                     |  
|-----------------------|-----------------------------|  
| Cadena de caracteres  | `"Jo"`                      |  
| Número               | `2345` o `12.05`            |  
| Booleano             | `true` o `false`            |  
| Nulo                 | `null`                      |  
| Objeto               | `{ "nombre": "Joan" }`      |  
| Array                | `[ "Jo", 12.05, null ]`     |  

## 2. Objetos  

Un **objeto** es una colección de pares *nombre-valor*, similar a diccionarios o estructuras en otros lenguajes. Comienza con `{` y termina con `}`, y los pares están separados por comas.  

**Formatos válidos.**  
- Objeto vacío: `{}`  
- Un solo par: `{"nombre": "Joan"}`  
- Múltiples pares:  

  ```json
  {
    "nombre": "Joan",
    "edad": 18,
    "dirección": {
      "calle": "Joan Miró",
      "número": 2,
      "cp": 07300,
      "localidad": "Inca"
    },
    "teléfonos": [123123123, 321321321]
  }
  ```  

## 3. Arrays  

Un **array** es una lista de valores, similar a vectores o listas en otros lenguajes. Comienza con `[` y termina con `]`, y los valores se separan por comas.  

**Formatos válidos.**  
- Array vacío: `[]`  
- Un solo valor: `[12]`  
- Múltiples valores:  

  ```json
  [12, "asd", 234.75, { "nombre": "Joan" }, [ "asd", 234.75 ], true]
  ```  

## 4. Conceptos relacionados  

| Término               | Definición                                                                 |  
|-----------------------|---------------------------------------------------------------------------|  
| **Binding**           | Vincular clases Java con formatos de almacenamiento como JSON de forma automatizada. |  
| **Marshalling**       | Proceso de convertir objetos Java a JSON (*serialización*).               |  
| **Unmarshalling**     | Proceso de convertir JSON a objetos Java (*deserialización*).             |  
| **POJO**             | Clase Java simple usada para intercambiar datos con fuentes externas. Suele tener atributos, getters/setters y constructores. |  

**Características de un POJO.**  
- Atributos con getters y setters.  
- Constructor sin parámetros.  
- Constructor con todos los parámetros (opcional).
