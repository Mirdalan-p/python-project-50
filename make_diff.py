import json


def key_set(source):
    return ({x for x in source})

def value_comparison(value, value_1, value_2):
    if value_1[value] == value_2[value]:
        return f"    {value}: {value_1[value]}\n"
    else:
        return f"  - {value}: {value_1[value]}\n  + {value}: {value_2[value]}\n"

def generate_diff(file_path1, file_path2):
    first = json.load(open(file_path1))
    second = json.load(open(file_path2))
    # Получаем список ключей, которые есть в обоих файлах, сортируем
    dict_keys = sorted(list(key_set(first) | key_set(second)))
    result ='{\n'
    for value in dict_keys:
        if value in first and value not in second:
            result += f"  - {value}: {first[value]}\n"
        elif value in second and value not in first:
            result += f"  + {value}: {second[value]}\n"
        elif value in first and value in second:
            result += value_comparison(value, first, second)
    
    
    return result + '}'

if __name__ == '__main__':
    print(generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json'))