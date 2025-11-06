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
