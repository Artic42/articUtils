import yaml
import os
from articlib import articFileUtils as FU

# Calculates home path
HOME_PATH = os.path.expanduser("~")

# Constants
CONFIG_PATH = f"{HOME_PATH}/.config/articutils/fileRemote.yaml"


class Config:
    _instance = None

    def __new__(cls, path: str = CONFIG_PATH):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        cls._instance._init(path=path)
        return cls._instance

    def _init(self, path: str = CONFIG_PATH) -> None:
        self.warnings = []
        if FU.fileExists(path):
            FP = open(path, "r")
            self.config = yaml.safe_load(FP)
        else:
            self.config = {}
            self.warnings.append(
                {"code": 1, "msg": "Init not ok due to no config file"}
            )
        self._set_defaults()
        FU.createDirectory(self.report_path())

    def _set_defaults(self) -> None:
        pass

    def refresh_rate_fast(self) -> int:
        return int(self.config["refreshRateFast"])

    def report_path(self) -> str:
        return self.config["reportPath"]
