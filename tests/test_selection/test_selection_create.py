from typing import Dict, Any

import pytest
from rest_framework.exceptions import ErrorDetail

from ads.models import Ad
from author.models import User


@pytest.mark.django_db
def test_create_selection(client, hr_token: str, ad: Ad) -> None:
    """
    The test_create_selection function is designed to check the functioning when sending a POST request
    to the application at /selection/create/ with valid data. Accepts as arguments a test client client,
    a token from the hr_token fixture, an ad object from the Ad factory. Checks the compliance of the status
    codes and the content of the response object.
    """
    expected_response: Dict[str, Any] = {
        "id": 1,
        "name": "test",
        "owner": User.objects.all()[1].id,
        "items": [ad.id]
    }

    data: Dict[str, Any] = {"name": "test", "items": [ad.id]}

    response = client.post(
        "/selection/create/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Bearer " + hr_token
    )

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_create_selection_with_out_token(client, ad: Ad) -> None:
    """
    The test_create_selection_with_out_token function is designed to check the functioning when sending
    a POST request to the application at /selection/create/ without token. Accepts as arguments a test client client
    and an ad object from the Ad factory. Checks the compliance of the status codes and the content
    of the response object.
    """
    data: Dict[str, Any] = {"name": "test", "items": [ad.id]}

    response = client.post(
        "/selection/create/",
        data,
        content_type='application/json'
    )

    assert response.status_code == 401
    assert response.data == {
        'detail': ErrorDetail(
            string='Authentication credentials were not provided.',
            code='not_authenticated'
        )}