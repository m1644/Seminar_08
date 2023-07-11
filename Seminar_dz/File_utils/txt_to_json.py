# __init__.py


import json


def create_json_file(result_file, json_file):
    data = []

    with open(result_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        name, value = line.strip().split()
        data.append({'name': name.encode('utf-8').decode('utf-8'), 'value': float(value)})

    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
