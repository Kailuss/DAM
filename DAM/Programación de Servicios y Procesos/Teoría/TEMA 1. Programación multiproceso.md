---
number headings: max 3, _.1.1., skip ^sk
tags:
  - DAM
  - PSP
banner: "![[psp.jpg]]"
banner_y: 0.32
cssclasses:
  - dam-psp
  - table-compact-clean
---

# **TEMA 1.** <br>Programación Multiproceso

```audio-player
[[Lecturas/Lectura_Tema_1_Programación_multiproceso.mp3]]
00:00:03 --- 1. Recordando cómo programar en Java y uso básico de NetBeans
00:01:09 --- 2. Introducción: Aplicaciones, Ejecutables y Procesos
00:02:58 --- 3. Gestión de procesos
00:10:19 --- 4. Programación concurrente
00:12:42 --- 5. Comunicación entre procesos
00:14:56 --- 6. Sincronización entre procesos
00:22:24 --- 7. Requisitos: seguridad, vivacidad, eficiencia y reusabilidad
00:25:39 --- 8. Programación paralela y distribuida
```

## 1. Recordando cómo programar en Java y el uso básico del IDE NetBeans

Java es un lenguaje de programación de alto nivel, orientado a objetos, que combina compilación e interpretación. Los programas Java se compilan a un lenguaje intermedio llamado **bytecode**, que es ejecutado por la **Java Virtual Machine (JVM).** La JVM actúa como un traductor entre el bytecode, el sistema operativo y el hardware, permitiendo que los programas Java sean multiplataforma.

La **plataforma Java** incluye la JVM y la **API Java**, un conjunto de bibliotecas (paquetes) que facilitan el desarrollo de aplicaciones. Las versiones principales de la plataforma son:

- **Java SE (Standard Edition).** Para aplicaciones en desktops, servidores y entornos empotrados.
- **Java EE (Enterprise Edition).** Orientada a aplicaciones empresariales en servidores.
- **Java ME (Micro Edition).** Para dispositivos móviles y empotrados.

Para desarrollar aplicaciones Java, se utiliza un **IDE (Entorno Integrado de Desarrollo)**, como NetBeans, que incluye herramientas como editor, compilador, depurador y control de versiones.

## 2. Introducción: Aplicaciones, Ejecutables y Procesos

Una **aplicación** es un programa diseñado para resolver un problema específico del usuario, como editar imágenes, enviar correos o navegar en Internet. A diferencia de otros programas (sistemas operativos, utilidades de mantenimiento, etc.), las aplicaciones están orientadas a tareas concretas.

Un **programa** es un conjunto de instrucciones que realizan una tarea. Los programadores escriben el **código fuente**, que se compila o interpreta para generar un **fichero ejecutable** (binario o interpretado). Este fichero contiene el código que el ordenador ejecuta.

Un **proceso** es un programa en ejecución. Mientras que un ejecutable es un fichero, un proceso es una entidad activa gestionada por el sistema operativo. Una aplicación puede involucrar varios procesos, ejecutables y librerías.

### 2.1. **Ejecutables. Tipos**

Los ejecutables pueden clasificarse según su tipo de código:

| Ejecutables                                                                     |   |
| ------------------------------------------------------------------------------- | - |
| **Binarios** | Contienen instrucciones directamente ejecutables por el procesador. Son específicos de una plataforma (no multiplataforma). Ejemplos: ejecutables de C o C++. |
| **Interpretados** | Contienen código que es traducido por un intérprete (como la JVM en Java). Son más propensos a ser multiplataforma. Ejemplos: bytecode de Java. |
| **Scripts** | Son ejecutables interpretados no compilados. Se pueden abrir y editar como texto plano. Ejemplos: JavaScript, Python, scripts de Bash. |
| **Librerías** | Contienen funciones reutilizables que son invocadas por otros programas. Ejemplos: DLL en Windows, API de Java. |

En sistemas como Windows, los ejecutables tienen extensión .**exe**, mientras que en GNU/Linux se identifican por permisos de ejecución.

## 3. Gestión de procesos

