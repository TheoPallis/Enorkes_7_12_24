import pandas as pd
from Main_Scripts.formatting  import format_date
from Config.Config import log_execution
# Change for_sxetika
@log_execution
def create_kliseis_df(df, antidikos_1, antidikos_2, antidikos_3, last_date, hours_col,
                      full_name_dikigorou, date_enorkis, sxetika1, sxetika2, sxetika3, sxetika4, sxetika5, sxetika6, sxetika7, sxetika8, sxetika9, sxetika10,sxetika11, sxetika12, sxetika13, sxetika14, sxetika15):
    
    print(f"Length of full name dikigorou : {len(df[full_name_dikigorou])}")
    print(f"Antidikos 1 length : {len(antidikos_1)}")
    print(f"Antidikos 2 length : {len(antidikos_2)}")
    print(f"Antidikos 3 length : {len(antidikos_3)}")
    print(f"Last date length : {len(last_date)}")
    print(f"Length of date enorkis : {len(date_enorkis)}")
    print(f"Sxetika 1 length : {len(sxetika1)}")
    print(f"Hours length : {len(hours_col)}")
    
    df = pd.DataFrame({
        'A/A': [x for x in range(1,len(df['Επωνυμία Αποδέκτη'])+1)],
        'Αντίδικος': df['Επωνυμία Αποδέκτη'],
        'Αντίδικος_1': antidikos_1,
        'Αντίδικος_2': antidikos_2,
        'Αντίδικος_3':antidikos_3,
        'Σχετικά1': sxetika1,
        'Σχετικά2' : sxetika2,
        'Σχετικά3' : sxetika3,
        'Σχετικά4' : sxetika4,
        'Σχετικά5' : sxetika5,
        'Σχετικά6': sxetika6,
        'Σχετικά7' : sxetika7,
        'Σχετικά8' : sxetika8,
        'Σχετικά9' : sxetika9,
        'Σχετικά10' : sxetika10,
        'Σχετικά11' : sxetika11,
        'Σχετικά12' : sxetika12,
        'Σχετικά13' : sxetika13,
        'Σχετικά14' : sxetika14,
        'Σχετικά15' : sxetika15,
        'Ημερομηνία_Αγωγής':  last_date,
        'Ημερομηνία_Ένορκης' : df[date_enorkis],
        'Ώρα ένορκης': hours_col,
        'Δικηγόρος' : df[full_name_dikigorou] ,
        'Ημερομηνία Κλήσης' : '-',
        'Αίθουσα' : 'στον 2ο όροφο, Αίθουσα Λέοντος Σοφού' 
    })
    df.replace(regex=True,inplace=True,to_replace="Ι.']",value="")
    return df


