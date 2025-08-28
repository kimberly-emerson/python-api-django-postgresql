"""
tba
"""
from faker import Faker


def get_unique_name(existing_names: dict, number: int):
    """
    tba
    """
    faker = Faker()
    name = None
    for _ in range(number):
        name = faker.word()
        if name not in existing_names:
            return name.title()
    raise ValueError("Could not find a unique name")


def get_unique_country_code(existing_codes: dict, number: int):
    """
    tba
    """
    faker = Faker()
    for _ in range(number):
        code = faker.country_code()
        if code not in existing_codes:
            return code
    raise ValueError("Could not find a unique country code")
