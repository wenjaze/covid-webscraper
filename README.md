## COVID-Webscraper
Are you looking for up to date COVID related information that you want use programatically both as Python object lists, or JSON?
You can use this project as a base for data visualizing, demonstrating
interesting facts or simply creating a CRUD API from it (Only for educational, demonstrational and non-monetizing purposes). Feel free to use it in any form
of application, that [worldometers](https://www.worldometers.info/coronavirus/) allows you to, by purchasing their LICENSE starting [here](https://www.worldometers.info/licensing-trial.php). I do not take responsibility and own any source of information provided.
This script scrapes LIVE COVID related informations about all the countries, continents and other places in the world from
[worldometers](https://www.worldometers.info/coronavirus/), including the following:
- Total cases
- Total deaths
- Total tests
- Cases / 1M
- Deaths / 1M
- Tests / 1M
#### Usage:
- **JSON**
 - Run main.py from the root directory
There you go, you have a time-stamped .json format file in the resources directory.
- **Python object**:
 - Call parser.fillCountriesList() -> returns a list of [Country](https://github.com/wenjaze/covid-webscraper/blob/master/model/country.py) objects.
