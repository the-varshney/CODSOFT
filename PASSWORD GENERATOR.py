import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password(length):
    """Generate a random password of specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_gui():
    def submit():
        """Handle button click to generate password."""
        username = username_entry.get()
        length = length_var.get()

        if not username:
            messagebox.showerror("Error", "Please enter a username.")
            return

        try:
            length = int(length)
            if length <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive integer for password length.")
            return

        password = generate_password(length)
        password_label.config(text=password)

    def copy_password():
        """Copy the generated password to clipboard."""
        password = password_label.cget("text")
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard.")

    def reset_fields():
        """Reset all input fields and generated password."""
        username_entry.delete(0, tk.END)
        length_entry.delete(0, tk.END)
        password_label.config(text="")

    # Create the main window
    root = tk.Tk()
    root.title("Password Generator")
    root.geometry("348x348")  # Set the size of the main window

    # Create a custom style for the GUI
    style = ttk.Style()
    style.theme_use("clam")

    # Configure specific style for buttons
    style.configure("TButton", font=("Arial", 12), padding=10)
    style.map("Reset.TButton", foreground=[('pressed', 'red'), ('active', 'blue')], background=[('active', 'lightgray')])
    style.map("TButton", foreground=[('active', 'blue')], background=[('active', 'lightgray')])

    # Username input
    tk.Label(root, text="Username:").pack()
    username_entry = ttk.Entry(root, width=30)
    username_entry.pack(pady=5)

    # Password length input
    tk.Label(root, text="Password Length:").pack()
    length_var = tk.StringVar()
    length_entry = ttk.Entry(root, textvariable=length_var, width=30)
    length_entry.pack(pady=5)

    # Submit button
    submit_button = ttk.Button(root, text="Generate Password", command=submit)
    submit_button.pack(pady=10)

    # Display generated password
    password_label = ttk.Label(root, text="", font=("Arial", 12), wraplength=400)
    password_label.pack(pady=10)

    # Copy password button
    copy_button = ttk.Button(root, text="Copy Password", command=copy_password)
    copy_button.pack(pady=10)

    # Reset button
    reset_button = ttk.Button(root, text="Reset", command=reset_fields, style="Reset.TButton")
    reset_button.pack(pady=10)

    root.mainloop()

# Run the password generator GUI
generate_password_gui()