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
    """Redirects url based on short link.

    :param slug: [description]
    :type slug: [type]
    """

    decoder = UrlEncoder(salt=current_app.config.get('ENCODER_SALT'))

    url_id = decoder.decode(slug)

    slug_link = Link.query.filter_by(id=url_id).first()

    return redirect(slug_link.url)
