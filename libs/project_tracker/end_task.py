from datetime import datetime
from libs.json import load_json, save_json
from libs.project_tracker.util import get_records_for_date, calculate_minutes

def update_end_time_for_active_tasks(file_path):
    data = load_json(file_path)
    if data is None:
        return
    
    current_time = datetime.now().strftime("%H:%M")
    today = datetime.now()
    records = get_records_for_date(data, today.year, today.month, today.day)
    
    for record in records:
        if record.get("start_time") and not record.get("end_time"):
            record["end_time"] = current_time
            record["actual_minutes"] = calculate_minutes(record["start_time"], record["end_time"])
    
    save_json(file_path, data)
