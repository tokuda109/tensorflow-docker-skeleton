# -*- coding: utf-8 -*-

import os

from app import create_app

root_path = os.path.abspath(os.path.dirname(__file__))

app = create_app(instance_path=root_path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
