import random
from words import words
from lives_visuals import lives_visual_dict
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    #get user input
    while len(word_letters) > 0 and lives > 0:

        #show used letters so far
        print(f'\nYou have {lives} lives left. Letters used: ', ' '.join(used_letters))

        #list current word to guess with dashes on empty letters
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('\nCurrent word: ', ' '.join(word_list))

        user_letter = input("\nLet\'s play Hangman! Choose a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else: 
                lives = lives - 1
                print('\nLetter is not in the word! You loose a life!')

        elif user_letter in used_letters:
            print('\nYou have already guessed that letter! Try again!')

        else:
            print('\nYou have entered an invalid character! Try again!')
    if lives == 0:
        print(f'\nYou died! The word was {word}')
        print(lives_visual_dict[0])
    else:
        print(f'\nYou guessed the word {word} !! Congratulations!')
hangman()