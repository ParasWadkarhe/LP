import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_registration():
    # Retrieving all the field data
    patient_name = entry_patient_name.get()
    patient_age = entry_patient_age.get()
    patient_gender = gender_var.get()
    patient_contact = entry_patient_contact.get()
    patient_email = entry_patient_email.get()
    patient_address = text_address.get("1.0", tk.END).strip()
    patient_blood_group = blood_group_var.get()
    patient_medical_history = medical_history_var.get()
    emergency_contact = entry_emergency_contact.get()
    
    # Validation for mandatory fields
    if not patient_name or not patient_age or not patient_contact or not patient_email or not patient_address:
        messagebox.showwarning("Incomplete Form", "Please fill in all required fields!")
    else:
        messagebox.showinfo("Registration Successful", "Patient registered successfully!")
        clear_form()

# Function to clear form fields
def clear_form():
    entry_patient_name.delete(0, tk.END)
    entry_patient_age.delete(0, tk.END)
    gender_var.set("")
    entry_patient_contact.delete(0, tk.END)
    entry_patient_email.delete(0, tk.END)
    text_address.delete("1.0", tk.END)
    blood_group_var.set("")
    medical_history_var.set(0)
    entry_emergency_contact.delete(0, tk.END)

# Main window setup
root = tk.Tk()
root.title("Patient Registration Form")
root.geometry("600x650")
root.config(bg="#f4f6f9")

# Main frame for form content
main_frame = tk.Frame(root, bg="#ffffff", padx=30, pady=30, relief="groove", borderwidth=2)
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# Title
title_label = tk.Label(main_frame, text="Patient Registration Form", font=("Helvetica", 18, "bold"), bg="#ffffff", fg="#2C3E50")
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Patient Name
tk.Label(main_frame, text="Patient Name:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=1, column=0, sticky="e", pady=5)
entry_patient_name = tk.Entry(main_frame, font=("Helvetica", 12), width=30, bd=2, relief="solid")
entry_patient_name.grid(row=1, column=1, pady=5)

# Patient Age
tk.Label(main_frame, text="Patient Age:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=2, column=0, sticky="e", pady=5)
entry_patient_age = tk.Entry(main_frame, font=("Helvetica", 12), width=30, bd=2, relief="solid")
entry_patient_age.grid(row=2, column=1, pady=5)

# Gender
tk.Label(main_frame, text="Gender:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=3, column=0, sticky="e", pady=5)
gender_var = tk.StringVar()
gender_radio_male = tk.Radiobutton(main_frame, text="Male", variable=gender_var, value="Male", font=("Helvetica", 12), bg="#ffffff")
gender_radio_male.grid(row=3, column=1, sticky="w", pady=5)
gender_radio_female = tk.Radiobutton(main_frame, text="Female", variable=gender_var, value="Female", font=("Helvetica", 12), bg="#ffffff")
gender_radio_female.grid(row=3, column=1, pady=5)

# Contact Information
tk.Label(main_frame, text="Contact Number:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=4, column=0, sticky="e", pady=5)
entry_patient_contact = tk.Entry(main_frame, font=("Helvetica", 12), width=30, bd=2, relief="solid")
entry_patient_contact.grid(row=4, column=1, pady=5)

# Email
tk.Label(main_frame, text="Email:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=5, column=0, sticky="e", pady=5)
entry_patient_email = tk.Entry(main_frame, font=("Helvetica", 12), width=30, bd=2, relief="solid")
entry_patient_email.grid(row=5, column=1, pady=5)

# Address
tk.Label(main_frame, text="Address:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=6, column=0, sticky="ne", pady=5)
text_address = tk.Text(main_frame, font=("Helvetica", 12), width=30, height=4, bd=2, relief="solid")
text_address.grid(row=6, column=1, pady=5)

# Blood Group
tk.Label(main_frame, text="Blood Group:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=7, column=0, sticky="e", pady=5)
blood_group_var = tk.StringVar()
blood_group_menu = tk.OptionMenu(main_frame, blood_group_var, "A+", "B+", "O+", "AB+", "A-", "B-", "O-", "AB-")
blood_group_menu.config(font=("Helvetica", 12), bg="#ffffff", width=27, bd=2, relief="solid")
blood_group_menu.grid(row=7, column=1, pady=5)

# Medical History (Checkbuttons)
tk.Label(main_frame, text="Medical History (If any):", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=8, column=0, sticky="ne", pady=5)
medical_history_var = tk.IntVar()
check_history = tk.Checkbutton(main_frame, text="Has Medical History", variable=medical_history_var, font=("Helvetica", 12), bg="#ffffff", fg="#34495E")
check_history.grid(row=8, column=1, pady=5)

# Emergency Contact Number
tk.Label(main_frame, text="Emergency Contact No:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=9, column=0, sticky="e", pady=5)
entry_emergency_contact = tk.Entry(main_frame, font=("Helvetica", 12), width=30, bd=2, relief="solid")
entry_emergency_contact.grid(row=9, column=1, pady=5)

# Submit and Clear Buttons
submit_button = tk.Button(main_frame, text="Submit", command=submit_registration, font=("Helvetica", 14, "bold"), bg="#2ecc71", fg="white", relief="raised", bd=2)
submit_button.grid(row=10, column=0, columnspan=2, pady=20)

clear_button = tk.Button(main_frame, text="Clear", command=clear_form, font=("Helvetica", 12), bg="#f39c12", fg="white", relief="raised", bd=2)
clear_button.grid(row=11, column=0, columnspan=2, pady=5)

# Run the application
root.mainloop()
