# Tecnología de Videojuegos: Toma de contacto con la plantilla

## Tareas iniciales
- Clonar el [respositorio](https://github.com/dfbarrero/community-rpg) con PyCharm.
- Instalar las dependencias del juego en un ambiente virtual.
- Jugar al juego identificando las mecánicas.
  
## Estructura del código fuente
- Comprender la estructura de directorios.
  - Código fuente.
  - Recursos.
- Entender la función de los archivos y directorios ocultos del directorio raíz. Buscar en Google en caso necesario.
  
## Generalidades
- Identificar punto de entrada al juego.
- Localizar las constantes y configuración del juego.
- Entender cómo se gestionan las dependencias del juego (uso de una biblioteca externa no vista en clase).
- Entender cómo se identifica el directorio raíz del proyecto.
  
## Ciclo de vida del videojuego
- Entender, a grandes rasgos, el proceso de inicialización del juego. La función *load_map()* es especialmente delicada e interesante, así que échala un vistazo por encima y la miraremos con más detenimiento después.
- Identificar qué hace la función *arcade.resources.add_resource_handle()* presente en el archivo *__main__.py*. Busca en la documentación de Arcade o en el propio código fuente si es necesario.
- Entender cómo se realizan las transiciones entre vistas.
- En la vista del juego hay un modo depuración, encuentra la manera de activarlo.
- Entender cómo se realizan las transiciones entre mapas.

## Gestión de niveles
- Descarga e instala [Tiled Map Editor](https://www.mapeditor.org/), si no lo tienes hecho.
- Localiza el archivo que almacena el proyecto de Tiled de ábrelo con el editor.
- Abre los distintos mapas.
- Identifica las capas que tiene el mapa principal.
- Localiza las capas bloqueantes y no bloqueantes.
- Identifica las formas (*shapes*) que tiene el mapa principal. ¿Para qué sirven?
- Abre el mapa del interior de la casa y repite el proceso.
- Identifica cómo se representan las luces y los objetos que se pueden recoger.
- Importante: observa cómo tanto las luces como los objetos guardan propiedades que nosotros podemos definir con el editor.
  
## Integración con editor de niveles
Volvamos a la función *load_map()*, en el archivo *load_game_map.py*:
- Localiza la línea de código en donde se carga el mapa y el tipo de objeto en donde se guarda dicho mapa.
- Entiende, a grandes rasgos, cómo se cargan los NPCs del juego. Ten presente que la información de los NPCs se guarda en un archivo JSON.
- Entiende, a grandes rasgos, cómo se cargan las luces del juego. Observa cómo se accede a las propiedades definidas en el editor, como el color o el radio.
- Identifica el código encargado de crear los muros.

## NPCs
- Localiza las clases que implementan a los NPCs y al personaje del juego.
- Explica la relación entre los NPCs y el archivo JSON que guarda parte de sus propiedades (mira en la función *load_map()* y el contenido de los propios archivos JSON).
- Entiende a grandes rasgos, la implementación de los NPCs y del personaje.

## Mecánicas del juego
- Localiza el código encargado de buscar objetos.
- Entiende cómo se gestiona la colisión entre el personaje y las zonas del mapa que conducen a otro mapa distinto.
- Entiende cómo se gestiona el control del personaje mediante el teclado.

## UI
- Localiza el código encargado de mostrar el inventario.
- Entiende la vista que muestra un menú de usuario.

## Más generalidades
- Entiende, a grades rasgos, los métodos *on_draw()* y *on_update()* de la vista del juego.
