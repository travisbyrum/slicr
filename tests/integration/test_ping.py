"""
Created May 25, 2018

@author: Travis Byrum
"""

import json


def test_ping(test_client):
    """Test ping resource."""

    response = test_client.get('/ping')
    response_data = json.loads(response.data)

    assert response.status_code == 200
    assert isinstance(response_data, dict)
    assert response_data.get('message') == 'pong'
