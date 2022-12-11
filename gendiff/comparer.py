from gendiff.formatters.formatter import make_formatted
from gendiff.parser import get_data


def generate_diff(filepath_1, filepath_2, formatter='stylish'):
    data = (get_data(filepath_1), get_data(filepath_2))
    return make_formatted(data, formatter)
