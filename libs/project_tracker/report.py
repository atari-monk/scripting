from datetime import datetime
from libs.json.json import load_json

def generate_markdown_report(file_path):
    data = load_json(file_path)
    if data is None:
        return "No data found."

    today = datetime.now()
    current_year, current_month = today.year, today.month
    
    report = f"# Report for {current_year}-{current_month:02d}\n\n"
    
    total_estimate = 0
    total_minutes = 0
    
    for month_entry in data:
        if month_entry["year"] == current_year and month_entry["month"] == current_month:
            for day_entry in month_entry.get("records", []):
                report += f"## Day: {day_entry['day']}\n"
                
                report += "| Project | Task | Start | End | Minutes |\n"
                report += "|---------|------|-------|-----|---------|\n"
                for record in day_entry.get("records", []):
                    start_time = record.get("start", "")
                    end_time = record.get("end", "")
                    minutes = record.get("minutes", 0)
                    report += f"| {record['project']} | {record['task']} | {start_time} | {end_time} | {minutes} |\n"
                    
                    total_estimate += record.get("estimate", 0)
                    total_minutes += minutes
                
                report += "\n"
            
            stats = day_entry.get("stats", {})
            report += "| Stat              | Value   |\n"
            report += "|-------------------|---------|\n"
            report += f"| Estimated Time    | {stats.get('estimate', '00:00')} |\n"
            report += f"| Total Time Spent  | {stats.get('total', '00:00')} |\n"
            report += "\n"
    
    report += "## Monthly Stats\n"
    report += "| Stat              | Value   |\n"
    report += "|-------------------|---------|\n"
    report += f"| Total Estimated Time | {total_estimate // 60:02}:{total_estimate % 60:02} |\n"
    report += f"| Total Time Spent    | {total_minutes // 60:02}:{total_minutes % 60:02} |\n"
    
    if len(report.strip()) == 0:
        report = "No records found for this month."
    
    markdown_report_path = f"{file_path.replace('.json', '')}_report.md"
    with open(markdown_report_path, "w") as file:
        file.write(report)
    
    return markdown_report_path
