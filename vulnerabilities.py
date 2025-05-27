#!/usr/bin/env python3
# Security vulnerabilities demonstration app

# VULNERABILITY 1: Hardcoded credentials
DATABASE_PASSWORD = "db_password_123!"
API_KEY = "sk_live_12345abcdef6789"

# VULNERABILITY 2: SQL Injection
import sqlite3

def get_user_data(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Vulnerable to SQL injection
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

# VULNERABILITY 3: Command Injection
import os
import subprocess

def run_system_command(user_command):
    # Vulnerable to command injection
    os.system("echo " + user_command)
    return "Command executed"

# VULNERABILITY 4: Insecure cryptography
import hashlib

def hash_password(password):
    # Using weak MD5 hash
    return hashlib.md5(password.encode()).hexdigest()

# VULNERABILITY 5: Potential path traversal
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Rest of the code...
