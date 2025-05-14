import tkinter as tk
from tkinter import Menu, filedialog, messagebox
import random
import string
import os

def generate_license_key():
    return '-'.join(
        ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        for _ in range(4)
    )

def generate_keys(count):
    output_text.delete(1.0, tk.END)
    keys = [generate_license_key() for _ in range(count)]
    output_text.insert(tk.END, '\n'.join(keys))

def save_to_file():
    keys = output_text.get(1.0, tk.END).strip()
    if not keys:
        messagebox.showwarning("Empty", "Please generate keys first.")
        return
    filepath = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if filepath:
        with open(filepath, 'w') as f:
            f.write(keys)
        messagebox.showinfo("Saved", f"Keys saved to:\n{os.path.basename(filepath)}")

def show_about():
    messagebox.showinfo(
        "About",
        "License Key Generator\n"
        "Version: 1.0\n"
        "Author: Temper144\n\n"
        "Generates random license keys in XXXX-XXXX-XXXX-XXXX format.\n"
        "You can choose how many keys to generate and save them to a .txt file.\n\n"
        "Built with Python and Tkinter."
    )

# Main GUI
root = tk.Tk()
root.title("Key Generator")
root.geometry("1000x500")
root.resizable(False, False)
root.iconbitmap("key.ico")
# Menus
menubar = Menu(root)

key_menu = Menu(menubar, tearoff=0)
for count in [1, 10, 100, 1000, 5000]:
    label = f"{count} Key" if count == 1 else f"{count} Keys"
    key_menu.add_command(label=label, command=lambda c=count: generate_keys(c))

file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Save", command=save_to_file)

about_menu = Menu(menubar, tearoff=0)
about_menu.add_command(label="About", command=show_about)

menubar.add_cascade(label="Key", menu=key_menu)
menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="About", menu=about_menu)
root.config(menu=menubar)

# Output Field
output_text = tk.Text(root, font=("Courier", 10))
output_text.pack(expand=True, fill="both")

root.mainloop()
