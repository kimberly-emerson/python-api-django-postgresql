"""
tba
"""

# import json
import pytest
from rest_framework.reverse import reverse
from faker import Faker
from model_bakery import baker
from decouple import config

from api.people.models.country_region_model import CountryRegion
from api.people.models.state_province_model import StateProvince
from api.utils.values_handler import get_unique_name


DB_ALIAS = f"{config('TEST_DB_PROFILE')}"

pytestmark = [
                pytest.mark.django_db(
                    databases=[f"{DB_ALIAS}"],
                    transaction=True),
                pytest.mark.e2e
             ]


class TestStateProvinceEndpoints:
    """
    tba
    """
    # pylint: disable=no-member

    def test_state_province_list(self, auth_client):
        """
        tba
        """
        data = StateProvince.objects.all().last()

        # if no object exists, create some
        if not data:
            list(self.create_state_provinces(3))

        # get the list endpoint
        url = reverse("state-provinces")

        # test returning list of objects
        response = auth_client.get(
            url,
            HTTP_ACCEPT='application/json'
        )

        # validate response
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        assert isinstance(response.data, dict)

    def test_state_province_create(self, auth_client):
        """
        tba
        """
        # get existing objects and their unique values
        # pylint: disable=no-member
        data = StateProvince.objects.all()

        names = data.values_list('name', flat=True)

        # set unique values to be created
        name = get_unique_name(names, 100)

        # create object
        instance = {
            'name': name
        }

        # get the create endpoint
        url = reverse("state-provinces")
        print("URL: ", url)

        # test the create endpoint
        response = auth_client.post(
            url,
            HTTP_ACCEPT='application/json',
            data={
                'name': instance['name']
            },
            format='json'
        )

        # validate response
        assert response.status_code == 201
        assert response.headers["Content-Type"] == "application/json"
        assert isinstance(response.data, dict)

    def test_state_province_retrieve(self, auth_client):
        """
        tba
        """
        # test if an object exists
        # pylint: disable=no-member
        data = StateProvince.objects.all().last()

        instance = {}
        if not data:
            # if no objects exist, create one
            instance = self.create_state_provinces(1)
        else:
            # otherwise, add existing object to dictionary
            instance['state_province_id'] = data.state_province_id
            instance['name'] = data.name

        # query created object
        query = StateProvince.objects.get(  # pylint: disable=no-member
            state_province_id=instance['state_province_id']
        )

        # get the retrieve endpoint
        url = reverse(
            "state-provinces-id",
            kwargs={"state_province_id": instance['state_province_id']}
        )
        # test the retrieve endpoint
        response = auth_client.get(
            url,
            HTTP_ACCEPT='application/json'
        )

        # Validate response
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        assert isinstance(response.data, dict)
        assert instance['state_province_id'] == query.state_province_id
        assert instance['name'] == query.name

    def test_state_province_update(self, auth_client):
        """
        tba
        """
        faker = Faker()
        # get last existing object
        # pylint: disable=no-member
        data = StateProvince.objects.all().last()

        instance = {}
        if not data:
            # if no objects exist, create one
            instance = self.create_state_provinces(1)
        else:
            # otherwise, add existing object to dictionary
            instance['state_province_id'] = data.state_province_id
            instance['name'] = data.name

        # update instance
        instance['name'] = faker.name()

        # get the update endpoint
        url = reverse(
            "state-provinces-id",
            kwargs={"state_province_id": instance['state_province_id']}
        )
        # test the update endpoint
        response = auth_client.put(
            url,
            data={
                'state_province_id': instance['state_province_id'],
                'name': instance['name']
            },
            format='json'
        )

        assert response.status_code == 200
        assert isinstance(response.data, dict)

    def test_state_province_partial_update(self, auth_client):
        """
        tba
        """
        faker = Faker()
        # get last existing object
        # pylint: disable=no-member
        data = StateProvince.objects.all().last()

        instance = {}
        if not data:
            # if no objects exist, create one
            instance = self.create_state_provinces(1)
        else:
            # otherwise, add existing object to dictionary
            instance['state_province_id'] = data.state_province_id
            instance['name'] = data.name

        # update instance
        instance['name'] = faker.name()

        # get the update endpoint
        url = reverse(
            "state-provinces-id",
            kwargs={"state_province_id": instance['state_province_id']}
        )
        # test the update endpoint
        response = auth_client.patch(
            url,
            data={
                'name': instance['name']
            },
            format='json'
        )

        assert response.status_code == 200
        assert isinstance(response.data, dict)

    def test_state_province_delete(self, auth_client):
        """
        tba
        """
        faker = Faker()
        # pylint: disable=no-member
        data = StateProvince.objects.all().last()

        instance = []
        if not data:
            state_province = {
                'state_province_id': faker.random_int(),
                'name': faker.word()
            }
            instance = baker.make(StateProvince, **state_province)
        else:
            instance = data

        # get the update endpoint
        url = reverse(
            "state-provinces-id",
            kwargs={"state_province_id": instance.state_province_id}
        )
        # test the delete endpoint
        response = auth_client.delete(
            url
        )

        assert response.status_code == 204

    def test_state_province_options(self, auth_client):
        """
        tba
        """
        # get the destroy endpoint
        url = reverse("state-provinces")

        # test the destroy endpoint
        response = auth_client.options(
            url,
            HTTP_ACCEPT='application/json'
        )

        assert response.status_code == 200

    def test_state_province_head(self, auth_client):
        """
        tba
        """
        # get the destroy endpoint
        url = reverse("state-provinces")

        # test the destroy endpoint
        response = auth_client.head(
            url,
            HTTP_ACCEPT='application/json'
        )

        assert response.status_code == 200

    def create_state_provinces(self, num: int) -> dict:
        """
        tba
        """
        faker = Faker()

        # get list of objects
        # pylint: disable=no-member
        data = StateProvince.objects.all().last()

        items = {}
        if not data:
            # create n objects
            country_region_code = CountryRegion.objects.all().last()
            for _ in range(num):
                state_province = {
                    'state_province_code': faker.state_abbr(),
                    'country_region_code': country_region_code,
                    'is_only_state_province_flag': faker.boolean(),
                    'sales_territory_id': faker.random_int(),
                    'name': faker.word()
                }
                # create address type object
                instance = baker.make(StateProvince, **state_province)

                # update list of objects
                items.update(instance)

        return items
