from json_parser import JsonParser


class Factory():

    @staticmethod
    def factory(typename):
        if typename == 'Json':
            return JsonParser()
