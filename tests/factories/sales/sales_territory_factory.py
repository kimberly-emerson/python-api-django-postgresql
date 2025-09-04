"""
tba
"""

import pytest
from django.forms.models import model_to_dict
from faker import Faker

from api.people.models.country_region_model import CountryRegion
from api.sales.models.sales_territory_model import SalesTerritory
from api.utils.values_handler import generate_continent
from tests.factories.people.country_region_factory import (
  CountryRegionFactory
)

MODEL = "SALES TERRITORIES"


class SalesTerritoryFactory:
    """
    tba
    """
    def __init__(self):
        self.country_region_factory = CountryRegionFactory()

    def create_sales_territories(self, number):
        """
        tba
        """
        instance = {}
        for _ in range(number):
            instance = self.create_sales_territory()
        return instance

    def create_sales_territory(self):
        """
        tba
        """
        # create object
        mock = self.mock_sales_territory()
        query = SalesTerritory.objects.create(
            name=mock['name'],
            country_region=CountryRegion(**mock['country_region']),
            region=mock['region'],
            sales_ytd=mock['sales_ytd'],
            sales_last_year=mock['sales_last_year'],
            cost_ytd=mock['cost_ytd'],
            cost_last_year=mock['cost_last_year']
        )
        print(MODEL, "FACTORY CREATE QUERY: ", query)

        instance = {}
        if query:
            # pylint: disable=protected-access
            field_names = [field.name for field in query._meta.fields]
            instance = model_to_dict(query, fields=field_names)
            return instance
        else:
            print("SalesTerritory was not created.")
            return instance

    def mock_sales_territory(self) -> dict:
        """
        tba
        """
        # create country region object
        country_region = self.country_region_factory.create_country_region()

        # get unique values
        names = self.get_unique_sales_territory_values()
        name = self.generate_sales_territory_name(names, 100)

        # mock sales territory object
        faker = Faker()
        mock = {
            'name': name,
            'country_region': country_region,
            'region': generate_continent(),
            'sales_ytd': faker.pyfloat(
                left_digits=10, right_digits=2, positive=True),
            'sales_last_year': faker.pyfloat(
                left_digits=10, right_digits=2, positive=True),
            'cost_ytd': faker.pyfloat(
                left_digits=10, right_digits=2, positive=True),
            'cost_last_year': faker.pyfloat(
                left_digits=10, right_digits=2, positive=True)
        }
        print(MODEL, "MOCK: ", mock)
        return mock

    def get_unique_sales_territory_values(self):
        """
        tba
        """
        # get existing values
        data = SalesTerritory.objects.all()
        names = data.values_list('name', flat=True)

        return names

    def generate_sales_territory_name(self, names: dict, number: int) -> str:
        """
        tba
        """
        faker = Faker()
        for _ in range(number):
            name = faker.state()
            if name not in names:
                return name
        raise ValueError("Could not find a unique sales territory name")


@pytest.fixture
def sales_territory_factory():
    """
    Fixture for injecting SalesTerritoryFactory into tests.

    Contributor Notes:
    - Enables method chaining for test setup.
    - Supports teardown via Django's test DB rollback.
    """
    return SalesTerritoryFactory()
