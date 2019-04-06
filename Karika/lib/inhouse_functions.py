# ======================================================================================================================
# This function adds the correct header name based on whether it was census year or not & also adds new column 'Year'
# ======================================================================================================================
def create_basic_df_for_that_year(df, year, is_census):
    header = ["Street Address","Full Name","Race_Code","Tenure","Census Name","Census Race_Code"]
    # If there is No census info available for that year then creates a blank column - so that 
    # the information across all the years is consistent
    
    if(is_census == 0):
        df["Census Name"] = ""
        df["Census Race_Code"] = ""
    
    df.columns = header
    df["Race_Color"] = ""
    df["Year"] = year
    # handling inconsistency of Street address across multiple csv files.
    df["Street Address"] = df["Street Address"].str.replace("Street","St") 
    return df

# ===============================================================================================================================
# This function adds additional information about the person living in that house (based on street addr) for that particular year
# ===============================================================================================================================
def create_additional_info_for_that_year(df, year):
    header = ["Relation", "Race_Color","Sex","Age","Occupation", "Own or Rent","Free or Mortgage","House or Farm"]

    street_add = df["House No"].astype(str) + " " + df["Street Name"].astype(str)
    full_name = df["GivenName"].astype(str) + " " + df["LastName"].astype(str)

    df_new = df.loc[:,["Relation (4)","Color or Race (5)","Sex (6)","Age at last birthday (8)","Occupation (19)","Own or Rent (25)", "Owned free or mortgage (26)","House or Farm (27)"]]

    df_new.columns = header # Set new header info for the existing CSV columns
    df_new["Street Address"] = street_add
    df_new["Name"] = full_name
    df_new["Year"] = year
    # Cleanup the columns Race_Color, Own or Rent, Age, Occupation
    df_new["Race_Color"] = df_new["Race_Color"].replace(['Mu', 'M', 'M/W', 'My'], "B") 
    
    df_new['Own or Rent'] = df_new['Own or Rent'].replace(['Rent '], "Rent")
    df_new['Own or Rent'] = df_new['Own or Rent'].replace(['Owned ','Owned'], "Own")
        
    df_new = df_new[df_new['Occupation'].notnull() & df_new['Year'].notnull()]
    occupations = ["Laborer","Laundress" ,"Cook" ,"Washwoman","Maid","Porter","Seamstress","Janitor",
    "Servant","Waitress","Owner of Business","Cleaner","Manager","Nurse","Presser","Driver","Clerk","Chauffeur",
    "Carpenter","lean",
    "rick","arber","elper"]

    for occupation in occupations:
        # for cases where we want to name the occupation different than the one listed (for easy understanding)
        new_string = occupation
        if(occupation == "Owner"):
            new_string = "Owner of Business" 
        elif(occupation == "Clean" or occupation == "lean"):
            new_string = "Cleaner"
        elif(occupation == "Maid" or occupation == "Servant"):
            new_string = "Servant"
        elif(occupation == "Laundress" or occupation == "Washwoman"):
            new_string = "Laundress"
        elif(occupation == "river"):
            new_string = "Driver"
        elif(occupation == "lerk"):
            new_string = "Clerk"
        elif(occupation == "ffe"):
            new_string = "Chauffeur"
        elif(occupation == "pent"):
            new_string = "Carpenter"
        elif(occupation == "rick"):
            new_string = "Bricklayer"
        elif(occupation == "arber"):
            new_string = "Barber"
        elif(occupation == "elper"):
            new_string = "Assistant"
        df_new['Occupation'][df_new.Occupation.str.contains(occupation)] = new_string 

    cols = df_new.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    cols = cols[-1:] + cols[:-1]

    df_new = df_new[cols] 
    
    return(df_new)