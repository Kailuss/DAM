**Un programa en ejecución es:**

- [ ] Una aplicación.

- [x] Un proceso.

- [ ] Un ejecutable.

Muy bien. Las aplicaciones, y en general los programas, se guardan en ficheros ejecutables, que al ejecutarse en el ordenador se convierten en procesos. Veremos en próximos apartados cómo el SO es el encargado de gestionar los procesos en ejecución de forma eficiente e intenta evitar que haya conflictos en el uso que hacen de los distintos recursos del sistema.

---

**Los ficheros ejecutables binarios, ¿funcionarán, sin recompilarlos, en cualquier plataforma?**

- [ ] Sí.

- [x] No.

Muy bien. Has captado la idea. No son los ficheros binarios, sino los interpretados. Los lenguajes interpretados, permiten que, en muchos casos, casi sin modificaciones en el código, podremos ejecutar nuestros programas en cualquier plataforma para la que esté disponible e instalado el correspondiente intérprete, sin recompilaciones en cada tipo de plataforma. En sistemas de 32 ó 64 bits, en Windows o GNU/Linux, etc.

---

**Un proceso se encuentra en estado Bloqueado cuando:**

- [ ] Está preparado para la ejecución de sus instrucciones.

- [ ] Ha sido llevado a un medio de almacenamiento secundario.

- [x] Está a la espera de que finalice una operación de E/S.

Así es. Un proceso se bloquea hasta que finaliza la operación de E/S que hubiera solicitado. Una vez que finalice esta operación, el proceso vuelve a estar Listo.

---

**¿Qué es un algoritmo de planificación?**

- [ ] Es la forma en la que el Sistema Operativo decide dónde cargar en memoria los procesos.

- [x] Es el que determina el comportamiento del gestor de procesos del Sistema Operativo.

Respuesta correcta. Recuerda que el gestor de procesos es el que se encarga de decidir qué proceso es ejecutado y durante cuánto tiempo. Esa decisión la toma de acuerdo al algoritmo de planificación que esté utilizando.

---

**El estado de la CPU está formado por todos los registros que la forman y sus circuitos operacionales. Toda esa información es la que hay que almacenar cuando se produce un cambio de contexto. ¿Cierto o falso?**

- [x] Falso.

- [ ] Cierto.

Así es. Todo es cierto salvo que los circuitos operacionales son circuitos electrónicos físicos y no forman parte del estado de la CPU, es la parte Hardware que realiza las operaciones.

---

**Es imposible lanzar la ejecución de cualquier aplicación desde una aplicación java.**

- [ ] Cierto.

- [x] Falso.

Por supuesto que es falso, sólo necesitamos conocer el comando que lanza la ejecución de la aplicación. Podemos comenzar escribiendo la ruta de acceso al ejecutable de la aplicación y pulsar intro; se lanzará la ejecución de la aplicación (si tenemos privilegios para ello).

---

**El comando `kill` en sistemas GNU/Linux se utiliza únicamente para matar procesos.**

- [ ] Cierto.

- [x] Falso.

Por supuesto que es falso. El comando `kill` envía distintos tipos de señales a los procesos, una de ellas, la señal de finalización forzosa, es la señal -9.

---

**El Administrador de tareas nos proporciona información sobre los archivos y recursos que está utilizando un proceso.**

- [ ] Falso.

- [x] Cierto.

---

**La concurrencia permite que la productividad de los equipos informáticos...**

- [x] Mejore.

- [ ] Empeore.

Correcto. El rendimiento mejora ya que, entre otras cosas, permite que se aprovechen mejor los recursos del sistema y a la larga permite que se finalice mayor número de tareas por unidad de tiempo.

---

**¿Qué nombre recibe la situación en la que varios procesos no pueden continuar su ejecución porque no pueden conseguir todos los recursos que necesitan para ello?**

- [ ] Región crítica.

- [x] Deadlock.

- [ ] Condición de competencia.

Es correcto. Esa situación recibe el nombre de deadlock o interbloqueo.

---

**Las primitivas de sincronización que utilizamos en nuestras aplicaciones, las proporcionan:**

- [ ] El sistema operativo.

- [ ] Los lenguajes de programación.

- [ ] El proceso.

- [x] Los lenguajes de programación y sistemas operativos.

Estás en lo cierto. Los sistemas operativos proporcionan los mecanismos de comunicación, que los lenguajes de programación encapsulan en objetos y métodos para que podamos incluirlos en la implementación de nuestras aplicaciones.


**¿Qué significa que una primitiva de comunicación sea bloqueante?**

- [ ] No existen primitivas de comunicación bloqueantes.

- [x] Los procesos que ejecuten una de estas primitivas, quedarán bloqueados o suspendidos de ejecución, hasta que se cumplan todas las especificaciones de esa primitiva.

Correcto. Dependiendo del tipo de primitiva, si utilizamos una implementación que sea bloqueante, el proceso quedará bloqueado hasta que se cumplan todas las especificaciones de esa primitiva. Por ejemplo, una primitiva bloqueante de lectura en un canal de comunicación, bloqueará el proceso hasta que haya un dato a leer y haya sido entregado al proceso.

