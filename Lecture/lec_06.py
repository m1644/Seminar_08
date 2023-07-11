import csv
from typing import Iterator


#### Запись CSV из словаря

'''
● csv_write.writeheader() - сохранение первой строки с заголовками в порядке их перечисления в параметре fieldnames
● csv_write.writerow(line) - сохранение списка в одной строке файла в формате CSV
● csv_write.writerows(all_data) - сохранение матрицы в нескольких строках файла в формате CSV
'''

with (
    open('Lecture/biostats_tab.csv', 'r', newline='') as f_read,
    open('Lecture/biostats_new.csv', 'w', newline='', encoding='utf-8') as f_write
):
    csv_read: Iterator[dict] = csv.DictReader(f_read,
                                              fieldnames=["name", "sex", "age", "height", "weight", "office"],
                                              restval="Main Office", dialect='excel-tab',
                                              quoting=csv.QUOTE_NONNUMERIC)
    csv_write = csv.DictWriter(f_write, fieldnames=["id", "name", "office", "sex", "age", "height", "weight"],
                               dialect='excel-tab', quoting=csv.QUOTE_ALL)
    csv_write.writeheader()
    all_data = []
    for i, dict_row in enumerate(csv_read):
        if i != 0:
            dict_row['id'] = i
            dict_row['age'] += 1
            all_data.append(dict_row)
    csv_write.writerows(all_data)
