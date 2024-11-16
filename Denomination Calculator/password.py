import tkinter as tk
def evaluate_strength():
    password = password_entry.get() 
    length = len(password)  
    if length < 6:
        strength_label.config(text="Password Strength: Weak", fg="red")
    elif 6 <= length <= 10:
        strength_label.config(text="Password Strength: Moderate", fg="orange")
    else:
        strength_label.config(text="Password Strength: Strong", fg="green")
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x200")
instruction_label = tk.Label(root, text="Enter your password:", font=("Arial", 12))
instruction_label.pack(pady=10)
password_entry = tk.Entry(root, show="*", font=("Arial", 12), width=20)
password_entry.pack(pady=10)
evaluate_button = tk.Button(root, text="Check Strength", font=("Arial", 12), command=evaluate_strength)
evaluate_button.pack(pady=10)
strength_label = tk.Label(root, text="Password Strength: ", font=("Arial", 12))
strength_label.pack(pady=10)
root.mainloop()

