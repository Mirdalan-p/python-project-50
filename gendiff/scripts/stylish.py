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
    print(data)
    for value in data:
        print(value)
        if not isinstance(value, list):
            for key, old, new, diff in value:
                if diff == 'equal':
                    output += f"{(indent + 2) * ' '}{key}: {data_type_check(old)}\n"
                elif diff == 'changed':
                    output += f"{indent * ' '}- {key}: {data_type_check(old)}\n{indent * ' '}+ {key}: {data_type_check(new)}\n"
                elif diff == 'deleted':
                    output += f"{indent * ' '}- {key}: {data_type_check(old)}\n"
                elif diff == 'added':
                    output += f"{indent * ' '}+ {key}: {data_type_check(new)}\n"
        else:
            output += make_stylish(value, indent + 2)
    output += '}'
    return output
