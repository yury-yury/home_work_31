from typing import List, Dict, Any

import pytest

from ads.models import Ad
from ads.serializers import AdListSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ads_list(client) -> None:
    """
    The test_ads_list function is designed to check the functioning when sending a GET request
    to the application at /ad/. Takes the test client client as an argument.
    Checks the compliance of the status codes and the content of the response object.
    """
    ads: List[Ad] = AdFactory.create_batch(10)

    expected_response: Dict[str, Any] = {
        "count": 10,
        "next": None,
        "previous": None,
        "results": AdListSerializer(ads, many=True).data
    }
    response = client.get("/ad/")

    assert response.status_code == 200
    assert response.data == expected_response
