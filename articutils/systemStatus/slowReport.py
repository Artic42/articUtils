import docker
import psutil
from typing import Any

from articutils.systemStatus import config
from articlib import jsonHandler


class SlowReport:
    def __init__(self):
        self.config = config.SystemStatusConfig()
        reportPath = self.config.report_path() + "slowReport.json"
        self.jsonFile = jsonHandler.JsonFile(reportPath,
                                             type="slowReport",
                                             write=True)
        self.dockerClient = docker.from_env()

    def _images(self) -> list[str]:
        imageNames = []
        imagesList = self.dockerClient.images.list()
        for image in imagesList:
            imageNames.append(image.tags[0])
        return imageNames

    def _conatainers(self) -> dict[str, Any]:
        containers: dict[str, Any] = {}
        rawData = self.dockerClient.containers.list()
        for entry in rawData:
            if entry.name == None:
                name: str = entry.attrs["Config"]["Image"]
            else:
                name: str = entry.name
            image = entry.attrs["Config"]["Image"]
            status = entry.attrs["State"]["Status"]
            ports = entry.attrs["NetworkSettings"]["Ports"]
            containers[name]["image"] = image
            containers[name]["status"] = status
            containers[name]["ports"] = ports
        return containers

    def _diskUsage(self) -> list[dict[str, Any]]:
        partitions = psutil.disk_partitions()
        result = []
        for p in partitions:
            usage = psutil.disk_usage(p.mountpoint)
            result.append({
                "mount_point": p.mountpoint,
                "total_gb": round(usage.total / (1024**3), 2),
                "used_percent": usage.percent})

        return result

    def report(self) -> None:
        data: dict[str, Any] = {}
        data["dockerImages"] = self._images()
        data["dockerContainer"] = self._conatainers()
        data["diskUsage"] = self._diskUsage()
        self.jsonFile.writeData(data)
