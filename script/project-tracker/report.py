import sys
sys.path.append('C:\\atari-monk\\code\\scripting')
from libs.project_tracker import generate_markdown_report

def main():
    if len(sys.argv) != 3:
        print("Usage: .\\generate_report.py <path_to_data_json> <path_to_stats_json>")
        input("Enter to close")
        sys.exit(1)
    
    data_file_path = sys.argv[1]
    stats_file_path = sys.argv[2]
    
    report_path = generate_markdown_report(data_file_path, stats_file_path)
    
    if report_path:
        print(f"Markdown report saved to: {report_path}")
    else:
        print("Error generating the report.")
    
    input("Enter to close")

if __name__ == "__main__":
    main()
