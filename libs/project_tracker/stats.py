from libs.json.json import load_json, save_json
from libs.project_tracker.util import format_time

def calculate_day_stats(load_file_path, save_file_path):
    data = load_json(load_file_path)
    if data is None:
        return
    
    stats_data = []
    date_stats = {}
    
    for day_entry in data:
        date = day_entry.get("date")
        
        if date not in date_stats:
            date_stats[date] = {
                "estimate_minutes": 0,
                "actual_minutes": 0
            }
        
        date_stats[date]["estimate_minutes"] += day_entry.get("estimate_minutes", 0)
        date_stats[date]["actual_minutes"] += day_entry.get("actual_minutes", 0)
    
    for date, stats in date_stats.items():
        estimate_time = format_time(stats["estimate_minutes"])
        actual_time = format_time(stats["actual_minutes"])
        
        stats_entry = {
            "date": date,
            "estimate_minutes": stats["estimate_minutes"],
            "actual_minutes": stats["actual_minutes"],
            "estimate_time": estimate_time,
            "actual_time": actual_time
        }
        
        stats_data.append(stats_entry)
    
    save_json(save_file_path, stats_data)
