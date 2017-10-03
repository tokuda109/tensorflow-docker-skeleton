# -*- coding: utf-8 -*-

from os.path import sep
from subprocess import Popen, PIPE
import sys

from fabric.api import local
from fabric.colors import blue, cyan

from utils import which

__all__ = (
    "AnonymousCommand",
    "BasicCommand"
)


class BaseCommand(object):

    command = None

    def run(self, args=None, show_stream=False):
        raise NotImplementedError()


class AnonymousCommand(BaseCommand):

    def run(self, args=None, show_stream=False):
        pass

    def __repr__(self):
        return "<AnonymousCommand {}>".format(
            self.command
        )


class BasicCommand(BaseCommand):

    def __init__(self, command=None):
        """
        """
        full_path = which(command)

        if full_path is None:
            raise RuntimeError("Command not found.")

        self.command = full_path

    def run(self, args=None, show_stream=False):
        """
        :param args:
        :param show_stream:
        """
        if isinstance(args, str):
            _args = args.split(" ")
            _cmd = [self.command] + _args
        elif isinstance(args, list):
            _args = args
            _cmd = [self.command] + _args
        else:
            raise RuntimeError("")

        print "{}: {}".format(
            blue("[{}]".format("/".join(self.command.split(sep)[1:-1])), bold=True),
            cyan(" ".join([self.command.split(sep)[-1]] + _args))
        )

        if show_stream:
            p = Popen(_cmd, stdout=PIPE, bufsize=1)

            with p.stdout:
                for line in iter(p.stdout.readline, ""):
                    sys.stdout.write(line)

            return p.stdout, p.stderr, p.returncode
        else:
            p = Popen(_cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)

            stdout, stderr = p.communicate()
            exit_code = p.wait()

            return stdout.decode("utf-8"), stderr.decode("utf-8"), exit_code

    def __repr__(self):
        return "<BasicCommand {}>".format(
            self.command
        )
