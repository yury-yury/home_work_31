from typing import Dict, Any

import pytest
from rest_framework.exceptions import ErrorDetail

from ads.models import Ad


@pytest.mark.django_db
def test_detail_ad(client, ad: Ad, hr_token: str) -> None:
    """
    The test_detail_ad function is designed to check the functioning when sending a GET request to the application
    at /ad/<int: pk>/ with valid data, It takes as arguments the test client client, the hr_token fixture
    and the ad object from the Ad factory. Checks the compliance of the status codes and the content
    of the response object.
    """
    expected_response: Dict[str, Any] = {
        "id": ad.id,
        "name": ad.name,
        "description": ad.description,
        "author": ad.author.username,
        "price": "100",
        "is_published": "FALSE",
        "category": ad.category.name,
        'image': None
    }

    response = client.get(
        f"/ad/{ad.pk}/",
        HTTP_AUTHORIZATION="Bearer " + hr_token
    )

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_detail_ad_with_out_token(client, ad: Ad) -> None:
    """
    The test_detail_ad_with_out_token function is designed to check the functioning when sending a GET request
    to the application at /ad/<int: pk>/ with unvalid data, It takes as arguments the test client client
    and the ad object from the Ad factory. Checks the compliance of the status codes and the content
    of the response object.
    """
    response = client.get(f"/ad/{ad.pk}/")

    assert response.status_code == 401
    assert response.data == {
        'detail': ErrorDetail(
            string='Authentication credentials were not provided.',
            code='not_authenticated'
        )}
