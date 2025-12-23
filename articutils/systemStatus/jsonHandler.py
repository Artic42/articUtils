import json
import socket
import logging
import mmap
from datetime import datetime


log = logging.getLogger()


class JsonFile:
    def __init__(self, path: str,
                 type: str = "",
                 size: int = 1024,
                 read: bool = False,
                 write: bool = False) -> None:
        self.clock = datetime.now()
        self.content = {}
        self._setHostname()
        self.read = read
        self.write = write

        if read is False and write is False:
            msg = "No mode selected at class creation"
            log.error(msg)
            raise ValueError(msg)

        if read is True and write is True:
            msg = "Both mode selected at class creation, only one allowed"
            log.error(msg)
            raise ValueError(msg)

        if type == "":
            self._setType(path)
        else:
            self._setType(type)

        self.size = size
        self.path = path

        if write is True:
            self.filePtr = open(path, "wb")
            self.filePtr.write(b"\x00" * size)
            self.filePtr.close()

        if read is True:
            self.filePtr = open(path, "r+b")
            self.filePtr.seek(size-1)
            self.filePtr.write(b"\x00")
            self.filePtr.close()

        self.filePtr = open(path, "r+b")
        self.fmap = mmap.mmap(self.filePtr.fileno(), size)

    def __del__(self) -> None:
        if hasattr(self, "fmap"):
            self.fmap.close()
        if self.read is True:
            return
        if self.write is True:
            self.bufferedWrite()

    def _setHostname(self) -> None:
        self.content["Hostname"] = socket.gethostname()

    def _setType(self, type: str) -> None:
        self.content["type"] = type

    def _setDate(self) -> None:
        self.content["year"] = int(self.clock.year)
        self.content["month"] = int(self.clock.month)
        self.content["day"] = int(self.clock.day)

    def _setTime(self) -> None:
        self.content["hour"] = int(self.clock.hour)
        self.content["minute"] = int(self.clock.minute)
        self.content["second"] = int(self.clock.second)

    def bufferedWrite(self) -> None:
        FilePtr = open(self.path, "w")
        json.dump(self.content, FilePtr, indent=4)
        FilePtr.close()

    def writeData(self, data: dict) -> int:
        if self.write is False:
            log.error("File was open without write mode and can't be written")
            return 3

        self.clock = datetime.now()
        self._setDate()
        self._setTime()
        self.content["data"] = data

        # Convert dict into bytes
        file_bytes = json.dumps(self.content, indent=4).encode()

        if len(file_bytes) > self.size:
            log.error("File too small, too much data to dump")
            return 1

        # Clear memory map
        self.fmap.seek(0)
        self.fmap.write(b"\x00" * self.size)

        # Write data
        self.fmap.seek(0)
        self.fmap.write(file_bytes)

        return 0

    def readData(self) -> int:
        if self.read is False:
            log.error("File was open without read mode and can't be read")
            return 2

        # Read the entire memory-mapped region (this IS the file)
        raw = self.fmap[:]

        # Stop at the first null byte (padding begins here)
        json_bytes = raw.split(b"\x00", 1)[0]

        # If file is empty or only padding
        if not json_bytes.strip():
            log.error("File is empty and can't be read")
            return 3

        # Decode and parse JSON
        self.content = json.loads(json_bytes.decode())
        return 0
