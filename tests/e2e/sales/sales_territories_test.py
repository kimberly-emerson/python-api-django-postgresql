"""
tba
"""

import pytest
from rest_framework.reverse import reverse
from faker import Faker
from django.forms.models import model_to_dict

from api.sales.models.sales_territory_model import SalesTerritory
from tests.factories.people.country_region_factory import (
   CountryRegionFactory
)
from tests.factories.sales.sales_territory_factory import (
   SalesTerritoryFactory
)

MODEL = "SALES TERRITORIES"
BASENAME = "sales-territories"

pytestmark = [
                pytest.mark.django_db(
                    databases=["default"],
                    transaction=True),
                pytest.mark.e2e
             ]


# pylint: disable=redefined-outer-name
@pytest.fixture
def country_region_factory() -> CountryRegionFactory:
    """
    tba
    """
    return CountryRegionFactory()

@pytest.fixture
def sales_territory_factory() -> SalesTerritoryFactory:
    """
    tba
    """
    return SalesTerritoryFactory()


class TestSalesTerritoryEndpoints:
    """
    tba
    """
    # pylint: disable=no-member
    def test_sales_territory_list(self, auth_client, sales_territory_factory):
        """
        tba
        """
        data = SalesTerritory.objects.all().last()
        if not data:
            sales_territory_factory.create_sales_territories(3)

        url = reverse(f"{BASENAME}-list")
        response = auth_client.get(
            url,
            HTTP_ACCEPT='application/json'
        )
        print(MODEL, "LIST RESPONSE: %s", response.data)

        # validate response
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        assert isinstance(response.data, dict)

    def test_sales_territory_create(
            self,
            auth_client,
            sales_territory_factory):
        """
        tba
        """

        # mock sales territory object
        instance = sales_territory_factory.mock_sales_territory()
        print(MODEL, 'CREATE MOCK: ', instance)

        # get the create endpoint
        url = reverse(f"{BASENAME}-list")

        # test the create endpoint
        response = auth_client.post(
            url,
            HTTP_ACCEPT='application/json',
            data={
                'name': instance['name'],
                'country_region': instance['country_region']['country_region_code'],
                'region': instance['region'],
                'sales_ytd': instance['sales_ytd'],
                'sales_last_year': instance['sales_last_year'],
                'cost_ytd': instance['cost_ytd'],
                'cost_last_year': instance['cost_last_year']
            },
            format='json'
        )
        print(MODEL, "CREATE RESPONSE: %s", response.data)

        # validate response
        assert response.status_code == 201
        assert response.headers["Content-Type"] == "application/json"
        assert isinstance(response.data, dict)
        assert response.data["data"]["name"] == instance['name']
        assert response.data["data"]["country_region_detail"]['name'] == (
            instance['country_region']['name']
        )

    def test_sales_territory_retrieve(
            self,
            auth_client,
            sales_territory_factory):
        """
        tba
        """
        # test if an object exists
        # pylint: disable=no-member
        data = SalesTerritory.objects.all().last()

        instance = {}
        if not data:
            # if no objects exist, create one
            instance = sales_territory_factory.create_sales_territory(1)
        else:
            # otherwise, add existing object to dictionary
            instance = model_to_dict(
                # pylint: disable=protected-access
                data, fields=[f.name for f in data._meta.fields]
            )
        print(MODEL, "RETRIEVE INSTANCE: %s", instance)

        # query created object
        # pylint: disable=no-member
        query = SalesTerritory.objects.get(
            sales_territory_id=instance['sales_territory_id']
        )
        print(MODEL, "RETRIEVE QUERY: %s", instance)

        # get the retrieve endpoint
        url = reverse(
            f"{BASENAME}-detail",
            kwargs={"sales_territory_id": instance['sales_territory_id']}
        )
        # test the retrieve endpoint
        response = auth_client.get(
            url,
            HTTP_ACCEPT='application/json'
        )
        print(MODEL, "RETRIEVE RESPONSE: %s", response.data)

        # Validate response
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        assert isinstance(response.data, dict)
        assert response.data['data']['sales_territory_id'] == (
            instance['sales_territory_id']
        )
        assert response.data['data']['name'] == instance['name']
        assert instance['sales_territory_id'] == query.sales_territory_id
        assert instance['name'] == query.name

    def test_sales_territory_update(
            self,
            auth_client,
            sales_territory_factory):
        """
        tba
        """
        faker = Faker()
        # get last existing object
        # pylint: disable=no-member
        data = SalesTerritory.objects.all().last()

        instance = {}
        if not data:
            # if no objects exist, create one
            instance = sales_territory_factory.create_sales_territory()
        else:
            # otherwise, add existing object to dictionary
            instance = model_to_dict(
                # pylint: disable=protected-access
                data, fields=[f.name for f in data._meta.fields]
            )
        print(MODEL, "UPDATE INSTANCE: %s", instance)

        # update instance
        instance['name'] = faker.country()

        # get the update endpoint
        url = reverse(
            f"{BASENAME}-detail",
            kwargs={"sales_territory_id": instance['sales_territory_id']}
        )
        # test the update endpoint
        response = auth_client.put(
            url,
            data={
                'name': instance['name'],
                'country_region': instance['country_region'],
                'region': instance['region'],
                'sales_ytd': instance['sales_ytd'],
                'sales_last_year': instance['sales_last_year'],
                'cost_ytd': instance['cost_ytd'],
                'cost_last_year': instance['cost_last_year']
            },
            format='json'
        )
        print(MODEL, "UPDATE RESPONSE: %s", response.data)

        # validate response
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        assert isinstance(response.data, dict)

    def test_sales_territory_partial_update(
            self,
            auth_client,
            country_region_factory,
            sales_territory_factory):
        """
        tba
        """
        # create object
        instance = sales_territory_factory.create_sales_territory()
        print(MODEL, "PARTIAL UPDATE INSTANCE: ", instance)

        # update instance
        faker = Faker()
        instance['name'] = faker.state()
        country_region = country_region_factory.create_country_region()

        # get the update endpoint
        url = reverse(
            f"{BASENAME}-detail",
            kwargs={"sales_territory_id": instance['sales_territory_id']}
        )
        # test the update endpoint
        response = auth_client.patch(
            url,
            data={
                'name': instance['name'],
                'country_region': country_region
            },
            format='json'
        )
        print(MODEL, "PARTIAL UPDATE RESPONSE: %s", response.data)

        # validate response
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        assert isinstance(response.data, dict)

    def test_sales_territory_delete(
            self,
            auth_client,
            sales_territory_factory):
        """
        tba
        """
        # pylint: disable=no-member
        instance = sales_territory_factory.create_sales_territory()
        print(MODEL, "DELETE INSTANCE: %s", instance)

        # get the update endpoint
        url = reverse(
            f"{BASENAME}-detail",
            kwargs={"sales_territory_id": instance['sales_territory_id']}
        )
        # test the delete endpoint
        response = auth_client.delete(url)
        print(MODEL, "DELETE RESPONSE: %s", response)
        assert response.status_code == 204

        # test delete was successful
        confirm = auth_client.delete(url)
        print(MODEL, "CONFIRM DELETE RESPONSE: %s", response)
        assert confirm.status_code == 404
