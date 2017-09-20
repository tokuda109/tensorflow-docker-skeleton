# -*- coding: utf-8 -*-

from flask import (
    Flask,
    render_template
)

from app.config import Config

__all__ = (
    "create_app",
)


def create_app():
    app = Flask(
        __name__,
        template_folder="../templates"
    )

    app.config.from_object(Config())

    @app.route("/", methods=["GET"])
    def index():
        ctx = {
        }

        return render_template("index.html", **ctx)

    return app
