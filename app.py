import streamlit as st

st.set_page_config(page_title="Royal Irish Automobile Club", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", [
    "📥 Upload Parking Records",
    "📖 Parking History",
    "👥 Members",
    "📊 Financial Report",
    "🧾 Invoices"
])

if page == "📥 Upload Parking Records":
    st.title("Register Parking Records")
    st.write("Manual entry and upload Excel file with In/Out Days and Hours.")
    # Placeholder

elif page == "📖 Parking History":
    st.title("Parking History")
    st.write("Search by Member ID or upload historical Excel file.")

elif page == "👥 Members":
    st.title("Members")
    st.write("Register members manually or via Excel upload.")

elif page == "📊 Financial Report":
    st.title("Financial Report")
    st.write("Generate summaries of invoices, revenue, and payment tracking.")

elif page == "🧾 Invoices":
    st.title("Invoices")
    st.write("Generate, download, and email invoices. Track paid/unpaid status.")
