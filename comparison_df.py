import pandas as pd


#ME FALTA DESARROLLAR UN POCO!!
def get_max_date():
    #df_from_db

    data={'User_id':[1,2],'Measurement_Date':['2022-04-23','2022-04-25'], 'Measurement_Time':['12:06:39','16:09:39']}

    df=pd.DataFrame(data)

    df_max = df.max(axis="User_id")
    print(df_max)

get_max_date()


