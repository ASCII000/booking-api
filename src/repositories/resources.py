"""
Module for resource repository
"""

from typing import List, Optional, Sequence

from fastapi import Depends

from sqlmodel import Session, select

from src.database.tables import Resource
from src.dependencies.database import get_session


class ResourceRepository:
    """
    Class for resource repository
    """

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_all_resources(self) -> Sequence[Resource]:
        """
        Get all resources
        """
        return self.session.exec(
            select(Resource)
        ).all()

    def create_resource(self, resource: Resource) -> Resource:
        """
        Create resource

        Args:
            resource: Resource

        Returns:
            Resource: Created resource
        """
        self.session.add(resource)
        self.session.flush()
        return resource

    def get_resource_by_id(self, resource_id: int) -> Optional[Resource]:
        """
        Get resource by id

        Args:
            resource_id: int

        Returns:
            Optional[Resource]: Resource if exists else None
        """
        return self.session.exec(
            select(Resource).where(Resource.id == resource_id)
        ).first()

    def get_resource_by_name(self, resource_name: str) -> Optional[Resource]:
        """
        Get resource by name

        Args:
            resource_name: str

        Returns:
            Optional[Resource]: Resource if exists else None
        """
        return self.session.exec(
            select(Resource).where(Resource.name == resource_name)
        ).first()

    def edit_resource(self, resource: Resource) -> Optional[Resource]:
        """
        Edit resource

        Args:
            resource: Resource
        """
        self.session.add(resource)
        return self.get_resource_by_id(resource.id)
