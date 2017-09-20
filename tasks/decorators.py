# -*- coding: utf-8 -*-

from functools import wraps
from sys import exit

from client import (
    MachineClient,
    DockerClient,
    VirtualboxClient,
    GoogleCloudStorageClient
)
from command import (
    AnonymousCommand,
    BasicCommand
)

__all__ = (
    "machine_client",
    "docker_client",
    "virtualbox_client",
    "gcp_client"
)


def machine_client(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        machineClient = MachineClient()

        kwargs["machine"] = machineClient

        return func(*args, **kwargs)
    return decorator


def docker_client(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        try:
            dockerClient = DockerClient()
        except RuntimeError:
            exit(1)

        kwargs["docker"] = dockerClient

        return func(*args, **kwargs)
    return decorator


def virtualbox_client(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        virtualboxClient = VirtualboxClient()

        kwargs["virtualbox"] = virtualboxClient

        return func(*args, **kwargs)
    return decorator


def gcp_client(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        gcpClient = GoogleCloudStorageClient()

        kwargs["gcp"] = gcpClient

        return func(*args, **kwargs)
    return decorator
