import json


def key_set(source):
    return ({x for x in source})

def value_comparison(value, value_1, value_2):
    if value_1 != value_2:
        return f"  - {value}: {value_1[value]}\n  + {value}: {value_2[value]}\n"

def generate_diff(file_path1, file_path2):
    first = json.load(open(file_path1))
    second = json.load(open(file_path2))
    dict_keys = sorted(list(key_set(first) | key_set(second)))
    result ='{\n'
    for value in dict_keys:
        if value in first and value not in second:
            result += f"  - {value}: {first[value]}\n"
        elif value in first and value in second:
            result += value_comparison(value, first, second)
        else:
            result += f"  + {value}: {second[value]}\n"
    
    
    return result + '}'

if __name__ == '__main__':
    PATH_1 = '/home/mirdalan/hexlet-projects/python-project-50/bin/files/file1.json'
    PATH_2 = '/home/mirdalan/hexlet-projects/python-project-50/bin/files/file2.json'
    print(generate_diff(PATH_1, PATH_2))
