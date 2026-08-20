
FILE_NAME = "tasks.txt"
 
 
def load_tasks():
    tasks = []
 
    try:
        file = open(FILE_NAME, "r")
 
        for line in file:
            line = line.strip()
 
            if line:
                status, title = line.split(" | ", 1)
 
                if status == "Done":
                    done = True
                else:
                    done = False
 
                tasks.append({"title": title, "done": done})
 
        file.close()
 
    except FileNotFoundError:
        pass
 
    return tasks
 
 
def save_tasks(tasks):
    file = open(FILE_NAME, "w")
 
    for task in tasks:
        if task["done"]:
            status = "Done"
        else:
            status = "Pending"
 
        file.write(status + " | " + task["title"] + "\n")
 
    file.close()
 
 
def add_task(tasks):
    title = input("Enter the task you want to add: ")
 
    if title:
        tasks.append({"title": title, "done": False})
        print("Task added successfully!\n")
    else:
        print("Task cannot be empty.\n")
 
 
def view_tasks(tasks):
    if len(tasks) == 0:
        print("Your to-do list is empty.\n")
        return
 
    print("\n----- YOUR TO-DO LIST -----")
 
    for i in range(len(tasks)):
        if tasks[i]["done"]:
            status = "Done"
        else:
            status = "Pending"
 
        print(str(i + 1) + ". " + tasks[i]["title"] + " [" + status + "]")
 
    print("----------------------------\n")
 
 
def update_task(tasks):
    view_tasks(tasks)
 
    if len(tasks) == 0:
        return
 
    try:
        choice = int(input("Enter the task number to mark as Done: "))
 
        if choice >= 1 and choice <= len(tasks):
            tasks[choice - 1]["done"] = True
            print("Task marked as Done!\n")
        else:
            print("Invalid task number.\n")
 
    except ValueError:
        print("Please enter a valid number.\n")
 
 
def delete_task(tasks):
    view_tasks(tasks)
 
    if len(tasks) == 0:
        return
 
    try:
        choice = int(input("Enter the task number to delete: "))
 
        if choice >= 1 and choice <= len(tasks):
            tasks.pop(choice - 1)
            print("Task deleted successfully!\n")
        else:
            print("Invalid task number.\n")
 
    except ValueError:
        print("Please enter a valid number.\n")
 
 
def main():
    tasks = load_tasks()
 
    while True:
        print("===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
 
        choice = input("Enter your choice (1-5): ")
 
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
 
 
main()
