"""
Created May 25, 2018

@author: Travis Byrum
"""

import pytest

from slicr import create_app


@pytest.fixture
def test_app():
    """Application test fixture."""

    app = create_app()

    return app


# pylint: disable=W0621
@pytest.yield_fixture
def test_client(test_app):
    """Flask test client fixture."""

    with test_app.test_client() as client:
        yield client
