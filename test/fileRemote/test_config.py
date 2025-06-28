from articutils.fileRemote import config


def test_config_default_creation():
    testConfig = config.Config()
    defaultMonPath = "~/.fileRemote"
    assert testConfig.refresh_rate == 1000
    assert testConfig.monitoring_path == defaultMonPath

