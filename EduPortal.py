import streamlit as st

# Initialize session state for login tracking
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
    st.session_state["username"] = ""
    st.session_state["message"] = ""  # Add a message state

st.set_page_config(page_title="Course Material Platform", layout="wide")

# Main entry point
def main():
    st.sidebar.title("Navigation")
    
    if st.session_state["logged_in"]:
        st.sidebar.success(f"Logged in as {st.session_state['username']}")
    else:
        st.sidebar.warning("Please log in to access the dashboard.")

    # Display success message if it exists
    if st.session_state["message"]:
        st.success(st.session_state["message"])
        st.session_state["message"] = ""  # Clear message after displaying

    st.write(
        """
        ### Welcome to the Course Material Platform!

        Use the sidebar to navigate between pages.
        """
    )

if __name__ == "__main__":
    main()
