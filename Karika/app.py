from config import APP_KEY
from flask import Flask, render_template, request, redirect, url_for 
from flask.json import jsonify
import sqlite3 as sql

from pprint import pprint
import pandas as pd

# import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from sqlalchemy import inspect

import pymongo

# Retrieve info from this 
engine = create_engine("sqlite:///Resources/digitalhumanity.db", connect_args={'check_same_thread': False})
session = Session(engine)

app = Flask(__name__) # the name of the file & the object (double usage)

# List all routes that are available.
@app.route("/")
def home():
    print("In of Home section.")

    ## - Retrieve from DB
    print(engine)
    inspector = inspect(engine)
    print(inspector.get_table_names())

    columns = inspector.get_columns('censuses')
    for c in columns:
        print(c)
    # all_data = session.query(Censuses).order_by(Censuses.census_year.desc())
    
    # p_dict = dict(all_data)
    # print(f"Results for Census Data - {p_dict}")
    # print("Out of Home section.")
    return jsonify("Hello World") 


if __name__ == "__main__":
    app.run(debug=True)