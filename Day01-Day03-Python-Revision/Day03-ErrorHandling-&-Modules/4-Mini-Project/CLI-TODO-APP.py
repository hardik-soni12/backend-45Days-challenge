'''Mini Project (CLI Todo App)
Goal: Learn how to build a simple but useful app in terminal.

Features: Add tasks, view tasks, delete tasks, save/load from file.
'''

def load_tasks():
    try:
        with open(r"D:\backend-45Days-challenge\Day01-Day03-Python-Revision\Day03-ErrorHandling-&-Modules\4-Mini-Project\tasks.txt", "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(r"D:\backend-45Days-challenge\Day01-Day03-Python-Revision\Day03-ErrorHandling-&-Modules\4-Mini-Project\tasks.txt", "w") as f:
        f.writelines([t + "\n" for t in tasks])

tasks = load_tasks()

while True:
    print("\n1. Add Task \n2. View Tasks \n3. Delete Task \n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        save_tasks(tasks)

    elif choice == "2":
        for i, t in enumerate(tasks):
            print(f"{i+1}. {t}")

    elif choice == "3":
        num = int(input("Enter task number: ")) - 1
        if 0 <= num < len(tasks):
            tasks.pop(num)
            save_tasks(tasks)

    elif choice == "4":
        break
