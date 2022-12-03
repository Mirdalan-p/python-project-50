import json


def is_changed(values, diff):
    old, new = values
    if diff == "deleted":
        return {"deleted": old}
    elif diff == "added":
        return {"added": new}
    elif diff == "changed":
        return {"deleted": old, "added": new}
    else:
        return str(old)


def make_dict(data):
    output = {}
    for element in data:
        key, values, diff = element
        if not isinstance(values, list):
            output[key] = is_changed(values, diff)
        else:
            output[key] = make_dict(values)
    return output


def make_json(data):
    return json.dumps(make_dict(data), sort_keys=True, indent=4)
