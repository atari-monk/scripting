import os
from datetime import datetime

def get_script_info(args):
    script_path = args[0]
    script_name = os.path.basename(script_path)
    script_directory = os.path.dirname(script_path)
    
    print(f"Script Name: {script_name}")
    print(f"Script Directory: {script_directory}")
    print(f"Arguments: {args}")
    
    return args[1:], script_name, script_directory

def get_file_path(config, args=[]):
    args, script_name, _ = get_script_info(args)
    
    base_directory = config['base_directory']
    filename = config['filename']
    
    default_file_path = os.path.join(base_directory, filename)
    
    if len(args) == 0:
        file_path = default_file_path
    elif len(args) == 1:
        file_path = args[0]
    else:
        raise ValueError(f"Invalid arguments. Usage: <{script_name}> [<month_number>] <path_to_json_file>")
    
    return file_path
