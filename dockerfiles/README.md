Instructions to build docker image. Set:



```
JUPYTERLAB_VERSION=2.1.4
REPO_URL=caroacostatovany/optimizacion-2-practica-1-parte-2
DIR=/home/<user>/<midir>
BUILD_DIR=${DIR}dockerfiles/pkg/
CONTAINER_NAME=optimizacion-2-practica-1-parte-2
```
*<midir> should be an empty directory

Clone:

```
git clone --single-branch -b main https://github.com/optimizacion-2-2021-1-gh-classroom/practica-1-segunda-parte-caroacostatovany.git $DIR
```

Build:

```
docker build $BUILD_DIR --force-rm -t $REPO_URL:$JUPYTERLAB_VERSION
```

Run:

```
docker run -v $(pwd):/datos --name ${CONTAINER_NAME} -p 8888:8888 -d $REPO_URL:$JUPYTERLAB_VERSION \
/usr/local/bin/jupyter lab --ip=0.0.0.0 --no-browser
```

or:

```
docker run --rm -v $(pwd):/datos --name ${CONTAINER_NAME} -p 8888:8888 -d $REPO_URL:$JUPYTERLAB_VERSION \
/usr/local/bin/jupyter lab --ip=0.0.0.0 --no-browser
```


## jupyter lab running at localhost:8888 , password: qwerty

(not necessary) Enter to docker container with:

```
docker exec -it -u=jovyan ${CONTAINER_NAME} bash
```

Stop:

```
docker stop ${CONTAINER_NAME}
```

Delete (if `--rm` wasn't used):


```
docker rm ${CONTAINER_NAME}
```


