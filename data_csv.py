import csv

def Writ_Data(data):
    with open('data.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Заголовок', 'Ссылка'])
        for item in data:
            writer.writerow(item)

