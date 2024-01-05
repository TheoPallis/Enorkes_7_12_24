#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os

# Function to retrieve all python files excluding __init__ files
def get_python_files(folder_path):
    py_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py") and not file.startswith("__init__"):
                py_files.append(os.path.join(root, file))
    return py_files

# Function to append the content of all python files to a main total file
def append_to_total_file(py_files, total_file_path):
    with open(total_file_path, "w") as total_file:
        for file in py_files:
            with open(file, "r", encoding='utf-8') as f:
                file_contents = f.read()
                total_file.write("\n\n" + "@@ Script -> " + os.path.basename(file) + "\n\n" + file_contents + "\n\n")

# Example usage
folder_path = r"C:\Users\pallist\Desktop\ΤΡΕΧΟΝΤΑ\Testing Folder\Auto_enorkes_5_1_24" # Replace with the actual parent folder path
total_file_path = r"C:\Users\pallist\Desktop\ΤΡΕΧΟΝΤΑ\Testing Folder\Auto_enorkes_5_1_24\Documentation\total_file.py"  # Replace with the actual path for the total file

# Get all python files from both folders
python_files = get_python_files(os.path.join(folder_path, "Helper_Scripts"))

# python_files = get_python_files(os.path.join(folder_path, "Main_Scripts"))
# python_files.extend(get_python_files(os.path.join(folder_path, "Helper_Scripts")))  # Use extend here

# Append content to the total file
append_to_total_file(python_files, total_file_path)

# Return the number of files processed
print(python_files)
len(python_files)


# In[ ]:




