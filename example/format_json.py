import sys
sys.path.append('C:\\atari-monk\\code\\scripting')
from libs.json import format_json 

json_data = [
  {},
  {
    "date": "2025-02-28",
    "project": "battleship-ts",
    "task": "Call game API",
    "estimate_minutes": 30,
    "start_time": "12:48",
    "end_time": "13:18",
    "actual_minutes": 30,
    "notes": []
  },
  {
    "date": "2025-02-28",
    "project": "battleship-ts",
    "task": "Call game API",
    "estimate_minutes": 30,
    "start_time": "12:48",
    "end_time": "13:18",
    "actual_minutes": 30,
    "notes": ["Failed—refactoring broke Vite and Webpack, changes discarded"]
  },
  {
    "date": "2025-02-28",
    "project": "battleship-ts",
    "task": "Call game API",
    "estimate_minutes": 30,
    "start_time": "12:48",
    "end_time": "13:18",
    "actual_minutes": 30,
    "notes": [
      "Refactor tests for SRP and better functionality",
    ]
  },
  {
    "date": "2025-02-28",
    "project": "battleship-ts",
    "task": "Call game API",
    "estimate_minutes": 30,
    "start_time": "12:48",
    "end_time": "13:18",
    "actual_minutes": 30,
    "notes": [
      "Refactor tests for SRP and better functionality",
      "Refactor tests for SRP and better functionality"
    ]
  }
]

print(format_json(json_data))
