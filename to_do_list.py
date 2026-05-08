#create an empty list to store the tasks and their status
#now to upgrade to GUI using tkinter 
import json
import tkinter as tk
from tkinter import ttk

todo_list = []
root = tk.Tk()
root.title("Work To-Do List")

entry = ttk.Entry(root)
entry.pack()

def add_task():
    task = entry.get()
    if task.strip() == "":
        return
    todo_list.append({"Task": task, "Status": "pending"})
    entry.delete(0, tk.END)
    save_to_json()
    print(todo_list)
    #listbox.insert(tk.END, f"{task} - pending")

    update_listbox()

button_add = ttk.Button(root, text="Add Task", command=add_task)
button_add.pack()
#entry.bind("<Return>", add_task)

def save_to_json():
    with open("todo_list.json", "w") as f:
        json.dump(todo_list, f, indent=4)
        print("Tasks saved to todo_list.json file successfully.")

def load_from_json():
    global todo_list
    try:
        with open("todo_list.json", "r") as f:
            task_list = json.load(f)
            todo_list.clear()
            todo_list.extend(task_list)
            update_listbox()
            print("Tasks loaded from todo_list.json file successfully.")
    except FileNotFoundError:
        print("No existing todo_list.json file found. Starting with an empty task list.")

def remove_task():
    try:
        selected = listbox.curselection()[0]
        removed_task = todo_list.pop(selected)
        print(f"Task removed is: {removed_task['Task']}")
        print(todo_list)
        save_to_json()
        update_listbox()
    except IndexError:
        print("Select a task first")


button_remove = ttk.Button(root, text = "Remove Task", command = remove_task)
button_remove.pack()

def mark_done():
    try:
        selected = listbox.curselection()[0]
        done_task = todo_list[selected]
        done_task["Status"] = "done"
        print(f"Task marked done is: {done_task['Task']}")
        print(todo_list)
        save_to_json()
        update_listbox()
    except IndexError:
        print("Select a task first")

button_done = ttk.Button(root, text = "Mark Done", command = mark_done)
button_done.pack()

def update_listbox():
    listbox.delete(0, tk.END)
    for index, task in enumerate(todo_list, 1):
        listbox.insert(tk.END, f"{index}: {task['Task']} - {task['Status']}")

listbox = tk.Listbox(root)

listbox.pack()  

'''
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
root.rowconfigure(0, weight=1)
#create a frame to hold the widgets
frame = ttk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

frame.columnconfigure(0, weight=1)``
frame.rowconfigure(1, weight=1)

task_entry = ttk.Entry(frame)
task_entry.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

add_button = ttk.Button(frame, text="Add Task", command=lambda: add_task(task_entry.get()))
add_button.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
delete_button = ttk.Button(frame, text="Delete Task", command=remove_task)
delete_button.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

done_button = ttk.Button(frame, text="Mark Done", command=mark_done)
done_button.grid(row=2, column=1, sticky="ew", padx=5, pady=5)


#function to add task
def add_task(task):
    if task.strip() == "":
        return
    
    todo_list.append({"Task": task, "Status": "pending"})
    task_entry.delete(0, tk.END)
    update_listbox()

def update_listbox():
    text_list.delete(0, tk.END)
    for index, task in enumerate(todo_list, 1):
        text_list.insert(tk.END, f"{index}: {task['Task']} - {task['Status']}")

#function to remove the task via index
def remove_task():
    try:
        selected = text_list.curselection()[0]
        todo_list.pop(selected)
        update_listbox()
    except IndexError:
        pass

#Function to mark task done
def mark_done():
    try:
        selected = text_list.curselection()[0]
        todo_list[selected]["Status"] = "done"
        update_listbox()
    except IndexError:
        pass
    



text_list = tk.Listbox(frame)
text_list.grid(row=1, column=0, columnspan=2, sticky="nsew")
'''
load_from_json()
root.mainloop()