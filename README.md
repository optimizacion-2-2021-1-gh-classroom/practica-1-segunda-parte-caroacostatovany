![](https://mcdatos.itam.mx/wp-content/uploads/2020/11/ITAM-LOGO.03.jpg)
# Optimización 2 2021-1 Práctica I - 2a Parte: Implementación de método numérico para resolver problemas de optimización convexa #

## Equipo 1

| Nombre | User Github | Tarea a realizar |
|:---:|:---:|:---|
| Carolina Acosta | caroacostatovany| TBD |
| Eduardo Moreno | Eduardo-Moreno| TBD |
| Leonardo Ceja | lecepe00| TBD |
| Cecilia Avilés | cecyar| TBD |

## Instrucciones

Implementar un método numérico que resuelva problemas de optimización convexa de pequeña escala. 

Se entrega:
* Implementación del método numérico elegido en un lenguaje de su elección.

* El método numérico debe poder usarse a través de un paquete del lenguaje que ustedes elijan (hay que crear un paquete que tenga su método numérico). Por ejemplo si es de *Python* entonces: `pip install <pkg>` y luego `import <pkg>`.

* Crear documentación del paquete con [sphinx](https://www.sphinx-doc.org/en/master/). Ver [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) para un ejemplo de lo que un paquete de software debería tener y [example-python-package-and-sphinx-doc](https://github.com/palmoreck/example-python-package-and-sphinx-doc) de instrucciones y archivos que pueden usar de apoyo. Si conocen otra herramienta para documentación pueden usarla. Algunos ejemplos de documentación de *Python, R, Julia* que pueden crearse con `sphinx` son: [rasterio](https://rasterio.readthedocs.io/en/latest/), [Spatial Data Science with R](https://rspatial.org/raster/index.html), [MLDataUtils](https://mldatautilsjl.readthedocs.io/en/latest/index.html). La publicación de la documentación realícenla con [github pages](https://pages.github.com/) o [readthedocs](https://readthedocs.org/). Ver [getting started with sphinx](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html#getting-started-with-sphinx). Para R se tiene [roxygen2](https://github.com/r-lib/roxygen2), [pkgdown](https://github.com/r-lib/pkgdown).

* Botón de [binder](https://mybinder.org/) para que desde este repo se pueda probar el paquete.

* *Dockerfile* e imagen de docker que instale todo el *software* necesario para que funcione su paquete y también tenga instalado su paquete. La imagen de docker debe estar alojada en su cuenta de *dockerhub*.

* *Tests* que muestren que su método numérico resuelve dos ejemplos de pequeña escala de problemas de optimización.

La imagen de docker debe construirse y alojarse (*build & push*) **automáticamente** en *dockerhub* con un lanzamiento de un *workflow* de github vía *github actions*. Consultar las  referencias para esto. Entonces colocan su *Dockerfile* en su repo. Cualquier *commit* que modifique su *Dockerfile* esto lanza un *worfklow* de github que hace un *build & push* a su *dockerhub* de manera automática.

Los *tests* deben pasarse **automáticamente** con un lanzamiento de un *workflow* de github vía *github actions*. El propósito de los *tests* es revisar que su método numérico resuelve correctamente dos problemas de optimización convexa.

## Lenguaje de programación

Python

## Fecha de entrega

Viernes 26/mar/2021 11:59pm

## Notas

* **Para la entrega crear un archivo con nombre:** `reporte_equipo_1_parte_2_practica_1.ipynb`
* Adjuntar screenshots en un directorio del repo para mostrar el uso de AWS. Debe aparecer en el screenshot nombre, clave única u otra forma de identificar el trabajo.

## Entregables

Para probar nuestro paquete, puedes hacer click en el siguiente botón

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/optimizacion-2-2021-1-gh-classroom/practica-1-segunda-parte-caroacostatovany/main?urlpath=lab)


## Referencias

* [build-push-action](https://github.com/docker/build-push-action)
* [publishing-images-to-docker-hub](https://docs.github.com/en/free-pro-team@latest/actions/guides/publishing-docker-images#publishing-images-to-docker-hub)
* [creating-encrypted-secrets-for-an-organization](https://docs.github.com/en/free-pro-team@latest/actions/reference/encrypted-secrets#creating-encrypted-secrets-for-an-organization)
* [example-docker-image-build-and-push](https://github.com/palmoreck/example-docker-image-build-and-push/blob/main/README.md)
* [JE Beasley: Ejemplos PLs 1](http://people.brunel.ac.uk/~mastjjb/jeb/or/morelp.html), [JE Beasley: Ejemplos PLs 2](http://people.brunel.ac.uk/~mastjjb/jeb/or/lpmore.html), [JE Beasley: or library](http://people.brunel.ac.uk/~mastjjb/jeb/info.html)
* [Introducción a la IDO](https://dudasytareas.files.wordpress.com/2017/05/hillier_lieberman.pdf)
* [workflow-syntax-for-github-actions](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)
* [github-actions](https://github.com/features/actions)
