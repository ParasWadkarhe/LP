import tkinter as tk
from tkinter import messagebox

def login():
    # Retrieve input values
    username = entry_username.get()
    password = entry_password.get()

    # Basic authentication check (for demonstration purposes)
    if username == "admin" and password == "password123":
        messagebox.showinfo("Login Success", "Welcome!")
        warning_label.config(text="", fg="")  # Clear any warning message
    else:
        warning_label.config(text="Invalid username or password. Please try again.", fg="red")

def forgot_username():
    messagebox.showinfo("Forgot Username", "Please contact support@example.com to retrieve your username.")

def forgot_password():
    messagebox.showinfo("Forgot Password", "Please use the password reset link sent to your registered email.")

def sign_up():
    messagebox.showinfo("Sign Up", "Redirecting to the Sign Up page.")

# Initialize the main window
root = tk.Tk()
root.title("Login Window")
root.geometry("400x450")
root.config(bg="#e8eaf6")  # Light blue-grey background for a soft look

# Create main frame to center the login form
main_frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20, relief="raised", borderwidth=1)
main_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame

# Title Label
title_label = tk.Label(main_frame, text="Login", font=("Times New Roman", 20, "bold"), bg="#ffffff", fg="#3f51b5")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Username Label and Entry
label_username = tk.Label(main_frame, text="Username:", font=("Times New Roman", 12), bg="#ffffff", fg="#333")
label_username.grid(row=1, column=0, sticky="e", pady=5)
entry_username = tk.Entry(main_frame, width=25, font=("Times New Roman", 12), borderwidth=1, relief="solid")
entry_username.grid(row=1, column=1, pady=5)

# Password Label and Entry
label_password = tk.Label(main_frame, text="Password:", font=("Times New Roman", 12), bg="#ffffff", fg="#333")
label_password.grid(row=2, column=0, sticky="e", pady=5)
entry_password = tk.Entry(main_frame, width=25, font=("Times New Roman", 12), show="*", borderwidth=1, relief="solid")
entry_password.grid(row=2, column=1, pady=5)

# Warning Label for invalid credentials
warning_label = tk.Label(main_frame, text="", font=("Times New Roman", 10), bg="#ffffff", fg="red")
warning_label.grid(row=3, column=0, columnspan=2, pady=5)

# Login Button
login_button = tk.Button(main_frame, text="Login", command=login, font=("Times New Roman", 12, "bold"),
                         bg="#3f51b5", fg="white", activebackground="#303f9f", activeforeground="white", padx=10, pady=5)
login_button.grid(row=4, column=0, columnspan=2, pady=10)

# Forgot Username and Forgot Password
forgot_username_button = tk.Button(main_frame, text="Forgot Username?", command=forgot_username, font=("Times New Roman", 10),
                                   bg="#ffffff", fg="#3f51b5", bd=0, cursor="hand2")
forgot_username_button.grid(row=5, column=0, pady=5, sticky="e")

forgot_password_button = tk.Button(main_frame, text="Forgot Password?", command=forgot_password, font=("Times New Roman", 10),
                                   bg="#ffffff", fg="#3f51b5", bd=0, cursor="hand2")
forgot_password_button.grid(row=5, column=1, pady=5, sticky="w")

# Divider Line
divider_label = tk.Label(main_frame, text="---------------- or ----------------", font=("Times New Roman", 10), bg="#ffffff", fg="#999")
divider_label.grid(row=6, column=0, columnspan=2, pady=10)

# Sign In and Sign Up Buttons (centered)
sign_in_button = tk.Button(main_frame, text="Sign In", command=login, font=("Times New Roman", 12, "bold"),
                           bg="#3f51b5", fg="white", activebackground="#303f9f", activeforeground="white", padx=20, pady=5)
sign_in_button.grid(row=7, column=0, columnspan=2, pady=10, sticky="nsew")  # Centered with columnspan

sign_up_button = tk.Button(main_frame, text="Sign Up", command=sign_up, font=("Times New Roman", 12, "bold"),
                           bg="#4CAF50", fg="white", activebackground="#388E3C", activeforeground="white", padx=20, pady=5)
sign_up_button.grid(row=8, column=0, columnspan=2, pady=10, sticky="nsew")  # Centered with columnspan

# Run the Tkinter main loop
root.mainloop()
