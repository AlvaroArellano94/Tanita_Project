import mysql.connector

#info to create this part: https://www.youtube.com/watch?v=91iNR0eG8kE&t=2s&ab_channel=TechWithTim
def insert_User_db(Name, Surnames, Gender, Age, Height, File_name):
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

    #to query mysql database it is necessary to create a cursor
    cursor_show_db = connection_to_mysql.cursor()  #this will connect to database

    #insert_string = f"INSERT INTO Users(User_name, User_surnames, Gender, Age, Height, File_name) VALUES (%s,%s,%s,%i,%d,%s), ({Name}, {Surnames}, {Gender}, {Age}, {Height}, {File_name});"
    insert_string = "INSERT INTO Users(User_name, User_surnames, Gender, Age, Height, File_name) VALUES (%s,%s,%s,%s,%s,%s)"

    cursor_show_db.execute(insert_string, (Name, Surnames, Gender, Age, Height, File_name))
    #los paso todos como string, pero luego la base de datos los almacena con su respectivo tipo
    connection_to_mysql.commit()

#example on how to use the function
#insert_User_db('Juan Miguel', 'Arellano Arnedo', 'Male', 59, 1.76, 'DATA4.CSV')