import os
import argparse
from file_system_utils import save_tree_to_md, get_default_output_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a Markdown file with a directory structure.")
    parser.add_argument("path", help="Path to the directory")
    parser.add_argument("-o", "--output", help="Output Markdown file name")

    args = parser.parse_args()

    if os.path.isdir(args.path):
        output_file = args.output if args.output else get_default_output_path(args.path)
        save_tree_to_md(args.path, output_file)
    else:
        print("❌ Error: Invalid directory path!")
