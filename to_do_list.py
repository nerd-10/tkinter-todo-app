#create an empty list to store the tasks and their status
todo_list = []



#function to add task
def add_task():
    task = input("Enter the task: ")
    todo_list.append({"Task": task, "Status": "pending"})
    print(1)
    print("New task added sucessfully\n")

#Function to view task
def view_task():
    print("Your to-do list: ")
    if len(todo_list) == 0:
        print("No pending task")
    else:
        for index, task in enumerate(todo_list, 1):
            print(f"{index}: {task['Task']} - {task['Status']}")
    print('\n')

#function to remove the task via index
def remove_task():
    if len(todo_list) == 0:
        print("\n List is empty")
    
    else:
        try:
            search_index = int(input("Enter the task number that want to be removed: ")) - 1
            if 0 <= search_index < len(todo_list):
                removed_task = todo_list.pop(search_index)
                print(f"Task removed is: {removed_task['Task']}")
            else:
                print("Invalid Task number")
        
        except ValueError:
            print("Please enter valid Task number")

#Function to mark task done

def mark_done():
    if len(todo_list) == 0:
        print("List is empty")
    else:
        try:
            search_index = int(input("Enter the task number that want to be marked done: ")) - 1
            if 0 <= search_index < len(todo_list):
                todo_list[search_index]['Status'] = 'done'
                print(f"Task {todo_list[search_index]['Task']} has been marked as Done")
            else:
                print("Invalid Task number")
        except ValueError:
            print("Please enter valid Task number")
    

#function to display a menu
def menu():
    while(True):       
        print("***MAIN MENU***")
        print("1. Add a new Task")
        print("2. View all Tasks")
        print("3. Remove a Task")
        print("4. Mark the task completed")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        
        elif choice == "2":
            view_task()
        
        elif choice == "3":
            remove_task()

        elif choice == "4":
            mark_done()
        
        elif choice == "5":
            print("Exiting the application")
            exit()
        
        else:
            print("Inavlid input and try again")
 
menu()