"""
tba
"""

import pytest
from django.forms.models import model_to_dict
from rest_framework.reverse import reverse

from api.sales.models.sales_territory_model import SalesTerritory
from api.sales.serializers.sales_territory_serializer import (
    SalesTerritorySerializer
)
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
        print(MODEL, "LIST RESPONSE: ", response.data)

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
        mock = sales_territory_factory.mock_sales_territory()

        # get the create endpoint
        url = reverse(f"{BASENAME}-list")

        # test the create endpoint
        response = auth_client.post(
            url,
            HTTP_ACCEPT='application/json',
            data={
                'name': mock['name'],
                'country_region_code': mock['country_region_code'],
                'region': mock['region'],
                'sales_ytd': mock['sales_ytd'],
                'sales_last_year': mock['sales_last_year'],
                'cost_ytd': mock['cost_ytd'],
                'cost_last_year': mock['cost_last_year']
            },
            format='json'
        )
        print(MODEL, "CREATE RESPONSE: %s", response.data)

        # validate response
        assert response.status_code == 201
        assert response.headers["Content-Type"] == "application/json"
        assert isinstance(response.data, dict)

    def test_sales_territory_retrieve(
            self,
            auth_client,
            sales_territory_factory):
        """
        tba
        """
        # test if an object exists
        data = SalesTerritory.objects.all().last()

        instance = data
        if not data:
            # if no objects exist, create one
            instance = sales_territory_factory.create_sales_territory(1)

        print(MODEL, "RETRIEVE INSTANCE: sales_territory_id: ",
              instance.sales_territory_id)

        # query created object
        query = SalesTerritory.objects.get(
            sales_territory_id=instance.sales_territory_id
        )
        print(MODEL, "RETRIEVE QUERY: ", query)

        # get the retrieve endpoint
        url = reverse(
            f"{BASENAME}-detail",
            kwargs={"sales_territory_id": query.sales_territory_id}
        )
        # test the retrieve endpoint
        response = auth_client.get(
            url,
            HTTP_ACCEPT='application/json'
        )
        print(MODEL, "RETRIEVE RESPONSE: ", response.data)

        # Validate response
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        assert isinstance(response.data, dict)

    def test_sales_territory_update(
            self,
            auth_client,
            sales_territory_factory):
        """
        tba
        """
        # test if an object exists
        data = SalesTerritory.objects.all().last()
        serializer = SalesTerritorySerializer(data)
        instance = dict(serializer.data)
        instance['country_region_code'] = (
            instance['country_region_detail']['country_region_code']
        )
        del instance['country_region_detail']

        if not data:
            # if no objects exist, create one
            instance = sales_territory_factory.create_sales_territory()
            instance = model_to_dict(instance)
            print(MODEL, "UPDATE CREATE INSTANCE: ", serializer.data)

        print(MODEL, "UPDATE INSTANCE: ", instance)

        # update instance
        names = sales_territory_factory.get_unique_sales_territory_names()
        instance['name'] = sales_territory_factory.generate_sales_territory(
            names,
            100)

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
                'country_region_code': instance['country_region_code'],
                'region': instance['region'],
                'sales_ytd': instance['sales_ytd'],
                'sales_last_year': instance['sales_last_year'],
                'cost_ytd': instance['cost_ytd'],
                'cost_last_year': instance['cost_last_year']
            },
            format='json'
        )
        print(MODEL, "UPDATE RESPONSE: ", response.data)

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
        # test if an object exists
        data = SalesTerritory.objects.all().last()

        instance = data
        if not data:
            # if no objects exist, create one
            instance = sales_territory_factory.create_sales_territory()

        print(MODEL, "UPDATE INSTANCE: ", instance)

        # update instance
        names = sales_territory_factory.get_unique_sales_territory_names()
        instance.name = sales_territory_factory.generate_sales_territory(
            names,
            100)
        country_region = country_region_factory.create_country_region()

        # get the update endpoint
        url = reverse(
            f"{BASENAME}-detail",
            kwargs={"sales_territory_id": instance.sales_territory_id}
        )
        # test the update endpoint
        response = auth_client.patch(
            url,
            data={
                'name': instance.name,
                'country_region_code': country_region['country_region_code']
            },
            format='json'
        )
        print(MODEL, "PARTIAL UPDATE RESPONSE: ", response.data)

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
        print(MODEL, "DELETE INSTANCE: ", instance)

        # get the update endpoint
        url = reverse(
            f"{BASENAME}-detail",
            kwargs={"sales_territory_id": instance.sales_territory_id}
        )
        # test the delete endpoint
        response = auth_client.delete(url)
        print(MODEL, "DELETE RESPONSE: ", response)
        assert response.status_code == 204

        # test delete was successful
        confirm = auth_client.get(url, HTTP_ACCEPT='application/json')
        print(MODEL, "CONFIRM DELETE GET RESPONSE: ", confirm.data)
        assert confirm.status_code == 404
