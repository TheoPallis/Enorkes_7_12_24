import sys
sys.path.append("..") 
import pandas as pd
from itertools import chain
from pandas.testing import assert_frame_equal
from Main_Scripts.formatting import (
    get_number_anathesis,
    remove_trailing_zero,
    remove_invalid_dates_anatheseis_format_dates_fill_na,
    filter_df,
    fill_lawyers,
    format_anathesis_phrase,
    create_file_list_based_on_list_ofeileton)
from Main_Scripts.folder_search import get_all_folders
from Main_Scripts.Extact_Text import get_text_and_date
from Main_Scripts.assign_hours import assign_hours
from Helper_Scripts.Folder_Search.generate_search_mappings import generate_mappings_for_folder_search
from Helper_Scripts.DF_Columns.df1 import create_path_df
from Helper_Scripts.DF_Columns.df2 import create_anafora_df
from Helper_Scripts.DF_Columns.df3 import create_kliseis_df
from Helper_Scripts.Create_Excel_File.Create_Excel_File import create_excel_file,load_excel_file
from Config.Config import out_path, mapping_dikigoron_excel_file, dedie_path

def main_function(excel_file_path,filtered_date=None,filtered_name_list=None,head=None,anathesi=None) :
    anathesi_df = load_excel_file(excel_file_path)
    anathesi_df = remove_invalid_dates_anatheseis_format_dates_fill_na(anathesi_df)
    anathesi_df = filter_df(anathesi_df,filtered_date,filtered_name_list,head,anathesi)
    anathesi_df = fill_lawyers(anathesi_df,mapping_dikigoron_excel_file)
    anathesi_df = remove_trailing_zero(anathesi_df,['ΓΑΚ','ΕΑΚ'])
    anathesi_df = assign_hours(anathesi_df)
    # Generate folder search mappings
    list_ofeileton,mapping_anatheseis,mapping_kodikoi = generate_mappings_for_folder_search(anathesi_df)
    number_anathesis = get_number_anathesis(anathesi_df)
    number_anathesis = format_anathesis_phrase(number_anathesis)
    path_df = create_path_df(anathesi_df)
        
    mapping_folders, mapping_files, mapping_kodikoi= get_all_folders(
    dedie_path,
    list_ofeileton,
    path_df,
    out_path,
    mapping_anatheseis,
    mapping_kodikoi,
    number_anathesis
    )
    print("Mapping folders : ", mapping_folders)
    print("Mapping files : ",mapping_files)
    df2 = create_anafora_df(anathesi_df)
    file_list = create_file_list_based_on_list_ofeileton(list_ofeileton, mapping_files)
    # Extract text and create kliseis_df
    antidikos_1, antidikos_2, antidikos_3, last_date,sxetika1, sxetika2, sxetika3, sxetika4, sxetika5, sxetika6,sxetika7, sxetika8,sxetika9,sxetika10,sxetika11,sxetika12,sxetika13,sxetika14,sxetika15  = get_text_and_date(file_list, dedie_path)  #  sxetika9, sxetika10        
    # Create kliseis df
    #temp
    # anathesi_df['hours'] = 0
    hours_col = anathesi_df['hours']
    df3 = create_kliseis_df(anathesi_df,antidikos_1,antidikos_2,antidikos_3,last_date,hours_col,'Ονοματεπώνυμο_Δικηγόρου','Ημερομηνία Προγραμματισμού  Ένορκης', sxetika1, sxetika2, sxetika3, sxetika4, sxetika5, sxetika6, sxetika7, sxetika8, sxetika9, sxetika10,sxetika11, sxetika12, sxetika13, sxetika14, sxetika15)
    create_excel_file(path_df,df2,df3)
    return mapping_files,df3,mapping_folders


from pandas.testing import assert_frame_equal
def test_main_function() :
    test_excel_file_path = r"C:\Users\pallist\Desktop\Desktop\ΤΡΕΧΟΝΤΑ\Ένορκες\90 12_12.xlsx"
    output_excel_file_path = r"C:\Users\pallist\Desktop\Desktop\ΤΡΕΧΟΝΤΑ\Testing Folder\Auto_enorkes_28_11_24 _sxetika_minimal\UATs\testing_file.xlsx"
    _,test_kliseis_df,_ = main_function(test_excel_file_path)
    kliseis_df = pd.read_excel(output_excel_file_path,sheet_name='Κλήσεις')
    assert_frame_equal(kliseis_df, test_kliseis_df,atol=0.04)
    