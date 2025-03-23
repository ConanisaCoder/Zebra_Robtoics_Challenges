'''
Create a program that manages a grocery list for the user:

Add grocery item
    - Input - item to add
    - Output - sorted list
Print grocery list
    - Input - none
    - Output - grocery list printed
Sort grocery items
    - Input - none
    - Output - sorted list
Remove grocery item
    - Input- item to remove
    - Output - new list
Count groceries
    - Input - none
    - Output - number of items in list
Replace grocery item
    - Input - item to be replace
    - Input - new item to replace with
    - Output - new list
'''
grocery_list = ["Orange", "Apple", "Apple"]
menu_true = input("Open the Menu (Y/N): ")
while menu_true ==  "Y":
    menu_fucntion = input("Add grocery item (1)\nPrint grocery list (2)\nSort grocery items (3)\nRemove grocery item (4)\nCount groceries (5)\nReplace grocery item (6)\nInput: ")
    if menu_fucntion == "1":
        item_add_num = int(input("How many items do you want to add: "))
        for i in range(0,item_add_num,1):
            item_add_item = input("The item you want to add: ")
            grocery_list.append(item_add_item)
        grocery_list.sort()
        print(grocery_list)
        menu_true = input("Open the Menu Again? (Y/N): ")
    elif menu_fucntion == "2":
        print(grocery_list)
        menu_true = input("Open the Menu Again? (Y/N): ")
    elif menu_fucntion == "3": 
        grocery_list.sort()
        print(grocery_list)
        menu_true = input("Open the Menu Again? (Y/N): ")
    elif menu_fucntion == "4":
        print(grocery_list)
        grocery_list_remove = input("What do you want to remove: ")
        grocery_list.remove(grocery_list_remove)
        menu_true = input("Open the Menu Again? (Y/N): ")
    elif menu_fucntion == "5": 
        grocery_list_count_func = input("Would like to count something spefic in the grocery list (Y/N): ")
        if grocery_list_count_func == "Y":
            print(grocery_list)
            grocery_list_count_func_item = input("What would like to count in list list: ")
            grocery_list_count_func_return = grocery_list.count(grocery_list_count_func_item)
            print(f"There are {grocery_list_count_func_return} {grocery_list_count_func_item}")
        elif grocery_list_count_func == "N":
            print(f" There are {grocery_list.count()} items in this Grocery List")
        menu_true = input("Open the Menu Again? (Y/N): ")
    elif menu_fucntion == "6":
        print(grocery_list)
        grocery_list_replace_times = input("How many vaules do want to replace: ")
        for i in range(0,grocery_list_replace_times,1):
            print(grocery_list)
            x = input("What vaule do want to replace starting from zero (int vaules): ")
            new_vaule = input("New item: ")
            grocery_list[x] = new_vaule
        print(grocery_list)
        menu_true = input("Open the Menu Again? (Y/N): ")
else:
    input("Press enter to close: ")