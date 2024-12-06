import pandas as pd
from Helper_Scripts.Preprocessing.Formatting.formatting import format_date,remove_trailing_zero
from Config.Config import log_execution
@log_execution
def create_anafora_df(anathesi_df):
    df2 = pd.DataFrame({
    'A/A': [x for x in range(1,len(anathesi_df['Επωνυμία Αποδέκτη'])+1)],
        'Αντίδικος': anathesi_df['Επωνυμία Αποδέκτη'],
        'Διαδικασία': anathesi_df['Διαδικασία'],
        'Δικαστικό Ίδρυμα': anathesi_df['Δικαστικό Ίδρυμα'],
        # 'Κατάθεση μικροδ ΝΚΠολ Δ': format_date(anathesi_df,'Κατάθεση μικροδ ΝΚΠολ Δ') if 'Κατάθεση μικροδ ΝΚΠολ Δ' in anathesi_df.columns else "" ,
        # 'Ημερομηνία Κατάθεσης': format_date(anathesi_df,'Ημ νια Κατάθεσης Αγωγής ΝΚπολ Δ') if 'Ημ νια Κατάθεσης Αγωγής ΝΚπολ Δ' in anathesi_df.columns else "" ,
        'ΓΑΚ':   anathesi_df['ΓΑΚ'],
        'ΕΑΚ':anathesi_df['ΕΑΚ']
    })

    return df2


import pandas as pd

