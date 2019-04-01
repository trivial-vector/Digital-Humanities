from config import APP_KEY
import requests
import json
from pprint import pprint
import pandas as pd
import pymongo

from flask import Flask, json, jsonify

# Datasource #1: Read CSV to get annual generation of Electricity in US all sectors

filename = "./Resources/Net_generation_United_States_all_sectors_annual.csv"
df_annual_allstates = pd.read_csv(filename)

# df_annual_allstates.head(20)

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define database and collection
db_EIA = client.EIA_db
summary_collection = db_EIA.summary
statewise_collection = db_EIA.statewise

# insert dataframe df_annual_allstates into summary collection
summary_collection.insert_many(df_annual_allstates.to_dict('records'))


app = Flask(__name__) # the name of the file & the object (double usage)

# List all routes that are available.
@app.route("/")
def home():
    print("In & Out of Home section.")

    ## - Retrieve from DB
    # Display items in summary collection
    # Prepare DF for all energy type for all 17 yrs
    sum_listings = summary_collection.find()
    df_sum_lists = pd.DataFrame(list(sum_listings))

    # Delete the _id
    del df_sum_lists['_id']

    # replace NaN with '0' esp. in case of solar energy production
    df_sum_lists = df_sum_lists.fillna(0)

    return (jsonify(df_sum_lists.to_json()))

if __name__ == "__main__":
    app.run(debug=True)