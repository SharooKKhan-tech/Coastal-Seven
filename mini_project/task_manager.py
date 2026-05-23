import json
import os


class TaskManager:
    def __init__(self):
        self.file_name = "tasks.json"
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.file_name):
            return []

        try:
            with open(self.file_name, "r") as file:
                return json.load(file)

        except json.JSONDecodeError:
            return []

    def save_tasks(self):
        with open(self.file_name, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        new_task = {
            "task": task,
            "status": "Pending"
        }

        self.tasks.append(new_task)
        self.save_tasks()

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks found.")
            return

        print("\n========== TASK LIST ==========")

        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task['task']} [{task['status']}]")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            removed_task = self.tasks.pop(index - 1)
            self.save_tasks()
            print(f"Task '{removed_task['task']}' deleted successfully!")

        else:
            print("Invalid task number.")

    def mark_completed(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1]["status"] = "Done"
            self.save_tasks()
            print("Task marked as completed!")

        else:
            print("Invalid task number.")