# ======================================================================================================================
# This function adds the correct header name based on whether it was census year or not & also adds new column 'Year'
# ======================================================================================================================
def create_basic_df_for_that_year(df, year, is_census):
    header = ["Street Address","Full Name","Race","Tenure","Census Name","Census Race"]
    # If there is No census info available for that year then creates a blank column - so that 
    # the information across all the years is consistent
    
    if(is_census == 0):
        df["Census Name"] = ""
        df["Census Race"] = ""
    
    df.columns = header
    df["Year"] = year
    # handling inconsistency of Street address across multiple csv files.
    df["Street Address"] = df["Street Address"].str.replace("Street","St", regex=False) 
    return df

# ===============================================================================================================================
# This function adds additional information about the person living in that house (based on street addr) for that particular year
# ===============================================================================================================================
def create_additional_info_for_that_year(df, year):
    street_add = df["House No"].astype(str) + " " + df["Street Name"].astype(str)
    full_name = df["GivenName"].astype(str) + " " + df["LastName"].astype(str)

    df_new = df.loc[:,["Relation (4)","Color or Race (5)","Sex (6)","Age at last birthday (8)","Occupation (19)","Own or Rent (25)", "Owned free or mortgage (26)","House or Farm (27)"]]

    df_new["Street Address"] = street_add
    df_new["Name"] = full_name

    cols = df_new.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    cols = cols[-1:] + cols[:-1]

    df_new = df_new[cols] 
    df_new["Year"] = year
    
    return(df_new)

# ===============================================================================================================================
# This function upserts the mongo collection with the dataframe content for that particular year
# ===============================================================================================================================
def update_db_document_for_that_particular_coll(df, year, db_coll_that_year):
    for row in df.iterrows():
        db_coll_that_year.update_many({'Year': year, 'Street Address': row[2]}, {"$set": row.to_dict()}, upsert=True)
