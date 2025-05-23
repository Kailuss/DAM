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

# **Ejercicios TEMA 2.2.** <br>Streams

## Instrucciones

1. Crea un proyecto para hacer los ejercicios o aprovecha el del bloque de ejercicios anterior.
    
2. Crea un paquete donde guardarás todas las clases creadas en estos ejercicios.
    
3. Crea otro paquete con una clase con main. Desde esta clase prueba todos los métodos creados en los ejercicios.
    
4. Crea una excepción para tratar los errores propias de la aplicación ( o reaprovecha la del bloque anterior).
    
5. Propaga las excepciones hasta el main y tratándolas allí.
    
6. Descarga del aula virtual la versión adecuada a tu sistema de el _Himno de los piratas de Mar y Cielo_ y el fichero del _Tirant Lo Blanc_.
    

## Ejercicios

1. Crea una clase de utilidad llamada Herramientas_ByteStream_ con los siguientes métodos estáticos. Podéis declarar la clase _abstract_ porque no crearemos objetos a partir de ella.
    
    1. En la clase _PruebasStreams_ crea un método llamado _pruebasByte_ desde donde llaves todos los métodos que programarás en los ejercicios siguientes. Para el ejercicio 5, utiliza una imagen o un pdf o zip que tengas en el disco duro. La copia debe quedar idéntica al original.
        
    2. _escribeByte(String desti,_ _byte[]_ _datos)_ Guarda en el fichero _dest__í_ el texto contenido dentro _de datos_. Pruebalo creando un array de bytes y también pasándole los bytes de un String ("Hola Llorenç".getBytes()).
        
    
    3. _t__ornaBytes(String origen)_ Recibe como parámetro un String con la ruta de un fichero. Lee el fichero byte a byte y vuelve un array con este bytes, de manera que la aplicación pueda tratarlos de la manera más adecuada. _Sugerencia: Ponte dentro de un ArrayList<Byte> y luego pasa su contenido a un byte[]_.
        
    4. _copiaBytes__(__String origen, String desti)_ Copia dentro del fichero _destino_ el contenido del fichero _origen_. Pruebalo con una imagen que tengas en el ordenador.
        
2. Crea otra clase abstracta llamada _Herramientas__CharacterStream_ con los métodos estáticos
    
    1. _muestraCharacters__(String origen)_. Recibe como parámetro un String con la ruta de un fichero con el texto con acentos, por ejemplo el _Himno de los piratas_. Lee el fichero carácter carácter y lo muestra por consola.
        
    2. _escribeCharacters_(String desti, String datos) Guarda en el fichero _destino_ el texto contenido dentro de datos.
        
    3. _copiaCharacters_(String origen, String desti) . Copia dentro del fichero _destino_ el contenido del fichero _origen_.
        
    4. En la clase _PruebasStreams_ crea un método p_rovesCharacterStream_ que llame a los métodos creados anteriormente. Utiliza la versión adecuada del Himno de los piratas.
        
    5. Copia la clase _Cronometro_ del aula virtual en el paquete _auxiliar_.
        
    6. Copia el método _muestraCharacters_ con el nombre _inutil_. Llevale la salida por consola. Utiliza la clase _Cronometro_ para mostrar por pantalla el tiempo que tarda el método _inutil_ para leer el fichero del _Tirant lo Blanc__._
        
3. Crea otra clase abstracta _Herramientas__BufferedStream_ con los métodos estáticos
    
    1. _tornaLine_. Recibe como parámetro un String con la ruta del fichero con el texto con acentos. Lee el fichero línea a línea, las guarda dentro de un ArrayList y vuelve este ArrayList.
        
    2. _escribeLine(String desti, String[] datos)_ Guarda en el fichero _destino_ el texto contenido dentro del array de cadenas _datos_. En el fichero se debe ver cada string en una línea (out.newLine());
        
    3. _copiaLine(String origen, String desti)._ Copia dentro del fichero _destino_ el contenido del fichero _origen_.
        
    4. En la clase _PruebasStreams_ crea un método p_rovesBufferedStream_ que llame a los métodos creados anteriormente. Utiliza la versión adecuada del Himno de los piratas.
        
    5. En la clase Herramientas_BufferedStream c_rea un método _inutil_ que lea las líneas del fichero _Tirant lo Blanc_ sin mostrarlas por pantalla ni devolverlas dentro de ningún array. Utiliza la clase _Cronometro_ para mostrar por pantalla el tiempo que tarda el método _inutil_ en ejecutarse. Compara el resultado con el de leer el mismo fichero carácter a carácter.
        
