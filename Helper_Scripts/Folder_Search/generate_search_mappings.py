import re

def generate_mappings_for_folder_search(anathesi_df) :
    pattern = r'\b\w\.\b'
    anathesi_list = list(anathesi_df['Ανάθεση'].apply(lambda x : str(x).split()[0].replace("η","").replace("ης","")))
    kodikos_list = list(anathesi_df['Κωδικός Ενέργειας'])
    list_ofeileton = list(anathesi_df['Επωνυμία Αποδέκτη'])
    list_ofeileton = [re.sub(pattern, '', x) for x in list_ofeileton]
    mapping_anatheseis = dict(zip(list_ofeileton,anathesi_list))
    mapping_kodikoi = dict(zip(list_ofeileton,kodikos_list))
    mapping_kodikos_check = dict(zip(list_ofeileton,"-"))
    return(list_ofeileton,mapping_anatheseis,mapping_kodikoi,mapping_kodikos_check)