from articutils.fileRemote import sys_command
from articutils.fileRemote import config
from unittest.mock import patch
from articlib.articFileUtils import fileExists

TEST_CONFIG_PATH = "test/files/fileRemoteConfig.yaml"


@patch('os.system')
def test_reboot_command_executes(mock_get):
    conf = config.Config()
    conf.update_config(TEST_CONFIG_PATH)
    open(conf.monitoring_path() + "/REBOOT", 'w')
    assert fileExists(conf.monitoring_path() + "/REBOOT")
    sys_command.monitor()
    assert not fileExists(conf.monitoring_path() + "/REBOOT")
    mock_get.assert_called_once_with("sudo reboot")
