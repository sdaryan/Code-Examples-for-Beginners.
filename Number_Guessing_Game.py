import random

secret_number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number between 1 and 100: "))
    
    if guess == secret_number:
        print("Congratulations! You guessed the number!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
        
        
        
'''
Explanation:

Start by importing the random module, which will allow you to generate a random number.
Generate a random number between 1 and 100 using the randint() function from the random module, and assign it to a variable.
Create a loop that allows the user to guess the number until they guess correctly. Inside the loop, prompt the user to enter their guess using the input() function, and convert their input to an integer using the int() function.
Add a conditional statement inside the loop that checks whether the user's guess is correct, too high, or too low. If the guess is correct, print a congratulatory message and break out of the loop. If the guess is too high or too low, print a hint message to help the user guess the number correctly.
Run the program and play the number guessing game!
'''