import pytest


@pytest.fixture
@pytest.mark.django_db
def hr_token(client, django_user_model) -> str:
    """
    The hr_token function is a fixture that creates a substitute user from the database, makes a token request
    and returns it as a string.
    """
    username: str = "test_user"
    password: str = "1234"

    django_user_model.objects.create_user(
        username=username,
        password=password
    )

    response = client.post(
        "/user/token/",
        {
            "username": username,
            "password": password,
            "location": "test_location",
            "birth_date": "2010-10-10"
        },
        format="json"
    )

    return response.data["access"]