import os
import re


parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

def find_unused_files_and_imports(directory=parent_dir):
    # Find all .py files in the directory
    py_files = set()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                py_files.add(os.path.splitext(file)[0])
    
    # Detect imported modules
    imported_modules = set()
    import_pattern = re.compile(r'^(?:from|import)\s+([\w\.]+)')

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        for line in f:
                            match = import_pattern.match(line.strip())
                            if match:
                                module_name = match.group(1).split('.')[0]
                                imported_modules.add(module_name)
                except (UnicodeDecodeError, IOError) as e:
                    print(f"Error reading file {file_path}: {e}")

    # Identify unused Python files
    unused_scripts = py_files - imported_modules

    return unused_scripts


def delete_unused_imports(directory):
    # Regular expression to identify import statements
    import_pattern = re.compile(r'^(?:import\s+([\w\.]+)|from\s+([\w\.]+)\s+import\s+[\w\*,]+)')
    
    # Scan Python files
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                    
                    imports = {}
                    used = set()
                    output_lines = []
                    
                    # First pass: collect imports
                    for i, line in enumerate(lines):
                        match = import_pattern.match(line.strip())
                        if match:
                            module = match.group(1) or match.group(2)
                            if module:
                                imports[i] = module.split('.')[0]
                                output_lines.append(line)  # Keep import temporarily
                        else:
                            output_lines.append(line)  # Non-import lines
                    
                    # Second pass: check for usage
                    for line in output_lines:
                        for module in imports.values():
                            if re.search(rf'\b{module}\b', line):
                                used.add(module)
                    
                    # Identify unused imports
                    unused = {i: module for i, module in imports.items() if module not in used}
                    
                    # Print unused imports
                    if unused:
                        print(f"File: {file_path}")
                        for i, module in unused.items():
                            print(f"  Line {i + 1}: {lines[i].strip()}")
                    
                    # Write file back without unused imports
                    with open(file_path, 'w', encoding='utf-8') as f:
                        for i, line in enumerate(output_lines):
                            if i in unused:
                                print(f"Removing unused import: {lines[i].strip()}")
                            else:
                                f.write(line)
                
                except (UnicodeDecodeError, IOError) as e:
                    print(f"Error processing file {file_path}: {e}")


delete_unused_imports(parent_dir)