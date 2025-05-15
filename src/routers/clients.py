"""
Endpoints for clients
"""

from fastapi import APIRouter, Depends, Body

from src.domain.clients import ClientDomain, LoginDomain
from src.models.clients.client import ClientRequestModel


router = APIRouter()


@router.post("/login")
def login_client(
    password: str = Body(..., description="Client password", embed=True),
    email: str = Body(..., description="Client email", embed=True),
    domain: LoginDomain = Depends(LoginDomain),
):
    """
    Get user tokens
    """
    return domain.login(email, password)


@router.post("")
def create_client(
    requested_client: ClientRequestModel,
    client: ClientDomain = Depends(ClientDomain),
) -> str:
    """
    Create client

    Notes:
        Email must be unique
    """
    return client.create_client(requested_client)
