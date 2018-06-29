# -*- coding: utf-8 -*-

"""
slicr
~~~~~
Slicr api resources and route definitions.

:copyright: © 2018
"""

from flask import Blueprint, jsonify, make_response

from slicr.common import SlicrApi

from .links import LinkResource
from .ping import PingResource


slicr_blueprint = Blueprint('slicr_blueprint', __name__)
slicr_api = SlicrApi(slicr_blueprint)


SLICR_RESOURCES = [LinkResource, PingResource]


@slicr_api.representation('application/json')
def output_json(data, status_code, headers=None):
    """Slicr json api representation using the flask serializer instead of the
    default provided through flask_restless.

    :param data: Request data to serialize.
    :type data: dict
    :param status_code: Http status code.
    :type status_code: int
    :param headers: Headers to be sent in response, defaults to None.
    :param headers: dict, optional
    :return: Json serialized output.
    :rtype: flask.Response
    """

    headers = headers or {}

    response = make_response(jsonify(data), status_code)
    response.headers.extend(headers)

    return response


for resource in SLICR_RESOURCES:
    slicr_api.add_resource(resource, *resource.endpoints)


__all__ = ['slicr_blueprint']
