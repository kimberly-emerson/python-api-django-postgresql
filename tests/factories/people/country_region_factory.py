"""
"""

from typing import List
import pytest
from django.forms.models import model_to_dict
from faker import Faker

from api.people.models.country_region_model import CountryRegion


class CountryRegionFactory:
    """
    """

    def create_country_regions(self, number: int):
        """
        """
        instance = {}
        for _ in range(number):
            instance = self.create_country_region()
        return instance

    def create_country_region(self):
        """
        tba
        """
        mock = self.mock_country_region()

        query = CountryRegion.objects.create(**mock)

        # pylint: disable=protected-access
        field_names = [field.name for field in query._meta.fields]
        instance = model_to_dict(query, fields=field_names)

        if instance:
            # object created
            print("SalesTerritory(name=%s) created successfully.",
                  instance['name'])
            return instance
        else:
            print("SalesTerritory was not created.")
            return instance

    def mock_country_region(self) -> dict:
        """
        tba
        """
        codes, names = self.get_unique_country_region_values()
        code = self.generate_country_region_code(codes, 100)
        name = self.generate_country_region_name(names, 100)

        instance = {
            'country_region_code': code,
            'name': name
        }
        return instance

    def get_unique_country_region_values(self):
        """
        """
        data = CountryRegion.objects.all()
        codes = data.values_list('country_region_code', flat=True)
        names = data.values_list('name', flat=True)

        return codes, names

    def generate_country_region_code(
        self,
        codes: List[str],
        number: int = 100
    ) -> str:
        """
        """
        faker = Faker()
        for _ in range(number):
            code = faker.country_code(representation="alpha-2")
            if code not in codes:
                return code
        raise ValueError("Could not find a unique country region code")

    def generate_country_region_name(
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
        raise ValueError("Could not find a unique country region name")


@pytest.fixture
def country_region_factory():
    """
    """
    return CountryRegionFactory()
