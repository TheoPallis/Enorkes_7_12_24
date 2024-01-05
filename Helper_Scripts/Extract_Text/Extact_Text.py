import docx
from docx import Document
import re
import pandas as pd
import os



def get_text_and_date(file_list,path_to_search_enorkes)
    antidikos_z = []
    paragraph_dict = {}
    string_dict = {}
    test_df = pd.DataFrame()
    test_df.reset_index(drop=True)

    name_list = []
    date_list = []
    antidikos_1 = []
    antidikos_2 = []
    antidikos_3 = []
    last_date = []
    nfound = []

    # Optional chars reg_date  = "[0-3]?[0-9]\/[0-1]?[0-9]\/[2]?[0]?[1-2][0-9]"
    reg_date = r'(\b\d{1,2}/\d{1,2}/\d{2,4})\s+Ο Πληρεξούσιος Δικηγόρος'

    # reg_date_orgiinial  = "[0-3][0-9]\/[0-1]?[0-9]\/[2][0][1-2][0-9]"
    # reg_name  = "(?<=ΚΑΤΑ).*?(?=.Ι.{2}ΕΙΣΑΓΩΓΙΚΑ)"
    reg_name  = "(?<=ΚΑΤΑ).*?(?=.ΕΙΣΑΓΩΓΙΚΑ)"
    pattern = ['Του','Της','Τoυ' ]
    regex = re.compile(r'\b(' + '|'.join(pattern) + r')\b')
    # Loop 

    for index,file in enumerate(file_list) :
        try :
            doc = Document(os.path.join(path_to_search_enorkes,file))                               # Get readable name of file    
            paragraph_text_list = [p.text for p in list(doc.paragraphs)]               
            s = ''.join(str(x) for x in  paragraph_text_list)                            # Create a dictionary (keys = files, values = paragraph string format)
            string_dict[file] = s                  
            date = re.findall(reg_date, string_dict[file])[-1]
            name = re.findall(reg_name, string_dict[file])
            s_name = str(name)
            tou_index = [m.start() for m in re.finditer(regex,s_name)]
            if len(tou_index) == 3  and name != []:                                                
                                                                
                antidikos_1.append(s_name[tou_index[0] :tou_index[1] -1])
                antidikos_2.append(s_name[tou_index[1]: tou_index[2] -1]) # -1 = ΄","
                antidikos_3.append(s_name[tou_index[2] : ])
                
                if date != [] :
                    last_date.append(date)     
                else :
                    last_date.append("-")

            elif len(tou_index) == 2  and  date != [] and name != []:

                antidikos_1.append(s_name[tou_index[0] :tou_index[1] -1])
                antidikos_2.append(s_name[tou_index[1] : ])
                antidikos_3.append("-")
                
                if date != [] :
                    last_date.append(date)     
                else :
                    last_date.append("-")

            elif len(tou_index) == 1 and  date != [] and name != []:
                antidikos_1.append(s_name[tou_index[0] :])
                antidikos_2.append("-")
                antidikos_3.append("-")
                
                if date != [] :
                    last_date.append(date)     
                else : 
                    last_date.append("----")
            
            elif name == [] :
                
                antidikos_1.append(s_name[tou_index[0] :])
                antidikos_2.append("---")
                antidikos_3.append("---")
                last_date.append("---")
                
            else :
                
                antidikos_1.append(s_name[tou_index[0] :])
                antidikos_2.append("?")
                antidikos_3.append("?")
                last_date.append("?")          
        except Exception as e :
                antidikos_1.append("Error ")
                antidikos_2.append(os.path.basename(file))
                antidikos_3.append(str(e))
                last_date.append(f"Found article : ")

    return antidikos_1,antidikos_2,antidikos_3,last_date