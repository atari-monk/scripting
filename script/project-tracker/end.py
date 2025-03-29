import sys
sys.path.append('C:\\atari-monk\\code\\scripting')
from libs.json import print_json
from libs.project_tracker import get_file_path, update_end_time_for_active_tasks

def main():
    config = {
    'base_directory': r'C:\atari-monk\code\blog\data\projects',
    'filename': 'tasks.json'
    }
    file_path = get_file_path(config, sys.argv)

    update_end_time_for_active_tasks(file_path)
    print_json(file_path)
    input("Enter to close")

if __name__ == "__main__":
    main()
