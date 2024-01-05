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