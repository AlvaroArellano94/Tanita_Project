import mysql.connector
import pandas as pd
#this functions returns a dataframe with the name of the user and the name of the file of that user that we have in the database
def check_Users_registered():
    try:
        connection_to_mysql = mysql.connector.connect(host='localhost',
                                database='Tanita_app_db',
                                user='root',
                                password='db_analytics_alvaro')
    except Exception as err:
        print("Error al conectar a la base de datos")
    else:
        print("Conectado a MySQL")
        print("")
        print(connection_to_mysql)
    
    cursor_select_users = connection_to_mysql.cursor()

    select_string = "SELECT User_id, File_name FROM Users;"

    cursor_select_users.execute(select_string)
    records = cursor_select_users.fetchall()
    #print(records)
    Users_dict = {}
    for row in records:
        Users_dict[row[0]]=row[1]
    
    return Users_dict


    #df_users = pd.DataFrame(cursor_select_users.fetchall(), columns=["User_id","File_name"])
    #return df_users

User_df = check_Users_registered()
print(User_df)
print(list(User_df.keys()))
print(list(User_df.values()))



