import tkinter as tk
def calculate_interest():
    principal = float(entry_principal.get())
    time = float(entry_time.get())
    rate = float(entry_rate.get())
    simple_interest = (principal * rate * time) / 100
    compound_interest = principal * (1 + rate / 100) ** time - principal
    result_simple.config(text=f"Simple Interest: {simple_interest:.2f}")
    result_compound.config(text=f"Compound Interest: {compound_interest:.2f}")
root = tk.Tk()
root.title("Interest Calculator")
label_principal = tk.Label(root, text="Initial Amount (Principal):")
label_principal.pack()
entry_principal = tk.Entry(root)
entry_principal.pack()
label_time = tk.Label(root, text="Time Period (in years):")
label_time.pack()
entry_time = tk.Entry(root)
entry_time.pack()
label_rate = tk.Label(root, text="Rate of Interest (in %):")
label_rate.pack()
entry_rate = tk.Entry(root)
entry_rate.pack()
button_calculate = tk.Button(root, text="Calculate Interest", command=calculate_interest)
button_calculate.pack()
result_simple = tk.Label(root, text="")
result_simple.pack()
result_compound = tk.Label(root, text="")
result_compound.pack()
root.mainloop()