Los sistemas operativos modernos son **multitarea**, permitiendo la ejecución simultánea de múltiples procesos. El sistema operativo gestiona cómo estos procesos comparten los recursos del procesador, alternando entre ellos para simular la ejecución simultánea.

Los procesos pueden clasificarse en:

| Procesos                                                                     |   |
| ------------------------------------------------------------------------------- | - |
| **Por lotes** | Tareas que se ejecutan sin interacción del usuario hasta su finalización. Ejemplo: impresión de documentos. |
| **Interactivos** | Procesos que requieren interacción constante con el usuario. Ejemplo: un procesador de textos. |
| **Tiempo real** | Procesos donde el tiempo de respuesta es crítico. Ejemplo: sistemas de control en automóviles o brazos robóticos. |

### 3.1. **Introducción**

En un sistema multitarea, como Windows o GNU/Linux, múltiples aplicaciones se ejecutan simultáneamente. Aunque el microprocesador ejecuta miles de millones de instrucciones por segundo, el sistema operativo (SO) gestiona qué proceso utiliza la CPU en cada momento. El SO asigna un tiempo de ejecución (quantum) a cada proceso, y cuando este tiempo termina, el proceso vuelve a la cola de espera para ceder la CPU a otro proceso.

Los sistemas modernos con múltiples núcleos pueden ejecutar varios procesos en paralelo, pero el SO sigue siendo necesario para gestionar la distribución de recursos entre los procesos activos, incluyendo los del propio sistema operativo.

### 3.2. **Estados de un proceso**

Un proceso pasa por varios estados durante su ciclo de vida:

| Estados del proceso                                                             |   |
| ------------------------------------------------------------------------------- | - |
| **Nuevo** | Proceso recién creado. |
| **Listo** | Proceso esperando su turno para usar la CPU |
| **En ejecución** | Proceso actualmente utilizando la CPU. |
| **Bloqueado** | Proceso esperando la finalización de una operación de entrada/salida (E/S). |
| **Suspendido** | Proceso movido a memoria secundaria para liberar RAM. |
| **Terminado** | Proceso que ha finalizado su ejecución.

El SO gestiona las transiciones entre estos estados, asegurando que los procesos avanzan de manera equitativa y eficiente.

### 3.3. **Planificación de procesos por el Sistema Operativo**

El SO utiliza un **planificador** para decidir qué proceso se ejecuta y durante cuánto tiempo. El planificador sigue un **algoritmo de planificación**, como:

| Algoritmos de planificación                                                            |   |
| ------------------------------------------------------------------------------- | - |
| **Round-Robin** | Cada proceso recibe un quantum de tiempo en la CPU. Si no termina, vuelve al final de la cola.  |
| **Por prioridad** | Los procesos con mayor prioridad se ejecutan primero. |
| **Múltiples colas** | Combina Round-Robin y prioridades, gestionando colas separadas para diferentes niveles de prioridad. |

El objetivo de la planificación es equilibrar la equidad, eficiencia, tiempo de respuesta y rendimiento del sistema.

#### Creación de procesos

El **cargador** es responsable de crear procesos. Cuando se inicia un proceso, el cargador:

- Reserva espacio en la memoria principal para el proceso.
- Crea una estructura de datos llamada **PCB (Bloque de Control de Proceso)**, que incluye:
   - Identificador del proceso (PID).
   - Estado actual del proceso.
   - Espacio de direcciones de memoria.
   - Información para la planificación (prioridad, quantum, etc.).
   - Registros de la CPU (contador de programa, puntero a pila, etc.).

El PCB permite al SO gestionar y controlar cada proceso de manera individual.

### 3.4. **Cambio de contexto en la CPU**

El **cambio de contexto** ocurre cuando el SO pasa la CPU de un proceso a otro. Durante este cambio, el SO guarda el estado actual de la CPU (registros, contador de programa, etc.) y restaura el estado del proceso que va a ejecutarse. Este mecanismo es esencial para la multitarea, permitiendo que múltiples procesos compartan la CPU de manera eficiente.

### 3.5. **Servicios e hilos**

- **Hilos (threads).** Son unidades de ejecución dentro de un proceso. Comparten la memoria y recursos del proceso, pero ejecutan tareas independientes. Los cambios de contexto entre hilos son más rápidos que entre procesos, ya que no requieren guardar y restaurar todos los registros de la CPU.
  
