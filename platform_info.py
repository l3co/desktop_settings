"""
This class is a wrapper of the module platform.
Platform module is a builtin module if you need more information check
the official documentation
"""

import platform
from abc import ABC, abstractmethod

import psutil


class Info(ABC):

    @abstractmethod
    def json(self) -> dict: ...


class PlatformInfo(Info):
    def __init__(self):
        self.__node = platform.node()
        self.__machine = platform.machine()
        self.__processor = platform.processor()
        self.__platform = platform.platform()
        self.__system = platform.system()
        self.__release = platform.release()
        self.__version = platform.version()

    @property
    def node(self):
        return self.__node

    @property
    def machine(self):
        return self.__machine

    @property
    def processor(self):
        return self.__processor

    @property
    def platform(self):
        return self.__platform

    @property
    def system(self):
        return self.__system

    @property
    def release(self):
        return self.__release

    @property
    def version(self):
        return self.__version

    def json(self):
        return {
            'node': self.__node,
            'machine': self.__machine,
            'processor': self.__processor,
            'platform': self.__platform,
            'system': self.__system,
            'version': self.__version
        }


class CoreSettings(Info):

    def __init__(self):
        self.__physical_cores = psutil.cpu_count(logical=False)
        self.__logical_cores = psutil.cpu_count(logical=True)

    @property
    def physical_cores(self):
        return self.__physical_cores

    @property
    def logical_cores(self):
        return self.__logical_cores

    def json(self):
        return {
            'physical_cores': self.__physical_cores,
            'logical_cores': self.__logical_cores
        }


class CoreFrequency(Info):

    def __init__(self):
        self.__cpu_freq_current = psutil.cpu_freq().current
        self.__cpu_freq_min = psutil.cpu_freq().min
        self.__cpu_freq_max = psutil.cpu_freq().max
        self.__core_percent_utilization = psutil.cpu_percent(interval=1)
        self.__each_core_percent_utilization = psutil.cpu_percent(interval=1, percpu=True)

    @property
    def cpu_freq_current(self):
        return self.__cpu_freq_current

    @property
    def cpu_freq_min(self):
        return self.__cpu_freq_min

    @property
    def cpu_freq_max(self):
        return self.__cpu_freq_max

    @property
    def core_percent_utilization(self):
        return self.__core_percent_utilization

    @property
    def each_core_percent_utilization(self):
        return self.__each_core_percent_utilization

    def json(self) -> dict:
        return {
            'cpu_freq_current': self.__cpu_freq_current,
            'cpu_freq_min': self.__cpu_freq_min,
            'cpu_freq_max': self.__cpu_freq_max,
            'core_percent_utilization': self.__core_percent_utilization,
            'each_core_percent_utilization': self.__each_core_percent_utilization
        }


class MemorySettings(Info):

    def __init__(self):
        # In GIGABYTE
        self.__ram_installed = round(psutil.virtual_memory().total / 1000000000, 2)
        self.__available_ram = round(psutil.virtual_memory().available / 1000000000, 2)
        self.__used_ram = round(psutil.virtual_memory().used / 1000000000, 2)
        # Percent
        self.__ram_usage = psutil.virtual_memory().percent

    @property
    def ram_installed(self):
        return self.__ram_installed

    @property
    def available_ram(self):
        return self.__available_ram

    @property
    def used_ram(self):
        return self.__used_ram

    @property
    def ram_usage(self):
        return self.__ram_usage

    def json(self) -> dict:
        return {
            'ram_installed': self.__ram_installed,
            'available_ram': self.__available_ram,
            'used_ram': self.__used_ram,
            'ram_usage': self.__ram_usage
        }
