import glob
import tkinter as tk 
from tkinter import combo,messagebox
import os

def open_file():
    # Fetch the selected item from the combobox
    selected_category = combo.get()
    
    # Get the .lnk file path corresponding to the selected item
    file_path = mapping_ypodeigmaton.get(selected_category)
    
    if file_path:
        try:
            os.startfile(file_path)  # Open the .lnk file
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open {file_path}. Error: {str(e)}")
    else:
        messagebox.showwarning("Warning", f"No file found for the category: {selected_category}")

# Dictionary mapping categories to their respective .lnk files
katigories_enorkon= ('''(1) ΠΙΘΑΝΟΛΟΓΟΥΜΕΝΗ,(2) ΑΥΘΑΙΡΕΤΗ ΕΠΑΝΑΣΥΝΔΕΣΗ,(3) ΑΥΘΑΙΡΕΤΗ ΕΠΑΝΑΣΥΝΔΕΣΗ ΜΕ ΠΑΡΑΚΑΜΨΗ ΜΕΤΡΗΤΗ,(4) ΠΑΡΑΚΑΜΨΗ ΜΕΤΡΗΤΗ ΧΩΡΙΣ ΑΥΘΑΙΡΕΤΗ ΕΠΑΝΑΣΥΝΔΕΣΗ,(5) ΛΑΜΑΚΙΑ,(6) ΒΕΒΑΙΗ ΡΕΥΜΑΤΟΚΛΟΠΗ,
 '''.split(","))
word_files = glob.glob(os.path.join(os.getcwd(), "*.lnk*"))[:5]
mapping_ypodeigmaton = dict(zip(katigories_enorkon,word_files))


# app = tk.Tk()
# app.title("Open File based on Category")

# # Create a label
# label = ttk.Label(app, text="Select a category:")
# label.pack(pady=10)

# # Create a combobox (drop-down list)
# combo = ttk.Combobox(app, values=list(mapping_ypodeigmaton.keys()))
# combo.pack(pady=10)

# # Create a button to open the file
# open_btn = ttk.Button(app, text="Open File", command=open_file)
# open_btn.pack(pady=20)

# app.mainloop()
