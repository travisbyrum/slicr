# -*- coding: utf-8 -*-

"""
slicr.resources
~~~~~~~~~~~~~~~
Api resource definitions.

:copyright: © 2018
"""

from flask_restful import Resource


# pylint: disable=R0201
class LinkResource(Resource):
    """Url short link resource."""

    endpoints = ['/link']

    def get(self):
        """GET links."""

        pass


# pylint: disable=R0201
class PingResource(Resource):
    """Ping pong response resource."""

    endpoints = ['/ping']

    def get(self):
        """Ping response."""

        return {'message': 'pong'}, 200
