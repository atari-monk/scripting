import sys
sys.path.append('C:\\atari-monk\\code\\scripting')
from libs.project_tracker import generate_markdown_report

def main():
    if len(sys.argv) != 2:
        print("Usage: .\\generate_report.py <path_to_json_file>")
        input("Enter to close")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    report_path = generate_markdown_report(file_path)
    
    if report_path:
        print(f"Markdown report saved to: {report_path}")
    else:
        print("Error generating the report.")
    
    input("Enter to close")

if __name__ == "__main__":
    main()
