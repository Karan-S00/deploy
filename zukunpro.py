import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import tempfile
import datetime

# ----------------- Modern Page Styling -----------------
st.set_page_config(page_title="Supermarket Billing", page_icon="🛒", layout="centered")

st.markdown("""
    <style>
        .main {
            background-color: #f7f9fc;
        }
        .card {
            background: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
            margin-bottom: 18px;
        }
        .title {
            font-size: 32px !important;
            color: #2C3E50;
            font-weight: bold;
            text-align: center;
            margin-bottom: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# ----------------- Title -----------------
st.markdown("<div class='title'>🛒 Supermarket Billing System</div>", unsafe_allow_html=True)

# Product list
products = {
    "Apple": 30, "Banana": 10, "Milk": 50, "Bread": 40,
    "Eggs": 5, "Cheese": 100, "Paneer": 200,
    "Chicken 1kg": 250, "Beef 1kg": 300
}

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🧺 Enter Quantities")
quantities = {}
cols = st.columns(2)

for i, (product, price) in enumerate(products.items()):
    with cols[i % 2]:
        quantities[product] = st.number_input(
            f"{product} (₹{price})",
            min_value=0,
            step=1
        )
st.markdown("</div>", unsafe_allow_html=True)

# GST Section
st.markdown("<div class='card'>", unsafe_allow_html=True)
gst_rate = st.slider("💰 Select GST %", 0, 28, 5)
st.markdown("</div>", unsafe_allow_html=True)

# Calculate Bill
if st.button("Calculate Total ✅"):
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    total = 0
    bill_details = []

    for product, qty in quantities.items():
        if qty > 0:
            cost = qty * products[product]
            total += cost
            bill_details.append((product, qty, cost))

    if total == 0:
        st.warning("No items selected!")
    else:
        gst_amount = (total * gst_rate) / 100
        grand_total = total + gst_amount

        st.subheader("🧾 Bill Summary")
        for item, qty, cost in bill_details:
            st.text(f"{item} × {qty} = ₹{cost}")

        st.write(f"**Subtotal:** ₹{total}")
        st.write(f"**GST ({gst_rate}%):** ₹{gst_amount:.2f}")
        st.write(f"### ✅ Final Total: ₹{grand_total:.2f}")

        # Generate PDF
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            file_path = tmp_file.name
            c = canvas.Canvas(file_path, pagesize=A4)
            y = 800

            c.setFont("Helvetica-Bold", 16)
            c.drawString(200, y, "Supermarket Bill")
            y -= 40

            c.setFont("Helvetica", 12)
            now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
            c.drawString(50, y, f"Date & Time: {now}")
            y -= 30

            for item, qty, cost in bill_details:
                c.drawString(50, y, f"{item} × {qty} = ₹{cost}")
                y -= 20

            y -= 20
            c.drawString(50, y, f"Subtotal: ₹{total}")
            y -= 20
            c.drawString(50, y, f"GST ({gst_rate}%): ₹{gst_amount:.2f}")
            y -= 20
            c.drawString(50, y, f"Grand Total: ₹{grand_total:.2f}")

            c.save()

        with open(file_path, "rb") as pdf_file:
            st.download_button(
                label="📄 Download Bill PDF",
                data=pdf_file,
                file_name="Supermarket_Bill.pdf",
                mime="application/pdf"
            )
    st.markdown("</div>", unsafe_allow_html=True)

# Clear Button
if st.button("🔄 Reset"):
    st.experimental_rerun()
