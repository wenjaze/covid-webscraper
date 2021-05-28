import requests
from bs4 import BeautifulSoup
import pandas as pd
import country


def getTable():
    URL = "https://www.worldometers.info/coronavirus/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.find(id='main_table_countries_today')


def createDataFrame():
    headers = []
    for i in getTable().find_all('th'):
        title = i.text
        headers.append(title)

    return pd.DataFrame(columns=headers)


def dataFrameToNumpyArray():
    df = createDataFrame()
    for j in getTable().find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [tr.text for tr in row_data]
        length = len(df)
        df.loc[length] = row
    return df.to_numpy()


def fillCountriesList():
    df = dataFrameToNumpyArray()
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
            row[20],
            row[21])
        countries.append(c)
    return countries


def printAllCountries(countries):
    for k in countries:
        print(vars(k))


if __name__ == "__main__":
    printAllCountries(fillCountriesList())
