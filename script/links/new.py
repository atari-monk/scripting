import sys
sys.path.append('C:\\atari-monk\\code\\scripting')
import os
from libs.json import print_json
from libs.links import add_new_link

def main():
    config = {
    'base_directory': r'C:\atari-monk\code\atari-monk-blog\links',
    'file_name_1': 'links.json',
    'file_name_2': 'links_by_category.json'
    }
    base_directory = config['base_directory']
    file_1_path = os.path.join(base_directory, config['file_name_1'])
    file_2_path = os.path.join(base_directory, config['file_name_2'])

    add_new_link(file_1_path, file_2_path)
    print_json(file_1_path)
    print_json(file_2_path)
    input("Enter to close")

if __name__ == "__main__":
    main()
