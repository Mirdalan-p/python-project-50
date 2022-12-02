def complex_check(value):  # Проверка на вложенность
    if value == 'null' or value == 'true' or value == 'false':
        return value
    elif isinstance(value, dict):
        return '[complex value]'
    else:
        return f"'{value}'"


def make_string(data):  # Сборка строки в зависимости от значения дифа
    values = data[1]
    diff = data[2]
    if diff == 'added':
        return f" was added with value: {complex_check(values[1])}\n"
    elif diff == 'deleted':
        return " was removed\n"
    elif diff == 'changed':
        return f" was updated. From {complex_check(values[0])}"\
            f" to {complex_check(values[1])}\n"


def make_plain(tree, path=''):
    output = ''
    for element in tree:
        key, values, diff = element
        if isinstance(values, list):
            output += make_plain(values, path + f"{key}.")
        else:
            if diff != 'equal':
                output += f"Property '{path}{key}'{make_string(element)}"

    return output
