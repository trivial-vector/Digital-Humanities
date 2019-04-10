from bson.json_util import dumps
import pymongo
from flask import Blueprint, render_template
from flask.json import jsonify
import os

import pandas as pd

# import config
# from config import DB_USERNAME
# from config import DB_PASSWORD
# from config import DB_HOST
# from config import DB_PORT
# from config import DB_NAME

apiroutes = Blueprint("apiroutes", __name__)

# Retrieve info from this
connnection = os.environ.get('MONGODB_URI')
client = pymongo.MongoClient(connnection)
db_DH = client['heroku_1zst25sm']


@apiroutes.route("/")
def instructions():
    print("In the main route")
    return jsonify({
        "error": "Try sending a request to /api/maps/<year>"
    })

# ========================================================================================================================================
# List all routes that are available.
# ========================================================================================================================================
# This api route takes in year
# Returns: JSON object for that particular year
# a) Street Address
# b) Lat & Long info
# c) Race_Color
# ========================================================================================================================================


@apiroutes.route("/maps/<year>")
def heat_maps(year):
    print("In of heat maps section.")
    print('year', year)
    # - Retrieve from DB
    collection_string = "censuses_" + year
    censuses_year_collection = db_DH[collection_string]
    all_data = dumps(censuses_year_collection.find({"Latitude": {"$ne": None}, "Longitude": {"$ne": None}},
                                                   {"_id": 0, "Full Name": 1, "Street Address": 1, "Latitude": 1, "Longitude": 1, "Race_Color": 1}))

    return all_data

# ========================================================================================================================================
# This api route takes in race color like B or W &
# Returns: JSON object for that particular race_color
# a) All census years (for our case 1900, 1910, 1920)
# b) All ages (infants to 65 +)
# ========================================================================================================================================


@apiroutes.route("/censusyears_vs_ages/<race_color>")
def censusyears_vs_ages(race_color):
    print("In census years_vs_ages section.")
    print('year', race_color)
    # - Retrieve from DB
    census_years = ["1900", "1910", "1920"]

    counter = 0
    for cy in census_years:
        collection_string = "censuses_" + cy
        censuses_year_collection = db_DH[collection_string]

        if(counter == 0):
            all_data = dumps(censuses_year_collection.find({"Race_Color": race_color},
                                                           {"_id": 0, "Year": 1, "Age": 1}))
        else:
            new_data = dumps(censuses_year_collection.find({"Race_Color": race_color},
                                                           {"_id": 0, "Year": 1, "Age": 1}))
            all_data = all_data + new_data
        counter = counter + 1
    return all_data