- **Servicios.** Son procesos que se ejecutan en segundo plano, generalmente iniciados durante el arranque del sistema. Esperan solicitudes para realizar tareas específicas, como el servicio de impresión, que gestiona la cola de trabajos de impresión.

### 3.6. **Creación de procesos en Java**

En Java, la creación de procesos se realiza utilizando las clases `java.lang.Process` y `java.lang.Runtime`. El método `Runtime.exec(String comando)` permite lanzar la ejecución de un programa externo, devolviendo un objeto `Process` que representa el proceso en ejecución.

**Ejemplo.** Para abrir múltiples instancias de un editor de texto, se puede utilizar el siguiente código:

```java
Runtime.getRuntime().exec("ruta/al/editor.jar");
```

Este código lanza un nuevo proceso del editor de texto cada vez que se ejecuta, permitiendo la edición simultánea de varios documentos.

### 3.7. **Comandos para la gestión de procesos**

Los comandos son esenciales para la gestión de procesos, ya que permiten interactuar directamente con el sistema operativo. Aunque las interfaces gráficas son comunes, los comandos ofrecen un control más preciso y son fundamentales en la administración de sistemas, especialmente en entornos remotos.

#### Trucos para usar comandos
- **Nombres de comandos.** Suelen estar relacionados con la tarea que realizan (en inglés o siglas). Por ejemplo:
  - **tasklist** (Windows): Muestra un listado de procesos.
  - **ps** (GNU/Linux): Muestra el estado de los procesos (siglas de "process status").
- **Sintaxis.** `nombreDelComando [opciones]`.
- **Manuales.** En GNU/Linux, usa `man nombreDelComando`; en Windows, `nombreDelComando /?`.

#### Comandos útiles

| Windows                                                             |   |
| ------------------------------------------------------------------------------- | - |
| **`tasklist`** | Lista los procesos activos, mostrando el nombre del ejecutable, PID y uso de memoria. |
| **`taskkill`** | Termina procesos. Ejemplo: `taskkill /PID <ID>`. |

| GNU/Linux                                                           |   |
| ------------------------------------------------------------------------------- | - |
| **`ps`** | Lista los procesos. Con la opción `aux`, muestra todos los procesos del sistema. |
| **`pstree`** | Muestra los procesos en forma de árbol, indicando relaciones entre ellos. |
| **`kill`** | Envía señales a procesos. Ejemplo: `kill -9 <PID>` para terminar un proceso. |
| **`killall`** | Termina procesos por nombre. Ejemplo: `killall nombreDeAplicacion`. |
| **`nice`** | Cambia la prioridad de un proceso. Ejemplo: `nice -n 5 comando`. |

### 3.8. **Herramientas gráficas para la gestión de procesos**

Además de los comandos, existen herramientas gráficas para gestionar procesos:

| Windows                                                             |   |
| ------------------------------------------------------------------------------- | - |
| **Administrador de tareas.** | Muestra procesos activos, uso de CPU, memoria, y permite finalizar procesos o cambiar su prioridad. |
| **SysInternals.** | Herramientas avanzadas como **Process Explorer** (información detallada de procesos) y **Process Monitor** (actividad de E/S y hilos). |

| GNU/Linux                                                           |   |
| ------------------------------------------------------------------------------- | - |
| **Monitor del sistema.** | Similar al Administrador de tareas de Windows, muestra procesos, uso de recursos y permite gestionarlos. |

## 4. Programación concurrente

La programación concurrente se refiere a la ejecución simultánea de múltiples procesos o hilos que compiten por recursos o necesitan comunicarse entre sí. Esto es esencial en sistemas modernos, donde los procesos no se ejecutan de forma aislada.

### 4.1. **¿Para qué concurrencia?**

| Razones para usar concurrencia |                                                                                              |
| ------------------------------------------ | -------------------------------------------------------------------------------------------- |
| **Optimización de recursos.**              | Permite solapar operaciones de E/S con ejecución de CPU, reduciendo tiempos de inactividad   |
| **Interactividad.**                        | Mejora la experiencia del usuario al permitir la ejecución simultánea de tareas.             |
| **Disponibilidad.**                        | En servidores, permite atender múltiples solicitudes de clientes de forma simultánea.        |
| **Diseño modular.**                        | Facilita la creación de aplicaciones más claras y mantenibles.                               |
| **Protección.**                            | Aísla tareas en procesos independientes, permitiendo su finalización sin afectar al sistema. |

