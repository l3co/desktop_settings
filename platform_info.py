"""
This class is a wrapper of the module platform.
Platform module is a builtin module if you need more information check
the official documentation
"""

import platform

import psutil


class PlatformInfo:
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


class CoreSettings:

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
