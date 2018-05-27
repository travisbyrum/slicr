# -*- coding: utf-8 -*-

"""
slicr
~~~~~
Link shortener application.

:copyright: © 2018
"""

from flask import Flask

from slicr.config import TestConfig
from slicr.routes import links_blueprint


__version__ = '0.0.1'


BLUEPRINTS = [links_blueprint]


def create_app(config=TestConfig, **kwargs):
    """Application factory."""

    app = Flask(__name__)
    app.config.from_object(config)

    for name, value in kwargs.items():
        setattr(app, name, value)

    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)

    return app
