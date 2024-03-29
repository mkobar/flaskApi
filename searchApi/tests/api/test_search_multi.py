import pytest
from flask import url_for
import json
from searchApi.blueprints import mockdata

# print(mockdata.mockDataKittens)
# print(mockdata.mockDataCats)
# print(mockdata.mockDataCars)


class TestSearchMulti(object):
    def test_multi_api(self, client, live):
        """multi-engine api should respond with a success 200."""
        response = client.get(url_for("search.multipleEngines"))
        assert response.status_code == 200


# --- Multi search API testing
@pytest.mark.parametrize(
    ("query", "message"),
    (
        ("cats", b'{"message": "ERROR: not yet supported"}'),
        ("cars", b'{"message": "ERROR: not yet supported"}'),
        ("kittens", b'{"message": "ERROR: not yet supported"}'),
    ),
)
def test_multi_search_live(client, query, message, live):
    response = client.get("/search/multi?q=" + query)
    assert message in response.data
