tasks = []

while True:
    print("\nSimple Todo List")
    print("1. Add task")
    print("2. View tasks")
    print("3. Quit")
    
    choice = input("Pick a Card: ")
    
    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print(f"Added: {task}")
    elif choice == "2":
        print("\nYour Tasks:")
        for i in range(len(tasks)):
         print(f"{i+1}. {tasks[i]}")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Unanipima Msee 🤬🤬🤬🤦‍♂️")
