# -*- coding: utf-8 -*-

"""
slicr.models.links
~~~~~~~~~~~~~~~~~~
Link data modeling.

:copyright: © 2018
"""

from marshmallow import Schema, fields
from sqlalchemy.ext.hybrid import hybrid_property

from slicr.encoder import UrlEncoder
from slicr.extensions import db

from .common import Model, column, relationship


# pylint: disable=C0103
# pylint: disable=R0201
class LinkSchema(Schema):
    """Link schema for object serialization."""

    url = fields.Str(required=True)
    clicks = fields.Int(required=True)
    created = fields.DateTime(dump_only=True)
    updated = fields.DateTime(dump_only=True)
    short_link = fields.Method('_create_short_link')

    def _update_field(self, obj):
        return obj.created

    def _create_short_link(self, obj):
        """Short link as encoded by the id.

        .. warning:: This property can only be called after flush.
        """

        encoder = UrlEncoder(salt=obj.salt)

        return encoder.encode(obj.id)


class Link(Model):
    """Links model."""

    __tablename__ = 'links'

    url = column(db.String(80), nullable=False)
    salt = column(db.Integer, nullable=False)
    clicks = column(db.Integer, nullable=False, default=0)
    domain_id = column(db.Integer, db.ForeignKey('domains.id'))
    domain = relationship('Domain', back_populates='links')

    @hybrid_property
    def short_link(self):
        """Short link as encoded by the id."""

        encoder = UrlEncoder(salt=self.salt)

        return encoder.encode(self.id)

    def __repr__(self):
        return '<link {}>'.format(self.id)
