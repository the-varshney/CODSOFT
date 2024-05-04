import tkinter as tk
from tkinter import ttk
import math

def button_click(event):
    # Function to handle button clicks
    current = entry.get()
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "√":
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(math.sqrt(float(current))))
    elif text == "x!":
        try:
            result = math.factorial(int(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except ValueError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "^":
        entry.insert(tk.END, "**")
    elif text == "%":
        entry.insert(tk.END, "/100*")
    elif text == "(":
        entry.insert(tk.END, "(")
    elif text == ")":
        entry.insert(tk.END, ")")
    elif text == "π":
        entry.insert(tk.END, str(math.pi))
    elif text == "⌫":  # Backspace button
        current = current[:-1]
        entry.delete(0, tk.END)
        entry.insert(tk.END, current)
    elif text == "1/x":  # Reciprocal button
        try:
            result = 1 / float(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except ValueError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
        except ZeroDivisionError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Undefined")
    else:
        entry.insert(tk.END, text)

# Create main window
root = tk.Tk()
root.title("Calculator")

# Apply a custom theme to the calculator buttons
style = ttk.Style()

# Configure specific button styles
style.map("Equals.TButton", foreground=[('pressed', 'red'), ('active', 'blue')])  # change color for '=' button
style.map("Clear.TButton", foreground=[('pressed', 'blue'), ('active', 'red')])    # change color for 'C' button
style.map("Back.TButton", foreground=[('pressed', 'purple'), ('active', 'green')]) # change color for back button
style.map("TButton", foreground=[('pressed', 'white'), ('active', 'black')])

# Configure button style for all buttons
style.configure("TButton", foreground="orange", background="black", font=('Arial', 18), padding=10, width=5)

# Create entry widget to display input and output
entry = tk.Entry(root, font=('Arial', 18), bd=5, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=5, pady=5)
root.columnconfigure(0, weight=1)

# Button labels for the calculator in the specified order
buttons = [
    '√', '(', ')', '%', 'C',
    '7', '8', '9', '/', '⌫',
    '4', '5', '6', '*', 'π',
    '1', '2', '3', '-', '^',
    '0', '.', '1/x', '+', '='
]

# Create and place themed buttons in the grid
row = 1
col = 0
for button_label in buttons:
    if button_label == "=":
        button = ttk.Button(root, text=button_label, style="Equals.TButton")
    elif button_label == "C":
        button = ttk.Button(root, text=button_label, style="Clear.TButton")
    elif button_label == "⌫":
        button = ttk.Button(root, text=button_label, style="Back.TButton")
    else:
        button = ttk.Button(root, text=button_label, style="TButton")
    
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    button.bind("<Button-1>", button_click)  
    col += 1
    if col > 4:
        col = 0
        row += 1

# Make all grid cells expandable
for i in range(5):
    root.columnconfigure(i, weight=1)
for i in range(1, 7):
    root.rowconfigure(i, weight=1)

# Run the main event loop
root.mainloop()
