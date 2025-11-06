'''from tkinter import *

# Create main window
window = Tk()
window.geometry("500x400")
window.title("Food Order System")

# Prices dictionary
prices = {
    "Aloo Paratha": 30,
    "Samosa": 5,
    "Pizza": 150,
    "Chilli Potato": 50,
    "Chowmein": 70,
    "Gulab Jamun": 35
}

# Labels and Entry widgets for items
labels = {}
entries = {}

y_pos = 50
for item, price in prices.items():
    labels[item] = Label(window, text=f"{item} (Rs {price})", font=("Arial", 14))
    labels[item].place(x=30, y=y_pos)
    entries[item] = Entry(window, width=5)
    entries[item].place(x=250, y=y_pos)
    y_pos += 40

# Function to calculate total bill
def calculate_total():
    total = 0
    for item in prices:
        qty_text = entries[item].get()
        if qty_text.isdigit():
            qty = int(qty_text)
            total += prices[item] * qty
    bill_label.config(text=f"Total Bill: Rs {total}")

# Button to calculate bill
calculate_btn = Button(window, text="Calculate Bill", command=calculate_total, font=("Arial", 14))
calculate_btn.place(x=150, y=y_pos+20)

# Label to display total bill
bill_label = Label(window, text="Total Bill: Rs 0", font=("Arial", 16, "bold"))
bill_label.place(x=150, y=y_pos+60)

# Run the GUI loop
window.mainloop()'''

'''import tkinter as tk
from tkinter import messagebox

class BusTicketBooking(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bus Ticket Booking System")
        self.geometry("400x300")

        # Passenger name entry
        tk.Label(self, text="Passenger Name:").pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        # Source selection
        tk.Label(self, text="Source:").pack()
        self.source_var = tk.StringVar(value="Delhi")
        sources = ["Delhi","coimbatore","chennai"]
        self.source_menu = tk.OptionMenu(self, self.source_var, *sources)
        self.source_menu.pack()

        # Destination selection
        tk.Label(self, text="Destination:").pack()
        self.destination_var = tk.StringVar(value="Mumbai")
        destinations = ["Mumbai", "Chennai", "Pune", "Kolkata"]
        self.dest_menu = tk.OptionMenu(self, self.destination_var, *destinations)
        self.dest_menu.pack()

        # Seat number entry
        tk.Label(self, text="Seat Number:").pack()
        self.seat_entry = tk.Entry(self)
        self.seat_entry.pack()

        # Book button
        self.book_btn = tk.Button(self, text="Book Ticket", command=self.book_ticket)
        self.book_btn.pack(pady=10)

        # Ticket display
        self.ticket_display = tk.Text(self, height=6, width=40)
        self.ticket_display.pack()

    def book_ticket(self):
        name = self.name_entry.get()
        source = self.source_var.get()
        destination = self.destination_var.get()
        seat = self.seat_entry.get()

        if not name or not seat:
            messagebox.showwarning("Input Error", "Please fill all the fields")
            return

        # Generate ticket id
        ticket_id = source[0].upper() + destination[0].upper() + seat.zfill(2)

        # Display ticket details
        ticket_info = f"--- Bus Ticket ---\nPassenger: {name}\nFrom: {source}\nTo: {destination}\nSeat: {seat}\nTicket ID: {ticket_id}\n"
        self.ticket_display.delete(1.0, tk.END)
        self.ticket_display.insert(tk.END, ticket_info)

if __name__ == "__main__":
    app = BusTicketBooking()
    app.mainloop()'''

