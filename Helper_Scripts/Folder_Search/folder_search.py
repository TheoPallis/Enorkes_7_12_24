import os
import shutil

def get_all_folders(path, list_ofeileton, df1, out_path,mapping_anatheseis,mapping_kodikoi,mapping_kodikos_check,mode):
    """Search for specific folders and files, and map them to the dataframe."""
    mapping_folders = {name: "-" for name in list_ofeileton} #Now that it returns one folder it is not needed
    mapping_files = {name: "-" for name in list_ofeileton}
    for root, _, files in os.walk(path):
        if "Υποθέσεις" in root and "ανάθεσης" in root:
            for name in list_ofeileton:
                 first_word_folder = os.path.basename(root).split()[0]
                 if mapping_anatheseis[name] in str(root):
                    if mode == 'name' :
                                if first_word_folder in name:

                                    mapping_folders[name] = root
                                    nea_agogi_found = False  # Flag to track if ΝΕΑ ΑΓΩΓΗ is found
                                
                                    for file in files:
                                        full_path = os.path.join(root, file)
                    
                                        if file.endswith(".docx"):
                                            # Check for 'ΝΕΑ ΑΓΩΓΗ' in file name
                                            # if "ΝΕΑ ΑΓΩΓΗ" in file:
                                            #     nea_agogi_found = True
                                            #     mapping_files[name] = full_path
                                            #     shutil.copy(full_path, out_path)
                                            #     break

                                            include_conditions = [first_word_folder in file, "ΣΧΕΔΙΟ ΑΓΩΓΗΣ ΔΕΔΔΗΕ" in file]
                                            exclude_conditions = ["ηρεξούσιο", "Προτάσεις", "Σχετικών", "ΒΕΒΑΙΗ", "οτάσεις", "ενορκη", "ΛΑΜΑΚΙΑ"]

                                            if any(include_conditions) and all(term not in file for term in exclude_conditions):
                                                if not nea_agogi_found:  # If 'ΝΕΑ ΑΓΩΓΗ' not already found
                                                    mapping_files[name] = full_path
                                                    shutil.copy(full_path, out_path)
                                                    print(f"!! Found : Ανάθεση : {mapping_anatheseis[name]}  Folder : {os.path.basename(root)}  Files : {files} Selected file : {file}")
                                                    break
                                            elif first_word_folder not in file:
                                                print(f"Not found : {first_word_folder} : {file}")

                    elif mode == 'number' :
                        if str(mapping_kodikoi[name]) in str(files):
                            print(str(mapping_kodikoi[name]),str(files))
                            mapping_folders[name] = root
                            nea_agogi_found = False  # Flag to track if ΝΕΑ ΑΓΩΓΗ is found
                        
                            for file in files:
                                full_path = os.path.join(root, file)
            
                                if file.endswith(".docx"):
                                    # Check for 'ΝΕΑ ΑΓΩΓΗ' in file name
                                    # if "ΝΕΑ ΑΓΩΓΗ" in file:
                                    #     nea_agogi_found = True
                                    #     mapping_files[name] = full_path
                                    #     shutil.copy(full_path, out_path)
                                    #     break

                                    include_conditions = [first_word_folder in file, "ΣΧΕΔΙΟ ΑΓΩΓΗΣ ΔΕΔΔΗΕ" in file]
                                    exclude_conditions = ["ηρεξούσιο", "Προτάσεις", "Σχετικών", "ΒΕΒΑΙΗ", "οτάσεις", "ενορκη", "ΛΑΜΑΚΙΑ"]

                                    if any(include_conditions) and all(term not in file for term in exclude_conditions):
                                        if not nea_agogi_found:  # If 'ΝΕΑ ΑΓΩΓΗ' not already found
                                            mapping_files[name] = full_path
                                            shutil.copy(full_path, out_path)
                                            break
                                    elif first_word_folder not in file:
                                        print(f"Not found : {first_word_folder} : {file}")

    df1['Φάκελος'] = df1['Αντίδικος'].map(mapping_folders)

    df1['Έλεγχος_κωδικού_ενέργειας'] = df1['Αντίδικος'].map(mapping_kodikos_check,'ignore')

    return mapping_files