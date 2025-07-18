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
        FU.createDirectory(self.monitoring_path())

    def _set_defaults(self):
        if "refreshRate" not in self.config:
            self.config["refreshRate"] = 1000
        if "monPath" not in self.config:
            self.config["monPath"] = f"{HOME_PATH}/.fileRemote"

    def refresh_rate(self) -> int:
        return int(self.config["refreshRate"])

    def monitoring_path(self) -> str:
        return self.config["monPath"]

    def update_config(self, path: str = CONFIG_PATH) -> None:
        self._init(path=path)

    def set_config(self, newConfig: dict) -> None:
        for key in newConfig:
            self.config[key] = newConfig[key]

    def read_warnings(self) -> list[str]:
        readWarnings = self.warnings
        self.warnings = []
        return readWarnings

    def save_config(self, path: str = CONFIG_PATH) -> None:
        FP = open(path, "w")
        yaml.dump(self.config, FP)
        FP.close()
