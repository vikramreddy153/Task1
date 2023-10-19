import json

# Function to load tasks from a JSON file
def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

# Function to save tasks to a JSON file
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to add a task
def add_task(tasks):
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (Low, Medium, High): ")
    
    task = {
        'description': description,
        'due_date': due_date,
        'priority': priority,
        'completed': False
    }
    
    tasks.append(task)
    print("Task added successfully!")

# Function to view tasks
def view_tasks(tasks):
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task['completed'] else "Not Done"
        print(f"{index}. Description: {task['description']}, Due Date: {task['due_date']}, Priority: {task['priority']}, Status: {status}")

# Function to mark a task as completed
def mark_completed(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the index of the task to mark as completed: ")) - 1
        tasks[index]['completed'] = True
        print("Task marked as completed!")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid task index.")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the index of the task to delete: ")) - 1
        deleted_task = tasks.pop(index)
        print(f"Task '{deleted_task['description']}' deleted successfully!")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid task index.")

# Main function
def main():
    tasks = load_tasks()
    
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
