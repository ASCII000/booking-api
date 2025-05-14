"""
Module for resource models
"""

from typing import Optional
from decimal import Decimal

from pydantic import BaseModel, Field


class ResourceResponse(BaseModel):
    """
    Response model for resources
    """

    id: int = Field(..., title="Resource ID")
    name: str = Field(..., title="Resource Name")
    description: str = Field(..., title="Resource Description")
    value_per_hour: Decimal = Field(..., title="Resource Value Per Hour")
    active: bool = Field(..., title="Resource Active")


class ResourceRequesModel(BaseModel):
    """
    Request model for resources
    """

    name: str = Field(..., title="Resource Name")
    description: str = Field(..., title="Resource Description")
    value_per_hour: Decimal = Field(..., title="Resource Value Per Hour")


class ResourceEditRequestModel(BaseModel):
    """
    Edit request model for resources
    """
    name: Optional[str] = Field(None, title="Resource Name")
    description: Optional[str] = Field(None, title="Resource Description")
    value_per_hour: Optional[Decimal] = Field(None, title="Resource Value Per Hour")
