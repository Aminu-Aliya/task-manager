import tkinter as tk
from tkinter import messagebox
from models.task import Task
from models.task_manager import TaskManager

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("REMIND ME")

        self.task_manager = TaskManager()

        self.title_entry = tk.Entry(root, width=40)
        self.title_entry.grid(row=0, column=1, padx=10, pady=5)
        tk.Label(root, text="TASK:").grid(row=0, column=0)

        self.deadline_entry = tk.Entry(root, width=40)
        self.deadline_entry.grid(row=1, column=1, padx=10, pady=5)
        tk.Label(root, text="DEADLINE (DD-MM-YYYY):").grid(row=1, column=0)

        self.priority_entry = tk.Entry(root, width=40)
        self.priority_entry.grid(row=2, column=1, padx=10, pady=5)
        tk.Label(root, text="PRIORITY (high, medium, low):").grid(row=2, column=0)

        tk.Button(root, text="ADD TASK", command=self.add_task).grid(row=3, column=0, pady=10)
        tk.Button(root, text="MARK COMPLETED", command=self.mark_completed).grid(row=3, column=1, pady=10)
        tk.Button(root, text="DELETE", command=self.delete_task).grid(row=4, column=0, pady=10)

        self.task_listbox = tk.Listbox(root, width=60)
        self.task_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.refresh_tasks()

    def add_task(self):
        title = self.title_entry.get()
        deadline = self.deadline_entry.get()
        priority = self.priority_entry.get()

        if title and deadline and priority:
            task = Task(title, deadline, priority)
            self.task_manager.add_task(task)
            self.refresh_tasks()
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Please fill all fields!")

    def delete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            self.task_manager.remove_task(index)
            self.refresh_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete!")

    def mark_completed(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            self.task_manager.mark_task_completed(index)
            self.refresh_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to mark completed!")

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.task_manager.tasks:
            display = f"{task.title} | {task.deadline} | {task.priority} | {task.status}"
            self.task_listbox.insert(tk.END, display)

    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.deadline_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="pink")
    app = TaskManagerApp(root)
    root.mainloop()