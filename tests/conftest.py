"""
Created May 25, 2018

@author: Travis Byrum
"""

import os

from click.testing import CliRunner
import pytest

from slicr import create_app
from slicr.config import Config
from slicr.models import db as test_db


class CustomTestConfig(Config):
    """Testing configuration."""

    JSONIFY_PRETTYPRINT_REGULAR = True
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'SQLALCHEMY_DATABASE_URI',
        'sqlite://'
    )
    WTF_CRSF_ENABLED = False


@pytest.fixture
def runner():
    """Click command line testing runner."""

    return CliRunner()


@pytest.fixture
def test_app():
    """Application test fixture."""

    app = create_app(config=CustomTestConfig)

    return app


# pylint: disable=W0621
@pytest.yield_fixture
def test_client(test_app):
    """Flask test client fixture."""

    with test_app.test_client() as client:
        yield client


# pylint: disable=C0103
@pytest.fixture
def db(test_app):
    """Database fixture for testing."""

    test_db.app = test_app

    with test_app.app_context():
        test_db.create_all()

    yield test_db

    test_db.session.close()
    test_db.drop_all()
