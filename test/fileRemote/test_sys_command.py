from articutils.fileRemote import sys_command
from articutils.fileRemote import config
from unittest.mock import patch

TEST_CONFIG_PATH = "test/files/fileRemoteConfig.yaml"


@patch('os.system')
def test_reboot_command_executes(mock_get):
    conf = config.Config()
    conf.update_config(TEST_CONFIG_PATH)
    open(conf.monitoring_path() + "/REBOOT", 'w')
    sys_command.monitor()
    mock_get.assert_called_once_with("sudo reboot")
