"""
Created June 29, 2018

@author: Travis Byrum
"""

import json


# pylint: disable=W0613
def test_link_post(test_client, db):
    """Test link resource."""

    test_url = 'https://www.google.com'

    request_payload = {'url': test_url}

    response = test_client.post(
        '/link',
        data=json.dumps(request_payload),
        content_type='application/json'
    )

    response_data = json.loads(response.data)

    assert response.status_code == 200
    assert isinstance(response_data, dict)
    assert response_data.get('data').get('url') == test_url
    assert response_data.get('url') == '/link'
    assert response_data.get('type') == 'link'
