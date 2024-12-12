### Call Main_Function
Start : Call main function from enorkes_main.py
Main Function : #Function/Enorkes  
1. Parameters:
	1. excel_file_path (str): The path to the Excel file containing the data.
	2. filtered_date (str, optional): The date to filter the data by. Defaults to None.
	3. filtered_name_list (list, optional): A list of names to filter the data by. Defaults to None.
	4. head (int, optional): The number of rows to display. Defaults to None.
2. Returns -> tuple:
	1. mapping_files (dict): A dictionary containing the mapping files.
	2. df3 (pandas.DataFrame): The df with the stoixeia agogon.
	3. mapping_folders (dict): A dictionary containing the mapping folders.
### Main_Function Flow
1. load_excel_file(excel_file_path) #Function 
	1. Parameters : Excel File
	2. Returns : Dataframe
	3. Action : Reads the df
2. remove_invalid_dates_anatheseis_format_dates_fill_na #Function 
	1. Parameters, Returns : Dataframe
	2. Parameters,Returns of all subfunctions : Dataframe
	3. Actions :
		1. remove_invalid_dates #Function  
			df[~df['Ημερομηνία Προγραμματισμού  Ένορκης'].str.contains(r'[α-ωΑ-Ω]', regex=True,na=False)]    
		2. remove_invalid_anatheseis #Function
			df.dropna(subset=['Ανάθεση'])
		3. format_date #Function
			1. Parameters : df,col
			2. Returns : df
			3. Actions :
				if col in df.columns :
					df[col] = df[col].fillna('1900-01-01 00:00:00')  # Use a default datetime string if NaN
					df[col] = pd.to_datetime(df[col], errors='coerce')  # Parse without enforcing a format
					df[col] = df[col].dt.strftime("%d/%m/%Y")  # Format into the desired date format
		4. df.fillna("") 	
3. filter_df #Function
	1. Parameters : df,filtered_date=None,filtered_name_list=None,head=None
	2. Returns : Dataframe
	3. Actions :
		1. if filtered_date:
			df = df[df['Ημερομηνία Προγραμματισμού  Ένορκης'].isin(filtered_date)]
			2. if filtered_name_list:
			df = df[df['Επωνυμία Αποδέκτη'].isin(filtered_name_list)]
		3. if head:
			df = df.head(head)
