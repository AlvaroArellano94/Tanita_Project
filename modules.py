from numpy import insert
import pandas as pd
import os

#this is a function that gets the names of the files (that gather information of escales) in this directory
def get_list_files_in_directory(files_directory):
    files_names_in_directory = os.listdir(files_directory)
    return files_names_in_directory


#this functions returns a list with the File_names that are in directory and in the User db 
def match_File_names(files_names_in_directory, User_df_dict):
    User_file_name_db_list = list(User_df_dict.keys())

    #match_File_names = set(User_file_name_db_list) & set(files_names_in_directory)

    final_File_names_dict = {}
    for key,value in User_df_dict.items():
        if value in files_names_in_directory:
            final_File_names_dict[key]=value

    return final_File_names_dict

