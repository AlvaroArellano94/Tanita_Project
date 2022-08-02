from numpy import insert
import pandas as pd
import os

def get_list_files_in_directory(files_directory):
    files_names_in_directory = os.listdir(files_directory)
    return files_names_in_directory