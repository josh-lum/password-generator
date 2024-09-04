import tkinter as tk
import string
import hashlib
import random

def password_gen(length = 12):

    # this part is used to create a random password 
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    text_field.delete(0, tk.END)
    text_field.insert(0, password)
    return password

def hash_password():

    # hashes the current password using a sha256 encyrption scheme
    original_password = text_field.get()
    hashed_password = hashlib.sha256(original_password.encode('utf-8')).hexdigest()
    text_field.delete(0, tk.END)
    text_field.insert(0, hashed_password)

# making a GUI window
root = tk.Tk()
root.title("Password Generator")

# making a text field
text_field = tk.Entry(root, width = 50)
text_field.pack()

# making a password generate button
password_button = tk.Button(root, text = "Generate Password", command = password_gen)
password_button.pack()

# making a hashing button 
hash_button = tk.Button(root, text = "Hash Password", command = hash_password)
hash_button.pack()

# GUI loop
root.mainloop()
    


# its giving an objects location in the memory not the hash of the object