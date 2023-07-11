import csv
import json
import hashlib


''' Задание №4
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы функции.
'''

def read_csv_and_convert(csv_file, jsonl_file):
    data = []

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            identifier = row[0].zfill(10)
            name = row[1].capitalize()
            access_level = int(row[2])

            hash_value = hashlib.sha256((name + identifier).encode('utf-8')).hexdigest()

            record = {
                'identifier': identifier,
                'name': name.lower(),
                'access_level': access_level,
                'hash': hash_value
            }
            data.append(record)

    with open(jsonl_file, 'w', encoding='utf-8') as file:
        for record in data:
            json.dump(record, file, ensure_ascii=False)
            file.write('\n')

    print("Данные сохранены в JSON-файле.")

csv_file = 'Seminar/Csv/users.csv'
jsonl_file = 'Seminar/Json/users_json.jsonl'
read_csv_and_convert(csv_file, jsonl_file)
