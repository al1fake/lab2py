from json_parser import JsonParser
from toml_parser import TomlParser
from pickle_parser import PickleParser
from yaml_parser import YamlParser


class Factory():

    @staticmethod
    def factory(typename):
        if typename == 'Json':
            return JsonParser()
        elif typename == 'Toml':
            return TomlParser()
        elif typename == 'Pickle':
            return PickleParser()
        elif typename == 'Yaml':
            return YamlParser()