4. Crea otra clase _Herramientas__DataStream_ con los métodos estáticos:
    
    1. _escribeDades(String desti, double[] datos)_ Escribe en el fichero _desti_ la longitud del array y luego uno a uno todos los elementos de el array.
        
    2. _double[] leeDades(String origen)_ Lee los datos que se han escrito en el fichero _origen_ y vuelve un array con los datos que ha leído.
        
    3. En la clase _PruebasStreams_ crea un método _pruebasDataStream_ que llame a los métodos creados anteriormente. Contestau con un println:Que pasa si no las leí en el mismo orden que ¿se han escrito?
        
5. Nos queda hacer una última prueba con ObjectStream's. Por ello:
    
    1. Crea en el paquete _auxiliar__s_ una clase _Datos_ con un atributo _numerico_ de tipo int y un _alfanumerico_ de tipo String. Añadale un constructor con los dos parámetros, los getters y los setters. Genera automáticamente el ecuales y el hashCode, y el toString.
        
    2. Haz lo que se tenga que hacer para que los objetos de la clase _Datos_ se puedan enviar a un _stream_.
        
    3. Crea una última clase _Herramientas__ObjectStream_ con los siguientes métodos estáticos:
        
        1. _escribeObjeto_. Recibe como parámetro la ruta del fichero destino donde se guardará el objeto, y **cualquier objeto** que se pueda enviar a un Stream.
            
        2. _leeObje._ Recibe como parámetro el fichero origen y vuelve un objeto que habrá leído de este fichero.
            
        3. En la clase _PruebasStreams_ añade el método _pruebasObjetoSimple_. Dentro crea un objeto de la clase _Datos_ y utiliza los métodos anteriores para guardarlo en un fichero y recuperarlo. Muestra por pantalla el objeto que has leído y el resultado de _ecuales_ comparando el objeto que has escrito y el que has leído.
            
    4. Crea una nueva clase _DatosComplejos_ en el paquete _auxiliar__s_. Tendrá como atributos un String _identificador_ y un objeto _datos_ de la clase _Datos_. Añadale un constructor con los dos parámetros, los getters y los setters. Genera automáticamente el ecuales y el hashCode y el toString.
        
        1. En la clase _PruebasStreams_ añade el método _pruebasObjetoComplexe_. Dentro crea un objeto de la clase _DatosComplejos_ y utiliza los métodos de la clase _Eine__sObjectStream_ para guardarlo en un fichero y recuperarlo. Muestra por pantalla el objeto que has leído y el resultado de _ecuales_ comparando el objeto que has escrito y el que has leído.
            
        2. Añade ahora el método _pruebasObjectLlista_. Dentro de este método crea un ArrayList<Dades> y utiliza uno for para guardar 10 objetos con el campo numérico=index y el campo alfanumeric="Somos el objeto "+index, donde _index_ es la variable del foro. Pasa la lista al método _escribeObject__e_. Utiliza el método _leeObject__e_ para recuperar la lista. Muestre por pantalla, mostrando a la misma línea el objeto original y el leído.
            
        3. Crea finalmente el método _pruebasMantenerReferencies_.
            
            1. Dentro de este método crea un ArrayList<Dades>.
                
            2. Crea un objeto _original_ de la clase _Datos_. Añadiéndolo dos veces a la lista.
                
            3. Cambia el valor del campo _numerico_ de el objeto y escribí la lista entera por pantalla. Tiene que haber cambiado a los dos objetos que aparecen.
                
            4. Guarda la lista a un fichero. Recuperala y asignándola a la variable _recuperada._ Muestra el contenido de esta lista por pantalla. Debe ser el mismo que ha escrito antes.
                
            5. Se habrán mantenido las ¿referencias? Cambia el campo _numérico_ al primer elemento de la lista. Vuelve mostrar la lista por pantalla. ¿Se han mantenido las referencias?