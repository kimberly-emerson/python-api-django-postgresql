"""
# `tests/e2e/people/state_provinces_test.py`

Test module for StateProvince DRF endpoints.

Purpose:
- Validates CRUD operations for StateProvince model via DRF viewsets.
- Ensures endpoint behavior aligns with expected response shapes and status
codes.
- Uses factory scaffolds for mock and persisted data generation.

Contributor Notes:
- All tests assume `auth_client` provides authenticated access.
- Uses `state_province_factory` for mock payloads and persisted instances.
- Requires Django test DB with transactional support.
- Designed for institutional review and onboarding clarity.
"""

import pytest
from rest_framework.reverse import reverse
from faker import Faker

from api.people.models.state_province_model import StateProvince
from tests.factories.people.state_province_factory import (
    StateProvinceFactory
)

MODEL = 'STATE PROVINCE'
BASENAME = 'address-types'

pytestmark = [
    pytest.mark.django_db(databases=["default"], transaction=True),
    pytest.mark.e2e
]


# pylint: disable=redefined-outer-name
def state_province_factory() -> StateProvinceFactory:
    """
    Fixture that returns an instance of StateProvinceFactory.

    Usage:
        def test_state_province_create(state_province_factory):
            payload = state_province_factory.mock_state_province()

    Contributor Notes:
    - Enables method chaining for test setup.
    - Supports teardown via Django's test DB rollback.
    """
    return StateProvinceFactory()


