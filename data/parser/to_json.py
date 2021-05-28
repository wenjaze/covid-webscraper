import json
import data.scrape as scraper
import os
import resources

"""Generate a JSON file from web-scraped python country objects."""


def countryToJson():
    resources_dir = os.path.join(os.path.dirname(resources.__file__))
    with open(resources_dir + "/countries.json", "r+") as file:
        countryList = [ob.__dict__ for ob in scraper.fillCountriesList()]
        json.dump({"countries": countryList}, file, indent=4)
