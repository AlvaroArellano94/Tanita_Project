import pandas as pd
from insert_body_comp import insert_Body_comp_db
from datetime import datetime

def get_row_newest_date_time(df):
    """
    This function recives a dataframe and It filters the registers to get the newest
    """

    #I filter the df that is passed to get the fields that we are interested in
    df_to_work = df[['User_id','Measurement_Date_Time']]

    #First, I want the max date
    max_date_in_df = df["Measurement_Date_Time"].max()

    #I filter the df for the rows with that value   
    final_df_row = df[df.Measurement_Date_Time == max_date_in_df]

    return final_df_row

def get_df_to_insert(df_oldest_row, df_from_file):
    #First, I get from the DDBBs the oldest date , time row.
    max_date_time_oldest_row = df_oldest_row["Measurement_Date_Time"].max()

    temp_df_to_insert = df_from_file[df_from_file.Measurement_Date_Time > max_date_time_oldest_row]
    return temp_df_to_insert

#The User_id will be already into the df
def insert_df_into_db(final_df_to_insert):
    """
    This function will recived a df with all the raws that wants to be inserted into the db. The function will take each individual row and inserted one by one.
    """
    for index in range(len(final_df_to_insert)):
        insert_Body_comp_db(final_df_to_insert.loc[index])