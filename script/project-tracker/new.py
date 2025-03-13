import sys
sys.path.append('C:\\atari-monk\\code\\scripting')
import os
from datetime import datetime
from libs.project_tracker import add_new_task
from libs.json import print_json

def main():
    current_month = datetime.now().strftime('%m')
    default_directory = r'C:\atari-monk\code\atari-monk-blog\project-tracker\2025\\'
    default_file_path = os.path.join(default_directory, current_month, 'tasks.json')

    if len(sys.argv) != 2:
        print(f"No argument provided, using default path: {default_file_path}")
        file_path = default_file_path
    else:
        file_path = sys.argv[1]
    
    add_new_task(file_path)
    print_json(file_path)
    input("Enter to close")

if __name__ == "__main__":
    main()
