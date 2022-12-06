def complex_check(value):  # Проверка на вложенность
    bools_ = ['null', 'true', 'false']
    if value in bools_ or isinstance(value, int):
        return value
    elif isinstance(value, dict):
        return '[complex value]'
    else:
        return f"'{value}'"


def make_string(data):  # Сборка строки в зависимости от значения дифа
    values = data[1]
    diff = data[2]
    if diff == 'added':
        return f" was added with value: {complex_check(values[1])}"
    elif diff == 'deleted':
        return " was removed"
    elif diff == 'changed':
        return f" was updated. From {complex_check(values[0])} to "\
            f"{complex_check(values[1])}"


def make_output(tree, path=''):
    output = ''
    for element in tree:
        key, values, diff = element
        if isinstance(values, list):
            output += make_output(values, path + f"{key}.")
        else:
            if diff != 'equal':
                output += '\n' + f"Property '{path}{key}'"\
                    f"{make_string(element)}"

    return output


def make_plain(tree):
    return make_output(tree).strip()
