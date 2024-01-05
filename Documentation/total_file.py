

@@ Script -> Create_Excel_File.py

import pandas as pd

def create_excel_file(df1,df2,df3,df4,df5,df6) :
    with pd.ExcelWriter('Βάση_auto.xlsx', engine='openpyxl') as writer:
        df1.to_excel(writer, sheet_name='Ένορκες', index=False)
        df2.to_excel(writer, sheet_name='Αναφορά', index=False)
        df3.to_excel(writer, sheet_name='Κλήσεις', index=False)
        df4.to_excel(writer, sheet_name='Συναρτήσεις', index=False)
        df5.to_excel(writer, sheet_name='Checks', index=False)
        df6.to_excel(writer, sheet_name='Checklist', index=False)



@@ Script -> df1.py


df1 = pd.DataFrame({
 'A/A': [x for x in range(1,len(anathesi_df['Επωνυμία Αποδέκτη'])+1)],
    'Αντίδικος': anathesi_df['Επωνυμία Αποδέκτη'],
    'Ανάθεση' : anathesi_df['Ανάθεση'].apply(lambda x : str(x)[:str(x).index(anathesi_word)]+ 'Ανάθεση'), #Clean Ανάθεση
    'ΔΙΚΑΣΤΙΚΟ ΙΔΡΥΜΑ': "",
    'Διαδκασία': "",

    'Μάρτυρας' : anathesi_df['Μάρτυρας'],
    'Φάκελος' : "",
})



df1['Φάκελος'] = (r"\\lawoffice\\Applications\\ScanDocs\\ΔΕΔΔΗΕ scandocs\\" 
                  + df1['Φάκελος'].apply(lambda x: get_folder_or_filename(x, -3)) # For subfolders (eg Θεσσαλονίκη)
                   + "\\" 
                  + df1['Φάκελος'].apply(lambda x: get_folder_or_filename(x, -2)) 
                  + "\\" 
                  + df1['Φάκελος'].apply(lambda x: get_folder_or_filename(x, -1)))

df1['Φάκελος'] = df1['Φάκελος'].astype(str) 
df1['Φάκελος'] =df1['Φάκελος'].apply(lambda x : x.replace("ΦΑΚΕΛΟΙ ΕΝΟΡΚΩΝ",""))





# Apply the function to the 'Φάκελος' column
df1['Φάκελος'] = df1['Φάκελος'].apply(write_hyperlink)

def write_hyperlink(link):
    # Using the openpyxl syntax to specify a hyperlink
    return f'=HYPERLINK("{link}", "{link}")'




@@ Script -> df2.py

df2 = pd.DataFrame({
 'A/A': [x for x in range(1,len(anathesi_df['Επωνυμία Αποδέκτη'])+1)],
    'Αντίδικος': anathesi_df['Επωνυμία Αποδέκτη'],
    'Διαδικασία': anathesi_df['Διαδικασία'],
    'Δικαστικό Ίδρυμα': anathesi_df['Δικαστικό Ίδρυμα'],
    # 'Ημερομηνία Κατάθεσης': anathesi_df['Date_Katathesi'],
    'Ημερομηνία Κατάθεσης': "-",
    
    'Ημερομηνία Κατάθεσης2': "",
    'ΓΑΚ':  anathesi_df['ΓΑΚ'].apply(lambda x :str(x).replace(".0","")).replace("nan",""),
    'ΕΑΚ' : anathesi_df['ΕΑΚ'].apply(lambda x :str(x).replace(".0","")).replace("nan","")
})





@@ Script -> df3.py

df3 = pd.DataFrame({
    'A/A': [x for x in range(1,len(anathesi_df['Επωνυμία Αποδέκτη'])+1)],
    'Αντίδικος': anathesi_df['Επωνυμία Αποδέκτη'],
    'Αντίδικος_1': antidikos_1,
    'Αντίδικος_2': antidikos_2,
    'Αντίδικος_3':antidikos_3,
    'Ημερομηνία_Αγωγής':  last_date,
    'Ημερομηνία_Ένορκης' : "-",
    'Ώρα ένορκης': hours_col,
    'Δικηγόρος' : anathesi_df['ΔΙΚΗΓΟΡΟΣ_full'] ,
    'Ημερομηνία Κλήσης' : '-',
    'Αίθουσα' : AITHOUSA
})
# df3['Ημερομηνία_Ένορκης']= pd.to_datetime(anathesi_df['Ημερομηνία Προγραμματισμού  Ένορκης'], errors='coerce')
# df3['Ημερομηνία_Ένορκης'] = df3['Ημερομηνία_Ένορκης'].dt.strftime('%d/%m/%Y')
df3.replace(regex=True,inplace=True,to_replace="Ι.']",value="")
# df3

