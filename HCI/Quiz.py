import tkinter as tk
from tkinter import messagebox

# Sample questions and answers for the quiz
questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Rome"], "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Venus", "Mars", "Jupiter"], "answer": "Mars"},
    {"question": "What is the largest mammal?", "options": ["Elephant", "Blue Whale", "Shark", "Giraffe"], "answer": "Blue Whale"},
    {"question": "Which is the smallest prime number?", "options": ["2", "3", "5", "7"], "answer": "2"},
    {"question": "What gas do plants absorb?", "options": ["Oxygen", "Hydrogen", "Carbon Dioxide", "Nitrogen"], "answer": "Carbon Dioxide"},
    {"question": "Who wrote 'Romeo and Juliet'?", "options": ["Shakespeare", "Hemingway", "Austen", "Orwell"], "answer": "Shakespeare"},
    {"question": "What is H2O commonly known as?", "options": ["Oxygen", "Water", "Acid", "Hydrogen"], "answer": "Water"},
    {"question": "What is the boiling point of water?", "options": ["100°C", "50°C", "0°C", "25°C"], "answer": "100°C"}
]

# Initialize variables
current_question = 0
score = 0
question_status = ["unsolved" for _ in questions]  # Track each question's status: "unsolved", "solved", "marked"

# Function to update heatmap colors
def update_heatmap():
    for idx, status in enumerate(question_status):
        if status == "solved":
            heatmap_buttons[idx].config(bg="#4CAF50")  # Green
        elif status == "unsolved":
            heatmap_buttons[idx].config(bg="#F44336")  # Red
        elif status == "marked":
            heatmap_buttons[idx].config(bg="#FFC107")  # Yellow

# Function to load a question
def load_question():
    global current_question
    question = questions[current_question]
    question_label.config(text=f"Q{current_question + 1}: {question['question']}")
    selected_option.set(None)
    
    for idx, option in enumerate(question["options"]):
        option_buttons[idx].config(text=option, value=option)
    
    update_heatmap()

# Function to mark the current question as solved
def mark_solved():
    selected = selected_option.get()
    if selected == questions[current_question]["answer"]:
        question_status[current_question] = "solved"
    else:
        question_status[current_question] = "unsolved"

# Function for "Next" button
def next_question():
    mark_solved()
    global current_question
    if current_question < len(questions) - 1:
        current_question += 1
        load_question()

# Function for "Previous" button
def previous_question():
    mark_solved()
    global current_question
    if current_question > 0:
        current_question -= 1
        load_question()

# Function to mark a question for review
def mark_for_review():
    question_status[current_question] = "marked"
    update_heatmap()

# Function to end the quiz and show score
def end_quiz():
    mark_solved()  # Mark the last answered question
    final_score = question_status.count("solved")
    messagebox.showinfo("Quiz Completed", f"Your Score: {final_score}/{len(questions)}")
    root.quit()

# Main window
root = tk.Tk()
root.title("Online Quiz")
root.geometry("600x500")
root.config(bg="#f2f5f9")

# Main frame for better organization and padding
main_frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20, relief="groove", borderwidth=2)
main_frame.pack(pady=20)

# Title label
title_label = tk.Label(main_frame, text="Online Quiz", font=("Times New Roman", 20, "bold"), bg="#ffffff", fg="#3f51b5")
title_label.pack(pady=(0, 20))

# Question label
question_label = tk.Label(main_frame, text="", font=("Times New Roman", 14), bg="#ffffff", fg="#333")
question_label.pack(pady=10)

# Variable to store selected option
selected_option = tk.StringVar(root)

# Option buttons
option_buttons = []
for i in range(4):
    option_button = tk.Radiobutton(main_frame, text="", variable=selected_option, font=("Times New Roman", 12),
                                   bg="#ffffff", fg="#333", activebackground="#ffffff", value="", anchor="w")
    option_button.pack(fill="x", padx=10, pady=5)
    option_buttons.append(option_button)

# Navigation buttons
nav_frame = tk.Frame(main_frame, bg="#ffffff")
nav_frame.pack(pady=10)

previous_button = tk.Button(nav_frame, text="Previous", command=previous_question, font=("Times New Roman", 12),
                            bg="#3f51b5", fg="white", padx=10, pady=5)
previous_button.grid(row=0, column=0, padx=5)

next_button = tk.Button(nav_frame, text="Next", command=next_question, font=("Times New Roman", 12),
                        bg="#3f51b5", fg="white", padx=10, pady=5)
next_button.grid(row=0, column=1, padx=5)

mark_button = tk.Button(nav_frame, text="Mark for Review", command=mark_for_review, font=("Times New Roman", 12),
                        bg="#FFC107", fg="black", padx=10, pady=5)
mark_button.grid(row=0, column=2, padx=5)

submit_button = tk.Button(nav_frame, text="Submit Quiz", command=end_quiz, font=("Times New Roman", 12, "bold"),
                          bg="#4CAF50", fg="white", padx=10, pady=5)
submit_button.grid(row=0, column=3, padx=5)

# Heatmap frame to track question status
heatmap_frame = tk.Frame(root, bg="#f2f5f9")
heatmap_frame.pack(pady=10)

heatmap_buttons = []
for i in range(len(questions)):
    btn = tk.Button(heatmap_frame, text=f"Q{i+1}", width=4, font=("Times New Roman", 10, "bold"), bg="#F44336", fg="white")
    btn.grid(row=0, column=i, padx=5)
    heatmap_buttons.append(btn)

# Load the first question
load_question()

# Run the application
root.mainloop()
