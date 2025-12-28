list = []

while True:
    print("1. Add item")
    print("2. Remove item")
    print("3. Show list")
    print("4. Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter item name: ")
        list.append(item)

    elif choice == 2:
        item = input("Enter item name to remove: ")
        if item in list:
            list.remove(item)
        else:
            print("Item not found")

    elif choice == 3:
        print("Shopping list:", list)

    elif choice == 4:
        print("Thanks!!!")
        break

    else:
        print("Invalid choice")
