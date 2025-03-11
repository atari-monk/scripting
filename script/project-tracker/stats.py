import sys
sys.path.append('C:\\atari-monk\\code\\scripting')
import os
from datetime import datetime
from libs.project_tracker import calculate_day_stats
from libs.json import print_json

def main():
    default_directory = r'C:\atari-monk\code\atari-monk-blog\project-tracker\2025\\'
    current_month = datetime.now().strftime('%m')
    
    default_input_file_path = os.path.join(default_directory, current_month + '.json')
    default_output_file_path = os.path.join(default_directory, current_month + '_stats.json')

    if len(sys.argv) != 3:
        print(f"Usage: .\\calculate_stats.py <path_to_input_json_file> <path_to_output_json_file>")
        print(f"Using default input file: {default_input_file_path}")
        print(f"Using default output file: {default_output_file_path}")
        
        load_file_path = default_input_file_path
        save_file_path = default_output_file_path
    else:
        load_file_path = sys.argv[1]
        save_file_path = sys.argv[2]
    
    calculate_day_stats(load_file_path, save_file_path)
    print_json(save_file_path)
    
    input("Enter to close")

if __name__ == "__main__":
    main()
