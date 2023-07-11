# __init__.py


import os
import json
import csv
import pickle


def traverse_directory(directory):
    results = []
    total_size = 0

    for root, dirs, files in os.walk(directory):
        dir_size = sum(os.path.getsize(os.path.join(root, file)) for file in files)
        total_size += dir_size

        for dir in dirs:
            path = os.path.join(root, dir)
            result = {
                'path': path,
                'type': 'directory',
                'size': dir_size,
                'parent_directory': os.path.dirname(path)
            }
            results.append(result)

        for file in files:
            path = os.path.join(root, file)
            size = os.path.getsize(path)
            result = {
                'path': path,
                'type': 'file',
                'size': size,
                'parent_directory': os.path.dirname(path)
            }
            results.append(result)

    with open('Seminar_dz/results.json', 'w', encoding='utf-8') as file:
        json.dump(results, file, indent=4)

    with open('Seminar_dz/results.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Path', 'Type', 'Size (bytes)', 'Parent Directory'])
        for result in results:
            writer.writerow([result['path'], result['type'], result['size'], result['parent_directory']])

    with open('Seminar_dz/results.pickle', 'wb') as file:
        pickle.dump(results, file)

    print("Результаты сохранены в файлах 'results.json', 'results.csv' и 'results.pickle'.")
    print("Общий размер директории (включая поддиректории и файлы):", total_size, "байт")
