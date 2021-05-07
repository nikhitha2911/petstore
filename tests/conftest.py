import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).joinpath("..", "..").resolve()))

import pytest

from api.server import APP


@pytest.fixture
def api_client():
    APP.config["TESTING"] = True
    client = APP.test_client()
    return client



