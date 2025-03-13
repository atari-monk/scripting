from datetime import datetime
from libs.json import load_json, save_json, format_json
from libs.project_tracker.util import get_active, calculate_minutes

def update_end_time_for_active_tasks(file_path):
    data = load_json(file_path)
    if data is None:
        return
    
    current_time = datetime.now().strftime("%H:%M")
    record = get_active(data)

    if record:
        record["end_time"] = current_time
        record["actual_minutes"] = calculate_minutes(record["start_time"], record["end_time"])

    json_string = format_json(data)
    save_json(file_path, json_string)
