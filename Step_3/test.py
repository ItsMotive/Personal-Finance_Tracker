import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Tkinter Table Example")

# Create a Treeview widget
tree = ttk.Treeview(root)

# Define the columns
tree["columns"] = ("Name", "Age", "City")

# Format columns
tree.column("#0", width=0, stretch=tk.NO)  # Hide the first column (id)
tree.column("Name", anchor=tk.W, width=120)
tree.column("Age", anchor=tk.W, width=100)
tree.column("City", anchor=tk.W, width=120)

# Create headings
tree.heading("#0", text="", anchor=tk.W)
tree.heading("Name", text="Name", anchor=tk.W)
tree.heading("Age", text="Age", anchor=tk.W)
tree.heading("City", text="City", anchor=tk.W)

# Insert data
tree.insert("", tk.END, values=("Alice", 30, "New York"))
tree.insert("", tk.END, values=("Bob", 25, "Los Angeles"))
tree.insert("", tk.END, values=("Charlie", 35, "Chicago"))

# Add the Treeview to the window
tree.pack(pady=10, padx=10)

# Start the Tkinter event loop
root.mainloop()