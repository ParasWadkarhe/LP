import tkinter as tk
from tkinter import messagebox

# Function to handle fund transfer submission
def submit_transfer():
    sender_account = entry_sender_account.get()
    recipient_account = entry_recipient_account.get()
    amount = entry_amount.get()
    transaction_type = transaction_type_var.get()

    # Validation to ensure fields are filled
    if not sender_account or not recipient_account or not amount or not transaction_type:
        messagebox.showwarning("Incomplete Information", "Please fill all the fields.")
    else:
        messagebox.showinfo("Transaction Successful", f"Funds successfully transferred from {sender_account} to {recipient_account}.")
        clear_form()

# Function to clear form fields
def clear_form():
    entry_sender_account.delete(0, tk.END)
    entry_recipient_account.delete(0, tk.END)
    entry_amount.delete(0, tk.END)
    transaction_type_var.set('')

# Main window setup
root = tk.Tk()
root.title("Fund Transfer")
root.geometry("600x400")
root.config(bg="#f4f6f9")

# Main frame for form content
main_frame = tk.Frame(root, bg="#ffffff", padx=30, pady=30, relief="groove", borderwidth=2)
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# Title
title_label = tk.Label(main_frame, text="Fund Transfer", font=("Helvetica", 20, "bold"), bg="#ffffff", fg="#2C3E50")
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Sender Account
tk.Label(main_frame, text="Sender Account No:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=1, column=0, sticky="e", pady=5)
entry_sender_account = tk.Entry(main_frame, font=("Helvetica", 12), width=30, bd=2, relief="solid")
entry_sender_account.grid(row=1, column=1, pady=5)

# Recipient Account
tk.Label(main_frame, text="Recipient Account No:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=2, column=0, sticky="e", pady=5)
entry_recipient_account = tk.Entry(main_frame, font=("Helvetica", 12), width=30, bd=2, relief="solid")
entry_recipient_account.grid(row=2, column=1, pady=5)

# Amount
tk.Label(main_frame, text="Amount:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=3, column=0, sticky="e", pady=5)
entry_amount = tk.Entry(main_frame, font=("Helvetica", 12), width=30, bd=2, relief="solid")
entry_amount.grid(row=3, column=1, pady=5)

# Transaction Type
tk.Label(main_frame, text="Transaction Type:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=4, column=0, sticky="e", pady=5)
transaction_type_var = tk.StringVar()
transaction_type_menu = tk.OptionMenu(main_frame, transaction_type_var, "Deposit", "Withdrawal", "Transfer")
transaction_type_menu.config(font=("Helvetica", 12), bg="#ffffff", width=28, bd=2, relief="solid")
transaction_type_menu.grid(row=4, column=1, pady=5)

# Submit Button
submit_button = tk.Button(main_frame, text="Submit", command=submit_transfer, font=("Helvetica", 14, "bold"), bg="#2ecc71", fg="white", relief="raised", bd=2)
submit_button.grid(row=5, column=0, columnspan=2, pady=20)

# Clear Button
clear_button = tk.Button(main_frame, text="Clear", command=clear_form, font=("Helvetica", 12), bg="#f39c12", fg="white", relief="raised", bd=2)
clear_button.grid(row=6, column=0, columnspan=2, pady=5)

# Run the application
root.mainloop()
