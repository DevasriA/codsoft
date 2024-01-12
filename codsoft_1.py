import tkinter as tk
from tkinter import messagebox

class TodoListApp:  
    def __init__(self, obj):  
        self.obj = obj
        self.obj.title("To-Do List Application")

        # Entry for adding tasks
        self.entry = tk.Entry(obj, width=40)
        self.entry.grid(row=0, column=0, padx=10, pady=10)

        # Button to add tasks
        self.add= tk.Button(obj, text="Add Task", command=self.add_task)
        self.add.grid(row=1, column=0, padx=10, pady=10)

        # Listbox to display tasks
        self.listbox = tk.Listbox(obj, height=10, width=50)
        self.listbox.grid(row=2, column=0, padx=10, pady=10)

        # Button to remove selected task
        self.remove = tk.Button(obj, text="Remove Task", command=self.remove_task)
        self.remove.grid(row=3, column=0,pady=10)


    def add_task(self):
        task = self.entry.get()
        if task:
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)


    def remove_task(self):  
        try:
            selected_task = self.listbox.curselection()[0]
            self.listbox.delete(selected_task)
            
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove")


def main():
    rt = tk.Tk()
    app = TodoListApp(rt)
    rt.mainloop()


if __name__ == "__main__":
    main()
