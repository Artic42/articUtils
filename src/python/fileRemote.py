import time
from articutils.fileRemote import config
from articutils.fileRemote import sys_command
from articutils.fileRemote import docker_command
from articlib.articFileUtils import fileExists
from articlib.articFileUtils import deleteFile


def loop():
    conf = config.Config()
    while not fileExists(conf.monitoring_path() + "/KILL"):
        monitor()
        time.sleep(conf.refresh_rate() / 1000)
    deleteFile(conf.monitoring_path() + "/KILL")


def monitor():
    sys_command.monitor()
    docker_command.monitor()


if __name__ == "__main__":
    loop()
