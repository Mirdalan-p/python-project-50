def get_diff(data):
    first, second = data
    
    if first == second:
        return 'equal'
    
    elif first and second is None:
        return 'deleted'
    elif first is None and second:
        return 'added'
    elif  first != second:
        return 'changed'
