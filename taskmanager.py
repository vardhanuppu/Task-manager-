import os
import json

TASK_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    print("\nYour Tasks:")
    for idx, task in enumerate(tasks):
        status = "Complete" if task["complete"] else "Incomplete"
        print(f"{idx + 1}. {task['description']} - {status}")

def add_task(tasks):
    description = input("Enter task description: ")
    tasks.append({"description": description, "complete": False})
    print("Task added!")

def edit_task(tasks):
    display_tasks(tasks)
    try:
        task_number = int(input("Enter task number to edit: ")) - 1
        if 0 <= task_number < len(tasks):
            new_description = input("Enter new task description: ")
            tasks[task_number]["description"] = new_description
            print("Task updated!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid task number.")

def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_number = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_number < len(tasks):
            tasks.pop(task_number)
            print("Task deleted!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid task number.")

def mark_task_complete(tasks):
    display_tasks(tasks)
    try:
        task_number = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= task_number < len(tasks):
            tasks[task_number]["complete"] = True
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Mark Task as Complete")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            mark_task_complete(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
