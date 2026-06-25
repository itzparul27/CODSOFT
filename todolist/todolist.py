"""
TASK 1 - TO-DO LIST APPLICATION
--------------------------------
A simple command-line To-Do List app made with Python.
Features:
1. Add a task
2. View all tasks
3. Update/Mark a task as done
4. Delete a task
5. Save tasks to a file so they aren't lost when you close the program
6. Exit

This is written in a simple, beginner-friendly way using basic
Python concepts: lists, dictionaries, functions, loops, and file handling.
"""

import os

FILE_NAME = "tasks.txt"


# ---------- Helper functions for saving/loading tasks ----------

def load_tasks():
    """Load tasks from the file into a list of dictionaries."""
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()
                if line:  # skip empty lines
                    status, title = line.split(" | ", 1)
                    tasks.append({"title": title, "done": status == "Done"})
    return tasks


def save_tasks(tasks):
    """Save the list of tasks back to the file."""
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            status = "Done" if task["done"] else "Pending"
            file.write(f"{status} | {task['title']}\n")


# ---------- Main features ----------

def add_task(tasks):
    title = input("Enter the task you want to add: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        print(f"Task '{title}' added successfully!\n")
    else:
        print("Task cannot be empty.\n")


def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.\n")
        return

    print("\n----- YOUR TO-DO LIST -----")
    for index, task in enumerate(tasks, start=1):
        status = "✔ Done" if task["done"] else "✘ Pending"
        print(f"{index}. {task['title']} [{status}]")
    print("----------------------------\n")


def update_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        choice = int(input("Enter the task number to mark as Done: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["done"] = True
            print(f"Task '{tasks[choice - 1]['title']}' marked as Done!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        choice = int(input("Enter the task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            print(f"Task '{removed['title']}' deleted successfully!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


# ---------- Main program loop ----------

def main():
    tasks = load_tasks()

    while True:
        print("===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number between 1-5.\n")


if __name__ == "__main__":
    main()