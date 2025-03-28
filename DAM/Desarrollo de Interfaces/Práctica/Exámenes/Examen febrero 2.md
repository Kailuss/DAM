---
tags: [DAM, DI]
cssclasses: [dam-di, table-compact-clean]
banner: "![[di.jpg]]"
banner_y: 0.76
---
1. En una aplicación con interfaz gráfica de usuario para gestionar las reservas de viviendas de turismo vacacional, los establecimientos pueden tener servicios como Wifi, Piscina, Parking, Aire Acondicionado, etc. ¿Qué controles swing son los más adecuados para incluir en un formulario para crear un nuevo establecimiento y representar si un alojamiento incluye esos servicios o no?

	- [ ] JCheckBox
	- [ ] JButton
	- [ ] JRadioButton
	- [ ] JTextField
---
      
2. Las imágenes estáticas que aparecen en la interfaz de una aplicación como iconos y logos, ¿en qué carpeta del proyecto maven es conveniente incluirlas para evitar problemas en NetBeans al ejecutar el proyecto?

	- [ ] src/main/java/resources
	- [ ] src/main/resources
	- [ ] src/images
	- [ ] Ninguna de las opciones anteriores es correcta
---

3. ¿Qué propiedad hay que modificar para cambiar el color del texto que se muestra en los JButton ?![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdUkoLApWRJE5GO1ExqcRNtpO0FHHnhl5xUvHCq-ep-ysT4nsFbc-cw9NYVZLvh4nIT-A7GSHb-A3qK6hyiHdJq6c5EO6EZshhtW5J9bikBM5MgIJiqYZ4C_SBZ2Uz0yCi_yCEr?key=9e1ypIjH40GfRWd62BRTTa1Y)
	- [x] foreground
	- [ ] text
	- [ ] font
	- [ ] color
---
    
4. ¿Qué componente swing podemos utilizar en una interfaz gráfica como lista desplegable?

	- [ ] JComboBox
	- [ ] JTextField
	- [ ] JList
	- [ ] JScrollPane
---

5. La propiedad ‘enabled’ común a la mayoría de controles de la biblioteca swing:

	- [ ] Permite mostrar u ocultar el control en la GUI.
	- [ ] Es de tipo String.
	- [ ] Hará que el control no pueda recibir el foco de la GUI en caso de estar deshabilitada.
	- [ ] Ninguna de las anteriores es correcta.
---
   
6. Si hemos declarado e inicializado un diálogo con la línea ‘JDialog myDialog = new JDialog(this, true);’, ¿qué orden deberemos ejecutar para mostrar el diálogo en modo modal?

	- [ ] myDialog.showDialog(true);
	- [ ] myDialog.setVisible(true);
	- [ ] myDialog.showModal(“OK”, “CANCEL”);
	- [ ] Ninguna de las anteriores es correcta.
---

7. Una consistencia adecuada de la interfaz gráfica de usuario contribuye a:

	- [ ] Recuperación de información, en caso de error.
	- [ ] Fácil mantenimiento.
	- [ ] Rápido aprendizaje.
	- [ ] Economizar en el desarrollo de la aplicación.
---

8. Se desea añadir a un componente que hereda de JPanel la capacidad de detectar cuando el ratón se ha movido dentro del área del componente. ¿Qué tipo de listener se debe añadir como argumento de la instrucción this.addMouseListener()?

	- [ ] MouseAdapter    
	- [ ] MouseListener    
	- [ ] ActionListener    
	- [ ] mouseMoved   
---

9. ¿Qué condiciones debe cumplir una clase para considerarse un JavaBean?

	- [ ] Implementar la interfaz Serializable y tener un constructor sin parámetros.
	- [ ] Las del apartado a y además proporcionar de un editor de propiedades.
	- [ ] Las del apartado b y además el BeanInfo correspondiente.    
	- [ ] Ninguna de las anteriores es correcta.
---

10. ¿Cuál es la salida de la siguiente aplicación?

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf7Kx986xgOyu4kZY7pa6TWxYhTB6sGE21lo98HBA9ocTZo4vRPxTE0BouC3KdfpzcSGZs71PuLpft35EdFr6M4gRB3hW49Kw7n8bIZrO5CxKb8iNMpZky3vGMSmF7pd2UdGMVtZw?key=9e1ypIjH40GfRWd62BRTTa1Y)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfKMFY-ynK0sHaeHOrJteEML0tudD66AlpI9cyRNCW1LAiZkEnvkbmV9jg2WFtdKQkzpdt1b7GTp22U2KudkLoJfWPXlOqEVVgDj2-8rDdQiXcyXrc08JuV6KUqcxRTg2l3uOX9?key=9e1ypIjH40GfRWd62BRTTa1Y)

