import os

from articutils.fileRemote import config
from articlib.articFileUtils import fileExists
from articlib.articFileUtils import deleteFile

conf = config.Config()

def monitor():
    if fileExists(conf.monitoring_path() + "/REBOOT"):
        deleteFile(conf.monitoring_path() + "/REBOOT")
        reboot()

def reboot():
    os.system("sudo reboot")
