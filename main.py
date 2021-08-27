from my_parser import Parser
from factory import Factory


def gettype(typename):
    parser = Parser()
    if typename == 'Json':
        parser = Factory.factory("Json")
    elif typename == 'Toml':
        parser = Factory.factory("Toml")
    return parser


def sum(n1, n2):
    return n1 + n2


def test_output():
    return 'Hello, World!'


def main():
    # json
    # fuction to file
    gettype("Json").dump(sum, "./func.json")

    # function to json and back

    gettype("Json").dump(test_output, 'func1.json')
    f = gettype("Json").load('func1.json')
    print(f())

    #json to toml
    gettype("Toml").dump(gettype("Json").load("./func.json"), "./func.toml")

if __name__ == '__main__':
    main()
