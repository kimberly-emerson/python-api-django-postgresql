"""
"""

from faker import Faker
from django.forms.models import model_to_dict

from api.people.models.state_province_model import StateProvince
from api.utils.values_handler import get_boolean
from tests.factories.people.country_region_factory import (
  CountryRegionFactory
)
from tests.factories.sales.sales_territory_factory import (
  SalesTerritoryFactory
)


class StateProvinceFactory:
    """
    """
    def __init__(self):
        self.country_region_factory = CountryRegionFactory()
        self.sales_territory_factory = SalesTerritoryFactory()

    def create_state_provinces(self, number):
        """
        """
        instance = {}
        for _ in range(number):
            instance = self.create_state_province()
        return instance


    def create_state_province(self):
        """
        """
        mock = self.mock_state_province()

        query = StateProvince.objects.create(**mock)

        # pylint: disable=protected-access
        field_names = [field.name for field in query._meta.fields]
        instance = model_to_dict(query, fields=field_names)

        # create object
        if instance:
            # object created
            print("StateProvince(state_province_code=%s, name=%s)"
                  "created successfully.",
                  query.state_province_code,
                  query.name)
            return instance
        else:
            print("StateProvince was not created.")

    def mock_state_province(self) -> dict:
        """
        """
        country_region = self.country_region_factory.mock_country_region()
        sales_territory = self.sales_territory_factory.mock_sales_territory()

        # get unique values
        codes, names = self.get_unique_state_province_values()
        # set unique values
        state_province_code = self.generate_state_province_code(codes, 100)
        name = self.generate_state_province_name(names, 100)

        # build state province object
        instance = {
            'state_province_code': state_province_code,
            'is_only_state_province_flag': get_boolean(),
            'name': name,
            'country_region': country_region,
            'sales_territory': sales_territory
        }

        return instance

    def get_unique_state_province_values(self):
        """
        """
        # get existing values
        data = StateProvince.objects.all()
        codes = data.values_list('state_province_code', flat=True)
        names = data.values_list('name', flat=True)

        return codes, names

    def generate_state_province_code(self, codes: dict, number: int) -> str:
        """
        """

        faker = Faker()
        for _ in range(number):
            code = faker.state_abbr(include_territories=True)
            if code not in codes:
                return code
        raise ValueError("Could not find a unique state/province code")

    def generate_state_province_name(self, names: dict, number: int) -> str:
        """
        """
        faker = Faker()
        for _ in range(number):
            name = faker.state()
            if name not in names:
                return name
        raise ValueError("Could not find a unique state/province name")


def state_province_factory():
    """
    Fixture for injecting StateProvinceFactory into tests.

    Contributor Notes:
    - Enables method chaining for test setup.
    - Supports teardown via Django's test DB rollback.
    """
    return StateProvinceFactory()
