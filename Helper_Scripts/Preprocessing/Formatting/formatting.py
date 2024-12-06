import re
import pandas as pd
from Config.Config import log_execution

def load_excel_file(path):
    return pd.read_excel(path,dtype=str)

def remove_invalid_fill_na_convert_time(anathesi_df)  : 
    anathesi_df = anathesi_df[~anathesi_df['Ημερομηνία Προγραμματισμού  Ένορκης'].str.contains(r'[α-ωΑ-Ω]', regex=True,na=False)]    
    anathesi_df = anathesi_df.dropna(subset=['Ανάθεση'])
    anathesi_df['Ημερομηνία Προγραμματισμού  Ένορκης'] = anathesi_df['Ημερομηνία Προγραμματισμού  Ένορκης'].fillna('1900-01-01 00:00')
    anathesi_df['Ημερομηνία Προγραμματισμού  Ένορκης'] = pd.to_datetime(anathesi_df['Ημερομηνία Προγραμματισμού  Ένορκης'], format='ISO8601',dayfirst=True)
    if 'Ημ νια Κατάθεσης Αγωγής ΝΚπολ Δ' in anathesi_df.columns :
        anathesi_df['Ημ νια Κατάθεσης Αγωγής ΝΚπολ Δ'] = anathesi_df['Ημ νια Κατάθεσης Αγωγής ΝΚπολ Δ'].fillna('1900-01-01 00:00')
        anathesi_df['Ημ νια Κατάθεσης Αγωγής ΝΚπολ Δ'] = pd.to_datetime(anathesi_df['Ημ νια Κατάθεσης Αγωγής ΝΚπολ Δ'], format='ISO8601',dayfirst=True)

    # Convert the date column to datetime format
    
    anathesi_df = anathesi_df.fillna("")
    return anathesi_df

def filter_df(anathesi_df,filtered_date,filtered_name_list,head) :
    if filtered_date is not None and filtered_date != [] :
        filtered_date2 = [pd.to_datetime(item, dayfirst=True) for item in filtered_date]
        anathesi_df = anathesi_df[anathesi_df['Ημερομηνία Προγραμματισμού  Ένορκης'].isin(filtered_date2)]
    if filtered_name_list is not None  and filtered_name_list != [] :
        anathesi_df = anathesi_df[anathesi_df['Επωνυμία Αποδέκτη'].isin(filtered_name_list)]  
    if head is not None :
        anathesi_df = anathesi_df.head(head)
    return anathesi_df

def fill_lawyers(anathesi_df, mapping_dikigoron_excel_file):
    mapping_df = pd.read_excel(mapping_dikigoron_excel_file, usecols=[0, 1, 2], dtype=str)
    # Create mapping dictionaries once
    lawyer_info_map = dict(zip(mapping_df.iloc[:, 0], mapping_df.iloc[:, 1]))
    lawyer_name_map = dict(zip(mapping_df.iloc[:, 2], mapping_df.iloc[:, 0]))
    # Apply mappings
    anathesi_df['Στοιχεία_Δικηγόρου'] = anathesi_df['Υπογράφων Δικηγόρος Ένορκης'].map(lawyer_info_map).fillna('Unknown')
    anathesi_df['Ονοματεπώνυμο_Δικηγόρου'] = anathesi_df['Υπογράφων Δικηγόρος Ένορκης'].map(lawyer_name_map).fillna('Unknown')
    return anathesi_df


def remove_trailing_zero(anathesi_df,cols):
    for col in cols :
        anathesi_df[col] = anathesi_df[col].apply(lambda x :str(x).replace(".0",""))
    return anathesi_df

# Get date katathesis and create anafora_df

def get_date_katathesis(df) :
    date_katathesi_options= ["Κατάθεση μικροδ ΝΚΠολ Δ",'Ημ νια Κατάθεσης Αγωγής ΝΚπολ Δ']
    for option in date_katathesi_options :
        if option in df.columns :
            # print(f"Column date_katathesis : {option}")
            return option
        # else :
            # print(f"Column date_katathesis not found")


def format_date(anathesi_df, col):
    if anathesi_df[col].isna().sum() < len(anathesi_df):
        anathesi_df[col] = anathesi_df[col].fillna('1900-01-01')
        anathesi_df[col] = anathesi_df[col].apply(lambda row: pd.to_datetime(row).strftime("%d/%m/%Y"))
    else :
        anathesi_df[col] = anathesi_df[col].fillna('')
    return anathesi_df[col] 


def get_number_anathesis(anathesi_df):
    number_anathesis =  set()
    for item in anathesi_df['Ανάθεση']:
        if isinstance(item, str):  # Check if the item is a string
            match = re.search(r'\d+', item)
            if match:
                number_anathesis.add(match.group())
    print(f"Anatheseis : {sorted(list(number_anathesis))} Count of anathesis : {len(number_anathesis)}")
    return number_anathesis

    


def format_anathesis_phrase(number_anathesis) :
    number_anathesis = [("Υποθέσεις " + str(x) + "ης Ανάθεσης") for x in number_anathesis]
    return number_anathesis

def create_file_list_based_on_list_ofeileton(list_ofeileton,mapping_files) :
    return [mapping_files.get(folder_name, "-") for folder_name in list_ofeileton]
    
    