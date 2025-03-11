from datetime import datetime
from libs.json.json import load_json, save_json

def get_records_for_date(data, year, month, day):
    for month_entry in data:
        if month_entry["year"] == year and month_entry["month"] == month:
            for day_entry in month_entry.get("records", []):
                if day_entry["day"] == day:
                    return day_entry.get("records", [])
    return []

def calculate_minutes(start, end):
    start_time = datetime.strptime(start, "%H:%M")
    end_time = datetime.strptime(end, "%H:%M")
    return (end_time - start_time).seconds // 60

def update_end_time_for_active_tasks(file_path):
    data = load_json(file_path)
    if data is None:
        return
    
    current_time = datetime.now().strftime("%H:%M")
    today = datetime.now()
    records = get_records_for_date(data, today.year, today.month, today.day)
    
    for record in records:
        if record.get("start") and not record.get("end"):
            record["end"] = current_time
            record["minutes"] = calculate_minutes(record["start"], record["end"])
    
    save_json(file_path, data)

def add_new_task(file_path):
    data = load_json(file_path)
    if data is None:
        return
    
    project = input("Enter project name: ")
    task = input("Enter task description: ")
    estimate = int(input("Enter estimated minutes: "))
    current_time = datetime.now().strftime("%H:%M")
    today = datetime.now()
    
    records = get_records_for_date(data, today.year, today.month, today.day)
    new_task = {
        "project": project,
        "task": task,
        "estimate": estimate,
        "start": current_time,
        "end": ""
    }
    records.append(new_task)
    
    save_json(file_path, data)

def calculate_day_stats(file_path):
    data = load_json(file_path)
    if data is None:
        return
    
    for month_entry in data:
        for day_entry in month_entry.get("records", []):
            records = day_entry.get("records", [])
            total_estimate = sum(record.get("estimate", 0) for record in records)
            total_minutes = sum(record.get("minutes", 0) for record in records)
            
            day_entry["stats"] = {
                "estimate": f"{total_estimate // 60:02}:{total_estimate % 60:02}",
                "total": f"{total_minutes // 60:02}:{total_minutes % 60:02}"
            }
    
    save_json(file_path, data)
