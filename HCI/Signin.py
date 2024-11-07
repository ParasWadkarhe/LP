import tkinter as tk
from tkinter import messagebox

# Function to handle sign-up button click
def signup():
    username = entry_username.get()
    email = entry_email.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    # Basic validation
    if not username or not email or not password or not confirm_password:
        messagebox.showwarning("Input Error", "All fields are required!")
    elif password != confirm_password:
        messagebox.showerror("Password Error", "Passwords do not match!")
    else:
        # Here you could add code to save user details, e.g., to a database
        messagebox.showinfo("Success", "You have successfully signed up!")
        # Clear the fields
        entry_username.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_password.delete(0, tk.END)
        entry_confirm_password.delete(0, tk.END)

# Function to open login window (dummy function in this example)
def go_to_login():
    messagebox.showinfo("Login", "Redirecting to Login...")

# Main window
root = tk.Tk()
root.title("Sign Up")
root.geometry("400x400")
root.config(bg="#f2f5f9")

# Main frame for better organization
main_frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20, relief="groove", borderwidth=2)
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# Title label
title_label = tk.Label(main_frame, text="Sign Up", font=("Times New Roman", 20, "bold"), bg="#ffffff", fg="#3f51b5")
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Username field
label_username = tk.Label(main_frame, text="Username:", font=("Times New Roman", 12), bg="#ffffff", fg="#333")
label_username.grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_username = tk.Entry(main_frame, font=("Times New Roman", 12), width=30)
entry_username.grid(row=1, column=1, pady=5)

# Email field
label_email = tk.Label(main_frame, text="Email:", font=("Times New Roman", 12), bg="#ffffff", fg="#333")
label_email.grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_email = tk.Entry(main_frame, font=("Times New Roman", 12), width=30)
entry_email.grid(row=2, column=1, pady=5)

# Password field
label_password = tk.Label(main_frame, text="Password:", font=("Times New Roman", 12), bg="#ffffff", fg="#333")
label_password.grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry_password = tk.Entry(main_frame, font=("Times New Roman", 12), show="*", width=30)
entry_password.grid(row=3, column=1, pady=5)

# Confirm Password field
label_confirm_password = tk.Label(main_frame, text="Confirm Password:", font=("Times New Roman", 12), bg="#ffffff", fg="#333")
label_confirm_password.grid(row=4, column=0, sticky="e", padx=5, pady=5)
entry_confirm_password = tk.Entry(main_frame, font=("Times New Roman", 12), show="*", width=30)
entry_confirm_password.grid(row=4, column=1, pady=5)

# Sign-Up button
signup_button = tk.Button(main_frame, text="Sign Up", command=signup, font=("Times New Roman", 12, "bold"),
                          bg="#4CAF50", fg="white", padx=10, pady=5)
signup_button.grid(row=5, column=0, columnspan=2, pady=20)

# Login link
login_label = tk.Label(main_frame, text="Already registered?", font=("Times New Roman", 10), bg="#ffffff", fg="#333")
login_label.grid(row=6, column=0, sticky="e", pady=(5, 0))
login_button = tk.Button(main_frame, text="Login", command=go_to_login, font=("Times New Roman", 10, "bold"),
                         bg="#3f51b5", fg="white", padx=5, pady=2)
login_button.grid(row=6, column=1, sticky="w", pady=(5, 0))

# Run the application
root.mainloop()
