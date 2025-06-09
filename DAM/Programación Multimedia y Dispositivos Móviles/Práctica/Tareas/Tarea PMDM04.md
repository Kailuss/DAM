---
tags: [DAM, PMDM]
cssclasses: [dam-pmdm, table-compact-clean]
banner: "![[pmdm.jpg]]"
banner_y: 0.42
---

# Tarea **PMDM04**
## 1. Instrucciones

Para esta práctica partiremos de un esqueleto de aplicación, al cual tendremos que añadir ciertas funcionalidades y lo iremos completando.

1. En primer lugar, partiréis del proyecto que se os ha compartido. Para abrir un nuevo proyecto, podéis hacerlo directamente desde VS Code, con la opción “Clonar el repositorio GIT...”. También podéis descargar la carpeta del proyecto del enlace del repositorio proporcionado y abrirla en el editor. Lo más recomendable es que clonéis el proyecto a partir del enlace proporcionado dentro del directorio de proyectos de Flutter de vuestro dispositivo. Después, abrid este proyecto. Normalmente, VSCode os mostrará un diálogo para ejecutar el comando (abajo a la derecha), pero en caso contrario y que veáis todo el proyecto con errores, etc., haced lo siguiente:
   - En la terminal, aseguraos de que estáis en el repositorio de vuestro proyecto.
   - Ejecutad el comando: `flutter pub get` en la terminal de vuestro VS Code.
![cover](../../../../_Media/Imágenes/PMDM/Pasted%20image%2020250601144857.png)

2. Como podéis observar, una vez creado el proyecto, ya contiene toda una estructura de directorios, clases, etc. Podemos dividir esta aplicación en una **HomeScreen** que carga **MapesScreen** o **DireccionsScreen** en función de un índice, el del widget “custom_navigationbar”.
![](../../../../Imagen_A2I.png)

   A continuación, las dos pantallas serán muy similares:

   - Una cargará un listado de geolocalizaciones escaneadas.
   - La otra cargará un listado de direcciones web.

   Cuando pulsemos sobre uno de los elementos de la lista se producirá un efecto para cada tipo:

   - En el caso de la geolocalización, abriremos una nueva página mostrando **Google Maps.**
   - En el caso de pulsar sobre una URL, lanzaremos un visor web del sistema. Aquí tendréis varias formas de hacerlo, pudiendo elegir un navegador web también.

3. Seguid los vídeos de la unidad. Una vez acabados los vídeos, realizad la tarea que se os encomienda de modificar la pantalla del Mapa y añadid una funcionalidad de **Google Maps** no mencionada ni que aparezca en la demostración.

4. Pensad que para la demostración, tenéis que leer un código QR de cada tipo, esto lo podéis hacer con un dispositivo físico, o bien desde el emulador como podéis ver en el siguiente enlace:  
   [https://stackoverflow.com/questions/9867410/barcode-scanning-in-android-emulator](https://stackoverflow.com/questions/9867410/barcode-scanning-in-android-emulator)

## 2. Criterios de calificación

Para la entrega de la práctica, el alumno deberá adjuntar todo el código del proyecto mediante un repositorio de **Github.** Además, realizar un vídeo de corta duración (**5 minutos como máximo**) explicando y demostrando la ejecución de las actividades.

- **Funcionamiento del código – 60%**
- **Estructura y formato del código - 10%**
- **Comentarios de código – 10%**
- **Vídeo demostración/Explicación – 20%**

**Nota:** Si se detecta plagio, el código da errores de compilación o no tiene una correcta ejecución, se considerará suspendida la práctica con una puntuación de **0.**
