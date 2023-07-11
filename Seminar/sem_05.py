import os
import json
import pickle


''' Задание №5
Напишите функцию, которая ищет json файлы в указанной директории 
и сохраняет их содержимое в виде одноимённых pickle файлов.
'''

def convert_json_to_pickle(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            json_file = os.path.join(directory, filename)
            pickle_file = os.path.join(directory_1, os.path.splitext(filename)[0] + ".pickle")

            with open(json_file, 'r', encoding='utf-8') as file:
                data = json.load(file)

            with open(pickle_file, 'wb') as file:
                pickle.dump(data, file)

    print("Преобразование JSON в Pickle завершено.")

directory = 'Seminar/Json'
directory_1 = 'Seminar/Pickle'
convert_json_to_pickle(directory)
