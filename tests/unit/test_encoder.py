"""
Created June 25, 2018

@author: Travis Byrum
"""

import pytest

from slicr.encoder import UrlEncoder


@pytest.mark.parametrize('test_id', range(1, 1000, 10))
def test_create_short_url(test_id):
    """Test short url encoding from ids."""

    test_encoder = UrlEncoder()

    short_url = test_encoder.encode(test_id)

    assert test_encoder.decode(short_url) == test_id


@pytest.mark.parametrize('test_id', range(1, 1000, 10))
@pytest.mark.parametrize('test_salt', [10, 100])
def test_create_short_url_with_salt(test_id, test_salt):
    """Test short url encoding with salt value."""

    test_encoder = UrlEncoder(salt=test_salt)

    short_url = test_encoder.encode(test_id)

    assert test_encoder.decode(short_url) == test_id


def test_encode_with_zero():
    """Test raise error on encoding zero id."""

    test_encoder = UrlEncoder()

    with pytest.raises(ValueError):
        test_encoder.encode(0)
