import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
from PIL import Image, ImageTk

# Generate a key for encryption and decryption
# You must use this key for both encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Function to encrypt the text
def encrypt_text():
    plain_text = entry_encrypt.get()
    if plain_text:
        encrypted_text = cipher_suite.encrypt(plain_text.encode()).decode()
        entry_decrypt.set(encrypted_text)
    else:
        messagebox.showwarning("Input Error", "Please enter text to encrypt")

# Function to decrypt the text
def decrypt_text():
    encrypted_text = entry_decrypt.get()
    if encrypted_text:
        try:
            decrypted_text = cipher_suite.decrypt(encrypted_text.encode()).decode()
            entry_decrypt.set(decrypted_text)
        except:
            messagebox.showerror("Decryption Error", "Invalid encrypted text")
    else:
        messagebox.showwarning("Input Error", "Please enter text to decrypt")

# Resize the background image to fit the window size while maintaining aspect ratio
def resize_image(event):
    new_width = event.width
    new_height = event.height
    # Maintain aspect ratio
    image = original_image.copy()
    image.thumbnail((new_width, new_height), Image.ANTIALIAS)
    # Center the image
    width, height = image.size
    x = (new_width - width) // 2
    y = (new_height - height) // 2
    background_image = ImageTk.PhotoImage(image)
    background_label.config(image=background_image)
    background_label.image = background_image
    background_label.place(x=x, y=y, anchor='nw')

# Create the main window
root = tk.Tk()
root.title("Text Encryptor/Decryptor")
root.geometry("600x400")

# Load the background image
original_image = Image.open("hacker.png")
background_image = ImageTk.PhotoImage(original_image)

# Set the background label with the image
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
background_label.bind('<Configure>', resize_image)

# Create StringVars to hold the input/output text
entry_encrypt = tk.StringVar()
entry_decrypt = tk.StringVar()

# Create and place the widgets with styling
label_encrypt = tk.Label(root, text="Enter text to encrypt/decrypt:", font=("Helvetica", 16), bg="black", fg="lime")
label_encrypt.pack(pady=10)

entry_encrypt_field = tk.Entry(root, textvariable=entry_encrypt, width=60, font=("Helvetica", 14))
entry_encrypt_field.pack(pady=5)

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text, bg="lightblue", fg="black", font=("Helvetica", 14), width=12)
encrypt_button.pack(pady=10)

label_decrypt = tk.Label(root, text="click to decrypt the  text:", font=("Helvetica", 16), bg="black", fg="lime")
label_decrypt.pack(pady=10)

entry_decrypt_field = tk.Entry(root, textvariable=entry_decrypt, width=60, font=("Helvetica", 14))
entry_decrypt_field.pack(pady=5)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text, bg="lightgreen", fg="black", font=("Helvetica", 14), width=12)
decrypt_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
