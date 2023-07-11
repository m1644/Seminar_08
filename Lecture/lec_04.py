import csv


#### CSV (Comma-Separated Values)
#### Формат CSV

## Запись CSV

'''
csv_write = csv.writer(f) - csv_write позволяет сохранять данные в формате CSV
csv_write.writerow(line) - сохранение списка в одной строке файла в формате CSV
csv_write.writerows(all_data) - сохранение матрицы в нескольких строках файла в формате CSV
'''

with (
    open('Lecture/biostats_tab.csv', 'r', newline='') as f_read,
    open('Lecture/new_biostats.csv', 'w', newline='', encoding='utf-8') as f_write
):
    csv_read = csv.reader(f_read, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    csv_write = csv.writer(f_write, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    all_data = []
    for i, line in enumerate(csv_read):
        if i == 0:
            csv_write.writerow(line)
        else:
            line[2] += 1
            for j in range(2, 4 + 1):
                line[j] = int(line[j])
            all_data.append(line)
    csv_write.writerows(all_data)
