import mysql.connector
import pandas as pd

test_file_directory = "TANITA\GRAPHV1\DATA"
file_directory = "TANITA\GRAPHV1\DATA\DATA2.CSV"

#It will return a tanita_subset filtering the columns and changing the names of the columns
#It needs to be integred the "user_id" into the df in this function because we get it from the file name
def get_rows_from_file(User_id, file_directory):

    tanita_headers = ["Unknow_0","Unknow_1","Unknow_2","Unknow_3","Unknow_4","Unknow_5","Unknow_6","Unknow_7","Unknow_8","Unknow_9","Model_index","Model_value","Measurement_Date_index","Measurement_Date_value","Measurement_Time_index","Measurement_Time_value","Unknow_10","Unknow_11","Gender_index","Gender_value","Age_index","Age_value","Height_index","Height_value","Activity_level_index","Activity_level_value","Body_Mass_index","Body_Mass_value","BMI_index","BMI_value","Global_Fat_Perc_index","Global_Fat_Perc_value","Arm_Fat_Right_Perc_index","Arm_Fat_Right_Perc_value","Arm_Fat_Left_Perc_index","Arm_Fat_Left_Perc_value","Leg_Fat_Right_Perc_index","Leg_Fat_Right_Perc_value","Leg_Fat_Left_Perc_index","Leg_Fat_Left_Perc_value","Torso_Fat_Perc_index","Torso_Fat_Perc_value","Global_Muscle_Perc_index","Global_Muscle_Perc_value","Arm_Muscle_Right_Perc_index","Arm_Muscle_Right_Perc_value","Arm_Muscle_Left_Perc_index","Arm_Muscle_Left_Perc_value","Leg_Muscle_Right_Perc_index","Leg_Muscle_Right_Perc_value","Leg_Muscle_Left_Perc_index","Leg_Muscle_Left_Perc_value","Torso_Muscle_Perc_index","Torso_Muscle_Perc_value","Estimated_Bone_Mass_index","Estimated_Bone_Mass_value","Visceral_Fat_Rating_index","Visceral_Fat_Rating_value","Daily_Calory_Intake_index","Daily_Calory_Intake_value","Estimated_Metabolic_Age_index","Estimated_Metabolic_Age_value","Global_Body_Water_Perc_index","Global_Body_Water_Perc_value","Unknow_12","Unknow_13"]

    #hago la primera prueba para cargar los datos
    tanita_df = pd.read_csv(file_directory, sep=",", header=None, names=tanita_headers)

    #filtering the columns of the dataframe
    tanita_subset_temp = tanita_df[["Measurement_Date_value", "Measurement_Time_value", "Body_Mass_value", "BMI_value", "Global_Fat_Perc_value", "Arm_Fat_Right_Perc_value", "Arm_Fat_Left_Perc_value", "Leg_Fat_Right_Perc_value", "Leg_Fat_Left_Perc_value", "Torso_Fat_Perc_value", "Global_Muscle_Perc_value", "Arm_Muscle_Right_Perc_value", "Arm_Muscle_Left_Perc_value", "Leg_Muscle_Right_Perc_value", "Leg_Muscle_Left_Perc_value", "Torso_Muscle_Perc_value", "Estimated_Bone_Mass_value", "Visceral_Fat_Rating_value", "Daily_Calory_Intake_value", "Estimated_Metabolic_Age_value", "Global_Body_Water_Perc_value"]]

    #change of the names of the columns
    new_col_names = ["Measurement_Date", "Measurement_Time", "Body_Mass", "BMI", "Global_Fat_Perc", "Arm_Fat_Right_Perc", "Arm_Fat_Left_Perc", "Leg_Fat_Right_Perc", "Leg_Fat_Left_Perc", "Torso_Fat_Perc", "Global_Muscle_Perc", "Arm_Muscle_Right_Perc", "Arm_Muscle_Left_Perc", "Leg_Muscle_Right_Perc", "Leg_Muscle_Left_Perc", "Torso_Muscle_Perc", "Estimated_Bone_Mass", "Visceral_Fat_Rating", "Daily_Calory_Intake", "Estimated_Metabolic_Age", "Global_Body_Water_Perc"]
    tanita_subset = tanita_subset_temp.set_axis(new_col_names, axis='columns')
    
    tanita_subset["User_id"] = User_id

    return tanita_subset

def transform_df_from_file(extraction_df_from_file):
    "This function adds into the dataframe a timestamp field created from two others fields."

    extraction_df_from_file['Measurement_Date'] = extraction_df_from_file["Measurement_Date"].str.replace('/','-')

    extraction_df_from_file['Measurement_Date'] = pd.to_datetime(extraction_df_from_file["Measurement_Date"], format='%d-%m-%Y')

    extraction_df_from_file['Measurement_Date'] = extraction_df_from_file["Measurement_Date"].dt.strftime('%Y-%m-%d')  

    extraction_df_from_file["Measurement_Date_Time"] = extraction_df_from_file["Measurement_Date"] +' '+ extraction_df_from_file["Measurement_Time"]
    extraction_df_from_file["Measurement_Date_Time"] = pd.to_datetime(extraction_df_from_file["Measurement_Date_Time"])
    print("It is done!")
    return extraction_df_from_file

def get_PK_from_file_df_tanita(tanita_subset):
    tanita_PK_subset = tanita_subset[["User_id","Measurement_Date", "Measurement_Time"]]
    return tanita_PK_subset

def get_rows_from_db(User_id_filter) -> object:
    """
    This function gets a pandas df of the PK of the table Body_Composition.
    
    """
    try:
        connection_to_mysql = mysql.connector.connect(host='localhost',
                                database='Tanita_app_db',
                                user='root',
                                password='db_analytics_alvaro')
    except Exception as err:
        print("Error al conectar a la base de datos")
    else:
        print("Conectado a MySQL")
        print(connection_to_mysql)
    
    
    cursor_select_users = connection_to_mysql.cursor()

    check_rows_query = f"SELECT count(*) as num_rows FROM Body_Composition WHERE User_id={User_id_filter};"

    cursor_select_users.execute(check_rows_query)
    
    number_of_rows = cursor_select_users.fetchall()[0][0]
    
    #We are going to check if the table is empty. In that case, we create a df with a very old date, in order to get all the rows.
    if number_of_rows > 0:
        select_string = f"SELECT User_id, Date_Time_Measurement FROM Body_Composition WHERE User_id={User_id_filter};"

        cursor_select_users.execute(select_string)
        temp_db_body_comp_df = pd.DataFrame(cursor_select_users.fetchall())
        new_columns_name = ["User_id","Measurement_Date_Time"]
        db_body_comp_df = temp_db_body_comp_df.set_axis(new_columns_name, axis="columns")
        
        return db_body_comp_df
    
    else:
        # initialize data of lists.
        invented_data = {'User_id': [User_id_filter],
                'Measurement_Date_Time': ["10-01-1999 11:00:29"]}
        
        df_created = pd.DataFrame(invented_data)
        print(df_created.astype)
        return df_created

