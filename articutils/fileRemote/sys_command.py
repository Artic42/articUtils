import os
import logging

from articutils.fileRemote import config
from articlib.articFileUtils import fileExists
from articlib.articFileUtils import deleteFile

conf = config.Config()
log = logging.getLogger()
REBOOT_FILE_PATH = conf.monitoring_path() + "/REBOOT"
UPDATE_FILE_PATH = conf.monitoring_path() + "/UPDATE"


def monitor():
    if fileExists(REBOOT_FILE_PATH):
        deleteFile(REBOOT_FILE_PATH)
        reboot()
    if fileExists(UPDATE_FILE_PATH):
        deleteFile(UPDATE_FILE_PATH)
        update()


def reboot():
    log.info("Reboot system send")
    os.system("sudo reboot")


def update():
    log.info("Update system started")
    updateDebian()


def updateDebian():
    os.system("sudo apt update && sudo apt upgrade -y")
