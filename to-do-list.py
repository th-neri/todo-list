import json

file_name = "to_do_list.json"

def load_tasks():
    with open(file_name, "r") as file:
        return json.load(file)

def view_tasks(tasks):
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("No tasks avaiable.")
    else:
        print("\nYour to-do list")
        for index, task in enumerate(task_list, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index}. {task["description"]} | {status}")
    

def save_tasks(tasks):
    with open(file_name, "w") as file:
        json.dump(tasks, file)

def add_tasks(tasks):
    description = input("Write the desired task: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "completed": False})
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
        print("Invalid number.")

def complete_task(tasks):
    view_tasks(tasks)
    task_no = tasks["tasks"]
    task_no = int(input("Enter the task number to mark as complete: ").strip())
    if 1 <= task_no <= len(tasks["tasks"]):
        tasks["tasks"][task_no - 1]["completed"] = True
        print("Task finished and marked as complete.")
    else:
        print("Invalid number")

def main():
    tasks = load_tasks()

    while True:
        print("\n ---To-do list---")
        print("1. View list")
        print("2. Add list")
        print("3. Delete list")
        print("4. Save list")
        print("5. Complete list")
        print("6. Exit\n")

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
            print("Have a nice day! :)")
            break
        else:
            print("Invalid choice.")

main()