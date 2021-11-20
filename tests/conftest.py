import pytest
from vintourage import app

@pytest.fixture
def app():
    app = create_app()
    return app