# -*- coding: utf-8 -*-

"""
slicr.models.domains
~~~~~~~~~~~~~~~~~~~~
Domain data modeling.

:copyright: © 2018
"""

from marshmallow import Schema, fields

from slicr.extensions import db
from .common import Model, column, relationship


# pylint: disable=C0103
class DomainSchema(Schema):
    """Domain schema for object serialization."""

    name = fields.Str()
    domain = fields.Str(required=True)
    created = fields.DateTime(dump_only=True)
    updated = fields.DateTime(dump_only=True)
    tag = fields.Str()


class Domain(Model):
    """Domain model."""

    __tablename__ = 'domains'

    name = column(db.String(120))
    domain = column(db.String(120), nullable=False)
    tag = column(db.String(120))
    links = relationship('Link', back_populates='domain')

    def __repr__(self):
        return '<domain {}>'.format(self.id)
