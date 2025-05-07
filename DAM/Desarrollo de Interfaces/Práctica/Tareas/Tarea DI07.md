---
tags: [DAM, DI]
cssclasses: [dam-di, table-compact-clean]
banner: "![[di.jpg]]"
banner_y: 0.72
---

# Tarea **DI07**

## 1. Dominio del problema

Es el momento de desplegar y distribuir nuestras aplicaciones para que los usuarios puedan instalarlas y ejecutarlas en sus dispositivos. El **dispositivo objetivo** del usuario es una **máquina Windows** sin ningún JRE o JDK instalado.

## 2. Especificaciones

-   Preparar el proyecto para su despliegue. El objetivo de este paso es crear el .jar principal de la aplicación a partir del cual crearemos el instalador.
	-   Hay que tener en cuenta que las dependencias de Maven utilizadas en el proyecto, si no se incluyen en la aplicación, esta no funcionará en una máquina diferente a la de desarrollo. Hay dos maneras de incluirlas en el .jar final:
		-   Como se vio en una unidad anterior con el `maven-shade-plugin`.
		-   Utilizando el `maven-jar-plugin` como se explica en los videos de soporte.
-   Realiza un Clean & Build del proyecto y comprueba que se genera correctamente el directorio `target` con todos los recursos necesarios.
-   Crea un instalable con Install4j.
	-   Debe contener las opciones habituales y mínimas para instalar la aplicación, además de una página de licencia.
	-   También deberá incluir una sección opcional para instalar en el sistema destino la documentación en HTML generada en la unidad anterior, así como el manual de usuario en PDF. Por ejemplo, en la carpeta `[Usuario]\AppData\[NombreDeTuAplicación]`. Añade a tu aplicación opciones de menú para abrir estas ayudas.
		-   **Help > API Docs.** Abrir el `index.html` de la documentación en el navegador.
		-   **Help > User Manual.** Abrir el PDF del manual de usuario en la aplicación correspondiente del sistema.
	-   El instalador debe incluir un bundle del JRE v21 para ejecutarse en máquinas donde Java no esté instalado. El instalador ha de ofrecer opciones para crear un grupo de programas en el menú de inicio, un acceso directo en el escritorio, así como un desinstalador. Personaliza todo lo posible el instalador, incluyendo el logo de la aplicación, un tema similar al de la aplicación, etc.
	-   Incluye también un desinstalador.
	-   El instalador deberá crear accesos directos en el escritorio (opcional) y un grupo de programas en el menú de inicio con opciones para ejecutar la aplicación y desinstalarla.
	-   Personaliza el look and feel de las pantallas del instalador para que sea coherente con el de tu aplicación.
	-   Personaliza también los iconos de los archivos clave de la aplicación: el .jar principal generado, el de setup, el .exe que empaqueta al .jar, los accesos directos, etc.
-   Ejecuta el instalador en algunas máquinas diferentes a la de desarrollo donde no esté instalado ninguna versión del JRE o JDK, y comprueba que la aplicación funcione correctamente.

## 3. Criterios de calificación

1.  Preparar el proyecto para su construcción y crear la carpeta `target` correctamente. Subir a GitHub la carpeta `target/`. **1 punto.**
2.  Crear un instalable con Install4j para ejecutar la aplicación en una máquina Windows sin JRE o JDK instalado. **4 puntos.**
3.  Añadir al instalador la página de licencia y la opción de instalar la documentación (API Docs y User Manual). **2 puntos.**
4.  Modificar el look and feel del instalador e iconos de los archivos de la aplicación. **1.5 puntos.**
5.  Documentar con un videotutorial (duración máxima de 3 minutos) o un manual con capturas de pantalla el proceso seguido en Install4j para generar el instalador. **1.5 puntos.**

## 4. Recursos necesarios para realizar la Tarea

-   Proyecto desarrollado en las unidades anteriores.
-   Al menos una máquina Windows (10 o 11) sin entorno de desarrollo instalado ni JDK o JRE. Puedes crear una o más máquinas virtuales con Windows en tu sistema si no tienes acceso a una máquina física.

## 5. Consejos y recomendaciones

-   Revisa los videos de las Support Notes y configura el proyecto y el archivo `pom.xml` para el empaquetado, mediante archivos JAR, de una aplicación Java de escritorio. Ten en cuenta que la aplicación debe incluir todas las librerías y recursos necesarios para su ejecución en otros ordenadores.
-   Los plugins (dependencias de Maven) deben copiarse automáticamente en la carpeta `target/lib`, por ejemplo, al realizar el build. Para ello, configura el `pom.xml` con el `maven-jar-plugin` como se muestra en los videos de soporte de DI07. Opcionalmente, se puede utilizar el `maven-shade-plugin` para incluirlos en el .jar de la aplicación.
-   Para aprender a usar Install4j, practica primero con una aplicación de prueba sencilla. Investiga los pasos y fases necesarios para crear un instalador con Install4j.
-   Para que Install4j cree una carpeta en `AppData` y coloque allí los archivos necesarios, una opción es utilizar la variable `sys.localAppdataDir` (ver [enlace](https://www.ej-technologies.com/resources/install4j/help/doc/concepts/variables.html)) y crear un "custom root" como se indica [aquí](https://www.ej-technologies.com/resources/install4j/help/doc/concepts/files.html).
-   En esta práctica, tendrás que agudizar tu ingenio y capacidad para leer/interpreter la documentación de Install4j y aprender mediante prueba y error. Pero si te quedas atascado, siempre puedes preguntar en el foro.
-   Se recomienda publicar una release de la aplicación en GitHub con el ejecutable del instalador y pedir a otros compañeros que lo prueben en máquinas sin entorno de desarrollo ni JDK/JRE instalados, así como en diferentes versiones de Windows (10, 11).

## 6. Indicaciones de entrega

-   El proyecto con el código fuente de la solución debe estar alojado en el repositorio de GitHub de tu aplicación entregado en las unidades 4 y 6.
-   Aunque no es lo habitual, **elimina de tu repositorio el `.gitignore`** (o modifícalo para que se suban todos los binarios generados en `target/...`).
-   El instalador .exe de la aplicación debe estar en GitHub como una release.
-   Envía a través de la plataforma Moodle el enlace al repositorio de GitHub y sube el archivo de video (duración máxima de 3 minutos) si corresponde.
-   Fecha límite de entrega: **8 de Mayo de 2025.**
