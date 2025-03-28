---
tags: [DAM, PMDM]
cssclasses: [dam-pmdm, table-compact-clean]
banner: "![[pmdm.jpg]]"
banner_y: 0.42
---

# **Tema 2.1** <br>Organización de Widgets

## 1. Organizar un widget

**Pasos para crear un widget simple**

**1.** Seleccionar un widget de diseño como `Center`.

**2.** Crear un widget visible como `Text`.

**3.** Agregar el widget visible al widget de diseño.

**4.** Incorporar el widget de diseño a la página en `build()`.

### 1.1. **Seleccionar un widget de diseño**

Elige entre una variedad de [widgets de diseño](https://docs.flutter.dev/ui/widgets/layout) según cómo quieras alinear o restringir un widget visible, ya que estas características generalmente se transmiten al widget contenido.

Por ejemplo, podrías usar el widget de diseño `Center` para centrar un widget visible horizontal y verticalmente:

```dart
Center(
  // contenido aquí
)
```

### 1.2. **Crear un widget visible**

Elige un [widget visible](https://docs.flutter.dev/ui/widgets) para que tu aplicación contenga elementos visibles, como texto, imágenes o iconos.

Por ejemplo, podrías usar el widget `Text` para mostrar texto:

```dart
Text('Hola Mundo')
```

### 1.3. **Agregar el widget visible al widget de diseño**

Todos los widgets de diseño tienen una de las siguientes propiedades:

- Una propiedad `child` si toman un solo hijo, como `Center` o `Container`.
- Una propiedad `children` si toman una lista de widgets, como `Row`, `Column`, `ListView` o `Stack`.

Agrega el widget `Text` al widget `Center`:

```dart
const Center(
  child: Text('Hello World'),
),
```

### 1.4. **Agregar el widget de diseño a la página**

Una aplicación de Flutter es en sí misma un widget, y la mayoría de los widgets tienen un método `build()`. Instanciar y devolver un widget en el método `build()` de la aplicación muestra el widget.

Para una aplicación general, puedes agregar el widget `Container` al método `build()` de la aplicación:

```dart
class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: const BoxDecoration(color: Colors.white),
      child: const Center(
        child: Text(
          'Hello World',
          textDirection: TextDirection.ltr,
          style: TextStyle(fontSize: 32, color: Colors.black87),
        ),
      ),
    );
  }
}
```

Por defecto, una aplicación general no incluye una `AppBar`, título o color de fondo. Si deseas estas características en una aplicación general, debes construirlas tú mismo. Esta aplicación cambia el color de fondo a blanco y el texto a gris oscuro para imitar una aplicación Material.

### 1.5. **Ejecutar tu aplicación**

Después de agregar tus widgets, ejecuta tu aplicación. Al ejecutarla, deberías ver *Hola Mundo*.

![Captura de pantalla de la aplicación mostrando Hola Mundo](Imágenes/flutter/9860ba00cb29d41fc94df99643f33d07_MD5.png)

## 2. Organizar múltiples widgets vertical y horizontalmente

**Objetivo**

- `Row` y `Column` son dos de los patrones de diseño más utilizados.
- `Row` y `Column` toman una lista de widgets hijos.
- Un widget hijo puede ser a su vez un `Row`, `Column` u otro widget complejo.
- Puedes especificar cómo un `Row` o `Column` alinea a sus hijos, tanto vertical como horizontalmente.
- Puedes estirar o restringir widgets hijos específicos.
- Puedes especificar cómo los widgets hijos usan el espacio disponible del `Row` o `Column`.

Para crear una fila o columna en Flutter, agregas una lista de widgets hijos a un widget `Row` o `Column`. A su vez, cada hijo puede ser una fila o columna, y así sucesivamente. El siguiente ejemplo muestra cómo es posible anidar filas o columnas dentro de filas o columnas.

Este diseño está organizado como una `Row`. La fila contiene dos hijos: una columna a la izquierda y una imagen a la derecha:

![Captura de pantalla con llamadas mostrando la fila que contiene dos hijos](Imágenes/flutter/8f450204425e5fb90544a50734fcf14e_MD5.png)

El árbol de widgets de la columna izquierda anida filas y columnas.

![Diagrama mostrando una columna izquierda desglosada en sus subfilas y subcolumnas](Imágenes/flutter/1a2816777a3f7c92878e6acbc7cb592b_MD5.png)

Implementarás parte del código de diseño de Pavlova en [Anidar filas y columnas](https://docs.flutter.dev/ui/layout#nesting-rows-and-columns).

> [!note] Nota
> `Row` y `Column` son widgets primitivos básicos para diseños horizontales y verticales. Estos widgets de bajo nivel permiten la máxima personalización. Flutter también ofrece widgets especializados de alto nivel que podrían ser suficientes para tus necesidades. Por ejemplo, en lugar de `Row`, podrías preferir `ListTile`, un widget fácil de usar con propiedades para iconos iniciales y finales, y hasta 3 líneas de texto. En lugar de `Column`, podrías preferir `ListView`, un diseño similar a una columna que se desplaza automáticamente si su contenido es demasiado largo para el espacio disponible. Para más información, consulta [Widgets de diseño comunes](https://docs.flutter.dev/ui/layout#common-layout-widgets). 

### 2.1. **Alinear widgets**

Puedes controlar cómo una fila o columna alinea a sus hijos usando las propiedades `mainAxisAlignment` y `crossAxisAlignment`. Para una fila, el eje principal corre horizontalmente y el eje transversal verticalmente. Para una columna, el eje principal corre verticalmente y el eje transversal horizontalmente.

![Diagrama mostrando el eje principal y transversal para una fila](Imágenes/flutter/e449c62c8a11bf9f1ba4a56f6ef9d53a_MD5.png)

![Diagrama mostrando el eje principal y transversal para una columna](Imágenes/flutter/9e4f6ec14ed7b76f02037f6873d6f443_MD5.png)

Los enums `MainAxisAlignment` y `CrossAxisAlignment` ofrecen una variedad de constantes para controlar la alineación.

> [!note] Nota
> Cuando agregas imágenes a tu proyecto, necesitas actualizar el archivo `pubspec.yaml` para acceder a ellas. Este ejemplo usa `Image.asset` para mostrar las imágenes. No necesitas hacer esto si estás referenciando imágenes en línea usando `Image.network`. 

En el siguiente ejemplo, cada una de las 3 imágenes tiene 100 píxeles de ancho. La caja de renderizado (en este caso, toda la pantalla) tiene más de 300 píxeles de ancho, por lo que configurar la alineación del eje principal como `spaceEvenly` divide el espacio horizontal libre de manera uniforme entre, antes y después de cada imagen.

```dart
Row(
  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
  children: [
    Image.asset('images/pic1.jpg'),
    Image.asset('images/pic2.jpg'),
    Image.asset('images/pic3.jpg'),
  ],
);
```

![Fila con 3 imágenes espaciadas uniformemente](Imágenes/flutter/ef4809dba83bb2cf8216946e11fee12e_MD5.png)

Las columnas funcionan de la misma manera que las filas. El siguiente ejemplo muestra una columna de 3 imágenes, cada una con 100 píxeles de alto. La altura de la caja de renderizado (en este caso, toda la pantalla) es mayor a 300 píxeles, por lo que configurar la alineación del eje principal como `spaceEvenly` divide el espacio vertical libre de manera uniforme entre, encima y debajo de cada imagen.

```dart
Column(
  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
  children: [
    Image.asset('images/pic1.jpg'),
    Image.asset('images/pic2.jpg'),
    Image.asset('images/pic3.jpg'),
  ],
);
```

![Columna mostrando 3 imágenes espaciadas uniformemente](Imágenes/flutter/634588ac17d31756a789260099257223_MD5.png)

### 2.2. **Dimensionar widgets**

Cuando un diseño es demasiado grande para un dispositivo, aparece un patrón amarillo y negro a lo largo del borde afectado. Aquí hay un ejemplo de una fila que es demasiado ancha:

![Fila demasiado ancha](Imágenes/flutter/fba874cf4dd57aceb7cd8b433507264f_MD5.png)

Los widgets pueden dimensionarse para ajustarse dentro de una fila o columna usando el widget `Expanded`. Para solucionar el ejemplo anterior donde la fila de imágenes es demasiado ancha para su caja de renderizado, envuelve cada imagen con un widget `Expanded`.

```dart
Row(
  crossAxisAlignment: CrossAxisAlignment.center,
  children: [
    Expanded(child: Image.asset('images/pic1.jpg')),
    Expanded(child: Image.asset('images/pic2.jpg')),
    Expanded(child: Image.asset('images/pic3.jpg')),
  ],
);
```

![Fila de 3 imágenes que son demasiado anchas, pero cada una está restringida a ocupar solo 1/3 del espacio](Imágenes/flutter/24a9808747e82cb358517472a9ea68c0_MD5.png)

Quizás quieras que un widget ocupe el doble de espacio que sus hermanos. Para esto, usa la propiedad `flex` del widget `Expanded`, un entero que determina el factor de flexión para un widget. El factor de flexión predeterminado es 1. El siguiente código establece el factor de flexión de la imagen del medio en 2:

```dart
Row(
  crossAxisAlignment: CrossAxisAlignment.center,
  children: [
    Expanded(child: Image.asset('images/pic1.jpg')),
    Expanded(flex: 2, child: Image.asset('images/pic2.jpg')),
    Expanded(child: Image.asset('images/pic3.jpg')),
  ],
);
```

![Fila de 3 imágenes con la imagen del medio el doble de ancha que las demás](Imágenes/flutter/d0d1a9b57afd2ac56a8867a66b2efb2a_MD5.png)

### 2.3. **Agrupar widgets**

Por defecto, una fila o columna ocupa tanto espacio como sea posible a lo largo de su eje principal, pero si deseas agrupar a los hijos más juntos, configura su `mainAxisSize` como `MainAxisSize.min`. El siguiente ejemplo usa esta propiedad para agrupar los iconos de estrellas.

```dart
Row(
  mainAxisSize: MainAxisSize.min,
  children: [
    Icon(Icons.star, color: Colors.green[500]),
    Icon(Icons.star, color: Colors.green[500]),
    Icon(Icons.star, color: Colors.green[500]),
    const Icon(Icons.star, color: Colors.black),
    const Icon(Icons.star, color: Colors.black),
  ],
)
```

![Fila de 5 estrellas, agrupadas en el centro de la fila](Imágenes/flutter/2b1881d5101cae69b9625ae2f772347c_MD5.png)

### 2.4. **Anidar filas y columnas**

El marco de diseño permite anidar filas y columnas dentro de filas y columnas tan profundamente como necesites. Veamos el código para la sección delineada del siguiente diseño:

![Captura de pantalla de la aplicación Pavlova, con las filas de calificaciones e iconos delineadas en rojo](Imágenes/flutter/e3ee024860b2c95492fe50ee2b75f170_MD5.png)

La sección delineada se implementa como dos filas. La fila de calificaciones contiene cinco estrellas y el número de reseñas. La fila de iconos contiene tres columnas de iconos y texto.

El árbol de widgets para la fila de calificaciones:

![Árbol de widgets de la fila de calificaciones](Imágenes/flutter/859d83117f1c422f728674a3543e99b1_MD5.png)

La variable `ratings` crea una fila que contiene una fila más pequeña de 5 iconos de estrellas y texto:

```dart
final stars = Row(
  mainAxisSize: MainAxisSize.min,
  children: [
    Icon(Icons.star, color: Colors.green[500]),
    Icon(Icons.star, color: Colors.green[500]),
    Icon(Icons.star, color: Colors.green[500]),
    const Icon(Icons.star, color: Colors.black),
    const Icon(Icons.star, color: Colors.black),
  ],
);

final ratings = Container(
  padding: const EdgeInsets.all(20),
  child: Row(
    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
    children: [
      stars,
      const Text(
        '170 Reseñas',
        style: TextStyle(
          color: Colors.black,
          fontWeight: FontWeight.w800,
          fontFamily: 'Roboto',
          letterSpacing: 0.5,
          fontSize: 20,
        ),
      ),
    ],
  ),
);
```

> [!note] Nota 
> Para minimizar la confusión visual que puede resultar del código de diseño fuertemente anidado, implementa partes de la interfaz de usuario en variables y funciones.

La fila de iconos, debajo de la fila de calificaciones, contiene 3 columnas; cada columna contiene un icono y dos líneas de texto, como puedes ver en su árbol de widgets:

![Árbol de widgets de iconos](Imágenes/flutter/d741feb2342132cfe44ed9347b91ba15_MD5.png)

La variable `iconList` define la fila de iconos:

```dart
const descTextStyle = TextStyle(
  color: Colors.black,
  fontWeight: FontWeight.w800,
  fontFamily: 'Roboto',
  letterSpacing: 0.5,
  fontSize: 18,
  height: 2,
);

// DefaultTextStyle.merge() permite crear un estilo de texto
// predeterminado que heredan su hijo y todos los hijos posteriores.
final iconList = DefaultTextStyle.merge(
  style: descTextStyle,
  child: Container(
    padding: const EdgeInsets.all(20),
    child: Row(
      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
      children: [
        Column(
          children: [
            Icon(Icons.kitchen, color: Colors.green[500]),
            const Text('PREP:'),
            const Text('25 min'),
          ],
        ),
        Column(
          children: [
            Icon(Icons.timer, color: Colors.green[500]),
            const Text('COOK:'),
            const Text('1 hr'),
          ],
        ),
        Column(
          children: [
            Icon(Icons.restaurant, color: Colors.green[500]),
            const Text('FEEDS:'),
            const Text('4-6'),
          ],
        ),
      ],
    ),
  ),
);
```

La variable `leftColumn` contiene las filas de calificaciones e iconos, así como el título y el texto que describe la Pavlova:

```dart
final leftColumn = Container(
  padding: const EdgeInsets.fromLTRB(20, 30, 20, 20),
  child: Column(children: [titleText, subTitle, ratings, iconList]),
);
```

La columna izquierda se coloca en un `SizedBox` para restringir su ancho. Finalmente, la interfaz de usuario se construye con toda la fila (que contiene la columna izquierda y la imagen) dentro de una `Card`.

La imagen de Pavlova es de *Pixabay*. Puedes incrustar una imagen de la red usando `Image.network()`, pero para este ejemplo, la imagen se guarda en un directorio de imágenes del proyecto, se agrega al archivo `pubspec` y se accede usando `Images.asset()`.

```dart
body: Center(
  child: Container(
    margin: const EdgeInsets.fromLTRB(0, 40, 0, 30),
    height: 600,
    child: Card(
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [SizedBox(width: 440, child: leftColumn), mainImage],
      ),
    ),
  ),
),
```

> [!note] Consejo
> El ejemplo de Pavlova funciona mejor horizontalmente en un dispositivo ancho, como una tableta. Si estás ejecutando este ejemplo en el simulador de iOS, puedes seleccionar un dispositivo diferente usando el menú **Hardware > Device.** Para este ejemplo, recomendamos el iPad Pro. Puedes cambiar su orientación al modo horizontal usando **Hardware > Rotate.** También puedes cambiar el tamaño de la ventana del simulador (sin cambiar el número de píxeles lógicos) usando **Window > Scale.**