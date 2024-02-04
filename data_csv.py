import csv

def Writ_Data(data, name_file):
    with open(f'{name_file}.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Заголовок', 'Ссылка'])
        for item in data:
            writer.writerow(item)

