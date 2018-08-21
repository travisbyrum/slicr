"""
Created June 29, 2018

@author: Travis Byrum
"""

import json


# pylint: disable=W0613
def test_link_post(test_client, db):
    """Test create link resource."""

    test_url = 'https://www.google.com'

    response = test_client.post(
        '/links',
        data=json.dumps({'url': test_url}),
        content_type='application/json'
    )

    assert response.status_code == 201
    assert isinstance(response.json, dict)
    assert response.json.get('data').get('url') == test_url
    assert response.json.get('data').get('clicks') == 0


def test_link_get(test_client, test_link):
    """Test get link resource."""

    test_url = 'https://www.google.com'

    response = test_client.get(
        '/links/{}'.format(test_link.id),
        content_type='application/json'
    )

    assert response.status_code == 200
    assert response.json.get('id') == test_link.id
    assert response.json.get('data').get('url') == test_url
    assert response.json.get('data').get('clicks') == 0
