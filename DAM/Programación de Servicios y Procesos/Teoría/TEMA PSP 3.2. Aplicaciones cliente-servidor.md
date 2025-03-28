---
tags: [DAM, PSP]
cssclasses: [dam-psp, table-compact-clean]
banner: "![[psp.jpg]]"
banner_y: 0.32
---

# **TEMA 3.2. **<br>Aplicaciones cliente-servidor

## 1. Paradigma Cliente/Servidor

El modelo Cliente/Servidor es el más utilizado en comunicaciones entre equipos debido a su flexibilidad, interoperabilidad y estabilidad. Surgió en los años 80 para describir un paradigma simple: un cliente solicita un servicio a un servidor. Funcionalmente, es una arquitectura distribuida que permite el acceso transparente a recursos en entornos multiplataforma, como datos, hardware o tiempo de procesamiento.

**Elementos del modelo**

**Cliente.** Proceso que interactúa con el usuario, realiza peticiones, las envía al servidor y muestra los resultados. Actúa como interfaz (front-end) y sus funciones incluyen interactuar con el usuario, validar peticiones, recibir resultados y formatearlos para su visualización.

**Servidor.** Proceso que recibe y procesa peticiones de clientes para permitir el acceso a recursos (back-end). Sus funciones son aceptar peticiones, procesarlas, enviar resultados, gestionar la lógica de la aplicación, asegurar la consistencia de la información y mantener la seguridad del sistema.

El modelo divide la funcionalidad del software en dos módulos (cliente y servidor) para facilitar el desarrollo y el mantenimiento.

### 1.1. **Características básicas**

- **Combinación de cliente y servidor.** El cliente interactúa con el usuario, mientras que el servidor gestiona los recursos compartidos.
- **Diferencias en el procesamiento.** El servidor realiza el trabajo pesado, mientras que el cliente se enfoca en la interacción con el usuario.
- **Relación entre procesos.** Los procesos pueden ejecutarse en uno o varios equipos distribuidos en la red.
- **Distinción de funciones.** Basada en el concepto de "servicio", donde un servidor puede atender a múltiples clientes.
- **Comunicación por mensajes.** Las interacciones se realizan mediante el intercambio de mensajes.
- **Heterogeneidad.** Los clientes pueden utilizar sistemas diferentes, permitiendo la conexión independientemente de la plataforma.

### 1.2. **Ventajas y desventajas**

**Ventajas.**
- Uso de clientes ligeros, ya que el servidor realiza el procesamiento.
- Facilita la integración entre sistemas y el uso de interfaces gráficas.
- Mantenimiento y desarrollo rápidos gracias a herramientas existentes.
- Escalabilidad y capacidad de crecimiento de la infraestructura.
- Acceso centralizado a recursos y compartición de información entre clientes.

**Desventajas.**
- Mayor dificultad en el mantenimiento debido a la interacción de hardware y software.
- Necesidad de estrategias para manejo de errores y seguridad.
- Requiere mecanismos de sincronización para garantizar la consistencia de la información.

### 1.3. **Modelos**

Los modelos Cliente/Servidor se clasifican según el número de capas (tiers):

- **1 capa (1-tier).** Cliente y servidor están en el mismo equipo. No se considera un modelo cliente/servidor real.
- **2 capas (2-tiers).** Modelo tradicional con un servidor y clientes diferenciados. No es escalable y puede sobrecargarse con muchas peticiones.
- **3 capas (3-tiers).** Incluye un servidor de aplicación y un servidor de datos para mejorar el rendimiento.
- **n capas (n-tiers).** Permite añadir capas adicionales de servidores para separar funcionalidades y mejorar el rendimiento.

### 1.4. **Programación**

**Pasos del servidor.**
1. Publicar el puerto para recibir conexiones.
2. Esperar peticiones de clientes y crear un socket para la comunicación.
3. Enviar y recibir datos mediante flujos de entrada y salida.
4. Cerrar el socket una vez finalizada la comunicación.

**Pasos del cliente.**
1. Conectarse al servidor en un puerto específico.
2. Enviar y recibir datos mediante flujos de entrada y salida.
3. Cerrar el socket al finalizar.

### 1.5. **Ejemplo I**

Ejemplo básico en Java donde un servidor acepta tres clientes de forma secuencial y les indica su número de cliente.

**Servidor.java.**

```java
import java.io.*;
import java.net.*;

class Servidor {
    static final int Puerto = 2000;

    public Servidor() {
        try {
            ServerSocket sServidor = new ServerSocket(Puerto);
            System.out.println("Escucho el puerto " + Puerto);

            for (int nCli = 0; nCli < 3; nCli++) {
                Socket sCliente = sServidor.accept();
                System.out.println("Sirvo al cliente " + nCli);
                DataOutputStream flujo_salida = new DataOutputStream(sCliente.getOutputStream());
                flujo_salida.writeUTF("Hola cliente " + nCli);
                sCliente.close();
            }
            System.out.println("Se han atendido los clientes");
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public static void main(String[] arg) {
        new Servidor();
    }
}
```

