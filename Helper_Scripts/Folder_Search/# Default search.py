# Default search

def get_all_folders(dedie_path, list_ofeileton, df1, out_path, mapping_anatheseis, mapping_kodikoi,  number_anathesis):
    """Search for specific folders and files, and map them to the dataframe."""
    mapping_folders = {name: ["-"] for name in list_ofeileton}
    mapping_files = {name: "-" for name in list_ofeileton}
    path_list = get_path_perimeter(number_anathesis, dedie_path)
    print(mapping_kodikoi)
    for path in path_list:
            print(f"Processing Path: {path}")
            for root, _, files in os.walk(path):
                print("     Processing root:", root)
                match = re.search(r'\d+ης', root)
                if not match:
                    continue
                number = match.group()[:-2]

                for name in list_ofeileton:
                    print("         Processing name:", name)
                    if mapping_anatheseis[name] != number:
                        continue
                    first_word_folder = os.path.basename(root).split()[0]
                    for file in files:
                            if mapping_kodikoi[name][0] in file :
                                print("             Found matching folder for:", name)
                                mapping_folders[name] = root
                            for file in files:
                                if file.endswith(".docx") and file_filter(file, first_word_folder):
                                    full_path = os.path.join(root, file)
                                    mapping_files[name] = full_path
                                    shutil.copy(full_path, out_path)
                                    break
                            continue  # No need to check further if folder already found
                        
    df1['Φάκελος'] = df1['Αντίδικος'].map(mapping_folders)

    return mapping_files, mapping_folders, mapping_kodikoi