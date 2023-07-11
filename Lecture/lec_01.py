import json


######## Сериализация данных

#### JSON (JavaScript Object Notation)
#### Преобразование JSON в Python

# json_file = json.load(f) - загрузка JSON из файла и сохранение в dict или list

with open('Lecture/user.json', 'r', encoding='utf-8') as f:
    json_file = json.load(f)

print(f'{type(json_file) = }\n{json_file = }')
print(f'{json_file["name"] = }')
print(f'{json_file["address"]["geo"] = }')
print(f'{json_file["email"] = }')
print('------------------------')


#  json_list = json.loads(json_text) - загрузка JSON из строки и сохранение в dict или list

json_text = """
[
    {
        "userid": 1,
        "id": 9,
        "title": "Lorem ipsum dolor sit amet",
        "body": "Ut enim ad minim veniam"
    },
    {
        "userid": 1,
        "id": 10,
        "title": "consectetur adipiscing elit",
        "body": "dolore magna aliqua"
    },
    {
        "userid": 2,
        "id": 11,
        "title": "Duis aute irure dolor",
        "body": "Excepteur sint occaecat"
    },
    {
        "userid": 2,
        "id": 12,
        "title": "sunt in culpa qui officia",
        "body": "anim id est laborum"
    }
]"""

print(f'{type(json_text) = }\n{json_text = }')
json_list = json.loads(json_text)
print(f'{type(json_list) = }\t{len(json_list) = }\n{json_list = }')
print('------------------------')
