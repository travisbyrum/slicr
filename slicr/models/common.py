# -*- coding: utf-8 -*-

"""
slicr.models.common
~~~~~~~~~~~~~~~~~~~
Api model mixins and common utilities.

:copyright: © 2018
"""

from datetime import datetime

from slicr.extensions import db


column = db.Column
relationship = db.relationship


class CrudMixin:
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


class TimestampMixin:
    """Includes datetime columns for updating and creation."""

    created = column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = column(db.DateTime, onupdate=datetime.utcnow)


class Model(CrudMixin, PkMixin, TimestampMixin, db.Model):
    """Default model including convenience mixins."""

    __abstract__ = True
