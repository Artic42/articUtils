import yaml
import os
import logging
import articlib.articFileUtils as FU

# Calculates home path
HOME_PATH = os.path.expanduser("~")

# Constants
CONFIG_PATH = f"{HOME_PATH}/.config/articutils/fileRemote.yaml"

# Default values
DEFAULT_REFRESH_RATE = 1000
DEFAULT_MONITOR_PATH = f"{HOME_PATH}/.fileRemote"

log = logging.getLogger()


class Config:
    _instance = None

    def __new__(cls, path: str = CONFIG_PATH):
        if cls._instance is None:
            log.info("Create new config for the first time")
            cls._instance = super().__new__(cls)
        cls._instance._init(path=path)
        return cls._instance

    def _init(self, path: str = CONFIG_PATH) -> None:
        self.warnings = []
        log.info("Initialize config")
        if FU.fileExists(path):
            log.info(f"Config file: {CONFIG_PATH}")
            FP = open(path, "r")
            self.config = yaml.safe_load(FP)
        else:
            log.warning(f"File path {CONFIG_PATH} doesn't exist, loading default config")
            self.config = {}
            self.warnings.append(
                {"code": 1, "msg": "Init not ok due to no config file"}
            )
        self._set_defaults()
        log.info(f"Create monitoring path, {self.monitoring_path()}")
        FU.createDirectory(self.monitoring_path())

    def _set_defaults(self):
        if "refreshRate" not in self.config:
            log.warning("No refresh rate set, it will set to default")
            log.info(f"Set refresh rate to {DEFAULT_REFRESH_RATE}")
            self.config["refreshRate"] = DEFAULT_REFRESH_RATE
        if "monPath" not in self.config:
            log.warning("No monitoring path set, it will set to default")
            log.info(f"Set mointoring path to {DEFAULT_MONITOR_PATH}")
            self.config["monPath"] = DEFAULT_MONITOR_PATH

    def log(self):
        log.info("This is the config of the system")
        log.info(f"    refreshRate: {self.refresh_rate()}")
        log.info(f"    monPath: {self.monitoring_path()}")

    def refresh_rate(self) -> int:
        return int(self.config["refreshRate"])

    def monitoring_path(self) -> str:
        return self.config["monPath"]

    def update_config(self, path: str = CONFIG_PATH) -> None:
        log.info(f"Update config with path {path}")
        self._init(path=path)

    def set_config(self, newConfig: dict) -> None:
        for key in newConfig:
            log.info(f"Update {key} with {newConfig[key]}")
            self.config[key] = newConfig[key]

    def read_warnings(self) -> list[dict[str, object]]:
        readWarnings = self.warnings
        self.warnings = []
        return readWarnings

    def save_config(self, path: str = CONFIG_PATH) -> None:
        log.info("Save current to config to config file")
        log.info(f"Path to file: {path}")
        self.log()
        FP = open(path, "w")
        yaml.dump(self.config, FP)
        FP.close()
