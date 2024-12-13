from docx import Document
import re
import pandas as pd
import os
from Config.Config import log_execution
#[Α|α|Β|β|Γ|γ|Δ|δ]
def append_empty(antidikos_1, antidikos_2, antidikos_3, last_date,  sxetika1, sxetika2, sxetika3, sxetika4, sxetika5, sxetika6, sxetika7, sxetika8,sxetika9, sxetika10, sxetika11, sxetika12, sxetika13, sxetika14, sxetika15):
    sxetika_lists = [ sxetika1, sxetika2, sxetika3, sxetika4, sxetika5, sxetika6, sxetika7, sxetika8,sxetika9, sxetika10, sxetika11, sxetika12, sxetika13, sxetika14, sxetika15]
    antidikos_1.append("No document found")
    antidikos_2.append("No document found")
    antidikos_3.append("No document found")
    last_date.append("No document found")
    # default = [
    #     "1) Την υπ’ αριθμ. 1617/09.05.2018 Επιστολή του ΔΕΔΔΗΕ προς τον φερόμενο ως υπαίτιο της ρευματοκλοπής.",
    #     "2) Το από 05/10/2017 Δελτίο Επίσκεψης Συνεργείου",
    #     "3) Την από 05/10/2017 εντολή εξυπηρέτησης",
    #     "4) Τις φωτογραφίες που ελήφθησαν κατά τον επιτόπιο έλεγχο του συνεργείου"
    # ]

    # Process sxetika_lists
    for index, sxetika in enumerate(sxetika_lists):
        # if sxetika not in sxetika_lists[:4]:  # Check if the current sxetika is not in the first four
        #     if index < len(default):  # Assign corresponding default if within range
        #         sxetika.append(default[index])
        #     else:  # Append "No document found" if no corresponding default
         sxetika.append("No document found")
    return sxetika1, sxetika2, sxetika3, sxetika4, sxetika5, sxetika6, sxetika7, sxetika8,sxetika9, sxetika10, sxetika11, sxetika12, sxetika13, sxetika14, sxetika15

def extract_sxetika(sxetika_found):
    if not sxetika_found:
        return None

    # Adjusted regex to split on all occurrences of "(Σχετικό X)" with optional spaces or additional characters
    # matches = re.split(r'\(Σχετικ[όά] (\d+(?:[Α-ωΑ-Ωα]*)?(?:,\s*\d+(?:[Α-ωΑ-Ωα]*)?)*(?:\s*και\s*\d+(?:[Α-ωΑ-Ωα]*)?)?)\)', sxetika_found[0])
    pattern = r'\(Σχετικ[όά]\s+(\d+(?:[α-ωΑ-Ω]*)?(?:,\s*\d+(?:[α-ωΑ-Ω]*)?)*(?:\s*και\s*\d+(?:[α-ωΑ-Ω]*)?)?(?:\s*αντίστοιχα)?)\)'

    matches = re.split(pattern,sxetika_found[0])


    formatted_list = []

    # Iterate through the matches to generate the final formatted output
    for i in range(1, len(matches), 2):
        order = matches[i].strip()
        content = matches[i - 1].strip().replace(".", "")
        # print(f"Έγγραφο {order} : {content} (Σχετικό {order})")
        # Check if there are multiple references (e.g., "5 και 5α")
        if "και" in order:
        # Split the order by "και" and process each part separately
            refs = [ref.strip() for ref in order.split("και")]
            contents = content.split("και")
        if "," in order:
            refs = [ref.strip() for ref in order.split(",")]
            contents = content.split(",")
            print(refs,contents)
            for ref, content in zip(refs, contents):   
                if len(formatted_item) < 250 :
                    formatted_item = f"Έγγραφο {ref} : {content} (Σχετικό {ref})"  
                    formatted_list.append(formatted_item)
                elif len(formatted_item) >= 250:
                    formatted_item = f"Έγγραφο {ref} : {content} (Σχετικό {ref})"  
                    formatted_item = formatted_item[:200] + f" !!Αδύνατη η αναγραφή λόγω μεγάλου μήκους" 
                    formatted_list.append(formatted_item)
        else:
            # if any(phrase in content for phrase in ["Διάγραμμα κύριου τιμολογίου", "Ένορκη βεβαίωση μάρτυρα", "Το τυποποιημένο φύλλο υπολογισμού", "Αντίγραφο της παρούσας αγωγής"]):
            #     # formatted_item = f"!!Εξαιρετέο σχετικό"
            #     formatted_item = ""
            #     formatted_list.append(formatted_item)
            # else : 
                if len(content) < 250 :
                    formatted_item = f"Έγγραφο {order} : {content}"
                    formatted_list.append(formatted_item)
                elif len(content) >= 250:
                    formatted_item = f"Έγγραφο {order} : {content}"
                    # formatted_item = formatted_item[:200] + f" !!Αδύνατη η αναγραφή λόγω μεγάλου μήκους" 
                    formatted_list.append(formatted_item)

    # Join the formatted items into a single string with line breaks
    result = "\n".join(formatted_list)
    # print(result)
    return result
    


