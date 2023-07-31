# task.py
# Import required modules
from datetime import date

# Define a class 'Task' to represent individual tasks in the To-Do list
class Task:
    # Class variable to keep track of the maximum task ID
    max_task_id = 0

    # Constructor to initialize a Task object
    def __init__(self, title, description, due_date, status="pending"): #constructor that takes parameters
        Task.max_task_id += 1
        self.task_id = Task.max_task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    # Custom string representation of the Task object
    def __str__(self): #printing the task details
        return f"[{self.status.capitalize()}] {self.title} - Due: {self.due_date}"
