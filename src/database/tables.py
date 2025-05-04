"""
Models for tables of system
"""

from decimal import Decimal

from sqlmodel import SQLModel, Field
from sqlmodel import DECIMAL, Column


class Resource(SQLModel, table=True):
    """Resource table"""

    id: int = Field(default=None, primary_key=True)
    name: str
    description: str
    value_per_hour: Decimal = Field(sa_column=Column(DECIMAL(10, 2)))
    active: bool = True
