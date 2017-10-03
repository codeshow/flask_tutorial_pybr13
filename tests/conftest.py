# coding: utf-8

import pytest
from cms.app import create_app


@pytest.fixture
def app():
    """Flask Pytest uses it"""
    return create_app('cms')
