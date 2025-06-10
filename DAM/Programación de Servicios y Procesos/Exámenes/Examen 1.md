---
tags:
  - DAM
  - PSP
cssclasses:
  - dam-psp
  - table-clean
banner: "![[psp.jpg]]"
banner_y: 0.25
number headings: off
---

# **Examen 1.** <br>Sistemas Operativos y Programación Concurrente

### **Pregunta a.** Ciclo de Vida de un Proceso

Un proceso atraviesa distintas etapas desde su creación hasta su finalización. Estas son:

| Etapa | Explicación | 
| - | - | 
| **New** | El proceso ha sido creado, pero aún no está listo para ejecutarse.| 
| **Ready** | El proceso está listo para ejecutarse y espera su turno de CPU.| 
| **Running** | El proceso está siendo ejecutado por el procesador.| 
| **Blocked** | El proceso está esperando un recurso o evento externo.| 
| **Detached (Terminado)** | El proceso ha finalizado su ejecución.| 

**Esquema recomendado:**

```plaintext
New → Ready → Running → Detached
          ↑     ↓
           Blocked
```

### **Pregunta b.** Diferencias entre Procesos e Hilos (con Java)

| |Comparten memoria | Afecta a otros (P/H)|
|---|---|---|
|Procesos|🟥|🟥|
|Hilos|🟩|🟩|

**Ejemplo de creación de un proceso:**

```java
ProcessBuilder pb = new ProcessBuilder(
    "java",
    "-cp",
    "../psp/out/artifacts/psp__jar/psp.jar",
    "org.example.carregarPaginaWeb"
);
Process p = pb.start();
```

**Ejemplo de creación de un hilo:**

```java
Thread srv = new Thread();
srv.start();

Server srv = new Server();
srv.start();

public class Server extends Thread {
    @Override
    public void run() {
        // Código del hilo
    }
}
```

### **Pregunta c.** Mecanismos de Sincronización en Java

**1. Semáforos (Semaphore)**  
Permiten controlar el acceso concurrente a recursos. Útil para limitar el número de hilos que acceden a una sección crítica.

```java
Semaphore[] s = new Semaphore[10];
s[0].acquire();
extras.contarNumeros();
s[0].release();
```

**2. Synchronized + wait/notify**  
Permite bloquear secciones de código para que solo un hilo las ejecute a la vez.

```java
public class Carrera {
    String nombreCaballo;
    final Object lock = new Object();
    static int contador = 0;
    static final int MAX_CABALLOS = 5;

    @Override
    public void run() {
        synchronized (lock) {
            contador++;
            extras.verificarPodio();
            if (contador == MAX_CABALLOS) {
                contador = 0;
                lock.notifyAll();
            } else {
                lock.wait();
            }
        }
    }
}
```

### **Pregunta d.** Modelo OSI y TCP/IP

**Modelo OSI (de capa 7 a 1):**

| Capa | Función | 
| - | - | 
| 1. **Aplicación** | Interactúa con el usuario (SMTP, HTTP, DNS, SSH) | 
| 2. **Presentación** | Traducción, cifrado y codificación de datos | 
| 3. **Sesión** | Controla y mantiene sesiones entre aplicaciones | 
| 4. **Transporte** | Transferencia de datos con control de errores (TCP, UDP) | 
| 5. **Red** | Enrutamiento de paquetes (IP) | 
| 6. **Enlace de Datos** | Manejo de direcciones físicas (MAC, switches) | 
| 6. **Física** | Medio de transmisión (cables, WiFi, etc.) | 

**Modelo TCP/IP (equivalente simplificado):**

1. **Acceso a la red**
2. **Internet**
3. **Transporte**
4. **Aplicación**
