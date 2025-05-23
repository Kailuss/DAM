# **Ejercicios TEMA 4.** <br>ORM

## Instrucciones

1. Sigue el documento _4.2 Instrucciones ORM_ para configurar un proyecto para utilizar JPA.
2. En el fichero _persistence.xml_ modifica la url de manera que utilice la base de datos _interinos_
3. Crea el paquete _cat.paucasesnovescifp.spadd__d.ut4_ y una clase con _main_ dentro de este paquete 
    

#### Datos de la conexión  

**Host**: daw.paucasesnovescifp.cat
**Puerto**: 3306
**Base de datos**: interinos
**Usuario**: usuario
**Contraseña**: seCret_24

**Importante**: La base de datos se reinicializa cada noche a las tres de la madrugada. Si, por ejemplo, hoy hacéis insertos o updates mañana no los encontraréis.

  

## Ejercicios

1. Crea el paquete _cat.paucasesnovescifp.spadd__d.ut4.auxiliares_
    1. Crea una excepción al paquete _cat.paucasesnovescifp.spadd.__ut4.auxiliares_. Utilizala para controlar los errores de la aplicación.
2. Crea el paquete _cat.paucasesnovescifp.spadd__d.ut4__.__modelo_
    1. Crea una clase entidad para representar la tabla _Islas_. Debe tener el constructor sin parámetros, el constructor con parámetros para todos los atributos, todos los getters y setters, el _toString_ y el _ecuales_ y el _hashcode_.
        
        Ninguno de estos atributos puede ser nulo, y las cadenas de texto tampoco pueden estar vacías ni sólo de espacios.
        
    2. A la clase con main recupera la manzana con _id 072_ y muestrala por pantalla_._
        
3. Copia dentro del paquete _cat.paucasesnovescifp.spadd__d.ut4__.__modelo_ las clases de entidad que encontrarás en el aula virtual.
    
    1. En la clase de entidad _Illa_ añade un atributo que represente la relación entre las tablas Islas y Localidades. Crea los getters y setters, pero no lo incluyas en el _toString_, _ecuales_ ni _hashcode_.
        
    2. En la clase con _main_ cuando hayas recuperado la isla recupera sus localidades y muestralas por pantalla. Qué pasa si intentamos acceder a la lista de localidades cuando el EntityManager ya está cerrado, por ejemplo fuera del try? Pone un println explicándolo.
        
4. Crea el paquete _cat.paucasesnovescifp.spadd.__ut4.controller_ con una clase llamada _Persistencia_. En la clase _Persistencia:_
    
    1. Crea un atributo de tipo cadena llamado _unidadPersistencia_. No se debe poder asignar una cadena nula, vacía o sólo de espacios a este atributo.
        
    2. Crea el constructor con un parámetro para el atributo.
        
    3. Crea el getter de el atributo.
        
    4. Crea los métodos. Pruebalos todos desde el main mostrando los datos que devuelve los métodos si es que lo hacen:
        
        1. _getAspirant__(String nif)_: vuelve el aspirante asociado al nif que recibe como parámetro.
            
        2. _modificaLlinajesAspirante(String nif, String linajes)_: recupera al aspirante con el nif solicitado, le cambia los linajes por el parámetro que ha recibido y guarda los cambios en la base de datos. En la base de datos linajes (y nombre tampoco) no puede ser nulo, por tanto modifica la clase Aspirante de manera que no permita valores nulos, cadenas vacías o todas blancos.
            
        3. _actualizaAspirante(Aspirante aspirante)_: Actualiza la base de datos con el objeto que recibe como parámetro.
            
        4. _g__etLocalidad(String idLocalidad):_ vuelve la localidad asociada al identificador.
            
        5. _inserta(Object objeto)_: Inserta cualquier objeto que le pasamos a la base de datos. Pruebalo añadiendo una isla.
            
        6. _actualiza(Object objeto)_: Actualiza cualquier objeto que le pasamos a la base de datos.
            
        7. _borra__(Object objeto)_: Borra cualquier objeto que le pasamos a la base de datos.
            
        8. _c__reaAspirante(paramos)_: Crea un aspirante con los parámetros que recibe y lo guarda dentro de la base de datos.
            
        9. _creaPreferencia(paramos)_: Crea una preferencia con las datos que recibe como parámetros y la guarda en la base de datos.mysql