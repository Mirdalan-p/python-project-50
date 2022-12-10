def get_difference(data):
    # Узнаём, изменился ли ключ, или значения по ключу
    first, second = data

    if first == second:
        return 'equal'
    elif first and second is None:
        return 'deleted'
    elif first is None and second:
        return 'added'
    elif first != second:
        return 'changed'


def data_type_check(tree, key):
    # Проверка на булева значения
    if key in tree:
        if tree[key] is None:
            return 'null'
        elif tree[key] is True:
            return 'true'
        elif tree[key] is False:
            return 'false'
        else:
            return tree[key]
    else:
        return None


def get_tree(data):
    first = data[0]
    second = data[1]
    keys = sorted(list(
        {x for x in first if x} | {y for y in second if y}))
    output = []
    for key in keys:
        if key in first and key in second:
            if isinstance(first[key], dict) and isinstance(second[key], dict):
                old = first[key]
                new = second[key]
                new_data = (old, new)
                value = (key, get_tree(new_data), 'equal')
                output.append(value)
            else:
                old = data_type_check(first, key)
                new = data_type_check(second, key)
                new_data = (old, new)
                value = (key, new_data, get_difference(new_data))
                output.append(value)

        else:
            old = data_type_check(first, key)
            new = data_type_check(second, key)
            new_data = (old, new)
            value = (key, new_data, get_difference(new_data))
            output.append(value)
    return output
