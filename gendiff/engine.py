from gendiff.scripts.parser import make_parse
from gendiff.formatters import get_plain, get_json, get_stylish
from gendiff.scripts.make_diff import get_tree


def generate_diff(filepath_1, filepath_2, formatter):
    data = (make_parse(filepath_1), make_parse(filepath_2))
    if formatter == 'plain':
        return get_plain.make_plain(get_tree(data))
    elif formatter == 'json':
        return get_json.make_json(get_tree(data))
    elif formatter == 'stylish':
        return get_stylish.make_stylish(get_tree(data))
