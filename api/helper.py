"""
helper functions script
"""
import requests
import math

# Function to check if a number is prime
def is_prime(n):
    # Handle negative numbers
    n = abs(n)
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Function to check if a number is perfect
def is_perfect(n):
    # Handle negative numbers
    n = abs(n)
    if n < 2:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

# Function to check if a number is an Armstrong number
def is_armstrong(n):
    # Handle negative numbers
    n = abs(n)
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

# Function to get the sum of digits
def sum_of_digits(n):
    # Handle negative numbers
    return sum(int(digit) for digit in str(abs(n)))

# Function to fetch a fun fact about the number
def fetch_fun_fact(n):
    # Use absolute value for API call
    abs_n = abs(n)
    url = f"http://numbersapi.com/{abs_n}/math?json"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            fact = response.json().get("text", "No fun fact available.")
            
            # Add context for negative numbers
            if n < 0:
                fact = f"Fact about the absolute value {abs_n}: {fact}"
            
            return fact
        return "Could not fetch fun fact."
    except requests.exceptions.RequestException:
        return "Fun fact service unavailable."