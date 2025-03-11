from libs.json.json import load_json, save_json
from libs.project_tracker.util import format_time

def calculate_day_stats(load_file_path, save_file_path):
    data = load_json(load_file_path)
    if data is None:
        return
    
    stats_data = []
    # Dictionary to hold cumulative minutes for each date
    date_stats = {}
    
    # Loop over the data
    for day_entry in data:
        date = day_entry.get("date")
        
        # Initialize stats for this date if it doesn't exist
        if date not in date_stats:
            date_stats[date] = {
                "estimate_minutes": 0,
                "actual_minutes": 0
            }
        
        # Add the minutes for the current task to the corresponding date
        date_stats[date]["estimate_minutes"] += day_entry.get("estimate_minutes", 0)
        date_stats[date]["actual_minutes"] += day_entry.get("actual_minutes", 0)
    
    # Now convert the dictionary into the desired format
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
    
    # Save the stats data
    save_json(save_file_path, stats_data)
