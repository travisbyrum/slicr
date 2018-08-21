"""
Created May 25, 2018

@author: Travis Byrum
"""

import os

from click.testing import CliRunner
import pytest

from slicr import create_app
from slicr.config import Config
from slicr.models import Domain, Link
from slicr.extensions import db as test_db


class CustomTestConfig(Config):
    """Testing configuration."""

    JSONIFY_PRETTYPRINT_REGULAR = True
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'TEST_SQLALCHEMY_DATABASE_URI',
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


@pytest.fixture
def test_domain(db):
    """Test domain fixture."""

    test_domain = Domain(
        name='test',
        domain='test@test.gov',
        tag='test'
    ).save()

    db.session.add(test_domain)
    db.session.commit()

    return test_domain


@pytest.fixture
def test_link(db):
    """Test link fixture."""

    test_url = 'https://www.google.com'

    test_link = Link(
        url=test_url,
        salt=0
    )

    db.session.add(test_link)
    db.session.commit()

    return test_link


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
