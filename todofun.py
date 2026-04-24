tasks = []
def show_menu():
    print("\n" + "="*30)
    print("        To-Do APP")
    print("="*30)
    print("1.Add Tasks")
    print("2.View Tasks")
    print("3.Delete Tasks")
    print("4.Exit")
    print("="*30)

def add_task():
    task = input("Enter Task: ")
    if task.strip() == "":
        print("Task cannot be empty!")
    else:
        task.append(task)
        print("Task added!")

def view_task():
    print("\n Your Tasks:")
    if len(tasks) == 0:
        print("No tasks yet")
    else:
        for i, t in enumerate(tasks):
            print(f"{i + 1}. {t}")
        
def delete_task():
    view_task()
    try:
        num = int(input("Enter number to delete: "))
        if 0 < num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Deleted: {removed}")
        else:
            print("Invalid nummber!")
    except:
        print("Please Enter a number!")

while True:
    show_menu()
    choice = input("Choose option:")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("GoodBye")
        break
    else:
        print("Invalid Choice")