**Compilación y ejecución.**

```bash
javac Servidor.java
java Servidor
```

El servidor procesa las solicitudes de tres clientes y les envía un mensaje indicando su número de cliente.

## 2. Optimización de sockets

Para garantizar un funcionamiento eficiente y seguro en aplicaciones cliente-servidor, es crucial optimizar el uso de sockets. Esto implica atender múltiples peticiones simultáneamente, asegurar la integridad y seguridad del sistema, y monitorizar los tiempos de respuesta.

### 2.1. **Atender múltiples peticiones simultáneas**

En un servidor tradicional, cada cliente es atendido de forma secuencial, lo que limita la capacidad de manejar múltiples conexiones al mismo tiempo. Para solucionar esto, se utiliza un enfoque concurrente donde cada cliente es atendido por una hebra (thread) independiente. Esto permite que el servidor maneje varias conexiones simultáneamente.

**Implementación.**
- Un bucle infinito (`while(true)`) espera conexiones de clientes.
- Cuando un cliente se conecta, se crea un nuevo thread para atenderlo.
- Cada thread gestiona la comunicación con su cliente correspondiente.

**Código básico.**

```java
while(true) {
    Socket skCliente = skServidor.accept(); 
    System.out.println("Cliente conectado");
    new Servidor(skCliente).start(); // Atiende al cliente en un thread
}
```

### 2.2. **Threads**

Los threads permiten ejecutar tareas de forma concurrente. Para implementar un servidor concurrente, se extiende la clase `Thread` y se sobrescribe el método `run()`, que contiene las tareas que realizará el thread.

**Estructura básica.**

```java
class Servidor extends Thread {
    Socket skCliente;

    public Servidor(Socket sCliente) {
        skCliente = sCliente;
    }

    public void run() {
        // Tareas que realiza la hebra
    }
}
```

### 2.3. **Ejemplo II**

**Servidor concurrente en Java.**

```java
import java.io.*;
import java.net.*;

class Servidor extends Thread {
    Socket skCliente;
    static final int Puerto = 2000;

    public Servidor(Socket sCliente) {
        skCliente = sCliente;
    }

    public static void main(String[] arg) {
        try {
            ServerSocket skServidor = new ServerSocket(Puerto);
            System.out.println("Escucho el puerto " + Puerto);

            while(true) {
                Socket skCliente = skServidor.accept();
                System.out.println("Cliente conectado");
                new Servidor(skCliente).start();
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public void run() {
        try {
            DataInputStream flujo_entrada = new DataInputStream(skCliente.getInputStream());
            DataOutputStream flujo_salida = new DataOutputStream(skCliente.getOutputStream());

            flujo_salida.writeUTF("Se ha conectado el cliente de forma correcta");
            skCliente.close();
            System.out.println("Cliente desconectado");
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
```

**Cliente básico en Java.**

```java
import java.io.*;
import java.net.*;

class Cliente {
    static final String HOST = "localhost";
    static final int Puerto = 2000;

    public Cliente() {
        try {
            Socket sCliente = new Socket(HOST, Puerto);
            DataInputStream flujo_entrada = new DataInputStream(sCliente.getInputStream());
            DataOutputStream flujo_salida = new DataOutputStream(sCliente.getOutputStream());

            String datos = flujo_entrada.readUTF();
            System.out.println(datos);

            sCliente.close();
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public static void main(String[] arg) {
        new Cliente();
    }
}
```

### 2.4. **Pérdida de información**

En las comunicaciones de red, la pérdida de paquetes es un problema común. Para evitarlo, se utiliza un mecanismo de confirmación (ACK) donde el receptor envía un paquete de confirmación al emisor por cada paquete recibido correctamente. Si el emisor no recibe el ACK en un tiempo determinado, retransmite el paquete.

**Mejoras.**
- **Envío de múltiples paquetes.** El emisor puede enviar varios paquetes sin esperar confirmaciones individuales, mejorando la eficiencia.
- **Control de paquetes.** Se utiliza un vector para llevar un registro de los paquetes enviados y confirmados. Este vector se desplaza a medida que se reciben confirmaciones, permitiendo enviar nuevos paquetes.

**Ejemplo de vector de ACK.**

|   |   |   |   |   |   |   |   |   |   |   |
| - | - | - | - | - | - | - | - | - | - | - |
| Mensaje | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| ACK     | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |

En este ejemplo, los mensajes 0, 1, 4 y 5 han sido confirmados. El vector se desplaza para permitir el envío de nuevos mensajes (10, 11, etc.) mientras se espera la confirmación de los restantes.

Este enfoque mejora el rendimiento, pero requiere un equilibrio entre el tamaño del vector y el uso de memoria.

### 2.5. **Transacciones**

