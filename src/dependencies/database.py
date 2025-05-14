"""
Module for database dependencies
"""

from typing import Generator

from sqlmodel import Session

from src.database.setup import engine


def get_session() -> Generator[Session, None, None]:
    """
    Get database session with commit/rollback management.
    """
    session = Session(engine)
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
