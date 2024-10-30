import mysql.connector as mc
import streamlit as st

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Shriya@123',
    'database': 'CourseworkMaterial',
    'auth_plugin': 'mysql_native_password'
}

def create_connection():
    try:
        connection = mc.connect(**DB_CONFIG)
        if connection.is_connected():
            return connection
    except mc.Error as e:
        st.error(f"Database connection error: {e}")
    return None
