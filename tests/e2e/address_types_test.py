"""
tba
"""

# import json
import pytest
from rest_framework.reverse import reverse
from faker import Faker
from model_bakery import baker
from api.models.address_type_model import AddressType

pytestmark = [pytest.mark.django_db, pytest.mark.api]


class TestAddressTypeEndpoints():
    """
    tba
    """
    endpoint = "/api/address-types"

    @pytest.mark.django_db(databases=["default"], transaction=True)
    def test_list(self, auth_client):
        """
        tba
        """
        baker.make(AddressType, _quantity=3, _using="default")

        # Call the list endpoint
        url = reverse("list")
        response = auth_client.get(
            url,
            HTTP_ACCEPT='application/json'
        )

        # Validate response
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        assert isinstance(response.data, dict)
        # assert len(response.data) == 3

    # Optional: Validate returned data matches seeded objects
    # returned_ids = {item["address_type_id"] for item in data}
    # expected_ids = {obj.address_type_id for obj in address_types}
    # assert returned_ids == expected_ids

    def test_create(self, auth_client):
        """
        tba
        """
        faker = Faker()
        name = faker.name()

        # Call the create endpoint
        url = "/api/address-types"
        response = auth_client.post(
            url,
            HTTP_ACCEPT='application/json',
            data={
                'name': name
            },
            format="json"
        )

        # Validate response
        assert response.status_code == 201
        assert response.headers["Content-Type"] == "application/json"
        assert isinstance(response.data, dict)
        # assert response['data'].name == name

    def test_retrieve(self, auth_client):
        """
        tba
        """
        instance = baker.make(AddressType)
        query = AddressType.objects.get(  # pylint: disable=no-member
            address_type_id=instance.address_type_id
        )

        # Call the retrieve endpoint
        url = reverse(
            "retrieve",
            kwargs={"address_type_id": instance.address_type_id}
        )
        response = auth_client.get(
            url,
            HTTP_ACCEPT='application/json'
        )

        # Validate response
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        assert isinstance(response.data, dict)
        assert instance.address_type_id == query.address_type_id
        assert instance.name == query.name

    def test_update(self, auth_client):
        """
        tba
        """
        instance = baker.make(AddressType)
        update = baker.prepare(AddressType)

        # item = {
        #     'name': update.name
        # }

        url = f"/api/address-types/{instance.address_type_id}"

        response = auth_client.put(
            url,
            data={
                'name': update.name
            },
            format='json'
        )

        assert response.status_code == 200

    def test_partial_update(self, auth_client):
        """
        tba
        """
        faker = Faker()
        instance = baker.make(AddressType)

        item = {
            'name': faker.name(),
        }

        url = f'/api/address-types/{instance.address_type_id}'

        response = auth_client.patch(
            url,
            data={
                'name': item['name']
            },
            format='json'
        )

        assert response.status_code == 200
        # assert response['data']['name'] == item['name']

    def test_delete(self, auth_client):
        """
        tba
        """
        instance = baker.make(AddressType)

        url = f'/api/address-types/{instance.address_type_id}'

        response = auth_client.delete(
            url
        )

        assert response.status_code == 204
