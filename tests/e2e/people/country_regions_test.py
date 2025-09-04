"""
# `tests/e2e/people/country_regions_test.py`

Test module for CountryRegion DRF endpoints.

Purpose:
- Validates CRUD operations for CountryRegion model via DRF viewsets.
- Ensures endpoint behavior aligns with expected response shapes and status
codes.
- Uses factory scaffolds for mock and persisted data generation.

Contributor Notes:
- All tests assume `auth_client` provides authenticated access.
- Uses `country_region_factory` for mock payloads and persisted instances.
- Requires Django test DB with transactional support.
- Designed for institutional review and onboarding clarity.
"""

import pytest
from rest_framework.reverse import reverse
from faker import Faker

from api.people.models.country_region_model import CountryRegion
from tests.factories.people.country_region_factory import (
    CountryRegionFactory
)


MODEL = 'COUNTRY REGION'
BASENAME = 'country-regions'

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
    Fixture that returns an instance of CountryRegionFactory.

    Usage:
        def test_country_region_create(country_region_factory):
            payload = country_region_factory.mock_country_region()

    Contributor Notes:
    - Enables method chaining for test setup.
    - Supports teardown via Django's test DB rollback.
    """
    return CountryRegionFactory()


class TestCountryRegionEndpoints:
    """
    """
    def test_country_region_list(self, auth_client, country_region_factory):
        """
        """
        data = CountryRegion.objects.all().last()
        if not data:
            list(country_region_factory.create_country_regions(3))

        url = reverse(f"{BASENAME}-list")
        response = auth_client.get(
            url,
            HTTP_ACCEPT='application/json'
        )

        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        assert isinstance(response.data, dict)

    def test_country_region_create(self, auth_client, country_region_factory):
        """
        Test for creating a country region via DRF endpoint.

        Ensures:
        - Endpoint returns 201 Created.
        - Response contains the created country_region_code and name.
        - Instance is valid and unique.

        Uses:
        - country_regions_factory.mock_country_region() for instance.
        """
        # build country region object
        instance = country_region_factory.mock_country_region()
        print("%s CREATE INSTANCE: %s", MODEL, instance)

        # get the create endpoint
        url = reverse(f"{BASENAME}-list")

        # test the create endpoint
        response = auth_client.post(
            url,
            HTTP_ACCEPT='application/json',
            data={
                'country_region_code': instance['country_region_code'],
                'name': instance['name']
            },
            format='json'
        )
        print("%s CREATE RESPONSE: %s", MODEL, response.data)

        # validate response
        assert response.status_code == 201
        assert response.headers["Content-Type"] == "application/json"
        assert isinstance(response.data, dict)
        assert response.data['data']['country_region_code'] == (
            instance['country_region_code']
        )
        assert response.data['data']['name'] == instance['name']

    def test_country_region_retrieve(
            self,
            auth_client,
            country_region_factory):
        """
        Test for retrieving a single country region via DRF endpoint.

        Ensures:
        - Endpoint returns 200 OK.
        - Response contains correct country_region_code and name.

        Uses:
        - country_region_factory.create_country-regions(1) for setup if needed.
        """
        # get existing data
        data = CountryRegion.objects.all().last()

        instance = {}
        if not data:
            # if no objects exist, create one
            instance = country_region_factory.create_country_regions(1)
        else:
            # otherwise, add existing object to dictionary
            instance['country_region_code'] = data.country_region_code
            instance['name'] = data.name
        print("%s RETRIEVE INSTANCE: %s", MODEL, instance)

        # query created object
        query = CountryRegion.objects.get(
            country_region_code=instance['country_region_code']
        )
        print("%s RETRIEVE QUERY: %s", MODEL, query)

        # get the retrieve endpoint
        url = reverse(
            f"{BASENAME}-detail",
            kwargs={"country_region_code": instance['country_region_code']}
        )
        # test the retrieve endpoint
        response = auth_client.get(
            url,
            HTTP_ACCEPT='application/json'
        )
        print("%s RETRIEVE RESPONSE: %s", MODEL, response.data)

        # Validate response
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        assert isinstance(response.data, dict)
        assert instance['country_region_code'] == query.country_region_code
        assert instance['name'] == query.name
        assert response.data['data']['country_region_code'] == (
            query.country_region_code
        )
        assert response.data['data']['name'] == query.name

    def test_country_region_update(self, auth_client):
        """
        Test for full update of a country region via DRF endpoint.

        Ensures:
        - Endpoint returns 200 OK.
        - Updated name is reflected in response.

        Uses:
        - Faker for new name.
        - country_region_factory.create_country_regions(1) for setup if needed.
        """
        # get existing object
        data = CountryRegion.objects.all().last()

        instance = {}
        if not data:
            # if no objects exist, create one
            instance = country_region_factory.create_country_regions(1)
        else:
            # otherwise, add existing object to dictionary
            instance['country_region_code'] = data.country_region_code
            instance['name'] = data.name
        print("%s UPDATE INSTANCE: %s", MODEL, instance)

        # update instance
        faker = Faker()
        instance['name'] = faker.name()

        # get the update endpoint
        url = reverse(
            f"{BASENAME}-detail",
            kwargs={"country_region_code": instance['country_region_code']}
        )
        # test the update endpoint
        response = auth_client.put(
            url,
            data={
                'country_region_code': instance['country_region_code'],
                'name': instance['name']
            },
            format='json'
        )
        print("%s UPDATE RESPONSE: %s", MODEL, response.data)

        assert response.status_code == 200
        assert isinstance(response.data, dict)
        assert response.data['data']['country_region_code'] == (
            instance['country_region_code']
        )
        assert response.data['data']['name'] == instance['name']

    def test_country_region_partial_update(
            self,
            auth_client,
            country_region_factory):
        """
        Test for partial update of a country region via DRF endpoint.

        Ensures:
        - Endpoint returns 200 OK.
        - Updated name is reflected in response.

        Uses:
        - Faker for new name.
        - country_region_factory.create_country_regions(1) for setup if needed.
        """
        # get existing object
        data = CountryRegion.objects.all().last()

        instance = {}
        if not data:
            # if no objects exist, create one
            instance = country_region_factory.create_country_regions(1)
        else:
            # otherwise, add existing object to dictionary
            instance['country_region_code'] = data.country_region_code
            instance['name'] = data.name
        print("%s PARTIAL UPDATE INSTANCE: %s", MODEL, instance)

        # update instance
        faker = Faker()
        instance['name'] = faker.name()

        # get the partial_update endpoint
        url = reverse(
            f"{BASENAME}-detail",
            kwargs={"country_region_code": instance['country_region_code']}
        )
        # test the update endpoint
        response = auth_client.patch(
            url,
            data={
                'name': instance['name']
            },
            format='json'
        )
        print("%s PARTIAL UPDATE RESPONSE: %s", MODEL, response.data)

        assert response.status_code == 200
        assert isinstance(response.data, dict)
        assert response.data['data']['country_region_code'] == (
            instance['country_region_code']
        )
        assert response.data['data']['name'] == instance['name']

    def test_country_region_delete(self, auth_client, country_region_factory):
        """
        tba
        """
        instance = country_region_factory.create_country_region()
        print(MODEL, "DELETE INSTANCE: ", instance)

        # get the delete endpoint
        url = reverse(
            f"{BASENAME}-detail",
            kwargs={"country_region_code": instance['country_region_code']}
        )
        # test the delete endpoint
        response = auth_client.delete(url)
        print(MODEL, "DELETE STATUS: %s", response.status_code)
        assert response.status_code == 204
