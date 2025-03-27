---
number headings: max 3, _.1.1.
tags: [PMDM]
obsidianUIMode: preview
banner: "![[pmdm.jpg]]"
banner_y: 0.42
cssclasses:
  - table-compact-clean
---

# **Tema 2.2** <br>Widgets de Diseño Básicos

Flutter tiene una amplia biblioteca de widgets de diseño. Aquí hay algunos de los más utilizados. El objetivo es que puedas comenzar rápidamente, en lugar de abrumarte con una lista completa. Para información sobre otros widgets disponibles consulta el [Catálogo de widgets](https://docs.flutter.dev/ui/widgets). Además, las páginas de widgets en la documentación de la API a menudo hacen sugerencias sobre widgets similares que podrían adaptarse mejor a tus necesidades.

Los siguientes widgets se dividen en dos categorías: widgets estándar de la [biblioteca de widgets](https://api.flutter.dev/flutter/widgets/widgets-library.html) y widgets especializados de la [Material Library](https://api.flutter.dev/flutter/material/material-library.html). Cualquier aplicación puede usar la biblioteca de widgets, pero solo las aplicaciones Material pueden usar la biblioteca de componentes Material.

|     |     |
| --- | --- |
| `Container`| Agrega relleno, márgenes, bordes, color de fondo u otras decoraciones a un widget.|
| `GridView`| Organiza widgets como una cuadrícula desplazable.|
| `ListView`| Organiza widgets como una lista desplazable.|
| `Stack`| Superpone un widget encima de otro.|

## 1. Container

Muchos diseños hacen un uso liberal de `Container` para separar widgets usando relleno, o para agregar bordes o márgenes. Puedes cambiar el fondo del dispositivo colocando todo el diseño en un `Container` y cambiando su color o imagen de fondo.

### 1.1. Resumen (Container)

- Agrega relleno, márgenes, bordes
- Cambia el color o imagen de fondo
- Contiene un solo widget hijo, pero ese hijo puede ser una `Row`, `Column` o incluso la raíz de un árbol de widgets

![Diagrama mostrando: margen, borde, relleno y contenido](Imágenes/flutter/edd190ada4103dd853937fad52a9b545_MD5.png)

### 1.2. Ejemplos (Container)

Este diseño consiste en una columna con dos filas, cada una conteniendo 2 imágenes. Se usa un `Container` para cambiar el color de fondo de la columna a un gris más claro.

```dart
Widget _buildImageColumn() {
  return Container(
    decoration: const BoxDecoration(color: Colors.black26),
    child: Column(children: [_buildImageRow(1), _buildImageRow(3)]),
  );
}
```

![Captura de pantalla mostrando 2 filas, cada una conteniendo 2 imágenes](Imágenes/flutter/1fb551a6122ccf7c51706817bb811b24_MD5.png)

También se usa un `Container` para agregar un borde redondeado y márgenes a cada imagen:

```dart
Widget _buildDecoratedImage(int imageIndex) => Expanded(
  child: Container(
    decoration: BoxDecoration(
      border: Border.all(width: 10, color: Colors.black38),
      borderRadius: const BorderRadius.all(Radius.circular(8)),
    ),
    margin: const EdgeInsets.all(4),
    child: Image.asset('images/pic$imageIndex.jpg'),
  ),
);

Widget _buildImageRow(int imageIndex) => Row(
  children: [
    _buildDecoratedImage(imageIndex),
    _buildDecoratedImage(imageIndex + 1),
  ],
);
```

## 2. GridView

Usa `GridView` para organizar widgets como una lista bidimensional. `GridView` proporciona dos listas prefabricadas, o puedes construir tu propia cuadrícula personalizada. Cuando un `GridView` detecta que su contenido es demasiado largo para la caja de renderizado, se desplaza automáticamente.

### 2.1. Resumen (GridView)

- Organiza widgets en una cuadrícula
- Detecta cuando el contenido de la columna excede la caja de renderizado y proporciona desplazamiento automático
- Construye tu propia cuadrícula personalizada, o usa una de las proporcionadas:
  - `GridView.count` te permite especificar el número de columnas
  - `GridView.extent` te permite especificar el ancho máximo en píxeles de un mosaico

> [!note]
> Cuando muestres una lista bidimensional donde es importante qué fila y columna ocupa una celda (por ejemplo, es la entrada en la columna "calorías" para la fila "aguacate"), usa `Table`.

### 2.2. Ejemplos (GridView)

![Una cuadrícula de 3 columnas de fotos](Imágenes/flutter/ddda61426f9eeafa35a71965e8cfb8bc_MD5.png)

Usa `GridView.extent` para crear una cuadrícula con mosaicos de un máximo de 150 píxeles de ancho.

![Una cuadrícula de 2 columnas con pies de página](Imágenes/flutter/bb3ba2b0e0271efe50579a58b3af6593_MD5.png)

Usa `GridView.count` para crear una cuadrícula de 2 mosaicos de ancho en modo retrato y 3 mosaicos de ancho en modo paisaje. Los títulos se crean configurando la propiedad `footer` para cada `GridTile`.

```dart
Widget _buildGrid() => GridView.extent(
  maxCrossAxisExtent: 150,
  padding: const EdgeInsets.all(4),
  mainAxisSpacing: 4,
  crossAxisSpacing: 4,
  children: _buildGridTileList(30),
);

// Las imágenes se guardan con nombres pic0.jpg, pic1.jpg...pic29.jpg.
// El constructor List.generate() permite una manera fácil de crear
// una lista cuando los objetos tienen un patrón de nombres predecible.
List<Widget> _buildGridTileList(int count) =>
    List.generate(count, (i) => Image.asset('images/pic$i.jpg'));
```

## 3. ListView

`ListView`, un widget similar a una columna, proporciona desplazamiento automático cuando su contenido es demasiado largo para su caja de renderizado.

### 3.1. Resumen (ListView)

- Una `Column` especializada para organizar una lista de cajas
- Puede organizarse horizontal o verticalmente
- Detecta cuando su contenido no cabe y proporciona desplazamiento
- Menos configurable que `Column`, pero más fácil de usar y admite desplazamiento

### 3.2. Ejemplos (ListView)

![ListView conteniendo cines y restaurantes](Imágenes/flutter/a1c77502321c256720ab8cdc0f656978_MD5.png)

Usa `ListView` para mostrar una lista de negocios usando `ListTile`s. Un `Divider` separa los cines de los restaurantes.

![ListView conteniendo tonos de azul](Imágenes/flutter/45c4f1962e9aa76a6712b30d0a3521d6_MD5.png)

Usa `ListView` para mostrar los `Colors` de la [paleta de diseño Material 2](https://m2.material.io/design/color/the-color-system.html#tools-for-picking-colors) para una familia de colores en particular.

```dart
Widget _buildList() {
  return ListView(
    children: [
      _tile('CineArts en el Empire', '85 W Portal Ave', Icons.theaters),
      _tile('The Castro Theater', '429 Castro St', Icons.theaters),
      _tile('Alamo Drafthouse Cinema', '2550 Mission St', Icons.theaters),
      _tile('Roxie Theater', '3117 16th St', Icons.theaters),
      _tile(
        'United Artists Stonestown Twin',
        '501 Buckingham Way',
        Icons.theaters,
      ),
      _tile('AMC Metreon 16', '135 4th St #3000', Icons.theaters),
      const Divider(),
      _tile('K\'s Kitchen', '757 Monterey Blvd', Icons.restaurant),
      _tile('Emmy\'s Restaurant', '1923 Ocean Ave', Icons.restaurant),
      _tile('Chaiya Thai Restaurant', '272 Claremont Blvd', Icons.restaurant),
      _tile('La Ciccia', '291 30th St', Icons.restaurant),
    ],
  );
}

ListTile _tile(String title, String subtitle, IconData icon) {
  return ListTile(
    title: Text(
      title,
      style: const TextStyle(fontWeight: FontWeight.w500, fontSize: 20),
    ),
    subtitle: Text(subtitle),
    leading: Icon(icon, color: Colors.blue[500]),
  );
}
```

## 4. Stack

Usa `Stack` para organizar widgets encima de un widget base, a menudo una imagen. Los widgets pueden superponerse completamente o parcialmente al widget base.

### 4.1. Resumen (Stack)

- Usa para widgets que se superponen a otro widget
- El primer widget en la lista de hijos es el widget base; los hijos posteriores se superponen encima de ese widget base
- El contenido de un `Stack` no puede desplazarse
- Puedes elegir recortar hijos que excedan la caja de renderizado

### 4.2. Ejemplos (Stack)

![Imagen de avatar circular con una etiqueta](Imágenes/flutter/1ce27b24a42f7051595b215c5af2b25a_MD5.png)

Usa `Stack` para superponer un `Container` (que muestra su `Text` en un fondo negro translúcido) encima de un `CircleAvatar`. El `Stack` desplaza el texto usando la propiedad `alignment` y `Alignment`s.

![Una imagen con un icono superpuesto encima](Imágenes/flutter/256ec9f92829d9ecfc02471c09050b06_MD5.png)

Usa `Stack` para superponer un icono encima de una imagen.

```dart
Widget _buildStack() {
  return Stack(
    alignment: const Alignment(0.6, 0.6),
    children: [
      const CircleAvatar(
        backgroundImage: AssetImage('images/pic.jpg'),
        radius: 100,
      ),
      Container(
        decoration: const BoxDecoration(color: Colors.black45),
        child: const Text(
          'Mia B',
          style: TextStyle(
            fontSize: 20,
            fontWeight: FontWeight.bold,
            color: Colors.white,
          ),
        ),
      ),
    ],
  );
}
```

## 5. Card

Una `Card`, de la *Material Library*, contiene fragmentos de información relacionados y puede componerse de casi cualquier widget, pero a menudo se usa con `ListTile`. `Card` tiene un solo hijo, pero su hijo puede ser una columna, fila, lista, cuadrícula u otro widget que admita múltiples hijos. Por defecto, una `Card` reduce su tamaño a 0 por 0 píxeles. Puedes usar `SizedBox` para restringir el tamaño de una tarjeta.

En Flutter, una `Card` tiene esquinas ligeramente redondeadas y una sombra paralela, dándole un efecto 3D. Cambiar la propiedad `elevation` de una `Card` te permite controlar el efecto de sombra. Por ejemplo, configurar la elevación a 24 eleva visualmente la `Card` más lejos de la superficie y hace que la sombra se disperse más. Para una lista de valores de elevación admitidos, consulta [Elevación](https://m3.material.io/styles/elevation) en las [directrices de Material](https://m3.material.io/styles). Especificar un valor no admitido deshabilita completamente la sombra paralela.

### 5.1. Resumen (Card)

- Implementa una tarjeta Material
- Usada para presentar fragmentos de información relacionados
- Acepta un solo hijo, pero ese hijo puede ser una `Row`, `Column` u otro widget que contenga una lista de hijos
- Se muestra con esquinas redondeadas y una sombra paralela
- El contenido de una `Card` no puede desplazarse
- De la [biblioteca Material](https://api.flutter.dev/flutter/material/material-library.html)
### 5.2. Ejemplos (Card)

![Card conteniendo 3 ListTiles](Imágenes/flutter/aa877d8e0ba6577d3663c2c5479f1f62_MD5.png)

Una `Card` que contiene 3 `ListTile`s y dimensionada envolviéndola con un `SizedBox`. Un `Divider` separa el primer y segundo `ListTile`.

![Tarjeta táctil conteniendo una imagen y múltiples formas de texto](Imágenes/flutter/b9abd4c999160a042d2065de07dcad95_MD5.png)

Una `Card` que contiene una imagen y texto.

```dart
Widget _buildCard() {
  return SizedBox(
    height: 210,
    child: Card(
      child: Column(
        children: [
          ListTile(
            title: const Text(
              '1625 Main Street',
              style: TextStyle(fontWeight: FontWeight.w500),
            ),
            subtitle: const Text('My City, CA 99984'),
            leading: Icon(Icons.restaurant_menu, color: Colors.blue[500]),
          ),
          const Divider(),
          ListTile(
            title: const Text(
              '(408) 555-1212',
              style: TextStyle(fontWeight: FontWeight.w500),
            ),
            leading: Icon(Icons.contact_phone, color: Colors.blue[500]),
          ),
          ListTile(
            title: const Text('costa@example.com'),
            leading: Icon(Icons.contact_mail, color: Colors.blue[500]),
          ),
        ],
      ),
    ),
  );
}
```

## 6. ListTile

Usa `ListTile`, un widget de fila especializado de la biblioteca Material, para crear fácilmente una fila que contenga hasta 3 líneas de texto y iconos iniciales y finales opcionales. `ListTile` se usa más comúnmente en `Card` o `ListView`, pero puede usarse en otros lugares.

### 6.1. Resumen (ListTile)

- Una fila especializada que contiene hasta 3 líneas de texto e iconos opcionales
- Menos configurable que `Row`, pero más fácil de usar
- De la [biblioteca Material](https://api.flutter.dev/flutter/material/material-library.html)

### 6.2. Ejemplos (ListTile)

![Card conteniendo 3 ListTiles](Imágenes/flutter/aa877d8e0ba6577d3663c2c5479f1f62_MD5.png)

Una `Card` que contiene 3 `ListTile`.

![4 ListTiles, cada una conteniendo un avatar inicial](Imágenes/flutter/fe50f415a41ec764560dc15f55b88131_MD5.png)

Usa `ListTile` con widgets iniciales.
