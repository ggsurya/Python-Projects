import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Length must be positive")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

tk.Label(root, text="Password Length:").pack(pady=10)
length_entry = tk.Entry(root)
length_entry.pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

tk.Label(root, text="Generated Password:").pack(pady=5)
password_entry = tk.Entry(root, width=30)
password_entry.pack()

root.mainloop()