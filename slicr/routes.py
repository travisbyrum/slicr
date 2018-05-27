# -*- coding: utf-8 -*-

"""
slicr.routes
~~~~~~~~~~~~
Application routing and controllers.

:copyright: © 2018
"""

from flask import Blueprint
from flask_restful import Api

from slicr.resources import LinkResource, PingResource


links_blueprint = Blueprint('link_blueprint', __name__)
links_api = Api(links_blueprint)


SLICR_RESOURCES = [LinkResource, PingResource]


for resource in SLICR_RESOURCES:
    links_api.add_resource(resource, *resource.endpoints)


__all__ = ['links_blueprint']
