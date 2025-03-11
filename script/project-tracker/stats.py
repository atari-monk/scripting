import sys
sys.path.append('C:\\atari-monk\\code\\scripting')
from libs.project_tracker import calculate_day_stats
from libs.json import print_json

def main():
    if len(sys.argv) != 2:
        print("Usage: .\\calculate_stats.py <path_to_json_file>")
        input("Enter to close")
        sys.exit(1)
    
    file_path = sys.argv[1]
    calculate_day_stats(file_path)
    print_json(file_path)
    input("Enter to close")

if __name__ == "__main__":
    main()