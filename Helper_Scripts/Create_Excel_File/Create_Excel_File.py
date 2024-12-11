import pandas as pd
import datetime
import os
from Helper_Scripts.Formtat_Excel_File.Format_Excel_File import format_df
from Config.Config import log_execution


def load_excel_file(path):
    return pd.read_excel(path,dtype=str)

def generate_timestamp_filename(filename_prefix,type):
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%d-%m-%y_%H-%M")
    return f"{filename_prefix}_{timestamp}{type}"

def create_excel_file(df1,df2,df3):#,df4,df5,df6) :
    if not os.path.exists("Output"):
        os.makedirs("Output")
    output = "Output"
    filename = generate_timestamp_filename('Βάση_auto','.xlsx')
    filename = os.path.join(output,filename)
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        df1.to_excel(writer, sheet_name='Ένορκες', index=False)
        df2.to_excel(writer, sheet_name='Αναφορά', index=False)
        df3.to_excel(writer, sheet_name='Κλήσεις', index=False)
        # format_df(filename)
        os.startfile(filename)
        # df4.to_excel(writer, sheet_name='Συναρτήσεις', index=False)
        # df5.to_excel(writer, sheet_name='Checks', index=False)
        # df6.to_excel(writer, sheet_name='Checklist', index=False)
