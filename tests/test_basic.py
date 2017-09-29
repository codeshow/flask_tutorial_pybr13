import pytest


@pytest.mark.skip
def test_app_secret_is_set(app):
    assert 'SECRET_KEY' in app.config
