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
censuses_year1900_collection = db_DH.censuses_1900
censuses_year1902_collection = db_DH.censuses_1902
censuses_year1903_collection = db_DH.censuses_1903
censuses_year1905_collection = db_DH.censuses_1905
censuses_year1907_collection = db_DH.censuses_1907
censuses_year1908_collection = db_DH.censuses_1908
censuses_year1910_collection = db_DH.censuses_1910
censuses_year1911_collection = db_DH.censuses_1911
censuses_year1912_collection = db_DH.censuses_1912
censuses_year1913_collection = db_DH.censuses_1913
censuses_year1915_collection = db_DH.censuses_1915
censuses_year1917_collection = db_DH.censuses_1917
censuses_year1918_collection = db_DH.censuses_1918
censuses_year1919_collection = db_DH.censuses_1919
censuses_year1920_collection = db_DH.censuses_1920

# ===============================================================================================================================
# Step 2: Retrieve basic info for years 1900 through 1920 from CSV file
# ===============================================================================================================================
filename = "./Resources/basic info w race column_TableToExcel.csv"
df_basic_data_allyrs = pd.read_csv(filename)

# Step 2a: Create separate dataframes for each year based on the info
df_basic_info_1900 = df_basic_data_allyrs.loc[:,["StNumClean","name1900","race1900","tenure1900","censusname1900","censusrace1900"]]
df_basic_info_1900 = vizgjk.create_basic_df_for_that_year(df_basic_info_1900, 1900, 1)

df_basic_info_1902 = df_basic_data_allyrs.loc[:,["StNumClean","name1902","race1902","tenure1902"]]
df_basic_info_1902 = vizgjk.create_basic_df_for_that_year(df_basic_info_1902, 1902, 0)

df_basic_info_1903 = df_basic_data_allyrs.loc[:,["StNumClean","name1903","race1903","tenure1903"]]
df_basic_info_1903 = vizgjk.create_basic_df_for_that_year(df_basic_info_1903, 1903, 0)

df_basic_info_1905 = df_basic_data_allyrs.loc[:,["StNumClean","name1905","race1905","tenure1905"]]
df_basic_info_1905 = vizgjk.create_basic_df_for_that_year(df_basic_info_1905, 1905, 0)

df_basic_info_1907 = df_basic_data_allyrs.loc[:,["StNumClean","name1907","race1907","tenure1907"]]
df_basic_info_1907 = vizgjk.create_basic_df_for_that_year(df_basic_info_1907, 1907, 0)

df_basic_info_1908 = df_basic_data_allyrs.loc[:,["StNumClean","name1908","race1908","tenure1908"]]
df_basic_info_1908 = vizgjk.create_basic_df_for_that_year(df_basic_info_1908, 1908, 0)

df_basic_info_1910 = df_basic_data_allyrs.loc[:,["StNumClean","name1910","race1910","tenure1910","censusname1910","censusrace1910"]]
df_basic_info_1910 = vizgjk.create_basic_df_for_that_year(df_basic_info_1910, 1910, 1)

df_basic_info_1911 = df_basic_data_allyrs.loc[:,["StNumClean","name1911","race1911","tenure1911"]]
df_basic_info_1911 = vizgjk.create_basic_df_for_that_year(df_basic_info_1911, 1911, 0)

df_basic_info_1912 = df_basic_data_allyrs.loc[:,["StNumClean","name1912","race1912","tenure1912"]]
df_basic_info_1912 = vizgjk.create_basic_df_for_that_year(df_basic_info_1912, 1912, 0)

df_basic_info_1913 = df_basic_data_allyrs.loc[:,["StNumClean","name1913","race1913","tenure1913"]]
df_basic_info_1913 = vizgjk.create_basic_df_for_that_year(df_basic_info_1913, 1913, 0)

df_basic_info_1915 = df_basic_data_allyrs.loc[:,["StNumClean","name1915","race1915","tenure1915"]]
df_basic_info_1915 = vizgjk.create_basic_df_for_that_year(df_basic_info_1915, 1915, 0)

df_basic_info_1917 = df_basic_data_allyrs.loc[:,["StNumClean","name1917","race1917","tenure1917"]]
df_basic_info_1917 = vizgjk.create_basic_df_for_that_year(df_basic_info_1917, 1917, 0)

df_basic_info_1918 = df_basic_data_allyrs.loc[:,["StNumClean","name1918","race1918","tenure1918"]]
df_basic_info_1918 = vizgjk.create_basic_df_for_that_year(df_basic_info_1918, 1918, 0)

df_basic_info_1919 = df_basic_data_allyrs.loc[:,["StNumClean","name1919","race1919","tenure1919"]]
df_basic_info_1919 = vizgjk.create_basic_df_for_that_year(df_basic_info_1919, 1919, 0)

df_basic_info_1920 = df_basic_data_allyrs.loc[:,["StNumClean","name1920","race1920","tenure1920","censusname1920","censusrace1920"]]
df_basic_info_1920 = vizgjk.create_basic_df_for_that_year(df_basic_info_1920, 1920, 1)

