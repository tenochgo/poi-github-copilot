# Write a function that returns the next palindrome number in the odometer based on a given mileage. And test the function 

def next_palindrome(mileage):
    mileage += 1
    while str(mileage) != str(mileage)[::-1]:
        mileage += 1
    return mileage

# Testing the function
mileage = 12321
next_palindrome_mileage = next_palindrome(mileage)
print(f"The next palindrome mileage after {mileage} is {next_palindrome_mileage}")