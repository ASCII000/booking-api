# pylint: disable=no-self-argument

"""
Module for client models
"""

import re
import hashlib

from fastapi.exceptions import RequestValidationError

from pydantic import BaseModel, Field, field_validator


class ClientRequestModel(BaseModel):
    """
    Request model for clients
    """

    name: str = Field(..., title="Client Name")
    email: str = Field(..., title="Client Email")
    password: str = Field(..., title="Client Password")

    @field_validator("password", mode="before")
    def validate_password(cls, value: str) -> str:
        """
        Validate password

        Args:
            value: str

        Returns:
            str: Validated password
        """

        # Verify password must be at least than 8 characters
        if re.match(r"^.{0,7}$", value):
            raise RequestValidationError(
                errors={
                    "password": "A senha deve ter no mínimo 8 caracteres.",
                },
            )

        # Verify password must be contain at least one uppercase letter
        if not re.match(r"^[A-Z]", value):
            raise RequestValidationError(
                errors={
                    "password": "A senha deve conter pelo menos uma letra maiúscula.",
                },
            )

        return hashlib.sha256(value.encode()).hexdigest()

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
