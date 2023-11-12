import pytest
from api.config import TestConfig
from api.index import create_app


@pytest.fixture
def test_client():
    return create_app(TestConfig).test_client()
