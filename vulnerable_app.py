```python
import sqlite3
import hashlib

# VULNERABLE APPLICATION FOR AUDIT PURPOSES ONLY

def get_user_data(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # Vulnerability 1: SQL Injection via string formatting
    query = f"SELECT id, username, email FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()

def hash_password(password):
    # Vulnerability 2: Weak cryptographic hashing (MD5 without salt)
    return hashlib.md5(password.encode()).hexdigest()

# Vulnerability 3: Hardcoded secret API key
API_SECRET_KEY = "sk_live_9876543210_super_secret_key"