### 4.2. **Beneficios de la concurrencia**

|Beneficios| |
| - | - |
|**Claridad**|Facilita la comprensión de lo que cada proceso debe hacer.|
|**Reducción de tiempo de ejecución**|En sistemas multiprocesador, los procesos se ejecutan en paralelo.|
|**Flexibilidad de planificación**|Permite priorizar procesos urgentes.|
|**Modelado más fiable**|Facilita el diseño y análisis de programas.|

### 4.3. **Condiciones de competencia**

Los procesos concurrentes pueden interactuar de tres formas:

- **Independientes.** Solo compiten por la CPU.
- **Cooperantes.** Un proceso produce información que otro consume.
- **Competidores.** Necesitan acceder a los mismos recursos de forma exclusiva.

#### Conceptos clave
- **Región crítica.** Conjunto de instrucciones donde un proceso utiliza un recurso de forma exclusiva.
- **Lock (bloqueo).** Un proceso obtiene acceso exclusivo a un recurso.
- **Deadlock (interbloqueo).** Situación en la que dos o más procesos no pueden continuar porque cada uno está esperando un recurso que otro tiene bloqueado.

#### Ejemplo de deadlock

Imagina un cruce de caminos con cuatro coches:

- Cada coche necesita dos regiones del cruce para avanzar.
- Si todos avanzan al mismo tiempo y bloquean las regiones que necesitan, quedan interbloqueados, sin poder continuar.

## 5. Comunicación entre procesos

Los procesos tienen espacios de memoria privados, lo que impide que accedan directamente a los datos de otros procesos. Sin embargo, en ocasiones, los procesos necesitan comunicarse o compartir recursos. Para ello, se utilizan mecanismos de comunicación proporcionados por los lenguajes de programación y el sistema operativo.

### 5.1. **Mecanismos básicos de comunicación**

Los procesos pueden comunicarse de dos formas principales:

- **Intercambio de mensajes.** Utiliza primitivas como `send` (enviar) y `receive` (recibir). Los mensajes pueden transmitirse a través de:
   - **Buffers de memoria.** Para procesos en la misma máquina.
   - **Sockets.** Para procesos en máquinas diferentes, conectados por red.

- **Recursos compartidos.** Utiliza primitivas como `read` (leer) y `write` (escribir) para acceder a recursos comunes, como memoria o archivos.

En Java, los sockets y buffers se manejan como flujos de datos (`streams`), utilizando métodos como `read` y `write`. Las operaciones de lectura y escritura son **bloqueantes**, lo que significa que un proceso se detiene hasta que la operación se completa.

### 5.2. **Tipos de comunicación**

La comunicación entre procesos puede clasificarse según:

#### 

|Dirección del flujo de información| |
| --- | --- |
|**Símplex.**|La comunicación es unidireccional (ejemplo: emisión de radio).|
|**Dúplex (Full Duplex).**|La comunicación es bidireccional y simultánea (ejemplo: telefonía).|
|**Semidúplex (Half Duplex).**|La comunicación es bidireccional, pero no simultánea (ejemplo: walkie-talkies).|

|Sincronía| |
| --- | --- |
|**Síncrona.**|El emisor espera a que el receptor reciba el mensaje antes de continuar.|
|**Asíncrona.**| El emisor continúa su ejecución inmediatamente después de enviar el mensaje.|
|**Invocación remota.**|El emisor espera confirmación del receptor antes de continuar.|

|Simetría| |
| --- | --- |
|**Simétrica.**|Todos los procesos pueden enviar y recibir mensajes.|
|**Asimétrica.**|Solo un proceso actúa como emisor, y los demás como receptores.|

## 6. Sincronización entre procesos

La sincronización es esencial cuando varios procesos acceden a recursos compartidos o necesitan coordinarse. Sin mecanismos de sincronización, pueden surgir inconsistencias, como en el caso de múltiples procesos leyendo y escribiendo en un mismo archivo.

