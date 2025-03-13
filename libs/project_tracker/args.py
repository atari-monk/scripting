import os
from datetime import datetime

def get_file_paths(config, args=[]):
    script_path = args[0]
    script_name = os.path.basename(script_path)
    script_directory = os.path.dirname(script_path)
    
    args = args[1:]
    
    print(f"Script Name: {script_name}")
    print(f"Script Directory: {script_directory}")
    print(f"Arguments: {args}")
    
    current_year = datetime.now().strftime('%Y')
    current_month = datetime.now().strftime('%m')
    
    base_directory = config['base_directory']
    input_filename = config['input_filename']
    output_filename = config['output_filename']
    
    default_directory = os.path.join(base_directory, current_year)
    default_input_file_path = os.path.join(default_directory, current_month, input_filename)
    default_output_file_path = os.path.join(default_directory, current_month, output_filename)
    
    if len(args) == 0:
        load_file_path = default_input_file_path
        save_file_path = default_output_file_path
    elif len(args) == 1:
        month = args[0].zfill(2)
        load_file_path = os.path.join(default_directory, month, input_filename)
        save_file_path = os.path.join(default_directory, month, output_filename)
    elif len(args) == 2:
        load_file_path = args[0]
        save_file_path = args[1]
    else:
        raise ValueError("Invalid arguments. Usage: <script_name> [<month_number>] <path_to_input_json_file> <path_to_output_json_file>")
    
    return load_file_path, save_file_path
