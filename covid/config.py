"""
Module containing configuration variables.
"""
from covid.utils.io import read_json_file


# define config class
class Config(dict):
    def __init__(self, path_to_config: str):
        config_dict = read_json_file(path_to_config)
        super(Config, self).__init__(**config_dict)
        self.__dict__ = self


class Secrets(dict):
    def __init__(self, path_to_secrets: str):
        config_dict = read_json_file(path_to_secrets)
        super(Secrets, self).__init__(**config_dict)
        self.__dict__ = self
