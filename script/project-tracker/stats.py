import sys
sys.path.append('C:\\atari-monk\\code\\scripting')
from libs.json import print_json
from libs.project_tracker import calculate_days_stats, get_file_paths

def main():
    config = {
    'base_directory': r'C:\atari-monk\code\atari-monk-blog\project-tracker',
    'input_filename': 'tasks.json',
    'output_filename': 'stats.json',
    'script_name': 'stats.py'
    }
    load_file_path, save_file_path = get_file_paths(config, sys.argv)

    calculate_days_stats(load_file_path, save_file_path)
    print_json(save_file_path)
    input("Press Enter to close")

if __name__ == "__main__":
    main()
