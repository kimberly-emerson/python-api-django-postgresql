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
from api.utils.values_handler import get_unique_name, get_unique_country_code


DB_ALIAS = f"{config('TEST_DB_PROFILE')}"

pytestmark = [
                pytest.mark.django_db(
                    databases=[f"{DB_ALIAS}"],
                    transaction=True),
                pytest.mark.e2e
             ]


class TestCountryRegionEndpoints:
    """
    tba
    """
    # pylint: disable=no-member

    def test_country_region_list(self, auth_client):
        """
        tba
        """
        data = CountryRegion.objects.all().last()

        # if no object exists, create some
        if not data:
            list(self.create_country_regions(3))

        # get the list endpoint
        url = reverse("country-regions")

        # test returning list of objects
        response = auth_client.get(
            url,
            HTTP_ACCEPT='application/json'
        )

        # validate response
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        assert isinstance(response.data, dict)

    def test_country_region_create(self, auth_client):
        """
        tba
        """
        # get existing objects and their unique values
        # pylint: disable=no-member
        data = CountryRegion.objects.all()
        codes = data.values_list('country_region_code', flat=True)
        names = data.values_list('name', flat=True)

        # set unique values to be created
        code = get_unique_country_code(codes, 100)
        name = get_unique_name(names, 100)

        # create object
        instance = {
            'country_region_code': code,
            'name': name
        }

        # get the create endpoint
        url = reverse("country-regions")
        print("URL: ", url)

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

        # validate response
        assert response.status_code == 201
        assert response.headers["Content-Type"] == "application/json"
        assert isinstance(response.data, dict)

    def test_country_region_retrieve(self, auth_client):
        """
        tba
        """
        # test if an object exists
        # pylint: disable=no-member
        data = CountryRegion.objects.all().last()

        instance = {}
        if not data:
            # if no objects exist, create one
            instance = self.create_country_regions(1)
        else:
            # otherwise, add existing object to dictionary
            instance['country_region_code'] = data.country_region_code
            instance['name'] = data.name

        # query created object
        query = CountryRegion.objects.get(  # pylint: disable=no-member
            country_region_code=instance['country_region_code']
        )

        # get the retrieve endpoint
        url = reverse(
            "country-regions-code",
            kwargs={"country_region_code": instance['country_region_code']}
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
        assert instance['country_region_code'] == query.country_region_code
        assert instance['name'] == query.name

    def test_country_region_update(self, auth_client):
        """
        tba
        """
        faker = Faker()
        # get last existing object
        # pylint: disable=no-member
        data = CountryRegion.objects.all().last()

        instance = {}
        if not data:
            # if no objects exist, create one
            instance = self.create_country_regions(1)
        else:
            # otherwise, add existing object to dictionary
            instance['country_region_code'] = data.country_region_code
            instance['name'] = data.name

        # update instance
        instance['name'] = faker.name()

        # get the update endpoint
        url = reverse(
            "country-regions-code",
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

        assert response.status_code == 200
        assert isinstance(response.data, dict)

    def test_country_region_partial_update(self, auth_client):
        """
        tba
        """
        faker = Faker()
        # get last existing object
        # pylint: disable=no-member
        data = CountryRegion.objects.all().last()

        instance = {}
        if not data:
            # if no objects exist, create one
            instance = self.create_country_regions(1)
        else:
            # otherwise, add existing object to dictionary
            instance['country_region_code'] = data.country_region_code
            instance['name'] = data.name

        # update instance
        instance['name'] = faker.name()

        # get the update endpoint
        url = reverse(
            "country-regions-code",
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

        assert response.status_code == 200
        assert isinstance(response.data, dict)

    def test_country_region_delete(self, auth_client):
        """
        tba
        """
        faker = Faker()
        # pylint: disable=no-member
        data = CountryRegion.objects.all().last()

        instance = []
        if not data:
            country_region = {
                'country_region_code': faker.random_int(),
                'name': faker.word()
            }
            instance = baker.make(CountryRegion, **country_region)
        else:
            instance = data

        # get the update endpoint
        url = reverse(
            "country-regions-code",
            kwargs={"country_region_code": instance.country_region_code}
        )
        # test the delete endpoint
        response = auth_client.delete(
            url
        )

        assert response.status_code == 204

    def test_country_region_options(self, auth_client):
        """
        tba
        """
        # get the destroy endpoint
        url = reverse("country-regions")

        # test the destroy endpoint
        response = auth_client.options(
            url,
            HTTP_ACCEPT='application/json'
        )

        assert response.status_code == 200

    def test_country_region_head(self, auth_client):
        """
        tba
        """
        # get the destroy endpoint
        url = reverse("country-regions")

        # test the destroy endpoint
        response = auth_client.head(
            url,
            HTTP_ACCEPT='application/json'
        )

        assert response.status_code == 200

    def create_country_regions(self, num: int) -> dict:
        """
        tba
        """
        faker = Faker()

        # get list of objects
        # pylint: disable=no-member
        data = CountryRegion.objects.all().last()

        items = {}
        if not data:
            # create n objects
            for _ in range(num):
                country_region = {
                    'name': faker.word()
                }
                # create address type object
                instance = baker.make(CountryRegion, **country_region)

                # update list of objects
                items.update(instance)

        return items
