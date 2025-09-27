import json
import os
from models import Task

TASKS_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        try:
            data = json.load(f)
            return [Task.from_dict(item) for item in data]
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump([task.to_dict() for task in tasks], f, indent=2)
