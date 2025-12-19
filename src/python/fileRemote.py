import time
import logging

from articutils.fileRemote import config
from articutils.fileRemote import sys_command
from articutils.fileRemote import docker_command
from articlib.articFileUtils import fileExists
from articlib.articFileUtils import deleteFile

log = logging.getLogger()


def loop():
    conf = config.Config()
    log_start()
    while not fileExists(conf.monitoring_path() + "/KILL"):
        monitor()
        time.sleep(conf.refresh_rate() / 1000)
    deleteFile(conf.monitoring_path() + "/KILL")


def monitor():
    sys_command.monitor()
    docker_command.monitor()


def log_start():
    log.info("File remote starting")
    config.log()


if __name__ == "__main__":
    loop()
