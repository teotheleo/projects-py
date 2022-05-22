import random

def computer_guessnum(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f"Is the number {guess} correct (C), high (H), or low (L)?").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"YAY! Computer guessed correctly your number is {guess}")

computer_guessnum(20)
