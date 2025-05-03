---
tags:
  - DAM
  - AD
cssclasses:
  - dam-ad
  - table-compact-clean
banner: "![[ad.jpg]]"
banner_y: 0.32
number headings: max 2, _.1.
---

# Tarea **AD05**


## 1. Instrucciones SQL

1. Crear un nuevo esquema en la base de datos llamado `ut5-practica`. Asegúrate de otorgar todos los privilegios a tu usuario.  
2. Puedes utilizar los asistentes de pgAdmin4 para realizar los ejercicios del apartado SQL.  
. 
## 2. Ejercicios SQL (4 puntos)

### Ejercicio 1 (2 puntos)

Crear un tipo de datos personalizado para almacenar la información de conexión a un servidor de base de datos. El tipo debe incluir:  

- **SGBD:** MySQL, PostgreSQL, Oracle, ZOODB, etc.  
- **IP o dominio:**  
- **Puerto** (numérico).  

Crear la tabla `servidors` con las siguientes columnas:  

- **Código alfanumérico** (clave primaria).  
- **Nombre descriptivo.**  
- **Array** con los nombres de usuario permitidos.  
- **Columna** para indicar si el servidor está activo (boolean).  
- **Columna** del tipo de datos creado anteriormente.  

**Restricciones.** Ningún dato puede ser nulo.  

### Ejercicio 2 (2 puntos)

Ejecutar las siguientes consultas y modificaciones:  

1. Insertar tres servidores con datos completos.  
2. Añadir un nuevo usuario a un servidor.  
3. Modificar un nombre de usuario en un servidor.  
4. Cambiar el puerto de conexión de un servidor.  

## 3. Instrucciones JDBC

- Leer todo el enunciado antes de comenzar.  
- Crear tres proyectos:  
  - **`ut5-practica-component`.** Incluir el driver de PostgreSQL. Este proyecto es el único que puede acceder a la base de datos, pero no interactúa con el usuario.  
  - **`ut5-practica-consola`.** Incluir el JAR del proyecto `ut5-practica-component`. Mostrará por consola los resultados de probar los métodos del componente.  
  - **`ut5-practica-gui`.** Incluir el JAR del proyecto `ut5-practica-component`. Utilizar Swing, JavaFX, AWT, etc., para la interfaz gráfica.  

## 4. `ut5-practica-component` (4 puntos)

### Ejercicio 3 (1.5 puntos)

Crear los POJOs necesarios para trabajar con la tabla `servidors`. Controlar todas las restricciones:  

- Evitar valores nulos.  
- Validar la longitud de los campos.  

### Ejercicio 4 (2.5 puntos)

Crear una clase que centralice las operaciones con la base de datos. Esta clase **no debe imprimir nada por pantalla ni acceder al teclado.** Debe permitir:  

1. Recuperar todos los servidores de la base de datos.  
2. Recuperar un servidor por su código.  
3. Insertar un servidor.  
4. Eliminar un usuario de un servidor.  
5. Modificar los datos de conexión de un servidor.  

## 5. `ut5-practica-consola` (1 punto)

### Ejercicio 5 (1 punto)

Este proyecto debe incluir el JAR de `ut5-practica-component`.  

- Crear una única clase con un método `main`.  
- Establecer una conexión a la base de datos y probar los métodos del componente.  
- Mostrar los resultados por consola. **No se permite entrada por teclado.**  
- Manejar errores mostrando mensajes descriptivos.  

**Nota.** Inicialmente, se recomienda crear esta clase en el proyecto del componente para facilitar las pruebas.  

## 6. `ut5-practica-gui` (1 punto)

### Ejercicio 6 (1 punto)

Utilizar una interfaz gráfica para:  

1. Solicitar al usuario el código de un servidor y sus datos de conexión (IP/dominio, SGBD, puerto).  
2. Incluir un botón para actualizar los datos del servidor en la base de datos.  
3. Manejar errores mostrando mensajes gráficos.  

## 7. Entrega

Entregar en el aula virtual un archivo ZIP que contenga:  

1. Un archivo SQL con las respuestas de la parte SQL.  
2. Un ZIP para cada uno de los tres proyectos (código completo).  
3. Los JARs de los tres proyectos.  

## 8. Evaluación

- Cada apartado indica su puntuación sobre 10.  
- No seguir las normas de nomenclatura o formato de Java penalizará hasta un 10% de la nota del ejercicio.  
- Esta práctica representa el 8.33% de la nota de actividades del curso.
