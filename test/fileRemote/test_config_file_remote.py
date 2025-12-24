import os
import logging
from articutils.fileRemote import config
from articlib import articFileUtils as FU

HOME_PATH = os.path.expanduser("~")

DEFAULT_MON_PATH = f"{HOME_PATH}/.fileRemote"
FILE_MON_PATH = "/tmp/fileRemote"
TEST_CONFIG_PATH = "test/files/fileRemoteConfig.yaml"

log = logging.getLogger()


def test_config_default_creation():
    log.info("===================================================")
    log.info("  Default config creation test")
    log.info("===================================================")
    testConfig = config.Config("BadPath")
    testConfig.update_config()
    assert testConfig.refresh_rate() == 1000
    assert testConfig.monitoring_path() == DEFAULT_MON_PATH
    log.info("===================================================")
    log.info("  Test finished")
    log.info("===================================================")
    log.info("")
    log.info("")


def test_set_config_value():
    log.info("===================================================")
    log.info("  Test setting config value")
    log.info("===================================================")
    testConfig = config.Config("BadPath")
    testConfig.update_config()
    testConfig.set_config({"refreshRate": 10})
    assert testConfig.refresh_rate() == 10
    assert testConfig.monitoring_path() == DEFAULT_MON_PATH
    log.info("===================================================")
    log.info("  Test finished")
    log.info("===================================================")
    log.info("")
    log.info("")


def test_read_config_from_file():
    log.info("===================================================")
    log.info("  Test read of config file")
    log.info("===================================================")
    testConfig = config.Config(path=TEST_CONFIG_PATH)
    testConfig.update_config(path=TEST_CONFIG_PATH)
    assert testConfig.refresh_rate() == 10
    assert testConfig.monitoring_path() == FILE_MON_PATH
    log.info("===================================================")
    log.info("  Test finished")
    log.info("===================================================")
    log.info("")
    log.info("")


def test_update_config():
    log.info("===================================================")
    log.info("  Test config update")
    log.info("===================================================")
    testConfig = config.Config("BadPath")
    testConfig.update_config()
    assert testConfig.refresh_rate() == 1000
    assert testConfig.monitoring_path() == DEFAULT_MON_PATH
    testConfig.update_config(path=TEST_CONFIG_PATH)
    assert testConfig.refresh_rate() == 10
    assert testConfig.monitoring_path() == FILE_MON_PATH
    log.info("===================================================")
    log.info("  Test finished")
    log.info("===================================================")
    log.info("")
    log.info("")


def test_singleton_behaviour():
    log.info("===================================================")
    log.info("  Test singleton behaviour")
    log.info("===================================================")
    testConfig = config.Config("BadPath")
    testConfig.update_config()
    testConfig2 = config.Config()
    testConfig.set_config({"refreshRate": 10})
    assert testConfig2.refresh_rate() == 10
    log.info("===================================================")
    log.info("  Test finished")
    log.info("===================================================")
    log.info("")
    log.info("")


def test_warning_if_no_config():
    log.info("===================================================")
    log.info("  Test for warning if there is no config")
    log.info("===================================================")
    testConfig = config.Config("BadPath")
    warnings = testConfig.read_warnings()
    assert {
        "code": 1,
        "msg": "Init not ok due to no config file",
    } in warnings, "Error in config file not reported"
    log.info("===================================================")
    log.info("  Test finished")
    log.info("===================================================")
    log.info("")
    log.info("")


def test_creation_of_folder():
    log.info("===================================================")
    log.info("  Folder creation test")
    log.info("===================================================")
    if os.path.isdir(FILE_MON_PATH):
        log.info(f"Delete folder {FILE_MON_PATH}")
        FU.deleteDirectory(FILE_MON_PATH)
    config.Config(path=TEST_CONFIG_PATH)
    assert os.path.isdir(FILE_MON_PATH)
    log.info("===================================================")
    log.info("  Test finished")
    log.info("===================================================")
    log.info("")
    log.info("")
