from File_utils.txt_to_json import create_json_file
from File_utils.add_users import add_user
from File_utils.json_to_csv import save_as_csv
from File_utils.json_to_pickle import convert_json_to_pickle
from File_utils.pickle_to_csv import convert_pickle_to_csv
from File_utils.traverse_directory import traverse_directory


# Пример использования функции txt_to_json
'''result_file = "Seminar/result.txt"
json_file = "Seminar_dz/func_result.json"
create_json_file(result_file, json_file)'''


# Пример использования функции add_users
'''users_file = 'Seminar_dz/add_users.json'
add_user(users_file)'''


# Пример использования функции json_to_csv
'''users_file = 'Seminar_dz/add_users.json'
csv_file = 'Seminar_dz/add_users.csv'
save_as_csv(users_file, csv_file)'''


# Пример использования функции json_to_pickle
'''directory = 'Seminar_dz'
convert_json_to_pickle(directory)'''


# Пример использования функции pickle_to_csv
'''pickle_file = 'Seminar_dz/func_result.pickle'
csv_file = 'Seminar_dz/func_result.csv'
convert_pickle_to_csv(pickle_file, csv_file)'''


# Пример использования функции traverse_directory
directory = 'Seminar_dz'
traverse_directory(directory)
