import requests
from bs4 import BeautifulSoup
import pandas as pd
from model import country

"""Extracting HTML table from worldometers."""


def getTable():
    URL = "https://www.worldometers.info/coronavirus/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.find(id='main_table_countries_today')


"""Creating pandas dataframe headers."""


def createDataFrame():
    headers = []
    for i in getTable().find_all('th'):
        title = i.text
        headers.append(title)

    return pd.DataFrame(columns=headers)


"""Filling pandas dataframe with rows and converting it to numpy array."""


def dataFrameToNumpyArray():
    df = createDataFrame()
    for j in getTable().find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [tr.text for tr in row_data]
        length = len(df)
        df.loc[length] = row
    return df.to_numpy()


"""Filling the list of Country objects."""


def fillCountriesList():
    df = dataFrameToNumpyArray()
    countries = []
    for row in df[7:]:
        countries.append(
            country.Country(
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
                row[21]))
    return countries
