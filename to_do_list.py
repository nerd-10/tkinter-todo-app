#To do list GUI using tkinter 
import json
import tkinter as tk

#create an empty list to store the tasks and their status
todo_list = []
#widgets are added here
root = tk.Tk()
root.title("Work To-Do List")
root.geometry("400x300")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#create a frame to hold the widgets
frame = tk.Frame(root, bg="lightgray")
frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.rowconfigure(1, weight=1)

#a label just to show the user what to do
label = tk.Label(frame, text="Enter a task", bg="lightgray", font=("Arial", 12))
label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

#create an entry widget to input the task
entry = tk.Entry(frame, font=("Arial", 12))
entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

def add_task(event=None):
    task = entry.get()
    if task.strip() == "":
        return show_message("Task cannot be empty")
    todo_list.append({"Task": task, "Status": "pending"})
    entry.delete(0, tk.END)
    entry.focus()
    save_to_json()
    print(todo_list)
    #listbox.insert(tk.END, f"{task} - pending")

    update_listbox()

button_add = tk.Button(frame, text="Add Task", command=add_task)
button_add.grid(row=0, column=2, sticky="ew", padx=5, pady=5)
entry.bind("<Return>", add_task)

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


def show_message(message):
    messagevar = tk.Message(frame, text=message)
    messagevar.grid(row=4, column=0, columnspan=3, sticky="ew", padx=5, pady=5)
    messagevar.after(2000, messagevar.destroy)  # Destroy the message after 2 seconds
    messagevar.config(bg="lightgray", font=("Arial", 10))
    print(message)
    
def remove_task():
    try:
        selected = listbox.curselection()[0]
        removed_task = todo_list.pop(selected)
        print(f"Task removed is: {removed_task['Task']}")
        print(todo_list)
        save_to_json()
        update_listbox()
    except IndexError:
        show_message("Select a task first")


button_remove = tk.Button(frame, text = "Remove Task", command = remove_task)
button_remove.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

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
        show_message("Select a task first")


button_done = tk.Button(frame, text = "Mark Done", command = mark_done)
button_done.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

def update_listbox():
    listbox.delete(0, tk.END)
    for index, task in enumerate(todo_list, 1):
        listbox.insert(tk.END, f"{index}: {task['Task']} - {task['Status']}")

scrollbar = tk.Scrollbar(frame, orient="vertical")
listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, font=("Arial", 12))

listbox.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)
scrollbar.config(command=listbox.yview)
scrollbar.grid(row=1, column=3, sticky="ns")

load_from_json()
root.mainloop()