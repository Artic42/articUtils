import pytest

from articlib import logUtils


@pytest.fixture(autouse=True)
def logTest(request):
    logUtils.logTestStart(request.node.name)
    yield
    logUtils.logTestEnd()
