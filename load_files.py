from user_object import *
import pandas as pd
import os
from modules import get_list_files_in_directory
from insert_body_comp import insert_Body_comp_db
#first of all it should

first_user = Person(user_id=23)
first_user.anyadir_date(date_1="23/02/2003")

print(first_user.date_1)
#primero debería chequear el directorio para ver que archivos hay subidos. Para cada uno de los archivos deberían tener asignados un usuario.
#El mapping entre usuarios y nombre de archivos se va a cargar desde una tabla de la bbdds de MySQL. 
#file directory from root:
file_directory = "TANITA\GRAPHV1\DATA"
Alvaro_User_File = "TANITA\GRAPHV1\DATA\DATA2.CSV"

tanita_headers = ["Unknow_0","Unknow_1","Unknow_2","Unknow_3","Unknow_4","Unknow_5","Unknow_6","Unknow_7","Unknow_8","Unknow_9","Model_index","Model_value","Measurement_Date_index","Measurement_Date_value","Measurement_Time_index","Measurement_Time_value","Unknow_10","Unknow_11","Gender_index","Gender_value","Age_index","Age_value","Height_index","Height_value","Activity_level_index","Activity_level_value","Body_Mass_index","Body_Mass_value","BMI_index","BMI_value","Global_Fat_Perc_index","Global_Fat_Perc_value","Arm_Fat_Right_Perc_index","Arm_Fat_Right_Perc_value","Arm_Fat_Left_Perc_index","Arm_Fat_Left_Perc_value","Leg_Fat_Right_Perc_index","Leg_Fat_Right_Perc_value","Leg_Fat_Left_Perc_index","Leg_Fat_Left_Perc_value","Torso_Fat_Perc_index","Torso_Fat_Perc_value","Global_Muscle_Perc_index","Global_Muscle_Perc_value","Arm_Muscle_Right_Perc_index","Arm_Muscle_Right_Perc_value","Arm_Muscle_Left_Perc_index","Arm_Muscle_Left_Perc_value","Leg_Muscle_Right_Perc_index","Leg_Muscle_Right_Perc_value","Leg_Muscle_Left_Perc_index","Leg_Muscle_Left_Perc_value","Torso_Muscle_Perc_index","Torso_Muscle_Perc_value","Estimated_Bone_Mass_index","Estimated_Bone_Mass_value","Visceral_Fat_Rating_index","Visceral_Fat_Rating_value","Daily_Calory_Intake_index","Daily_Calory_Intake_value","Estimated_Metabolic_Age_index","Estimated_Metabolic_Age_value","Global_Body_Water_Perc_index","Global_Body_Water_Perc_value","Unknow_12","Unknow_13"]

#hago la primera prueba para cargar los datos
tanita_df = pd.read_csv(Alvaro_User_File, sep=",", header=None, names=tanita_headers)

#where I got the headers info: https://github.com/cab938/tanita
#first, I want to filter the columns I am interested with
print(type(tanita_df))

#print(tanita_df)
#tanita_df.to_excel("df_new_fields_name.xlsx")

tanita_subset_temp = tanita_df[["Measurement_Date_value", "Measurement_Time_value", "Body_Mass_value", "BMI_value", "Global_Fat_Perc_value", "Arm_Fat_Right_Perc_value", "Arm_Fat_Left_Perc_value", "Leg_Fat_Right_Perc_value", "Leg_Fat_Left_Perc_value", "Torso_Fat_Perc_value", "Global_Muscle_Perc_value", "Arm_Muscle_Right_Perc_value", "Arm_Muscle_Left_Perc_value", "Leg_Muscle_Right_Perc_value", "Leg_Muscle_Left_Perc_value", "Torso_Muscle_Perc_value", "Estimated_Bone_Mass_value", "Visceral_Fat_Rating_value", "Daily_Calory_Intake_value", "Estimated_Metabolic_Age_value", "Global_Body_Water_Perc_value"]]
#tanita_subset.to_excel("finally_df_tanita.xlsx")

new_col_names = ["Measurement_Date", "Measurement_Time", "Body_Mass", "BMI", "Global_Fat_Perc", "Arm_Fat_Right_Perc", "Arm_Fat_Left_Perc", "Leg_Fat_Right_Perc", "Leg_Fat_Left_Perc", "Torso_Fat_Perc", "Global_Muscle_Perc", "Arm_Muscle_Right_Perc", "Arm_Muscle_Left_Perc", "Leg_Muscle_Right_Perc", "Leg_Muscle_Left_Perc", "Torso_Muscle_Perc", "Estimated_Bone_Mass", "Visceral_Fat_Rating", "Daily_Calory_Intake", "Estimated_Metabolic_Age", "Global_Body_Water_Perc"]
tanita_subset = tanita_subset_temp.set_axis(new_col_names, axis='columns')

first_row_tanita = tanita_subset.iloc[0]

#this function needs to be passed a row that it is not into the database
#insert_Body_comp_db working correctly!!
#######insert_Body_comp_db(1, first_row_tanita)
