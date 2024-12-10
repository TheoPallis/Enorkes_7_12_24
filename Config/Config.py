import os
import inspect

out_path = os.path.join(os.path.expanduser('~'), 'Desktop')
if not os.path.exists(out_path):
    os.makedirs(out_path)
mapping_dikigoron_excel_file = os.path.join('..', 'Data', 'Mappings', 'ΛΙΣΤΑ ΔΙΚΗΓΟΡΩΝ ΕΝΟΡΚΩΝ.xlsx')
prod_dedie_path = r"\\lawoffice\Applications\ScanDocs\ΔΕΔΔΗΕ scandocs"
testing_dedie_path = r"C:\Users\pallist\Desktop\Desktop\ΤΡΕΧΟΝΤΑ\Testing Folder\Testing dedie"
testing_dedie_path = r"C:\Users\pallist\Desktop\Desktop\ΤΡΕΧΟΝΤΑ\Testing Folder\Testing deddie 2"
dedie_path = prod_dedie_path

import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, filename='function_logs.log', 
                    format='%(asctime)s - %(message)s')


import time
import logging
import inspect
import os
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, filename='function_logs.log', 
                    format='%(asctime)s - %(message)s')


def log_execution(func):

    def wrapper(*args, **kwargs):
        file_name = os.path.basename(inspect.getfile(func))
        start_timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")
        
        # Extract arguments and conditionally show value if the name is 'path'
        bound_args = inspect.signature(func).bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        arg_list = []
        for name, value in bound_args.arguments.items():
            if name == 'path':
                arg_list.append(os.path.basename(value))
            else:
                arg_list.append(name)
        
        arg_display = ', '.join(arg_list)
        
        # print(f"Starting execution of function '{func.__name__}' in file '{file_name}' at {start_timestamp} with arguments: {arg_display}")
        logging.info(f"Starting execution of function '{func.__name__}' in file '{file_name}' at {start_timestamp} with arguments: {arg_display}")
        
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            duration = time.time() - start_time
            # print(f"    Function '{func.__name__}' in file '{file_name}' executed successfully in {duration:.4f} seconds.\n")
            logging.info(f" Function '{func.__name__}' in file '{file_name}' executed successfully in {duration:.4f} seconds.")
            return result
        except Exception as e:
            duration = time.time() - start_time
            logging.error(f"    Function '{func.__name__}' in file '{file_name}' failed after {duration:.4f} seconds. Error: {e}")
            raise
    return wrapper