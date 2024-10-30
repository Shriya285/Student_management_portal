import hashlib
from utils.db import create_connection
import streamlit as st

def hash_password(password):
    """Hash the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(srn, username, password):
    """Register a new user."""
    hashed_password = hash_password(password)
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO Users (SRN, Username, Password) VALUES (%s, %s, %s)",
                (srn, username, hashed_password)
            )
            connection.commit()
            return True  # Registration successful
        except Exception as e:
            st.error(f"Registration error: {e}")
            return False  # Registration failed
        finally:
            cursor.close()
            connection.close()

def is_user_registered(srn, password):
    """Check if user credentials are valid."""
    hashed_password = hash_password(password)
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT Username FROM Users WHERE SRN = %s AND Password = %s",
                (srn, hashed_password)
            )
            result = cursor.fetchone()
            return result  # Return user info if valid
        except Exception as e:
            st.error(f"Login error: {e}")
            return None
        finally:
            cursor.close()
            connection.close()
    return None  # User not found or incorrect credentials
