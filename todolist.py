def main():
    tasks = []

    while True:
        print("Welcome to Codsoft\n")
        print("To-Do List\n")
        print("1. Add your task")
        print("2. Display task")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            n_tasks = int(input("How many tasks you want to add: ")) 
            
            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added successfully!")

        elif choice == '2':
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '3':
            task_index = int(input("Enter the task number you'd like to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number. Please try again.")

        elif choice == '4':
            print("Exiting the To-Do List. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 4.")

if __name__ == "__main__": 
    main()
