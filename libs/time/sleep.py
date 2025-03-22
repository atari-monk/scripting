from datetime import datetime
import sys
sys.path.append('C:\\atari-monk\\code\\scripting')
from libs.json import load_json, save_json, format_json

DATA_FILE = r"C:\atari-monk\code\atari-monk-blog\project-tracker\2025\03\sleep_data.json"

def calculate_sleep_duration(start, end):
    start_dt = datetime.strptime(f"{start['date']} {start['time']}", "%Y-%m-%d %H:%M")
    end_dt = datetime.strptime(f"{end['date']} {end['time']}", "%Y-%m-%d %H:%M")
    
    duration = end_dt - start_dt
    hours, remainder = divmod(duration.total_seconds(), 3600)
    minutes = remainder // 60
    return f"{int(hours)}h {int(minutes)}m"

def register_sleep():
    date_str = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
    time_str = input("Enter time (HH:MM, 24-hour format): ").strip()
    
    if not date_str:
        date_str = datetime.today().strftime('%Y-%m-%d')

    try:
        datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
    except ValueError:
        print("Invalid date or time format. Please try again.")
        return

    data = load_json(DATA_FILE)

    if data and "end" not in data[-1]:  
        data[-1]["end"] = {"date": date_str, "time": time_str}
        data[-1]["duration"] = calculate_sleep_duration(data[-1]["start"], data[-1]["end"])
        print(f"Wake-up recorded: {date_str} at {time_str}")
        print(f"Total sleep: {data[-1]['duration']}")
    else:  
        data.append({"start": {"date": date_str, "time": time_str}})
        print(f"Sleep recorded: {date_str} at {time_str}")

    json_string = format_json(data)
    save_json(DATA_FILE, json_string)

if __name__ == "__main__":
    register_sleep()
