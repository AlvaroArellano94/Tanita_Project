import pandas as pd
from insert_body_comp import insert_Body_comp_db

def get_row_oledest_date_time(df):

    #I filter the df that is passed to get the fields that we are interested in
    df_to_work = df[['User_id','Measurement_Date', 'Measurement_Time']]

    #First, I want the max date
    max_date_in_df = df["Measurement_Date"].max()

    #I filter the df for the rows with that value
    df_max_date = df[df.Measurement_Date == max_date_in_df]
    #Now, I want to check if there are more than 1 row. In that case, I will look for the oldest "Measurement_Time"
    num_rows_max_date = len(df_max_date.index)
    #print(df_max_date)
    if num_rows_max_date>1:
        max_time_in_df = df_max_date["Measurement_Time"].max()
        final_df_row = df[(df.Measurement_Date ==max_date_in_df) & (df.Measurement_Time==max_time_in_df)]

        return final_df_row
    else:
        final_df_row = df[df.Measurement_Date ==max_date_in_df]

        return final_df_row

"""
#TEST: vamos a generar un df ficticio
data={'User_id':[1,2,3],'Measurement_Date':['2022-04-23','2022-04-25','2022-04-25'], 'Measurement_Time':['12:06:39','20:09:39','19:44:23']}
#transformamos el diccionario en df
df=pd.DataFrame(data)

print(get_row_oledest_date_time(df))
"""
#this function needs to be checked
def get_df_to_insert(df_olest_row, df_from_file):
    max_date_oldest_row = df_olest_row["Measurement_Date"].max()
    max_time_oldest_row = df_olest_row["Measurement_Time"].max()



    temp_df_to_insert = df_from_file[(df_from_file.Measurement_Date > max_date_oldest_row)]
    #check if there is a row that has the same day but older time
    
    rows_from_oldest_date = len(df_from_file[(df_from_file.Measurement_Date==max_date_oldest_row)].index)

    if  rows_from_oldest_date>1:
        final_df_to_insert = df_from_file[(df_from_file.Measurement_Date==max_date_oldest_row) & (df_from_file.Measurement_Time > max_time_oldest_row)]
        return final_df_to_insert
    else:
        return temp_df_to_insert


#The User_id will be already into the df
def insert_df_into_db(final_df_to_insert):
    """
    This function will recived a df with all the raws that wants to be inserted into the db. The function will take each individual row and inserted one by one.
    """
    for index in range(len(final_df_to_insert)):
        insert_Body_comp_db(final_df_to_insert.loc[index])
    

    
    


