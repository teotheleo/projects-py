import random

def computer_guessnum(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = high
        feedback = input(f"Is the number {guess} correct (C), high (H), or low (L)?").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"YAY! Computer guessed correctly your number is {guess}")

computer_guessnum(20)
