# Create a function that calculates the factorial of a given positive integer. Test that a positive integer is given and test the function 

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Testing the function
num = 5
print(f"The factorial of {num} is: {factorial(num)}")