---
tags:
  - DAM
  - PSP
cssclasses:
  - table-compact-clean
  - dam-psp
banner: "![[psp.jpg]]"
banner_y: 0.25
number headings: off
---

# **Examen de PSP**

## Ejercicio 1.
Explica y pon ejemplos de:  
1. Qué es un proceso. Explica qué es un proceso padre e hijo y cómo pueden comunicarse entre sí en Java.
2. Modelos OSI y TCP/IP. Capas y función.
3. Describe dos protocolos vistos que pertenecen a la capa de aplicación del modelo TCP/IP.
4. Las etapas o estados por los que pasa un proceso durante su ciclo de vida. Se recomienda un esquema además de una breve explicación de cada uno de ellos.
5. Cuáles son las diferencias entre procesos e hilos. Pon ejemplos de cómo se declara cada uno de ellos en el lenguaje Java.
6. Cuáles son los mecanismos de sincronización existentes. Describe cada uno de ellos (ventajas, diferencias, etc.), pon ejemplos y explica cómo se instancian en Java.

---

## Ejercicio 2.
Explica y pon ejemplos utilizando Java y/o pseudocódigo sobre los hilos:  
1. ¿Cómo se crea un proceso en Java?
2. ¿Cómo se llama un proceso en Java?
3. ¿Cómo se puede pasar información entre procesos en Java?
4. ¿Cuáles son las formas de declarar hilos?
5. ¿Cómo se puede ejecutar un hilo según la forma en que ha sido creado?
6. ¿Cómo se pueden bloquear hilos y por qué motivo? Pon un ejemplo de alguna forma de hacerlo.
7. Mecanismos de Sincronización en Java: `Semaphore` y `Synchronized` + `wait/notify`.

---

## Ejercicio 3.
Trata de construir un programa parecido a un chat, usando un protocolo orientado a conexión. Para realizar este ejercicio, la estructura tiene que ser Cliente-Servidor, donde habrá un único servidor y múltiples hilos cliente. Explica todo lo que puedas y realiza un programa en Java o pseudocódigo que simule el funcionamiento.

La idea es que los clientes envíen mensajes al servidor, este los imprima por pantalla y les responda con el mensaje “Mensaje recibido”. Para añadir control de concurrencia, necesitamos que los mensajes recibidos por el servidor, además de imprimirse, también se almacenen en un fichero.

---

## Ejercicio 4.
En el ejercicio anterior, queremos mejorar la seguridad del sistema. Por eso, implementa un método de encriptación (si es posible) que consideres apropiado para proteger la comunicación entre el cliente y el servidor, y viceversa.

---

## Ejercicio 5.
Crea la siguiente aplicación en Java:
1. Escribe un programa llamado “ExercicisMultiproces1_ParellSenar”. Este recibirá un número entero positivo y deberá mostrar el resultado “Parell” si es par o “Senar” si es impar.
2. Escribe un programa llamado “ExercicisMultiproces1”. Este creará un proceso hijo para ejecutar el programa “ParellSenar” anterior. El proceso padre mostrará por pantalla “Introdueix un nombre:” y el usuario podrá introducir:
    - Un número entero positivo: en ese caso se creará el proceso hijo y se mostrará el resultado de su ejecución.
    - La palabra “exit”: en ese caso se terminará la ejecución del programa.
    

**Ejemplo:**

```plaintext
Introdueix un nombre:
10
Parell
Introdueix un nombre:
15
Senar
Introdueix un nombre:
30
Parell
Introdueix un nombre:
exit
BUILD SUCCESSFUL (total time: 9 seconds)
```

---

## Ejercicio 6.
Escribe un programa que haga lo siguiente:  
1. Crear un proceso hijo llamado `ExercicisMultiproces2_ModificarString`.
2. El proceso padre (llamado `ExercicisMultiproces2`) y el proceso hijo se comunicarán de forma bidireccional utilizando streams.
3. El padre leerá líneas desde su entrada estándar y las enviará a la entrada estándar del hijo (utilizando el `OutputStream` del hijo).
4. El hijo leerá el texto desde su entrada estándar, lo transformará todo a letras mayúsculas y sustituirá todas las vocales por el símbolo de guion bajo `_`. 
5. El padre imprimirá por pantalla lo que reciba del hijo mediante el InputStream del mismo. 
6. Cuando el padre hable, la salida en pantalla debe comenzar con: `El PADRE dice:` y cuando hable el hijo debe comenzar con: `El Hijo dice:`

**Ejemplo:**

```terminal
hello, world!
El PADRE dice: El hijo dice: H_LL_, W_RLD!
BUILD SUCCESSFUL (total time: 10 seconds)
```

**Tienes que crear dos proyectos:**

- `ExercicisMultiproces2` (padre)
- `ExercicisMultiproces2_ModificarString` (hijo)
    

---

## Ejercicio 7.
Se trata de construir un programa llamado TICTACTOC. La idea es que al ejecutarse imprima por pantalla la secuencia TIC – TAC – TOC. Cada hilo imprimirá la palabra correspondiente y la irá concatenando dentro de una variable compartida entre todos. Una vez que todos los hilos hayan terminado, el programa principal imprimirá esa variable compartida por pantalla.
    

Ten en cuenta que la ejecución por pantalla debe seguir el orden TIC – TAC – TOC – TIC – TAC – TOC, etc., pero la variable puede quedar con otro orden, por ejemplo:  
`tictactoctoctictactactoc` o `tictictictactoctoctoctictac`

Escribe en Java o pseudocódigo todas las clases que consideres necesarias.

---

## Ejercicio 8.

La topología de red en anillo se caracteriza por formar una conexión circular, en la que cada nodo solo puede comunicarse con el siguiente, hasta cerrar el anillo.
    

Simula esta topología en anillo usando **Datagram Sockets**, donde cada nodo (ordenador) será un Datagrama. El primer nodo iniciará la transmisión enviando su ID. Cada nodo, al recibir un mensaje, le concatenará su propio ID y lo reenviará al siguiente. La comunicación finaliza cuando el anillo se cierra.

El resultado final podría ser:

```
Impreso desde el NODO1: Nodo1 Nodo2 Nodo3 Nodo4
```

Escribe en Java o pseudocódigo todas las clases necesarias para esta simulación.

---

## Ejercicio 9.
De los siguientes protocolos, escoge uno. Ubícalo dentro de una de las capas del modelo TCP/IP, explica todo lo que sepas sobre él (puedes usar esquemas si lo deseas) y pon un ejemplo de uso en pseudocódigo o Java. Protocolos: `DNS`, `SMTP`, `FTP` o `HTTP`.
    

---

## Ejercicio 10.
Explica cómo se realiza la **comunicación a través de SSL** y pon un ejemplo de utilización del protocolo. Puedes usar pseudocódigo o Java.