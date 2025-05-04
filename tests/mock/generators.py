"""
Module for generators (Mock)
"""

from faker import Faker

from src.database.tables import Resource


class Generator:
    """
    Class for generators (Mock)
    """

    def __init__(self):
        self.faker = Faker(locale="pt_BR")

    def generate_resource(self, **overrides) -> Resource:
        """
        Generate fake resource model

        Args:
            overrides (kwargs): Dictionary with overrides

        Returns:
            Resource: Fake resource
        """

        return Resource(
            id=overrides.get("id", self.faker.random_int()),
            name=overrides.get("name", self.faker.name()),
            description=overrides.get("description", self.faker.text()),
            value_per_hour=overrides.get("value_per_hour", self.faker.pydecimal()),
            active=overrides.get("active", True),
        )


# Instance of Generator
generator = Generator()
