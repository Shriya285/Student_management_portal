# import streamlit as st

# def dashboard():
#     if not st.session_state.get("logged_in"):
#         st.warning("You need to log in to view the dashboard.")
#         st.button("Go to Login", on_click=lambda: st.experimental_rerun())
#         return

#     st.title("Dashboard")
#     st.write("Welcome to your Dashboard, {st.session_state['username']}!")

# if __name__ == "__main__":
#     dashboard()

import streamlit as st

# Redirect to login page if not logged in
if not st.session_state.get("logged_in", False):
    st.warning("You need to log in to view the dashboard.")
    st.button("Go to Login", on_click=lambda: st.experimental_rerun())
    st.stop()

st.title(f"Welcome to your Dashboard, {st.session_state['username']}!")

st.write("Here you can access your courses, assignments, and materials.")

if st.button("Logout"):
    st.session_state["logged_in"] = False
    st.session_state["username"] = ""
    st.experimental_rerun()  # Redirect back to login page
