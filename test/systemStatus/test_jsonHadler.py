import logging
import pytest
import json

from articutils.systemStatus import jsonHandler


log = logging.getLogger()
PATH = "temp/testJson.json"


@pytest.fixture
def reportWrite(makeTempFolder):
    assert makeTempFolder == 1
    log.info(f"Create the the json object with path {PATH}")
    report = jsonHandler.JsonFile(PATH, type="Test", write=True)
    yield report
    del report


@pytest.fixture
def reportRead(makeTempFolder):
    assert makeTempFolder == 1
    log.info("Read file for test")
    report = jsonHandler.JsonFile(PATH, type="Test", read=True)
    yield report
    del report


def test_data_report(reportWrite, reportRead):
    testData = {}
    testData["test"] = True
    assert reportWrite.writeData(testData) == 0
    reportRead.readData()
    jsonDict = reportRead.content
    assert jsonDict["data"] == testData
    assert "year" in jsonDict
    assert "month" in jsonDict
    assert "day" in jsonDict
    assert "hour" in jsonDict
    assert "minute" in jsonDict
    assert "second" in jsonDict
    assert jsonDict["type"] == "Test"
    assert "Hostname" in jsonDict


def test_json_readable_afterFinish(makeTempFolder):
    assert makeTempFolder == 1
    file = jsonHandler.JsonFile(PATH, write=True)
    dict = {}
    dict["test"] = "test"
    file.writeData(dict)
    del file

    readFile = open(PATH, "r")
    readDict = json.load(readFile)
    assert readDict["data"] == dict


def test_read_normal_json(makeTempFolder):
    assert makeTempFolder == 1
    writeFile = open(PATH, "w")
    dict = {}
    dict["test"] = "test"
    json.dump(dict, writeFile)
    writeFile.close()

    file = jsonHandler.JsonFile(PATH, read=True)
    file.readData()
    assert dict == file.content


def test_no_mode_selected():
    with pytest.raises(ValueError) as excinfo:
        jsonHandler.JsonFile("test")
    errorMsg = "No mode selected at class creation"
    assert errorMsg in str(excinfo.value)


def test_both_modes_selected():
    with pytest.raises(ValueError) as excinfo:
        jsonHandler.JsonFile("test", read=True, write=True)
    errorMsg = "Both mode selected at class creation, only one allowed"
    assert errorMsg in str(excinfo.value)


def test_read_on_write_from(reportWrite):
    assert reportWrite.readData() == 2


def test_write_on_read_mode(reportWrite, reportRead):
    emptyDict = {}
    reportWrite.writeData(emptyDict)
    assert reportRead.writeData(emptyDict) == 3


def test_max_size_error(reportWrite):
    large_dict = {i: i**2 for i in range(1, 1000)}
    assert reportWrite.writeData(large_dict) == 1
