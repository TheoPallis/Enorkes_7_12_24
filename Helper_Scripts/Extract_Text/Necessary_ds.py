# 2) Εξαγωγή φακέλου και λεκτικού αγωγής

list_ofeileton = list(anathesi_df['Επωνυμία Αποδέκτη'])
pattern = r'\b\w\.\b'
list_ofeileton = [re.sub(pattern, '', x) for x in list_ofeileton]
half_list_ofeileton = [x.split(" ")[0] for x in list_ofeileton]
out_path = r"C:\Users\pallist\Desktop\ΤΡΕΧΟΝΤΑ\Testing Folder\ΦΑΚΕΛΟΙ ΕΝΟΡΚΩΝ\Results" 
path_to_search_enorkes = r"C:\Users\pallist\Desktop\ΤΡΕΧΟΝΤΑ\Testing Folder\ΦΑΚΕΛΟΙ ΕΝΟΡΚΩΝ"
anathesi_list = list(anathesi_df['Ανάθεση'].apply(lambda x : str(x).split()[0].replace("η","").replace("ης","")))
kodikos_list = list(anathesi_df['Κωδικός Ενέργειας'])
mapping_anatheseis = dict(zip(list_ofeileton,anathesi_list))
mapping_kodikoi = dict(zip(list_ofeileton,kodikos_list))
mapping_kodikos_check = dict(zip(list_ofeileton,"-"))
empty_doc = Document()
empty_doc.save(os.path.join(out_path,'empty.docx'))
empty = os.path.join(out_path,'empty.docx')