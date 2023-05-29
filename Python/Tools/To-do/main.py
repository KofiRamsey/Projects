
def display_tasks(tasks):
    if len(tasks) == 0:
        print("Your to-do list is empty!")
    else:
        print('------------')
        print("Your to-do list:")
        print('------------')
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        print('------------')

def main():
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. Mark a task as complete")
        print("3. Remove a task")
        print("4. Display the to-do list")
        print("5. Exit")
        print('------------')

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter the task: ")
            tasks.append(task)
            print("Task added successfully!")
        elif choice == "2":
            display_tasks(tasks)
            task_number = int(input("Enter the task number to mark as complete: "))
            if 1 <= task_number <= len(tasks):
                tasks.pop(task_number - 1)
                print("Task marked as complete!")
            else:
                print("Invalid task number.")
        elif choice == "3":
            display_tasks(tasks)
            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(tasks):
                tasks.pop(task_number - 1)
                print("Task removed successfully!")
            else:
                print("Invalid task number.")
        elif choice == "4":
            display_tasks(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
