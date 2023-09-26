import tkinter as tk

task_counter = 1

def add_task():
    global task_counter
    task = entry.get()
    task_with_number = f"{task_counter} - {task}"

    listbox.insert(tk.END, task_with_number)
    entry.delete(0, tk.END)
    task_counter += 1

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)


window = tk.Tk()
window.title("To-Do List")
window.geometry("500x400")


entry = tk.Entry(window, font=("Arial", 14))
entry.pack(pady=30)

add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

exit_button = tk.Button(window, text="Exit", command=exit)
exit_button.pack(pady=5)



listbox = tk.Listbox(window, font=("Arial", 12), width=50)
listbox.pack(pady=10)

window.mainloop()