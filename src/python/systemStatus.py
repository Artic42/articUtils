import time
import threading

from articlib.articFileUtils import fileExists
from articlib.articFileUtils import deleteFile
from articutils.systemStatus import config


conf = config.Config()


def loop():
    slowTask = threading.Thread(target=reportSlowTask)
    fastTask = threading.Thread(target=reportFastTask)
    slowTask.start()
    fastTask.start()
    fastTask.join()
    slowTask.join()
    deleteFile(conf.report_path() + "/KILL")


def reportFastTask():
    while not fileExists(conf.report_path() + "/KILL"):
        reportFast()
        time.sleep(conf.refresh_rate_fast())


def reportSlowTask():
    while not fileExists(conf.report_path() + "/KILL"):
        reportSlow()
        time.sleep(conf.refresh_rate_slow())


def reportFast():
    pass


def reportSlow():
    pass


if __name__ == "__main__":
    loop()
