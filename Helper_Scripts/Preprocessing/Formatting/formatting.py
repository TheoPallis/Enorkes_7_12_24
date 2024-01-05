def clean_anathesi_column(anathesi_df, anathesi_column = 'Ανάθεση',anathesi_word = 'ΑΝΑΘΕΣΗ'):
    anathesi_df[anathesi_column] =  anathesi_df[anathesi_column].apply(lambda x : str(x)[:str(x).index(anathesi_word)]+ 'Ανάθεση' if anathesi_word in x else x ) #Clean Ανάθεση
    return anathesi_df

def remove_nans(anathesi_df,col):
    anathesi_df[col] = anathesi_df[col].apply(lambda x :str(x).replace(".0","")).replace("nan","")
    return anathesi_df