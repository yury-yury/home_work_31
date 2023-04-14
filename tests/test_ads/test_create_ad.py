from typing import Dict, Any

import pytest
from rest_framework.exceptions import ErrorDetail

from categories.models import Category


@pytest.mark.django_db
def test_create_ad(client, hr_token: str, category: Category) -> None:
    """
    The test_create_ad function is designed to check the normal functioning when sending a POST request
    to the application at /ad/create/ with valid data. Accepts as arguments the test client client,
    the hr_token fixture and the category object from the Category factory. Checks the compliance of the status codes
    and the content of the response object.
    """
    expected_response: Dict[str, Any] = {
        "id": 1,
        "name": "test test 1",
        "description": None,
        "author": "test_user",
        "price": "100",
        "is_published": "FALSE",
        "category": category.name
    }

    data: Dict[str, Any] = {
        "name": "test test 1",
        "author": "test_user",
        "price": "100",
        "category": category.name
    }
    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Bearer " + hr_token
    )

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_create_ad_false_min_length(client, hr_token: str, category: Category) -> None:
    """
    The test_create_ad_false_min_length function is designed to check the functioning when sending a POST request
    to the application at /ad/create/ with invalid data, It takes as arguments the test client client,
    the hr_token fixture and the category object from the Category factory. Checks the compliance of the status codes
    and the content of the response object.
    """
    data: Dict[str, Any] = {
        "name": "test",
        "author": "test_user",
        "price": "100",
        "category": category.name
    }
    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Bearer " + hr_token
    )

    assert response.status_code == 400
    assert response.data == {
        'name': [ErrorDetail(
            string='Ensure this field has at least 10 characters.',
            code='min_length'
        )]}


@pytest.mark.django_db
def test_create_ad_false_is_published(client, hr_token, category):
    """
    The test_create_ad_false_is_published function is designed to check the functioning when sending a POST request
    to the application at /ad/create/ with invalid data, It takes as arguments the test client client,
    the hr_token fixture and the category object from the Category factory. Checks the compliance of the status codes
    and the content of the response object.
    """
    data: Dict[str, Any] = {
        "name": "test text 1",
        "author": "test_user",
        "price": "100",
        "category": category.name,
        "is_published": "TRUE"
    }
    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Bearer " + hr_token
    )

    assert response.status_code == 400
    assert response.data == {
        'is_published': [ErrorDetail(
            string='The value of the is_published field cannot be TRUE when creating the ad.',
            code='invalid'
        )]}

@pytest.mark.django_db
def test_create_ad_false_negative_price(client, hr_token: str, category: Category) -> None:
    """
    The test_create_ad_false_negative_price function is designed to check the functioning when sending a POST request
    to the application at /ad/create/ with invalid data, It takes as arguments the test client client,
    the hr_token fixture and the category object from the Category factory. Checks the compliance of the status codes
    and the content of the response object.
    """
    data: Dict[str, Any] = {
        "name": "test text 1",
        "author": "test_user",
        "price": "-100",
        "category": category.name
    }
    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Bearer " + hr_token
    )

    assert response.status_code == 400
    assert response.data == {
        'price': [ErrorDetail(
            string='Ensure this value is greater than or equal to 0.',
            code='min_value'
        )]}
