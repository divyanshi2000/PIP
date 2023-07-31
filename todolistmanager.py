# todolistmanager.py
import json
from datetime import datetime, date

from task import Task

# Custom JSON Encoder to handle serialization of date objects to JSON format
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()
        return super().default(obj)

class ToDoListManager:

    # Constructor to initialize the manager with a list of tasks and load existing tasks from a file
    def __init__(self):
        self.tasks = [] #array of task
        self.load_tasks_from_file()

    # Method to add a new task to the To-Do list
    def add_task(self, title, description, due_date):
        task = Task(title, description, due_date) #creating object of task
        self.tasks.append(task) #adding to the arraylist
        self.save_tasks_to_file()
        print(f"Task \"{title}\" added successfully!")

    # Method to view all tasks in the To-Do list
    def view_all_tasks(self):
        if not self.tasks: #if arraylist of tasks is empty
            print("No tasks found.")
        else:
            for task in self.tasks:
                print(task)

    # Method to view pending tasks in the To-Do list
    def view_pending_tasks(self):
        pending_tasks = [task for task in self.tasks if task.status == "pending"]
        if not pending_tasks:
            print("No pending tasks.")
        else:
            for task in pending_tasks:
                print(task)

    # Method to view completed tasks in the To-Do list
    def view_completed_tasks(self):
        completed_tasks = [task for task in self.tasks if task.status == "completed"]
        if not completed_tasks:
            print("No completed tasks.")
        else:
            for task in completed_tasks:
                print(task)

    # Method to mark a task as completed based on the task ID
    def mark_task_completed(self, task_id):
        if 1 <= task_id <= len(self.tasks):
            task = self.tasks[task_id - 1]
            task.status = "completed"
            self.save_tasks_to_file()
            print(f"Task \"{task.title}\" marked as completed!")
        else:
            print("Invalid task number.")

    # Method to delete a task based on the task ID
    def delete_task(self, task_id):
        if 1 <= task_id <= len(self.tasks):
            task = self.tasks[task_id - 1]
            self.tasks.pop(task_id - 1)
            self.save_tasks_to_file()
            print(f"Task \"{task.title}\" deleted successfully!")
        else:
            print("Invalid task number.")

    # Method to load tasks from a JSON file and populate the To-Do list
    def load_tasks_from_file(self):
        try:
            with open("tasks.json", "r") as file:
                data = json.load(file)
                for task_data in data:
                    task = Task(task_data['title'], task_data['description'],
                                datetime.strptime(task_data['due_date'], "%Y-%m-%d").date(), task_data['status'])
                    self.tasks.append(task)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    # Method to save tasks to a JSON file
    def save_tasks_to_file(self):
        with open("tasks.json", "w") as file:
            data = [{'task_id': task.task_id, 'title': task.title, 'description': task.description,
                     'due_date': task.due_date, 'status': task.status} for task in self.tasks]
            json.dump(data, file, cls=CustomJSONEncoder)
