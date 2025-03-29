import sys
sys.path.append('C:\\atari-monk\\code\\scripting')
from libs.json import print_json
from libs.project_tracker import get_file_paths, calculate_days_stats

def main():
    config = {
    'base_directory': r'C:\atari-monk\code\blog\data\projects',
    'filename_1': 'tasks.json',
    'filename_2': 'stats.json'
    }
    file_1_path, file_2_path = get_file_paths(config, sys.argv)

    calculate_days_stats(file_1_path, file_2_path)
    print_json(file_2_path)
    input("Press Enter to close")

if __name__ == "__main__":
    main()
