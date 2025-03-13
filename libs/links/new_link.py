from datetime import datetime
from libs.json import load_json, save_json, format_json

def add_new_link(file_path):
    data = load_json(file_path)
    if data is None:
        return
    
    name = input("Enter link name: ")
    url = input("Enter URL: ")
    tags = input("Enter tags (comma-separated): ").split(',')
    description = input("Enter description (optional): ")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    new_link = {
        "name": name,
        "url": url,
        "tags": [tag.strip() for tag in tags],
        "description": description,
        "created_at": current_time,
        "last_accessed": "",
        "access_count": 0
    }
    
    data.append(new_link)
    json_string = format_json(data)
    save_json(file_path, json_string)
