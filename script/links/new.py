import sys
sys.path.append('C:\\atari-monk\\code\\scripting')
from libs.json import print_json
from libs.shared import get_file_path
from libs.links import add_new_link

def main():
    config = {
    'base_directory': r'C:\atari-monk\code\atari-monk-blog\links',
    'filename': 'links.json'
    }
    file_path = get_file_path(config, sys.argv)

    add_new_link(file_path)
    print_json(file_path)
    input("Enter to close")

if __name__ == "__main__":
    main()
