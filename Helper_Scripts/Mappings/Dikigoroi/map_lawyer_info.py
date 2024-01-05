import os
import pandas as pd
# TODO Define file pathc -> Import from path config file

mapping_dikigoron_excel_file = os.path.join('..', 'Data', 'Mappings', 'ΛΙΣΤΑ ΔΙΚΗΓΟΡΩΝ ΕΝΟΡΚΩΝ.xlsx')

def read_lawyer_excel(mapping_dikigoron_excel_file):
    return pd.read_excel(mapping_dikigoron_excel_file)

def map_lawyer_info(anathesi_df, mapping_dikigoron_excel_file, key_column, value_column, new_column_name):
    dikigoroi_df = read_lawyer_excel(mapping_dikigoron_excel_file)
    mapping = dict(zip(dikigoroi_df.iloc[:, key_column], dikigoroi_df.iloc[:, value_column]))
    anathesi_df[new_column_name] = anathesi_df['Υπογράφων Δικηγόρος Ένορκης'].map(mapping)
    return anathesi_df

