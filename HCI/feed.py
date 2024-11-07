import tkinter as tk
from tkinter import messagebox, filedialog
#pip install tkcalendar
from tkcalendar import DateEntry  # Requires tkcalendar package

# Function to handle form submission
def submit_feedback():
    # Retrieve all field data
    name = entry_name.get()
    email = entry_email.get()
    comments = text_comments.get("1.0", tk.END).strip()
    food_quality = food_quality_var.get()
    cleanliness = cleanliness_var.get()
    management_friendliness = management_friendliness_var.get()

    # Validation for mandatory fields
    if not name or not email or not comments:
        messagebox.showwarning("Incomplete Form", "Please fill in all required fields: Name, Email, and Comments!")
    else:
        # Example: You could save data to a database here
        messagebox.showinfo("Thank You!", "Your feedback has been submitted successfully!")
        clear_form()

# Function to clear form fields
def clear_form():
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    text_comments.delete("1.0", tk.END)
    food_quality_var.set("")
    cleanliness_var.set("")
    management_friendliness_var.set("")

# Function to upload a photo
def upload_photo():
    filedialog.askopenfilename(title="Select a photo", filetypes=[("Image files", "*.jpg *.jpeg *.png")])

# Main window setup
root = tk.Tk()
root.title("Customer Feedback Form")
root.geometry("750x750")  # Adjusted size for additional fields
root.config(bg="#f4f6f9")

# Main frame for form content
main_frame = tk.Frame(root, bg="#ffffff", padx=30, pady=30, relief="groove", borderwidth=2)
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# Title
title_label = tk.Label(main_frame, text="Customer Feedback Form", font=("Helvetica", 20, "bold"), bg="#ffffff", fg="#2C3E50")
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Name and Email
tk.Label(main_frame, text="Name:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=1, column=0, sticky="e", pady=5)
entry_name = tk.Entry(main_frame, font=("Helvetica", 12), width=30, bd=2, relief="solid")
entry_name.grid(row=1, column=1, pady=5)

tk.Label(main_frame, text="Email:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=2, column=0, sticky="e", pady=5)
entry_email = tk.Entry(main_frame, font=("Helvetica", 12), width=30, bd=2, relief="solid")
entry_email.grid(row=2, column=1, pady=5)

# Comments
tk.Label(main_frame, text="Comments:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=3, column=0, sticky="ne", pady=5)
text_comments = tk.Text(main_frame, font=("Helvetica", 12), width=30, height=3, bd=2, relief="solid")
text_comments.grid(row=3, column=1, pady=5)

# Rating Fields
tk.Label(main_frame, text="Food Quality:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=4, column=0, sticky="e", pady=5)
food_quality_var = tk.StringVar()
food_quality_menu = tk.OptionMenu(main_frame, food_quality_var, "Excellent", "Good", "Average", "Poor")
food_quality_menu.config(font=("Helvetica", 12), bg="#ffffff", width=24, bd=2, relief="solid")
food_quality_menu.grid(row=4, column=1, pady=5)

tk.Label(main_frame, text="Place Cleanliness:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=5, column=0, sticky="e", pady=5)
cleanliness_var = tk.StringVar()
cleanliness_menu = tk.OptionMenu(main_frame, cleanliness_var, "Excellent", "Good", "Average", "Poor")
cleanliness_menu.config(font=("Helvetica", 12), bg="#ffffff", width=24, bd=2, relief="solid")
cleanliness_menu.grid(row=5, column=1, pady=5)

tk.Label(main_frame, text="Management Friendliness:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=6, column=0, sticky="e", pady=5)
management_friendliness_var = tk.StringVar()
management_friendliness_menu = tk.OptionMenu(main_frame, management_friendliness_var, "Excellent", "Good", "Average", "Poor")
management_friendliness_menu.config(font=("Helvetica", 12), bg="#ffffff", width=24, bd=2, relief="solid")
management_friendliness_menu.grid(row=6, column=1, pady=5)

# Upload Photo and Permissions
upload_button = tk.Button(main_frame, text="Upload a Photo", command=upload_photo, font=("Helvetica", 10), bg="#3498db", fg="white", relief="raised", bd=2)
upload_button.grid(row=7, column=0, columnspan=2, pady=5)

feedback_use_var = tk.IntVar()
tk.Checkbutton(main_frame, text="I allow my feedback to be used for marketing.", variable=feedback_use_var, font=("Helvetica", 10), bg="#ffffff", fg="#34495E").grid(row=8, column=0, columnspan=2, pady=5)

contact_var = tk.IntVar()
tk.Checkbutton(main_frame, text="I would like to be contacted for follow-up.", variable=contact_var, font=("Helvetica", 10), bg="#ffffff", fg="#34495E").grid(row=9, column=0, columnspan=2, pady=5)

# Submit Button
submit_button = tk.Button(main_frame, text="Submit Feedback", command=submit_feedback, font=("Helvetica", 14, "bold"), bg="#2ecc71", fg="white", relief="raised", bd=2)
submit_button.grid(row=10, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()
