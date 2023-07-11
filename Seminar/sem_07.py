import csv
import pickle


''' Задание №7
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Распечатайте его как pickle строку.
'''

def read_csv_as_pickle_string(csv_file):
    data = []

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            data.append(row)

    pickle_string = pickle.dumps(data)

    return pickle_string

csv_file = 'Seminar/Csv/users_csv.csv'
pickle_string = read_csv_as_pickle_string(csv_file)
print(pickle_string)
