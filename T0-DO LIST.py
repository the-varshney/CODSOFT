import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("ToDo List")
        self.master.geometry("512x512") 

        # Title Label
        self.title_label = tk.Label(self.master, text="ToDo List", bg="blue", fg="white", font=("Helvetica", 16, "bold"))
        self.title_label.pack(fill=tk.X, pady=10)

        # Task Entry Field
        self.task_entry = tk.Entry(self.master, font=("Times New Roman", 12))
        self.task_entry.pack(pady=10, padx=20, fill=tk.X)

        # Add Button
        self.add_button = tk.Button(self.master, text="Add", command=self.add_task, bg="black", fg="white")
        self.add_button.pack(pady=5)

        # Tasks Section
        self.tasks_frame = tk.Frame(self.master)
        self.tasks_frame.pack(pady=20)
        tk.Label(self.tasks_frame, text="Tasks", font=("Times New Roman", 18, "bold")).pack(anchor=tk.W)

        # Completed Tasks Section
        self.completed_tasks_frame = tk.Frame(self.master)
        self.completed_tasks_frame.pack(pady=20)
        tk.Label(self.completed_tasks_frame, text="Completed Tasks", font=("Helvetica", 14, "bold")).pack(anchor=tk.W)

        # List to store tasks
        self.tasks = []

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            # Create task frame
            task_frame = tk.Frame(self.tasks_frame, bd=2)
            task_frame.pack(fill=tk.X)

            # Checkbox
            task_checkbutton = tk.Checkbutton(task_frame, command=lambda: self.mark_task_complete(task_frame))
            task_checkbutton.pack(side=tk.LEFT, padx=5)

            # Task Label
            task_label = tk.Label(task_frame, text=task_text, font=("Helvetica", 12), padx=10)
            task_label.pack(side=tk.LEFT, fill=tk.X, expand=True)

            # Delete Button
            delete_button = tk.Button(task_frame, text="Delete", command=lambda: self.remove_task(task_frame), bg="red", fg="black")
            delete_button.pack(side=tk.RIGHT, padx=5)

            # Append task to the list
            self.tasks.append((task_frame, task_checkbutton, task_label, delete_button))

            # Clear task entry
            self.task_entry.delete(0, tk.END)

    def mark_task_complete(self, task_frame):
        # Create a new frame for the completed task
        completed_task_frame = tk.Frame(self.completed_tasks_frame, bd=2)
        completed_task_frame.pack(fill=tk.X, pady=5)

        # Find the task label associated with the checkbox
        for task in self.tasks:
            if task[0] == task_frame:
                task_label_text = task[2].cget("text")
                break

        # Create a new label for the completed task
        completed_task_label = tk.Label(completed_task_frame, text=task_label_text, font=("Helvetica", 12), padx=10, fg="green", bg="lightgrey")
        completed_task_label.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Create a new delete button for the completed task
        completed_delete_button = tk.Button(completed_task_frame, text="Delete", command=lambda: self.remove_completed_task(completed_task_frame), bg="red", fg="black")
        completed_delete_button.pack(side=tk.RIGHT, padx=5)

        # Destroy the original task frame
        task_frame.destroy()

    def remove_task(self, task_frame):
        if messagebox.askokcancel("Delete Task", "Are you sure you want to delete this task?"):
            # Destroy the task frame
            task_frame.destroy()

            # Remove task from the list
            self.tasks = [task for task in self.tasks if task[0] != task_frame]

    def remove_completed_task(self, completed_task_frame):
        if messagebox.askokcancel("Delete Task", "Are you sure you want to delete this completed task?"):
            # Destroy the completed task frame
            completed_task_frame.destroy()

def main():
    root = tk.Tk()
    todo_app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
