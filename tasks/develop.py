# -*- coding: utf-8 -*-

import os
import sys

from fabric.api import local, task
from fabric.colors import red

from command import BasicCommand
from config import config
from decorators import (
    machine_client,
    docker_client,
    virtualbox_client
)
from messages import msg
from utils import is_gpu_server, is_circleci

__all__ = (
    "up",
    "build",
    "run"
)


@task
@machine_client
@virtualbox_client
def up(machine, virtualbox):
    """
    Creates and configures guest machines.
    """
    if machine.is_running:
        print msg.up_already_running
    elif machine.is_stopped:
        machine.start()
        machine.env()

    if machine.has_host_error:
        machine.create()
        machine.stop()
        virtualbox.prepare()
        machine.start()
        machine.env()

    sys.exit(0)


@task
@machine_client
@docker_client
def build(machine, docker):
    """
    """
    if is_gpu_server():
        build_type = "gpu"
    else:
        build_type = "cpu"

    dockerfile_path = os.path.join(
        config.get("base_path"),
        "docker/Dockerfile.{}".format(build_type)
    )

    docker.build(dockerfile_path=dockerfile_path)


@task
@machine_client
@docker_client
def run(machine, docker, cmd=None, daemon=False):
    """
    """
    _args = ""

    if is_gpu_server():
        _args += " --device /dev/nvidia0:/dev/nvidia0"
        _args += " --device /dev/nvidiactl:/dev/nvidiactl"
        _args += " --device /dev/nvidia-uvm:/dev/nvidia-uvm"
        _args += " -v /usr/local/cuda/lib64:/usr/local/cuda/lib64"
        _args += " -v /usr/lib/x86_64-linux-gnu:/usr/lib/x86_64-linux-gnu"
        _args += " -v /usr/lib/nvidia-375/:/usr/lib/nvidia-375/"

    if not is_circleci():
        _args += " -p {:04d}:6006".format(config.get("tensorboard_port"))
        _args += " -p {:04d}:8888".format(config.get("jupyter_port"))
        _args += " -p {:04d}:8080".format(config.get("webserver_port"))

        _args += " -v {}/notebooks:/root/notebooks".format(config.get("base_path"))
        _args += " -v {}/src:/root/src".format(config.get("base_path"))
        _args += " -v {}/tmp:/root/tmp".format(config.get("base_path"))
        _args += " -v {}/tests:/root/tests".format(config.get("base_path"))

    _args += " {}".format(config.get("tag"))

    if cmd is None:
        _args += " supervisord --nodaemon"
    else:
        _args += " {}".format(cmd)

    docker.run_or_exec(_args, daemon)
