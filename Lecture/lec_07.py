import pickle
import os


#### Модуль Pickle

res = pickle.loads(b"cos\nsystem\n(S'echo Hello world!'\ntR.")
print(f'{res = }')

os.system('echo Hello world!')
print('------------------------')


## Сериализация
'''
● pickle.dump(my_dict, f) - сохранение объекта в бинарном файле
'''

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

print(my_dict)
res = pickle.dumps(my_dict, protocol=pickle.DEFAULT_PROTOCOL)
print(f'{res = }')
print(f'{pickle.DEFAULT_PROTOCOL = }')
print('------------------------')


'''
● result = pickle.dumps(my_dict) - сохранение объекта в строку байт
'''

def func(a, b, c):
    return a + b + c

my_dict = {
    "numbers": [42, 4.1415, 7+3j],
    "functions": (func, sum, max),
    "others": {True, False, 'Hello world!'},
}

with open('Lecture/my_dict.pickle', 'wb') as f:
    pickle.dump(my_dict, f)
print('------------------------')


#### Десериализация
'''
● new_dict = pickle.load(f) - загрузка из бинарного файла и сохранение в объекта
'''

data = b'\x80\x04\x95\x8c\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\nfirst_name\x94\x8c\x03Jon\x94\x8c\tlast_name\x94\x8c\x05Smith\x94\x8c\x07hobbies\x94]\x94(\x8c\x04funy\x94\x8c\x03jok\x94e\x8c\x03age\x94K,\x8c\x08children\x94]\x94(}\x94(h\x01\x8c\x0c\xd0\x9c\xd0\xb0\xd1\x80\xd1\x83\xd1\x81\xd1\x8f\x94h\tK\x08u}\x94(h\x01\x8c\x08\xd0\x94\xd0\xb8\xd0\xbc\xd0\xb0\x94h\tK\x10ueu.'

new_dict = pickle.loads(data)
print(f'{new_dict = }')
print('------------------------')


'''
● new_dict = pickle.loads(data) - получение объекта из бинарной строки
'''

def func(a, b, c):
    return a * b * c

with open('Lecture/my_dict.pickle', 'rb') as f:
    new_dict = pickle.load(f)

print(f'{new_dict = }')
print(f'{new_dict["functions"][0](2, 3, 4) = }')
print('------------------------')
