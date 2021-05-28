import data.scrape as scraper
import json


def countryToJson():
    for country in scraper.fillCountriesList():
        country_in_json = json.dumps(country.__dict__)

    print(country_in_json)


def write_json(new_data, filename='data.json'):
    with open(filename, 'r+') as file:
        json.dump(file_data, file, indent=4)
