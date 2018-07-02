"""
Created June 29, 2018

@author: Travis Byrum
"""


from slicr.models import Link


def _add_link(db):
    test_url = 'https://www.google.com'

    test_link = Link(
        url=test_url,
        salt=0
    )

    db.session.add(test_link)
    db.session.commit()

    return test_link


# pylint: disable=W0613
def test_default_redirect(test_client, db):
    """Test redirect after created link."""

    test_link = _add_link(db)

    test_slug = test_link.slug

    response = test_client.get('/{}'.format(test_slug))

    assert response.status_code == 302
    assert '<a href="{0}">{0}</a>'.format(
        'https://www.google.com'
    ) in str(response.data)


def test_click_increment(test_client, db):
    """Test link click count increments after update."""

    test_link = _add_link(db)

    test_slug = test_link.slug
    test_id = test_link.id

    test_client.get('/{}'.format(test_slug))

    assert test_link.clicks == 1

    test_client.get('/{}'.format(test_slug))

    update_link = Link.query.filter_by(id=test_id).first()

    assert update_link.clicks == 2
