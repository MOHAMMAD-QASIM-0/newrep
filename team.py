import json
import os

DATA_FILE = "data/tasks.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(title, assignee):
    tasks = load_tasks()
    tasks.append({"title": title, "assignee": assignee, "status": "Pending"})
    save_tasks(tasks)
    print(f"Task '{title}' assigned to {assignee} successfully!")

if __name__ == "__main__":
    print("--- Hackathon Team Hub ---")
    add_task("Set up database connection", "Alice")