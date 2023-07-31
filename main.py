# main.py
from datetime import datetime

from todolistmanager import ToDoListManager

# Function to display the main menu of the To-Do List Manager
def display_menu():
    print("\nWelcome to the To-Do List Manager!")
    print("1. Add New Task")
    print("2. View All Tasks")
    print("3. View Pending Tasks")
    print("4. View Completed Tasks")
    print("5. Mark Task as Completed")
    print("6. Delete Task")
    print("7. Exit")

# Function to get a valid date from the user
def get_date_from_user():
    while True:
        date_str = input("Enter the due date (YYYY-MM-DD): ")
        try:
            due_date = datetime.strptime(date_str, "%Y-%m-%d")
            return due_date.date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

# Main function to run the To-Do List Manager application
def main():
    todo_manager = ToDoListManager()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the task title: ")
            description = input("Enter the task description: ")
            due_date = get_date_from_user()
            todo_manager.add_task(title, description, due_date)

        elif choice == "2":
            print("- All Tasks ---")
            todo_manager.view_all_tasks()

        elif choice == "3":
            print("- Pending Tasks ---")
            todo_manager.view_pending_tasks()

        elif choice == "4":
            print("- Completed Tasks ---")
            todo_manager.view_completed_tasks()

        elif choice == "5":
            task_id = int(input("Enter the task number to mark as completed: "))
            todo_manager.mark_task_completed(task_id)

        elif choice == "6":
            task_id = int(input("Enter the task number to delete: "))
            todo_manager.delete_task(task_id)

        elif choice == "7":
            break

        else:
            print("Invalid choice. Please try again.")
# Entry point of the script, starting the To-Do List Manager
if __name__ == "__main__":
    main()
