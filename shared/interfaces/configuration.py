from abc import ABC, abstractmethod

from shared.models.appsection import  AppSection


class Configuration(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_app_section(self) -> AppSection:
        pass

