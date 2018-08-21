"""
Created August 21, 2018

@author: Travis Byrum
"""

import json


# pylint: disable=W0613
def test_domain_post(test_client, db):
    """Test create domain resource."""

    response = test_client.post(
        '/domains',
        data=json.dumps(
            {
                'name': 'custom_domain',
                'domain': 'test.com',
                'tag': 'test'
            }
        ),
        content_type='application/json'
    )

    assert response.status_code == 201
    assert isinstance(response.json, dict)
    assert response.json.get('id') == 1
    assert response.json.get('data').get('domain') == 'test.com'


def test_link_get(test_client, test_domain):
    """Test get link resource."""

    response = test_client.get(
        '/domains/{}'.format(test_domain.id),
        content_type='application/json'
    )

    assert response.status_code == 200
    assert response.json.get('id') == test_domain.id
    assert response.json.get('data').get('domain') == test_domain.domain
