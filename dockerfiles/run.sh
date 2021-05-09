#!/bin/bash
NB_USER=jovyan
HOME=/home/${NB_USER}
cd ${HOME} && pip install matplotlib && pip install scipy && pip install networkx && git clone -b master --single-branch https://github.com/optimizacion-2-2021-1-gh-classroom/practica-1-segunda-parte-caroacostatovany.git

exec "$@"
