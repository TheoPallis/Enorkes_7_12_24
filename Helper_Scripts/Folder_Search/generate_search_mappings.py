from collections import defaultdict
import re
from Config.Config import log_execution
@log_execution
def generate_mappings_for_folder_search(anathesi_df) :
    pattern = r'\b\w\.\b'
    list_ofeileton = list(anathesi_df['Επωνυμία Αποδέκτη'])
    list_ofeileton = [re.sub(pattern, '', str(x)) for x in list_ofeileton]
    anathesi_list = list(anathesi_df['Ανάθεση'].apply(lambda x : str(x).split()[0].replace("η","").replace("ης","")))
    mapping_anatheseis = dict(zip(list_ofeileton,anathesi_list))    
    kodikos_list = list(anathesi_df['Κωδικός Ενέργειας'])
    ordered_dict = {}
    for key, value in zip(list_ofeileton, kodikos_list):
        if key not in ordered_dict:
            ordered_dict[key] = []
        ordered_dict[key].append(value)
    extra = set()
    for k,v in ordered_dict.items():
        if len(v) > 1:
            extra.add(k)
    print("Dupes : ",extra)

    return(list_ofeileton,mapping_anatheseis,ordered_dict)