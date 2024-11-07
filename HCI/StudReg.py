import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_registration():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    course = listbox_courses.get(tk.ACTIVE)
    terms_accepted = terms_var.get()
    
    # Validation to ensure fields are filled
    if not name or not age or not gender or not course or not terms_accepted:
        messagebox.showwarning("Incomplete Information", "Please fill all fields and accept the terms.")
    else:
        messagebox.showinfo("Registration Successful", f"Registration Complete!\n\nName: {name}\nAge: {age}\nGender: {gender}\nCourse: {course}")
        clear_form()

# Function to clear form fields
def clear_form():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    gender_var.set("")
    listbox_courses.selection_clear(0, tk.END)
    terms_var.set(False)

# Main window setup
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("500x500")
root.config(bg="#f4f6f9")

# Main frame for form content
main_frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20, relief="groove", borderwidth=2)
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# Title
title_label = tk.Label(main_frame, text="Student Registration Form", font=("Helvetica", 18, "bold"), bg="#ffffff", fg="#2C3E50")
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Name
tk.Label(main_frame, text="Name:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=1, column=0, sticky="e", pady=5)
entry_name = tk.Entry(main_frame, font=("Helvetica", 12), width=30, bd=2, relief="solid")
entry_name.grid(row=1, column=1, pady=5)

# Age
tk.Label(main_frame, text="Age:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=2, column=0, sticky="e", pady=5)
entry_age = tk.Entry(main_frame, font=("Helvetica", 12), width=30, bd=2, relief="solid")
entry_age.grid(row=2, column=1, pady=5)

# Gender
tk.Label(main_frame, text="Gender:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=3, column=0, sticky="e", pady=5)
gender_var = tk.StringVar()
gender_frame = tk.Frame(main_frame, bg="#ffffff")
gender_frame.grid(row=3, column=1, pady=5, sticky="w")
tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male", font=("Helvetica", 10), bg="#ffffff").pack(side="left")
tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female", font=("Helvetica", 10), bg="#ffffff").pack(side="left")

# Course Selection
tk.Label(main_frame, text="Select Course:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=4, column=0, sticky="e", pady=5)
listbox_courses = tk.Listbox(main_frame, font=("Helvetica", 12), height=4, selectmode=tk.SINGLE, bd=2, relief="solid", width=28)
courses = ["Computer Science", "Mechanical Engineering", "Civil Engineering", "Electrical Engineering", "Data Science"]
for course in courses:
    listbox_courses.insert(tk.END, course)
listbox_courses.grid(row=4, column=1, pady=5)


# Terms and Conditions
terms_var = tk.BooleanVar()
terms_check = tk.Checkbutton(main_frame, text="I accept the terms and conditions", variable=terms_var, font=("Helvetica", 10), bg="#ffffff")
terms_check.grid(row=5, column=0, columnspan=2, pady=10)

# Submit Button
submit_button = tk.Button(main_frame, text="Submit", command=submit_registration, font=("Helvetica", 14, "bold"), bg="#2ecc71", fg="white", relief="raised", bd=2)
submit_button.grid(row=6, column=0, columnspan=2, pady=20)

# Clear Button
clear_button = tk.Button(main_frame, text="Clear", command=clear_form, font=("Helvetica", 12), bg="#f39c12", fg="white", relief="raised", bd=2)
clear_button.grid(row=7, column=0, columnspan=2, pady=5)

# Run the application
root.mainloop()
