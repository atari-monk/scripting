import sys
sys.path.append('C:\\atari-monk\\code\\scripting')
from libs.project_tracker import get_file_paths, generate_markdown_report

def main():
    config = {
    'base_directory': r'C:\atari-monk\code\atari-monk-blog\project-tracker',
    'filename_1': 'tasks.json',
    'filename_2': 'stats.json'
    }
    file_1_path, file_2_path = get_file_paths(config, sys.argv)

    report_path = generate_markdown_report(file_1_path, file_2_path, sys.argv[1])
    
    if report_path:
        print(f"Markdown report saved to: {report_path}")
    else:
        print("Error generating the report.")
    
    input("Enter to close")

if __name__ == "__main__":
    main()
