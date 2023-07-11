# __init__.py


import pickle
import csv


def convert_pickle_to_csv(pickle_file, csv_file):
    with open(pickle_file, 'rb') as file:
        data = pickle.load(file)

    if len(data) > 0:
        keys = data[0].keys()

        with open(csv_file, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)

        print("Преобразование Pickle в CSV завершено.")
    else:
        print("Ошибка: Пустой список словарей.")
