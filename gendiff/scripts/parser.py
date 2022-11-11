import json
import yaml


def make_parse(file_path):
    data = []
    with open(file_path, 'r') as file:
        if '.json' in file_path:
            data = json.load(open(file_path))
        elif '.yaml' in file_path or '.yml' in file_path:
            data = yaml.load(file, Loader=yaml.FullLoader)
    return data
