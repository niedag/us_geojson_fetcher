import requests
import json
import pandas as pd
import numpy as np


def get_geojson_for_state(state_initial):
    # Fetch the data from the repository
    url = f"https://theunitedstates.io/districts/states/{state_initial}/shape.geojson"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        geojson_data = response.json()
        return geojson_data
    else:
        print("Error fetching data")

def get_geojson_for_district(state_initial, district_number):
    district_year = get_district_year(state_initial, district_number);
    url = f"https://theunitedstates.io/districts/cds/{district_year}/{state_initial}-{district_number}/shape.geojson"
    response = requests.get(url)
    if response.status_code == 200:
        geojson_data = response.json()
        return geojson_data
    else:
        print("Error fetching data")
def get_county_geojson(state_initial, county_name):
    # Fetch the data from the repository
    url = "google.com"
    response = requests.get(url)
    if response.status_code == 200:
        geojson_data = response.json()
        return geojson_data
    else:
        print("Error fetching data")

def get_district_year(state_initial, district_id):
    # Search and fetch data from a database or form
    df = pd.read_csv('us_districts.csv')
    search = df[(df["district_id"] == district_id) & (df['state_initial'] == state_initial)]
    if not search.empty:
        return search.iloc[0]['year_in_effect']
    else: return None

# TODO: create a database with all district names for each state, year the district came into effect.
# create a function that returns the county number based on the name.
# database should include the following parameters:
# state_name, state_initial, county_name, district_number, district_effect_year
# pandas can also be used with SQL, json, html, etc.  

# Example usage:
state_initial = "NY"
district_num = "1"

county_name = "Santa Clara"
#state_geojson = get_geojson_for_state(state_initial)
print(state_geojson)

district_geojson = get_geojson_for_district(state_initial, district_num)
print(district_geojson)
# county_geojson = get_district_geojson_for_county(state_name, county_name)
# print(county_geojson)
