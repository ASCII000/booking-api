"""
Module for resource transactions
"""

from fastapi import APIRouter


router = APIRouter()


@router.post("/rent")
async def rent_resource():
    """
    Rent resource
    """
