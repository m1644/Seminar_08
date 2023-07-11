import json


######## Сериализация данных

#### JSON (JavaScript Object Notation)
#### Преобразование JSON в Python

#  json.dump(my_dict, f) - сохранение dict или list в файле в виде JSON

my_dict = {
    "first_name": "Jon",
    "last_name": "Smith",
    "hobbies": ["funy", "jok"],
    "age": 44,
    "children": [
        {
            "first_name": "Маруся",
            "age": 8
        },
        {
            "first_name": "Дима",
            "age": 16
        },
    ]
}

print(f'{type(my_dict) = }\n{my_dict = }')

with open('Lecture/new_user.json', 'w', encoding='utf-8') as f:
    json.dump(my_dict, f, ensure_ascii=False)
print('------------------------')


# dict_to_json_text = json.dumps(my_dict) - сохранение dict или list в виде JSON строки

dict_to_json_text = json.dumps(my_dict)
print(f'{type(dict_to_json_text) = }\n{dict_to_json_text = }')

dict_to_json_text = json.dumps(my_dict, ensure_ascii=False)
print(f'{type(dict_to_json_text) = }\n{dict_to_json_text = }')
print('------------------------')


# Дополнительные параметры dump и dumps

my_dict_1 = {
    "id": 123,
    "name": "Clementine Bauche",
    "username": "Cleba",
    "email": "cleba@mail.ru",
    "address": {
        "street": "Central",
        "city": "Omsk",
        "zipcode": "123654"
    },
    "phone": "+7-999-123-45-67"
}

res = json.dumps(my_dict_1, indent=2, separators=('.', ':'), sort_keys=True)
print(res)
print('------------------------')


# Задача_1

a = 'Hello world!'
b = {key: value for key, value in enumerate(a)}
c = json.dumps(b, indent=3, separators=('; ', '= '))
print(c)
print('------------------------')
