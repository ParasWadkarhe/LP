import tkinter as tk
from tkinter import messagebox


# Function to close the Help screen
def close_help():
    root.destroy()


# Main window setup
root = tk.Tk()
root.title("App Help")
root.geometry("700x600")
root.config(bg="#f4f6f9")

# Main frame for the Help screen content
main_frame = tk.Frame(root, bg="#ffffff", padx=30, pady=30, relief="groove", borderwidth=2)
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# Title
title_label = tk.Label(main_frame, text="Help & Support", font=("Helvetica", 18, "bold"), bg="#ffffff", fg="#2C3E50")
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Instructions Section
instructions_label = tk.Label(main_frame, text="How to Use the App:", font=("Helvetica", 14, "bold"), bg="#ffffff", fg="#2C3E50")
instructions_label.grid(row=1, column=0, columnspan=2, pady=(0, 10))

instructions_text = """1. Start by signing up for an account.
2. Once logged in, you can access the main menu.
3. Navigate through the app using the navigation bar.
4. To complete a task, select the appropriate option from the menu and follow the instructions.
5. Use the 'Help' section for any additional assistance."""
text_instructions = tk.Label(main_frame, text=instructions_text, font=("Helvetica", 12), bg="#ffffff", fg="#34495E", justify="left")
text_instructions.grid(row=2, column=0, columnspan=2, pady=5)

# Troubleshooting Section
troubleshooting_label = tk.Label(main_frame, text="Troubleshooting:", font=("Helvetica", 14, "bold"), bg="#ffffff", fg="#2C3E50")
troubleshooting_label.grid(row=3, column=0, columnspan=2, pady=(15, 10))

troubleshooting_text = """- If you are having issues logging in, check your username and password.
- Ensure you have a stable internet connection.
- For any bugs or errors, please report them via the support link."""
text_troubleshooting = tk.Label(main_frame, text=troubleshooting_text, font=("Helvetica", 12), bg="#ffffff", fg="#34495E", justify="left")
text_troubleshooting.grid(row=4, column=0, columnspan=2, pady=5)

# Contact Information Section
contact_label = tk.Label(main_frame, text="Contact Support:", font=("Helvetica", 14, "bold"), bg="#ffffff", fg="#2C3E50")
contact_label.grid(row=5, column=0, columnspan=2, pady=(15, 10))

contact_text = """If you need further assistance, you can reach our support team via the following channels:
- Email: support@app.com
- Phone: +1 234 567 890
- Website: www.app.com/contact"""
text_contact = tk.Label(main_frame, text=contact_text, font=("Helvetica", 12), bg="#ffffff", fg="#34495E", justify="left")
text_contact.grid(row=6, column=0, columnspan=2, pady=5)

# Button to close Help screen
close_button = tk.Button(main_frame, text="Close", command=close_help, font=("Helvetica", 14, "bold"), bg="#e74c3c", fg="white", relief="raised", bd=2)
close_button.grid(row=7, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()
