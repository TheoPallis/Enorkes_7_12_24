import pandas as pd
from Helper_Scripts.Folder_Search.get_modified_folder_name import get_folder_or_filename

def create_path_df(anathesi_df) :
    df1 = pd.DataFrame({

    'A/A': [x for x in range(1,len(anathesi_df['Επωνυμία Αποδέκτη'])+1)],
        'Αντίδικος': anathesi_df['Επωνυμία Αποδέκτη'],
        'Ανάθεση' : anathesi_df['Ανάθεση'],
        'ΔΙΚΑΣΤΙΚΟ ΙΔΡΥΜΑ': "",
        'Διαδκασία': "",
        'Μάρτυρας' : anathesi_df['Μάρτυρας'],
        'Φάκελος' : "",
    })
    
    return df1


def create_shared_paths(df1):
    df1['Φάκελος'] = (r"\\lawoffice\\Applications\\ScanDocs\\ΔΕΔΔΗΕ scandocs\\" 
                    + df1['Φάκελος'].apply(lambda x: get_folder_or_filename(x, -3)) # For subfolders (eg Θεσσαλονίκη)
                    + "\\" 
                    + df1['Φάκελος'].apply(lambda x: get_folder_or_filename(x, -2)) 
                    + "\\" 
                    + df1['Φάκελος'].apply(lambda x: get_folder_or_filename(x, -1)))

    df1['Φάκελος'] = df1['Φάκελος'].astype(str) 
    df1['Φάκελος'] =df1['Φάκελος'].apply(lambda x : x.replace("ΦΑΚΕΛΟΙ ΕΝΟΡΚΩΝ",""))

    return df1

def convert_to_hyperlink(df1):
    # Apply the function to the 'Φάκελος' column
    df1['Φάκελος'] = df1['Φάκελος'].apply(write_hyperlink)
    return df1

def write_hyperlink(link):
    # Using the openpyxl syntax to specify a hyperlink
    return f'=HYPERLINK("{link}", "{link}")'
