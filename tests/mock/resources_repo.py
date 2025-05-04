# pylint: disable=unused-argument

"""
Module for resource repository
"""

from typing import List, Optional

from tests import constants
from src.database.tables import Resource
from .generators import generator


class MockResourceRepository:
    """
    Class for resource repository
    """

    def get_all_resources(self) -> List[Resource]:
        """
        Get all resources
        """
        return [generator.generate_resource() for _ in range(10)]

    def create_resource(self, resource: Resource) -> Resource:
        """
        Create resource

        Args:
            resource: Resource

        Returns:
            Resource: Created resource
        """
        return generator.generate_resource()

    def get_resource_by_id(self, resource_id: int) -> Optional[Resource]:
        """
        Get resource by id

        Args:
            resource_id: int

        Returns:
            Optional[Resource]: Resource if exists else None
        """
        return generator.generate_resource(id=resource_id)

    def get_resource_by_name(self, resource_name: str) -> Optional[Resource]:
        """
        Get resource by name

        Args:
            resource_name: str

        Returns:
            Optional[Resource]: Resource if exists else None
        """

        # Ensure a name is valid for the creation, because a name is unique
        if resource_name == constants.RESOURCE_NAME_DONT_EXIST:
            return None

        return generator.generate_resource(name=resource_name)
