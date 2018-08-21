# -*- coding: utf-8 -*-

"""
slicr.resources.domains
~~~~~~~~~~~~~~~~~~~~~~~
Slicr link resource.

:copyright: © 2018
"""

from flask import current_app
from flask_restful import Resource
from webargs import fields
from webargs.flaskparser import use_args

from slicr.models import Domain, DomainSchema
from slicr.utils import convert_args


domain_args = {
    'name': fields.Str(),
    'domain': fields.Str(required=True),
    'tag': fields.Str()
}


# pylint: disable=R0201
class DomainResource(Resource):
    """Domain resource."""

    endpoints = ['/domains', '/domains/<int:domain_id>']
    schema = DomainSchema()

    def get(self, domain_id):
        """Get domain resource.

        .. :quickref: Domain collection.

        **Example request**:

        .. sourcecode:: http

            GET /domains/1 HTTP/1.1
            Host: example.com
            Accept: application/json, text/javascript

            {
                "name": "custom_domain",
                "domain": "test.com",
                "tag": "test"
            }

        **Example response**:

        .. sourcecode:: http

            HTTP/1.1 201 OK
            Vary: Accept
            Content-Type: text/javascript

            {
                "data": {
                    "created": "2018-08-21T19:53:53.581148+00:00",
                    "domain": "test.com",
                    "name": "custom_domain",
                    "tag": "test",
                    "updated": null
                },
                "id": 1,
                "type": "domain",
                "url": "/domains"
            }

        :query domain_id: ID for domain resource
        :reqheader Accept: The response content type depends on
            :mailheader:`Accept` header
        :reqheader Authorization: Optional authentication token.
        :resheader Content-Type: this depends on :mailheader:`Accept`
            header of request
        :statuscode 200: No error
        """

        domain = Domain.query.filter_by(id=domain_id).first()

        domain_data, errors = self.schema.dump(domain)

        if errors:
            current_app.logger.warning(errors)

        response_out = {
            'id': domain.id,
            'data': domain_data,
            'url': '/links',
            'type': 'link'
        }

        return response_out, 200

    @use_args(domain_args)
    def post(self, args):
        """Create link domain.

        .. :quickref: Domain collection.

        **Example request**:

        .. sourcecode:: http

            POST /domains HTTP/1.1
            Host: example.com
            Accept: application/json, text/javascript

            {
                "name": "custom_domain",
                "domain": "test.com",
                "tag": "test"
            }

        **Example response**:

        .. sourcecode:: http

            HTTP/1.1 201 OK
            Vary: Accept
            Content-Type: text/javascript

            {
                "data": {
                    "created": "2018-08-21T19:53:53.581148+00:00",
                    "domain": "test.com",
                    "name": "custom_domain",
                    "tag": "test",
                    "updated": null
                },
                "id": 1,
                "type": "domain",
                "url": "/domains"
            }

        :jsonparam name: Name for domain
        :jsonparam domain: Domain address
        :jsonparam tag: Tag for domain reference
        :reqheader Accept: The response content type depends on
            :mailheader:`Accept` header
        :reqheader Authorization: Optional authentication token.
        :resheader Content-Type: this depends on :mailheader:`Accept`
            header of request
        :statuscode 200: No error
        """

        args = convert_args(args)

        domain = Domain(
            name=args.name,
            domain=args.domain,
            tag=args.tag
        ).save()

        domain_data, errors = self.schema.dump(domain)

        if errors:
            current_app.logger.warning(errors)

        response_out = {
            'id': domain.id,
            'data': domain_data,
            'url': '/domains',
            'type': 'domain'
        }

        return response_out, 201
