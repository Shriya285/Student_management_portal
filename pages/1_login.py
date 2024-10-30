import streamlit as st
from utils.auth import register_user, is_user_registered

st.title("Login or Register")

# Login section
with st.form("login_form"):
    st.subheader("Login")
    srn = st.text_input("Enter SRN")
    password = st.text_input("Enter Password", type='password')
    login_button = st.form_submit_button("Login")

if login_button:
    user = is_user_registered(srn, password)
    if user:
        st.session_state["logged_in"] = True
        st.session_state["username"] = user[0]
        st.success(f"Welcome, {user[0]}!")
        st.experimental_rerun()  # Reload to redirect to dashboard
    else:
        st.error("Invalid SRN or password.")