class TestStateProvinceEndpoints:
    """
    Test suite for StateProvince DRF endpoints.

    Covers:
    - List
    - Create
    - Retrieve
    - Update
    - Partial Update
    - Delete

    Contributor Notes:
    - Uses `state_province_factory` for mock and persisted data.
    - Validates response status codes, content types, and payload structure.
    - Designed for onboarding and institutional review.
    """

    # pylint: disable=no-member

    def test_state_province_list(self, auth_client, state_province_factory):
        """
        Test for listing state provinces via DRF endpoint.

        Ensures:
        - Endpoint returns 200 OK.
        - Response is JSON and contains a dictionary.
        - At least one StateProvince exists or is created.

        Uses:
        - state_province_factory.create_state_provinces(3) for setup.
        """
        data = StateProvince.objects.all().last()
        if not data:
            list(state_province_factory.create_state_provinces(3))

        url = reverse(f"{BASENAME}-list")
        response = auth_client.get(
            url,
            HTTP_ACCEPT='application/json'
        )
        print("%s LIST RESPONSE: %s", MODEL, response.data)

        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        assert isinstance(response.data, dict)

    def test_state_province_create(self, auth_client, state_province_factory):
        """
        Test for creating an state province via DRF endpoint.

        Ensures:
        - Endpoint returns 201 Created.
        - Response contains the created name.
        - Payload is valid and unique.

        Uses:
        - state_province_factory.mock_state_province() for payload.
        """
        instance = state_province_factory.mock_state_province()
        print("%s CREATE INSTANCE: %s", MODEL, instance)

        url = reverse(f"{BASENAME}-list")

        response = auth_client.post(
            url,
            HTTP_ACCEPT='application/json',
            data={'name': instance['name']},
            format='json'
        )
        print("%s CREATE RESPONSE: %s", MODEL, response.data)

        assert response.status_code == 201
        assert response.headers["Content-Type"] == "application/json"
        assert isinstance(response.data, dict)
        assert response.data['data']['name'] == instance['name']

    def test_state_province_retrieve(
            self,
            auth_client,
            state_province_factory):
        """
        Test for retrieving a single state province via DRF endpoint.

        Ensures:
        - Endpoint returns 200 OK.
        - Response contains correct state_province_id and name.

        Uses:
        - state_province_factory.create_state_provinces(1) for setup if needed.
        """
        data = StateProvince.objects.all().last()
        instance = {}

        if not data:
            instance = state_province_factory.create_state_provinces(1)
        else:
            instance['name'] = data.name
        print("%s RETRIEVE INSTANCE: %s", MODEL, instance)

        query = StateProvince.objects.get(name=instance['name'])
        print("%s RETRIEVE QUERY: %s", MODEL, query)

        url = reverse(f"{BASENAME}-detail",
                      kwargs={"state_province_id": query.state_province_id})

        response = auth_client.get(
            url,
            HTTP_ACCEPT='application/json'
        )
        print("%s RETRIEVE RESPONSE: %s", MODEL, response.data)

        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        assert isinstance(response.data, dict)
        assert instance['name'] == query.name
        assert response.data['data']['state_province_id'] == (
            query.state_province_id
        )
        assert response.data['data']['name'] == query.name

    def test_state_province_update(self, auth_client, state_province_factory):
        """
        Test for full update of an state province via DRF endpoint.

        Ensures:
        - Endpoint returns 200 OK.
        - Updated name is reflected in response.

        Uses:
        - Faker for new name.
        - state_province_factory.create_state_provinces(1) for setup if needed.
        """
        data = StateProvince.objects.all().last()
        instance = {}

        if not data:
            instance = state_province_factory.create_state_provinces(1)
        else:
            instance['name'] = data.name
        print("%s UPDATE INSTANCE: %s", MODEL, instance)

        query = StateProvince.objects.get(name=instance['name'])
        print("%s UPDATE QUERY: %s", MODEL, query)

        faker = Faker()
        instance['name'] = faker.name()

        url = reverse(f"{BASENAME}-detail",
                      kwargs={"state_province_id": query.state_province_id})

        response = auth_client.put(
            url,
            data={'name': instance['name']},
            format='json'
        )
        print("%s UPDATE RESPONSE: %s", MODEL, response.data)

        assert response.status_code == 200
        assert isinstance(response.data, dict)
        assert response.data['data']['name'] == instance['name']

    def test_state_province_partial_update(
            self,
            auth_client,
            state_province_factory):
        """
        Test for partial update of an state province via DRF endpoint.

        Ensures:
        - Endpoint returns 200 OK.
        - Updated name is reflected in response.

        Uses:
        - Faker for new name.
        - state_province_factory.create_state_provinces(1) for setup if needed.
        """
        data = StateProvince.objects.all().last()
        instance = {}

        if not data:
            instance = state_province_factory.create_state_provinces(1)
        else:
            instance['name'] = data.name
        print("%s PARTIAL UPDATE INSTANCE: %s", MODEL, instance)

        query = StateProvince.objects.get(name=instance['name'])
        print("%s PARTIAL UPDATE QUERY: %s", MODEL, query)

        faker = Faker()
        instance['name'] = faker.name()

        url = reverse(f"{BASENAME}-detail",
                      kwargs={"state_province_id": query.state_province_id})

        response = auth_client.put(
            url,
            data={'name': instance['name']},
            format='json'
        )
        print("%s PARTIAL UPDATE RESPONSE: %s", MODEL, response.data)

        assert response.status_code == 200
        assert isinstance(response.data, dict)
        assert response.data['data']['name'] == instance['name']

    def test_state_province_delete(self, auth_client, state_province_factory):
        """
        Test for deleting an state province via DRF endpoint.

        Ensures:
        - Endpoint returns 204 No Content.
        - Subsequent delete returns non-204 (object no longer exists).

        Uses:
        - state_province_factory.create_state_province() for setup if needed.
        """
        instance = state_province_factory.create_state_province()
        print(MODEL, "DELETE INSTANCE: %s", instance)

        query = StateProvince.objects.get(
            name=instance['name']
        )
        print("%s DELETE QUERY: %s", MODEL, query)

        url = reverse(f"{BASENAME}-detail",
                      kwargs={"state_province_id": query.state_province_id})

        response = auth_client.delete(url)
        print("%s DELETE RESPONSE: %s", MODEL, response)
        assert response.status_code == 204

        response = auth_client.delete(url)
        print(MODEL, "DELETE RESPONSE: %s", response)
        assert response.status_code != 204
