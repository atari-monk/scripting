from datetime import datetime
from libs.json.json import load_json, save_json
from libs.project_tracker.util import get_records_for_date

def add_new_task(file_path):
    data = load_json(file_path)
    if data is None:
        return
    
    project = input("Enter project name: ")
    task = input("Enter task description: ")
    estimate_minutes = int(input("Enter estimated minutes: "))
    current_time = datetime.now().strftime("%H:%M")
    today = datetime.now()
    
    records = get_records_for_date(data, today.year, today.month, today.day)
    
    new_task = {
        "date": today.strftime("%Y-%m-%d"),
        "project": project,
        "task": task,
        "estimate_minutes": estimate_minutes,
        "start_time": current_time,
        "end_time": "",
        "actual_minutes": 0,
        "notes": []
    }
    
    records.append(new_task)
    
    save_json(file_path, data)
