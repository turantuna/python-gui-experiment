import tkinter as tk
import random
import string

def generate_password():
    length = int(entry_length.get())        
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    entry_password.delete(0, tk.END)        
    entry_password.insert(0, password)      


root = tk.Tk()
root.title("Password Generator")
root.geometry("300x200")


label_length = tk.Label(root, text="Password Length:")
label_length.pack()

entry_length = tk.Entry(root)
entry_length.pack()

button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.pack(pady=10)

entry_password = tk.Entry(root, width=30)
entry_password.pack()

root.mainloop()
