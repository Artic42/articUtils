import pytest
from freezegun import freeze_time
from unittest.mock import patch
from typing import Any
from articutils.systemStatus import fastReport
from articutils.systemStatus import config
from articlib.jsonHandler import JsonFile


TEST_PATH = "test/files/systemStatusConfig.yaml"

class FakeVM:
    total = 7.54 * (1024**3)
    used = 4.91 * (1024**3)
    percent = 9.95


@pytest.fixture()
def psutil_cpu_mock():
    with patch("psutil.cpu_percent", return_value=[50.0, 25.0]):
        yield 1

@pytest.fixture()
def psutil_ram_mock():
    with patch("psutil.virtual_memory", return_value=FakeVM()):
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

def readFastReport() -> dict[str, Any]:
    file = JsonFile("/tmp/systemStatus/fastReport.json",read=True)
    assert 0 == file.readData()
    return file.content
    

@freeze_time("2025-12-16 13:02:22")
def test_header(fastReportInstance):
    fastReportInstance.report()
    content = readFastReport()
    assert content["type"] == "fastReport"
    assert content["month"] == 12
    assert content["year"] == 2025
    assert content["day"] == 16
    assert content["hour"] == 13
    assert content["minute"] == 2
    assert content["second"] == 22

def test_cpu_usage(fastReportInstance, psutil_cpu_mock):
    assert psutil_cpu_mock == 1
    fastReportInstance.report()
    content = readFastReport()
    assert content["data"]["cpu"]["cpu0"] == 50.0
    assert content["data"]["cpu"]["cpu1"] == 25.0

def test_ram_usage(fastReportInstance, psutil_ram_mock):
    assert psutil_ram_mock == 1
    fastReportInstance.report()
    content = readFastReport()
    assert content["data"]["ram"]["total"] == 7.54
    assert content["data"]["ram"]["used"] == 4.91
    assert content["data"]["ram"]["percent"] == 9.95


    




