from articutils.fileRemote import config


DEFAULT_MON_PATH = "~/.fileRemote"
FILE_MON_PATH = "/var/temp/fileRemote"
TEST_CONFIG_PATH = "test/files/fileRemoteConfig.yaml"

def test_config_default_creation():
    testConfig = config.Config("BadPath")
    testConfig.update_config()
    assert testConfig.refresh_rate() == 1000
    assert testConfig.monitoring_path() == DEFAULT_MON_PATH

def test_set_config_value():
    testConfig = config.Config("BadPath")
    testConfig.update_config()
    testConfig.set_config({"refreshRate":10})
    assert testConfig.refresh_rate() == 10
    assert testConfig.monitoring_path() == DEFAULT_MON_PATH

def test_read_config_from_file():
    testConfig = config.Config(path = TEST_CONFIG_PATH)
    testConfig.update_config(path = TEST_CONFIG_PATH)
    assert testConfig.refresh_rate() == 100
    assert testConfig.monitoring_path() == FILE_MON_PATH

def test_update_config():
    testConfig = config.Config("BadPath")
    testConfig.update_config()
    assert testConfig.refresh_rate() == 1000
    assert testConfig.monitoring_path() == DEFAULT_MON_PATH
    testConfig.update_config(path = TEST_CONFIG_PATH)
    assert testConfig.refresh_rate() == 100
    assert testConfig.monitoring_path() == FILE_MON_PATH

def test_singleton_behaviour():
    testConfig = config.Config("BadPath")
    testConfig.update_config()
    testConfig2 = config.Config()
    testConfig.set_config({"refreshRate":10})
    assert testConfig2.refresh_rate() == 10

def test_warning_if_no_config():
    testConfig = config.Config("BadPath")
    warnings = testConfig.read_warnings()
    assert {"code":1, "msg":"Init not ok due to no config file"} in warnings, "Error in config file not reported"
