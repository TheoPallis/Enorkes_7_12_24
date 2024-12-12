import os
import shutil
import re
from Config.Config import log_execution
from collections import defaultdict
from formatting import get_number_anathesis_from_folder,handle_file_mapping
def get_only_the_relevant_paths_for_arxeio_anathesis(number_anathesis, dedie_path):
    """Generate a list of paths matching the perimeter conditions."""
    print(f"Starting get_only_the_relevant_paths_for_arxeio_anathesis with number_anathesis: {number_anathesis} and dedie_path: {dedie_path}")
    lowercase_anathesis = [
        re.sub(r'Ανάθεσης', 'ανάθεσης', item) if item != 'Υποθέσεις Ποινικό' else 'Υποθέσεις απο Ποινικά-Λαμία'
        for item in number_anathesis
    ]
    lowercase_anathesis = [
        re.sub(r' New$', '', item) if item == 'Υποθέσεις 133ης Ανάθεσης New' else item for item in lowercase_anathesis
    ]
    number_anathesis.extend(lowercase_anathesis)
    return [
        os.path.join(dedie_path, path) for path in os.listdir(dedie_path)
        if all(sub in path for sub in ["Υποθέσεις", "σης"]) and any(sub in path for sub in number_anathesis)
    ]

def file_is_agogi(file, first_word_folder):
    """Filter files based on inclusion and exclusion conditions."""
     
    include_conditions = [
        first_word_folder in file,
        "ΣΧΕΔΙΟ ΑΓΩΓΗΣ ΔΕΔΔΗΕ" in file,
        'ΑΓΩΓΗ ΔΕΔΔΗΕ' in file,
        'ΑΓΩΓΗ_ΔΕΔΔΗΕ' in file
    ]
    exclude_conditions = ["ηρεξούσιο", "Προτάσεις", "Σχετικών", "ΒΕΒΑΙΗ", "οτάσεις", "ενορκη"]
    additional_valid_combinations = ["ΛΑΜΑΚΙΑ", "ΑΥΘΑΙΡΕΤΗ", "ΠΑΡΑΚΑΜΨΗ"]

    if any(include_conditions) and all(term not in file for term in exclude_conditions) and file.endswith(".docx"):
        return True
    if "ΑΓΩΓΗ" in file and any(comb in file for comb in additional_valid_combinations) and file.endswith(".docx"):
        return True
    return False

def get_all_folders(dedie_path, list_ofeileton, df1, out_path, mapping_anatheseis, mapping_kodikoi,  number_anathesis):
    """Search for specific folders and files, and map them to the dataframe."""
    mapping_folders = {name: [""] for name in list_ofeileton}
    mapping_files = {name: "" for name in list_ofeileton}
    path_list = get_only_the_relevant_paths_for_arxeio_anathesis(number_anathesis, dedie_path)
    print(mapping_kodikoi)

    for path in path_list:
            folder_names = [folder.name for folder in os.scandir(path)]
            print(f"Processing Path: {path}")

            for root, _, files in os.walk(path):
                print("     Processing root:", root)
                number =  get_number_anathesis_from_folder(root)
                if number == None :
                    continue
                for name in list_ofeileton:
                    if mapping_anatheseis[name] != number:
                        continue
                
                    first_word_folder = os.path.basename(root).split()[0]
                    full_name = ' '.join(name.split(' ')[:2])
                    count_full_name_occurrences = (sum(len(re.findall(full_name, item)) for item in folder_names))
                      
                    for file in files:
                        if any(kodikos in file for kodikos in mapping_kodikoi.get(name, [])):
                            if count_full_name_occurrences > 1:
                                mapping_folders[name] = ''.join(mapping_folders.get(name, '')) + root if root not in mapping_folders.get(name, '') else mapping_folders[name]
                            else:
                                mapping_folders[name] = root

                            for docx_file in (f for f in files if  file_is_agogi(f, first_word_folder)) :
                                if handle_file_mapping(root, name, docx_file,mapping_files,count_full_name_occurrences,out_path):
                                    break
                            break
         
    df1['Φάκελος'] = df1['Αντίδικος'].map(mapping_folders)

    return mapping_folders,mapping_files, mapping_kodikoi

