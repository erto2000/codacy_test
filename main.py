def calculate_factorial(n):
    """Calculate the factorial of a number recursively."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)

def find_largest_number(numbers):
    """Find the largest number in a list."""
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Example usage
if __name__ == "__main__":
    print("Factorial of 5:", calculate_factorial(5))
    print("Largest number in [3, 5, 7, 2, 8]:", find_largest_number([3, 5, 7, 2, 8]))