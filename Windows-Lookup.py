import os
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

# Function to test the file properties
def test_file():
    file_path = file_entry.get()
    
    if not file_path:
        messagebox.showwarning("Input Error", "Please select a file.")
        return

    if os.path.exists(file_path):
        file_info = os.stat(file_path)
        
        file_size = file_info.st_size
        last_modified = datetime.fromtimestamp(file_info.st_mtime)
        is_readable = os.access(file_path, os.R_OK)
        is_writable = os.access(file_path, os.W_OK)
        
        # Display file information
        result_text.set(
            f"File Exists: Yes\n"
            f"File Size: {file_size} bytes\n"
            f"Last Modified: {last_modified}\n"
            f"Readable: {'Yes' if is_readable else 'No'}\n"
            f"Writable: {'Yes' if is_writable else 'No'}"
        )
    else:
        result_text.set("File does not exist.")

# Function to browse files
def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

# Setting up the GUI window
root = tk.Tk()
root.title("File Tester Tool")
root.geometry("400x300")

# File selection
file_label = tk.Label(root, text="Select File:")
file_label.pack(pady=10)

file_entry = tk.Entry(root, width=50)
file_entry.pack(pady=5)

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack(pady=5)

# Test button
test_button = tk.Button(root, text="Test File", command=test_file)
test_button.pack(pady=20)

# Result display
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left", font=("Arial", 10))
result_label.pack(pady=10)

# Run the GUI loop
root.mainloop()
