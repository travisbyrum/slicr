"""
Created June 29, 2018

@author: Travis Byrum
"""

from slicr.models import Link


def test_default_redirect(test_client, test_link):
    """Test redirect after created link."""

    test_short = test_link.short_link

    response = test_client.get('/{}'.format(test_short))

    assert response.status_code == 302
    assert '<a href="{0}">{0}</a>'.format(
        'https://www.google.com'
    ) in str(response.data)


def test_click_increment(test_client, test_link):
    """Test link click count increments after update."""

    test_short = test_link.short_link
    test_id = test_link.id

    test_client.get('/{}'.format(test_short))

    assert test_link.clicks == 1

    test_client.get('/{}'.format(test_short))

    update_link = Link.query.filter_by(id=test_id).first()

    assert update_link.clicks == 2
