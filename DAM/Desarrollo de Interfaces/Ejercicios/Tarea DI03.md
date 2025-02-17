---
tags: []
---
## 1 Dominio del problema

Nuestros clientes han estado realizando pruebas con nuestras aplicaciones y están muy satisfechos con la funcionalidad, pero tienen algunas quejas sobre la usabilidad de la interfaz.

Por tanto, ha llegado el momento de centrarnos en la usabilidad y la experiencia de usuario de nuestra aplicación.

Rediseñaremos la interfaz de usuario (UI) y la estructura del proyecto que hemos estado desarrollando para crear un producto que cumpla con los requisitos de nuestros clientes.

---

## 2 Especificaciones

**Objetivo:** Mejorar la usabilidad de la aplicación aplicando los conocimientos adquiridos en los apuntes de la unidad.

### 2.1 Elementos de usabilidad

- **Color y estilo:** Apariencia general.
- **Texto:** Fuentes y tipografía.
- **Imágenes e iconos.**
- **Interacción.**
- **Metáforas.**
- **Facilidad de uso (Affordance):**
    - Visibilidad.
    - Retroalimentación.
    - Correspondencia natural (Natural mapping).
    - Restricciones.

**Otras funcionalidades requeridas:**

- Búsqueda, filtros, paginación.
- Tecla Enter -> Activar el botón por defecto.
- Incluir un **dark pattern**.
- Uso de hilos (threads) y evitar llamadas bloqueantes.
- Expresiones regulares.

---

## 3 Criterios de calificación

1. Modificar el aspecto de las ventanas para que sean más atractivas y estén en línea con las tendencias actuales (p. ej., diseño plano, esquemas de color). **1 punto.**
2. Añadir iconos u otros elementos visuales a los componentes para mejorar la usabilidad de la interfaz. **1 punto.**
3. Modificar las fuentes y los componentes que muestren texto para que sea legible e inteligible. **1 punto.**
4. Organizar y agrupar los componentes de manera más atractiva y lógica para el usuario. **1 punto.**
5. Redefinir los **Layouts** de los contenedores (JFrame, JDialog, etc.), incluyendo anclajes, ajustes automáticos y tamaños mínimo y máximo, para garantizar la usabilidad en caso de redimensionamiento. Utilizar preferentemente **MigLayout**, aunque se puede usar **BorderLayout** si es necesario. **No se permite usar null layout.** **2 puntos.**
6. Implementar la gestión de errores y excepciones, informando y dando retroalimentación al usuario cuando sea necesario (sin necesidad de usar una API de validación). **1 punto.**
7. Añadir más cambios que mejoren la usabilidad, documentándolos en el archivo **Readme.md** del repositorio y justificando las decisiones tanto en interfaz como en código. **3 puntos.**
8. **Código limpio:** Nombres descriptivos, estructura del proyecto, commits claros en GitHub, y un archivo Readme bien redactado. **1 punto.**

---

## 4 Recursos necesarios para realizar la tarea

- Servidor **MS SQL Server.**
- Cliente SQL (**SQL Server Management Studio**).
- Proyecto entregado en la UT01.
- Cuenta de almacenamiento en **Azure** para alojar vídeos en la nube.

---

### 4.1 Consejos y recomendaciones

- Puedes cambiar cualquier elemento de la interfaz y la aplicación, incluso rediseñarla desde cero, siempre que se respete la funcionalidad.

**Sugerencias:**

- Añadir iconos a los botones o sustituirlos por imágenes con **tooltips** y efectos al pasar el ratón (**hover**).
- Añadir un menú, barra de herramientas (**toolbar**), barra de estado (**status bar**).
- Incluir mensajes informativos (p. ej., "X intentos necesitan revisión", "email o contraseña no encontrados").
- Implementar barras de progreso, GIFs animados para estados de espera, etc.
- Puedes integrar componentes personalizados (**JavaBeans**) creados por ti o disponibles en internet siempre que su licencia lo permita. Indica su uso en el **Readme.md**, mencionando al autor y la fuente.

---

## 5 Indicaciones de entrega

- El proyecto debe estar desarrollado con **NetBeans** y el **JDK 21**. Ha de ser un proyecto **Maven**.
- El proyecto debe alojarse en un repositorio privado de **GitHub**. Continúa los commits del proyecto desarrollado en las unidades 1 y 3.
- Añade como colaborador al usuario **spdvi** (o **[gjm@paucasesnovescifp.cat](mailto:gjm@paucasesnovescifp.cat)**).
- Envía el enlace al repositorio en la asignación de la tarea en Moodle en cuanto lo crees.
- Realiza commits y pushes frecuentes con mensajes claros y descriptivos.
- Documenta en el **Readme.md** del repositorio todos los recursos externos que utilices (videos, consultas en Google, ayuda de chats, etc.).
- **Citar código:** Si utilizas código no escrito por ti o adaptas código de otras fuentes, cita claramente las fuentes en tu código. Consulta [MIT Integrity](http://integrity.mit.edu/handbook/writing-code).
- No copies código de compañeros ni de internet sin entenderlo perfectamente y citar la fuente. Respeta las licencias de código.
- Cumple con las convenciones de nombres y documenta todo lo que no sea fácilmente comprensible (con **Javadoc** para métodos y atributos).

**Fecha límite para el último push al repositorio:**  
**30 de enero de 2025 a las 7:00 am.**