# Define a function to check if the password is strong enough
def password_checker(password):
    # Define the criteria for a strong password
    min_length = 8
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special_char = False
    special_chars = "!@#$%^&*()-_=+[{]}\|;:',<.>/?"
    
    # Check the length of the password
    if len(password) < min_length:
        print("Password is too short!")
        return False
    
    # Check if the password contains an uppercase letter, lowercase letter, digit, and special character
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special_char = True
    
    # Print an error message for each missing criteria
    if not has_uppercase:
        print("Password must contain at least one uppercase letter!")
        return False
    if not has_lowercase:
        print("Password must contain at least one lowercase letter!")
        return False
    if not has_digit:
        print("Password must contain at least one digit!")
        return False
    if not has_special_char:
        print("Password must contain at least one special character!")
        return False
    
    # If all criteria are met, print a success message
    print("Password is strong!")
    return True

# Prompt the user to enter a password and check if it meets the criteria
password = input("Enter a password: ")
password_checker(password)



'''
Explanation:

In this code, we define a function called password_checker() that takes a password as an argument and checks if it meets certain criteria for strength.
We first define the criteria for a strong password – a minimum length of 8 characters, at least one uppercase letter, one lowercase letter, one digit, and one special character.
We then check the length of the password and whether it contains the required types of characters using a for loop that iterates through each character in the password.
If the password fails to meet any of the criteria, we print an error message and return False to indicate that the password is not strong enough. Otherwise, we print a success message and return True.
Finally, we prompt the user to enter a password using the input() function and pass it to the password_checker() function to check if it meets the criteria.
'''