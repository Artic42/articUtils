import pytest
from unittest.mock import patch
from articutils.systemStatus import fastReport
from articutils.systemStatus import config
from articlib.jsonHandler import JsonFile


TEST_PATH = "test/files/systemStatusConfig.yaml"


@pytest.fixture()
def psutil_cpu_mock():
    with patch("psutil.cpu_percent", return_value=[50.0, 25.0]):
        yield 1


@pytest.fixture()
def fastReportInstance():
    instance = fastReport.Fast()
    yield instance
    del instance


@pytest.fixture(autouse=True)
def preConfSystemStatus() -> None:
    conf = config.SystemStatusConfig()
    conf.update_config(TEST_PATH)


def test_writing_cpu(psutil_cpu_mock, fastReportInstance):
    assert psutil_cpu_mock == 1
    fastReportInstance.report()
    file = JsonFile(TEST_PATH,read=True)
    assert 0 == file.readData()


