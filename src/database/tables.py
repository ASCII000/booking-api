"""
Models for tables of system
"""

from decimal import Decimal
from datetime import datetime

from sqlmodel import SQLModel, Field
from sqlmodel import DECIMAL, Column


class Resource(SQLModel, table=True):
    """Resource table"""

    id: int = Field(default=None, primary_key=True)
    name: str
    description: str
    image: str
    value_per_hour: Decimal = Field(sa_column=Column(DECIMAL(10, 2)))
    active: bool = True


class Client(SQLModel, table=True):
    """Client table"""

    id: int = Field(default=None, primary_key=True)
    name: str = Field(..., unique=False)
    balance: Decimal = Field(sa_column=Column(DECIMAL(10, 2)), default=Decimal(0))
    email: str = Field(..., unique=True, nullable=False)
    password: str = Field(..., nullable=False)
    created_at: datetime = Field(default_factory=datetime.now)


class ClientResource(SQLModel, table=True):
    """ClientResource table"""

    id: int = Field(default=None, primary_key=True)
    client_id: int = Field(..., foreign_key="client.id")
    resource_id: int = Field(..., foreign_key="resource.id")
    created_at: datetime = Field(default_factory=datetime.now)
