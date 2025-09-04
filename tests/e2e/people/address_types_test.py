"""
"""

import pytest
from rest_framework.reverse import reverse
from faker import Faker

from api.people.models.address_type_model import AddressType
from tests.factories.people.address_type_factory import (
    AddressTypeFactory
)

MODEL = 'ADDRESS TYPE'
BASENAME = 'address-types'

pytestmark = [
    pytest.mark.django_db(databases=["default"], transaction=True),
    pytest.mark.e2e
]


# pylint: disable=redefined-outer-name
@pytest.fixture
def address_type_factory() -> AddressTypeFactory:
    """
    """
    return AddressTypeFactory()


class TestAddressTypeEndpoints:
    """
    """

    # pylint: disable=no-member

    def test_address_type_list(self, auth_client, address_type_factory):
        """
        """
        data = AddressType.objects.all().last()
        if not data:
            list(address_type_factory.create_address_types(3))

        url = reverse(f"{BASENAME}-list")
        response = auth_client.get(
            url,
            HTTP_ACCEPT='application/json'
        )
        print("%s LIST RESPONSE: %s", MODEL, response.data)

        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        assert isinstance(response.data, dict)

    def test_address_type_create(self, auth_client, address_type_factory):
        """
        """
        instance = address_type_factory.mock_address_type()
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

    def test_address_type_retrieve(self, auth_client, address_type_factory):
        """
        """
        data = AddressType.objects.all().last()
        instance = {}

        if not data:
            instance = address_type_factory.create_address_types(1)
        else:
            instance['name'] = data.name
        print("%s RETRIEVE INSTANCE: %s", MODEL, instance)

        query = AddressType.objects.get(name=instance['name'])
        print("%s RETRIEVE QUERY: %s", MODEL, query)

        url = reverse(f"{BASENAME}-detail",
                      kwargs={"address_type_id": query.address_type_id})

        response = auth_client.get(
            url,
            HTTP_ACCEPT='application/json'
        )
        print("%s RETRIEVE RESPONSE: %s", MODEL, response.data)

        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        assert isinstance(response.data, dict)
        assert instance['name'] == query.name
        assert response.data['data']['address_type_id'] == (
            query.address_type_id
        )
        assert response.data['data']['name'] == query.name

    def test_address_type_update(self, auth_client, address_type_factory):
        """
        """
        data = AddressType.objects.all().last()
        instance = {}

        if not data:
            instance = address_type_factory.create_address_types(1)
        else:
            instance['name'] = data.name
        print("%s UPDATE INSTANCE: %s", MODEL, instance)

        query = AddressType.objects.get(name=instance['name'])
        print("%s UPDATE QUERY: %s", MODEL, query)

        faker = Faker()
        instance['name'] = faker.name()

        url = reverse(f"{BASENAME}-detail",
                      kwargs={"address_type_id": query.address_type_id})

        response = auth_client.put(
            url,
            data={'name': instance['name']},
            format='json'
        )
        print("%s UPDATE RESPONSE: %s", MODEL, response.data)

        assert response.status_code == 200
        assert isinstance(response.data, dict)
        assert response.data['data']['name'] == instance['name']

    def test_address_type_partial_update(
            self,
            auth_client,
            address_type_factory):
        """
        """
        data = AddressType.objects.all().last()
        instance = {}

        if not data:
            instance = address_type_factory.create_address_types(1)
        else:
            instance['name'] = data.name
        print("%s PARTIAL UPDATE INSTANCE: %s", MODEL, instance)

        query = AddressType.objects.get(name=instance['name'])
        print("%s PARTIAL UPDATE QUERY: %s", MODEL, query)

        faker = Faker()
        instance['name'] = faker.name()

        url = reverse(f"{BASENAME}-detail",
                      kwargs={"address_type_id": query.address_type_id})

        response = auth_client.put(
            url,
            data={'name': instance['name']},
            format='json'
        )
        print("%s PARTIAL UPDATE RESPONSE: %s", MODEL, response.data)

        assert response.status_code == 200
        assert isinstance(response.data, dict)
        assert response.data['data']['name'] == instance['name']

    def test_address_type_delete(self, auth_client, address_type_factory):
        """
        """
        instance = address_type_factory.create_address_type()
        print(MODEL, "DELETE INSTANCE: %s", instance)

        query = AddressType.objects.get(
            name=instance['name']
        )
        print(MODEL, "DELETE QUERY: %s", query)

        url = reverse(f"{BASENAME}-detail",
                      kwargs={"address_type_id": query.address_type_id})

        response = auth_client.delete(url)
        print(MODEL, "DELETE RESPONSE: %s", response)
        assert response.status_code == 204

        response = auth_client.delete(url)
        print(MODEL, "CONFIRM DELETE RESPONSE: %s", response)
        assert response.status_code != 204
