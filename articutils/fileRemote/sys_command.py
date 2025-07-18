import os

from articutils.fileRemote import config
from articlib.articFileUtils import fileExists
from articlib.articFileUtils import deleteFile

conf = config.Config()
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
    os.system("sudo reboot")


def update():
    os.system("sudo apt update && sudo apt upgrade -y")
