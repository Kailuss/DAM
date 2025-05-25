---
cssclasses:
  - dam-di
banner: "![[di.jpg]]"
---
# Examen

#### **1.** ¿Cuál de las siguientes afirmaciones es la correcta?

2) Para ejecutar una aplicación empaquetada en un .jar es necesario que en la máquina donde se va a ejecutar esté instalado el JRE.  
3) En un paquete .jar se pueden incluir las librerías necesarias del JDK para que se ejecute una aplicación Java sin necesidad de que exista el JRE en la máquina destino.  
4) **En los paquetes .jar no podemos incluir las librerías del JDK que necesita una aplicación pero podemos crear un instalador .exe con Install4j que incluya el JRE y lo instale automáticamente en la máquina destino.**  
5) Ninguna de las opciones anteriores es correcta.

#### **2.** Las imágenes estáticas que aparecen en la interfaz de una aplicación como iconos y logos, ¿en qué carpeta del proyecto Maven es conveniente incluirlas para evitar problemas en NetBeans al ejecutar el proyecto?

1) src/images  
2) target/resources  
3) **src/main/resources**  
4) Ninguna de las opciones anteriores es correcta.

#### **3.** ¿Qué plugin de Maven se puede utilizar para incluir los jar de las dependencias en el jar de la aplicación generado?

1) maven-shade-plugin  
2) maven-resources-plugin  
3) maven-compiler-plugin  
4) **maven-dependency-plugin**

**4. ¿Cuál de las siguientes afirmaciones es cierta?**

1) Install4j lee el pom.xml del proyecto las dependencias Maven y las descarga e incluye en el instalador automáticamente.  
2) Install4j sólo permite crear instaladores para distribuir nuestra aplicación en máquinas donde ya exista instalada previamente una versión del JRE o el JDK.  
3) La versión de prueba de Install4j no permite crear instaladores que necesiten elevación de privilegios para ser instalados.  
4) **Para crear un instalador con Install4j, el fichero jar con la aplicación principal generado desde NetBeans debe incluir los jars de las dependencias de nuestro proyecto.**  
5) **Install4j permite crear instaladores para Windows, Mac y Linux.**

**5. ¿En qué sección principal del pom.xml se tiene que poner la referencia al maven-shade-plugin para que se incluyan automáticamente los jar de las dependencias de un proyecto en el .jar que se generará cuando se hace el build?**

1) \<repositories\>...\</repositories\>  
2) \<dependencies\>...\</dependencies\>  
3) **\<build\>...\</build\>**  
4) \<properties\>...\</properties\>

**6. ¿En qué carpeta por defecto se crea el fichero .jar generado al hacer un ‘Clean and Build’ de una aplicación Java Maven?**

1) build  
2) **target**  
3) dist  
4) src

**7. Respecto de una aplicación Java con Maven, ¿cuál de las siguientes opciones es cierta?**

1) Las dependencias se incluyen dentro del fichero .jar generado cuando hacemos el ‘Build’ de la aplicación.  
2) No se puede distribuir como un paquete .jar para Linux.  
3) **Siempre se debe indicar la clase principal del proyecto en el pom.xml si queremos crear un .jar distribuible en otras máquinas.**  
4) Hay que copiar manualmente todos los .jar de las dependencias a la carpeta lib una vez hecho el ‘Build’.

**8. Quina d’aquestes opcions és vertadera, respecte els comentaris Javadoc?**

1) És tot aquell text al fitxer font que es troba entre els caràcters /\* i \*/  
2) No poden emprar etiquetes HTML.  
3) Poden precedir mètodes i propietats d’una classe, però no a una classe ni al seu constructor.  
4) **Cada línia, excepte la primera i la darrera, comença amb el caràcter ‘\*’.**

**9. Quina etiqueta Javadoc s’empra per documentar els arguments d’un mètode?**

1) @args  
2) **@param**  
3) @[tipus_de_dades_del_parametre]  
4) @see

**10. Quina etiqueta Javadoc s’empra per documentar el valor que torna un mètode?**

1) @[tipus_de_dades_del_valor_de_retorn]  
2) **@return**  
3) @param  
4) @out

---

**1. Enumera los diferentes tipos de documentación que podemos encontrar en un proyecto de software dirigidas al usuario final de la aplicación.**

**End user:**  
Product Documentation:
- Instructional manual (manual de usuario)  
- Reference manual  
- Installation Guides  

User Documentation:
- How-to guides  
- Tutorials  
- Reference docs  
- Explanations  

**IT:**  
Technical Documentation:
- API documentation  
- Data model documentation  
- Architecture documentation  
- User guide  
- Release notes  
- Readme  

System Documentation:
- Troubleshooting guide  
- Architecture documentation  
- User manual  

**2. Indica cuáles son los tipos de documentación de un proyecto de software dirigidas al equipo de desarrollo del proyecto.**

Project Documentation (durante el proceso de un proyecto):
- Technical design documents  
- Project plans  
- Project requirements specifications  

Process Documentation (Processes and procedures for develop, test & maintain):
- Development plans  
- Testing plans  
- Release plans  
- Bug tracking reports  

System Documentation:
- Troubleshooting guide  
- Architecture documentation  
- User manual  

**3. Explica de forma esquemática pero precisa cuál es el procedimiento que hay que seguir para crear un instalador para Windows de una aplicación Java utilizando la herramienta Install4j. Se ha de tener en cuenta que la aplicación Java puede tener dependencias y recursos externos que también hay que desplegar o instalar en las máquinas destino.**

1. **Indicar la ruta a "target\carpetaBuild"**  
2. **Launcher:**  
   - Indicar nombre del ejecutable  
   - Ruta de los logs  
   - Nivel de ejecución (admin o no)  
   - Icono del launcher  
   - El .jar al que se va a llamar y la clase Main  
   - Splash Screen  
3. **Media:**  
   - Tipo de SO  
   - El Bundle de JRE por si la máquina destino no lo tiene instalado  
4. **Installer:**  
   - Acceso al escritorio  
   - Copia de ficheros a rutas específicas  
5. **Build**  

**4. Explica detalladamente qué hay que hacer en Install4j para crear una carpeta en `C:\Users\[usuario]\AppData\Local` y que se escriban en ella un conjunto de ficheros cuando la aplicación se instale.**

En el paso de Installer añadiremos la opción “Copy files and directories”.  
En la ruta origen seleccionaremos la carpeta con el conjunto de ficheros.  
En la ruta destino usaremos las variables del Install4j `sys.localappdata` y le añadiremos `\\nombreCarpeta`.  
De este modo nos va a crear la carpeta con todo su contenido en `%localAppdata%`.  