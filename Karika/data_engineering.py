print("In the data engineering")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
# ===============================================================================================================================
# All the packages used for data engineering & cleaning part
# ===============================================================================================================================
import pandas as pd
import pymongo

# created our own library
import lib
from lib import inhouse_functions as vizgjk

# ===============================================================================================================================
# Step 1: Initialize PyMongo to work with MongoDBs & create our OWN db to store information
# ===============================================================================================================================
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Retrieve OR Create New database and collection
db_DH = client.digitalHumanity_db
years = ["1900","1902","1903","1905","1907","1908","1910","1911","1912","1913","1915","1917","1918","1919","1920"]
census_years = ["1900","1910","1920"]

dict_censuses_col = {}

# Create collections for each year of data (that is obtained through XLS) in Mongo DB
for y in years:
    census_str = "censuses_" + y
    dict_censuses_col[y] = db_DH[census_str]

# ===============================================================================================================================
# Step 2: Retrieve basic info for years 1900 through 1920 from CSV file
# ===============================================================================================================================
filename = "./Resources/basic info w race column_TableToExcel.csv"
df_basic_data_allyrs = pd.read_csv(filename)

# Step 2a: Create separate dataframes for each year based on the info
# Step 2b: insert dataframes into respective MongoDB collections

for y in years:
    name = "name"+y
    race = "race"+y
    tenure = "tenure"+y
    censusname = "censusname"+y
    censusrace = "censusrace"+y

    iscensus = 0 # variable to determine if its census year
    for cy in census_years:
        # Check if its the census year
        if(cy == y):
            iscensus = 1
            break # it should exit the for loop of census year (cy) - which will happen for yrs 1900,1910,1920
    if(iscensus):
        # Yes it is census year then we have census race & name column to access
        df = df_basic_data_allyrs.loc[:,["StNumClean",name,race,tenure,censusname,censusrace]]
    else:
        df = df_basic_data_allyrs.loc[:,["StNumClean",name,race,tenure]]
    # populate dataframe with the basic info
    df = vizgjk.create_basic_df_for_that_year(df, y, iscensus)
    # push that information in mongo db
    dict_censuses_col[y].insert_many(df.to_dict('records'))

# ===============================================================================================================================
# Step 3: Retrieve Occupation, Color, Age, Sex, Owned based on Street Address, Year & Full Name/ Census Name
# ===============================================================================================================================

# Step 3a: Retrieve additional info for census years 1900, 1910 & 1920 from CSV file
# Step 3b: Create separate dataframes for each year based on the info
# Step 3c: Upsert the mongo collection with the dataframe content for that particular year

for cy in census_years:
    filename = "./Resources/Reservation Census charting_" + cy + ".csv"
    df = pd.read_csv(filename)
    df_new = vizgjk.create_additional_info_for_that_year(df, cy)
    for index, row in df_new.iterrows():
        dict_censuses_col[cy].update_many({'Year': row[-1], 'Street Address': row[0], 'Census Name': row[1]}, {"$set": row.to_dict()}, upsert=True)

# ===============================================================================================================================
# Step 4: Retrieve the Latitude & Longitude info based on Street Address, Year & Full Name/ Census Name
# ===============================================================================================================================

# Step 4a: Retrieve the lat long info from CSV file
filename_latlong = "./Resources/LatLong_Info.csv"
df_latlong = pd.read_csv(filename_latlong)

# handling inconsistency of Street address across multiple csv files.
df_latlong["Street Address"] = df_latlong["Street Address"].str.replace("Street","St", regex=False) 

# Step 4b: insert lat long info into MongoDB collections for different years
for y in years:
    for row in df_latlong.iterrows():
        data = dict(row[1])
        dict_censuses_col[y].update_many({'Year': y, 'Street Address': row[1]["Street Address"]}, {"$set": data}, upsert=True)
print("Done with Data engineering. Check your MongoCompass for 'digitalHumanity_db' database")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")