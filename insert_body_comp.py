import mysql.connector
import datetime
#info to create this part: https://www.youtube.com/watch?v=91iNR0eG8kE&t=2s&ab_channel=TechWithTim
#El dataframe que se pasa está compuesto por un solo registro. Es decir, el dataframe total, se debe filtrar por el registro que queremos introducir
#si queremos introducir más de un registro, se debe llamar a esta función más de una vez.
def insert_Body_comp_db(User_id, df_row_tanita):
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

    insert_string = "INSERT INTO Body_Composition(User_id, Body_mass, Body_mass_index, Global_fat_percentage, Fat_right_arm_perc,\
    Fat_left_arm_perc, Fat_right_leg_perc, Fat_left_leg_perc, Fat_torso_perc, Global_muscle_perc,\
    Muscle_right_arm_perc, Muscle_left_arm_perc, Muscle_right_leg_perc, Muscle_left_leg_perc, Muscle_torso_perc,\
    Bone_mass_estimated, Fat_visceral_rating, Calory_intake_daily, Metabolic_age_estimated, Global_body_water_perc,\
    Date_Measurement, Time_Measurement) \
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    
    #no esta cargando bien la fecha, por esa razón debemos hacer un casting más complejo
    date_time_obj = datetime.datetime.strptime(df_row_tanita["Measurement_Date"], '%d/%m/%Y')
    date_cast = date_time_obj.date()

    data_to_insert = (User_id, float(df_row_tanita["Body_Mass"]), float(df_row_tanita["BMI"]), float(df_row_tanita["Global_Fat_Perc"]), float(df_row_tanita["Arm_Fat_Right_Perc"]),\
        float(df_row_tanita["Arm_Fat_Left_Perc"]), float(df_row_tanita["Leg_Fat_Right_Perc"]), float(df_row_tanita["Leg_Fat_Left_Perc"]), float(df_row_tanita["Torso_Fat_Perc"]), \
        float(df_row_tanita["Global_Muscle_Perc"]), float(df_row_tanita["Arm_Muscle_Right_Perc"]), float(df_row_tanita["Arm_Muscle_Left_Perc"]), float(df_row_tanita["Leg_Muscle_Right_Perc"]),\
        float(df_row_tanita["Leg_Muscle_Left_Perc"]), float(df_row_tanita["Torso_Muscle_Perc"]), float(df_row_tanita["Estimated_Bone_Mass"]), int(df_row_tanita["Visceral_Fat_Rating"]), \
        int(df_row_tanita["Daily_Calory_Intake"]), int(df_row_tanita["Estimated_Metabolic_Age"]), float(df_row_tanita["Global_Body_Water_Perc"]), \
        date_cast, df_row_tanita["Measurement_Time"])
    
    #NOW IT NEEDS TO PROGRAM HOW TO DEAL WITH DATAFRAMES! HAS A PARAMETER IT WILL GET THE DATAFRAME!!!!
    cursor_show_db.execute(insert_string, data_to_insert)
    #los paso todos como string, pero luego la base de datos los almacena con su respectivo tipo
    connection_to_mysql.commit()