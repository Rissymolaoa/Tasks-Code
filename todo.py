import json
import os

class TodoList:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from a JSON file if it exists."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    def save_tasks(self):
        """Save tasks to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        """Add a new task to the list."""
        self.tasks.append({'task': task, 'completed': False})
        print(f'Task "{task}" added.')

    def list_tasks(self):
        """Display all tasks with their status."""
        if not self.tasks:
            print("No tasks found.")
            return
        print("\nTo-Do List:")
        for idx, task in enumerate(self.tasks, 1):
            status = "✓" if task['completed'] else "✗"
            print(f"{idx}. [{status}] {task['task']}")

    def complete_task(self, task_number):
        """Mark a task as completed."""
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]['completed'] = True
            print(f'Task #{task_number} marked as completed.')
        else:
            print("Invalid task number.")

def main():
    todo = TodoList()

    while True:
        print("\nMenu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Save and Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            todo.list_tasks()
        elif choice == '2':
            task = input("Enter the new task: ").strip()
            if task:
                todo.add_task(task)
            else:
                print("Task cannot be empty.")
        elif choice == '3':
            todo.list_tasks()
            try:
                task_num = int(input("Enter task number to complete: "))
                todo.complete_task(task_num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            todo.save_tasks()
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 4.")

if __name__ == "__main__":
    main()
