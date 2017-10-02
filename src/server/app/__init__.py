# -*- coding: utf-8 -*-

import os

from flask import (
    Flask,
    render_template,
    send_from_directory
)

from app.config import Config

__all__ = (
    "create_app",
)


def create_app(instance_path=None):
    app = Flask(
        __name__,
        static_folder='../public',
        static_url_path="",
        template_folder="../templates",
        instance_path=instance_path
    )

    app.config.from_object(Config())

    @app.route("/favicon.ico")
    def favicon():
        return send_from_directory(
            os.path.join(app.root_path, "../public"),
            "favicon.ico",
            mimetype="image/x-icon"
        )

    @app.route("/", methods=["GET"])
    def index():
        ctx = {
        }

        return render_template("index.html", **ctx)

    return app
