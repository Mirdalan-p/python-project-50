
def make_path(tree):
    return ('.'.join(tree))

def complex_check(value):
    if value is 'null' or value is 'true' or value is 'false':
        return value
    elif isinstance(value, dict):
        return '[complex value]'
    else:
        return f"'{value}'"

def make_string(data):
    values = data[1]
    diff = data[2]
    if diff == 'added':
        return f" was added with value: {complex_check(values[1])}\n"
    elif diff == 'deleted':
        return f" was removed\n"
    elif diff == 'changed':
        return f" was updated from {complex_check(values[0])} to {complex_check(values[1])}\n"

def make_plain(tree, path= None):
    output = ''
    if path == None:
        path = []
    for element in tree:
        key, values, diff = element
        if diff == 'equal':
            if isinstance(values, list):
                output += make_plain(values, [key])
            else:
                output += f"Property {make_path(key)}{make_string(element)}"
        else:
            output += f"Property {make_path(key)}{make_string(element)}"

    return output
