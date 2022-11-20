def get_diff(data):
    first, second = data
    if first:
        if first == second:
            return 'equal'
        if first != second:
            return 'changed'
        if not second:
            return 'added'
    else:
        return 'deleted'
