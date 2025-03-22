import os

CHAR_LIMIT = 4096

def get_base_folder():
    base_folder = input("Enter the path to the base folder: ")
    if not os.path.isdir(base_folder):
        print("The provided path is not valid. Exiting.")
        return None
    return base_folder

def get_ignored_projects():
    return {".git", "script", "node_modules", "dist", "build"}

def get_ignored_files():
    return {"package-lock.json"}

def list_available_folders(base_folder, ignored_projects):
    return [
        f for f in os.listdir(base_folder)
        if os.path.isdir(os.path.join(base_folder, f)) and f not in ignored_projects
    ]

def choose_project_folder(subfolders):
    if not subfolders:
        print("No available project folders found.")
        return None
    for idx, folder in enumerate(subfolders, 1):
        print(f"{idx}: {folder}")
    choice = input("Enter the number corresponding to the project folder: ")
    try:
        return subfolders[int(choice) - 1]
    except (IndexError, ValueError):
        print("Invalid choice. Exiting.")
        return None

def get_files_to_merge(project_folder, file_extensions, ignored_projects, ignored_files):
    for root, dirs, files in os.walk(project_folder):
        dirs[:] = [d for d in dirs if d not in ignored_projects]
        for file in files:
            if file in ignored_files:
                continue
            if any(file.endswith(ext) for ext in file_extensions):
                yield os.path.join(root, file)

def write_to_multiple_files(all_contents, project_folder):
    file_number = 1
    output_file = os.path.join(project_folder, f"{str(file_number).zfill(3)}_merge.txt")
    current_content = ""
    
    for content in all_contents:
        if len(current_content) + len(content) > CHAR_LIMIT:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(current_content)
            file_number += 1
            output_file = os.path.join(project_folder, f"{str(file_number).zfill(3)}_merge.txt")
            current_content = content
        else:
            current_content += content
    
    if current_content:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(current_content)

def merge():
    base_folder = get_base_folder()
    if not base_folder:
        return
    ignored_projects = get_ignored_projects()
    ignored_files = get_ignored_files()
    subfolders = list_available_folders(base_folder, ignored_projects)
    selected_folder = choose_project_folder(subfolders)
    if not selected_folder:
        return
    project_folder = os.path.join(base_folder, selected_folder)
    file_extensions = ['.json', '.html', '.js', '.css', '.ts']
    
    all_contents = []
    
    for file_path in get_files_to_merge(project_folder, file_extensions, ignored_projects, ignored_files):
        rel_path = os.path.relpath(file_path, project_folder)
        all_contents.append(f"File: {rel_path}\n")
        
        try:
            with open(file_path, "r", encoding="utf-8") as file_content:
                content = file_content.read()
            all_contents.append(f"Content:\n{content}\n\n")
        except Exception as e:
            all_contents.append(f"Could not read file content: {e}\n\n")
    
    write_to_multiple_files(all_contents, project_folder)
    print(f"File list with content saved to multiple files in: {project_folder}")

if __name__ == "__main__":
    merge()
