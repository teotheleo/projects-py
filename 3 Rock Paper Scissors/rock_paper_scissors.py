import random

def game():
    user = input("Choose! 'R' for rock, 'P' for paper, 'S' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'

    # r > s, p > r, s > p
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'

def is_win(player, opponent):
    # return true if the player wins

    if (player == 'r' and opponent =='s') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'r'):
        return True

print(game())