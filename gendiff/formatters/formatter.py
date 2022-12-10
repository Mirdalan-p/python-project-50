from gendiff.formatters import get_plain, get_json, get_stylish
from gendiff.scripts.make_diff import get_tree


def make_formatted(data, formatter):
    if formatter == 'plain':
        return get_plain.make_plain(get_tree(data))
    elif formatter == 'json':
        return get_json.make_json(get_tree(data))
    else:
        return get_stylish.make_stylish(get_tree(data))