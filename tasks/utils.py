# -*- coding: utf-8 -*-

import os

__all__ = (
    "is_gpu_server",
    "is_circleci",
    "which"
)


def is_gpu_server():
    """
    :return: Returns whether it is a GPU server or not.
    :rtype: boolean
    """
    return which("nvidia-docker") is not None


def is_circleci():
    """
    :return: Returns whether it is a CircleCI environment or not.
    :rtype: boolean
    """
    return "CIRCLECI" in os.environ


def which(command):
    """
    :param command:
    :type command: str
    :return: The path of program file or None
    :rtype: str
    """
    result = None

    for p in os.getenv("PATH").split(os.path.pathsep):
        full_path = os.path.join(p, command)

        if os.path.exists(full_path):
            result = full_path
            break

    return result
