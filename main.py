from bs4 import BeautifulSoup
import requests, csv

# url_search = 'https://www.avito.ru/all?q='
# search_query = input()
# data_link = []

# src = requests.get(url_search+search_query)



# link_list = soup.find_all('a', class_='styles-module-root-QmppR styles-module-root_noVisited-aFA10')

def Writ_CSV(data, name_file):
    with open(f'{name_file}.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Заголовок', 'Ссылка'])
        for item in data:
            writer.writerow(item)

# for item in link_list:
#     data_link.append([item.text, f'https://www.avito.ru{ item.get("href")}'])
#     Writ_CSV(data_link, search_query)


class SearchAvito():
    "Хранит поисковый запрос"
    def __init__(self):
        self.query = input()

class ParserAvito():
    "Объект парсит данные с авито по полученному запросу"
    url_search = 'https://www.avito.ru/all?q='
    data_link = []
    link_list = []

    def __init__(self):
        self.search_query = SearchAvito()
        self.src = requests.get(self.url_search + self.search_query.query)

    def Write_CSV(self):
        for item in self.link_list:
            self.data_link.append([item.text, f'https://www.avito.ru{ item.get("href")}'])
            Writ_CSV(self.data_link, self.search_query.query)


parser_avito = ParserAvito()

soup = BeautifulSoup(parser_avito.src.text, 'html.parser')

parser_avito.link_list = soup.find_all('a', class_='styles-module-root-QmppR styles-module-root_noVisited-aFA10')
parser_avito.Write_CSV()