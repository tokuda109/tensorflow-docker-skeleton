# -*- coding: utf-8 -*-

import os

__all__ = (
    "config",
)


# ==========================================================
# Project code
# ==========================================================

PROJECT_CODE = u"tensorflow-docker-skeleton"

# ==========================================================
# Port settings
# ==========================================================

TENSORBOARD_PORT = 6006
WEBSERVER_PORT = 8080
JUPYTER_PORT = 8888

# ==========================================================
# Cloud Storage settings
# ==========================================================

BUCKET_NAME = ""

# ==========================================================
# Docker Hub
# ==========================================================

DOCKER_USERNAME = ""

# ==========================================================
# End of configurable settings. Do not edit below this line.
# ==========================================================

current_path = os.path.abspath(os.path.dirname(__file__))

config = {
    "project_code": PROJECT_CODE,
    "machine_name": PROJECT_CODE,
    "base_path": os.path.abspath(os.path.join(current_path, '..')),
    "source_path": os.path.abspath(os.path.join(current_path, '../src')),
    "tasks_path": current_path,
    "tests_path": os.path.abspath(os.path.join(current_path, '../tests')),
    "tmp_path": os.path.abspath(os.path.join(current_path, '../tmp')),
    "tag": "{}/{}".format(DOCKER_USERNAME, PROJECT_CODE),
    "bucket_name": BUCKET_NAME,
    "tensorboard_port": TENSORBOARD_PORT,
    "jupyter_port": JUPYTER_PORT,
    "webserver_port": WEBSERVER_PORT
}
