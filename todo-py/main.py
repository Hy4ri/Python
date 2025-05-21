file_path = "tasks.txt"


def read_tasks():
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(file_path, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def show_tasks(tasks):
    if not tasks:
        print("** no tasks available **")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def add_task(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("task added")


def delete_task(tasks):
    show_tasks(tasks)
    try:
        tasks_len = len(tasks)
        task = int(input(f"chose a taske to delete (1 - {tasks_len}): "))
        if 1 <= task <= tasks_len:
            removed = tasks.pop(task - 1)
            print(f"** {removed} is deleted **")
        else:
            print("invalid number")
    except ValueError:
        print("Please enter a valid number ")


def mark_task(tasks):
    show_tasks(tasks)
    try:
        tasks_len = len(tasks)
        task = int(input(f"chose a taske to delete (1 - {tasks_len}): "))
        if 1 <= task <= tasks_len:
            if not tasks[task - 1].endswith(" [DONE]"):
                tasks[task - 1] += " [DONE]"
                save_tasks(tasks)
            else:
                print("Task is marked as done")
        else:
            print("Invalid Number")
    except ValueError:
        print("Please enter a valid number ")


def main():
    tasks = read_tasks()
    while True:
        print("\nTodo App")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Mark task as done")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
