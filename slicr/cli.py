# -*- coding: utf-8 -*-

"""
slicr.cli
~~~~~~~~~
Command line utility for application tasks.

:copyright: © 2018
"""

import click
from flask.cli import FlaskGroup

from slicr import create_app


@click.group(cls=FlaskGroup, create_app=create_app)
def main():
    """Slicr command line interface.\n

    This utility can be used to automate tasks associated with the slicr api.
    This includes database instantiation and cleanup.\n

    Example usage:

    $ slicr db create\n
    $ slicr --help

    """

    pass


@main.group(name='db')
def db_handler():
    """Init application, creating and dropping database."""

    pass


@db_handler.command()
def create():
    """Create database with tables."""

    from slicr.extensions import db

    click.echo('creating database...')

    db.create_all()


@db_handler.command()
def delete():
    """Delete database with tables."""

    from slicr.extensions import db

    click.echo('deleting database...')

    db.drop_all()


if __name__ == '__main__':
    main()
