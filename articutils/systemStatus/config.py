import yaml
import os
import articlib.articFileUtils as FU

# Calculates home path
HOME_PATH = os.path.expanduser("~")

# Constants
CONFIG_PATH = f"{HOME_PATH}/.config/articutils/fileRemote.yaml"


class SystemStatusConfig:
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
        if "reportPath" not in self.config:
            self.config["reportPath"] = f"{HOME_PATH}/.systemStatus"
        if "refreshRateFast" not in self.config:
            self.config["refreshRateFast"] = 10
        if "refreshRateSlow" not in self.config:
            self.config["refreshRateSlow"] = 1000

    def refresh_rate_fast(self) -> int:
        return int(self.config["refreshRateFast"])

    def refresh_rate_slow(self) -> int:
        return int(self.config["refreshRateSlow"])

    def report_path(self) -> str:
        return self.config["reportPath"]

    def update_config(self, path: str = CONFIG_PATH) -> None:
        self._init(path=path)

    def set_config(self, newConfig: dict) -> None:
        for key in newConfig:
            self.config[key] = newConfig[key]

    def read_warnings(self) -> list[dict[str, object]]:
        readWarnings = self.warnings
        self.warnings = []
        return readWarnings

    def save_config(self, path: str = CONFIG_PATH) -> None:
        FP = open(path, "w")
        yaml.dump(self.config, FP)
        FP.close()
