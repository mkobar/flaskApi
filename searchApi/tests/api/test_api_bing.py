import pytest
from flask import url_for
import json
from searchApi.blueprints import mockdata

# print(mockdata.mockDataKittens)
# print(mockdata.mockDataCats)
# print(mockdata.mockDataCars)


class TestApiBing(object):
    def test_bing_api(self, client, live):
        """ bing api should respond with a success 200. """
        response = client.get(url_for("api.bingApi"))
        assert response.status_code == 200


# --- Bing API testing
@pytest.mark.parametrize(
    ("query", "message"),
    (
        ("cats", b'{"message": "ERROR: not yet supported"}'),
        ("cars", b'{"message": "ERROR: not yet supported"}'),
        ("kittens", b'{"message": "ERROR: not yet supported"}'),
    ),
)
def test_bing_api_live(client, query, message, live):
    response = client.get("/api/bing?q=" + query)
    assert message in response.data


@pytest.mark.parametrize(
    ("query", "message"),
    (
        ("cats", b'{"message": "ERROR: not yet supported"}'),
        ("cars", b'{"message": "ERROR: not yet supported"}'),
        ("kittens", b'{"message": "ERROR: not yet supported"}'),
    ),
)
def test_bing_api_mock(client, query, message, mock):
    response = client.get("/api/bing?q=" + query + "&mock=1")
    assert message in response.data
