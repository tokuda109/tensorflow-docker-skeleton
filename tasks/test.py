# -*- coding: utf-8 -*-

import os
import sys

from docker import from_env
from fabric.api import local, task

from decorators import (
    machine_client,
    docker_client
)
from develop import run

__all__ = (
    "test",
)


@task
@machine_client
@docker_client
def test(machine, docker):
    """
    """
    run(cmd="python3 ./src/train/test.py")
