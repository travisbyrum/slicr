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
    """Mixin object to add methods for saving, deleting, and updating
    objects."""

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


class Model(CrudMixin, db.Model):
    """Base model class that includes CRUD convenience methods."""

    __abstract__ = True


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
    """Update time."""

    created = column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = column(db.DateTime, onupdate=datetime.utcnow)


class Link(PkMixin, TimestampMixin, Model):
    """Links resource schema."""

    __tablename__ = 'links'

    url = column(db.String(80))
    salt = column(db.Integer, nullable=False)

    @hybrid_property
    def slug(self):
        """Note can only be called after flush."""

        encoder = UrlEncoder(salt=self.salt)

        return encoder.encode(self.id)

    def to_dict(self):
        dictionary_out = super().to_dict()

        dictionary_out.update({'slug': self.slug})

        return dictionary_out

    def __repr__(self):
        return '<link: {}>'.format(self.id)


class Domain(PkMixin, TimestampMixin, Model):
    """Domain resource schema."""

    __tablename__ = 'domains'

    user_id = column(db.Integer, nullable=False)
    name = column(db.String(120), nullable=False)

    def __repr__(self):
        return '<domain: {}>'.format(self.name)
