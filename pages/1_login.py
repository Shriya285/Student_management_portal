import streamlit as st
from utils.auth import is_user_registered
#updated
def login():
    st.title("Login Page")
    srn = st.text_input("SRN")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        user=is_user_registered(srn, password)
        if user:
            st.session_state["logged_in"] = True
            st.session_state["username"] = user[0]
            st.success("Sucess")
            # st.experimental_rerun()  # Redirect to the dashboard after showing the message
        else:
            st.error("Invalid SRN or password.")


if __name__ == "__main__":
    login()
