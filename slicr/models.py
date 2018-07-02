# -*- coding: utf-8 -*-

"""
slicr.models
~~~~~~~~~~~~
Api database models and utilities.

:copyright: © 2018
"""

from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property

from slicr.encoder import UrlEncoder
from slicr.extensions import db


column = db.Column
relationship = db.relationship


class CrudMixin(object):
    """Mixin for convenient crud methods."""

    def to_dict(self):
        """Method to convert object to dictionary for serialization."""

        return {
            col.name: getattr(self, col.name) for col in self.__table__.columns
        }

    def update(self, **kwargs):
        """Update specific fields of a record."""

        for attr, value in kwargs.items():
            setattr(self, attr, value)

        db.session.commit()

        return self

    def save(self):
        """Save the record."""

        db.session.add(self)
        db.session.commit()

        return self

    def delete(self):
        """Remove the record from the database."""

        db.session.delete(self)
        db.session.commit()

        return self


# pylint: disable=C0103
class PkMixin:
    """A mixin that adds a surrogate integer 'primary key' column named ``id``
    to any declarative-mapped class.
    """

    id = column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )


class TimestampMixin(object):
    """Includes datetime columns for updating and creation."""

    created = column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = column(db.DateTime, onupdate=datetime.utcnow)


class Model(CrudMixin, PkMixin, TimestampMixin, db.Model):
    """Default model including convenience mixins."""

    __abstract__ = True


class Link(Model):
    """Links model."""

    __tablename__ = 'links'

    url = column(db.String(80), nullable=False)
    salt = column(db.Integer, nullable=False)
    clicks = column(db.Integer, nullable=False, default=0)

    @hybrid_property
    def slug(self):
        """Link slug as encoded by the url.

        .. warning:: This property can only be called after flush."""

        encoder = UrlEncoder(salt=self.salt)

        return encoder.encode(self.id)

    def to_dict(self):
        dictionary_out = super().to_dict()

        dictionary_out.update({'slug': self.slug})

        return dictionary_out

    def __repr__(self):
        return '<link: {}>'.format(self.id)


class Domain(Model):
    """Domain model."""

    __tablename__ = 'domains'

    user_id = column(db.Integer, nullable=False)
    name = column(db.String(120), nullable=False)

    def __repr__(self):
        return '<domain: {}>'.format(self.name)
