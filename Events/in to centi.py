import tkinter as tk
def convert_to_centimeters():
    inches = float(entry.get())
    centimeters = inches * 2.54
    result_label.config(text=f"{inches} inches is {centimeters:.2f} centimeters")
root = tk.Tk()
root.title("Inches to Centimeters Converter")
input_label = tk.Label(root, text="Enter inches:")
input_label.pack()
entry = tk.Entry(root)
entry.pack()
convert_button = tk.Button(root, text="Convert", command=convert_to_centimeters)
convert_button.pack()
result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()
