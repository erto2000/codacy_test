# ultimate_insecure_app_with_duplications.py

import os, subprocess, random, math, json
import sqlite3

# Hardcoded sensitive information (security issue)
USERNAME = "admin"
PASSWORD = "12345"
API_KEY = "sk_test_super_sensitive_api_key_1234567890"

# SQL Injection vulnerability
def connect_to_db():
    """Connect to the SQLite database."""
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    return connection, cursor

hdsflashdkajfsadfadsf

def create_table():
    """Create a user table."""
    connection, cursor = connect_to_db()
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
    cursor.execute(query)
    connection.commit()
    connection.close()

def get_user(username):
    """Get user data by username (vulnerable to SQL injection)."""
    connection, cursor = connect_to_db()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    print(f"Executing insecure query: {query}")
    result = cursor.execute(query)
    user = result.fetchone()
    connection.close()
    return user

# Duplicated SQL functions
def get_user_duplicate(username):
    """Get user data by username (duplicate function)."""
    connection, cursor = connect_to_db()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    print(f"Executing insecure query: {query}")
    result = cursor.execute(query)
    user = result.fetchone()
    connection.close()
    return user

def insert_user_duplicate(username, password):
    """Insert a user (duplicate function)."""
    connection, cursor = connect_to_db()
    query = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
    print(f"Insecure query: {query}")
    cursor.execute(query)
    connection.commit()
    connection.close()

# Inefficient password generation
def generate_password(length):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ""
    for i in range(0, length):
        password += random.choice(chars)
    return password

# Duplicated password generator
def generate_password_duplicate(length):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ""
    for i in range(0, length):
        password += random.choice(chars)
    return password

# Command injection vulnerability
def execute_system_command(command):
    subprocess.call(command, shell=True)

# Duplicated command execution
def execute_system_command_duplicate(command):
    subprocess.call(command, shell=True)

# Recursive Fibonacci (duplicated)
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_duplicate(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_duplicate(n - 1) + fibonacci_duplicate(n - 2)

def long_and_redundant_function(data, multiplier):
    """Perform a series of redundant calculations."""
    result = []
    total = 0

    # Simulated redundant calculations
    for i in range(len(data)):
        value = data[i] * multiplier
        if value % 2 == 0:
            value = value ** 2
        else:
            value = math.sqrt(value) 

        # Add random noise
        noise = random.random() * 0.1
        value += noise

        # Append value to result
        result.append(value)
        total += value

    # Additional redundant loop
    for i in range(len(result)):
        result[i] = result[i] * 2
        if result[i] > 100:
            result[i] = 100

    # Generate summary statistics
    average = total / len(data) if len(data) > 0 else 0
    maximum = max(result) if result else 0
    minimum = min(result) if result else 0

    return {
        "processed_data": result,
        "average": average,
        "max": maximum,
        "min": minimum,
    }

# Duplicate the function with minimal changes
def long_and_redundant_function_duplicate(data, multiplier):
    """Perform a series of redundant calculations (duplicated)."""
    result = []
    total = 0

    # Simulated redundant calculations
    for i in range(len(data)):
        value = data[i] * multiplier
        if value % 2 == 0:
            value = value ** 2
        else:
            value = math.sqrt(value)

        # Add random noise
        noise = random.random() * 0.1
        value += noise

        # Append value to result
        result.append(value)
        total += value

    # Additional redundant loop
    for i in range(len(result)):
        result[i] = result[i] * 2
        if result[i] > 100:
            result[i] = 100

    # Generate summary statistics
    average = total / len(data) if len(data) > 0 else 0
    maximum = max(result) if result else 0
    minimum = min(result) if result else 0

    return {
        "processed_data": result,
        "average": average,
        "max": maximum,
        "min": minimum,
    }

# Example usage
if __name__ == "__main__":
    input_data = [random.randint(1, 10) for _ in range(20)]
    multiplier = 3

    result1 = long_and_redundant_function(input_data, multiplier)
    result2 = long_and_redundant_function_duplicate(input_data, multiplier)

    create_table()

    # Insert users
    insert_user("alice", "password123")
    insert_user("bob", "ilovecats")
    insert_user_duplicate("charlie", "hunter2")

    # Retrieve users
    print(get_user("alice"))
    print(get_user_duplicate("bob"))

    # Command execution
    execute_system_command("echo Hello World")
    execute_system_command_duplicate("echo Duplicate Command")

    # Password generation
    print(generate_password(12))
    print(generate_password_duplicate(12))

    # Fibonacci calculation
    print(fibonacci(10))
    print(fibonacci_duplicate(10))
