# Write a function that checks if a given string is a palindrome (reads the same backward as forward). And test the functon 

def is_palindrome(string):
    # Remove any whitespace and convert to lowercase
    string = string.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    if string == string[::-1]:
        return True
    else:
        return False

# Test the function
string = "tacocat"
if is_palindrome(string):
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")