import tkinter as tk
from tkinter import messagebox

# Function to check login credentials
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if username == "yogaboy" and password == "9900":
        messagebox.showinfo("Login Successful", "Welcome yogaboy!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Create the main window
root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")
root.configure(bg="#FFA652")  # Set the background color to pink

# Username label and entry box
label_username = tk.Label(root, text="Username:", bg="#FFA652")
label_username.pack(pady=10)

entry_username = tk.Entry(root)
entry_username.pack()

# Password label and entry box
label_password = tk.Label(root, text="Password:", bg="#FFA652")
label_password.pack(pady=10)

entry_password = tk.Entry(root, show="*")
entry_password.pack()

# Login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=20)

# Start the GUI loop
root.mainloop()
