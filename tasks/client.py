# -*- coding: utf-8 -*-

import os
import sys

from docker import from_env
from docker.errors import APIError
from fabric.colors import red
from google.cloud.storage import Client
from requests import ConnectionError

from command import (
    AnonymousCommand,
    BasicCommand
)
from config import config
from messages import msg
from utils import is_gpu_server


__all__ = (
    "MachineClient",
    "DockerClient",
    "VirtualboxClient",
    "GoogleCloudStorageClient"
)


class BaseClient(object):

    def ready(self):
        raise NotImplementedError()


class MachineClient(BaseClient):

    def __init__(self):
        if os.environ.get("CIRCLECI", False):
            cmd = AnonymousCommand()
        else:
            cmd = BasicCommand("docker-machine")

        self.command = cmd
        self.cache = {}

    @property
    def is_running(self):
        stdout, _, _ = self.status()
        return stdout.rstrip() == "Running"

    @property
    def is_stopped(self):
        stdout, _, _ = self.status()
        return stdout.rstrip() == "Stopped"

    @property
    def has_host_error(self):
        _, stderr, _ = self.status()
        return "Host does not exist" in stderr

    def ready(self):
        _args = ["config", config.get("machine_name")]
        _, _, exit_code = self.command.run(_args)
        return exit_code == 0

    def create(self):
        _args = ["create", "--driver", "virtualbox", config.get("machine_name")]
        return self.command.run(_args, show_stream=True)

    def status(self):
        _args = ["status", config.get("machine_name")]
        return self.command.run(_args)

    def start(self):
        _args = ["start", config.get("machine_name")]
        return self.command.run(_args, show_stream=True)

    def stop(self):
        _args = ["stop", config.get("machine_name")]
        return self.command.run(_args, show_stream=True)

    def env(self):
        _args = ["env", config.get("machine_name")]
        return self.command.run(_args, show_stream=True)


class DockerClient(BaseClient):

    def __init__(self):
        if is_gpu_server():
            self.command = BasicCommand("nvidia-docker")
        else:
            self.command = BasicCommand("docker")

        self.client = from_env()

        try:
            self.client.ping()
        except ConnectionError:
            print red(msg.command_not_found.format("docker"))

    def ready(self):
        pass

    def build(self, dockerfile_path=None):
        if not os.path.exists(dockerfile_path):
            return

        _args = ["build"]

        _args.append("-t")
        _args.append(config.get("tag"))

        _args.append("-f")
        _args.append(dockerfile_path)

        _args.append("--build-arg")
        _args.append("jupyter_port={:04d}".format(
            config.get("jupyter_port")
        ))

        _args.append("--build-arg")
        _args.append("tensorboard_port={:04d}".format(
            config.get("tensorboard_port")
        ))

        _args.append("--build-arg")
        _args.append("webserver_port={:04d}".format(
            config.get("webserver_port")
        ))

        _args.append(".")

        self.command.run(_args, show_stream=True)

    def run_or_exec(self, args=None, daemon=False):
        container_count = len(self.client.containers.list())

        if container_count > 1 or args is None:
            sys.exit(1)

        _args = []

        is_str_args = isinstance(args, str)

        if is_str_args:
            args = filter(None, args.split(" "))

        if container_count == 0:
            _args.append("run")
        elif container_count == 1:
            _args.append("exec")

        if daemon:
            _args.append("-d")
        else:
            _args.append("-it")

        if container_count == 1:
            for c in self.client.containers.list():
                _args.append(c.id)

        _args = _args + args

        self.command.run(_args, show_stream=True)


class VirtualboxClient(BaseClient):

    def __init__(self):
        self.command = BasicCommand("VBoxManage")

    def ready(self):
        _args = ["showvminfo", config.get("machine_name")]
        _, _, exit_code = self.command.run(_args)
        return exit_code == 0

    def prepare(self):
        self.command.run("modifyvm {} --natpf1 tensorboard,tcp,127.0.0.1,{},,{}".format(
            config.get("machine_name"),
            config.get("tensorboard_port"),
            config.get("tensorboard_port")
        ), show_stream=True)

        self.command.run("modifyvm {} --natpf1 jupyter,tcp,127.0.0.1,{},,{}".format(
            config.get("machine_name"),
            config.get("jupyter_port"),
            config.get("jupyter_port")
        ), show_stream=True)

        self.command.run("modifyvm {} --natpf1 webserver,tcp,127.0.0.1,{},,{}".format(
            config.get("machine_name"),
            config.get("webserver_port"),
            config.get("webserver_port")
        ), show_stream=True)


class GoogleCloudStorageClient(BaseClient):

    def __init__(self):
        self.command = AnonymousCommand()
        self.client = self._prepare_client()

    def _prepare_client(self):
        keyfile_filename = "gcp_key_file.json"

        keyfile_path = os.path.join(
            config.get("tasks_path"),
            keyfile_filename
        )

        try:
            client = Client.from_service_account_json(keyfile_path)
        except TypeError as e:
            sys.exit(1)

        return client

    def ready(self):
        pass
