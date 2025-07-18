from articutils.fileRemote import docker_command
from articutils.fileRemote import config
from unittest.mock import patch
from articlib.articFileUtils import fileExists

TEST_CONFIG_PATH = "test/files/fileRemoteConfig.yaml"


@patch("os.system")
def test_up_command_executes(mock_get):
    conf = config.Config()
    conf.update_config(TEST_CONFIG_PATH)
    upCommand = f"docker-compose up -d -f {docker_command.UP_FILE_PATH}"
    open(docker_command.UP_FILE_PATH, "w")
    assert fileExists(docker_command.UP_FILE_PATH)
    docker_command.monitor()
    assert not fileExists(docker_command.UP_FILE_PATH)
    mock_get.assert_called_once_with(upCommand)


@patch("os.system")
def test_down_command_executes(mock_get):
    conf = config.Config()
    conf.update_config(TEST_CONFIG_PATH)
    downCommand = f"docker-compose down -d -f {docker_command.DOWN_FILE_PATH}"
    open(docker_command.DOWN_FILE_PATH, "w")
    assert fileExists(docker_command.DOWN_FILE_PATH)
    docker_command.monitor()
    assert not fileExists(docker_command.DOWN_FILE_PATH)
    mock_get.assert_called_once_with(downCommand)


@patch("os.system")
def test_create_command_executes(mock_get):
    conf = config.Config()
    conf.update_config(TEST_CONFIG_PATH)
    command = f"docker build -t test_image {docker_command.CREATE_FILE_PATH}"
    FP = open(docker_command.CREATE_FILE_PATH, "w")
    FP.write("# test_image")
    FP.close()
    assert fileExists(docker_command.CREATE_FILE_PATH)
    docker_command.monitor()
    assert not fileExists(docker_command.CREATE_FILE_PATH)
    mock_get.assert_called_once_with(command)


@patch("os.system")
def test_remove_command_executes(mock_get):
    conf = config.Config()
    conf.update_config(TEST_CONFIG_PATH)
    command = "docker rmi test_image"
    FP = open(docker_command.REMOVE_FILE_PATH, "w")
    FP.write("test_image")
    FP.close()
    assert fileExists(docker_command.REMOVE_FILE_PATH)
    docker_command.monitor()
    assert not fileExists(docker_command.REMOVE_FILE_PATH)
    mock_get.assert_called_once_with(command)
