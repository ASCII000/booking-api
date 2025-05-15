"""
Module for business logic for clients
"""

from fastapi import Depends, status
from fastapi.exceptions import HTTPException

from src.database.tables import Client
from src.repositories.clients import ClientRepository
from src.models.clients.client import ClientRequestModel


class ClientDomain:
    """
    Class for client business logic
    """

    def __init__(self, client_repository: ClientRepository = Depends(ClientRepository)):
        self.client_repository = client_repository

    def create_client(self, client: ClientRequestModel) -> str:
        """
        Create client

        Args:
            client: Client

        Returns:
            str: Success message
        """

        # Check if client email already in use
        if self.client_repository.get_client_by_email(client.email):

            # Raise exception
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email já em uso.",
            )

        # Create user Client
        client_model = Client(
            name=client.name,
            email=client.email,
            password=client.password,
        )

        # Create client
        self.client_repository.create_client(client_model)

        # Return success message
        return "Cliente criado com sucesso!"
