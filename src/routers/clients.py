"""
Endpoints for clients
"""

from fastapi import APIRouter, Depends

from src.domain.clients.client import ClientDomain
from src.models.clients.client import ClientRequestModel


router = APIRouter()


@router.post("")
async def create_client(
    requested_client: ClientRequestModel,
    client: ClientDomain = Depends(ClientDomain),
) -> str:
    """
    Create client

    Notes:
        Email must be unique
    """
    return client.create_client(requested_client)
