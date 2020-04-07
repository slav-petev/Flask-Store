from injector import singleton

from shared.interfaces.configuration import Configuration
from shared.implementations.iniconfiguration import IniConfiguration


def configure(binder):
    binder.bind(Configuration, to=IniConfiguration, scope=singleton)