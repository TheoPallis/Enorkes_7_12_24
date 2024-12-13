from enorkes_main import main_function,test_main_function
from Extact_Text import get_text_and_date
excel = r"C:\Users\pallist\Desktop\Desktop\ΤΡΕΧΟΝΤΑ\Ένορκες\90 12_12.xlsx"
# excel = r"\\lawoffice\Applications\ScanDocs\ΔΕΔΔΗΕ scandocs\$ Υποδείγματα\Ένορκες Βεβαιώσεις\Πειραματικά\Αυτοματοιημένες\2024\ΜΙΚΡΟΔΙΑΦΟΡΕΣ\new pool Ενόρκων_Νέες Μικροδιαφορές 2024 Σωστό.xlsx"
file = [r"\\lawoffice\Applications\ScanDocs\ΔΕΔΔΗΕ scandocs\Υποθέσεις 151ης Ανάθεσης\ΜΟΥΚΟΣ ΙΩΑΝΝΗΣ\ΑΓΩΓΗ ΔΕΔΔΗΕ κατά ΜΟΥΚΟΥ ΙΩΑΝΝΗ.docx"]
#Parameters for main function:
# excel_file_path = None #(str): The path to the Excel file containing the data.
filtered_date = None #(str, optional): The date to filter the data by. Defaults to None.
filtered_name_list = None #(list, optional): A list of names to filter the data by. Defaults to None.
head = None #(int, optional): The number of rows to display. Defaults to None.
anathesi = None #(str, optional): The number of the anathesi to filter the data by. Defaults to None.
# Parameters for get_text_and_date function:
specific_file = file #(str, optional): The name of the specific file to extract the data by. Defaults to None.


#16 minuts for 90 cases
# 10 minutes for pre computed number and joined path word
mapping_files,df3,mapping_folders = main_function(excel)#,date="19/12/2024")#,filtered_name_list=['ΜΟΥΚΟΣ ΙΩΑΝΝΗΣ'])
# test_main_function()
# _= get_text_and_date(file)
