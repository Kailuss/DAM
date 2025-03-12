---
number headings: first-level 3, max 3, skip ^skipped, _.1.1.
cssclasses:
  - table-clean
banner: "![[psp.jpg]]"
banner_y: 0.36
---

# **Resumen TEMA 2.** Programación Multihilo

### 1. Conceptos Básicos
- **Hilo (Thread):** Flujo de ejecución independiente dentro de un proceso. Comparten memoria con otros hilos del mismo proceso.
- **Ventajas:** Menor consumo de recursos, conmutación rápida y eficiencia en sistemas multiprocesador.
- **Problemas comunes:** Condiciones de carrera, interbloqueos (deadlocks).

### 2. Creación de Hilos
#### Extendiendo `Thread`

```java
class HiloSaludo extends Thread {
    @Override
    public void run() {
        System.out.println("Hilo creado extendiendo Thread.");
    }

    public static void main(String[] args) {
        HiloSaludo hilo = new HiloSaludo();
        hilo.start(); // Inicia el hilo
    }
}
```

#### Implementando `Runnable` (Recomendado)

```java
class TareaSaludo implements Runnable {
    @Override
    public void run() {
        System.out.println("Hilo creado con Runnable.");
    }

    public static void main(String[] args) {
        Thread hilo = new Thread(new TareaSaludo());
        hilo.start();
    }
}
```

### 3. Estados de un Hilo

| Estado               | Descripción                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| **Nuevo**            | Hilo creado pero no iniciado.                                               |
| **Ejecutable**       | Listo para ejecutarse (puede estar en espera de CPU).                       |
| **No Ejecutable**    | Bloqueado (por `sleep()`, `wait()`, o E/S).                                 |
| **Terminado**        | Finalizó su ejecución.                                                      |

### 4. Sincronización
#### Palabra Clave `synchronized`

Protege secciones críticas para evitar condiciones de carrera.

```java
class Contador {
    private int valor = 0;

    public synchronized void incrementar() {
        valor++;
    }

    public synchronized int getValor() {
        return valor;
    }
}
```

#### Comunicación entre Hilos (`wait()`, `notify()`)

Ejemplo: **Productor-Consumidor.**

```java
class Buffer {
    private int dato;
    private boolean disponible = false;

    public synchronized void producir(int valor) throws InterruptedException {
        while (disponible) wait(); // Espera si hay dato sin consumir
        dato = valor;
        disponible = true;
        notify(); // Notifica al consumidor
    }

    public synchronized int consumir() throws InterruptedException {
        while (!disponible) wait(); // Espera si no hay dato
        disponible = false;
        notify(); // Notifica al productor
        return dato;
    }
}
```

### 5. Herramientas Avanzadas
#### `Semaphore`

Controla el acceso a recursos limitados.

```java
Semaphore semaforo = new Semaphore(3); // Permite 3 accesos simultáneos

semaforo.acquire(); // Adquiere un permiso
// Acceso al recurso
semaforo.release(); // Libera el permiso
```

#### `CountDownLatch`

Espera a que múltiples hilos completen tareas.

```java
CountDownLatch latch = new CountDownLatch(3);

// En cada hilo:
latch.countDown(); // Decrementa el contador

// Hilo principal:
latch.await(); // Espera hasta que el contador llegue a 0
```

#### `ExecutorService` (Pools de Hilos)

Maneja hilos de manera eficiente.

```java
ExecutorService executor = Executors.newFixedThreadPool(4);
executor.submit(() -> {
    // Tarea a ejecutar
});
executor.shutdown();
```

### 6. Buenas Prácticas

|     |     |
| --- | --- |
| **Evitar Interbloqueos** | Ordenar la adquisición de recursos.|
| **Manejo de Excepciones** | Usar `UncaughtExceptionHandler`.|
| **Documentación** | Comentar código y usar JavaDoc.|

### 7. Ejemplo Integrado: Sistema de Venta de Tickets

```java
class SistemaTickets {
    private int ticketsDisponibles = 100;
    private final Lock lock = new ReentrantLock();

    public void comprarTicket(String cliente) {
        lock.lock();
        try {
            if (ticketsDisponibles > 0) {
                System.out.println(cliente + " compró ticket #" + ticketsDisponibles);
                ticketsDisponibles--;
            }
        } finally {
            lock.unlock();
        }
    }

    public static void main(String[] args) {
        SistemaTickets sistema = new SistemaTickets();
        ExecutorService executor = Executors.newFixedThreadPool(5);

        for (int i = 0; i < 10; i++) {
            executor.submit(() -> sistema.comprarTicket(Thread.currentThread().getName()));
        }

        executor.shutdown();
    }
}
```

**Explicación:**
- Usa `ReentrantLock` para sincronizar el acceso a `ticketsDisponibles`.
- Un `ExecutorService` maneja 5 hilos que compiten por comprar tickets.
- Cada hilo ejecuta `comprarTicket()`, que reduce el contador de forma segura.

### 8. Conclusión

La programación multihilo en Java permite ejecutar tareas concurrentes eficientemente. Claves:

- Usar `Runnable` para flexibilidad.
- Sincronizar con `synchronized` o `Lock`.
- Utilizar herramientas como `Semaphore` y `ExecutorService` para casos complejos.
- Evitar interbloqueos y condiciones de carrera con diseño cuidadoso.
