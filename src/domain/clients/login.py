"""
Modules with login
"""

from fastapi import Depends, status
from fastapi.exceptions import HTTPException

from src.repositories.clients import ClientRepository
from src.models.clients import ClientTokensModel
from src.utils.security import hash_password, generate_jwt_token


class LoginDomain:
    """
    Login domain
    """

    def __init__(self, client_repository: ClientRepository = Depends(ClientRepository)):
        self.client_repository = client_repository

    def login(self, email: str, password: str) -> ClientTokensModel:
        """
        Login with email and password

        Args:
            email (str): Email of client
            password: (str): Password of client
        """

        # Get client by email
        client = self.client_repository.get_client_by_email(email)

        if not client:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email ou senha incorretos.",
            )

        if client.password != hash_password(password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email ou senha incorretos.",
            )

        return ClientTokensModel(
            access_token=generate_jwt_token(
                user_id=client.id,
                user_name=client.name,
                expiration_time_minutes=60,
            ),
            refresh_token=generate_jwt_token(
                user_id=client.id,
                user_name=client.name,
                expiration_time_minutes=1440,
            )
        )
