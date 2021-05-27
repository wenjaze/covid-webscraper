import requests
from bs4 import BeautifulSoup
import pandas as pd
import country


URL = 'https://www.worldometers.info/coronavirus/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

table_data = soup.find(id='main_table_countries_today')


# for c in countries:
# 	if c.find('a') != None:
# 		a.append(c.find('a').text.strip())


# print(a)
# for s in soup:
# 	print(soup)
headers = []
for i in table_data.find_all('th'):
    title = i.text
    headers.append(title)

df = pd.DataFrame(columns = headers)

for j in table_data.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [tr.text for tr in row_data]
        length = len(df)
        df.loc[length] = row  
df = df.to_numpy()

countries = []

for row in df:
	c = country.Country(
		row[1],
		row[2],
		row[3],
		row[4],
		row[5],
		row[6],
		row[7],
		row[8],
		row[9],
		row[10],
		row[11],
		row[12],
		row[13],
		row[14],
		row[15],
		row[16],
		row[17],
		row[18],
		row[19],
		row[20])
	countries.append(c)

country_name = input("Enter a country:")

for k in countries:
	if k.name == country_name:
		print(str(k))