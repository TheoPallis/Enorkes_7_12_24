import os
import shutil
import re
from Main_Scripts.Config import log_execution
from collections import defaultdict
def get_path_perimeter(number_anathesis,dedie_path):
    lowercase_anathesis = [re.sub(r'Ανάθεσης', 'ανάθεσης', item) if item != 'Υποθέσεις Ποινικό' else 'Υποθέσεις απο Ποινικά-Λαμία' for item in number_anathesis]
    # Additional condition for 'Υποθέσεις 133ης Ανάθεσης New'
    lowercase_anathesis = [re.sub(r' New$', '', item) if item == 'Υποθέσεις 133ης Ανάθεσης New' else item for item in lowercase_anathesis]
    number_anathesis.extend(lowercase_anathesis)
    # print(sorted(number_anathesis))
    path_list = [os.path.join(dedie_path, path) for path in os.listdir(dedie_path) if all(sub in path for sub in ["Υποθέσεις", "σης"]) and any(sub in path for sub in number_anathesis)]
    return path_list

def file_filter(file, first_word_folder):
    include_conditions = [first_word_folder in file, "ΣΧΕΔΙΟ ΑΓΩΓΗΣ ΔΕΔΔΗΕ" in file,'ΑΓΩΓΗ ΔΕΔΔΗΕ' in file,'ΑΓΩΓΗ_ΔΕΔΔΗΕ' in file]
    exclude_conditions = ["ηρεξούσιο", "Προτάσεις", "Σχετικών", "ΒΕΒΑΙΗ", "οτάσεις", "ενορκη", "ΛΑΜΑΚΙΑ"]
    additional_valid_combinations = ["ΛΑΜΑΚΙΑ", "ΒΕΒΑΙΗ", "ΑΥΘΑΙΡΕΤΗ", "ΠΑΡΑΚΑΜΨΗ"]

    # Check for initial inclusion and exclusion conditions
    if any(include_conditions) and all(term not in file for term in exclude_conditions):
        return True

    # Check for additional valid combinations
    if "ΑΓΩΓΗ" in file and any(combination in file for combination in additional_valid_combinations):
        return True
@log_execution
def get_all_folders(dedie_path, list_ofeileton, df1, out_path, mapping_anatheseis, mapping_kodikoi, number_anathesis):
    """Search for specific folders and files, and map them to the dataframe."""
    mapping_folders   = {name: ["-"] for name in list_ofeileton}
    mapping_files = {name: "-" for name in list_ofeileton}
    path_list = get_path_perimeter(number_anathesis, dedie_path)
    extra = []
    @log_execution
    def path_processor(path,mapping_files):
                    for root, _, files in os.walk(path):
                        match = re.search(r'\d+ης', root)
                        if not match:
                            continue
                        number = match.group()[:-2]

                        for name in list_ofeileton:
                            if mapping_anatheseis[name] != number:
                                continue
                            if "-" in root :
                                first_word_folder = os.path.basename(root).split("-")[0]
                            else :
                                 first_word_folder = os.path.basename(root).split()[0]
                            pattern = re.compile(fr"{re.escape(str(mapping_kodikoi[name]))}[-_]?")
                            
                            if any(pattern.search(file) for file in files): 
                                
                                if mapping_folders[name] == ["-"]:
                                    mapping_folders[name] = root
                                
                                else :
                                     mapping_folders[name] = mapping_folders[name] + "/"+ root 

                                for file in files:
                                    if file.endswith(".docx") and file_filter(file, first_word_folder):
                                        full_path = os.path.join(root, file)
                                        mapping_files[name] = full_path
                                        shutil.copy(full_path, out_path)
                       
                            continue  # No need to check further if folder already found
    for path in path_list:
        path_processor(path,mapping_files)

    df1['Φάκελος'] = df1['Αντίδικος'].map(mapping_folders)
    print(extra)
    return mapping_files



