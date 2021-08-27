from my_parser import Parser
from factory import Factory


def gettype(typename):
    parser = Parser()
    if typename == 'Json':
        parser = Factory.factory("Json")
    elif typename == 'Toml':
        parser = Factory.factory("Toml")
    elif typename == 'Pickle':
        parser = Factory.factory("Pickle")
    elif typename == 'Yaml':
        parser = Factory.factory("Yaml")
    return parser


def sum(n1, n2):
    return n1 + n2


def test_output():
    return 'Hello, World!'


def main():

    # function to json
    gettype("Json").dump(sum, "./func.json")
    f = gettype("Json").load('func.json')
    print(f(10, 11))

    # function to json and back
    gettype("Json").dump(test_output, 'func1.json')
    f = gettype("Json").load('func1.json')
    print(f())

    # json to toml
    gettype("Toml").dump(gettype("Json").load("./func.json"), "./func.toml")
    f = gettype("Toml").load('func.toml')
    print(f(55, 15))

    # pickle test
    gettype("Pickle").dump(sum, "func.pickle")
    f = gettype("Pickle").load("func.pickle")
    print(f(10, 14))

    # yaml test
    gettype("Yaml").dump(sum, "func.yaml")
    f = gettype("Yaml").load("func.yaml")
    print(f(50, 2134123))


if __name__ == '__main__':
    main()
