FROM ubuntu:bionic

ENV JUPYTERLAB_VERSION 3.0.0
ENV USER_BINDER jovyan
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

ENV DEB_PACKAGES="sudo nano less git python3-dev python3-pip python3-setuptools nodejs build-essential "

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive && echo "America/Mexico_City" > /etc/timezone && apt-get install -y tzdata

RUN apt-get update && apt-get install -y $DEB_PACKAGES && pip3 install --upgrade pip


RUN groupadd ${USER_BINDER}
RUN useradd ${USER_BINDER} -g ${USER_BINDER} -m -s /bin/bash
RUN echo 'jovyan ALL=(ALL:ALL) NOPASSWD:ALL' | (EDITOR='tee -a' visudo)
RUN echo 'jovyan:qwerty' | chpasswd
RUN pip3 install jupyter jupyterlab==$JUPYTERLAB_VERSION --upgrade
RUN pip3 install matplotlib
RUN pip3 install scipy
RUN pip3 install networkx
RUN pip3 install "git+https://github.com/optimizacion-2-2021-1-gh-classroom/practica-1-segunda-parte-caroacostatovany.git#egg=mex&subdirectory=src"

RUN chown -R ${USER_BINDER}:${USER_BINDER} /home/${USER_BINDER}/   
USER ${USER_BINDER}

RUN jupyter notebook --generate-config && sed -i "s/#c.NotebookApp.password = .*/c.NotebookApp.password = u'sha1:115e429a919f:21911277af52f3e7a8b59380804140d9ef3e2380'/" /home/${USER_BINDER}/.jupyter/jupyter_notebook_config.py
ENTRYPOINT ["/usr/local/bin/jupyter", "lab", "--ip=0.0.0.0", "--no-browser"]
