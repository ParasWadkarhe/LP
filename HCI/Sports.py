import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_form():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    sport = sport_var.get()
    contact = entry_contact.get()
    email = entry_email.get()
    address = text_address.get("1.0", tk.END).strip()

    # Validation for mandatory fields
    if not name or not age or not gender or not sport or not contact or not email:
        messagebox.showwarning("Incomplete Form", "Please fill in all required fields!")
    else:
        # Example: Save data or send email
        messagebox.showinfo("Success", "Registration Successful!")
        clear_form()

# Function to clear form fields
def clear_form():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    gender_var.set("")
    sport_var.set("")
    entry_contact.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    text_address.delete("1.0", tk.END)

# Main window setup
root = tk.Tk()
root.title("Sports Academy Registration Form")
root.geometry("600x700")
root.config(bg="#f2f3f4")

# Main frame for form content
main_frame = tk.Frame(root, bg="#ffffff", padx=30, pady=30, relief="groove", borderwidth=2)
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# Title Label
title_label = tk.Label(main_frame, text="Sports Academy Registration", font=("Helvetica", 20, "bold"), bg="#ffffff", fg="#2C3E50")
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Name
tk.Label(main_frame, text="Full Name:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=1, column=0, sticky="e", pady=5)
entry_name = tk.Entry(main_frame, font=("Helvetica", 12), width=30, bd=2, relief="solid")
entry_name.grid(row=1, column=1, pady=5)

# Age
tk.Label(main_frame, text="Age:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=2, column=0, sticky="e", pady=5)
entry_age = tk.Entry(main_frame, font=("Helvetica", 12), width=30, bd=2, relief="solid")
entry_age.grid(row=2, column=1, pady=5)

# Gender
tk.Label(main_frame, text="Gender:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=3, column=0, sticky="e", pady=5)
gender_var = tk.StringVar()
gender_options = ["Male", "Female", "Other"]
gender_menu = tk.OptionMenu(main_frame, gender_var, *gender_options)
gender_menu.config(font=("Helvetica", 12), bg="#ffffff", width=28, bd=2, relief="solid")
gender_menu.grid(row=3, column=1, pady=5)

# Sport Type
tk.Label(main_frame, text="Select Sport:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=4, column=0, sticky="e", pady=5)
sport_var = tk.StringVar()
sport_options = ["Football", "Basketball", "Tennis", "Cricket", "Swimming", "Other"]
sport_menu = tk.OptionMenu(main_frame, sport_var, *sport_options)
sport_menu.config(font=("Helvetica", 12), bg="#ffffff", width=28, bd=2, relief="solid")
sport_menu.grid(row=4, column=1, pady=5)

# Contact Number
tk.Label(main_frame, text="Contact Number:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=5, column=0, sticky="e", pady=5)
entry_contact = tk.Entry(main_frame, font=("Helvetica", 12), width=30, bd=2, relief="solid")
entry_contact.grid(row=5, column=1, pady=5)

# Email
tk.Label(main_frame, text="Email Address:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=6, column=0, sticky="e", pady=5)
entry_email = tk.Entry(main_frame, font=("Helvetica", 12), width=30, bd=2, relief="solid")
entry_email.grid(row=6, column=1, pady=5)

# Address
tk.Label(main_frame, text="Address:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=7, column=0, sticky="ne", pady=5)
text_address = tk.Text(main_frame, font=("Helvetica", 12), width=30, height=3, bd=2, relief="solid")
text_address.grid(row=7, column=1, pady=5)

# Terms and Conditions
tk.Checkbutton(main_frame, text="I agree to the terms and conditions.", font=("Helvetica", 10), bg="#ffffff", fg="#34495E").grid(row=8, column=0, columnspan=2, pady=10)

# Buttons
button_frame = tk.Frame(main_frame, bg="#ffffff")
button_frame.grid(row=9, column=0, columnspan=2, pady=20)

submit_button = tk.Button(button_frame, text="Submit", command=submit_form, font=("Helvetica", 12, "bold"), bg="#3498db", fg="white", relief="raised", bd=2)
submit_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="Clear", command=clear_form, font=("Helvetica", 12, "bold"), bg="#e74c3c", fg="white", relief="raised", bd=2)
clear_button.grid(row=0, column=1, padx=10)

# Run the main window
root.mainloop()
