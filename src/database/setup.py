"""
Module for setup database connection
"""

from sqlmodel import SQLModel, create_engine


engine = create_engine("sqlite:///src/database/booking_database.db")
SQLModel.metadata.create_all(engine)
