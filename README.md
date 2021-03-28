![](https://github.com/optimizacion-2-2021-1-gh-classroom/practica-1-segunda-parte-caroacostatovany/blob/main/src/docs/images/mex_simplex_logo.png) ![](https://mcdatos.itam.mx/wp-content/uploads/2020/11/ITAM-LOGO.03.jpg)
# Optimización 2 2021-1 Práctica I - 2a Parte: Implementación de método numérico para resolver problemas de optimización convexa #

## Equipo 1

| Nombre | User Github | Tarea a realizar |
|:---:|:---:|:---|
| Eduardo Moreno | Eduardo-Moreno| Programación método numérico y pruebas |
| Cecilia Avilés | cecyar| Programación método numérico y pruebas |
| Carolina Acosta | caroacostatovany| Github workflows y documentación del paquete |
| Leonardo Ceja | lecepe00| Imagen de Docker y documentación / **Project Manager** |

## Aplicando el método simplex

- En esta práctica se desarrolló un paquete de Python para resolver problemas de optimización por medio del método Simplex. 

- Nuestro paquete se llama ***`mex`***. La documentación del mismo se desarrolló con [Sphinx](https://www.sphinx-doc.org/en/master/), la puedes encontrar [aquí](https://optimizacion-2-2021-1-gh-classroom.github.io/practica-1-segunda-parte-caroacostatovany/).

- Para probar nuestro paquete puedes hacer uso del siguiente botón de binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/optimizacion-2-2021-1-gh-classroom/practica-1-segunda-parte-caroacostatovany/main?urlpath=lab). Puedes probar el Jupyter notebook [Pruebas_Resultados.ipynb](https://github.com/optimizacion-2-2021-1-gh-classroom/practica-1-segunda-parte-caroacostatovany/tree/main/notebooks), que se encuentra en el directorio `/notebooks`.

- Adicionalmente, se creó la imagen de Docker **`optimizacion-2-practica-1-parte-2`** que contiene todo lo necesario para ejecutar el paquete.

- Para el desarrollo del proyecto se levantó una instancia de AWS donde se cargó una imagen de Docker que contiene JupyterLab. La evidencia del uso de la misma se encuentra en el directorio [AWS_screenshots](https://github.com/optimizacion-2-2021-1-gh-classroom/practica-1-segunda-parte-caroacostatovany/tree/main/AWS_screenshots).

- Puedes encontrar el reporte de nuestro trabajo en el archivo [reporte_equipo_1_parte_2_practica_1](https://github.com/optimizacion-2-2021-1-gh-classroom/practica-1-segunda-parte-caroacostatovany/blob/main/reporte_equipo_1_parte_2_practica_1.ipynb), ubicado en la raíz de este repositorio.

## Fecha de entrega

Sábado 27/mar/2021 11:59pm

## Referencias

- [Build-push-action](https://github.com/docker/build-push-action)
- [Creating-encrypted-secrets-for-an-organization](https://docs.github.com/en/free-pro-team@latest/actions/reference/encrypted-secrets#creating-encrypted-secrets-for-an-organization)
- [Example-docker-image-build-and-push](https://github.com/palmoreck/example-docker-image-build-and-push/blob/main/README.md)
- [Github-actions](https://github.com/features/actions)
- Moore, Jacob.  (2018).  [Coding the Simplex Algorithm from scratch using Python and Numpy](https://medium.com/@jacob.d.moore1/coding-the-simplex-algorithm-from-scratch-using-python-and-numpy-93e3813e6e70)
- Palacios M., Erick. (2021). Libro de Optimización 2021. [4.2. Programación lineal (PL) y método símplex](https://itam-ds.github.io/analisis-numerico-computo-cientifico/IV.optimizacion_en_redes_y_prog_lineal/4.2/Programacion_lineal_y_metodo_simplex.html)
- Palacios M., Erick. (2021). Libro de Optimización 2021. [4.3. Ejemplo del método símplex de redes](https://itam-ds.github.io/analisis-numerico-computo-cientifico/IV.optimizacion_en_redes_y_prog_lineal/4.3/Ejemplo_metodo_simplex_de_redes.html) 
- Palacios M., Erick. (2021). Libro de Optimización 2021. [4.4. Dualidad, lema de Farkas y condiciones de Karush-Kuhn-Tucker (KKT) de optimalidad](https://itam-ds.github.io/analisis-numerico-computo-cientifico/IV.optimizacion_en_redes_y_prog_lineal/4.4/Dualidad_lema_de_Farkas_condiciones_KKT_de_optimalidad.html) 
- [Publishing-images-to-docker-hub](https://docs.github.com/en/free-pro-team@latest/actions/guides/publishing-docker-images#publishing-images-to-docker-hub)
- SciPy.org [scipy.optimize.linprog](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html#scipy.optimize.linprog)
- [Workflow-syntax-for-github-actions](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)