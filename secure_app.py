import sqlite3
import os
import bcrypt

# REMEDIATED SECURE APPLICATION

def get_user_data(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # Remediation 1: Parameterized query prevents SQL Injection
    query = "SELECT id, username, email FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    result = cursor.fetchall()
    conn.close()
    return result

def hash_password(password):
    # Remediation 2: Strong salted password hashing using bcrypt
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

# Remediation 3: Load secrets from environment variables
API_SECRET_KEY = os.environ.get("API_SECRET_KEY")
