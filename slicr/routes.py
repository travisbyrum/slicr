# -*- coding: utf-8 -*-

"""
slicr.routes
~~~~~~~~~~~~
Default application routing.

:copyright: © 2018
"""

from flask import Blueprint, current_app, jsonify, redirect, Response

from slicr.common import _create_error_out
from slicr.encoder import UrlEncoder
from slicr.models import Link


default_blueprint = Blueprint('default_blueprint', __name__)


@default_blueprint.errorhandler(Exception)
def handler_errors(api_exception):
    """Default error handler."""

    error_out, status_code, headers = _create_error_out(api_exception)

    return Response(jsonify(error_out), status=status_code, headers=headers)


@default_blueprint.route('/<string:short>')
def redirect_from_short(short):
    """Redirect from short link.

    .. :quickref: Link redirection.

    **Example request**:

    .. sourcecode:: http

        GET /7yupBn HTTP/1.1
        Host: example.com
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 302 OK
        Vary: Accept
        Content-Type: application/json

    :status 302: successful redirect
    """

    decoder = UrlEncoder(salt=current_app.config.get('ENCODER_SALT'))

    url_id = decoder.decode(short)

    short_link = Link.query.filter_by(id=url_id).first()

    short_link.clicks += 1
    short_link.update()

    return redirect(short_link.url)
