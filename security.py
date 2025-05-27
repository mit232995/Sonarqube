Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #!/usr/bin/env python3
... # Security vulnerabilities demonstration app
... 
... # VULNERABILITY 1: Hardcoded credentials
... DATABASE_PASSWORD = "db_password_123!"
... API_KEY = "sk_live_12345abcdef6789"
... 
... # VULNERABILITY 2: SQL Injection
... import sqlite3
... 
... def get_user_data(username):
...     conn = sqlite3.connect('users.db')
...     cursor = conn.cursor()
...     # Vulnerable to SQL injection
...     query = "SELECT * FROM users WHERE username = '" + username + "'"
...     cursor.execute(query)
...     result = cursor.fetchall()
...     conn.close()
...     return result
... 
... # VULNERABILITY 3: Command Injection
... import os
... import subprocess
... 
... def run_system_command(user_command):
...     # Vulnerable to command injection
...     os.system("echo " + user_command)
...     return "Command executed"
... 
... # VULNERABILITY 4: Insecure cryptography
... import hashlib
... 
... def hash_password(password):
...     # Using weak MD5 hash
...     return hashlib.md5(password.encode()).hexdigest()
... 
... # VULNERABILITY 5: Potential path traversal
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# CODE SMELL: Unused imports
import json
import random
import time
import sys

# BUG: Division by zero risk
def calculate_average(values):
    total = sum(values)
    return total / len(values)  # Can fail with empty list

# Main application
def main():
    # Print sensitive information
    print(f"Connecting with API key: {API_KEY}")
    
    # Simulate SQL injection vulnerability
    user_input = "admin' OR '1'='1"
    users = get_user_data(user_input)
    
    # Command injection example
    run_system_command("date | grep 2025")
    
    # Weak hashing
    user_password = "password123"
    hashed = hash_password(user_password)
    print(f"Hashed password: {hashed}")
    
    # Path traversal risk
    try:
        config = read_file("../config.ini")
    except:
        pass
    
    # Bug demonstration
    try:
        avg = calculate_average([])
    except ZeroDivisionError:
        pass

if __name__ == "__main__":
