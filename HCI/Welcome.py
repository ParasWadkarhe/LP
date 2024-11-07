import tkinter as tk
from tkinter import messagebox

# Function to handle the Login button click
def handle_login():
    messagebox.showinfo("Login", "Proceed to Login Screen")

# Function to handle the Sign Up button click
def handle_signup():
    messagebox.showinfo("Sign Up", "Proceed to Sign Up Screen")

# Function to exit the application
def exit_application():
    root.quit()

# Main window setup
root = tk.Tk()
root.title("Welcome to Our App")
root.geometry("800x600")  # Adjust window size for better layout
root.config(bg="#f4f6f9")  # Light background color

# Main frame for the content
main_frame = tk.Frame(root, bg="#ffffff", padx=30, pady=50)
main_frame.place(relx=0.5, rely=0.5, anchor="center")  # Centering the frame

# Title label (App Name)
title_label = tk.Label(main_frame, text="Welcome to Our App", font=("Helvetica", 24, "bold"), bg="#ffffff", fg="#2C3E50")
title_label.grid(row=0, column=0, columnspan=2, pady=20)

# Subtitle label (Slogan or App Description)
subtitle_label = tk.Label(main_frame, text="Your Gateway to a Seamless Experience", font=("Helvetica", 14), bg="#ffffff", fg="#7F8C8D")
subtitle_label.grid(row=1, column=0, columnspan=2, pady=(0, 40))

# Buttons for Login, Sign Up, and Exit
login_button = tk.Button(main_frame, text="Login", command=handle_login, font=("Helvetica", 14, "bold"), bg="#3498db", fg="white", relief="raised", width=20, height=2)
login_button.grid(row=2, column=0, pady=15)

signup_button = tk.Button(main_frame, text="Sign Up", command=handle_signup, font=("Helvetica", 14, "bold"), bg="#2ecc71", fg="white", relief="raised", width=20, height=2)
signup_button.grid(row=3, column=0, pady=15)

exit_button = tk.Button(main_frame, text="Exit", command=exit_application, font=("Helvetica", 14, "bold"), bg="#e74c3c", fg="white", relief="raised", width=20, height=2)
exit_button.grid(row=4, column=0, pady=15)

# Footer with additional information
footer_label = tk.Label(main_frame, text="© 2024 Our App | All Rights Reserved", font=("Helvetica", 10), bg="#ffffff", fg="#BDC3C7")
footer_label.grid(row=5, column=0, columnspan=2, pady=(40, 0))

# Run the main window
root.mainloop()
