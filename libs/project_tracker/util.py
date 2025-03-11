from datetime import datetime

def get_records_for_date(data, year, month, day):
    target_date = f"{year:04d}-{month:02d}-{day:02d}"
    for entry in data:
        if entry["date"] == target_date:
            return data
    return []

def calculate_minutes(start_time, end_time):
    start = datetime.strptime(start_time, "%H:%M")
    end = datetime.strptime(end_time, "%H:%M")
    delta = end - start
    return delta.seconds // 60

def format_time(minutes):
    return f"{minutes // 60:02}:{minutes % 60:02}"
