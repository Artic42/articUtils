import pytest
import psutil
from unittest.mock import patch


@pytest.fixture()
def psutil_cpu_mock():
    with patch("psutil.cpu_percent", return_value=[50.0, 25.0]):
        yield 1


def test_writing_cpu(psutil_cpu_mock):
    assert psutil_cpu_mock == 1
