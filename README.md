# TensorFlow Docker Skeleton &middot; ![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg) [![CircleCI](https://circleci.com/gh/tokuda109/tensorflow-docker-skeleton/tree/master.svg?style=svg&circle-token=47409f3138010c606f60e578b53022f8bf22ae07)](https://circleci.com/gh/tokuda109/tensorflow-docker-skeleton/tree/master)

Project skeleton and CLI tools for TensorFlow and Docker.

## Tech Stack

* Docker
* Python
* TensorFlow
* Numpy
* Scipy
* Jupyter
* Matplotlib
* Pandas

## Directory Layout

```sh
├─ docker      #:
├─ etc         #:
├─ notebooks   #:
├─ src         #:
│  ├─ server   #:
│  └─ train    #:
├─ tasks       #:
├─ tests       #:
└─ tmp         #:
```

## Getting Started

### Install dependencies

```sh
$ pip install -r requirements.txt
```

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

### Exec training program

```sh
$ fab train:max_steps=100000,num_gpus=2
```