- [ ] Muestra por la consola estándar el mensaje “zxc” cada 0.4 segundos.
- [ ] No muestra ningún mensaje en la consola.
- [ ] La aplicación no llega a compilar.
- [ ] La aplicación lanza una ‘Java Runtime Listener Exception’ cuando ejecuta la línea ‘Timer t = new Timer(400, myX);’.
---

11. Se ha creado un JavaBean ‘ImageShowerJB’ y se ha añadido a la Palette de controles swing del Designer de NetBeans. El código de control se muestra a continuación. Indica cuál de las siguientes opciones es la correcta.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeXkFa_pa7SYSF5J-1Lx57Q_eShtEPTm5Cw-bwq-D3ao24AXmfMK5OaAGIL7OLsiMufD27e7uVqsWfjZlE5Hk7jBrYBYEfMbNVUysIID-Xm1YxXCmEeAdWaVz0OUfSDTl4rmkkgQQ?key=9e1ypIjH40GfRWd62BRTTa1Y)

12. Las propiedades ‘images’ y ‘showingImageIndex’ no se mostrarán en el panel de Properties del Designer de NetBeans.
    
13. El componente debería haber implementado la interfaz BeanInfo para poderse haber añadido a la ‘Palette’ del Designer de NetBeans.
    
14. Al hacer click en el botón ‘...’ del panel de Properties del componente ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe2j6vw0TWjvU3sD-LG5iQAJY9bADQ2yPo00JfspPZPeu1-xd0FxamnSipyF8Qzi9jVotg8JAfY9LUoVXYVNUquPaftukzM-Ke0SKJrlSf4d1B2irsPy8F6jxWBqJvjZ6f_IX-v2A?key=9e1ypIjH40GfRWd62BRTTa1Y) aparecerá un JFileChooser que nos permitirá seleccionar los ficheros de imágen a mostrar.
    
15. El componente emitirá un evento ‘OnPaintComponent’ cada vez que sea redimensionado.
    

  

16. Se desea programar un listener para dotar a un componente de la posibilidad de emitir un evento el cual transfiera información a sus listeners (por ejemplo los datos de un fichero de imagen) a través del objeto event. ¿De qué clase debe heredar ETVImageChangedEvent?

  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdZ2EoXRgBT1W41m2PU5OpwuT9mtYdGorwIoCFyzIGlW1u6HATOv_fr2sqKywsh2UCR-enD8fzzZ94hJDf1bsIXroSOxF34KvNsW23pMx3XuOhdZ-Kbw0ntSJn0i1zv7kvs3nTs?key=9e1ypIjH40GfRWd62BRTTa1Y)

17. ActionListener
    
18. EventObject
    
19. EventListener
    
20. PropertyChangeSupport
    

  

21. Se está trabajando en NetBeans con un proyecto que contiene el JFrame ‘Main’ y cuyo layout se ha establecido a null. Si se arrastra un JButton desde la Palette de controles swing a la posición (10,30) aproximadamente del JFrame y el tamaño por defecto asignado a los JButtons es de 75 x 23, escribe el código añadido por NetBeans al método initComponents del fichero Main.java. ¿Escribe NetBeans alguna línea de código más en la clase Main?

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdHZ-PAkyhzdh9ONBD419ltbHykZmEwa_kCCG5vpqlMzxBKWsc07gmRBuz_lgP1tzlLgsFO-Sckd0FpSbkB2me4fgpDUsBTDrcRTbjt0C6f2Q9psimcWHqJBrbAPK3LFQTn6PNpLw?key=9e1ypIjH40GfRWd62BRTTa1Y)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdR3UNv5DMt_1flpF6gIXsvTrf70EjIq_yZ3BIA9YHAm4Vd1b_Exk0DP8SRyWNJtT8y3lPFcvj7P80SAVc_mWO7lVUW1V5LCNL-D7hRRnzFBHvKh-_z3OCdA4MQoV6-oLc90YaR?key=9e1ypIjH40GfRWd62BRTTa1Y)

**