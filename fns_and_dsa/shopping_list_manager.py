shopping_list = []
i = 0

def add_item():
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"'{item}' added to the list.")

def remove_item(item):
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
    else:
        print("Invalid, item does not exist on list")

def display_item():
    if not shopping_list:
        print(f"Shopping list is currently empty")
    else:
        print("Your shoopping list is:")
        for i in [shopping_list]:
            print(i)
            i += 1

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")