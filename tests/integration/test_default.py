"""
Created June 29, 2018

@author: Travis Byrum
"""

from slicr.models import Link


# pylint: disable=W0613
def test_default_redirect(test_client, db):
    """Test redirect after created link."""

    test_url = 'https://www.google.com'

    test_link = Link(
        url=test_url,
        salt=0
    )

    db.session.add(test_link)
    db.session.commit()

    slug_url = test_link.slug

    response = test_client.get('/{}'.format(slug_url))

    assert response.status_code == 302

    assert '<a href="{0}">{0}</a>'.format(test_url) in str(response.data)
