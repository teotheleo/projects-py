import random

# -To Add:
# choose range
# count trys, print a message 
# closer range, print a message
# add a check for user input / should be only numbers

def guess(x):
    random_number = random.randint(1, x)
    user_guess = 0
    while user_guess != random_number :
        user_guess = int(input(f"Try your luck! Guess the number between 1 and {x}: "))
        if user_guess < random_number:
            print("Too low! Guess again!")
        elif user_guess > random_number:
            print("Too high! Guess again!")   
        
    print(f"YAY!! You guessed correctly, answer is: {random_number} !")  

guess(30)
