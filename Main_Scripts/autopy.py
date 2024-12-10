from enorkes_main import main_function

excel = r"C:\Users\pallist\Desktop\Desktop\ΤΡΕΧΟΝΤΑ\Ένορκες\90 12_12.xlsx"
# excel=r"C:\Users\pallist\Desktop\Desktop\ΤΡΕΧΟΝΤΑ\Ένορκες\Νέο pool ενόρκων Τακτική - Παλιές Μικροδιαφορές.xlsx"
filtered_name_list = ["ΑΡΓΥΡΑΚΗΣ ΑΝΤΩΝΙΟΣ"]
mapping_files, kliseis_df = main_function(
    excel, filtered_name_list=filtered_name_list
)  # filtered_date=["19/12/2024"],head=10)