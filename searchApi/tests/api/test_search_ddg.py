import pytest
from flask import url_for
import json
from searchApi.blueprints import mockdata

# print(mockdata.mockDataKittens)
# print(mockdata.mockDataCats)
# print(mockdata.mockDataCars)


class TestSearchDDG(object):
    def test_ddg_api(self, client, live):
        """ ddg api should respond with a success 200. """
        response = client.get(url_for("search.ddg"))
        assert response.status_code == 200


# --- DDG search API testing
@pytest.mark.parametrize(
    ("query", "message"),
    (
        ("cats", b'{"message": "ERROR: not yet supported"}'),
        ("cars", b'{"message": "ERROR: not yet supported"}'),
        ("kittens", b'{"message": "ERROR: not yet supported"}'),
    ),
)
def test_ddg_search_live(client, query, message, live):
    response = client.get("/search/ddg?q=" + query)
    assert message in response.data


@pytest.mark.parametrize(
    ("query", "message"),
    [
        ("cats", b'{"message": "ERROR: not yet supported"}'),
        ("cars", b'{"message": "ERROR: not yet supported"}'),
        ("kittens", b'{"message": "ERROR: not yet supported"}'),
    ],
    ids=["cats", "cars", "kittens"],
)
def test_ddg_search_mock(client, query, message, mock):
    response = client.get("/search/ddg?q=" + query + "&mock=1")
    assert message in response.data
