import csv


#### Чтение CSV в словарь

'''
● fieldnames — список заголовков столбцов, ключей словаря
● restkey — значение ключа для столбцов, которых нет в fieldnames
● restval — значение поля для ключей fieldnames, которых нет в файле CSV
'''

with open('Lecture/biostats_tab.csv', 'r', newline='') as f:
    csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age", "height", "weight", "office"],
                              restkey="new", restval="Main Office", dialect='excel-tab',
                              quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(f'{line = }')
        print(f'{line["name"] = }\t{line["age"] = }')
print('------------------------')


with open('Lecture/biostats_tab.csv', 'r', newline='') as f:
    csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age", ], restkey="new", restval="Main Office", 
                              dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(f'{line = }')
        print(f'{line["name"] = }\t{line["age"] = }')
print('------------------------')
