---
tags:
  - DAM
  - AD
cssclasses:
  - dam-ad
  - table-clean
banner: "![[ad.jpg]]"
banner_y: 0.32
number headings: off
---

# **Examen TEMA 2.2.** <br>Flujos de Información

### Examen Práctico - Nivel Básico
**Tiempo estimado.** 2 horas

**Instrucciones.** Implementa utilidades para trabajar con diferentes tipos de flujos.

**Ejercicio.**
1. Crea una clase `GestorFlujos` con los siguientes métodos estáticos:
   - `copiarArchivoBytes(String origen, String destino)`: Copia un archivo usando flujos de bytes
   - `copiarArchivoCaracteres(String origen, String destino)`: Copia un archivo de texto usando flujos de caracteres
   - `copiarArchivoBuffer(String origen, String destino)`: Copia un archivo usando flujos con buffer
   - `compararRendimiento(String archivo)`: Compara el tiempo de lectura del archivo con los tres métodos anteriores

2. Requisitos técnicos:
   - Implementa try-with-resources para la gestión de recursos
   - Maneja adecuadamente las excepciones
   - Documenta el código

3. Entrega:
   - Código fuente de la clase GestorFlujos
   - Clase de prueba que demuestre el funcionamiento de todos los métodos
   - Informe de comparación de rendimiento

### Examen Práctico - Nivel Avanzado
**Tiempo estimado.** 4 horas

**Instrucciones.** Desarrolla una aplicación de serialización de objetos complejos.

**Ejercicio.**
1. Crea una aplicación para gestionar un inventario de productos con las siguientes funcionalidades:
   - Definir clases para Producto, Categoría y Proveedor con relaciones entre ellas
   - Guardar y recuperar el inventario completo usando serialización
   - Implementar búsqueda de productos por diferentes criterios
   - Generar informes de inventario

2. Requisitos técnicos:
   - Las clases deben implementar Serializable
   - Gestiona adecuadamente las referencias entre objetos
   - Implementa try-with-resources para la gestión de recursos
   - Documenta el código

3. Entrega:
   - Código fuente de la aplicación
   - Archivo de ejemplo con datos serializados
   - Documentación del diseño