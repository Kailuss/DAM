# **Ejercicios TEMA 6.1.** <br>MongoDB

## Instrucciones

- Realiza los ejercicios en la consola de Compass y engancha las pedidos a un fichero de texto.
- Entrega un pdf con el contenido del fichero anterior.

## Ejercicios

- En tu base de datos crea una colección llamada *aspirantes* utilizando createCollection.
- En el compass refresca la base de datos si no ves la colección acabada de crear.
- Importa el contenido del fichero *aspirantsComplet.json* dentro de la colección que has creado.
	
### find

1. Selecciona todos los aspirantes
	
2. Selecciona a los aspirantes de nombre Bartomeu.
	
3. Selecciona a los aspirantes que sean de la localidad *CALONGE.*
	
4. Encuentra el aspirante con NIF 47537490F
	
5. Encuentra a los aspirantes que sean de Calonge y nomin Bartomeu. No utilices and.
	
6. Busca a los aspirantes que sean de Calonge y nomin Bartomeu. Utiliza and.
	
7. Busca a los aspirantes que sean de Calonge o nomin Bartomeu.
	
8. Muestra los aspirantes que sean de Muro o de Sant Rafel. Utiliza oro.
	
9. Muestra los aspirantes que sean de Muro o de Sant Rafel. Utiliza in.
	
10. Muestra a los aspirantes que no sean de Muro o de Sant Rafel. Utiliza nin.

### Proyecciones y suerte

11. Selecciona a todos los aspirantes y ordenalos alfabéticamente por los linajes y el nombre.
	
12. Selecciona todos los aspirantes y ordenalos alfabéticamente por los nombre de la localidad, linajes y nombre.
	
13. Muestra el nif, el nombre y los linajes de todos los aspirantes ordenados por linajes y nombre.
	
14. Muestra toda la información de los aspirantes excepto _id ordenados por linajes y nombre.
	
15. Muestra el nif, el nombre y los linajes de los aspirantes que tengan alguna preferencia de la especialidad con idCos=0590 e idEspecialidad=107 ordenados por linajes y nombre.

### Update, ..

16. Inserta en la colección *aspirantes* un nuevo aspirante sólo con el nif, nombre y linajes.
	
17. Inserta en la colección *aspirantes* dos nuevos aspirantes sólo con el nif, nombre y linajes.
	
18. Modifica el nombre de uno de los aspirantes acabado de insertar.
	
19. Añade el campo "adresa" al aspirante que estamos manipulando.
	
20. Cambia el nombre del campo adresa por dirección a todos los que lo tengan.
	
21. Añade al aspirante un campo teléfonos con un array con, de momento un solo teléfono.
	
22. Utiliza push para añadir dos teléfonos más al arriendo del aspirante utilizando each.
	
23. Comprueba que addToSet no permite duplicados.
	
24. Elimina el primer teléfono de el array con pulpo.
	
25. Elimina al aspirante con lo que debemos trabajando.

### aggregate

26. Utiliza *aggregate* para filtrar a los aspirantes con nombre Bartomeu.
	
27. Modifica la instrucción anterior de manera que sólo muestre las propiedades nombre y linajes.
	
28. Modifica la instrucción anterior de manera que muestre los resultados ordenados alfabéticamente por linajes.
	
29. Modificala de nuevo por mostrar un único campo con el formato *linajes, nombre*.
	
30. Muestra el nombre completo de los 10 primeros aspirantes.
	
31. Muestra a los aspirantes entre los 10 y los 20 primeros (ordenados por nombreComplet).
	
32. Extrae las localidades de la colección, de manera que sean únicas, utilizando $group. Tienes que volver a _id y el nombre, la isla no hace falta. Ordena las localidades por nombre.
	
33. Crea la colección *l__ocalidades* con los datos del ejercicio anterior.
