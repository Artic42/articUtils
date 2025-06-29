import yaml
from articlib import articFileUtils as FU

# Constants
CONFIG_PATH = "~/.config/articutils/fileRemote.yaml"


class Config:
    _instance = None

    def __new__(cls, path : str = CONFIG_PATH):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init(path = path)
        return cls._instance

    def __del__(self):
        print("Destroy instance")
        self._instance = None

    def _init(self, path : str = CONFIG_PATH) -> None:
        if FU.fileExists(path):
            FP = open(path, 'r')
            self.config = yaml.safe_load(FP)
        else:
            print(f"WARNING: File {path} doesn't exist")
            self.config = {}
        self._set_defaults()

    def _set_defaults(self):
        if "refreshRate" not in self.config:
            self.config["refreshRate"] = 1000
        if "monPath" not in self.config:
            self.config["monPath"] = "~/.fileRemote"
    
    def refresh_rate(self) -> int:
        return int(self.config["refreshRate"])

    def monitoring_path(self) -> int:
        return self.config["monPath"]

    def update_config(self, path : str = CONFIG_PATH) -> None:
        self._init(path = path)

    def set_config(self, newConfig:dict) -> None:
        for key in newConfig:
            self.config[key] = newConfig[key]

