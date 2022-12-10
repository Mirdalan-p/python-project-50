from gendiff.parser import make_parse
from gendiff.formatters.formatter import make_formatted


def generate_diff(filepath_1, filepath_2, formatter='stylish'):
    data = (make_parse(filepath_1), make_parse(filepath_2))
    return make_formatted(data, formatter)