'''import tkinter as tk
from tkinter import messagebox

class SupermarketBilling:
    def __init__(self, root):
        self.root = root
        self.root.title("Supermarket Billing System")
        self.root.geometry("500x550")

        # Prices for products
        self.products = {
            "Apple": 30,
            "Banana": 10,
            "Milk": 50,
            "Bread": 40,
            "Eggs": 5,
            "cheese":100,
            "paneer":200,
            "chicken 1kg":250,
            "Beef 1kg":300
        }

        self.entries = {}
        row = 0
        tk.Label(root, text="Product", font=('Arial', 14, 'bold')).grid(row=row, column=0, padx=10, pady=10)
        tk.Label(root, text="Price", font=('Arial', 14, 'bold')).grid(row=row, column=1, padx=10, pady=10)
        tk.Label(root, text="Qty", font=('Arial', 14, 'bold')).grid(row=row, column=2, padx=10, pady=10)
        row += 1

        for product, price in self.products.items():
            tk.Label(root, text=product, font=('Arial', 12)).grid(row=row, column=0, padx=10, pady=5)
            tk.Label(root, text=f"₹{price}", font=('Arial', 12)).grid(row=row, column=1, padx=10, pady=5)
            qty_entry = tk.Entry(root, width=10)
            qty_entry.grid(row=row, column=2, padx=10, pady=5)
            self.entries[product] = qty_entry
            row += 1

        self.total_label = tk.Label(root, text="Total: ₹0", font=('Arial', 14, 'bold'))
        self.total_label.grid(row=row, column=0, columnspan=3, pady=20)

        btn_total = tk.Button(root, text="Calculate Total", command=self.calculate_total)
        btn_total.grid(row=row+1, column=0, pady=10)

        btn_clear = tk.Button(root, text="Clear", command=self.clear_entries)
        btn_clear.grid(row=row+1, column=1, pady=10)

        btn_exit = tk.Button(root, text="Exit", command=root.quit)
        btn_exit.grid(row=row+1, column=2, pady=10)

    def calculate_total(self):
        total = 0
        bill_details = ""
        for product, entry in self.entries.items():
            qty_text = entry.get()
            if qty_text.isdigit():
                qty = int(qty_text)
                if qty > 0:
                    price = self.products[product]
                    cost = qty * price
                    total += cost
                    bill_details += f"{product} x {qty} = ₹{cost}\n"
            elif qty_text.strip() != "":
                messagebox.showerror("Invalid input", f"Quantity for {product} must be a number")
                return
        self.total_label.config(text=f"Total: ₹{total}")
        if total > 0:
            messagebox.showinfo("Bill Details", bill_details + f"\nTotal Amount: ₹{total}")
        else:
            messagebox.showinfo("Bill Details", "No items selected")

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.total_label.config(text="Total: ₹0")

if __name__ == "__main__":
    root = tk.Tk()
    app = SupermarketBilling(root)
    root.mainloop()'''


import tkinter as tk
from tkinter import messagebox

class SupermarketBilling:
    def __init__(self, root):
        root.title("Supermarket Billing System")
        root.geometry("500x550")

        self.products = {
            "Apple": 30, "Banana": 10, "Milk": 50, "Bread": 40,
            "Eggs": 5, "Cheese": 100, "Paneer": 200,
            "Chicken 1kg": 250, "Beef 1kg": 300
        }

        tk.Label(root, text="Product", font=('Arial', 14, 'bold')).grid(row=0, column=0, padx=10, pady=10)
        tk.Label(root, text="Price", font=('Arial', 14, 'bold')).grid(row=0, column=1)
        tk.Label(root, text="Qty", font=('Arial', 14, 'bold')).grid(row=0, column=2)

        self.entries = {}
        for i, (product, price) in enumerate(self.products.items(), start=1):
            tk.Label(root, text=product, font=('Arial', 12)).grid(row=i, column=0, padx=10, pady=5)
            tk.Label(root, text=f"₹{price}", font=('Arial', 12)).grid(row=i, column=1)
            self.entries[product] = tk.Entry(root, width=10)
            self.entries[product].grid(row=i, column=2)

        self.total_label = tk.Label(root, text="Total: ₹0", font=('Arial', 14, 'bold'))
        self.total_label.grid(row=len(self.products)+1, column=0, columnspan=3, pady=20)

        tk.Button(root, text="Calculate Total", command=self.calculate_total).grid(row=len(self.products)+2, column=0)
        tk.Button(root, text="Clear", command=self.clear_entries).grid(row=len(self.products)+2, column=1)
        tk.Button(root, text="Exit", command=root.quit).grid(row=len(self.products)+2, column=2)

    def calculate_total(self):
        total, details = 0, ""
        for p, e in self.entries.items():
            qty = e.get()
            if qty.isdigit() and int(qty) > 0:
                cost = int(qty) * self.products[p]
                total += cost
                details += f"{p} x {qty} = ₹{cost}\n"
            elif qty.strip():
                return messagebox.showerror("Invalid input", f"Quantity for {p} must be a number")

        self.total_label.config(text=f"Total: ₹{total}")
        messagebox.showinfo("Bill Details", details + f"\nTotal: ₹{total}" if total else "No items selected")

    def clear_entries(self):
        for e in self.entries.values():
            e.delete(0, tk.END)
        self.total_label.config(text="Total: ₹0")

if __name__ == "__main__":
    root = tk.Tk()
    SupermarketBilling(root)
    root.mainloop()
