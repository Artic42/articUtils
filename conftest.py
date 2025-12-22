import pytest

from articlib import logUtils
from articlib import articFileUtils as FU


@pytest.fixture(autouse=True)
def logTest(request):
    logUtils.logTestStart(request.node.name)
    yield
    logUtils.logTestEnd()


@pytest.fixture
def makeTempFolder():
    if FU.directoryExists("temp") is False:
        FU.createDirectory("temp")
    yield 1
