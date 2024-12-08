# ultimate_insecure_app.py

import os, subprocess, random, math, json  # Multiple unused imports
import sqlite3  # Used but mismanaged

# Hardcoded sensitive information (security issue)
USERNAME = "admin"
PASSWORD = "12345"
API_KEY = "sk_test_super_sensitive_api_key_1234567890"

# SQL Injection vulnerability
def connect_to_db():
    """Connect to the SQLite database."""
    connection = sqlite3.connect("example.db")  # Hardcoded database name
    cursor = connection.cursor()
    return connection, cursor

def create_table():
    """Create a user table."""
    connection, cursor = connect_to_db()
    # Inefficient and insecure table creation
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        )
    """)
    connection.commit()
    connection.close()

def insert_user(username, password):
    """Insert a user (vulnerable to SQL injection)."""
    connection, cursor = connect_to_db()
    query = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
    print(f"Insecure query: {query}")
    cursor.execute(query)  # Vulnerable to SQL injection
    connection.commit()
    connection.close()

def get_user(username):
    """Get user data by username (vulnerable to SQL injection)."""
    connection, cursor = connect_to_db()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    print(f"Executing insecure query: {query}")
    result = cursor.execute(query)  # Vulnerable to SQL injection
    user = result.fetchone()
    connection.close()
    return user

# Inefficient random password generator
def generate_password(length):
    """Generate a random password of given length."""
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ""
    for i in range(0, length):
        password += random.choice(chars)  # Inefficient concatenation in a loop
    return password

# Command injection vulnerability
def execute_system_command(command):
    """Execute a shell command (insecure)."""
    print(f"Executing command: {command}")
    subprocess.call(command, shell=True)  # Vulnerable to shell injection

# Poorly designed math operations
def calculate_large_factorial(n):
    """Calculate factorial with no recursion limit handling."""
    if n < 0:
        raise ValueError("Negative numbers are not allowed.")
    result = 1
    for i in range(1, n + 1):  # Inefficient iterative loop
        result *= i
    return result

# A recursive Fibonacci function (inefficient)
def fibonacci(n):
    """Calculate Fibonacci recursively."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Inefficient recursion

# Logging sensitive data
def log_data(data):
    """Log data insecurely to a file."""
    with open("log.txt", "a") as file:  # Unsecured logging
        file.write(f"Logged data: {data}\n")

# Poor input validation
def risky_input(prompt):
    """Get input without validation."""
    return input(prompt)  # No validation, allows malicious input

# Example usage
if __name__ == "__main__":
    print("Starting the ultimate insecure app...")

    # SQL injection example
    create_table()
    insert_user("alice", "password123")
    insert_user("bob", "ilovecats")
    print("Retrieved user:", get_user("alice' OR '1'='1"))  # SQL injection payload

    # Command injection example
    execute_system_command("ls -la && echo Hacked!")

    # Generate an insecure password
    password = generate_password(16)
    print("Generated password:", password)

    # Calculate a large factorial
    print("Factorial of 10:", calculate_large_factorial(10))

    # Recursive Fibonacci example
    print("Fibonacci of 10:", fibonacci(10))

    # Log sensitive data
    log_data({"username": USERNAME, "password": PASSWORD})

    # Risky user input
    cmd = risky_input("Enter a shell command to execute: ")
    execute_system_command(cmd)  # Dangerous execution of user input
