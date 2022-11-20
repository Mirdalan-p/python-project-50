from gendiff.scripts.make_diff import generate_diff


def data_type_check(value):
    if isinstance(value, bool):
        if value is None:
            return 'null'
        else:
            return str(value).lower()
    else:
        return value

def make_stylish(data, indent=2):
    output = "{\n"
    for key, old, new, diff in data:
        if not isinstance(key, list):
            if diff == 'equal':
                output += f"{(indent + 2) * ' '}{key}: {data_type_check(old)}\n"
            elif diff == 'changed':
                output += f"{indent * ' '}- {key}: {data_type_check(old)}\n{indent * ' '}+ {key}: {data_type_check(new)}\n"
            elif diff == 'deleted':
                output += f"{indent * ' '}- {key}: {data_type_check(old)}\n"
            elif diff == 'added':
                output += f"{indent * ' '}+ {key}: {data_type_check(new)}\n"
        elif isinstance(key, list):
            return make_stylish(key, indent + 2)
    output += '}'
    return output
