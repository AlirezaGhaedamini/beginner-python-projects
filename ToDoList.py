
list_of_tasks = []

while True:
    print("\n📋 To-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        new_task = input("\n enter a new task: ")
        list_of_tasks.append(new_task)
        print(f"Task '{new_task}' added to the list.")
    elif choice == 2:
        if not list_of_tasks:
            print("No tasks to display.")
        for i, task in enumerate(list_of_tasks, start=1):
            print(f"{i}. {task}")
    elif choice == 3:
        if not list_of_tasks:
            print("No tasks to remove.")
        else:
            remove_task = int(input("Enter the number of the task to remove: "))
            removed_task = list_of_tasks.pop(remove_task - 1)
            print(f"Task '{removed_task}' removed from the list.")

    elif choice == 4:
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")



