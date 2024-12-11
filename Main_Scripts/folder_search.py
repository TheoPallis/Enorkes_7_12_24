import os
import shutil
import re
from Config.Config import log_execution
from collections import defaultdict

def get_path_perimeter(number_anathesis, dedie_path):
    """Generate a list of paths matching the perimeter conditions."""
    print(f"Starting get_path_perimeter with number_anathesis: {number_anathesis} and dedie_path: {dedie_path}")
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

def file_filter(file, first_word_folder):
    """Filter files based on inclusion and exclusion conditions."""
    include_conditions = [
        first_word_folder in file,
        "ΣΧΕΔΙΟ ΑΓΩΓΗΣ ΔΕΔΔΗΕ" in file,
        'ΑΓΩΓΗ ΔΕΔΔΗΕ' in file,
        'ΑΓΩΓΗ_ΔΕΔΔΗΕ' in file
    ]
    exclude_conditions = ["ηρεξούσιο", "Προτάσεις", "Σχετικών", "ΒΕΒΑΙΗ", "οτάσεις", "ενορκη"]
    additional_valid_combinations = ["ΛΑΜΑΚΙΑ", "ΑΥΘΑΙΡΕΤΗ", "ΠΑΡΑΚΑΜΨΗ"]

    if any(include_conditions) and all(term not in file for term in exclude_conditions):
        return True
    if "ΑΓΩΓΗ" in file and any(comb in file for comb in additional_valid_combinations):
        return True
    return False

def get_all_folders(dedie_path, list_ofeileton, df1, out_path, mapping_anatheseis, mapping_kodikoi,  number_anathesis):
    """Search for specific folders and files, and map them to the dataframe."""
    mapping_folders = {name: [""] for name in list_ofeileton}
    mapping_files = {name: "" for name in list_ofeileton}
    path_list = get_path_perimeter(number_anathesis, dedie_path)
    print(mapping_kodikoi)
    for path in path_list:
            folder_names = [folder.name for folder in os.scandir(path)]
            print(f"Processing Path: {path}")
            for root, _, files in os.walk(path):
                print("     Processing root:", root)
                match = re.search(r'\d+ης', root)
                if not match:
                    continue
                number = match.group()[:-2]
                for name in list_ofeileton:
                    # print("         Processing name:", name)
                    if mapping_anatheseis[name] != number:
                        continue
                    first_word_folder = os.path.basename(root).split()[0]
    
                    for file in files:
                            full_name  = name.split(' ')[:2]
                            full_name = ' '.join(full_name)
                            count_full_name_occurrences = (sum(len(re.findall(full_name, item)) for item in folder_names))
                            # print("Full Name:", full_name)
                            if count_full_name_occurrences > 1:
                                 for kodikos in mapping_kodikoi[name]:
                                      if kodikos in file :
                                            print("             Found matching folder for :", kodikos," for:", name," with mutliple occurrences")
                                            mapping_folders[name] = ''.join(mapping_folders[name]) +  root if root not in mapping_folders[name] else mapping_folders[name]
                                            for file in files:
                                                if file.endswith(".docx") and file_filter(file, first_word_folder):
                                                    full_path = os.path.join(root, file)
                                                    mapping_files[name] =   ''.join(mapping_files[name]) + full_path
                                                    shutil.copy(full_path, out_path)
                                                    break
                                            continue  # No need to check further if folder already found                            
                            
                            
                            else:
                                if mapping_kodikoi[name][0] in file :
                                    # print("             Found matching folder for:", name," with a single occurrence")
                                    mapping_folders[name] = root
                                    for file in files:
                                        if file.endswith(".docx") and file_filter(file, first_word_folder):
                                            full_path = os.path.join(root, file)
                                            mapping_files[name] = full_path
                                            print("             Found matching file for:", name, " at:", full_path)
                                            shutil.copy(full_path, out_path)
                                            break
                                    continue  # No need to check further if folder already found
                                                        
                            
    df1['Φάκελος'] = df1['Αντίδικος'].map(mapping_folders)

    return mapping_folders,mapping_files, mapping_kodikoi

