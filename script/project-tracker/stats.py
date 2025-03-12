import sys
sys.path.append('C:\\atari-monk\\code\\scripting')
import os
from datetime import datetime
from libs.project_tracker import calculate_day_stats
from libs.json import print_json

def main():
    # Get current month and ensure it's formatted as two digits (e.g., '03' for March)
    current_month = datetime.now().strftime('%m')

    # Default directory and file paths
    default_directory = r'C:\atari-monk\code\atari-monk-blog\project-tracker\2025\\'
    default_input_file_path = os.path.join(default_directory, current_month, 'tasks.json')
    default_output_file_path = os.path.join(default_directory, current_month, 'stats.json')

    # Check for arguments: first argument is the month (optional), second is the input and output file paths (optional)
    if len(sys.argv) == 1:
        load_file_path = default_input_file_path
        save_file_path = default_output_file_path
    elif len(sys.argv) == 2:
        # User only provided the month number, so use the default paths but with specified month
        month = sys.argv[1].zfill(2)  # Ensure the month is two digits
        load_file_path = os.path.join(default_directory, month, 'tasks.json')
        save_file_path = os.path.join(default_directory, month, 'stats.json')
    elif len(sys.argv) == 3:
        # User explicitly provided both file paths
        load_file_path = sys.argv[1]
        save_file_path = sys.argv[2]
    else:
        print(f"Usage: .\\stats.py [<month_number>] <path_to_input_json_file> <path_to_output_json_file>")
        return

    # Execute the stats calculation and print the results
    calculate_day_stats(load_file_path, save_file_path)
    print_json(save_file_path)

    input("Press Enter to close")

if __name__ == "__main__":
    main()