# Step 2b: insert dataframes into respective MongoDB collections
censuses_year1900_collection.insert_many(df_basic_info_1900.to_dict('records'))
censuses_year1902_collection.insert_many(df_basic_info_1902.to_dict('records'))
censuses_year1903_collection.insert_many(df_basic_info_1903.to_dict('records'))
censuses_year1905_collection.insert_many(df_basic_info_1905.to_dict('records'))
censuses_year1907_collection.insert_many(df_basic_info_1907.to_dict('records'))
censuses_year1908_collection.insert_many(df_basic_info_1908.to_dict('records'))
censuses_year1910_collection.insert_many(df_basic_info_1910.to_dict('records'))
censuses_year1911_collection.insert_many(df_basic_info_1911.to_dict('records'))
censuses_year1912_collection.insert_many(df_basic_info_1912.to_dict('records'))
censuses_year1913_collection.insert_many(df_basic_info_1913.to_dict('records'))
censuses_year1915_collection.insert_many(df_basic_info_1915.to_dict('records'))
censuses_year1917_collection.insert_many(df_basic_info_1917.to_dict('records'))
censuses_year1918_collection.insert_many(df_basic_info_1918.to_dict('records'))
censuses_year1919_collection.insert_many(df_basic_info_1919.to_dict('records'))
censuses_year1920_collection.insert_many(df_basic_info_1920.to_dict('records'))

# ===============================================================================================================================
# Step 3: Retrieve Occupation, Color, Age, Sex, Owned based on Street Address, Year & Full Name/ Census Name
# ===============================================================================================================================

# Step 3a: Retrieve additional info for census years 1900, 1910 & 1920 from CSV file
filename_1900 = "./Resources/Reservation Census charting_1900.csv"
df_reservation_1900 = pd.read_csv(filename_1900)

filename_1910 = "./Resources/Reservation Census charting_1910.csv"
df_reservation_1910 = pd.read_csv(filename_1910)

filename_1920 = "./Resources/Reservation Census charting_1920.csv"
df_reservation_1920 = pd.read_csv(filename_1920)

# Step 3b: Create separate dataframes for each year based on the info
df_new_1900 = vizgjk.create_additional_info_for_that_year(df_reservation_1900, 1900)
df_new_1910 = vizgjk.create_additional_info_for_that_year(df_reservation_1910, 1910)
df_new_1920 = vizgjk.create_additional_info_for_that_year(df_reservation_1920, 1920)

# Step 3c: Upsert the mongo collection with the dataframe content for that particular year
for index, row in df_new_1900.iterrows():
    censuses_year1900_collection.update_many({'Year': row[-1], 'Street Address': row[0], 'Census Name': row[1]}, {"$set": row.to_dict()}, upsert=True)

for index, row in df_new_1910.iterrows():
    censuses_year1910_collection.update_many({'Year': row[-1], 'Street Address': row[0], 'Census Name': row[1]}, {"$set": row.to_dict()}, upsert=True)
    
for index, row in df_new_1920.iterrows():
    censuses_year1920_collection.update_many({'Year': row[-1], 'Street Address': row[0], 'Census Name': row[1]}, {"$set": row.to_dict()}, upsert=True)    

# ===============================================================================================================================
# Step 4: Retrieve the Latitude & Longitude info based on Street Address, Year & Full Name/ Census Name
# ===============================================================================================================================

# Step 4a: Retrieve the lat long info from CSV file
filename_latlong = "./Resources/LatLong_Info.csv"
df_latlong = pd.read_csv(filename_latlong)

# handling inconsistency of Street address across multiple csv files.
df_latlong["Street Address"] = df_latlong["Street Address"].str.replace("Street","St", regex=False) 

# Step 4b: insert lat long info into MongoDB collections for different years
vizgjk.update_db_document_for_that_particular_coll(df_latlong, 1900, censuses_year1900_collection)
vizgjk.update_db_document_for_that_particular_coll(df_latlong, 1902, censuses_year1902_collection)
vizgjk.update_db_document_for_that_particular_coll(df_latlong, 1903, censuses_year1903_collection)
vizgjk.update_db_document_for_that_particular_coll(df_latlong, 1905, censuses_year1905_collection)
vizgjk.update_db_document_for_that_particular_coll(df_latlong, 1907, censuses_year1907_collection)
vizgjk.update_db_document_for_that_particular_coll(df_latlong, 1908, censuses_year1908_collection)
vizgjk.update_db_document_for_that_particular_coll(df_latlong, 1910, censuses_year1910_collection)
vizgjk.update_db_document_for_that_particular_coll(df_latlong, 1911, censuses_year1911_collection)
vizgjk.update_db_document_for_that_particular_coll(df_latlong, 1912, censuses_year1912_collection)
vizgjk.update_db_document_for_that_particular_coll(df_latlong, 1913, censuses_year1913_collection)
vizgjk.update_db_document_for_that_particular_coll(df_latlong, 1915, censuses_year1915_collection)
vizgjk.update_db_document_for_that_particular_coll(df_latlong, 1917, censuses_year1917_collection)
vizgjk.update_db_document_for_that_particular_coll(df_latlong, 1918, censuses_year1918_collection)
vizgjk.update_db_document_for_that_particular_coll(df_latlong, 1919, censuses_year1919_collection)
vizgjk.update_db_document_for_that_particular_coll(df_latlong, 1920, censuses_year1920_collection)

print("Done with Data engineering. Check your MongoCompass for 'digitalHumanity_db' database")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")