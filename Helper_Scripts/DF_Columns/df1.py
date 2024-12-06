import pandas as pd
# from Helper_Scripts.Folder_Search.get_modified_folder_name import get_folder_or_filename
from Config.Config import log_execution
@log_execution
def create_path_df(anathesi_df,path_list) :
    df1 = pd.DataFrame({
    'A/A': [x for x in range(1,len(anathesi_df['Επωνυμία Αποδέκτη'])+1)],
        'Αντίδικος': anathesi_df['Επωνυμία Αποδέκτη'],
        'Ανάθεση' : anathesi_df['Ανάθεση'],
        'ΔΙΚΑΣΤΙΚΟ ΙΔΡΥΜΑ': "",
        'Διαδκασία': "",
        'Μάρτυρας' : anathesi_df['Μάρτυρας'],
        'Φάκελος' : path_list,
        'Κωδικός Ενέργειας' : anathesi_df['Κωδικός Ενέργειας'],	
    })
    
    return df1


def convert_to_hyperlink(df1):
    # Apply the function to the 'Φάκελος' column
    df1['Φάκελος'] = df1['Φάκελος'].apply(write_hyperlink)
    return df1

def write_hyperlink(link):
    # Using the openpyxl syntax to specify a hyperlink
    return f'=HYPERLINK("{link}", "{link}")'
