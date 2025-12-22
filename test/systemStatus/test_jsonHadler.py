import logging
import pytest
import json

from articlib import logUtils
from articutils.systemStatus import jsonHandler


log = logging.getLogger()


@pytest.fixture
def report(makeTempFolder) -> jsonHandler.JsonFile:
    assert makeTempFolder == 1
    PATH = "temp/testJson.json"
    log.info(f"Create the the json object with path {PATH}")
    report = jsonHandler.JsonFile(PATH)
    return report


def test_data_report(report):
    testData = {}
    testData["test"] = True
    assert report.writeData(testData) == 0


def test_max_size_error(report):
    large_dict = {i: i**2 for i in range(1, 1000)}
    assert report.writeData(large_dict) == 1