### 6.1. **Regiones críticas**

Una **región crítica** es un conjunto de instrucciones que acceden a un recurso compartido y deben ejecutarse de forma **atómica** (indivisible) y **exclusiva.** Esto evita que otros procesos accedan al recurso mientras se está modificando.

#### Características de las regiones críticas
- Solo un proceso puede estar en su región crítica a la vez.
- Los demás procesos esperan fuera de la región crítica.
- Al finalizar, el recurso se libera para que otros procesos lo usen.

En Java, las regiones críticas se implementan utilizando mecanismos como **bloqueos (locks)** o **sincronización de hilos**, que veremos en unidades posteriores.

**Ejemplo:**
En un sistema donde múltiples procesos incrementan un valor en un archivo, la secuencia **leer-incrementar-escribir** debe ser una región crítica para evitar inconsistencias.

#### Categoría de proceso cliente-suministrador

En la programación concurrente, los procesos pueden clasificarse como **cliente** o **suministrador** (también llamado **servidor** en algunos contextos).

- **Cliente.** Es un proceso que solicita información o servicios de otro proceso.
- **Suministrador.** Es un proceso que proporciona información o servicios a otros procesos. Puede hacerlo a través de memoria compartida, archivos, red, etc.

La comunicación entre cliente y suministrador se basa en un **protocolo**, que define las reglas para el intercambio de mensajes. Esta comunicación puede ser síncrona o asíncrona, y puede utilizar recursos compartidos o intercambio de mensajes.

#### Sincronización entre cliente y suministrador

Para garantizar la correcta comunicación entre cliente y suministrador, se necesitan mecanismos de sincronización que aseguren:

- **El cliente no lee datos incompletos.** El cliente debe esperar a que el suministrador haya producido completamente el dato antes de leerlo.
- **El suministrador no desborda al cliente.** El suministrador no debe escribir datos si el cliente no está listo para recibirlos.

Un enfoque sencillo es utilizar una **variable compartida** que indique si el dato está listo para ser leído. Sin embargo, este enfoque puede ser ineficiente debido a la **espera activa**, donde el cliente consume tiempo de CPU sin realizar tareas útiles.

### 6.2. **Semáforos**

Los **semáforos** son una herramienta de sincronización que permite controlar el acceso a recursos compartidos en un entorno concurrente. Funcionan como un semáforo de tráfico, indicando cuándo un proceso puede acceder a un recurso y cuándo debe esperar.

#### Tipos de semáforos

- **Semáforos binarios.** Solo pueden tomar los valores 0 (cerrado) o 1 (abierto).
- **Semáforos generales.** Pueden tomar cualquier valor entero no negativo.

#### Operaciones con semáforos

- **wait().** Si el semáforo está abierto (valor > 0), decrementa su valor y permite el acceso al recurso. Si está cerrado (valor = 0), el proceso se bloquea y se añade a una lista de espera.
- **signal().** Si hay procesos en espera, despierta a uno de ellos. Si no hay procesos en espera, incrementa el valor del semáforo.

#### Uso de semáforos

- Un proceso padre crea e inicializa el semáforo.
- Los procesos hijos acceden al recurso compartido utilizando `wait()` antes de entrar en la región crítica y `signal()` al salir.

#### Ventajas y desventajas

- **Ventajas.** Son fáciles de entender y proporcionan una solución eficiente para la sincronización.
- **Desventajas.** Su bajo nivel de abstracción los hace propensos a errores, como **interbloqueos** (deadlocks), y su gestión puede ser complicada.

En Java, los semáforos están implementados en la clase `Semaphore` del paquete `java.util.concurrent`.

### 6.3. **Monitores**

Los **monitores** son una abstracción de alto nivel que encapsula recursos compartidos y garantiza el acceso a ellos en **exclusión mutua.** A diferencia de los semáforos, los monitores proporcionan una interfaz clara y segura para acceder a los recursos.

**Características de los monitores**

