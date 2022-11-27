from gendiff.scripts.make_diff import generate_diff
from gendiff.scripts.make_diff import data_type_check

import itertools


def is_dict(value, level, separator= '  '):
    output =''
    if isinstance(value, dict):
        for key in value:
            output += f"{separator * (level + 2)}{key}: {is_dict(value[key], level + 2)}\n"
        return "{\n" + f"{output}{level * separator}" + "}"
    else:
        return value


def get_sign(data):
    result = ()
    if data == 'changed':
        result = ('-', "+")
    elif data == 'deleted':
        result = ('-')
    elif data == 'added':
        result = ('+')
    elif data == 'equal':
        result = (' ')
    i = iter(result)
    return i


def make_stylish(data, level=0, separator= '  '):
    output = '{\n'
    for element in data:
        key, tree, diff = element
        if not isinstance(tree, list):
            sign = get_sign(diff)
            old = tree[0]
            new = tree[1]
            if diff == 'added':
                output += f"{separator * (level + 1)}{next(sign)} {key}: {is_dict(new, level + 2)}\n"
            elif diff == 'deleted':
                output += f"{separator * (level + 1)}{next(sign)} {key}: {is_dict(old, level + 2)}\n"
            elif diff == 'equal':
                output += f"{separator * (level + 1)}{next(sign)} {key}: {is_dict(old, level + 2)}\n"
            elif diff == 'changed':
                output += f"{separator * (level + 1)}{next(sign)} {key}: {is_dict(old, level + 2)}\n"\
                    f"{separator * (level + 1)}{next(sign)} {key}: {is_dict(new, level)}\n"

        else:
            key, values, diff = element
            sign = get_sign(diff)
            output += f"{separator * (level + 1)}{next(sign)} {key}: {make_stylish(values, level + 2)}\n"
    
    
    
    output += level * separator + "}"
    return output
