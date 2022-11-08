import json


def data_type_check(value):
    if isinstance(value, bool):
        if value == None:
            return 'null'
        else:
            return str(value).lower()
    else:
        return value

def key_set(source):
    return ({x for x in source})

def value_comparison(value, value_1, value_2):
    if value_1[value] == value_2[value]:
        return f"    {value}: {data_type_check(value_1[value])}\n"
    else:
        return f"  - {value}: {data_type_check(value_1[value])}\n  + {value}: {data_type_check(value_2[value])}\n"

def generate_diff(file_path1, file_path2):
    first = json.load(open(file_path1))
    second = json.load(open(file_path2))
    # Получаем список ключей, которые есть в обоих файлах, сортируем
    dict_keys = sorted(list(key_set(first) | key_set(second)))
    result ='{\n'
    for value in dict_keys:
        if value in first and value not in second:
            result += f"  - {value}: {data_type_check(first[value])}\n"
        elif value in second and value not in first:
            result += f"  + {value}: {data_type_check(second[value])}\n"
        elif value in first and value in second:
            result += value_comparison(value, first, second)
    
    
    return result + '}'

if __name__ == '__main__':
    print(generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json'))