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

# **Ejercicios TEMA 6.2.** <br>Mongodb y java

## 1. Instrucciones

1. Crea un proyecto java, si puede ser con maven.
2. Incluye en el proyecto la dependencia del driver (o el jar si no utilizas maven).
3. Crea un paquete y una clase con main llamada `Ejercicios`.
4. Crea otro paquete con una clase llamada `BaseDades`.
5. Crea otro paquete con una clase que contienda atributos por el nif, el nombre, los linajes y el código postal de un aspirante, el constructor completo, los getters y los setters.
6. Cómo siempre, crea una excepción para tratar los errores de la aplicación.
7. Utiliza la colección `aspirantes` creada en el bloque de ejercicios anterior.

## 2. Ejercicios

1. En la clase `BaseDades` crea atributos para la url, la base de datos y la colección, con los correspondientes getters.
2. Al constructor recibe parámetros para el host, el puerto, la base de datos y la colección. Como alternativa puedes poner como parámetro un objeto `Properties`. Inicializa los atributos.

### 2.1. **Insert**

3. En la clase `BaseDades` crea un método que reciba un documento y lo inserte en la base de datos. No debe permitir insertar documentos null o vacías.
4. En el main de la clase `Ejercicios` crea un objeto aspirante. Crea un documento a partir de este objeto utilizando `append`. Añadiéndolo a la colección.
5. Añade el método `toMap` a la clase del aspirante. Debe volver un HashMap con una entrada para cada atributo del objeto.
6. En el main de la clase `Ejercicios` crea un nuevo aspirante. Crea un documento a partir del HashMap del aspirante e inserte en la colección.
7. En `BaseDades` crea un método que reciba por parámetro un objeto Aspirante y lo inserte en la base de datos sin tener que crear el Documento. En el main de la clase `Ejercicios` crea un nuevo y pasalo al método que acabas de crear.

### 2.2. **Find**

8. Crea un método que vuelva dentro de un **ArrayList** los documentos de la colección. Muestralos por pantalla en el main. 
9. Crea un método para recuperar todos documentos y devuelva un `ArrayList<Aspirant>`. Muéstralos por pantalla en el main.
10. Crea un método con dos parámetros, la posición inicial del primer documento que queremos recuperar y la cantidad de documentos que queremos recuperar. Debe poner estos documentos dentro de de un **ArrayList.**

### 2.3. **Filters***

11. Crea otro método que filtre documentos por **códigoPostal.** Debe recibir el código postal por y devolver los documentos dentro de un **ArrayList.**
12. Crea otro método que reciba como parámetros el **códigoPostal** y el nombre y devuelva todos los documentos que cumplan los dos requisitos.
13. Crea otro método que reciba como parámetros dos nombres y devuelva todos los documentos que contiendan un de los dos nombres.
14. Crea otro método que reciba como parámetros dos nombres y devuelva todos los documentos que no contiendan ninguno de los dos nombres.

### 2.4. **Sorts**

15. Crea otro método que ordene a los aspirantes por nombre con **ascending.**
16. Crea otro método que ordene a los aspirantes primero por un **ascending** de los linajes y del nombre.
17. Crea otro método que ordene a los aspirantes primero por un **ascending** de los linajes y luego por otro **descending** del nombre. ¿Que pasa?
18. Repite el ejercicio anterior a un nuevo método utilizando esta vez **orderBy.**
19. Crea otro método que devuelva todos los documentos de la colección ordenados por un campo. Debe tener un parámetro para el nombre del campo y otro por si queremos el orden ascendente o descendiente.

### 2.5. **Proyecciones**

20. Crea un método que devuelva un `ArrayList<Document>` y que utilice **include** para mostrar el nombre y los linajes de los aspirantes.
21. Crea un método que devuelva un `ArrayList<Document>` y que utilice **fields** para mostrar el nombre y los linajes y no la _id.
22. Crea otro método que reciba como parámetro una lista con los nombres de los campos que quiere incluir resultado. Tiene que devolver la lista con los documentos.

### 2.6. **Agregaciones**

23. Crea un método que utilice `aggregate` para devolver el nif, nombre linajes de cada aspirante con la cantidad de preferencias que tiene cada uno de ellos, ordenados por linajes. Utiliza `unwind` y `group`.
24. Crea un método que vuelva una lista con los centros de la colección, de manera que sean únicos, utilizando group.
25. Crea un método que añada a la base de datos una nueva colección con los centros únicos.

### 2.7. **Modificaciones**

26. Crea un método que reciba el nombre de un campo y el valor por el que filtrar los documentos y el nombre de un campo a modificar y el nuevo valor de este campo. Utilízalo desde el main para cambiar el nombre de el aspirante con nif 14140460F, de Virginia a Catalina.
27. Crea un método que permita cambiar todas las ocurrencias de un códigoPostal por otro. Por ejemplo, todos los aspirantes con código postal 07300 ahora deben tener el código postal 07301. Este método debe utilizar internamente el método del ejercicio anterior.

### 2.8. **Borrado**

28. Crea un método que elimine un documento. Debe recibir el **id** de parámetro. Utilizalo para eliminar al aspirante que has introducido anteriormente al ejercicio 6. Si el **id** es del tipo **ObjectId** tenéis que pasar un objeto de este tipo al filtro `new ObjectId(valor del parámetro)`.