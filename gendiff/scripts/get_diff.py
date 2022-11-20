def get_diff(data):
    first, second = data
    if first:
        if first == second:
            return 'equal'
        elif not second:
            return 'deleted'
        elif first != second:
            return 'changed'
    else:
        return 'added'
