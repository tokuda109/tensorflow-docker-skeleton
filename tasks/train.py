# -*- coding: utf-8 -*-

import os
import sys
import zipfile

from docker import from_env
from fabric.api import local, task

from config import config
from decorators import (
    machine_client,
    docker_client,
    gcp_client
)
from utils import is_gpu_server

__all__ = (
    "download_dataset",
    "train",
)


@task
@gcp_client
def download_dataset(gcp):
    bucket = gcp.client.bucket(config.get("bucket_name"))

    blob_path = "/".join([
        "datasets",
        "{}.zip".format(config.get("project_code"))
    ])

    blob = bucket.blob(blob_path)

    zipfile_path = os.path.join(config.get("tmp_path"), "dataset.zip")
    has_zipfile = os.path.exists(zipfile_path)

    if has_zipfile:
        os.remove(zipfile_path)

    if blob.exists():
        with open(zipfile_path, "wb") as file:
            blob.download_to_file(file)

        with zipfile.ZipFile(zipfile_path, "r") as zip:
            zip.extractall(os.path.join(
                config.get("tmp_path"),
                "dataset"
            ))


@task
@machine_client
@docker_client
def clear_tensorboard(machine, docker):
    """
    """
    _args = ["rm", "-rf", "/root/tmp/tensorboard"]

    docker.run_or_exec(_args)


@task
@machine_client
@docker_client
def train(machine,
          docker,
          max_steps=10000,
          num_gpus=0,
          learning_rate=None):
    """
    """
    _args = ["python3"]

    _args.append("./src/train/main.py")
    _args.append("--max_steps={}".format(max_steps))

    if is_gpu_server():
        if num_gpus is 0:
            _args.append("--num_gpus=1")
        else:
            _args.append("--num_gpus={}".format(num_gpus))
    else:
        _args.append("--num_gpus=0")

    if learning_rate is not None:
        _args.append("--learning_rate=" + learning_rate)

    docker.run_or_exec(_args)
