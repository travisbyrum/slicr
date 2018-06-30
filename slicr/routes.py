# -*- coding: utf-8 -*-

"""
slicr.routes
~~~~~~~~~~~~
Default application routing.

:copyright: © 2018
"""

from flask import Blueprint, redirect, current_app

from slicr.encoder import UrlEncoder
from slicr.models import Link


default_blueprint = Blueprint('default_blueprint', __name__)


@default_blueprint.route('/<string:slug>')
def redirect_from_slug(slug):
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

    url_id = decoder.decode(slug)

    slug_link = Link.query.filter_by(id=url_id).first()

    return redirect(slug_link.url)
