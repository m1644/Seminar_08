import pickle
import csv


''' Задание №6
Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
'''

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

pickle_file = 'Seminar/Pickle/result.pickle'
csv_file = 'Seminar/Csv/users_csv.csv'
convert_pickle_to_csv(pickle_file, csv_file)
