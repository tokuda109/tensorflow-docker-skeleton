# -*- coding: utf-8 -*-

from fabric.api import local, task

__all__ = (
    "lint",
)


@task
def lint():
    """
    """
    local("flake8 src")