# Change_for_sxetika
@log_execution
def get_text_and_date(file_list):
    antidikos_1, antidikos_2, antidikos_3, last_date,sxetika_list = [], [], [], [],[]
    sxetika1, sxetika2, sxetika3, sxetika4, sxetika5, sxetika6, sxetika7, sxetika8, sxetika9, sxetika10,sxetika11,sxetika12,sxetika13,sxetika14,sxetika15 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
    pattern = r'\b(\d{1,2}[-/\.]\d{1,2}[-/\.]\d{2,4})\b\s+(Ο Πληρεξούσιος Δικηγόρος|Η Πληρεξούσια Δικηγόρος|Η Πληρεξούσιος( της «ΔΕΔΔΗΕ Α\.Ε»)? Δικηγόρος)'
    reg_name = r"(?<=ΚΑΤΑ).*?(?=.ΕΙΣΑΓΩΓΙΚΑ)"
    tou_pattern = re.compile(r'\b(Του|Της|Τoυ)\b')
    sxetika_pattern = r"(?<=ήτοι\s:\s)([\s\S]*?)(?=ΓΙΑ\sΤΟΥΣ\sΛΟΓΟΥΣ\sΑΥΤΟΥΣ)"
    sxetika_lists = [sxetika1, sxetika2, sxetika3, sxetika4, sxetika5, sxetika6, sxetika7, sxetika8, sxetika9, sxetika10,sxetika11,sxetika12,sxetika13,sxetika14,sxetika15]

    for file in file_list:
        try:
            # Step 1: Open and read the document
            try:
                doc = Document(file)
                paragraphs = ''.join(p.text for p in doc.paragraphs)
            except Exception as e:
                raise  # Re-raises the exception to skip to the outer except block

            # Step 2: Extract dates
            try:
                found_dates = re.findall(pattern, paragraphs)
                last_found_date = found_dates[-1][0] if found_dates else "-"
            except Exception as e:
                last_found_date = "Error extracting dates"

            # Step 5: Append the last date found
            last_date.append(last_found_date if last_found_date else "---")

            # Step 3: Extract names
            try:
                names = re.findall(reg_name, paragraphs)
                name_str = names[0] if names else "---"
                name_str = name_str.replace(". ΚΑΙ", ". ")
                name_str = name_str.replace('καιΤου','Του')
                name_str = name_str.replace('καιΤης','Της')
            except Exception as e:
                name_str = "---"

            # Step 4: Extract antidikos information
            try:
                tou_indices = [m.start() for m in re.finditer(tou_pattern, name_str)]
                if len(tou_indices) == 3:
                    antidikos_1.append(name_str[tou_indices[0]:tou_indices[1] - 1])
                    antidikos_2.append(name_str[tou_indices[1]:tou_indices[2] - 1])
                    antidikos_3.append(name_str[tou_indices[2]:])
                elif len(tou_indices) == 2:
                    antidikos_1.append(name_str[tou_indices[0]:tou_indices[1] - 1])
                    antidikos_2.append(name_str[tou_indices[1]:])
                    antidikos_3.append("-")
                elif len(tou_indices) == 1:
                    antidikos_1.append(name_str[tou_indices[0]:])
                    antidikos_2.append("-")
                    antidikos_3.append("-")
                else:
                    antidikos_1.append("Did not find tou_indices")
                    antidikos_2.append("Did not find tou_indices")
                    antidikos_3.append("Did not find tou_indices")
            except Exception as e:
                antidikos_1.append("Error extracting antidikos info")
                antidikos_2.append("Error extracting antidikos info")
                antidikos_3.append("Error extracting antidikos info")

            # Step 6: Extract "sxetika" information
            try:
                sxetika_found = re.findall(sxetika_pattern, paragraphs)
                # sxetika_found = [sxetiko.replace(' αντίστοιχα).',")") for sxetiko in sxetika_found]                 
                sxetika_list = extract_sxetika(sxetika_found).split("\n")
                for i, sxetika in enumerate(sxetika_lists):
                    try:
                        sxetika.append(sxetika_list[i])
                    except IndexError:
                        sxetika.append("")
            except Exception as e:
                for sxetika in sxetika_lists:
                    sxetika.append(f"Error extracting sxetika: {e}")
        except Exception as main_exception:
            append_empty(antidikos_1, antidikos_2, antidikos_3, last_date, sxetika1, sxetika2, sxetika3, sxetika4, sxetika5, sxetika6, sxetika7, sxetika8, sxetika9, sxetika10, sxetika11, sxetika12, sxetika13, sxetika14, sxetika15)
       
    return antidikos_1,antidikos_2, antidikos_3, last_date, sxetika1, sxetika2, sxetika3, sxetika4, sxetika5, sxetika6, sxetika7, sxetika8,sxetika9, sxetika10, sxetika11, sxetika12, sxetika13, sxetika14, sxetika15