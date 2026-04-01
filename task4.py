import json
import os

FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Add task
def add_task(tasks):
    task_name = input("Enter new task: ")
    tasks.append({"task": task_name, "done": False})
    save_tasks(tasks)
    print("Task added successfully!\n")

# View tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.\n")
        return

    print("\nYour Tasks:")
    for i, t in enumerate(tasks, start=1):
        status = "✔️" if t["done"] else "❌"
        print(f"{i}. {t['task']} [{status}]")
    print()

# Delete task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"Deleted: {removed['task']}\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

# Mark task as done
def mark_done(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]["done"] = True
            save_tasks(tasks)
            print("Task marked as completed!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("==== TO-DO LIST ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            mark_done(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")

# Run program
main()