**¿Cómo clasificarías, de entre las siguientes opciones, la emisión de una emisora de radio?**

- [ ] Dúplex, síncrona y simétrica.

- [ ] Semi-dúplex, asíncrona y simétrica.

- [x] Símplex, asíncrona y asimétrica.

- [ ] Símplex, síncrona y asimétrica.

Correcto. El mensaje sólo viaja del emisor a los receptores. El emisor sigue emitiendo independientemente de si los receptores están recibiendo o no el mensaje. Sólo hay un emisor, el resto de interlocutores, son receptores.

**Todas las aplicaciones que funcionan como se espera de forma aislada, también lo harán en un entorno de ejecución concurrente.**

- [ ] Cierto.

- [x] Falso.

Claro que es falso. Habrá aplicaciones que dé igual que se ejecuten en un entorno concurrente como que no. Pero, si la aplicación hace uso de un recurso compartido y no incluimos en la implementación mecanismos de sincronización, sus resultados serán impredecibles y por lo tanto, no serán correctos.

**Cuando una aplicación va a ejecutarse en un entorno concurrente, debemos incluir todas las instrucciones de la aplicación protegidas en la misma región crítica.**

- [ ] Cierto.

- [x] Falso.

Claro que es falso. Sólo las instrucciones que acceden a un recurso compartido, son susceptibles de ser protegidas en una sección crítica, y, es más, podemos y debemos definir regiones críticas independientes para cada grupo de instrucciones que deban ser ejecutadas en exclusión mutua y de forma atómica; además de intentar que esas regiones críticas abarquen el mínimo de instrucciones imprescindibles.

**No es necesario el uso de primitivas específicas de programación concurrente para la sincronización de procesos. Los lenguajes de programación secuenciales, ya nos proporcionan mecanismos eficientes para resolver los problemas de sincronización.**

- [ ] Cierto.

- [x] Falso.

Sí, es falso. Las soluciones que podemos implementar a los problemas de sincronismo con lenguajes secuenciales, serán ineficientes, al implicar incluir un bucle que simule un bloqueo en un proceso esperando a que una variable cambie de valor.

**¿Podemos resolver el problema de sincronización de los procesos suministrador y cliente que comparten un dato con un semáforo?**

- [x] Sí.

- [ ] No.

Por supuesto que sí. Sólo tenemos que pensar cómo conseguimos el sincronismo que deseamos entre esos procesos utilizando un semáforo. Por ejemplo: el suministrador ejecutará `semaforoDato.signal()`; y el cliente, `semaforoDato.wait()`.

**Cuando invoco un método sobre un objeto que, implica el acceso a un recurso y, su definición me indica que, el proceso quedará bloqueado en ese método a la espera de se complete la tarea, y, que garantiza que sólo este proceso estará haciendo uso de ese recurso en ese instante, ¿estoy utilizando un monitor?**

- [x] Sí.

- [ ] No.

Sí, es así, aunque el objeto por el que estás accediendo al recurso no se llame Monitor, su funcionamiento e implementación se corresponden con lo que hemos definido en este apartado.

**Un proceso suministrador puede escribir datos en un recurso compartido al ritmo que desee, no tiene restricciones al generar datos.**

- [ ] Cierto.

- [x] Falso.

Sí, es falso. El proceso suministrador debe respetar el ritmo de consumo (de servicios o datos) del proceso cliente, ya que si genera el servicio o la información más rápido de lo que es consumida, desbordará al cliente y hará que éste pierda información.

**En los sistemas actuales, no hay ninguna posibilidad de compartir zonas de memoria entre distintos procesos.**

- [ ] Cierto.

- [x] Falso.

Sí, es falso. La programación multihilo y los sistemas de multiprocesamiento actual, pueden utilizar sistemas de memoria compartida (implementados por el lenguaje de programación o soportados por el sistema operativo específico) para resolver problemas complejos computacionalmente.

**La sincronización de procesos por paso de mensajes, necesita de la existencia memoria compartida entre los procesos que se están comunicando.**

- [ ] Cierto.

- [x] Falso.

Sí, es falso. El paso de mensajes es una técnica que permite sincronización entre procesos y exclusión mutua, sin memoria compartida.

**Entre las siguientes marca las propiedades de calidad del** software **específicas en el desarrollo de aplicaciones concurrentes:**

- [ ] Eficiencia.

- [ ] Reusabilidad.

- [x] Seguridad.

- [x] Vivacidad.

Todas son propiedades relativas a la calidad del software, pero aplicadas específicamente a programación concurrente son Seguridad y Vivacidad.

**La depuración de aplicaciones concurrentes es exactamente igual de compleja que la depuración de aplicaciones secuenciales.**

- [ ] Sí.

- [x] No.

Estás en lo cierto. Como hemos visto, para depurar un programa concurrente, tendremos que comprobar la corrección de cada una de sus instrucciones como en los programas secuenciales;  y,  además, que su comportamiento global las cumpla.

**Marca, de entre las siguientes, la característica que diferencia la programación paralela de la distribuida.**

- [x] La programación paralela trabaja sobre computadores homogéneos y la distribuida sobre heterogéneos.

- [ ] La programación paralela trabaja sobre computadores heterogéneos y la distribuida sobre homogéneos.

