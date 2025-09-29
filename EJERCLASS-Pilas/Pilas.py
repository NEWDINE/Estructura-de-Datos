stack = []

while True:
    print(" ")
    print("1. Push (add element)")
    print("2. Pop (remove element)")
    print("3. Show stack")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        value = input("Enter a value to push: ")
        stack.append(value)
        print(f"{value} added to stack")

    elif choice == "2":
        if stack:
            item = stack.pop()
            print(f"Removed: {item}")
        else:
            print("Stack is empty")

    elif choice == "3":
        if stack:
            print("\nCurrent stack:")
            for item in reversed(stack):
                print("|", item, "|")
        else:
            print("Stack is empty")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid option, try again")
