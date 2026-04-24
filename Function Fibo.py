def add_numbers(num1, num2):
    """This function adds two numbers and returns the result"""
    sum_result = num1 + num2
    return sum_result
a = 5
b = 10
result = add_numbers(a, b)
print(f"The sum of {a} and {b} is: {result}")

# Example of a simple function without parameters
def say_hello():
    print("Hello! This is a simple function call.")
say_hello()

# Function to generate Fibonacci series
def fibonacci(n):
    # Starting values for Fibonacci series
    a = 0
    b = 1
    # Loop to print the series
    for i in range(n):
        print(a, end=" ")
        next_term = a + b
        # Update values
        a = b
        b = next_term
terms = int(input("Enter the number of terms: "))
# Calling the function
fibonacci(terms)