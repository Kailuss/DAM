---
tags:
  - DAM
  - PSP
cssclasses:
  - dam-psp
  - table-compact-clean
banner: "![[psp.jpg]]"
banner_y: 0.25
number headings: off
---

# **Examen 2.** <br>Gestión de Procesos en Java


### **Pregunta a.** ¿Cómo se crea un proceso en Java?

```java
ProcessBuilder pb = new ProcessBuilder("notepad.exe");
```


### **Pregunta b.** ¿Cómo se llama (inicia) un proceso en Java?

```java
Process p = pb.start();
```


### **Pregunta c.** ¿Cómo pasar información entre procesos en Java?

**Enviar datos al proceso:**

```java
try (BufferedWriter out = new BufferedWriter(
        new OutputStreamWriter(p.getOutputStream()))) {
    out.write("Lo que queramos pasar");
    out.flush();
}
```

**Recibir datos del proceso:**

```java
try (BufferedReader in = new BufferedReader(
        new InputStreamReader(p.getInputStream()))) {
    String line = in.readLine();
}
```