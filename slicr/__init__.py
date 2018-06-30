# -*- coding: utf-8 -*-

"""
slicr
~~~~~
Link shortener application.

:copyright: © 2018
"""

from flask import Flask

from slicr.config import TestConfig
from slicr.extensions import db
from slicr.resources import slicr_blueprint
from slicr.routes import default_blueprint


__version__ = '0.0.1'


BLUEPRINTS = [default_blueprint, slicr_blueprint]


def create_app(config=TestConfig, **kwargs):
    """Application factory.

    :param config: Application configuration object, defaults to TestConfig
    :type config: slicr.config, optional
    :return: Slicr application.
    :rtype: flask.app.Flask
    """

    app = Flask(__name__)
    app.config.from_object(config)

    for name, value in kwargs.items():
        setattr(app, name, value)

    db.init_app(app)

    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)

    return app
