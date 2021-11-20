import pytest
from flask import url_for
import json
from searchApi.blueprints import mockdata

# print(mockdata.mockDataKittens)
# print(mockdata.mockDataCats)
# print(mockdata.mockDataCars)


class TestSearch(object):
    def test_google_api(self, client, live):
        """ google api should respond with a success 200. """
        response = client.get(url_for("search.google") + "?q=test")
        assert response.status_code == 200

    def test_ddg_api(self, client, live):
        """ ddg api should respond with a success 200. """
        response = client.get(url_for("search.ddg"))
        assert response.status_code == 200

    def test_bing_api(self, client, live):
        """ bing api should respond with a success 200. """
        response = client.get(url_for("search.bing"))
        assert response.status_code == 200

    def test_multi_api(self, client, live):
        """ multi-engine api should respond with a success 200. """
        response = client.get(url_for("search.multipleEngines"))
        assert response.status_code == 200


# --- Google search API testing
@pytest.mark.parametrize(
    ("query", "count"),
    [
        ("cats", 6),
        ("cars", 6),
        ("kittens", 6),
        # ('blocked', 0),
    ],
    ids=["cats", "cars", "kittens"],
)
# data returned from /search/Google is HTML
# data returned from Google Search is too variable for ==
def test_google_search_live(client, query, count, live):
    response = client.get("/search/google?q=" + query)

    # dic = json.loads(response.data)

    # assert query in dic['search_parameters']['q']
    # assert count <= len(dic['organic_results'])
    assert b"Total Results" in response.data


@pytest.mark.parametrize(
    ("query", "message", "count"),
    [("cars", b'{"message": "ERROR: not yet supported"}', 13)],
    ids=["cars"],
)
# data returned from Google Search is too variable
def NOtest_google_search_live_oneoff(client, query, message, count, live):
    response = client.get("/search/google?q=" + query)

    dic = json.loads(response.data)
    assert query in dic["search_parameters"]["q"]
    if count != len(dic["organic_results"]):
        assert count - 1 == len(dic["organic_results"])
    else:
        assert count == len(dic["organic_results"])


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
def test_google_search_mock(client, query, message, mock):
    response = client.get("/search/google?q=" + query + "&mock=1")

    # mockResponse = json.loads(response.data.decode('utf-8'))
    # mockResponse = response.data.decode('utf-8')
    mockResponse = response.data
    # print(mockResponse)

    # dicMessage = json.load(message)

    # assert message in response.data
    # assert dicMessage == response.data
    # assert message in mockResponse
    assert message == mockResponse
    # assert message == response.data


def test_google_search_blocked(client, mock):
    response = client.get("/search/google?q=" + "blocked" + "&blocked=1")

    mockResponse = json.loads(response.data.decode("utf-8"))
    # assert 'BLOCKED' in mockResponse
    assert {"message": "ERROR: we have been BLOCKED"} == mockResponse


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


# --- Bing search API testing
@pytest.mark.parametrize(
    ("query", "message"),
    (
        ("cats", b'{"message": "ERROR: not yet supported"}'),
        ("cars", b'{"message": "ERROR: not yet supported"}'),
        ("kittens", b'{"message": "ERROR: not yet supported"}'),
    ),
)
def test_bing_search_live(client, query, message, live):
    response = client.get("/search/bing?q=" + query)
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
def test_bing_search_mock(client, query, message, mock):
    response = client.get("/search/bing?q=" + query + "&mock=1")
    assert message in response.data


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
