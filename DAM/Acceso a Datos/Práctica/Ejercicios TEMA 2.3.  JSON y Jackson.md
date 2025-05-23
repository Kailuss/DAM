# **Ejercicios TEMA 2.3.** <br>JSON y Jackson

## Instrucciones

1. Crea un proyecto nuevo, si puede ser con _maven_.
    
2. Incluye al proyecto jackson-databind y sus dependencias.
    
3. Crea un paquete con el nombre correcto con una clase ejecutable.
    
4. Crea dos paquetes dentro de lo anterior, uno para mantener las clases del modelo de datos y un otro para mantener las clases del controlador.
    
5. Utiliza una excepción propia para tratar los errores de la aplicación.
    
6. A no ser que se diga lo contrario la única clase que puede imprimir por pantalla es la que tiene el main.
    

## Ejercicios

1. Al controlador crea un método que devuelva el json de un objeto. Tenéis que crear este json a mano, siempre puede ser lo mismo. El objeto debe tener un atributo de tipo cadena, uno de tipo booleano, otro numérico y un array con unos cuantos enteros.
    
2. Al controlador crea un método que devuelva el json de un array con dos objetos como los del ejercicio anterior.
    
3. Utiliza _Jackson_ para tratar el contenido del fichero _modul.json_ que encontrarás en el aula virtual.
    
    1. Dentro del package _model_ crea una clase _Modul_ que pueda contener toda la información del fichero json. No utilices tipos primitivos, es decir, en lugar de int utiliza Integer.
        
        Programa los constructores(sin parámetros y con parámetros para todos los atributos), getters, setters, toString, ecuals y hashcode.
        
    2. En la clase controlador crea un método que pueda recibir por parámetro la ruta de un fichero que contienda un módulo. Debe devolver un objeto de la clase que he hecho en el ejercicio anterior.
        
    3. Desde la clase con _main_ llama el método anterior y muestra el resultado por pantalla.
        
    4. En la clase controlador crea un método que reciba por parámetro la ruta de un fichero y un objeto de tipo Modulo_._ Debe escribir el json de este objeto dentro del fichero.
        
    5. Desde el main crea un objeto de la clase Modulo y llama al método anterior pasándole la ruta del fichero y el objeto. Comprueba desde el navegador de archivos que el fichero se ha generado correctamente.
        
4. Repite el ejercicio 3 (con todos sus puntos) con fichero _curs.json_. Tendrás que crear una clase dentro del paquete _modelo_ para poder guardar la información de este fichero.
    
    La clase Curso deberás tener un atributo de tipo _ArrayList<Modulo>_ Al generar el fichero te debes asegurar que el nombre del ciclo aparezca antes de la lista de módulos.
    
5. Modifica la clase _Módulo_ de manera que no se incluyan en los json los atributos con valor null.
    
    Al _main_ crea un objeto de la clase _Modul_ con algún atributo con valor null. Comprueba que si lo escribes a un fichero con el método del controlador creado en el ejercicio 3.4 este No se ha incluido.
    
6. Modifica la clase _Ciclo_ de manera que no se incluya el atributo _código_ a los json.
    
    Al _main_ crea un objeto de la clase _Ciclo_. Comprueba que si lo escribes en un fichero con el método del controlador creado en el ejercicio 4.4 este atributo no se ha incluido.