#!/usr/bin/env python

"""
Created May 25, 2018

@author: Travis Byrum
"""

from slicr import create_app
from slicr.config import Config


class ProdConfig(Config):
    """Production configuration for consumption by gunicorn."""

    ASSETS_DEBUG = True
    DEBUG = False
    TESTING = False


def wsgi():
    """Application entrypoint for gunicorn."""

    app = create_app(config=ProdConfig)

    return app
