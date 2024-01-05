import re

PATTERN = r'\b\w\.\b'

def get_modified_folder_name(folder_name, pattern=PATTERN):
    """Modify the folder name based on the provided pattern."""
    return re.sub(pattern, '', folder_name)

def get_folder_or_filename(x, position=-1):
    parts = str(x).split("\\")
    if len(parts) > 1:  # check if there's at least one delimiter
        return parts[position]
    return ""  # return an empty string if not