Uno de los principales problemas de seguridad en aplicaciones cliente-servidor es que el cliente pueda realizar operaciones no autorizadas o enviar mensajes mal formados. Para evitar estos problemas, es crucial modelar el flujo de información y el comportamiento del servidor utilizando un diagrama de estados o autómata.

**Ejemplo de diagrama de estados.**
- El servidor inicia en el estado 0 y envía al cliente el mensaje "Introduce el comando".
- El cliente puede enviar los comandos:
  - `ls`: Muestra el contenido del directorio y vuelve al estado 1.
  - `get`: Solicita el nombre del archivo, lo muestra y vuelve al estado 1.
  - `exit`: Finaliza la conexión del cliente (estado -1).
- Cualquier otro comando hace que el servidor solicite un comando válido.

Para implementar este comportamiento, el servidor utiliza dos variables:

- `estado`: Almacena la posición actual en el autómata.
- `comando`: Almacena el comando recibido del cliente, permitiendo la transición entre estados.

### 2.6. **Ejemplo III**

**Implementación del diagrama de transiciones.**

```java
int estado = 1;

do {
    switch(estado) {
        case 1:
            flujo_salida.writeUTF("Introduce comando (ls/get/exit)");
            comando = flujo_entrada.readUTF();

            if (comando.equals("ls")) {
                System.out.println("\tEl cliente quiere ver el contenido del directorio");
                // Muestro el directorio
                estado = 1;
                break;
            } else if (comando.equals("get")) {
                // Voy al estado 3 para mostrar el fichero
                estado = 3;
                break;
            } else {
                estado = 1;
                break;
            }

        case 3:
            flujo_salida.writeUTF("Introduce el nombre del archivo");
            String fichero = flujo_entrada.readUTF();
            // Muestro el fichero
            estado = 1;
            break;
    }

    if (comando.equals("exit")) estado = -1;
} while (estado != -1);
```

## 2.7. Monitorizar tiempos de respuesta

Para evaluar el rendimiento de una aplicación cliente-servidor, es importante medir dos tiempos clave:

- **Tiempo de procesamiento.** El tiempo que el servidor tarda en procesar una petición.
- **Tiempo de transmisión.** El tiempo que tarda un mensaje en viajar a través de la red.

**Medición del tiempo de procesamiento.**

```java
import java.util.Date;

long tiempo1 = (new Date()).getTime();
// Procesar la petición del cliente
long tiempo2 = (new Date()).getTime();
System.out.println("\tTiempo = " + (tiempo2 - tiempo1) + " ms");
```

**Medición del tiempo de transmisión.**
- Los relojes del cliente y servidor deben estar sincronizados (usando NTP).
- El servidor envía su tiempo actual al cliente, quien calcula la diferencia con su propio tiempo.

**Sincronización de relojes en GNU/Linux.**

```bash
/usr/sbin/ntpdate -u 0.centos.pool.ntp.org
```

**Uso del comando `ping`.**
- Permite medir el tiempo de transmisión entre el cliente y el servidor.
- Ejemplo: `ping www.google.es` muestra el tiempo de ida y vuelta.

### 2.8. **Ejemplo IV**

**Servidor que envía el tiempo actual al cliente.**

```java
import java.io.*;
import java.net.*;
import java.util.Date;

class Servidor {
    static final int Puerto = 2000;

    public Servidor() {
        try {
            ServerSocket sServidor = new ServerSocket(Puerto);
            System.out.println("Escucho el puerto " + Puerto);

            Socket sCliente = sServidor.accept();
            System.out.println("Cliente conectado");

            DataInputStream flujo_entrada = new DataInputStream(sCliente.getInputStream());
            DataOutputStream flujo_salida = new DataOutputStream(sCliente.getOutputStream());

            long tiempo1 = (new Date()).getTime();
            flujo_salida.writeUTF(Long.toString(tiempo1));

            sCliente.close();
            System.out.println("Cliente desconectado");
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public static void main(String[] arg) {
        new Servidor();
    }
}
```

**Cliente que calcula la diferencia de tiempo.**

```java
import java.io.*;
import java.net.*;
import java.util.Date;

class Cliente {
    static final String HOST = "localhost";
    static final int Puerto = 2000;

    public Cliente() {
        try {
            Socket sCliente = new Socket(HOST, Puerto);

            DataInputStream flujo_entrada = new DataInputStream(sCliente.getInputStream());
            DataOutputStream flujo_salida = new DataOutputStream(sCliente.getOutputStream());

            String datos = flujo_entrada.readUTF();
            long tiempo1 = Long.valueOf(datos);
            long tiempo2 = (new Date()).getTime();
            System.out.println("\nEl tiempo es: " + (tiempo2 - tiempo1));

            sCliente.close();
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public static void main(String[] arg) {
        new Cliente();
    }
}
``` 

Este ejemplo mide el tiempo de transmisión entre el cliente y el servidor, mostrando la diferencia en milisegundos.
