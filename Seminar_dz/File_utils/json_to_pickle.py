# __init__.py


import os
import json
import pickle


def convert_json_to_pickle(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            json_file = os.path.join(directory, filename)
            pickle_file = os.path.join(directory, os.path.splitext(filename)[0] + ".pickle")

            with open(json_file, 'r', encoding='utf-8') as file:
                data = json.load(file)

            with open(pickle_file, 'wb') as file:
                pickle.dump(data, file)

    print("Преобразование JSON в Pickle завершено.")
