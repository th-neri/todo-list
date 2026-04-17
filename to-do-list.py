import json
from datetime import datetime

file_name = "to_do_list.json"

def load_tasks():
    with open(file_name, "r") as file:
        return json.load(file)

def view_tasks(tasks):
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("No tasks avaiable.")
    else:
        print("\n---Your to-do list---")
        for index, task in enumerate(task_list, start=1):
            status = "Completed" if task["completed"] else "Pending"
            due_date = datetime.strptime(task['due'], "%Y-%m-%d").strftime("%B %d, %Y") 
            print(f"{index}. {task["description"]} | Due: {due_date} | {status}")
    
def save_tasks(tasks):
    with open(file_name, "w") as file:
        json.dump(tasks, file)

def add_tasks(tasks):
    description = input("Write the desired task: ").strip()
    date_input = input("Write the deadline(YYYY-MM-DD): ").strip()
    if description and date_input:
        tasks["tasks"].append({"description": description, "due": date_input, "completed": False})
        save_tasks(tasks)
        print("Task saved successfully.")
    else:
        print("You have to write something.")

def delete_tasks(tasks):
    view_tasks(tasks)
    task_no = tasks["tasks"]
    task_no = int(input("Enter the number of the task to erase it: ").strip())
    if 1 <= task_no <= len(tasks["tasks"]):
        tasks["tasks"].pop(task_no - 1)
        save_tasks(tasks)
        print(f"{task_no} deleted successfully.")
    else:
        print("Invalid number. Try Again")

def complete_task(tasks):
    view_tasks(tasks)
    task_no = tasks["tasks"]
    task_no = int(input("Enter the task number to mark as complete: ").strip())
    if 1 <= task_no <= len(tasks["tasks"]):
        tasks["tasks"][task_no - 1]["completed"] = True
        save_tasks(tasks)
        print("Task finished and marked as complete.")
    else:
        print("Invalid number. Try again")

def undo_complete_task(tasks):
    view_tasks(tasks)
    task_no = tasks["tasks"]
    task_no = int(input("Enter the task you want to mark as pending again: ").strip())
    if 1 <= task_no <= len(tasks["tasks"]):
        tasks["tasks"][task_no -1]["completed"] = False
        save_tasks(tasks)
        print(f"Task {task_no} marked as pending again.")
    else:
        print("Invalid number. Try again.")
        
def main():
    tasks = load_tasks()

    while True:
        print("\n ---To-Do list---")
        print("1. View list")
        print("2. Add task")
        print("3. Delete task")
        print("4. Save list")
        print("5. Complete task")
        print("6. Mark it as pending again")
        print("7. Exit\n")

        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_tasks(tasks)
        elif choice == "3":
            delete_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
        elif choice == "5":
            complete_task(tasks)
        elif choice == "6":
            undo_complete_task(tasks)
        elif choice == "7":
            print("Have a nice day! :)")
            break
        else:
            print("Invalid choice.")

main()