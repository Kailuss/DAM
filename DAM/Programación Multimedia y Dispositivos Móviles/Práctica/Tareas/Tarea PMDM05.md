---
tags: [DAM, PMDM]
cssclasses: [dam-pmdm, table-compact-clean]
banner: "![[pmdm.jpg]]"
banner_y: 0.42
---
# Tarea **PMDM05.**

## 1. Enunciado

**Instrucciones.** Para esta práctica partiremos de un esqueleto de aplicación, al cual deberemos añadir ciertas funcionalidades y completarlo.

1. En primer lugar, comenzaréis con el proyecto que se os ha compartido. En concreto, de un repositorio en modo plantilla. En este caso, podéis crear un repositorio a partir de una plantilla, hacer un *fork*, clonarlo, etc.  
   **Enlace al repositorio.** [https://github.com/jaumecf/productes_app](https://github.com/jaumecf/productes_app)  

2. Como podréis observar una vez creado el proyecto, este ya contiene toda una estructura de directorios, clases, etc. Podemos dividir esta aplicación en dos partes: por un lado, la clase `HomeScreen` y la de `Login`. Lo primero que debéis hacer es entender la estructura de la aplicación de la plantilla. Esta consta de una pantalla inicial de `Login`, con un formulario validado. Una vez hagamos *login* con **CUALQUIER** correo electrónico y una contraseña aleatoria, podremos acceder a `HomeScreen`.  

   Una vez entendida la estructura y el funcionamiento de la plantilla proporcionada, lo primero que debéis hacer es explicar el funcionamiento del formulario respondiendo en el vídeo las siguientes cuestiones (basta con un minuto en total):  

   - ¿Dónde y cómo se valida el formulario?  
   - ¿En qué momento se pueden recoger los valores finales de los campos del formulario?  

3. Finalmente, la funcionalidad a implementar se dividirá en dos apartados:  
   - Realizar un *login* y registro en la aplicación mediante **Firebase Authentication.**  
   - Seguir los vídeos proporcionados para crear una tienda online tipo *Wallapop*, con nuestro propio *backend* (API con **Realtime Database** de Firebase).  

4. Como podéis ver, son funcionalidades completamente separadas y se pueden realizar de forma independiente. Da igual cuál hagáis primero. Recordad que en el `main` podéis modificar la `initial route` y poner, por ejemplo, `home` para que no se inicie el *login* al arrancar la aplicación.  

   Para implementar el *login*, tendréis que crear, además de una pantalla de *login*, otra de registro (basta con correo electrónico y contraseña). Podéis emplear los estilos que queráis. Se os proporcionará una plantilla de ejemplo y enlaces para inicializar **Firebase CLI** y configurar todo lo necesario.  

## 2. Criterios de calificación  

Para la entrega de la práctica, el alumno deberá adjuntar **todo el código del proyecto**, además de realizar un **vídeo de corta duración (unos 5 minutos)** explicando y demostrando la ejecución de las actividades.  

- **Funcionamiento del código** – 65%  
- **Estructura y formato del código** – 5%  
- **Comentarios en el código** – 10%  
- **Vídeo de demostración/explicación** – 20%  

**Si el código tiene errores de compilación o no se ejecuta correctamente, la práctica se considerará suspensa con una puntuación de 0.** 
