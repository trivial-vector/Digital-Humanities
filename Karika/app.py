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
# Route for heat map.
@app.route("/api/maps/<year>")
def heat_maps(year):
    print("In of heat maps section.")
    print('year', year)
    ## - Retrieve from DB
    ## - Retrieve from DB
    db_DH = client.digitalHumanity_db
    collection_string = "censuses_" + year
    censuses_year_collection = db_DH[collection_string]
    all_data = dumps(censuses_year_collection.find({"Latitude":{"$ne":None},"Longitude":{"$ne":None}},
    {"_id":0,"Street Address":1,"Latitude":1, "Longitude":1, "Race":1}))
    
    return all_data

if __name__ == "__main__":
    app.run(debug=True)