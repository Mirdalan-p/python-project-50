def get_difference(data):
    first, second = data
    diff = ''
    if first == second:
        diff = 'equal'
    elif first and second is None:
        diff = 'deleted'
    elif first is None and second:
        diff = 'added'
    elif first != second:
        diff = 'changed'
    return diff


def data_type_check(tree, key):
    value = ''
    if key in tree:
        if tree[key] is None:
            value = 'null'
        elif tree[key] is True:
            value = 'true'
        elif tree[key] is False:
            value = 'false'
        else:
            value = tree[key]
    else:
        value = None
    return value


def get_tree(data):
    first = data[0]
    second = data[1]
    keys = sorted(list(
        {x for x in first if x} | {y for y in second if y}))
    output = []
    for key in keys:
        old = data_type_check(first, key)
        new = data_type_check(second, key)
        new_data = (old, new)
        if key in first and key in second:
            if isinstance(first[key], dict) and isinstance(second[key], dict):
                old = first[key]
                new = second[key]
                new_data = (old, new)
                value = (key, get_tree(new_data), 'equal')
                output.append(value)
            else:
                value = (key, new_data, get_difference(new_data))
                output.append(value)

        else:
            value = (key, new_data, get_difference(new_data))
            output.append(value)
    return output
