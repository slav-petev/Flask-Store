from configparser import ConfigParser

from shared.interfaces.configuration import Configuration
from shared.models.appsection import AppSection


class IniConfiguration(Configuration):
    def __init__(self):
        super().__init__()
        self.parser = ConfigParser()
        self.parser.read("config.ini")

    def get_app_section(self) -> AppSection:
        return AppSection(self.parser.getint("App", "Port"),
                          self.parser.getboolean("App", "Debug"))
