# Videogame design and programming course

## Contents

0.- [Git and GitHub](git/)

1.- [Python for videogames](python/)

2.- [More Python for videogames](morePython/)

3.- [OOP in Arcade](oop-arcade/)

4.- [Introduction to videogames](introduction/)

5.- [Videogames development team](team/)

6.- [Videogame engine](engine/)

7.- [Videogame engine architecture](architecture/)

8.- [Design patterns in videogames](patterns/)

## Assignments

- Ejemplo de tareas [[GitHub](assignment/tareas.md), [HackMD](https://hackmd.io/@dfbarrero/tareas)]
- Toma de contacto con la plantilla [[GitHub](assignment/proyecto.md), [HackMD](https://hackmd.io/@dfbarrero/proyecto-101)]

## Compilation

Use xelatex or lualatex as latex processors, otherones would raise a compilation error. Custom UAH fonts are needed to properly compile the project. The original template used to format the slides, including the fonts, can be downloaded from [this repository](https://github.com/dfbarrero/UAH-beamer-template). By default, the theme will use UAH fonts installed in the system, edit the theme to easily change this behaviour.

*Manual execution of xelatex or lualatex would generate a compilation error*, since the tex documents require a variable containing the course for which the slides are compiled. You should use instead the command make which calls xelatex with the proper variable definition.

Several Makefiles are provided to ease repository management. Make executed from the root folder would compile the entire collections of slides for all the courses, while "make view" would open a PDF viewer with all the complided slides. On the contrary, if make is executed within a subfolder, it would only compile the slided contained in that folder. By default, make compiles the slides for all the courses, while "make course" would build the slides for that course. 

The courses for which the slides are compiled are defined in the TARGET variable, in the begining of the Makefiles. The courses details such their names are defined in [gsi-parametros.sty](gsi-parametros.sty), in the root folder.
