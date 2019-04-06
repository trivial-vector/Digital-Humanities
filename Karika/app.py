from config import APP_KEY
from flask import Flask, render_template, request, redirect, url_for 
from flask.json import jsonify

import pandas as pd

import pymongo
from bson.json_util import dumps

# Retrieve info from this 
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

app = Flask(__name__) # the name of the file & the object (double usage)

# List all routes that are available.

# This api route takes in year
# Returns: JSON object for that particular year 
# a) Street Address
# b) Lat & Long info
# c) Race_Color
@app.route("/api/maps/<year>")
def heat_maps(year):
    print("In of heat maps section.")
    print('year', year)
    ## - Retrieve from DB
    db_DH = client.digitalHumanity_db
    collection_string = "censuses_" + year
    censuses_year_collection = db_DH[collection_string]
    all_data = dumps(censuses_year_collection.find({"Latitude":{"$ne":None},"Longitude":{"$ne":None}},
    {"_id":0,"Street Address":1,"Latitude":1, "Longitude":1, "Race_Color":1}))
    
    return all_data

# This api route takes in race color like B or W & 
# Returns: JSON object for that particular race_color 
# a) All census years (for our case 1900, 1910, 1920)
# b) All ages (infants to 65 +)
@app.route("/api/censusyears_vs_ages/<race_color>")
def censusyears_vs_ages(race_color):
    print("In census years_vs_ages section.")
    print('year', race_color)
    ## - Retrieve from DB
    db_DH = client.digitalHumanity_db
    census_years = ["1900","1910","1920"]
    
    counter = 0
    for cy in census_years:
        collection_string = "censuses_" + cy
        censuses_year_collection = db_DH[collection_string]
        
        if(counter == 0):
            all_data = dumps(censuses_year_collection.find({"Race_Color":race_color},
            {"_id":0,"Year":1,"Age":1}))
        else:
            new_data = dumps(censuses_year_collection.find({"Race_Color":race_color},
            {"_id":0,"Year":1,"Age":1}))
            all_data = all_data + new_data
        counter = counter + 1
    return all_data

if __name__ == "__main__":
    app.run(debug=True)