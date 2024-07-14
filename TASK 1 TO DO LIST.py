tasks=[]

def add_task():
    task_description=input("Enter the task description: ")
    tasks.append({"description":task_description,"done":False})
    print("The task has been added successsfully")

def view_tasks():
    if not tasks:
        print("There is no task available")
    else:
        for index,task in enumerate(tasks):
            status="done" if task["done"] else "not done"
            print(f"{index+1}.{task['description']}-{status}")

def update_task():
    view_tasks()
    if not tasks:
        print("No tasks available to update.")
        return

    task_number = int(input("Enter the task number to update: "))
    if 1 <= task_number <= len(tasks):
        new_description = input("Enter the updated task description: ")
        tasks[task_number - 1]["description"] = new_description
        print("Task updated successfully.")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    task_number=int(input("Enter the task number to be deleted:  "))
    if 1<= task_number <= len(tasks):
        tasks.pop(task_number-1)
        print("task has been deleted successfully")
    else:
        print("invalid task number")

def track_task_status():
    total_tasks=len(tasks)
    done_tasks=sum(1 for task in tasks if task["done"])
    pending_tasks=total_tasks-done_tasks
    print(f"Total tasks: {total_tasks}")
    print(f"completed tasks: {done_tasks}")
    print(f"Pending tasks: {pending_tasks}")

while True:
    print("\n1. add task \n2. view tasks \n3. update task \n4. delete task \n5. tracking the task status \n6. exit")
    choice=int(input("Enter your choice: "))

    if choice==1:
        add_task()
    elif choice==2:
        view_tasks()
    elif choice==3:
        update_task()
    elif choice==4:
        delete_task()
    elif choice==5:
        track_task_status()
    elif choice==6:
        print("exit")
        break








