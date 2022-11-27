from gendiff.scripts.get_diff import get_diff


def key_set(source):
    if source:
        keys = list(source.keys())
        return set(keys)
    else:
        return set([])

def data_type_check(value):
    if isinstance(value, dict):
        return value
    else:
        if value is None:
            return None
        else:
            return str(value).lower()

def generate_diff(data):
    first = data[0]
    second = data[1]
    keys = sorted(list(key_set(first) | key_set(second)))
    output = []
    for key in keys:
        if key in first and key in second:
            if isinstance(first[key], dict) and isinstance(second[key], dict):
                old = first[key]
                new = second[key]
                new_data = (old, new)
                value = (key, generate_diff(new_data), 'equal')
                output.append(value)
            else:
                old = data_type_check(first[key])
                new = data_type_check(second[key])
                new_data = (old, new)
                value = (key, new_data,  get_diff(new_data))
                output.append(value)
            
        else:
            old = data_type_check(first.get(key))
            new = data_type_check(second.get(key))
            new_data = (old, new)
            value = (key, new_data, get_diff(new_data))
            output.append(value)
    return output
