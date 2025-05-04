"""
Module for test resources routers
"""

from .constants import RESOURCE_NAME_DONT_EXIST


class TestGetAllResources:
    """
    Test get endpoint getting all resources
    """

    def test_get_all_resources(self, client):
        """
        Test get endpoint getting all resources
        """

        response = client.get("/v1/resources")
        assert response.status_code == 200


class TestCreateResource:
    """
    Test post endpoint creating a resource
    """

    def test_create_resource(self, client):
        """
        Test post endpoint creating a resource
        """

        payload = {
            "name": RESOURCE_NAME_DONT_EXIST,
            "description": "Test description",
            "value_per_hour": 10,
        }

        response = client.post("/v1/resources", json=payload)
        assert response.status_code == 200
