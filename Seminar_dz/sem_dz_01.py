import os
import json
import csv
import pickle


''' Задание №1
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. 
Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, 
а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
'''

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

    with open('Seminar/results.json', 'w', encoding='utf-8') as file:
        json.dump(results, file, indent=4)

    with open('Seminar/results.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Path', 'Type', 'Size (bytes)', 'Parent Directory'])
        for result in results:
            writer.writerow([result['path'], result['type'], result['size'], result['parent_directory']])

    with open('Seminar/results.pickle', 'wb') as file:
        pickle.dump(results, file)

    print("Результаты сохранены в файлах 'results.json', 'results.csv' и 'results.pickle'.")
    print("Общий размер директории (включая поддиректории и файлы):", total_size, "байт")

directory = 'Seminar'
traverse_directory(directory)
