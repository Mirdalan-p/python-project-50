from gendiff.scripts.get_diff import get_diff


def key_set(source):
    if source:
        keys = list(source.keys())
        return set(keys)
    else:
        return set([])


def generate_diff(data):
    first = data[0]
    second = data[1]
    keys = sorted(list(key_set(first) | key_set(second)))
    print(keys)
    output = []
    for key in keys:
        if key in first:
            if not isinstance(first[key], dict):
                old = first.get(key)
                new = second.get(key)
                new_data = (old, new)
                value = (key, old, new,  get_diff(new_data))
                output.append(value)
            else:
                if key in first and key in second:
                    new_data = (first.get(key), second.get(key))
                    return generate_diff(new_data)
                else:
                    value = (key, old, new,  get_diff(new_data))
                    output.append(value)
        else:
            old = first.get(key)
            new = second.get(key)
            new_data = (old, new)
            value = (key, old, new, get_diff(new_data))
            output.append(value)
    print(output)
    return output
