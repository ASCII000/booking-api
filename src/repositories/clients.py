"""
Module for repository for clients
"""

from typing import Optional

from fastapi import Depends

from sqlmodel import Session, select

from src.database.tables import Client
from src.dependencies.database import get_session


class ClientRepository:
    """
    Repository for clients
    """

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create_client(self, client: Client) -> Client:
        """
        Create client

        Args:
            client: Client

        Returns:
            Client: Created client
        """
        self.session.add(client)
        self.session.commit()
        return client

    def get_client_by_id(self, client_id: int) -> Optional[Client]:
        """
        Get client by id

        Args:
            client_id: int

        Returns:
            Optional[Client]: Client if exists else None
        """
        return self.session.exec(select(Client).where(Client.id == client_id)).first()

    def get_client_by_email(self, client_email: str) -> Optional[Client]:
        """
        Get client by email

        Args:
            client_email: str

        Returns:
            Optional[Client]: Client if exists else None
        """
        return self.session.exec(
            select(Client).where(Client.email == client_email)
        ).first()
