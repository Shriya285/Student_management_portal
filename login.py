import mysql.connector as mc
import hashlib
import streamlit as st
from registration import create_connection

# Check if user is registered (for login)
def is_user_registered(srn, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT Username FROM Users WHERE SRN = %s AND Password = %s",
                (srn, hashed_password)
            )
            result = cursor.fetchone()
            return result
        except mc.Error as e:
            st.error(f"Login error: {e}")
        finally:
            cursor.close()
            connection.close()
    return None
