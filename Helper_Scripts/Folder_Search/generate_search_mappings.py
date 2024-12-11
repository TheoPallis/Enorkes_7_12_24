from collections import defaultdict
import re
from Config.Config import log_execution

def create_mapping_kodikon_dict(list_ofeileton, kodikos_list):
    mapping_kodikon = {}
    for key, value in zip(list_ofeileton, kodikos_list):
        if key not in mapping_kodikon:
            mapping_kodikon[key] = []
        mapping_kodikon[key].append(value)
    return mapping_kodikon

def get_names_with_multiple_codes(mapping_kodikon):
        extra = set()
        for k,v in mapping_kodikon.items():
            if len(v) > 1:
                extra.add(k)
        print("Dupes : ",extra)

def generate_mappings_for_folder_search(df) :
    pattern = r'\b\w\.\b'
    list_ofeileton = list(df['Επωνυμία Αποδέκτη'])
    list_ofeileton = [re.sub(pattern, '', str(x)) for x in list_ofeileton]
    anathesi_list = list(df['Ανάθεση'].apply(lambda x : str(x).split()[0].replace("η","").replace("ης","")))
    mapping_anatheseis = dict(zip(list_ofeileton,anathesi_list))    
    kodikos_list = list(df['Κωδικός Ενέργειας'])
    mapping_kodikon = create_mapping_kodikon_dict(list_ofeileton, kodikos_list)
    get_names_with_multiple_codes(mapping_kodikon)
    return(list_ofeileton,mapping_anatheseis,mapping_kodikon)