"""
Module for business logic for resources
"""

from typing import List

from fastapi import Depends, status
from fastapi.exceptions import HTTPException

from src.repositories.resources import ResourceRepository, Resource
from src.models.resources.resources import (
    ResourceResponse,
    ResourceRequesModel,
    ResourceEditRequestModel,
)


class ResourceDomain:
    """
    Resource domain
    """

    def __init__(self, repository: ResourceRepository = Depends(ResourceRepository)):
        """
        Args:
            repository: ResourceRepository
        """
        self.repository = repository

    def get_all_resources(self) -> List[ResourceResponse]:
        """
        Get all resources

        Returns:
            List[Resource]: List of resources
        """

        # Get all resources
        resources = self.repository.get_all_resources()

        # Map resources to ResourceResponse
        return [
            ResourceResponse(
                id=resource.id,
                active=resource.active,
                description=resource.description,
                name=resource.name,
                value_per_hour=resource.value_per_hour,
            )
            for resource in resources
        ]

    def create_resource(self, resource: ResourceRequesModel) -> ResourceResponse:
        """
        Create resource

        Args:
            resource: ResourceRequesModel

        Returns:
            ResourceResponse: Created resource
        """

        # Check if name already exists
        if self.repository.get_resource_by_name(resource.name):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Um recurso com esse nome já existe",
            )

        # Parse request model to Resource sqlmodel
        parsed_resource = Resource(
            name=resource.name,
            description=resource.description,
            value_per_hour=resource.value_per_hour,
            image=resource.image,
        )

        # Create resource
        created_resource = self.repository.create_resource(parsed_resource)

        # Map resource to ResourceResponse
        return ResourceResponse(
            id=created_resource.id,
            active=created_resource.active,
            description=created_resource.description,
            name=created_resource.name,
            value_per_hour=created_resource.value_per_hour,
        )

    def reserve_resource(self, resource_id: int) -> str:
        """
        Reserve resource

        Args:
            resource_id: int
        """

        # Get resource by id
        resource = self.repository.get_resource_by_id(resource_id)

        # Check if resource exists
        if not resource:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Recurso não encontrado",
            )

        # Reserve resource
        self.repository.reserve_resource(resource)

        return "Alugado com sucesso"

    def edit_resource(self, resource_id: int, edit_resource: ResourceEditRequestModel):
        """
        Edit resource
        
        Args:
            resource_id (int): Resource id
            edit_resourcel (ResourceEditRequestModel): Resource edit request model
        """

        # Get resource by id
        resource = self.repository.get_resource_by_id(resource_id)

        # Check if resource exists
        if not resource:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Recurso não encontrado",
            )

        # Wrap model excludes None Fields
        edit_resource = edit_resource.model_dump(exclude_none=True)

        # Choice values in wraped model
        for key, value in edit_resource.items():
            setattr(resource, key, value)

        # Edit resource
        self.repository.edit_resource(resource)

        return "Recurso editado com sucesso"
