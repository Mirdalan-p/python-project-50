from gendiff.scripts.get_diff import get_diff


def key_set(source):
    return ({x for x in source if x})


def generate_diff(data):
    first = data[0]
    second = data[1]
    keys = sorted(list(key_set(first) | key_set(second)))
    output = []
    for key in keys:
        if first.get(key):
            if not isinstance(first.get(key), dict):
                old = first.get(key)
                new = second.get(key)
                value = (key, old, new,  get_diff((old, new), keys)) ## Диф по ключу(кортеж)
                output.append(value)
            elif isinstance(first.get(key), dict):
                child = (first.get(key), second.get(key))
                return generate_diff(child)
        
    return [('адын', 'щячло', 'попячсо', 'changed'), ('адын', 'щячло', 'попячсо', 'added'), ('адын', 'щячло', 'попячсо', 'deleted'), ('адын', 'щячло', 'попячсо', 'equal')]
    