#!/usr/bin/env python

"""
Created May 25, 2018

@author: Travis Byrum
"""

import logging

from slicr import create_app
from slicr.config import Config


class ProdConfig(Config):
    """Production configuration for consumption by gunicorn."""

    ASSETS_DEBUG = True
    DEBUG = False
    TESTING = False


def wsgi():
    """Application entrypoint for gunicorn."""

    gunicorn_logger = logging.getLogger('gunicorn.errors')

    app = create_app(config=ProdConfig)

    app.logger.handlers = gunicorn_logger.handlers

    return app
