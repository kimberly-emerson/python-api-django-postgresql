"""
tba
"""

import pytest
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import call_command
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


@pytest.fixture(scope="session")
def django_db_setup(django_db_blocker):
    """
    Applies migrations to the 'test' DB alias during pytest startup.
    """
    with django_db_blocker.unblock():
        db_config = settings.DATABASES.get("default")
        if not db_config:
            raise RuntimeError("Missing 'default' DB alias in settings.DATABASES")

        db_name = db_config["NAME"]
        print(f"Migrating test DB: {db_name}")
        call_command("migrate", database="default", verbosity=0)


@pytest.fixture
def api_client():
    """
    tba
    """
    return APIClient()


@pytest.fixture
def create_user(db):
    """
    tba
    """
    def make_user(**kwargs):
        return User.objects.create_user(**kwargs)
    return make_user


@pytest.fixture
def auth_client(create_user):
    """
    Authenticated APIClient using the 'test' DB alias.
    """
    # Create user directly on the 'test' DB
    user = User.objects.db_manager("default").create_user(
        username="testuser",
        password="showgirl"
    )

    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    client.headers = headers
    client.force_authenticate(user=user)

    return client


def pytest_configure(config: pytest.Config):
    """
    tba
    """
    config.addinivalue_line("markers", "unit: tests isolated from DB, external"
                            "APIs, and internal mocks")
    config.addinivalue_line("markers", "e2e: tests related to API endpoints")
    config.addinivalue_line("markers", "integration: integration-level tests")
    config.addinivalue_line("markers", "regression: regression test suite")
