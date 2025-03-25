import os
import pyperclip

IGNORE_FOLDERS = ["node_modules", "dist", "__pycache__", ".git", ".venv"]
IGNORE_FILES = [".DS_Store", "Thumbs.db", "package-lock.json"]

def get_default_output_path(input_path):
    base_directory = os.path.basename(os.path.normpath(input_path))
    return os.path.join(input_path, f"{base_directory}_folder_structure.md")

def generate_tree(directory, prefix=""):
    entries = sorted(os.listdir(directory))
    tree_str = ""
    
    for i, entry in enumerate(entries):
        path = os.path.join(directory, entry)
        
        if os.path.basename(path) in IGNORE_FOLDERS and os.path.isdir(path):
            continue
        if os.path.basename(path) in IGNORE_FILES and os.path.isfile(path):
            continue

        is_last = i == len(entries) - 1
        connector = "└── " if is_last else "├── "
        tree_str += f"{prefix}{connector}{entry}\n"

        if os.path.isdir(path):
            extension = "    " if is_last else "│   "
            tree_str += generate_tree(path, prefix + extension)

    return tree_str

def save_tree_to_md(directory, output_file="folder_structure.md"):
    tree_md = f"# Folder Structure\n\n```\n{directory}\n" + generate_tree(directory) + "```\n"
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(tree_md)

    pyperclip.copy(tree_md)
    print(f"✅ Folder structure saved to {output_file} and copied to clipboard!")
