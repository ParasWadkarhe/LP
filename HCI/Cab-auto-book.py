import tkinter as tk
from tkinter import messagebox

# Function to handle booking submission
def submit_booking():
    # Retrieve all form data
    name = entry_name.get()
    pickup_location = entry_pickup.get()
    dropoff_location = entry_dropoff.get()
    vehicle_type = vehicle_var.get()
    payment_method = payment_var.get()

    # Validate mandatory fields
    if not name or not pickup_location or not dropoff_location or not vehicle_type or not payment_method:
        messagebox.showwarning("Incomplete Form", "Please fill in all required fields!")
    else:
        # Here, you can add code to process the booking, save it to a database, or send confirmation email
        messagebox.showinfo("Booking Confirmed", "Your cab booking has been confirmed!")
        clear_form()

# Function to clear the form fields
def clear_form():
    entry_name.delete(0, tk.END)
    entry_pickup.delete(0, tk.END)
    entry_dropoff.delete(0, tk.END)
    vehicle_var.set("")
    payment_var.set("")

# Main window setup
root = tk.Tk()
root.title("Cab/Auto Booking App")
root.geometry("600x600")
root.config(bg="#f2f3f4")

# Main frame for form content
main_frame = tk.Frame(root, bg="#ffffff", padx=30, pady=30, relief="groove", borderwidth=2)
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# Title Label
title_label = tk.Label(main_frame, text="Cab/Auto Booking Form", font=("Helvetica", 20, "bold"), bg="#ffffff", fg="#2C3E50")
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Name
tk.Label(main_frame, text="Full Name:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=1, column=0, sticky="e", pady=5)
entry_name = tk.Entry(main_frame, font=("Helvetica", 12), width=30, bd=2, relief="solid")
entry_name.grid(row=1, column=1, pady=5)

# Pickup Location
tk.Label(main_frame, text="Pickup Location:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=2, column=0, sticky="e", pady=5)
entry_pickup = tk.Entry(main_frame, font=("Helvetica", 12), width=30, bd=2, relief="solid")
entry_pickup.grid(row=2, column=1, pady=5)

# Dropoff Location
tk.Label(main_frame, text="Dropoff Location:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=3, column=0, sticky="e", pady=5)
entry_dropoff = tk.Entry(main_frame, font=("Helvetica", 12), width=30, bd=2, relief="solid")
entry_dropoff.grid(row=3, column=1, pady=5)

# Vehicle Type Selection
tk.Label(main_frame, text="Vehicle Type:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=4, column=0, sticky="e", pady=5)
vehicle_var = tk.StringVar()
vehicle_options = ["Cab", "Auto", "Bike"]
vehicle_menu = tk.OptionMenu(main_frame, vehicle_var, *vehicle_options)
vehicle_menu.config(font=("Helvetica", 12), bg="#ffffff", width=28, bd=2, relief="solid")
vehicle_menu.grid(row=4, column=1, pady=5)

# Payment Method Selection
tk.Label(main_frame, text="Payment Method:", font=("Helvetica", 12), bg="#ffffff", fg="#34495E").grid(row=5, column=0, sticky="e", pady=5)
payment_var = tk.StringVar()
payment_options = ["Cash", "Credit Card", "Debit Card", "UPI"]
payment_menu = tk.OptionMenu(main_frame, payment_var, *payment_options)
payment_menu.config(font=("Helvetica", 12), bg="#ffffff", width=28, bd=2, relief="solid")
payment_menu.grid(row=5, column=1, pady=5)

# Buttons
button_frame = tk.Frame(main_frame, bg="#ffffff")
button_frame.grid(row=6, column=0, columnspan=2, pady=20)

submit_button = tk.Button(button_frame, text="Submit Booking", command=submit_booking, font=("Helvetica", 12, "bold"), bg="#3498db", fg="white", relief="raised", bd=2)
submit_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="Clear", command=clear_form, font=("Helvetica", 12, "bold"), bg="#e74c3c", fg="white", relief="raised", bd=2)
clear_button.grid(row=0, column=1, padx=10)

# Run the main window
root.mainloop()
