"""
"""

from typing import List
import pytest
from django.forms.models import model_to_dict
from faker import Faker

from api.people.models.address_type_model import AddressType


class AddressTypeFactory:
    """
    """

    def create_address_types(self, number: int):
        """
        """
        instance = {}
        for _ in range(number):
            instance = self.create_address_type()
        return instance

    def create_address_type(self):
        """
        """
        mock = self.mock_address_type()

        query = AddressType.objects.create(**mock)

        # pylint: disable=protected-access
        field_names = [field.name for field in query._meta.fields]
        instance = model_to_dict(query, fields=field_names)

        if instance:
            print("Address_Type(name=%s) created successfully.",
                  instance['name'])
            return instance
        else:
            print("Address_Type was not created.")
            return instance

    def mock_address_type(self) -> dict:
        """
        """
        names = self.get_unique_address_type_values()
        name = self.generate_address_type_name(names, 100)
        return {'name': name}

    def get_unique_address_type_values(self) -> List[str]:
        """
        """
        data = AddressType.objects.all()
        names = data.values_list('name', flat=True)
        return [names]

    def generate_address_type_name(
        self,
        names: List[str],
        number: int = 100
    ) -> str:
        """
        """
        faker = Faker()
        for _ in range(number):
            name = faker.country()
            if name not in names:
                return name
        raise ValueError("Could not find a unique country name")


@pytest.fixture
def address_type_factory():
    """
    """
    return AddressTypeFactory()
