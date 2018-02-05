# TensorFlow Docker Skeleton &middot; ![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg) [![CircleCI](https://circleci.com/gh/tokuda109/tensorflow-docker-skeleton/tree/master.svg?style=svg&circle-token=47409f3138010c606f60e578b53022f8bf22ae07)](https://circleci.com/gh/tokuda109/tensorflow-docker-skeleton/tree/master)

Project skeleton and CLI tools for TensorFlow and Docker.

[![asciicast](https://asciinema.org/a/140327.png)](https://asciinema.org/a/140327)

## Specs

* Docker
* VirtualBox
* Python
* [CUDA](https://developer.nvidia.com/cuda-toolkit)
* [cuDNN](https://developer.nvidia.com/cudnn)
* [TensorFlow](https://www.tensorflow.org)
* [Sonnet](https://deepmind.github.io/sonnet/)
* [scikit-learn](http://scikit-learn.org)
* [Numpy](http://www.numpy.org)
* [Scipy](https://www.scipy.org)
* [Jupyter](http://jupyter.org)
* [Matplotlib](https://matplotlib.org)
* [Pandas](http://pandas.pydata.org)

## Directory Layout

```sh
├─ docker      #: contains CPU / GPU version of Dockerfile.
├─ etc         #: contains configs of process to be used in the container.
├─ notebooks   #: directory for putting .ipynb files.
├─ src         #:
│  ├─ server   #: directory for demo server.
│  └─ train    #: directory for training scripts.
├─ tasks       #: directory for task definitions.
├─ tests       #: directory for test files.
└─ tmp         #: directory for temporary files.
```

## Prerequisites

1. Install Docker following [the installation guide](https://docs.docker.com/install/) for your platform.
2. Install VirtualBox.
2. If you plan to use the GPU version, install the [drivers](https://www.nvidia.com/Download/index.aspx?lang=en-us) and [nvidia-docker](https://github.com/NVIDIA/nvidia-docker).

## Getting Started

### Install dependencies

```sh
$ pip install -r requirements.txt
```

### Prepare config file & Google Cloud Storage key file

Copy and edit `config-sample.py` to `config.py`.

```sh
$ cp ./tasks/config-sample.py ./tasks/config.py
```

And set your `PROJECT_CODE`, `BUCKET_NAME` and `DOCKER_USERNAME`.

### Prepare guest machine

```sh
$ fab up
```

### Build container

```sh
$ fab build
```

### Run container

Run webserver, jupyter notebooks server and tensorboard server.

```sh
$ fab run
```

and then connect your browser to:

* http://localhost:8888 for Jupyter Notebook
* http://localhost:6006 for TensorBoard
* http://localhost:8080 for Demo server

### Exec training program

```sh
$ fab train:max_steps=100000,num_gpus=2
```
