import json
import data.scrape as scraper
import os
import resources
from datetime import datetime
"""Generate a JSON file from web-scraped python country objects."""


def countryToJson():
    currentTimeStamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    resources_dir = os.path.join(os.path.dirname(resources.__file__))
    with open(resources_dir + "/covid-countries-data_"+currentTimeStamp+".json", "w") as file:
        countryList = [ob.__dict__ for ob in scraper.fillCountriesList()]
        json.dump({"countries": countryList}, file, indent=4)
