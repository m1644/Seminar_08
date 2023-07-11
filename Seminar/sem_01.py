import json


''' Задание №1
Вспоминаем задачу 3 из прошлого семинара. 
Мы сформировали текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
'''

def create_json_file(result_file, json_file):
    data = []

    with open(result_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        name, value = line.strip().split()
        data.append({'name': name.encode('utf-8').decode('utf-8'), 'value': float(value)})

    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

result_file = "Seminar/result.txt"
json_file = "Seminar/Json/result.json"
create_json_file(result_file, json_file)
