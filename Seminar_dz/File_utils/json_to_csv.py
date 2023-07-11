# __init__.py


import csv
import json


def save_as_csv(users_file, csv_file):
    users = {}
    try:
        with open(users_file, 'r', encoding='utf-8') as file:
            users = json.load(file)
    except FileNotFoundError:
        pass

    with open(csv_file, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Идентификатор', 'Имя', 'Уровень доступа'])

        for identifier, user_data in users.items():
            name = user_data['name']
            access_level = user_data['access_level']
            writer.writerow([identifier, name, access_level])

    print("Данные сохранены в файле 'users.csv'.")
