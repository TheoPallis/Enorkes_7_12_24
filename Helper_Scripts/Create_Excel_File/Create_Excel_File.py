import pandas as pd

def create_excel_file(df1,df2,df3,df4,df5,df6) :
    with pd.ExcelWriter('Βάση_auto.xlsx', engine='openpyxl') as writer:
        df1.to_excel(writer, sheet_name='Ένορκες', index=False)
        df2.to_excel(writer, sheet_name='Αναφορά', index=False)
        df3.to_excel(writer, sheet_name='Κλήσεις', index=False)
        df4.to_excel(writer, sheet_name='Συναρτήσεις', index=False)
        df5.to_excel(writer, sheet_name='Checks', index=False)
        df6.to_excel(writer, sheet_name='Checklist', index=False)