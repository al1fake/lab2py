from json_parser import JsonParser
from toml_parser import  TomlParser

class Factory():

    @staticmethod
    def factory(typename):
        if typename == 'Json':
            return JsonParser()
        elif typename == 'Toml':
            return TomlParser()
