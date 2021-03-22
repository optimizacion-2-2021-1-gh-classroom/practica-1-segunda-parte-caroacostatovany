#see: https://setuptools.readthedocs.io/en/latest/userguide/package_discovery.html
from setuptools import setup, find_packages

setup(name="mex",
      version="0.1",
      description=u"Paquete que resuelve metodo simplex",
      url="",
      author="itam",
      author_email="",
      license="MIT",
      packages=find_packages(),
      install_requires = [
                          "numpy",
                          "pandas",
                          "nose"
                          ],
      )