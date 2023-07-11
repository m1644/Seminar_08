import csv


#### CSV (Comma-Separated Values)
#### Формат CSV

## Чтение CSV

# with open('biostats.csv', 'r', newline='') as f: - параметр newline='' для работы с CSV
# csv_file = csv.reader(f) - csv_file позволяет построчно читать csv файл в список list

with open('Lecture/biostats.csv', 'r', newline='') as f:
    csv_file = csv.reader(f)
    for line in csv_file:
        print(line)
    print(type(line))
print('------------------------')

with open('Lecture/biostats_tab.csv', 'r', newline='') as f1:
    csv_file1 = csv.reader(f1, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file1:
        print(line)
    print(type(line))
