import yaml


# Constants
CONFIG_PATH = "~/.config/articutils/fileRemote.yaml"


class Config:
    __instance = None

    @staticmethod
    def getConfig():
        if Config.__instance is None:
            Config.__instance = Config()
        return Config.__instance

    def __init__(self) -> None:
        FP = open(CONFIG_PATH, 'r')
        self.config = yaml.safe_load(FP)
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

    def update_config(self) -> None:
        self.__init__()
