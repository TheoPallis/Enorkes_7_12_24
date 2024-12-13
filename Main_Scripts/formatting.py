import os 
import shutil
import re
import pandas as pd
from Config.Config import log_execution



def remove_invalid_dates(df):
    df = df[~df['Ημερομηνία Προγραμματισμού  Ένορκης'].str.contains(r'[α-ωΑ-Ω]', regex=True,na=False)]    
    return df

def remove_invalid_anatheseis(df) :
    df = df.dropna(subset=['Ανάθεση'])
    return df

def format_date(df,col) :
    if col in df.columns :
        df[col] = df[col].fillna('1900-01-01 00:00:00')  # Use a default datetime string if NaN
        df[col] = pd.to_datetime(df[col], errors='coerce')  # Parse without enforcing a format
        df[col] = df[col].dt.strftime("%d/%m/%Y")  # Format into the desired date format  
    return df

def remove_invalid_dates_anatheseis_format_dates_fill_na(df)  : 
    df = remove_invalid_dates(df)    
    df = remove_invalid_anatheseis(df)
    df = format_date(df,'Ημερομηνία Προγραμματισμού  Ένορκης')
    df = format_date(df,'Ημ νια Κατάθεσης Αγωγής ΝΚπολ Δ')
    df = df.fillna("")
    return df

def filter_df(df, filtered_date=None, filtered_name_list=None, head=None,anathesi = None):
    if anathesi :
        df = df[df['Ανάθεση'].str.contains(anathesi)]
    if filtered_date:
        df = df[df['Ημερομηνία Προγραμματισμού  Ένορκης'].isin(filtered_date)]
    if filtered_name_list:
        df = df[df['Επωνυμία Αποδέκτη'].isin(filtered_name_list)]
    if head:
        df = df.head(head)
    return df

def create_mapping_dict(df,col_index_1,col_index_2) :
     return dict(zip(df.iloc[:, col_index_1], df.iloc[:, col_index_2]))
     
def fill_lawyers(df, mapping_dikigoron_excel_file):
    # Load and prepare mapping dictionaries directly
        mapping_df = pd.read_excel(mapping_dikigoron_excel_file, usecols=[0, 1, 2], dtype=str)
        lawyer_info_map = create_mapping_dict(mapping_df,0,1)
        lawyer_name_map = create_mapping_dict(mapping_df,0,2)    
        # Apply mappings efficiently
        df = df.assign(
            Στοιχεία_Δικηγόρου=df['Υπογράφων Δικηγόρος Ένορκης'].map(lawyer_info_map).fillna('Unknown'),
            Ονοματεπώνυμο_Δικηγόρου=df['Υπογράφων Δικηγόρος Ένορκης'].map(lawyer_name_map).fillna('Unknown')
        )
        return df

def remove_trailing_zero(df,cols):
    for col in cols:
        df[col] = df[col].astype(str)#.str.rstrip('.0')
    return df

# Get date katathesis and create anafora_df

def get_date_katathesis(df) :
    date_katathesi_options= ["Κατάθεση μικροδ ΝΚΠολ Δ",'Ημ νια Κατάθεσης Αγωγής ΝΚπολ Δ']
    for option in date_katathesi_options :
        if option in df.columns :
            # print(f"Column date_katathesis : {option}")
            return option
        # else :
            # print(f"Column date_katathesis not found")
# def format_date_old(df, col):
#     if df[col].isna().sum() < len(df):
#         df[col] = df[col].fillna('1900-01-01')
#         df[col] = df[col].apply(lambda row: pd.to_datetime(row).strftime("%d/%m/%Y"))
#     else :
#         df[col] = df[col].fillna('')
#     return df[col] 


def get_number_anathesis(df):
    number_anathesis =  set()
    for item in df['Ανάθεση']:
        if isinstance(item, str):  # Check if the item is a string
            match = re.search(r'\d+', item)
            if match:
                number_anathesis.add(match.group())
    print(f"Anatheseis : {sorted(list(number_anathesis))} Count of anathesis : {len(number_anathesis)}")
    return number_anathesis


def get_number_anathesis_from_folder(folder) :
    match = re.search(r'\d+ης', folder)
    if not match:
        return None
    number = match.group()[:-2]
    return number


def format_anathesis_phrase(number_anathesis) :
    number_anathesis = [("Υποθέσεις " + str(x) + "ης Ανάθεσης") for x in number_anathesis]
    return number_anathesis

def create_file_list_based_on_list_ofeileton(list_ofeileton,mapping_files,path_to_search_enorkes) :
    return [os.path.join(path_to_search_enorkes,mapping_files.get(folder_name, "-")) for folder_name in list_ofeileton]

def handle_file_mapping(root, name, docx_file,mapping_files,count_full_name_occurrences,out_path):
    full_path = os.path.join(root, docx_file)
    mapping_files[name] = ''.join(mapping_files.get(name, '')) + full_path if count_full_name_occurrences > 1 else full_path
    shutil.copy(full_path, out_path)
    return True  # Stop further processing for this file
