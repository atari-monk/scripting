import sys
sys.path.append('C:\\atari-monk\\code\\scripting')
from libs.project_tracker import calculate_day_stats
from libs.json import print_json

def main():
    if len(sys.argv) != 3:
        print("Usage: .\\calculate_stats.py <path_to_input_json_file> <path_to_output_json_file>")
        input("Enter to close")
        sys.exit(1)
    
    load_file_path = sys.argv[1]
    save_file_path = sys.argv[2]
    
    calculate_day_stats(load_file_path, save_file_path)
    
    print_json(save_file_path)
    
    input("Enter to close")

if __name__ == "__main__":
    main()
