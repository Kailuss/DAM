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

# **Examen TEMA 2.1.** <br>Sistemas de Archivos

### Examen Práctico - Nivel Básico
**Tiempo estimado.** 1.5 horas

**Instrucciones.** Implementa una utilidad para gestionar archivos y directorios.

**Ejercicio.**
1. Crea una clase `GestorArchivos` con los siguientes métodos estáticos:
   - `obtenerInformacionRuta(String ruta)`: Muestra toda la información disponible de la ruta
   - `crearDirectorio(String ruta)`: Crea un directorio en la ruta especificada
   - `copiarArchivo(String origen, String destino)`: Copia un archivo de origen a destino
   - `moverArchivo(String origen, String destino)`: Mueve un archivo de origen a destino
   - `listarContenidoDirectorio(String ruta)`: Lista el contenido de un directorio

2. Requisitos técnicos:
   - Utiliza las clases Path y Files
   - Implementa manejo adecuado de excepciones
   - Documenta el código

3. Entrega:
   - Código fuente de la clase GestorArchivos
   - Clase de prueba que demuestre el funcionamiento de todos los métodos

### Examen Práctico - Nivel Avanzado
**Tiempo estimado.** 3 horas

**Instrucciones.** Desarrolla una aplicación de sincronización de directorios.

**Ejercicio.**
1. Crea una aplicación que sincronice el contenido de dos directorios con las siguientes funcionalidades:
   - Comparar archivos por nombre, tamaño y fecha de modificación
   - Copiar archivos nuevos o modificados del directorio origen al destino
   - Eliminar archivos en el directorio destino que no existen en el origen (opcional)
   - Generar un informe de la sincronización

2. Requisitos técnicos:
   - Utiliza las clases Path y Files
   - Implementa manejo adecuado de excepciones
   - Utiliza programación funcional donde sea apropiado
   - Documenta el código

3. Entrega:
   - Código fuente de la aplicación
   - Informe de ejemplo de una sincronización
   - Documentación del diseño