import os
import shutil
import re
from Config.Config import log_execution
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
def get_all_folders(dedie_path, list_ofeileton, out_path, mapping_anatheseis, mapping_kodikoi, number_anathesis):
    """Search for specific folders and files, and map them to the dataframe."""
    mapping_folders = {name: ["-"] for name in list_ofeileton}
    mapping_files = {name: "-" for name in list_ofeileton}
    path_list = get_path_perimeter(number_anathesis, dedie_path)

    def find_matching_code_files(root, files, current_codes, folder_mapping, file_mapping, name, output_path):
        """Find files matching specific codes and update mappings."""
        for current_code in current_codes: 
            for file in files:
                if current_code in file:
                    print(f"    Found matching file: {file} in {root}")
                    if folder_mapping[name] == ["-"]:
                        folder_mapping[name] = [root]
                    else:
                        folder_mapping[name].append(root)
                    if current_code in mapping_kodikoi[name]:
                        mapping_kodikoi[name].remove(current_code)
                    break  # Stop checking other codes for this file
            
            if file.endswith(".docx") and file_filter(file, root):
                file_mapping[name] = os.path.join(root, file)
                shutil.copy(file_mapping[name], output_path)
        return mapping_kodikoi, folder_mapping, file_mapping

    @log_execution
    def process_single_path(path, folder_mapping, file_mapping, mapping_kodikoi):
        """Process each path for folder and file mapping."""
        for root, _, files in os.walk(path):
            match = re.search(r'\d+ης', root)
            if not match:
                continue
            folder_number = match.group()[:-2]

            for name in list_ofeileton:
                if mapping_anatheseis.get(name) != folder_number:
                    continue

                current_codes = mapping_kodikoi[name]
    
                if not current_codes:
                    continue

                mapping_kodikoi, folder_mapping, file_mapping = find_matching_code_files(
                    root=root,
                    files=files,
                    current_codes=current_codes,
                    folder_mapping=folder_mapping,
                    file_mapping=file_mapping,
                    name=name,
                    output_path=out_path
                )
        return mapping_kodikoi, folder_mapping, file_mapping

    for path in path_list:
        mapping_kodikoi, mapping_folders, mapping_files = process_single_path(
            path, mapping_folders, mapping_files, mapping_kodikoi
        )

    return mapping_folders, mapping_files
