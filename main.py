import requests
from bs4 import BeautifulSoup
import re

r = requests.get("http://www.siatka-lodzkie.org/term/1a.htm")

c = r.content

soup = BeautifulSoup(c, "html.parser")

data = []

table = (soup.find("table", {"class": "MsoTableGrid"}))

rows = table.find_all("tr")

for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

data = [i for i in data if len(i) > 0]

games = {}
last_date = ''

for record in data:
    if re.search('\d{2}.\d{2}.\d{4}', record[0]):
        last_date = record[0]
        if last_date not in games:
            games[last_date] = []
    elif len(record) > 1:
        games[last_date].append(record)


for key, values in games.items():
    print(key)
    for val in values:
        print(val)
