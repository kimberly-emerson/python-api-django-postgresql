"""
tba
"""

from typing import List
import pytest
from faker import Faker

from api.people.models.country_region_model import CountryRegion
from api.sales.models.sales_territory_model import SalesTerritory
from api.utils.values_handler import generate_continent, generate_territory
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

    def create_sales_territories(self, number) -> List[SalesTerritory]:
        """
        tba
        """
        instance = {}
        for _ in range(number):
            instance = self.create_sales_territory()
        return instance

    def create_sales_territory(self) -> SalesTerritory:
        """
        tba
        """
        mock = self.mock_sales_territory()

        country_region, _ = CountryRegion.objects.get_or_create(
            country_region_code=mock['country_region_code'],
            defaults={'name': mock['country_region_name']}
        )

        mock['country_region'] = country_region

        instance = SalesTerritory.objects.create(
            name=mock['name'],
            country_region=mock['country_region'],
            region=mock['region'],
            sales_ytd=mock['sales_ytd'],
            sales_last_year=mock['sales_last_year'],
            cost_ytd=mock['cost_ytd'],
            cost_last_year=mock['cost_last_year']
        )
        print(MODEL, "FACTORY CREATE QUERY: sales_territory_id: ",
              instance.sales_territory_id)

        # instance = {}
        if not instance:
            print("SalesTerritory was not created.")

        return instance

    def mock_sales_territory(self) -> dict:
        """
        tba
        """
        # create country region object
        country_region = self.country_region_factory.create_country_region()
        print(MODEL, "MOCK CREATE REGION: ", country_region)

        # get unique values
        names = self.get_unique_sales_territory_names()
        name = self.generate_sales_territory(names, 100)

        # mock sales territory object
        faker = Faker()
        mock = {
            'name': name,
            'country_region_code': country_region['country_region_code'],
            'country_region_name': country_region['name'],
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
        print(MODEL, "MOCK SALES TERRITORY: ", mock)
        return mock

    def get_unique_sales_territory_names(self):
        """
        tba
        """
        # get existing values
        data = SalesTerritory.objects.all()
        names = data.values_list('name', flat=True)

        return names

    def generate_sales_territory(self, names: dict, number: int) -> str:
        """
        tba
        """
        for _ in range(number):
            name = generate_territory()
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
