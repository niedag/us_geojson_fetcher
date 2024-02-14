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


def get_district_geojson_for_county(state_initial, county_name):
    district_number = get_district_number(state_initial, county_name)
    district_effect_year = get_district_year(state_initial, county_name)

    # Fetch the data from the repository
    url = f"https://theunitedstates.io/districts/cds/{district_effect_year}/{state_initial}-{district_number}/shape.geojson"
    response = requests.get(url)
    if response.status_code == 200:
        geojson_data = response.json()
        return geojson_data
    else:
        print("Error fetching data")


def get_district_number(state_name, county_name):
    # Search and fetch data from a database or form
    us_districts_df = pd.read_csv("./us_county_to_district.csv")  # Later may be possible to change this to gpt input but to limit the calls and price, this is a simple solution
    print(us_districts_df.columns)

    search_result = "01"
    return search_result


def get_district_year(state_initial, district_number):
    # TODO: Search the database / form for the associated district year using state and number
    district_year = 2012
    return district_year


# TODO: create a database with all district names for each state, year the district came into effect.
# create a function that returns the county number based on the name.
# database should include the following parameters:
# state_name, state_initial, county_name, district_number, district_effect_year

# pandas can also be used with SQL, json, html, etc. 


# Example usage:
state_name = "NY"
county_name = "01"
state_geojson = get_geojson_for_state(state_name)
print(state_geojson)
county_geojson = get_district_geojson_for_county(state_name, county_name)
print(county_geojson)