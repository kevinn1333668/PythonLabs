import json
import json
import csv
import sys
import os

def json_to_csv(json_filename):
    with open(json_filename, 'r') as f:
        data = json.load(f)

    csv_filename = os.path.splitext(json_filename)[0] + '.csv'

    with open(csv_filename, 'w', newline='') as csv_file:
        if isinstance(data, list):
            #JSON — список словарей
            writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        elif isinstance(data, dict):
            #JSON — словарь
            if all(isinstance(val, (str, int, float, bool)) for val in data.values()):
                #Простые ключ-значение
                writer = csv.DictWriter(csv_file, fieldnames=data.keys())
                writer.writeheader()
                writer.writerow(data)
            else:
                #Вложенные списки
                for key, records in data.items():
                    if isinstance(records, list):
                        writer = csv.DictWriter(csv_file, fieldnames=records[0].keys())
                        writer.writeheader()
                        writer.writerows(records)
json_to_csv('test.json')