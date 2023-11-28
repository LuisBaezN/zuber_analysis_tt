import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html'

req = requests.get(url)

soup = BeautifulSoup(req.text)

raw_table = soup.find('table', attrs={"id": "weather_records"})

col_names = []

for row in raw_table.find_all('th'):
    col_names.append(row.text)

table = []

for row in raw_table.find_all('tr'):
    if not row.find_all('th'):
        table.append([element.text for element in row.find_all('td')])

weather_records = pd.DataFrame(table, columns=col_names)
