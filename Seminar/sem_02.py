import json


''' Задание №2
Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
'''

def add_user(users_file):
    users = {}
    try:
        with open(users_file, 'r', encoding='utf-8') as file:
            users = json.load(file)
    except FileNotFoundError:
        pass

    while True:
        name = input("Введите имя пользователя (или 'exit' для завершения): ")
        if name.lower() == 'exit':
            break

        identifier = input("Введите личный идентификатор пользователя: ")
        access_level = int(input("Введите уровень доступа (от 1 до 7): "))

        if access_level not in range(1, 8):
            print("Некорректный уровень доступа. Попробуйте снова.")
            continue

        if identifier in users:
            print("Идентификатор уже занят. Попробуйте снова.")
            continue

        users[identifier] = {'name': name.encode('utf-8').decode('utf-8'), 'access_level': access_level}

        with open(users_file, 'w', encoding='utf-8') as file:
            json.dump(users, file, indent=4, ensure_ascii=False)

    print("Данные сохранены в файле 'users.json'.")

users_file = 'Seminar/Json/users.json'
add_user(users_file)