4. fill_lawyers #Function
	1. Parameters  : df,mapping_dikigoron_excel_file
	2. Returns : df
	3. Actions :
		1. mapping_df = pd.read_excel(mapping_dikigoron_excel_file, usecols=[0, 1, 2], dtype=str)
		2. lawyer_info_map = create_mapping_dict.get(mapping_df,0,1)
		3. lawyer_name_map = create_mapping_dict.get(mapping_df,0,2)    
		4. df.assign(
			1. Στοιχεία_Δικηγόρου=df['Υπογράφων Δικηγόρος Ένορκης'].map(lawyer_info_map).fillna('Unknown'),
			2. Ονοματεπώνυμο_Δικηγόρου=df['Υπογράφων Δικηγόρος Ένορκης'].map(lawyer_name_map).fillna('Unknown')
5. remove_trailing_zero #Function 
	1. Parameters : df,'ΓΑΚ','ΕΑΚ'
	2. Returns : df
	3. Action :
	  for col in cols: 
	   df[col] = df[col].astype(str).str.rstrip('.0')
6. assign_hours #Function
	1. Parameters : df
	2. Returns : df
	3. Actions (hour_index = 0):
		for name in anathesi_df[lawyer].unique():
				hour_assignments[lawyer] = hours[hour_index]
				hour_index += 1
7. generate_mappings_for_folder_search #Function 
	1. Parameters : df
	2. Returns : df
	3. Actions :
		1. Remove single middle name -> list_ofeileton
		2. Convert 1η ανάθεση το 1ης
		3. mapping_anatheseis -> k:ofeiletis, v: anathesi
		4. mapping_kodikoi -> create_mapping_kodikon_dict #Function 
			1. Parameters : list_ofeileton, list_kodikon
			2. Returns : dict
			3. Actions : Append all the relevant values to each ofeiletis as key
			4. Code : 
				for k,v in dict(zip(name,kodikoi))...    mapping_kodikon[key].append(value)
8. get_number_anathesis #Function 
	1. Parameters : Df
	2. Returns : Set
	3. Actions :  Get the unique numbers of all αναθέσεις
9. format_anathesis_phrase(number_anathesis) #Function 
	1. Parameters : number_anathesis
	2. Returns : list
	3. Actions : For each anathesi number format it as Υποθέσεις nης Ανάθεσης
10. create_path_df #Function 
	1. Parameters : df
	2. Returns : df
	3. Actions : Copy columns from initial df & create index
### Priority 2
11. get_all_folders()
### Priority 3
12. create_anafora_df(df)
13. create_file_list_based_on_list_ofeileton
### Priority 4
14. get_text_and_date
15. create_kliseis_df
16. create_excel_file	   

### get_all_folders 
 Parameters : 
	dedie_path,
	list_ofeileton,
	path_df,
	out_path,
	mapping_anatheseis,
	mapping_kodikoi,
	mapping_kodikos_check,
	number_anathesis
Output : mapping_files -> k:name,v:doc_file_path
Actions :
	mapping_folders = {name: ["-"] for name in list_ofeileton}
	mapping_files = {name: "-" for name in list_ofeileton}
	get_path_perimeter #Function/Enorkes/get_all_folders
		Parameters : number_anathesis, dedie_path
		Output : path_list
		Actions 
	for each path in the path list (os.walk)
	get the folders that end with ης
	get the number from those folders
	ensure that the number matches to the anathesi of the ofeileti (mapping_anatheseis) 	
	get the first word of the folder
	check if any file contains the legal action code
	if yes fill the mapping_folders name key with the folder
	if a file also aligns with the file filter :
		fill the mapping_files key name with the full file path
	file_filter #Function/Enorkes/get_all_folders 
	df1['Φάκελος'] = df1['Αντίδικος'].map(mapping_folders)
Output : antidikos_1, antidikos_2, antidikos_3, last_date,sxetika1, sxetika2, sxetika3, sxetika4, sxetika5, sxetika6,sxetika7, sxetika8,sxetika9
### Extract text
Parameters : file_list, dedie_path
Actions :
Initialise antidikoi and sxeitka lists
Define regex date pattern
Define regex στοιχεία pattern (ΚΑΤΑ...ΕΙΣΑΓΩΓΙΚΑ)
Define regex ενεχόμενοι pattern (\b(Του|Της|Τoυ)\b)
Define regex sxetika pattern (ήτοι ... ΓΙΑ ΤΟΥΣ ΛΟΓΟΥΣ ΑΥΤΟΥΣ)
For every file in the inputted file_list :
	Append the dedie scandocs path
	Read it as a doc file
	Join its paragraphs into a single text (paragraphs)
	Extract its last date	and append it to the date_list
	Extract its stoixeia part
	Find the indexes of each enexomenos` tou_indices = [m.start() for m in re.finditer(tou_pattern, name_str)]
    Based on the indexes extract each enexomenoi part
	Extract its sxetika part
	Split them by new line and create the sxetika_list
	Append the sxetika_list to sxetika_final list
    If exception occurs append to each list an exception value
### Later
1. Not found -> Default arxiki lista
2. Unused scripts
3. Enorkes sxetika -> When it is not copy pasted it is not read in the word document
4. Docker all python folders
5. Add ai pdf
6. Νέα αγωγή filter
	```
	for file in files:
		full_path = os.path.join(root, file)
		if file.endswith(".docx"):
			# Check for 'ΝΕΑ ΑΓΩΓΗ' in file name
			# if "ΝΕΑ ΑΓΩΓΗ" in file:
			#     nea_agogi_found = True
			#     mapping_files[name] = full_path
			#     shutil.copy(full_path, out_path)
			#     break
			if file_filter(file, first_word_folder):
				if not nea_agogi_found:  # If 'ΝΕΑ ΑΓΩΓΗ' not already found
					mapping_files[name] = full_path
					shutil.copy(full_path, out_path)
					# print(f"!! Found : Ανάθεση : {mapping_anatheseis[name]}  Folder : {os.path.basename(root)}  Files : {files} Selected file : {file}")
					break
	```
#### Done
- [x] Check where agogi date is used in the doc
- [x] Remove index error
- [x] Decorator : Succesful run and duration
- [x] Remove the fill excluded with blank
- [x] Length -> Not written due to length or concatenate missing due to length
- [x] Add  more sxetika
- [x] Large length -> cropped text + Αδύνατη η αναγραφή
- [x] Add extra sxetika to excel
- [x] add to  word docs 
- [x] Check if get_modified_folder_name or get_folder_or_filename is needed -> removed
- [x]  Check why some docs are not found even though they contain the legal action code
	1. The legal action codes are found
		1. The file filter criteria are not covered 
			1. First word folder != First word doc (there is - instead of space)
			2. ΑΓΩΓΗ_ΔΕΔΔΗΕ not in include_conditions
	2. The legal action codes are not found
		1. Add an optional "-" or " _ "  #redundant 
- [x] Multiple folders : 
	- [x] If for the same name there are 2+ folders
	- [x] Append to mapping_folders[name] the second+ folder
	- [ ] The problem is that a name can have multiple folders with the same name in the anathesi path. Because the folders are read in order irrespective of the inital order in the anathesi df, the files are appended to the mapping files according to the os.walk order.
- [x] UAT	
	1. ΠΑΡΑΣΤΑΤΙΔΗΣ :  Δεν είχε γίνει η αντικατάσταση -> No doc found
	2. [[ΠΑΤΥΝΙΩΣΤΗΣ]] : Χάνονταν ενδιάμεσα ψηφία -> Δεν είχε ενσωματωθεί στο regex το εναλλακτικό λεκτικό Σχετικά (μόνο το Σχετικό)
- [x] Testing that final ouput file == frozen output file