"""
Routers for resources
"""

from typing import List

from fastapi import APIRouter, Depends

from src.domain.resources.resources import ResourceDomain
from src.models.resources.resources import ResourceResponse, ResourceRequesModel


router = APIRouter()


@router.get("")
async def get_all_resources(
    domain: ResourceDomain = Depends(ResourceDomain),
) -> List[ResourceResponse]:
    """
    Get all resources
    """
    return domain.get_all_resources()


@router.post("")
async def create_resource(
    resource: ResourceRequesModel,
    domain: ResourceDomain = Depends(ResourceDomain),
) -> ResourceResponse:
    """
    Create resource
    """
    return domain.create_resource(resource)
