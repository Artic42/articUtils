from articutils.fileRemote import sys_command
from articutils.fileRemote import config
from unittest.mock import patch

TEST_CONFIG_PATH = "test/files/fileRemoteConfig.yaml"

def test_reboot_command_executes():
    conf = config.Config()
    conf.update_config(TEST_CONFIG_PATH)
    mock_system = patch("os.system")
    open(conf.monitoring_path() + "/REBOOT", 'w')
    sys_command.monitor()
    mock_system.assert_called_once_with("sudo reboot")
