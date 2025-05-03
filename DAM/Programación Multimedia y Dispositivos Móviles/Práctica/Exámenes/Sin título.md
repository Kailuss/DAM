---
cssclasses:
  - dam-pmdm
  - table-clean
---
# EXAMEN PRÁCTICO

Pautas de realización (indicar en primer lugar si el trabajo es individual o en grupo):
Instrucciones:

- Puedes utilizar los recursos que tengas en tu ordenador, así como consultar Internet.
- Está prohibido usar cualquier programa/herramienta para compartir archivos y/o comunicarse con compañeros/as. Si se detecta, se asignará una calificación de cero en toda la prueba de síntesis.
- Recuerda justificar las respuestas mediante comentarios.
- Cada pregunta tiene una puntuación asignada.

Realiza los siguientes supuestos prácticos. Recuerda que puedes utilizar apuntes relacionados con la asignatura y consultar Internet. Para ser evaluado, debes entregar el enlace del proyecto de GitHub con modo público en la tarea habilitada en el aula virtual antes del tiempo máximo establecido. No hacerlo a tiempo implicará que no se ha realizado el ejercicio correspondiente.  

Recuerda hacer un commit inicial cuando hayas creado el proyecto y realizar varios commits durante el examen. Justifica en cada apartado, o página, qué tipo de Widget (con estado o sin estado) empleas y para qué, puedes hacerlo con un comentario de párrafo. ¡Recuerda comentar el código!  

El primer apartado será crear una aplicación desde cero, llamada: `examen_final_primerllintage` y publicarla en Git inmediatamente.  

## Ejercicio 1 (4 puntos)  

En primer lugar, para hacer la aplicación segura, deberás acceder con un login que solicite un usuario y una contraseña. Una vez iniciada sesión, la aplicación almacenará localmente las credenciales introducidas y redirigirá al `HomeScreen`. Cabe mencionar que en el `HomeScreen` debe haber algún botón para hacer "logout".  

Si cerramos la aplicación y la volvemos a abrir, pueden pasar dos cosas:  

1. Si habíamos iniciado sesión satisfactoriamente y tenemos las credenciales almacenadas, se redirigirá sin necesidad de ninguna acción al `HomeScreen`.  
2. En caso de no haber iniciado sesión nunca o haber cerrado sesión, se iniciará la pantalla de login con los campos de credenciales vacíos.  

En ambos casos, la aplicación debería iniciarse desde el login.  

## Ejercicio 2 (4 puntos)  

Cuando estamos en el `HomeScreen`, encontraremos un listado de platos que están almacenados en una base de datos de Firebase. Implementa una Fake API mediante Firebase que dé soporte a esta aplicación. Se debe tener en cuenta que todos los atributos de un plato tendrán valor siempre, excepto `foto`, que puede ser `null` en algún caso concreto.  

También se puede emplear la siguiente API:  

```
https://examen-practic-sim-default-rtdb.europe-westl.firebasedataloa
se.app/plats.json
```  

(Para los que vean el enunciado en papel, encontrarán el enlace en el aula virtual, junto a la tarea de entrega).  

Los diferentes platos tienen la siguiente estructura en formato JSON:  

```json
{
    "nom": "Sandvitx Mixte",
    "descripcio": "Sandvitx de York i Formatge",
    "tipus": "Sandvitxos/Bocadillos",
    "disponible": true,
    "restaurant": "Bar Triton",
    "geo": "40.4165,-3.7026",
    "foto": "https://tl.uc.ltmedn.com/es/posts/0/6/9/como_hacer_un_sandwich_mixto_33960_orig.jpg"
}
```

### Ejercicio 2.1 (2 puntos)  

Muestra el listado de platos que hay. Debe mostrarse solo: `nom` y la `foto`. Recordar que `foto` puede ser `null` (mostrar imagen por defecto).  

### Ejercicio 2.2 (2 puntos)  

Muestra el detalle de un plato cuando se hace clic sobre él. De este deberás mostrar todos los campos en formato de texto, excepto `disponible`, que debe verse con alguna utilidad "booleana", y la imagen, que debes visualizar mediante algún widget.  

## Ejercicio 3 (2 puntos)  

Implementa una funcionalidad que se active con algún botón desde la pantalla de detalle. Esta funcionalidad consiste en mostrar la geolocalización del restaurante que hace el plato, mediante un Google Maps.  

### Criterios de calificación  

El examen práctico cuenta con **7.5 puntos sobre 10.** La nota final está compuesta por:  

- Nota tipo test (25%) + Nota Práctica (75%).  

**Puntuación sobre 10:**  
- **Ejercicio 1:** 4 puntos  
- **Ejercicio 2.1:** 2 puntos  
- **Ejercicio 2.2:** 2 puntos  
- **Ejercicio 3:** 2 puntos  

**Se valorará:**  
- **Funcionamiento correcto de la aplicación en todos los casos (60%).**  
- **Comentarios explicativos del código, justificaciones y claridad (15%).**  
- **Resolución eficiente, nomenclatura correcta y tabulaciones adecuadas (25%).**  
