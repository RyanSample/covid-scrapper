import requests
import json
from pathlib import Path
from datetime import datetime


STL_COUNTY_CASES_BY_ZIP_URL = "https://services2.arcgis.com/w657bnjzrjguNyOy/arcgis/rest/services/covid19_by_zip_daily/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"


def get_json(url):
    request = requests.get(url)
    return json.loads(request.text)


def output_to_file(path, data):
    current_date = datetime.now()
    fname = f"{current_date.month:02}_{current_date.day:02}_{current_date.year}_{current_date.hour:02}-{current_date.minute:02}-{current_date.second:02}.json"
    with open(path + fname, 'w') as f:
        json.dump(data, f)


def main():
    path = "data/"
    cases_per_county = get_json(STL_COUNTY_CASES_BY_ZIP_URL)
    output_to_file(path, cases_per_county)


if __name__ == '__main__':
    main()    