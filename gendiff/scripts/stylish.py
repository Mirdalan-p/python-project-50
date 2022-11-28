from gendiff.scripts.get_diff import get_sign

SEPARATOR = '  '


def is_dict(value, level):
    output = ''
    if isinstance(value, dict):
        for key in value:
            output += f"{SEPARATOR * (level + 2)}{key}:"\
                f" {is_dict(value[key], level + 2)}\n"
        return "{\n" + f"{output}{level * SEPARATOR}" + "}"
    else:
        return value


def get_string(data, level, diff):
    key, old, new, sign = data
    output = ''
    if diff == 'added':
        output += f"{SEPARATOR * (level + 1)}{next(sign)}"\
            f" {key}: {is_dict(new, level + 2)}\n"
    elif diff == 'deleted':
        output += f"{SEPARATOR * (level + 1)}{next(sign)}"\
            f" {key}: {is_dict(old, level + 2)}\n"
    elif diff == 'equal':
        output += f"{SEPARATOR * (level + 1)}{next(sign)}"\
            f" {key}: {is_dict(old, level + 2)}\n"
    elif diff == 'changed':
        output += f"{SEPARATOR * (level + 1)}{next(sign)}"\
            f" {key}: {is_dict(old, level + 2)}\n"\
            f"{SEPARATOR * (level + 1)}{next(sign)}"\
            f" {key}: {is_dict(new, level)}\n"
    return output


def make_stylish(data, level=0):
    output = '{\n'
    print(data)
    for element in data:
        key, tree, diff = element
        if not isinstance(tree, list):
            sign = get_sign(diff)
            old = tree[0]
            new = tree[1]
            data = (key, old, new, sign)
            output += get_string(data, level, diff)
        else:
            key, values, diff = element
            sign = get_sign(diff)
            output += f"{SEPARATOR * (level + 1)}{next(sign)}"\
                f" {key}: {make_stylish(values, level + 2)}\n"

    output += level * SEPARATOR + "}"
    return output
