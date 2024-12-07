import tkinter as tk
from tkinter import ttk, messagebox
class RetaurantOrderManagement:
    def __init__(self, root):
        self.root=root
        self.root.title("Restaurant Management App")
        self.menu_items={"FRIESMEA": 2, "LUNCH MEAL": 2, "BURGER MEAL": 3, "PIZZA MEAL": 4, "CHEESE BURGER": 2.5, "DRINKS": 1 }
    self.exchange_rate=82
    self.setup_background(root)
    frame=ttk.Frame(root)
    frame.place[relx=0.5, rely=0.5, anchor=tk.CENTER)]
    ttk.Label(frame, text="Restaurant Oder Managemnt, font=("Arial", 20, "bold")).grind(row=0, columnspan3, padx=10, pady=10)
    self.menu_labels={}
    self.menu_quantites={}
    for i, (item, price) in enumerate(self.menu_items.items(), start=1):
        label=ttk.Label(frame, text=f"{item} (${price}):",font=("Aria",12))
        label.grid(row=i, column=0, padx=10, pady=5)
        self.menu_labels[item]=label
        quantity_entry=ttk.Entry(frame, width=5)
        quantity_entry.grid
        quantity_entry.grid(row=i, column1, padx=10, pady=5)
        self.menu_quantities[item]=quantity_entry
    self.curreny_var=tk.StringVar()
    ttk.Label(frame, text="Currency:", font=("Arial", 12)).grid(row=len(self.menu_items)+1, column=0, padx=10,pady=5)
    currency_dropdown= ttk.Cobobox(frame, textvarriable=self.currency_var, state="readonly", width=18, values=("USD", "INR"))
    currency_dropdown.grid(row=len(self.menu_items)+1, column=1, padx=10, pady=5)
    currency_dropdown.current(0)      
    self.currency_var.trace("w", self.updatee_menu_prices)
    order_button=ttk.Button(frame, tet="Plae Order", command=self.palce_order)
    order_button.grid(row=len(self.menu_items)+ 2,columnspan=3, padx=10, pady=10)
def set_background(self, root):
    bg_width, bg_height=800,600
    canvas=tk.Canvas(root, width=bg_width, height=bg_height)
    canvas.pack()
    original_image=tk.PhotoImage(file="background.png")
    background_image=oringial_image.subsample(orignal_image.width()//bg_width,original_image.height()//bg_height)
    
