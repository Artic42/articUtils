import psutil
from typing import Any

from articutils.systemStatus import config
from articlib import jsonHandler


class Fast:
    def __init__(self):
        self.config = config.SystemStatusConfig()
        reportPath = self.config.report_path() + "fastReport.json"
        self.jsonFile = jsonHandler.JsonFile(reportPath,
                                             type="fastReport",
                                             write=True)
        psutil.cpu_percent()

    def _cpu(self) -> dict[str, Any]:
        usage: list[float] = psutil.cpu_percent(percpu=True)
        cpu = {}
        for core in range(len(usage)):
            cpu["cpu" + str(core)] = usage[core]
        return cpu

    def _ram(self) -> dict[str, Any]:
        mem = psutil.virtual_memory()
        ram = {}
        ram["total"] = round(mem.total / (1024**3), 2)
        ram["used"] = round(mem.used / (1024**3), 2)
        ram["percent"] = mem.percent
        return ram

    def _temperature(self) -> dict[str, Any]:
        temps = psutil.sensors_temperatures()
        temperature = {}
        if "cpu_thermal" in temps:
            temperature["core"] = temps["cpu_thermal"][0].current
        return temperature

    def report(self) -> None:
        data: dict[str, Any] = {}
        data["cpu"] = self._cpu()
        data["ram"] = self._ram()
        data["temperature"] = self._temperature()
        self.jsonFile.writeData(data)
