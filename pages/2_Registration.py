import streamlit as st
from utils.auth import register_user

def registration():
    st.title("Registration Page")
    srn = st.text_input("SRN")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Register"):
        if srn and username and password:
            if register_user(srn, username, password):
                st.success("Registered Successfully! You can now log in.")
            else:
                st.error("Registration failed. Please try again.")
        else:
            st.error("Please fill in all fields.")

if __name__ == "__main__":
    registration()
