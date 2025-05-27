---
tags: [DAM, DI]
cssclasses: [dam-di, table-compact-clean]
banner: "![[di.jpg]]"
banner_y: 0.72
---

# **Resumen Anexo TEMA 6.** <br> Documentación de Software
## 1. ¿Qué es la documentación de software?  
Material que describe características, uso y aspectos técnicos de un producto de software. Esencial para:  
- Usuarios (aprender a usar el software).  
- Desarrolladores (mantenimiento y colaboración).  
- Empresas (calidad y eficiencia).  
> *"La documentación es una parte crítica, pero a menudo descuidada, del software"* — Eric Holscher.  
## 2. Tipos de documentación  
### 2.1. **Documentación de proyecto**  
Para equipos de desarrollo:  
- Diseño técnico.  
- Planes de proyecto.  
- Especificaciones de requisitos.  
### 2.2. **Documentación de producto**  
Para usuarios finales:  
- Manuales de usuario.  
- Guías de instalación.  
- Tutoriales paso a paso.  
### 2.3. **Documentación técnica**  
Detalles para desarrolladores:  
- **API.** Referencia de llamadas y clases.  
- **Modelo de datos.** Estructuras y relaciones.  
- **Arquitectura.** Diseño del sistema.  
- **README.** Visión general con el código.  
### 2.4. **Documentación del sistema**  
Información técnica avanzada:  
- Guías de resolución de problemas.  
- Diagramas de arquitectura.  
- Manuales de administración.  
## 3. Beneficios clave  
- **Mejora la experiencia del usuario.** Instrucciones claras.  
- **Facilita la colaboración.** Comprensión técnica compartida.  
- **Aumenta la eficiencia.** Reduce tiempo en depuración.  
- **Garantiza calidad.** Registro de decisiones y procesos.  
## 4. Cómo escribir documentación efectiva  
### 4.1. **Priorízala en el desarrollo**  
- No lanzar funciones sin documentación.  
- Invertir en herramientas y redactores técnicos.  
### 4.2. **Identifica la audiencia**  
- **Usuarios finales.** Lenguaje simple, ejemplos visuales.  
- **Desarrolladores.** Detalles técnicos (API, algoritmos).  
### 4.3. **Estrategia de contenido**  
- Planifica actualizaciones y responsables.  
- Usa guías de estilo (ejemplo: IBM, Microsoft).  
### 4.4. **Claridad y estructura**  
- Aplica el principio **KISS** (*Keep It Simple, Stupid*).  
- Usa listas, encabezados y ejemplos.  
### 4.5. **Revisión y mejora continua**  
- Involucra a desarrolladores y usuarios.  
- Actualiza con cada cambio en el software.  
## 5. Mejores prácticas adicionales  
- **Elementos visuales.** Diagramas y videos para claridad.  
- **Inclusividad.** Documentación accesible (alto contraste, lectores de pantalla).  
- **Facilidad de búsqueda.** Indexar en motores de búsqueda y ayuda contextual.  
  *Ejemplo: Slack enlaza documentación relevante desde su interfaz.*  
## 6. Herramientas útiles  
- **Generación automática.** Doxygen (extrae comentarios del código).  
- **Colaboración.** Confluence, GitBook.  
- **Bases de conocimiento.** Centralizan documentación con búsqueda avanzada.  
## 7. Base de conocimientos  
Ventajas:  
- **Organización.** Control de versiones y actualizaciones.  
- **Accesibilidad.** Búsqueda rápida y análisis de uso.  
### 7.1. **Ejemplo de estructura para documentación técnica (API)  **
```markdown
# API Reference  
## Endpoint: `/users`  
- **GET.** Lista todos los usuarios.  
  ```json
  Response: [{"id": 1, "name": "Alice"}]
  ``´
- **POST.** Crea un nuevo usuario.  
  Parámetros: `name` (string), `email` (string).  
```  
### 7.2. **Fragmento de guía de estilo  **
> **Terminología.**  
> - Usar "iniciar sesión" en lugar de "log in".  
> **Formato.**  
> - Encabezados en negrita (`##` en Markdown).  
> - Código en bloques con sintaxis resaltada.  
--- 
Este resumen destaca los puntos clave del tema, incluyendo tipos de documentación, estrategias de creación y herramientas recomendadas.
