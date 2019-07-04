from os.path import realpath, dirname
import json
import os


def get_config(name):
    path = dirname(realpath(__file__)) + '/config/' + name + '.json'
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())


# if __name__ == "__main__":
#     print(os.getcwd())
#     print(dirname(realpath(__file__)))
#     dd = get_config('china')
#     print(dd)
#     print(type(dd))

