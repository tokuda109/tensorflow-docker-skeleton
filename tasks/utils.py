# -*- coding: utf-8 -*-

import os

__all__ = (
    "is_gpu_server",
    "is_circleci"
)


def is_gpu_server():
    """
    """
    return os.environ.get("DOCKER_BUILD_TYPE", "CPU") == "GPU"


def is_circleci():
    """
    """
    return os.environ.get("CIRCLECI") == "true"
