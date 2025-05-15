"""
Module for functions for security
"""

from datetime import datetime, timezone, timedelta

import hashlib

import jwt


def hash_password(password: str) -> str:
    """
    Hash password

    Args:
        password: str

    Returns:
        str: Hashed password
    """
    return hashlib.sha256(password.encode()).hexdigest()

def generate_jwt_token(
    user_id: int,
    user_name: str,
    expiration_time_minutes: int,
) -> str:
    """
    Generate JWT token

    Args:
        user_id: int

    Returns:
        str: JWT token
    """

    exp_time = datetime.now(timezone.utc) + timedelta(minutes=expiration_time_minutes)
    exp_time = int(exp_time.timestamp())

    payload = {
        "user_id": user_id,
        "user_name": user_name,
        "exp": exp_time
    }

    return jwt.encode(payload, "secret", algorithm="HS256")
