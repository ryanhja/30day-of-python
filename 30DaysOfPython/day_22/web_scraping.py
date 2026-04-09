# Day 22: 30 Days of python programming

import requests
from bs4 import BeautifulSoup

url = 'https://www.touteleurope.eu/l-europe-et-moi/la-liste-des-indicatifs-telephoniques-par-pays-de-l-union-europeenne/'

response = requests.get(url)

content = response.content

soup = BeautifulSoup(content, 'html.parser')
# print(soup.title)
# print(soup.body.get_text())

with open('phone_indicative_by_country.txt', 'w') as f:
    f.write(soup.body.get_text())

print("data exported successfully")