import sys
sys.path.append('C:\\atari-monk\\code\\scripting')
from libs.json import *

def main():
    if len(sys.argv) != 2:
        print("Usage: .\\print_json.py <path_to_json_file>")
        input("Enter to close")
        sys.exit(1)
    
    file_path = sys.argv[1]
    print_json(file_path)
    input("Enter to close")

if __name__ == "__main__":
    main()