- **Encapsulación.** Los recursos compartidos y las operaciones sobre ellos están encapsulados dentro del monitor.
- **Exclusión mutua.** Solo un proceso puede ejecutar un método del monitor a la vez.
- **Lista de espera.** Los procesos que intentan acceder al monitor mientras está ocupado se bloquean y se añaden a una lista de espera.

**Ventajas de los monitores**

- **Uniformidad.** Proporcionan una única forma de gestionar la exclusión mutua.
- **Modularidad.** El código de sincronización está separado del resto del programa.
- **Simplicidad.** El programador no necesita preocuparse por los detalles de la sincronización.

**Desventajas de los monitores**

- **Complejidad.** Cuando hay múltiples condiciones de sincronización, el código del monitor puede volverse complejo.

En Java, aunque no existe una clase `Monitor`, se pueden implementar monitores utilizando semáforos o sincronización de hilos.

#### Lecturas y escrituras bloqueantes en recursos compartidos

En Java, las operaciones de lectura y escritura en recursos compartidos (como archivos o sockets) pueden ser **bloqueantes**, lo que significa que el proceso se detiene hasta que la operación se completa. Esto es útil para sincronizar procesos cliente y suministrador.

#### Ejemplo de uso
- **Cliente.** Lee datos de un recurso compartido utilizando métodos como `read()`.
- **Suministrador.** Escribe datos en el recurso compartido utilizando métodos como `write()`.

En Java, las clases `FileChannel` y `SocketChannel` (del paquete `java.nio.channels`) permiten realizar operaciones bloqueantes de lectura y escritura, y también proporcionan métodos como `lock()` para implementar regiones críticas.

### 6.4. **Memoria compartida**

La **memoria compartida** es una forma natural de comunicación entre procesos, donde varios procesos pueden acceder a la misma zona de memoria. Sin embargo, los sistemas operativos modernos protegen la memoria de cada proceso, haciéndola privada. A pesar de esto, la **programación multihilo** (varios hilos dentro de un mismo proceso) permite compartir memoria entre hilos, lo que facilita la comunicación y sincronización.

En sistemas **multiprocesador** o **distribuidos**, la memoria compartida se utiliza para dividir tareas grandes en partes más pequeñas, asignando cada parte a un procesador o núcleo diferente. Esto permite resolver problemas complejos más rápidamente, aunque requiere una cuidadosa gestión de la sincronización y la división de tareas.

### 6.5. **Cola de mensajes**

El **paso de mensajes** es una técnica de comunicación entre procesos que no requiere memoria compartida. Los elementos principales son:

- **Emisor.** Proceso que envía el mensaje.
- **Receptor.** Proceso que recibe el mensaje.
- **Mensaje.** Información transmitida.

**Tipos de paso de mensajes**

- **Asíncrono.** El emisor no espera a que el receptor reciba el mensaje. Se utilizan **buzones** o **colas** para almacenar mensajes pendientes.
- **Síncrono.** El emisor espera a que el receptor reciba el mensaje antes de continuar. También se conoce como **encuentro** o **rendezvous.**

El paso de mensajes es fundamental en sistemas distribuidos, donde los procesos se comunican a través de redes.

## 7. Requisitos: seguridad, vivacidad, eficiencia y reusabilidad

Los programas concurrentes deben cumplir requisitos de calidad, como:

**Propiedades de seguridad ("safety")**
- **Exclusión mutua.** Dos procesos no deben entrar simultáneamente en una región crítica.
- **Sincronización.** El consumidor no debe consumir datos antes de que el productor los haya producido, y el productor no debe producir datos si el buffer está lleno.

**Propiedades de vivacidad ("liveness")**
- **Evitar bloqueos activos (livelock).** Los procesos no deben ejecutar tareas que no conduzcan a un progreso constructivo.
- **Evitar aplazamiento indefinido (starvation).** Ningún proceso debe quedar indefinidamente sin acceso a los recursos.
- **Evitar interbloqueos (deadlock).** Los procesos no deben quedar bloqueados esperando recursos que nunca obtendrán.

**Eficiencia y reusabilidad**
- **Eficiencia.** Utilizar solo los recursos necesarios y optimizar el código.
- **Reusabilidad.** Diseñar el código de forma modular y documentarlo adecuadamente.

### 7.1. **Arquitecturas y patrones de diseño**

