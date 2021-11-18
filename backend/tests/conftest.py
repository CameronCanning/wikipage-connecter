
from wikipageconnecter import create_app
import pytest


@pytest.fixture
def client():
    app = create_app({'TESTING': True})

    with app.test_client() as client:
        yield client

