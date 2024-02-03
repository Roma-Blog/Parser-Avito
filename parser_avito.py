from bs4 import BeautifulSoup
import requests, data_csv

url_search = 'https://www.avito.ru/all?q='
search_query = input()
data_link = []

src = requests.get(url_search+search_query)

soup = BeautifulSoup(src.text, 'html.parser')

link_list = soup.find_all('a', class_='styles-module-root-QmppR styles-module-root_noVisited-aFA10')

for item in link_list:
    data_link.extend([[item.text, f'https://www.avito.ru{ item.get("href")}']])
    data_csv.Writ_Data(data_link)


    