#### Arquitecturas de software
- **Monolítica.** Software estructurado en grupos funcionales muy acoplados.
- **Cliente-servidor.** Divide la carga de cómputo entre clientes (consumidores) y servidores (proveedores).
- **Tres niveles.** Divide el software en capas de presentación, lógica de negocio y almacenamiento.
- **Orientada a servicios (SOA).** Basada en servicios independientes que se comunican a través de interfaces estándar.

#### Patrones de diseño
- **Ventajas.** Facilitan el diseño de programas complejos, promueven la reusabilidad y son bien conocidos.
- **Ejemplos.** Patrones como **Productor-Consumidor** o **Observador** son comunes en programación concurrente.

### 7.2. **Documentación**

La documentación es esencial para entender y mantener el código. En Java, se utilizan:

- **Comentarios Javadoc.** Para documentar clases, métodos y variables.
- **Comentarios de una línea (`//`).** Para explicar fragmentos de código.
- **Comentarios de bloque (`/* ... */`).** Para desactivar código o explicar secciones largas.

En aplicaciones concurrentes, es importante documentar:

- Las **condiciones de sincronización.**
- Las **regiones críticas** y los recursos compartidos que protegen.

### 7.3. **Dificultades en la depuración**

Depurar programas concurrentes es más complejo que depurar programas secuenciales debido a:

- **Errores de temporización.** Dependen del orden de ejecución de los procesos.
- **Interferencias entre procesos.** Cuando varios procesos acceden a recursos compartidos.
- **Falta de herramientas.** Las herramientas de depuración no siempre están preparadas para manejar concurrencia.

#### Herramientas de depuración
- **Depurador de NetBeans.** Útil para depurar hilos dentro de un mismo proceso.
- **Volcados de actividad.** Registrar la ejecución en un archivo de log.
- **Herramientas específicas.** Como **TotalView** o **StreamIt Debugger Tool.**

## 8. Programación paralela y distribuida

### 8.1. **Conceptos básicos**

- **Programación paralela.** Ejecución simultánea de tareas en sistemas con múltiples núcleos o procesadores.
- **Programación distribuida.** Ejecución de tareas en sistemas heterogéneos conectados por redes.

#### Taxonomía de Flynn
- **SISD (Single Instruction, Single Data).** Arquitectura secuencial.
- **SIMD (Single Instruction, Multiple Data).** Misma instrucción aplicada a múltiples datos.
- **MISD (Multiple Instruction, Single Data).** Múltiples instrucciones aplicadas a un solo dato.
- **MIMD (Multiple Instruction, Multiple Data).** Múltiples instrucciones aplicadas a múltiples datos.

#### Sistemas distribuidos
- **Clusters.** Conjunto de ordenadores conectados para trabajar en tareas comunes.
- **Grids.** Clusters conectados a través de Internet.

### 8.2. **Tipos de paralelismo**

- **A nivel de bit.** Incrementar el tamaño de la palabra del procesador (ejemplo: 32 bits a 64 bits).
- **A nivel de instrucciones.** Uso de **pipeline** para ejecutar múltiples instrucciones simultáneamente.
- **A nivel de bucle.** Dividir iteraciones de bucles para ejecutarlas en paralelo.
- **A nivel de procedimientos.** Ejecutar fragmentos de código de forma simultánea.
- **A nivel de tareas.** Ejecutar tareas independientes en paralelo.
- **A nivel de aplicación.** Gestión de procesos por el sistema operativo.

#### Granularidad
- **Grano fino.** Paralelización automática de pequeñas secciones de código.
- **Grano grueso.** Paralelización de grandes secciones de código, optimizando el rendimiento.

### 8.3. **Modelos de infraestructura para programación distribuida**

- **Sockets.** Comunicación de bajo nivel entre procesos.
- **RPC (Remote Procedure Call).** Invocación remota de procedimientos.
- **RMI (Remote Method Invocation).** Invocación remota de métodos en objetos distribuidos.
- **CORBA (Common Object Request Broker Architecture).** Estándar para aplicaciones cliente-servidor.
- **MPI (Message Passing Interface).** Protocolo para comunicación entre nodos en sistemas distribuidos.
