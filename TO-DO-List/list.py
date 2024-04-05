# Define an empty list to store tasks
tasks = []

# Function to add a new task
def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{idx}. {task['task']} - {status}")

# Function to mark a task as completed
def mark_completed():
    view_tasks()
    idx = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= idx < len(tasks):
        tasks[idx]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task():
    view_tasks()
    idx = int(input("Enter the task number to delete: ")) - 1
    if 0 <= idx < len(tasks):
        del tasks[idx]
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

# Main function to run the To-Do List Application
def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Thank you for using the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
