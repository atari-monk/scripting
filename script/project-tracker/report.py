import sys
sys.path.append('C:\\atari-monk\\code\\scripting')
import os
from datetime import datetime
from libs.project_tracker import generate_markdown_report

def main():
    default_directory = r'C:\atari-monk\code\atari-monk-blog\project-tracker\2025\\'
    current_month = datetime.now().strftime('%m')
    default_task_file_path = os.path.join(default_directory, current_month, 'tasks.json')
    default_stats_file_path = os.path.join(default_directory, current_month, 'stats.json')

    if len(sys.argv) != 3:
        print(f"Usage: .\\generate_report.py <path_to_data_json> <path_to_stats_json>")
        print(f"Using default data file: {default_task_file_path}")
        print(f"Using default stats file: {default_stats_file_path}")
        
        task_file_path = default_task_file_path
        stats_file_path = default_stats_file_path
    else:
        task_file_path = sys.argv[1]
        stats_file_path = sys.argv[2]
    
    report_path = generate_markdown_report(task_file_path, stats_file_path)
    
    if report_path:
        print(f"Markdown report saved to: {report_path}")
    else:
        print("Error generating the report.")
    
    input("Enter to close")

if __name__ == "__main__":
    main()
