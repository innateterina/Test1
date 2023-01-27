#Прочитать сохранённый json-файл из задания №18 и записать данные на диск в csv-файл,
# первой строкой которого озаглавив каждый столбец и добавив новый столбец “телефон”.

import json
import csv

with open("voc_file.json") as f:
    data = json.load(f)

name_of_fields = ['id', 'name', 'age', 'telephone']
fields = []
for item in data:
    value = data[item]
    value.insert(0, item)
    value.insert(3, '')
    fields.append(value)
print(fields)

with open("voc_file02.csv", mode='w', encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file)
    file_writer.writerow(name_of_fields)
    for item in fields:
        file_writer.writerow(item)





