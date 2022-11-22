from gendiff.scripts.make_diff import generate_diff


def data_type_check(value):
    if value is "None":
        return 'null'
    else:
        return str(value).lower()


def make_stylish(data, indent=2):
    output = "{\n"
    print(data)
    for value in data:
        key, values, diff = value
        if not isinstance(values, list):
            old, new = values
            if diff == 'equal':
                output += f"{(indent + 2) * ' '}{key}: {data_type_check(old)}\n"
            elif diff == 'changed':
                output += f"{indent * ' '}- {key}: {data_type_check(old)}\n{indent * ' '}+ {key}: {data_type_check(new)}\n"
            elif diff == 'deleted':
                output += f"{indent * ' '}- {key}: {data_type_check(old)}\n"
            elif diff == 'added':
                output += f"{indent * ' '}+ {key}: {data_type_check(new)}\n"
        else:
            key, result, diff = value
            output += f"{indent * ' '}{key}: {make_stylish(result, indent + 2)}\n"
    
    return output + '}'
