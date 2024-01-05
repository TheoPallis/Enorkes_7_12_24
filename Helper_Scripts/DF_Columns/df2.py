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

