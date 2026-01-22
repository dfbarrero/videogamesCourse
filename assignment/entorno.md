# Lab 0: Puesta a punto del entorno de trabajo

### Objetivos
-  Preparar el entorno de trabajo necesario para seguir la asignatura
-  Introducir los entornos virtuales

### Prerrequisitos
Se presupone que tanto Python como VS Code están debidamente instalados. También se va a necesitar la extensión *Python Environments*.

### Introducción
Un problema recurrente en la Programación es gestionar múltiples versiones de las bibliotecas. Normalmente vamos a hacer actualizaciones del sistema que modernizarán la versión de las bibliotecas que tenemos instalada, y, si esa nueva versión rompe la compatibilidad hacia atrás, nuestras aplicaciones dejarían de funcionar correctamente.

Un problema asociado y también muy común, es que una aplicación que funciona correctamente en un determinado equipo, al ser ejecutada en otro equipo, con otras versiones de las bibliotecas, puede generar un error. Esto es algo especialmente importante cuando trabajamos en un entorno de desarrollo diferente al de producción (lo habitual en el mundo profesional) o cuando un profesor corrige una práctica en su pripio equipo (lo habitual mientras estás la carrera).

> [!Warning]
> Bajo ninguna circunstancia es admisible que nuestros desarrollos fallen cuando se ejecutan en equipos distintos, incluyendo el equipo del profesor. No vale la excusa de que funciona en tu equipo: **las potenciales causas de fallo deberían de ser conocidas y prevenidas**. Un ejemplo de causa de fallo es que haya distintas versiones de bibliotecas.

Además de que la versión de la biblioteca puede ser problemática, también la propia versión de Python es algo que puede inducir errores. Una aplicación que funciona correctamente en una determinada versión de Python, puede no funcionar en otra versión de Python. Por ejemplo,`print "Hola, Mundo"` funcionaría con Python 2.x, pero no con Python 3.x.

El problema se hace mayor si consideramos que habitualmente vamos a estar trabajando en distintos proyectos, que pueden tener distintas necesidades en cuanto a la versión de las bibliotecas y de Python. En estas circunstancias una simple actualización del sistema puede tener un impacto impredecible.

En general, desarrollar sobre la instalación desnuda de Python que tengamos en nuestra máquina es una mala costumbre que puede generar problemas, sobre todo cuando se desarrolla a nivel profesional. Para solucionar esta problema se crearon los entornos virtuales, cuya utilización es siempre recomendable.

> [!NOTE] 
> Hay algunas situaciones muy concretas en donde puede estar justifcado no usar ambientes virtuales, pero por lo general es seguro acostumbrarse a usar entornos virtuales para todos nuestros proyectos.

### Entornos virtuales
El concepto de entorno virtual es muy similar al de máquina virtual. Si una máquina virtual permite que las aplicaciones se ejecuten sobre una arquitectura desligada de nuestra máquina física, un entorno virtual permite ejecutar aplicaciones Python con un intérprete y bibliotecas diferentes a las del sistema.

Un entorno virtual permite definir entornos de ejecución completos, lo que incluye tanto al **intérprete de Python** como al **conjunto de bibliotecas**. Existen distintas soluciones para crear entornos virtuales en Python, siendo las más conocidas las siguientes:

- **venv** - Herramienta incluída por defecto en Python a partir de la versión 3.3. Es sencilla y ampliamente utilizada. Su uso es recomendable para la mayoría de nuestros proyectos.
- **virtualenv** - Antecesor de venv, asociados a versiones antiguas de Python. En desuso a favor de venv.
- **conda** - Herramienta especialmente popular en el mundo de la Inteligencia Artificial / Ciencia de Datos, en donde su uso es mayoritario. Incorpora todo un conjunto de soluciones para la gestión de depencias que va más allá de Python. 

Existen otros entornos virtuales con mucha menos presencia: pipenv, poetry o pyenv.

### Preparación del entorno virtual

De cara a la asignatura se recomienda utilizar venv, por su sencillez, y por ser suficiente para las necesidades que tendremos. Por fortuna, venv ya viene  por defecto en la mayoría de las instalaciones de Python, lo que simplifica su utilización.

Para poder trabajar con un entorno virtual, lo primero que tendremos que hacer es crearlo, para lo que se define qué intérprete tendrá asociado, y se instalarán una serie de bibliotecas que *sólo estarán disponbles dentro de ese entorno*. El entorno virtual se instala dentro de un directorio oculto llamado`.venv` en la raíz del proyecto; este directorio contendrá una instalación completa de Python así como de las bibliotecas asociadas, por lo que apenas afecta al sistema.

> [!TIP] 
> Cada proyecto debería de tener su propio entorno virtual.


La siguiente animación muestra cómo se crea un nuevo ambiente venv en VSCode.

![Creación de un nuevo entorno virtual en VS Code](https://raw.githubusercontent.com/dfbarrero/videogamesCourse/master/assignment/entorno/venv-vscode.gif)

Observa que al crear el nuevo entorno virtual, VSCode nos permite asociarlo a una determinada versión del intérprete Python. 

> [!WARNING]  Se recomienda usar la versión 3.10 de Python.

Fíjate también que al crear el entorno virtual, se agrega un nuevo directorio al proyecto con el intérprete y las bibliotecas. Merece la pena que dedices unos segundos a navegar por ese directorio.

### Instalación de las bibliotecas

Crea un proyecto nuevo e intenta ejecutar el siguiente código dentro de un entorno virtual limpio:

```Python=
import arcade

WIDTH = 600
HEIGHT = 800

arcade.open_window(WIDTH, HEIGHT, "Ejemplo")

arcade.run()
```

Si todo está bien hecho, debería de salir un error como el siguiente:

```
Traceback (most recent call last):
  File "/home/david/videojuegos/hola.py", line 1, in <module>
    import arcade
ModuleNotFoundError: No module named 'arcade'
```

Es una indicación de que el intérprete no ha encontrado la biblioteca Arcade, y no la ha encontrado porque no está instalada. Por fortuna Python nos proporciona ```pip```, una herramienta que nos facilita en gran medida la gestión de paquetes.

Ve a la terminal de VS Code e introduce la orden ```pip install arcade==2.6.17```. La terminal mostrará bastante texto, indicando que tanto Arcade como todas sus depenencias se están instalando; si todo está correcto, una vez finalice deberías de tener la biblioteca instalada en tu entorno virtual. Observa que hemos especificado una versión concreta de Arcade, la 2.6.17. Si lo dejamos vacío pip instalaría la última versión disponible.

> [!WARNING]  Se debe usar la versión 2.6.17 de Arcade.

Vuelve a ejecutar el script anterior.

Y ya está, el entorno de trabajo está preparado.

### Más información

Tienes más información sobre entornos virtuales en el siguiente enlace.

- [Python environments in VS Code](https://code.visualstudio.com/docs/python/environments)

El siguiente video es un tutorial para instalar PyGame (otra biblioteca para desarrollo de videjuegos hecha con Python) en un entorno virtual:

{%youtube -IRMWgjOMDo %}
