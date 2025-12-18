import os
import logging

from articutils.fileRemote import config
from articlib.articFileUtils import fileExists
from articlib.articFileUtils import deleteFile
from articlib.logUtils import logFile


conf = config.Config()
UP_FILE_PATH = conf.monitoring_path() + "/UP_DOCKER_CONTAINER"
DOWN_FILE_PATH = conf.monitoring_path() + "/DOWN_DOCKER_CONTAINER"
CREATE_FILE_PATH = conf.monitoring_path() + "/CREATE_DOCKER_CONTAINER"
REMOVE_FILE_PATH = conf.monitoring_path() + "/REMOVE_DOCKER_CONTAINER"
log = logging.getLogger()


def monitor():
    if fileExists(UP_FILE_PATH):
        upContainer()
        deleteFile(UP_FILE_PATH)
    if fileExists(DOWN_FILE_PATH):
        downContainer()
        deleteFile(DOWN_FILE_PATH)
    if fileExists(CREATE_FILE_PATH):
        buildImage()
        deleteFile(CREATE_FILE_PATH)
    if fileExists(REMOVE_FILE_PATH):
        removeImage()
        deleteFile(REMOVE_FILE_PATH)


def upContainer():
    log.info("Get up container into system")
    logFile(UP_FILE_PATH)
    os.system(f"docker-compose up -d -f {UP_FILE_PATH}")


def downContainer():
    log.info("Get up container into system")
    logFile(UP_FILE_PATH)
    os.system(f"docker-compose down -d -f {DOWN_FILE_PATH}")


def buildImage():
    FP = open(CREATE_FILE_PATH, "r")
    lines = FP.readlines()
    imageName = lines[0][2:]
    log.info(f"Build image with name {imageName} with dockerfile:")
    logFile(CREATE_FILE_PATH)
    os.system(f"docker build -t {imageName} {CREATE_FILE_PATH}")


def removeImage():
    FP = open(REMOVE_FILE_PATH, "r")
    lines = FP.readlines()
    imageName = lines[0]
    log.info(f"Delete image with name {imageName}")
    os.system(f"docker rmi {imageName}")
