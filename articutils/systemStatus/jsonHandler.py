import json
import socket
import logging
import mmap
from datetime import datetime

from articutils.systemStatus import config
from articlib.articFileUtils import fileExists


conf = config.Config()
log = logging.getLogger()


class JsonFile:
    def __init__(self, path: str, size: int = 1024) -> None:
        self.clock = datetime.now()
        self.content = {}
        self.size = size
        self.path = path
        self.filePtr = open(path, "wb")
        if fileExists(path) is False:
            self.filePtr.write(b"\x00" * size)
            self.filePtr.close()
        self.filePtr = open(path, "r+b")
        self.fmap = mmap.mmap(self.filePtr.fileno(), size)

    def _setHostname(self) -> None:
        self.content["Hostname"] = socket.gethostname()

    def _setDate(self) -> None:
        self.content["year"] = int(self.clock.year)
        self.content["month"] = int(self.clock.month)
        self.content["day"] = int(self.clock.day)

    def _setTime(self) -> None:
        self.content["hour"] = int(self.clock.hour)
        self.content["minute"] = int(self.clock.minute)
        self.content["second"] = int(self.clock.second)

    def writeData(self, data: dict) -> None:
        self.clock = datetime.now()
        self._setDate()
        self._setTime()
        self.content["data"] = data

        # Convert dict into bytes
        file_bytes = json.dumps(self.content).encode()

        if len(file_bytes) > self.size:
            log.error("File too big expected too much data")

        # Clear memory map
        self.fmap.seek(0)
        self.fmap.write(b"\x00" * self.size)

        # Write data
        self.fmap.seek(0)
        self.fmap.write(file_bytes)
