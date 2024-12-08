# insecure_app.py

import os
import subprocess
import random

# Hardcoded credentials (security issue)
DB_USERNAME = "admin"
DB_PASSWORD = "password123"

# SQL Injection vulnerability
def get_user_data(user_id):
    """Retrieve user data from a database (insecure)."""
    query = f"SELECT * FROM users WHERE id = {user_id};"  # Unsafe string interpolation
    # Simulated insecure database execution
    print(f"Executing query: {query}")
    return "Simulated result"

# Hardcoded sensitive API key (security issue)
API_KEY = "sk_test_51JHGK3X0jfasdfkasjdf92834"

# Poor exception handling
def divide_numbers(a, b):
    """Divide two numbers."""
    try:
        return a / b
    except:
        print("An error occurred!")  # Catch-all exception, no logging

# Using subprocess insecurely
def run_command(cmd):
    """Run a shell command."""
    subprocess.call(cmd, shell=True)  # Vulnerable to shell injection

# Unused import and dead code
def generate_random_numbers():
    """Generate random numbers."""
    result = []
    for i in range(0, 10):
        number = random.randint(1, 100)  # Inefficient loop
    return result  # Result is never used

# Example usage
if __name__ == "__main__":
    print("Starting insecure app...")
    user_data = get_user_data("1 OR 1=1")  # Example SQL injection payload
    print("User Data:", user_data)

    print("Result of division:", divide_numbers(10, 0))  # Intentional division by zero
    run_command("ls -la")  # Command execution with no validation
