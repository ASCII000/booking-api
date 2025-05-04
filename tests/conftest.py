"""
Module for creating a test client
"""

from fastapi.testclient import TestClient

import pytest

from src.main import app
from src.repositories.resources import ResourceRepository
from tests.mock.resources_repo import MockResourceRepository


@pytest.fixture()
def client() -> TestClient:
    """
    Fixture for creating a test client
    """

    # Mock resource repository
    app.dependency_overrides[ResourceRepository] = MockResourceRepository

    # Create test client
    return TestClient(app)
