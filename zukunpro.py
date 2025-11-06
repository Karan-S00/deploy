import streamlit as st

# Product list with prices
products = {
    "Apple": 30, "Banana": 10, "Milk": 50, "Bread": 40,
    "Eggs": 5, "Cheese": 100, "Paneer": 200,
    "Chicken 1kg": 250, "Beef 1kg": 300
}

st.title("🛒 Supermarket Billing System")

st.write("Enter quantity for each item:")

qty_inputs = {}
for product, price in products.items():
    qty = st.number_input(f"{product} (₹{price})", min_value=0, step=1, key=product)
    qty_inputs[product] = qty

# Calculate button
if st.button("Calculate Total"):
    total = 0
    bill_details = ""

    for product, qty in qty_inputs.items():
        if qty > 0:
            cost = qty * products[product]
            total += cost
            bill_details += f"{product} x {qty} = ₹{cost}\n"

    if total == 0:
        st.warning("No items selected.")
    else:
        st.success(f"### Total Bill: ₹{total}")
        st.text_area("Bill Details", bill_details + f"\nTotal: ₹{total}", height=200)

# Clear button - Page refresh simulation
if st.button("Clear"):
    st.experimental_rerun()
