import pytest

from searchApi.app import create_app


@pytest.yield_fixture(scope="session")
def app():
    """
    Setup our flask test app, this only gets executed once.

    :return: Flask app
    """
    # params = {"DEBUG": False, "TESTING": True, "WTF_CSRF_ENABLED": False}

    _app = create_app("config.settings_test")

    # Establish an application context before running the tests.
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.yield_fixture(scope="function")
def client(app):
    """
    Setup an app client, this gets executed for each test function.

    :param app: Pytest fixture
    :return: Flask app client
    """
    yield app.test_client()


# http://pythontesting.net/framework/pytest/pytest-run-tests-using-particular-fixture/
# conftest.py


def pytest_collection_modifyitems(items, config):
    fixture_name = config.option.usesfixture
    if fixture_name is not None:
        selected_items = []
        deselected_items = []

        for item in items:
            if fixture_name in getattr(item, "fixturenames", ()):
                selected_items.append(item)
            else:
                deselected_items.append(item)
        config.hook.pytest_deselected(items=deselected_items)
        items[:] = selected_items


def pytest_addoption(parser):
    parser.addoption(
        "--usesfixture",
        action="store",
        default=None,
        help="just run tests that use a particular fixture",
    )


@pytest.fixture
def live():
    return "live"


@pytest.fixture
def mock():
    return "mock"
