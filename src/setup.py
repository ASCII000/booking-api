# pylint: disable=invalid-name, too-few-public-methods

"""
Module for API configuration
"""
from dotenv import dotenv_values


class Config:
    """Configuration class for the API"""

    def __init__(self):

        # Load environment variables from .env file
        self.config = dotenv_values(".env")

        # API configuration
        self.API_ORIGINS = self.config.get("API_ORIGINS", "*").split(",")
        self.API_PORT = int(self.config.get("API_PORT", 8000))
        self.API_HOST = self.config.get("API_HOST", "0.0.0.0")
        self.API_TITLE = self.config.get("API_TITLE", "API Booking")


# Create an instance of the Config class
config = Config()
