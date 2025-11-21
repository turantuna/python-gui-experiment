import tkinter as tk
import random
import string
def generate_random_pass(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_pass = ''.join(random.choice(characters) for i in range(length))
    return random_pass
root = tk.Tk()
root.title("Random String Generator")
root.geometry("400x200")
button = tk.Button(root,text= "Generate Random String",command=generate_random_pass)
button.pack()
root.mainloop()