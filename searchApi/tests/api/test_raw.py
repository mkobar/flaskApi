import pytest
from flask import url_for
import json
from searchApi.blueprints import mockdata

# print(mockdata.mockDataKittens)
# print(mockdata.mockDataCats)
# print(mockdata.mockDataCars)


class TestRaw(object):
    def test_google_raw(self, client, live):
        """ google raw should respond with a success 200. """
        response = client.get(url_for("raw.googleRaw") + "?q=test")
        assert response.status_code == 200

    def test_ddg_raw(self, client, live):
        """ ddg api should respond with a success 200. """
        response = client.get(url_for("raw.ddgRaw"))
        assert response.status_code == 200

    def test_bing_raw(self, client, live):
        """ bing api should respond with a success 200. """
        response = client.get(url_for("raw.bingRaw"))
        assert response.status_code == 200

    def test_multi_raw(self, client, live):
        """ multi-engine api should respond with a success 200. """
        response = client.get(url_for("raw.multipleEnginesRaw"))
        assert response.status_code == 200


# --- Google Raw API testing
@pytest.mark.parametrize(
    ("query", "message"),
    [
        # ('cats', '{"message": "mocked"}'),
        ("cats", mockdata.mockDataCatsHtml),
        # ('cars', '{"message": "mocked"}'),
        ("cars", mockdata.mockDataCarsHtml),
        # ('kittens', b'{"message": "mocked"}'),
        ("kittens", mockdata.mockDataKittensHtml),
        # ('other', {"message": "mocked"}),
        ("other", mockdata.mockDataHtml),
    ],
    ids=["cats", "cars", "kittens", "other"],
)
def test_google_raw_mock(client, query, message, mock):
    response = client.get("/raw/google?q=" + query + "&mock=1")

    # mockResponse = json.loads(response.data.decode('utf-8'))
    mockResponse = response.data
    # dicMessage = json.load(message)

    # assert message in response.data
    # assert dicMessage == response.data
    # assert message in mockResponse
    assert message == mockResponse
    # assert message == response.data


def test_google_raw_blocked(client, mock):
    response = client.get("/raw/google?q=" + "blocked" + "&blocked=1")

    mockResponse = json.loads(response.data.decode("utf-8"))
    # assert 'BLOCKED' in mockResponse
    assert {"message": "ERROR: we have been BLOCKED"} == mockResponse


# --- DDG Raw API testing


@pytest.mark.parametrize(
    ("query", "message"),
    (
        ("cats", b'{"message": "ERROR: not yet supported"}'),
        ("cars", b'{"message": "ERROR: not yet supported"}'),
        ("kittens", b'{"message": "ERROR: not yet supported"}'),
    ),
)
def test_ddg_raw_mock(client, query, message, mock):
    response = client.get("/raw/ddg?q=" + query + "&mock=1")
    assert message in response.data


# --- Bing Raw API testing
@pytest.mark.parametrize(
    ("query", "message"),
    (
        ("cats", b'{"message": "ERROR: not yet supported"}'),
        ("cars", b'{"message": "ERROR: not yet supported"}'),
        ("kittens", b'{"message": "ERROR: not yet supported"}'),
    ),
)
def test_bing_raw_mock(client, query, message, mock):
    response = client.get("/raw/bing?q=" + query + "&mock=1")
    assert message in response.data


# --- Multi Raw API testing
@pytest.mark.parametrize(
    ("query", "message"),
    (
        ("cats", b'{"message": "ERROR: not yet supported"}'),
        ("cars", b'{"message": "ERROR: not yet supported"}'),
        ("kittens", b'{"message": "ERROR: not yet supported"}'),
    ),
)
def test_multi_raw_mock(client, query, message, mock):
    response = client.get("/raw/multi?q=" + query + "&mock=1")
    assert message in response.data
