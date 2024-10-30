import streamlit as st

# Redirect to login page if not logged in
if not st.session_state.get("logged_in", False):
    st.warning("Please log in to access the dashboard.")
    st.stop()

st.title(f"Welcome to your Dashboard, {st.session_state['username']}!")

st.write("Here you can access your courses, assignments, and materials.")

if st.button("Logout"):
    st.session_state["logged_in"] = False
    st.session_state["username"] = ""
    st.experimental_rerun()  # Redirect back to login page
