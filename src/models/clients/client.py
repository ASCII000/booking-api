# pylint: disable=no-self-argument

"""
Module for client models
"""

import re

from fastapi.exceptions import RequestValidationError

from pydantic import BaseModel, Field, field_validator


class ClientRequestModel(BaseModel):
    """
    Request model for clients
    """

    name: str = Field(..., title="Client Name")
    email: str = Field(..., title="Client Email")
    password: str = Field(..., title="Client Password")

    @field_validator("email", mode="before")
    def validate_email(cls, value: str) -> str:
        """
        Validate email

        Args:
            value: str

        Returns:
            str: Validated email
        """
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        if not re.fullmatch(regex, value):
            raise RequestValidationError(
                errors={
                    "email": "Email informado nao e valido.",
                    "regex": str(regex),
                },
            )
        return value
