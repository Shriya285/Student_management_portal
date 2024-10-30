import streamlit as st
from utils.auth import register_user, is_user_registered


# Registration section
with st.form("registration_form"):
    st.subheader("Register")
    reg_srn = st.text_input("Enter SRN (for registration)")
    reg_username = st.text_input("Enter Username")
    reg_password = st.text_input("Enter Password", type='password')
    reg_button = st.form_submit_button("Register")

if reg_button:
    if register_user(reg_srn, reg_username, reg_password):
        st.success("Registration successful! Please log in.")
    else:
        st.error("Registration failed. Try again.")
