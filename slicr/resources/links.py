# -*- coding: utf-8 -*-

"""
slicr.resources.link
~~~~~~~~~~~~~~~~~~~~
Slicr link resource.

:copyright: © 2018
"""

from flask import current_app
from flask_restful import Resource
from webargs import fields
from webargs.flaskparser import use_args

from slicr.models import Link
from slicr.utils import convert_args


link_args = {
    'url': fields.Str(required=True, location='json')
}


# pylint: disable=R0201
class LinkResource(Resource):
    """Link resource."""

    endpoints = ['/link']

    @use_args(link_args)
    def post(self, args):
        """Create shortened link.

        .. :quickref: Link collection.

        **Example request**:

        .. sourcecode:: http

            POST /links HTTP/1.1
            Host: example.com
            Accept: application/json, text/javascript

            {
                "url": "https://www.google.com"
            }

        **Example response**:

        .. sourcecode:: http

            HTTP/1.1 200 OK
            Vary: Accept
            Content-Type: text/javascript

        :jsonparam string url: url for which to create short link.
        :reqheader Accept: The response content type depends on
            :mailheader:`Accept` header
        :reqheader Authorization: Optional authentication token.
        :resheader Content-Type: this depends on :mailheader:`Accept`
            header of request
        :statuscode 200: No error
        """

        args = convert_args(args)

        link = Link(
            url=args.url,
            salt=int(current_app.config.get('ENCODER_SALT'))
        ).save()

        response_out = {
            'data': link.to_dict(),
            'url': '/link',
            'type': 'link'
        }

        return response_out, 200
