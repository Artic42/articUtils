from articutils.fileRemote import sys_command
from articutils.fileRemote import config
from unittest.mock import patch
from articlib.articFileUtils import fileExists

TEST_CONFIG_PATH = "test/files/fileRemoteConfig.yaml"


@patch('os.system')
def test_reboot_command_executes(mock_get):
    conf = config.Config()
    conf.update_config(TEST_CONFIG_PATH)
    open(sys_command.REBOOT_FILE_PATH, 'w')
    assert fileExists(sys_command.REBOOT_FILE_PATH)
    sys_command.monitor()
    assert not fileExists(sys_command.REBOOT_FILE_PATH)
    mock_get.assert_called_once_with("sudo reboot")


@patch('os.system')
def test_update_command_executes(mock_get):
    conf = config.Config()
    conf.update_config(TEST_CONFIG_PATH)
    open(sys_command.UPDATE_FILE_PATH, 'w')
    assert fileExists(sys_command.UPDATE_FILE_PATH)
    sys_command.monitor()
    assert not fileExists(sys_command.UPDATE_FILE_PATH)
    mock_get.assert_called_once_with("sudo apt update && sudo apt upgrade -y")
